#!/usr/bin/env python3
"""Opponent starter injury flags + same-proTeam crosswalk vs our roster. Dump-only."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DATA, DATA_RECON, week_dir  # noqa: E402

RECON = DATA_RECON


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", type=int, default=1)
    ap.add_argument("--write", action="store_true", default=True)
    ap.add_argument("--no-write", action="store_true")
    args = ap.parse_args()

    rost = json.loads((RECON / "league_rosters.json").read_text())
    ours_doc = json.loads((DATA / "roster.json").read_text())
    our_players = {p["name"]: p for p in ours_doc.get("players", [])}
    # also from league dump team 13
    for t in rost["teams"]:
        if t.get("teamId") == 13:
            for p in t.get("roster", []):
                our_players.setdefault(p["name"], p)

    flags = []
    for t in rost["teams"]:
        if t.get("teamId") == 13:
            continue
        by = {p["name"]: p for p in t.get("roster", [])}
        for slot, name in (t.get("starters") or {}).items():
            if slot in ("DST", "K"):
                continue
            st = (by.get(name) or {}).get("injuryStatus")
            if st and st != "ACTIVE":
                flags.append(
                    {
                        "abbrev": t.get("abbrev"),
                        "waiverRank": t.get("waiverRank"),
                        "slot": slot,
                        "player": name,
                        "status": st,
                    }
                )

    cuffs = []
    for name, p in sorted(our_players.items()):
        pt = p.get("proTeamId")
        if pt is None:
            continue
        mates = []
        for t in rost["teams"]:
            if t.get("teamId") == 13:
                continue
            for q in t.get("roster", []):
                if q.get("proTeamId") == pt and q.get("name") != name:
                    mates.append(
                        {
                            "abbrev": t.get("abbrev"),
                            "waiverRank": t.get("waiverRank"),
                            "player": q.get("name"),
                            "slot": q.get("slot"),
                            "status": q.get("injuryStatus"),
                            "posId": q.get("defaultPositionId"),
                        }
                    )
        if mates:
            cuffs.append(
                {
                    "our_player": name,
                    "our_status": p.get("injuryStatus"),
                    "proTeamId": pt,
                    "mates": mates,
                }
            )

    out = {
        "as_of": rost.get("as_of"),
        "skill_starter_flags": flags,
        "same_proTeam_crosswalk": cuffs,
        "caveat": "ESPN injuryStatus fields only; preseason Q volume can be noise. Not official OUT clears.",
    }
    text = json.dumps(out, indent=2)
    print(text)
    if args.write and not args.no_write:
        path = week_dir(args.week) / "opponent-flags.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        print(f"# wrote {path}", file=__import__("sys").stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
