import pandas as pd,numpy as np
d=pd.read_pickle('players.pkl');d=d[(d.proj>=6)&(d.out==0)&d.imp.notna()].copy()
d['flex']=d.pos.isin(['RB','WR','TE']);d['sw']=d.season*100+d.week
F=['proj','imp','proj_share','home','dome','rest','spread','wind','opp_allow','q','lim','vac_team','vac_grp','vol3','vol_trend','snap3','snap1','resid_std','pts_sd','proj_trend','tgt3']
out=[]
rng=np.random.default_rng(0)
for (sw),x in d.groupby('sw'):
  x=x.reset_index(drop=True);p=x.proj.values
  A,B=np.where((np.abs(p[:,None]-p[None,:])<3)&(p[:,None]>p[None,:]))
  same=(x.pos.values[A]==x.pos.values[B])|(x.flex.values[A]&x.flex.values[B]&(x.pos.values[A]!='QB'))
  A,B=A[same],B[same]
  diffteam=x.team.values[A]!=x.team.values[B];A,B=A[diffteam],B[diffteam]
  r=pd.DataFrame({'sw':sw,'season':x.season.iloc[0],'week':x.week.iloc[0],'pos':x.pos.values[A]+'-'+x.pos.values[B],'gap':p[A]-p[B],'ya':x.act.values[A],'yb':x.act.values[B]})
  for f in F:r['d_'+f]=x[f].values[A]-x[f].values[B]
  r['a_pos']=x.pos.values[A];r['ta']=x.team.values[A];r['tb']=x.team.values[B]
  out.append(r)
Pp=pd.concat(out);Pp=Pp[Pp.ya!=Pp.yb];Pp['y']=(Pp.ya>Pp.yb).astype(int)
Pp.to_pickle('pairs.pkl');print(len(Pp));print(Pp.groupby('season').y.agg(['size','mean']))
print(Pp.groupby(pd.cut(Pp.gap,[0,1.5,3])).y.mean())
