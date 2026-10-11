# Quick ESPN accuracy check: all 12 teams' starters (incl K, D/ST), 2026 wks 1-4. Run in the dir holding r1..r4.json
import json,pandas as pd,numpy as np,itertools
rows=[]
for wk in range(1,5):
  for t in json.load(open(f'r{wk}.json'))['teams']:
    for e in t['roster']['entries']:
      p=e['playerPoolEntry']['player'];pr=ac=None
      for s in p.get('stats',[]):
        if s['scoringPeriodId']==wk and s['statSplitTypeId']==1:
          if s['statSourceId']==1: pr=s['appliedTotal']
          if s['statSourceId']==0: ac=s['appliedTotal']
      rows.append(dict(week=wk,fantasy_team_id=t['id'],espn_player_id=p['id'],name=p['fullName'],default_pos_id=p['defaultPositionId'],slot=e['lineupSlotId'],espn_proj=pr,actual_ppr=ac))
d=pd.DataFrame(rows);d.to_csv('espn_2026_wk1-4_all_rostered.csv.gz',index=False)
s=d[~d.slot.isin([20,21])&d.espn_proj.notna()&d.actual_ppr.notna()]
print('n',len(s),'corr',np.corrcoef(s.espn_proj,s.actual_ppr)[0,1],'MAE',(s.espn_proj-s.actual_ppr).abs().mean())
w=[]
for wk,x in s.groupby('week'):
  for a,b in itertools.combinations(x.to_dict('records'),2):
    if a['espn_proj']==b['espn_proj'] or a['actual_ppr']==b['actual_ppr']:continue
    hi,lo=(a,b) if a['espn_proj']>b['espn_proj'] else (b,a);w.append((hi['espn_proj']-lo['espn_proj'],hi['actual_ppr']>lo['actual_ppr']))
w=pd.DataFrame(w,columns=['g','y']);print(w.groupby(pd.cut(w.g,[0,1.5,3,5,999],right=False)).y.agg(['size','mean']))
