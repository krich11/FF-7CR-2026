import json,pandas as pd,numpy as np,os
P=json.load(open('players.json'));gs={k:v.get('gsis_id') for k,v in P.items() if v.get('gsis_id')}
rows=[]
for s in range(2021,2027):
  for w in range(1,19):
    if not os.path.exists(f'projections-{s}-{w}.json'):continue
    st={r['player_id']:r for r in json.load(open(f'stats-{s}-{w}.json'))}
    if len(st)<200: continue
    for r in json.load(open(f'projections-{s}-{w}.json')):
      pp=r['stats'].get('pts_ppr');pos=r['player']['position'] if r.get('player') else None
      if pp is None or pos not in('QB','RB','WR','TE') or not r.get('team'):continue
      a=st.get(r['player_id']);ast=a['stats'] if a else {}
      rows.append(dict(season=s,week=w,pid=r['player_id'],pos=pos,team=r['team'],opp=r.get('opponent'),proj=pp,
        act=ast.get('pts_ppr',0.0),active=ast.get('gms_active',0)>0 or ast.get('off_snp',0)>0,
        snp=ast.get('off_snp',0),tmsnp=ast.get('tm_off_snp',np.nan),tgt=ast.get('rec_tgt',0),car=ast.get('rush_att',0),
        pyd=ast.get('pass_att',0),rz=ast.get('rec_tgt_rz',0) if 'rec_tgt_rz' in ast else np.nan))
d=pd.DataFrame(rows);d['gsis']=d.pid.map(gs)
d=d.sort_values(['pid','season','week'])
g=d.groupby(['pid','season'])
d['opp_vol']=d.tgt+d.car
d['snapsh']=d.snp/d.tmsnp
def lag(col,n): return g[col].transform(lambda x:x.where(d.loc[x.index,'active']).shift(1).rolling(n,min_periods=1).mean())
d['vol3']=lag('opp_vol',3);d['vol1']=lag('opp_vol',1);d['tgt3']=lag('tgt',3)
d['snap3']=lag('snapsh',3);d['snap1']=lag('snapsh',1)
d['res']=d.act-d.proj
d['resid_std']=g['res'].transform(lambda x:x.where(d.loc[x.index,'active']).shift(1).expanding().mean())
d['pts_sd']=g['act'].transform(lambda x:x.where(d.loc[x.index,'active']).shift(1).expanding(min_periods=2).std())
d['proj_prev']=g['proj'].shift(1);d['proj_trend']=d.proj-d['proj_prev']
d['vol_trend']=d.vol1-d.vol3
# games
G=pd.read_csv('games.csv');G=G[G.game_type=='REG']
t=[]
for _,x in G.iterrows():
  ih=x.total_line/2+x.spread_line/2; ia=x.total_line/2-x.spread_line/2
  dome=1 if x.roof in('dome','closed') else 0
  t.append(dict(season=x.season,week=x.week,team=x.home_team,home=1,imp=ih,spread=x.spread_line,dome=dome,rest=x.home_rest-x.away_rest,wind=x.wind if x.roof=='outdoors' else 0,temp=x.temp))
  t.append(dict(season=x.season,week=x.week,team=x.away_team,home=0,imp=ia,spread=-x.spread_line,dome=dome,rest=x.away_rest-x.home_rest,wind=x.wind if x.roof=='outdoors' else 0,temp=x.temp))
T=pd.DataFrame(t);fix={'LA':'LAR','LV':'LV','OAK':'LV','SD':'LAC','STL':'LAR'}
T['team']=T.team.replace({'LA':'LAR'})
d=d.merge(T,on=['season','week','team'],how='left')
d['proj_share']=d.proj/d.imp
# opponent allowed to position, prior weeks
o=d[d.active].groupby(['season','week','opp','pos']).act.sum().reset_index().sort_values(['opp','pos','season','week'])
o['opp_allow']=o.groupby(['opp','pos','season']).act.transform(lambda x:x.shift(1).expanding().mean())
d=d.merge(o[['season','week','opp','pos','opp_allow']],on=['season','week','opp','pos'],how='left')
# injuries
I=pd.concat([pd.read_csv(f'inj_{s}.csv') for s in range(2021,2027)]);I=I[I.game_type=='REG']
I=I.drop_duplicates(['season','week','gsis_id'],keep='last')
I['q']=I.report_status.isin(['Questionable']).astype(int)
I['out']=I.report_status.isin(['Out','Doubtful']).astype(int)
I['lim']=I.practice_status.fillna('').str.contains('Limited|Did Not').astype(int)
d=d.merge(I[['season','week','gsis_id','q','out','lim']].rename(columns={'gsis_id':'gsis'}),on=['season','week','gsis'],how='left')
for c in['q','out','lim']:d[c]=d[c].fillna(0)
# vacated volume: teammates ruled out pregame, their prior vol3
d['vac']=d.out*d.vol3.fillna(0)
grp=lambda p:'REC' if p in('WR','TE') else p
d['grp']=d.pos.map(grp)
tv=d.groupby(['season','week','team']).vac.sum().rename('vac_team');tg=d.groupby(['season','week','team','grp']).vac.sum().rename('vac_grp')
d=d.join(tv,on=['season','week','team']).join(tg,on=['season','week','team','grp'])
d['vac_team']-=d.vac;d['vac_grp']-=d.vac
d.to_pickle('players.pkl');print(d.shape);print(d.groupby('season').size())
