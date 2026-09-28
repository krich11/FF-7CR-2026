#!/usr/bin/env python3
"""CLI: sync | plan | apply | verify — never prints cookies."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from client import (
    BASE,
    EspnAuth,
    apply_and_verify,
    assignments_to_expected,
    fetch_league,
    normalize_roster,
    plan_moves_to_assignments,
    starters_map,
    sync_roster_json,
    team_roster_entries,
    verify_starters,
)

LEAGUE = "1776545061"
TEAM = 13
SEASON = 2026


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["sync", "plan", "apply", "verify", "starters"])
    ap.add_argument("--week", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.cmd == "sync":
        print(json.dumps(sync_roster_json(LEAGUE, SEASON, TEAM), indent=2))
        return 0

    auth = EspnAuth.load()
    league = fetch_league(auth, LEAGUE, SEASON)
    rows = normalize_roster(team_roster_entries(league, TEAM))
    if args.cmd == "starters":
        print(json.dumps(starters_map(rows), indent=2))
        return 0

    dec_path = BASE / "decisions" / f"week-{args.week}.json"
    decisions = json.loads(dec_path.read_text())
    assignments = decisions["assignments"]
    moves, expected, errors = plan_moves_to_assignments(rows, assignments)
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, indent=2))
        return 2

    if args.cmd == "plan":
        print(json.dumps({"moves": moves, "expected": expected, "current": starters_map(rows)}, indent=2))
        return 0

    if args.cmd == "verify":
        v = verify_starters(auth, LEAGUE, SEASON, TEAM, expected)
        print(json.dumps(v, indent=2))
        return 0 if v["ok"] else 1

    if args.cmd == "apply":
        if args.dry_run:
            print(json.dumps({"dry_run": True, "moves": moves, "expected": expected}, indent=2))
            return 0
        if not moves:
            v = verify_starters(auth, LEAGUE, SEASON, TEAM, expected)
            print(json.dumps({"noop": True, "verify": v, "alert": not v["ok"]}, indent=2))
            return 0 if v["ok"] else 1
        result = apply_and_verify(LEAGUE, SEASON, TEAM, moves, expected)
        print(json.dumps({
            "write_http": result["write_http"],
            "write_ok": result["write_ok"],
            "verify": result["verify"],
            "alert": result["alert"],
            "before": result["before"],
        }, indent=2))
        return 0 if not result["alert"] else 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
