import json,csv,re,collections
T={1:'ATL',2:'BUF',3:'CHI',4:'CIN',5:'CLE',6:'DAL',7:'DEN',8:'DET',9:'GB',10:'TEN',11:'IND',12:'KC',13:'LV',14:'LA',15:'MIA',16:'MIN',17:'NE',18:'NO',19:'NYG',20:'NYJ',21:'PHI',22:'ARI',23:'PIT',24:'LAC',25:'SF',26:'SEA',27:'TB',28:'WAS',29:'CAR',30:'JAX',33:'BAL',34:'HOU'}
POS={1:'QB',2:'RB',3:'WR',4:'TE'}
def nk(n): n=re.sub(r"[.'’]|\b(jr|sr|ii|iii|iv)\b","",n.lower()); return re.sub(r'\s+',' ',n).strip()
rows=[]
for wk in range(1,5):
  d=json.load(open(f'r{wk}.json'))
  for t in d['teams']:
    for e in t['roster']['entries']:
      p=e['playerPoolEntry']['player']; pos=POS.get(p['defaultPositionId'])
      if not pos: continue
      pr=ac=None
      for s in p.get('stats',[]):
        if s['scoringPeriodId']==wk and s['statSourceId']==1 and s['statSplitTypeId']==1: pr=s['appliedTotal']
        if s['scoringPeriodId']==wk and s['statSourceId']==0 and s['statSplitTypeId']==1: ac=s['appliedTotal']
      hist={s['scoringPeriodId']:(s['statSourceId'],s['appliedTotal']) for s in p.get('stats',[])}
      rows.append(dict(wk=wk,team=t['id'],pid=p['id'],name=p['fullName'],pos=pos,nfl=T.get(p['proTeamId']),slot=e['lineupSlotId'],proj=pr,act=ac,elig=p['eligibleSlots']))
# season residual: per player proj/act by week from all weeks files
pa=collections.defaultdict(dict)
for r in rows:
  if r['proj'] is not None and r['act'] is not None: pa[r['pid']][r['wk']]=(r['proj'],r['act'])
# nflverse
snap=collections.defaultdict(dict)
for x in csv.DictReader(open('snaps26.csv')):
  snap[(nk(x['player']),x['team'])][int(x['week'])]=float(x['offense_pct'] or 0)
ps=collections.defaultdict(dict); teamopp=collections.defaultdict(lambda:collections.Counter())
for x in csv.DictReader(open('ps.csv')):
  if x['season_type']!='REG':continue
  w=int(x['week']); o=float(x['targets'] or 0)+float(x['carries'] or 0)
  ps[(nk(x['player_display_name']),x['team'])][w]=dict(opp=o,tgt=float(x['targets'] or 0),car=float(x['carries'] or 0),rz=0)
  teamopp[x['team']][w]+=o
itt={}
for g in csv.DictReader(open('games.csv')):
  if g['season']!='2026' or g['game_type']!='REG':continue
  w=int(g['week']);s=float(g['spread_line'] or 0);tl=float(g['total_line'] or 0)
  itt[(g['home_team'],w)]=(tl/2+s/2,1,g['roof']); itt[(g['away_team'],w)]=(tl/2-s/2,0,g['roof'])
miss=0
for r in rows:
  k=(nk(r['name']),r['nfl']); w=r['wk']
  sn=snap.get(k,{}); pp=ps.get(k,{})
  r['snap1']=sn.get(w-1); r['trend']=(sn[w-1]-sn[w-2]) if (w-1 in sn and w-2 in sn) else None
  pw=[x for x in range(1,w) if x in pp]
  r['oppg']=sum(pp[x]['opp'] for x in pw)/len(pw) if pw else None
  r['oppsh']=sum(pp[x]['opp'] for x in pw)/max(1,sum(teamopp[r['nfl']][x] for x in pw)) if pw else None
  it=itt.get((r['nfl'],w)); r['itt'],r['home'],r['dome']=(it[0],it[1],1 if it[2] in('dome','closed') else 0) if it else (None,None,None)
  prior=[pa[r['pid']][x] for x in range(1,w) if x in pa[r['pid']]]
  r['resid']=sum(a-p for p,a in prior)/len(prior) if prior else None
  r['snapmean']=sum(sn[x] for x in range(1,w) if x in sn)/max(1,len([x for x in range(1,w) if x in sn])) if any(x in sn for x in range(1,w)) else None
  if w>1 and not sn and r['proj'] and r['proj']>3: miss+=1
print(len(rows),'unmatched snaps',miss)
json.dump(rows,open('rows.json','w'))
