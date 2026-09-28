#!/usr/bin/env python3
"""Refresh Recon ESPN dumps (READ-ONLY). Never prints cookies. Never writes to ESPN."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

from repo import repo_root

ROOT = repo_root()
sys.path.insert(0, str(ROOT / "code" / "espn_api"))
from client import (  # type: ignore
    PT,
    EspnAuth,
    READ_BASE,
    fetch_league,
    normalize_roster,
    starters_map,
    _request,
)

RECON = ROOT / "data" / "recon"
SNAP = RECON / "snapshots"
LEAGUE = "1776545061"
SEASON = 2026
US = 13


def now_pt() -> str:
    return datetime.now(PT).isoformat()


def snapshot_existing() -> Path | None:
    paths = [
        RECON / "league_index.json",
        RECON / "league_rosters.json",
        RECON / "transactions_recent.json",
    ]
    if not all(p.exists() for p in paths):
        return None
    stamp = datetime.now(PT).strftime("%Y%m%d-%H%M%S")
    dest = SNAP / stamp
    dest.mkdir(parents=True, exist_ok=True)
    for p in paths:
        shutil.copy2(p, dest / p.name)
    (dest / "meta.json").write_text(
        json.dumps({"snapshotted_at": now_pt(), "files": [p.name for p in paths]}, indent=2)
    )
    return dest


def team_record(t: dict) -> dict:
    r = ((t.get("record") or {}).get("overall")) or {}
    return {
        "wins": int(r.get("wins") or 0),
        "losses": int(r.get("losses") or 0),
        "ties": int(r.get("ties") or 0),
        "pointsFor": float(r.get("pointsFor") or 0.0),
        "pointsAgainst": float(r.get("pointsAgainst") or 0.0),
    }


def build_rosters(league: dict) -> dict:
    teams_out = []
    for t in sorted(league.get("teams", []), key=lambda x: x.get("id") or 0):
        tid = t.get("id")
        entries = (t.get("roster") or {}).get("entries") or []
        rows = normalize_roster(entries)
        teams_out.append(
            {
                "teamId": tid,
                "name": t.get("name") or t.get("location"),
                "abbrev": t.get("abbrev"),
                "playoffSeed": t.get("playoffSeed"),
                "waiverRank": t.get("waiverRank"),
                "record": team_record(t),
                "starters": starters_map(rows),
                "roster": rows,
                "is_quantum_blitz": tid == US,
            }
        )
    return {
        "as_of": now_pt(),
        "leagueId": LEAGUE,
        "seasonId": SEASON,
        "scoringPeriodId": league.get("scoringPeriodId"),
        "source": "espn_api",
        "team_count": len(teams_out),
        "teams": teams_out,
    }


def build_index(rosters: dict) -> dict:
    teams = []
    for t in rosters["teams"]:
        teams.append(
            {
                "teamId": t["teamId"],
                "name": t["name"],
                "abbrev": t["abbrev"],
                "waiverRank": t["waiverRank"],
                "record": t["record"],
                "is_quantum_blitz": t["is_quantum_blitz"],
                "starter_count": len(t.get("starters") or {}),
                "roster_count": len(t.get("roster") or []),
            }
        )
    return {"as_of": rosters["as_of"], "teams": teams}


def fetch_transactions(auth: EspnAuth, limit: int = 250) -> dict:
    url = (
        f"{READ_BASE}/seasons/{SEASON}/segments/0/leagues/{LEAGUE}/transactions"
        f"?limit={limit}"
    )
    status, data = _request("GET", url, auth)
    rows: list = []
    if status == 200:
        if isinstance(data, list):
            rows = data
        elif isinstance(data, dict):
            rows = data.get("transactions") or data.get("items") or []
    if not rows:
        url2 = f"{READ_BASE}/seasons/{SEASON}/segments/0/leagues/{LEAGUE}?view=mTransactions2"
        status2, data2 = _request("GET", url2, auth)
        if status2 == 200 and isinstance(data2, dict):
            rows = data2.get("transactions") or []
        else:
            raise RuntimeError(f"transactions fetch failed HTTP {status}/{status2}")

    out_rows = []
    for x in rows[:limit]:
        items = [{"type": it.get("type"), "playerId": it.get("playerId")} for it in x.get("items") or []]
        tid = x.get("teamId")
        if tid is None:
            members = x.get("members") or []
            if members and isinstance(members[0], dict):
                tid = members[0].get("teamId")
        if tid is None and x.get("primaryTeamId") is not None:
            tid = x.get("primaryTeamId")
        out_rows.append(
            {
                "id": x.get("id"),
                "type": x.get("type"),
                "status": x.get("status"),
                "teamId": tid,
                "scoringPeriodId": x.get("scoringPeriodId"),
                "items": items,
            }
        )
    return {"as_of": now_pt(), "n": len(rows), "note": "fetched via read API", "transactions": out_rows}


def main() -> int:
    ap = argparse.ArgumentParser(description="Refresh recon dumps (ESPN read-only)")
    ap.add_argument("--tx-limit", type=int, default=250)
    ap.add_argument("--skip-tx", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    auth = EspnAuth.load()
    snap = None if args.dry_run else snapshot_existing()
    league = fetch_league(auth, LEAGUE, SEASON, views=["mRoster", "mTeam", "mSettings"])
    rosters = build_rosters(league)
    index = build_index(rosters)
    tx = None if args.skip_tx else fetch_transactions(auth, limit=args.tx_limit)

    if args.dry_run:
        print(json.dumps({
            "dry_run": True,
            "team_count": rosters["team_count"],
            "scoringPeriodId": rosters["scoringPeriodId"],
            "tx_n": None if tx is None else tx["n"],
        }, indent=2))
        return 0

    RECON.mkdir(parents=True, exist_ok=True)
    (RECON / "league_rosters.json").write_text(json.dumps(rosters, indent=2))
    (RECON / "league_index.json").write_text(json.dumps(index, indent=2))
    if tx is not None:
        (RECON / "transactions_recent.json").write_text(json.dumps(tx, indent=2))
    meta = {
        "refreshed_at": now_pt(),
        "snapshot": str(snap) if snap else None,
        "scoringPeriodId": rosters["scoringPeriodId"],
        "team_count": rosters["team_count"],
        "tx_n": None if tx is None else tx["n"],
    }
    (RECON / "last_refresh.json").write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
