#!/usr/bin/env python3
"""ESPN Fantasy Football API client for Quantum Blitz.

Read: lm-api-reads
Write: lm-api-writes /transactions/ (LINEUP moves)
Auth: box-local cookies from browser session (secrets/espn_cookies.json)
Never print cookie values.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

BASE = Path("/workspace/fantasy/quantum-blitz")
SECRETS = BASE / "secrets" / "espn_cookies.json"
AUDIT = BASE / "audit.log"
PT = ZoneInfo("America/Los_Angeles")

SLOT_NAME = {
    0: "QB",
    2: "RB",
    4: "WR",
    6: "TE",
    16: "DST",
    17: "K",
    20: "BE",
    21: "IR",
    23: "FLEX",
}
NAME_SLOT = {v: k for k, v in SLOT_NAME.items()}
START_SLOTS = {0, 2, 4, 6, 16, 17, 23}

READ_BASE = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl"
WRITE_BASE = "https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl"


@dataclass
class EspnAuth:
    swid: str
    espn_s2: str

    @classmethod
    def load(cls, path: Path = SECRETS) -> "EspnAuth":
        raw = json.loads(path.read_text())
        return cls(swid=raw["SWID"]["value"], espn_s2=raw["espn_s2"]["value"])

    def cookie_header(self) -> str:
        return f"SWID={self.swid}; espn_s2={self.espn_s2}"


def _request(
    method: str,
    url: str,
    auth: EspnAuth,
    body: dict | None = None,
    timeout: int = 30,
) -> tuple[int, Any]:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) QuantumBlitz/1.0",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Cookie": auth.cookie_header(),
            "X-Fantasy-Source": "kona",
            "X-Fantasy-Platform": "kona-l5.t.1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode() or "{}"
            return resp.status, json.loads(raw)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode(errors="replace")
        try:
            parsed = json.loads(err_body)
        except Exception:
            parsed = {"raw": err_body[:2000]}
        return e.code, parsed


def fetch_league(
    auth: EspnAuth,
    league_id: str,
    season_id: int,
    views: list[str] | None = None,
) -> dict:
    views = views or ["mRoster", "mTeam", "mSettings"]
    qs = "&".join(f"view={urllib.parse.quote(v)}" for v in views)
    url = f"{READ_BASE}/seasons/{season_id}/segments/0/leagues/{league_id}?{qs}"
    status, data = _request("GET", url, auth)
    if status != 200:
        raise RuntimeError(f"ESPN read failed HTTP {status}: {data}")
    return data


def team_roster_entries(league: dict, team_id: int) -> list[dict]:
    team = next((t for t in league.get("teams", []) if t.get("id") == team_id), None)
    if not team:
        raise RuntimeError(f"team_id {team_id} not in league payload")
    return (team.get("roster") or {}).get("entries") or []


def normalize_roster(entries: list[dict]) -> list[dict]:
    rows = []
    for e in entries:
        p = ((e.get("playerPoolEntry") or {}).get("player") or {})
        slot_id = e.get("lineupSlotId")
        rows.append(
            {
                "playerId": e.get("playerId"),
                "name": p.get("fullName") or p.get("name") or f"id:{e.get('playerId')}",
                "lineupSlotId": slot_id,
                "slot": SLOT_NAME.get(slot_id, str(slot_id)),
                "injuryStatus": p.get("injuryStatus"),
                "defaultPositionId": p.get("defaultPositionId"),
                "proTeamId": p.get("proTeamId"),
            }
        )
    rows.sort(key=lambda r: (0 if r["lineupSlotId"] in START_SLOTS else 1, r["lineupSlotId"] or 99, r["name"]))
    return rows


def starters_map(rows: list[dict]) -> dict[str, str]:
    """slot_label -> player name for starting slots (RB/WR may duplicate keys with index)."""
    out: dict[str, str] = {}
    rb_i = wr_i = 0
    for r in rows:
        if r["lineupSlotId"] not in START_SLOTS:
            continue
        slot = r["slot"]
        if slot == "RB":
            rb_i += 1
            out[f"RB{rb_i}"] = r["name"]
        elif slot == "WR":
            wr_i += 1
            out[f"WR{wr_i}"] = r["name"]
        else:
            out[slot] = r["name"]
    return out


def write_lineup_moves(
    auth: EspnAuth,
    league_id: str,
    season_id: int,
    team_id: int,
    scoring_period_id: int,
    moves: list[dict],
) -> tuple[int, Any]:
    """moves: [{playerId, fromLineupSlotId, toLineupSlotId}, ...]"""
    items = [
        {
            "playerId": m["playerId"],
            "type": "LINEUP",
            "fromLineupSlotId": m["fromLineupSlotId"],
            "toLineupSlotId": m["toLineupSlotId"],
        }
        for m in moves
    ]
    payload = {
        "isLeagueManager": False,
        "teamId": team_id,
        "type": "ROSTER",
        "memberId": auth.swid,
        "scoringPeriodId": scoring_period_id,
        "executionType": "EXECUTE",
        "items": items,
    }
    url = f"{WRITE_BASE}/seasons/{season_id}/segments/0/leagues/{league_id}/transactions/"
    return _request("POST", url, auth, body=payload)


def verify_starters(
    auth: EspnAuth,
    league_id: str,
    season_id: int,
    team_id: int,
    expected: dict[str, str],
) -> dict:
    """expected: e.g. {QB: Dart, RB1: Achane, ..., FLEX: Goedert}. Returns ok + mismatches."""
    league = fetch_league(auth, league_id, season_id)
    rows = normalize_roster(team_roster_entries(league, team_id))
    actual = starters_map(rows)
    mismatches = []
    for slot, name in expected.items():
        got = actual.get(slot)
        if got != name:
            mismatches.append({"slot": slot, "expected": name, "actual": got})
    return {
        "ok": len(mismatches) == 0,
        "expected": expected,
        "actual": actual,
        "mismatches": mismatches,
        "scoringPeriodId": league.get("scoringPeriodId"),
        "as_of": datetime.now(PT).isoformat(),
    }


def audit(line: str) -> None:
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT.open("a") as f:
        f.write(f"{datetime.now(PT).isoformat()}\t{line}\n")


def apply_and_verify(
    league_id: str,
    season_id: int,
    team_id: int,
    moves: list[dict],
    expected_starters: dict[str, str],
    scoring_period_id: int | None = None,
) -> dict:
    """Write lineup moves then re-read API. On verify fail, sets alert=True for Ken ping."""
    auth = EspnAuth.load()
    league = fetch_league(auth, league_id, season_id)
    sp = scoring_period_id or int(league.get("scoringPeriodId") or 1)
    before = starters_map(normalize_roster(team_roster_entries(league, team_id)))
    status, write_resp = write_lineup_moves(auth, league_id, season_id, team_id, sp, moves)
    verify = verify_starters(auth, league_id, season_id, team_id, expected_starters)
    result = {
        "write_http": status,
        "write_ok": 200 <= status < 300,
        "write_response": write_resp if isinstance(write_resp, dict) else {"raw": str(write_resp)[:500]},
        "before": before,
        "verify": verify,
        "alert": (not verify["ok"]) or not (200 <= status < 300),
        "scoringPeriodId": sp,
    }
    if result["alert"]:
        audit(
            f"ESPN_API_VERIFY_FAIL write_http={status} mismatches={verify.get('mismatches')}"
        )
    else:
        audit(f"ESPN_API_APPLY_OK sp={sp} moves={len(moves)} verify=ok")
    return result


def assignments_to_expected(assignments: dict) -> dict[str, str]:
    """Map decisions.json assignments → starters_map keys (RB1/RB2/WR1/WR2)."""
    out: dict[str, str] = {}
    out["QB"] = assignments["QB"]
    rbs = assignments["RB"] if isinstance(assignments["RB"], list) else [assignments["RB"]]
    wrs = assignments["WR"] if isinstance(assignments["WR"], list) else [assignments["WR"]]
    for i, n in enumerate(rbs, 1):
        out[f"RB{i}"] = n
    for i, n in enumerate(wrs, 1):
        out[f"WR{i}"] = n
    out["TE"] = assignments["TE"]
    out["FLEX"] = assignments["FLEX"]
    dst = (assignments.get("DST") or "").strip()
    if dst and "D/ST" not in dst:
        dst = f"{dst} D/ST"
    out["DST"] = dst
    out["K"] = assignments["K"]
    return out


def _name_key(n: str) -> str:
    return (n or "").lower().replace(".", "").replace("'", "").replace(" jr", "").replace(" sr", "").strip()


def find_player(rows: list[dict], name: str) -> dict | None:
    nk = _name_key(name)
    for r in rows:
        if _name_key(r["name"]) == nk:
            return r
    # DST fuzzy: "Steelers" vs "Steelers D/ST"
    for r in rows:
        if nk in _name_key(r["name"]) or _name_key(r["name"]) in nk:
            if "d/st" in _name_key(r["name"]) or "d/st" in nk:
                return r
    return None


def plan_moves_to_assignments(
    rows: list[dict],
    assignments: dict,
    unlocked_slots: set[str] | None = None,
) -> tuple[list[dict], dict[str, str], list[str]]:
    """Compute LINEUP moves so starters match assignments.

    unlocked_slots: slot labels like QB, RB1, FLEX — if set, only those may change.
    Returns (moves, expected_starters, errors).
    """
    expected = assignments_to_expected(assignments)
    # Fix DST name against roster
    for r in rows:
        if r["slot"] in ("DST",) or r["lineupSlotId"] == 16:
            # match expected DST loosely
            if _name_key(expected["DST"]).replace(" d/st", "") in _name_key(r["name"]) or _name_key(r["name"]).replace(" d/st", "") in _name_key(expected["DST"]):
                expected["DST"] = r["name"]
                break

    current = starters_map(rows)
    errors: list[str] = []
    # Build desired: slot_key -> player name
    desired = dict(expected)
    if unlocked_slots is not None:
        for k in list(desired.keys()):
            if k not in unlocked_slots and current.get(k) != desired.get(k):
                # keep current for locked slots
                desired[k] = current.get(k) or desired[k]

    # If already matches, no moves
    if all(current.get(k) == desired.get(k) for k in desired):
        return [], desired, errors

    # Map name -> row
    by_name = {_name_key(r["name"]): r for r in rows}

    # Slot key -> lineupSlotId (for multi RB/WR use first free of that type — we move by player)
    # Strategy: for each mismatched start slot, move desired player into that slot id,
    # and move displaced starter to BE (20).
    # Collect target slot ids for each key.
    slot_ids_for_key = {
        "QB": 0, "TE": 6, "FLEX": 23, "DST": 16, "K": 17,
        "RB1": 2, "RB2": 2, "WR1": 4, "WR2": 4,
    }

    # Who currently occupies each start slot instance
    # For duplicate slot ids (2 RB), track by order in starters_map
    occupied: dict[str, dict] = {}
    for r in rows:
        if r["lineupSlotId"] not in START_SLOTS:
            continue
        # assign key
        sm = starters_map([r] + [x for x in rows if x is not r])  # unused
    # rebuild occupied from starters_map + rows
    for key, name in current.items():
        p = find_player(rows, name)
        if p:
            occupied[key] = p

    moves: list[dict] = []
    # First: everyone who should leave a start slot but isn't the desired occupant → to BE
    # Better algorithm used by fantasy tools: simultaneous swap list.

    # Desired occupants
    want_player_for_key = {}
    for key, name in desired.items():
        p = find_player(rows, name)
        if not p:
            errors.append(f"Player not on roster: {name} for {key}")
            continue
        want_player_for_key[key] = p

    if errors:
        return [], desired, errors

    # Build moves: for each key where current != desired, move desired into slot,
    # and if current occupant isn't needed in another start we're filling, send to BE.
    # Use a staging approach: (1) move all mismatched starters to BE, (2) move desired into slots.
    # But two RBs share slotId 2 — ESPN uses two entries both with lineupSlotId=2.
    # from/to must use the player's current lineupSlotId.

    # Phase 1: anyone in a start slot who shouldn't be there → BE
    desired_names = {_name_key(n) for n in desired.values()}
    for key, p in occupied.items():
        if unlocked_slots is not None and key not in unlocked_slots:
            continue
        if _name_key(p["name"]) not in desired_names or desired.get(key) != p["name"]:
            # if they're desired for another key, leave for now
            if any(desired.get(k) == p["name"] for k in desired):
                continue
            if p["lineupSlotId"] != 20:
                moves.append({
                    "playerId": p["playerId"],
                    "fromLineupSlotId": p["lineupSlotId"],
                    "toLineupSlotId": 20,
                })

    # Refresh conceptual positions after phase1 in the move list only — ESPN executes as batch.
    # Phase 2: place desired players into their slots
    for key, p in want_player_for_key.items():
        if unlocked_slots is not None and key not in unlocked_slots:
            continue
        if current.get(key) == p["name"]:
            continue
        target_slot = slot_ids_for_key[key]
        # from: if we already queued a move to BE for this player, from is still current
        from_slot = p["lineupSlotId"]
        # if player is currently in another start slot that we're also filling, from is that slot
        if from_slot == target_slot and current.get(key) == p["name"]:
            continue
        moves.append({
            "playerId": p["playerId"],
            "fromLineupSlotId": from_slot,
            "toLineupSlotId": target_slot,
        })

    # Deduplicate by playerId keeping last
    by_pid: dict[int, dict] = {}
    for m in moves:
        by_pid[m["playerId"]] = m
    moves = list(by_pid.values())
    # Drop no-ops
    moves = [m for m in moves if m["fromLineupSlotId"] != m["toLineupSlotId"]]
    return moves, desired, errors


def sync_roster_json(
    league_id: str,
    season_id: int,
    team_id: int,
    out_path: Path | None = None,
) -> dict:
    """Write roster.json from API. Returns summary."""
    auth = EspnAuth.load()
    league = fetch_league(auth, league_id, season_id)
    rows = normalize_roster(team_roster_entries(league, team_id))
    players = []
    for r in rows:
        players.append({
            "name": r["name"],
            "pos": {1: "QB", 2: "RB", 3: "WR", 4: "TE", 5: "K", 16: "DST"}.get(
                r.get("defaultPositionId"), r["slot"] if r["slot"] != "BE" else "?"
            ),
            "espn_id": r["playerId"],
            "espn_slot": r["slot"],
            "lineupSlotId": r["lineupSlotId"],
            "status_tag": None if r.get("injuryStatus") in (None, "ACTIVE") else r.get("injuryStatus"),
            "eligible_slots": [],
        })
    payload = {
        "as_of": datetime.now(PT).isoformat(),
        "week": league.get("scoringPeriodId"),
        "source": "espn_api",
        "league_id": league_id,
        "team_id": team_id,
        "season_id": season_id,
        "scoringPeriodId": league.get("scoringPeriodId"),
        "starters": starters_map(rows),
        "players": players,
    }
    path = out_path or (BASE / "roster.json")
    path.write_text(json.dumps(payload, indent=2) + "\n")
    audit(f"ESPN_API_SYNC n={len(players)} starters={payload['starters']}")
    return {"n": len(players), "starters": payload["starters"], "path": str(path)}
