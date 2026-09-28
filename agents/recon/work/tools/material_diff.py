#!/usr/bin/env python3
"""Diff current transactions dump vs a snapshot — flag material FA/waiver/trade competition."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DATA_RECON, SNAP, rel, week_dir  # noqa: E402

RECON = DATA_RECON
US = 13
MATERIAL_TYPES = {"WAIVER", "FREEAGENT", "FA", "TRADE"}


def load_tx(path: Path) -> dict:
    return json.loads(path.read_text())


def ids(tx: dict) -> set[str]:
    return {str(x.get("id")) for x in tx.get("transactions", []) if x.get("id")}


def is_material(x: dict) -> bool:
    return x.get("type") in MATERIAL_TYPES


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--against", type=str, default="")
    ap.add_argument("--week", type=int, default=1)
    ap.add_argument("--include-pending", action="store_true")
    ap.add_argument("--write", action="store_true", default=True)
    ap.add_argument("--no-write", action="store_true")
    args = ap.parse_args()

    cur = load_tx(RECON / "transactions_recent.json")
    against = Path(args.against) if args.against else None
    if against is None:
        snaps = []
        if SNAP.exists():
            snaps = sorted(
                (s for s in SNAP.iterdir() if (s / "transactions_recent.json").exists()),
                reverse=True,
            )
        if not snaps:
            print(json.dumps({"ok": False, "error": "no snapshot to diff against", "competition": []}, indent=2))
            return 1
        against = snaps[0] / "transactions_recent.json"
    elif against.is_dir():
        against = against / "transactions_recent.json"

    prev = load_tx(against)
    prev_ids = ids(prev)
    new_rows = [x for x in cur.get("transactions", []) if str(x.get("id")) not in prev_ids]
    material = [x for x in new_rows if is_material(x)]
    if not args.include_pending:
        material = [x for x in material if (x.get("status") or "EXECUTED") == "EXECUTED"]

    rost = json.loads((RECON / "league_rosters.json").read_text())
    pid = {}
    tmap = {}
    for t in rost.get("teams", []):
        tmap[t["teamId"]] = t.get("abbrev")
        for p in t.get("roster", []):
            pid[p["playerId"]] = p.get("name")

    def enrich(x: dict) -> dict:
        items = []
        for it in x.get("items") or []:
            items.append(
                {
                    "type": it.get("type"),
                    "playerId": it.get("playerId"),
                    "player": pid.get(it.get("playerId")) or f"id:{it.get('playerId')}",
                }
            )
        return {
            "id": x.get("id"),
            "type": x.get("type"),
            "status": x.get("status"),
            "teamId": x.get("teamId"),
            "abbrev": tmap.get(x.get("teamId")),
            "scoringPeriodId": x.get("scoringPeriodId"),
            "items": items,
            "is_us": x.get("teamId") == US,
        }

    enriched = [enrich(x) for x in material]
    competition = [x for x in enriched if not x["is_us"]]
    ours = [x for x in enriched if x["is_us"]]

    out = {
        "against": rel(against),
        "as_of_current": cur.get("as_of"),
        "as_of_prev": prev.get("as_of"),
        "new_tx_count": len(new_rows),
        "competition_count": len(competition),
        "our_count": len(ours),
        "competition": competition,
        "ours_observed": ours,
        "ping_blitz": len(competition) > 0,
        "note": "Competition = other teams WAIVER/FA/TRADE. Our rows listed for awareness only — Blitz owns claim board.",
    }
    text = json.dumps(out, indent=2)
    print(text)
    if args.write and not args.no_write:
        path = week_dir(args.week) / "material-diff.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
