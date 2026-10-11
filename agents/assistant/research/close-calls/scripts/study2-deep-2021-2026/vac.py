import pandas as pd,numpy as np
d=pd.read_pickle('players.pkl')
I=pd.concat([pd.read_csv(f'inj_{s}.csv') for s in range(2021,2027)]);I=I[(I.game_type=='REG')]
I=I.drop_duplicates(['season','week','gsis_id'],keep='last')
o=I[I.report_status.isin(['Out','Doubtful'])][['season','week','gsis_id','team']].rename(columns={'gsis_id':'gsis'})
a=d[d.active&d.gsis.notna()][['gsis','season','week','opp_vol','pos','team']]
# prior-3-active-games volume per player as of each week
m=o.merge(a,on=['gsis','season'],suffixes=('','_p'))
m=m[m.week_p<m.week].sort_values('week_p').groupby(['season','week','gsis']).tail(3)
v=m.groupby(['season','week','gsis','team_p','pos']).opp_vol.mean().reset_index().rename(columns={'team_p':'team','opp_vol':'vac'})
v['grp']=v.pos.map(lambda p:'REC' if p in('WR','TE') else p)
d=d.drop(columns=['vac','vac_team','vac_grp'])
d=d.join(v.groupby(['season','week','team']).vac.sum().rename('vac_team'),on=['season','week','team']).join(v.groupby(['season','week','team','grp']).vac.sum().rename('vac_grp'),on=['season','week','team','grp'])
d[['vac_team','vac_grp']]=d[['vac_team','vac_grp']].fillna(0)
print((d.vac_team>0).mean(),d[d.proj>=6].q.mean(), d[d.proj>=6].gsis.notna().mean())
d.to_pickle('players.pkl')
