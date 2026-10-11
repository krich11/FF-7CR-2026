# Pull ESPN mRoster (lineup slot, weekly projection, actual) for League 1776545061, 2026 weeks 1-5.
# Private league: needs your own ESPN cookies. Set ESPN_S2 and SWID in the environment (never commit them).
import os,json,requests
h={'Cookie':f"espn_s2={os.environ['ESPN_S2']}; SWID={os.environ['SWID']}"}
B='https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2026/segments/0/leagues/1776545061'
for wk in range(1,6):
    r=requests.get(B,params={'view':'mRoster','scoringPeriodId':wk},headers=h,timeout=60)
    print(wk,r.status_code); json.dump(r.json(),open(f'r{wk}.json','w'))
