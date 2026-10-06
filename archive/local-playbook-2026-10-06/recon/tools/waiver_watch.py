#!/usr/bin/env python3
"""WAIVER WATCH scanner over recon dumps. Read-only. Never prints cookies."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

BASE = Path("/workspace/fantasy/quantum-blitz")
RECON = BASE / "recon"


def load() -> tuple[dict, dict, dict]:
    idx = json.loads((RECON / "league_index.json").read_text())
    rost = json.loads((RECON / "league_rosters.json").read_text())
    tx = json.loads((RECON / "transactions_recent.json").read_text())
    return idx, rost, tx


def pid_index(rost: dict) -> dict[int, dict]:
    out: dict[int, dict] = {}
    for t in rost.get("teams", []):
        for p in t.get("roster", []):
            out[p["playerId"]] = {
                "name": p.get("name"),
                "teamId": t["teamId"],
                "abbrev": t.get("abbrev"),
                "team": t.get("name"),
                "slot": p.get("slot"),
                "status": p.get("injuryStatus"),
            }
    return out


def team_map(idx: dict) -> dict[int, dict]:
    return {t["teamId"]: t for t in idx.get("teams", [])}


def non_draft_moves(tx: dict, pids: dict, teams: dict) -> list[dict]:
    rows = []
    for x in tx.get("transactions", []):
        if x.get("type") == "DRAFT":
            continue
        items = []
        for it in x.get("items", []):
            pid = it.get("playerId")
            meta = pids.get(pid, {})
            items.append(
                {
                    "itemType": it.get("type"),
                    "playerId": pid,
                    "player": meta.get("name") or (f"FA/unknown:{pid}" if pid is not None else None),
                    "onRosterOf": meta.get("abbrev"),
                }
            )
        tid = x.get("teamId")
        t = teams.get(tid, {})
        rows.append(
            {
                "type": x.get("type"),
                "status": x.get("status"),
                "teamId": tid,
                "abbrev": t.get("abbrev"),
                "team": t.get("name"),
                "waiverRank": t.get("waiverRank"),
                "scoringPeriodId": x.get("scoringPeriodId"),
                "items": items,
            }
        )
    return rows


def summary(idx: dict, rost: dict, tx: dict) -> dict:
    teams = team_map(idx)
    pids = pid_index(rost)
    moves = non_draft_moves(tx, pids, teams)
    types = Counter(m["type"] for m in moves)
    order = sorted(teams.values(), key=lambda t: t.get("waiverRank") or 99)
    adds = [m for m in moves if m["type"] in ("WAIVER", "FREEAGENT", "FA") or any(i.get("itemType") == "ADD" for i in m["items"])]
    drops_creating_fa = []
    for m in moves:
        for it in m["items"]:
            if it.get("itemType") == "DROP" and it["playerId"] not in pids:
                drops_creating_fa.append(it)
    return {
        "as_of_index": idx.get("as_of"),
        "as_of_rosters": rost.get("as_of"),
        "as_of_tx": tx.get("as_of"),
        "tx_file_n": tx.get("n"),
        "tx_rows": len(tx.get("transactions", [])),
        "non_draft_type_counts": dict(types),
        "waiver_order": [
            {
                "rank": t.get("waiverRank"),
                "abbrev": t.get("abbrev"),
                "name": t.get("name"),
                "teamId": t.get("teamId"),
                "is_us": bool(t.get("is_quantum_blitz") or t.get("teamId") == 13),
            }
            for t in order
        ],
        "competition_moves": moves,
        "add_like_moves": adds,
        "drops_now_fa": drops_creating_fa,
    }


def render_md(s: dict, week: int) -> str:
    lines = [
        f"# WAIVER WATCH — Week {week:02d}",
        f"**dumps as_of:** index `{s['as_of_index']}` · rosters `{s['as_of_rosters']}` · tx `{s['as_of_tx']}`",
        f"**tx coverage:** {s['tx_rows']} rows in file (reported n={s['tx_file_n']})",
        "",
        "## Order map",
        "| Rank | Abbr | Team |",
        "|-----:|------|------|",
    ]
    for t in s["waiver_order"]:
        mark = " *(us)*" if t["is_us"] else ""
        lines.append(f"| {t['rank']} | {t['abbrev']} | {t['name']}{mark} |")
    lines += ["", "## Non-draft activity", f"Type counts: `{s['non_draft_type_counts']}`", ""]
    if not s["competition_moves"]:
        lines.append("_No non-DRAFT transactions in dump._")
    else:
        lines += ["| Type | Team | WR# | Items |", "|------|------|----:|-------|"]
        for m in s["competition_moves"]:
            items = "; ".join(
                f"{i.get('itemType')} {i.get('player')}" for i in m["items"]
            )
            lines.append(
                f"| {m['type']} | {m.get('abbrev') or m.get('teamId')} | {m.get('waiverRank') or ''} | {items} |"
            )
    lines += ["", "## Drops now FA (not on any roster)", ""]
    if not s["drops_now_fa"]:
        lines.append("_None in dump._")
    else:
        for d in s["drops_now_fa"]:
            lines.append(f"- `{d.get('playerId')}` {d.get('player')}")
    lines += [
        "",
        "## Lane note",
        "Competition intel only — no Quantum Blitz claim recommendations.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="WAIVER WATCH from recon dumps")
    ap.add_argument("--week", type=int, default=1)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--write", action="store_true", default=True)
    ap.add_argument("--no-write", action="store_true")
    args = ap.parse_args()
    idx, rost, tx = load()
    s = summary(idx, rost, tx)
    if args.json:
        print(json.dumps(s, indent=2))
    else:
        md = render_md(s, args.week)
        print(md)
        if args.write and not args.no_write:
            out = RECON / "weekly" / f"w{args.week:02d}" / "waiver-watch.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md)
            # also machine snapshot
            (out.with_suffix(".json")).write_text(json.dumps(s, indent=2))
            print(f"\n# wrote {out}", file=__import__("sys").stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
