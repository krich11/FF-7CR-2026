#!/usr/bin/env python3
"""READ-ONLY: pull FA/WAIVERS player pool, raw tx, pro schedule. Never prints cookies. GET only."""
import json, sys, urllib.request
from pathlib import Path
sys.path.insert(0, "/workspace/fantasy/quantum-blitz/espn_api")
from client import EspnAuth, READ_BASE  # type: ignore
OUT = Path("/workspace/fantasy/quantum-blitz/recon/weekly/w03/raw")
L = f"{READ_BASE}/seasons/2026/segments/0/leagues/1776545061"
auth = EspnAuth.load()
def get(url, filt=None):
    h = {"User-Agent": "Mozilla/5.0", "Accept": "application/json", "Cookie": auth.cookie_header(),
         "X-Fantasy-Source": "kona", "X-Fantasy-Platform": "kona-l5.t.1"}
    if filt: h["X-Fantasy-Filter"] = json.dumps(filt)
    with urllib.request.urlopen(urllib.request.Request(url, headers=h, method="GET"), timeout=60) as r:
        return json.loads(r.read().decode())
filt = {"players": {"filterStatus": {"value": ["FREEAGENT", "WAIVERS"]},
        "limit": 600, "sortPercOwned": {"sortPriority": 1, "sortAsc": False},
        "filterSlotIds": {"value": [0,2,4,6,16,17,23]}}}
d = get(f"{L}?scoringPeriodId=3&view=kona_player_info", filt)
(OUT / "fa_pool.json").write_text(json.dumps(d))
tx = get(f"{L}?scoringPeriodId=3&view=mTransactions2")
(OUT / "tx_raw_sp3.json").write_text(json.dumps(tx))
tx2 = get(f"{L}?scoringPeriodId=2&view=mTransactions2")
(OUT / "tx_raw_sp2.json").write_text(json.dumps(tx2))
sch = get(f"{READ_BASE}/seasons/2026?view=proTeamSchedules_wl")
(OUT / "pro_sched.json").write_text(json.dumps(sch))
st = get(f"{L}?view=mSettings&view=mStatus&view=mTeam")
(OUT / "settings.json").write_text(json.dumps(st))
print(len(d.get("players", [])), len(tx.get("transactions", [])), len(tx2.get("transactions", [])))
