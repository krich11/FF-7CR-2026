#!/usr/bin/env python3
"""READ-ONLY: pull FA/WAIVERS player pool, raw tx, pro schedule. Never prints cookies. GET only.

Raw captures go to a LOCAL-only dir ($RECON_RAW_DIR/wNN/, default
/workspace/fantasy/quantum-blitz/recon/raw/wNN/). Never written inside the repo.
"""
import argparse
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _paths import DATA_RECON, raw_dir, use_espn_client  # noqa: E402

use_espn_client()
from client import EspnAuth, READ_BASE  # type: ignore  # noqa: E402

LEAGUE = "1776545061"
SEASON = 2026
L = f"{READ_BASE}/seasons/{SEASON}/segments/0/leagues/{LEAGUE}"


def current_sp() -> int:
    try:
        return int(json.loads((DATA_RECON / "last_refresh.json").read_text())["scoringPeriodId"])
    except Exception:
        return 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sp", type=int, default=None, help="scoring period (default: data/recon/last_refresh.json)")
    ap.add_argument("--week", type=int, default=None, help="raw dir week (default: --sp)")
    args = ap.parse_args()
    sp = args.sp or current_sp()
    out = raw_dir(args.week or sp)
    out.mkdir(parents=True, exist_ok=True)
    auth = EspnAuth.load()

    def get(url, filt=None):
        h = {"User-Agent": "Mozilla/5.0", "Accept": "application/json", "Cookie": auth.cookie_header(),
             "X-Fantasy-Source": "kona", "X-Fantasy-Platform": "kona-l5.t.1"}
        if filt:
            h["X-Fantasy-Filter"] = json.dumps(filt)
        with urllib.request.urlopen(urllib.request.Request(url, headers=h, method="GET"), timeout=60) as r:
            return json.loads(r.read().decode())

    filt = {"players": {"filterStatus": {"value": ["FREEAGENT", "WAIVERS"]},
            "limit": 600, "sortPercOwned": {"sortPriority": 1, "sortAsc": False},
            "filterSlotIds": {"value": [0, 2, 4, 6, 16, 17, 23]}}}
    d = get(f"{L}?scoringPeriodId={sp}&view=kona_player_info", filt)
    (out / "fa_pool.json").write_text(json.dumps(d))
    counts = [len(d.get("players", []))]
    for p in (sp, sp - 1):
        if p < 0:
            continue
        tx = get(f"{L}?scoringPeriodId={p}&view=mTransactions2")
        (out / f"tx_raw_sp{p}.json").write_text(json.dumps(tx))
        counts.append(len(tx.get("transactions", [])))
    sch = get(f"{READ_BASE}/seasons/{SEASON}?view=proTeamSchedules_wl")
    (out / "pro_sched.json").write_text(json.dumps(sch))
    st = get(f"{L}?view=mSettings&view=mStatus&view=mTeam")
    (out / "settings.json").write_text(json.dumps(st))
    print(*counts, f"-> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
