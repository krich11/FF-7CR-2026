import json,itertools,random,math
R=[r for r in json.load(open('rows.json')) if r['proj'] is not None and r['act'] is not None and r['slot']!=21]
SLOT={0:'QB',2:'RB',4:'WR',6:'TE',23:'FLEX'}
def ok(a,b):
  if a['pos']=='QB' or b['pos']=='QB': return a['pos']==b['pos']
  return True  # RB/WR/TE flex-eligible
print('== QBZ back-trace')
for w in range(1,5):
  q=[r for r in R if r['team']==13 and r['wk']==w]
  for s in q:
    if s['slot'] not in SLOT: continue
    for b in q:
      if b['slot']!=20: continue
      if SLOT[s['slot']]=='FLEX':
        if b['pos']=='QB':continue
      elif b['pos']!=SLOT[s['slot']]: continue
      if s['proj']-b['proj']<3:
        print(w,SLOT[s['slot']],f"{s['name']} {s['proj']:.1f}/{s['act']:.1f}  vs bench {b['name']} {b['proj']:.1f}/{b['act']:.1f}  lost {max(0,b['act']-s['act']):.1f}  snap1 {s['snap1']}/{b['snap1']} oppsh {s['oppsh'] and round(s['oppsh'],3)}/{b['oppsh'] and round(b['oppsh'],3)}")
def pairs(scope,G=3):
  out=[]
  for w in range(2,5):
    W=[r for r in R if r['wk']==w and r['proj']>=4]
    for a,b in itertools.combinations(W,2):
      if scope=='team' and a['team']!=b['team']:continue
      if not ok(a,b) or abs(a['proj']-b['proj'])>=G or a['act']==b['act']:continue
      out.append((a,b))
  return out
sig={'proj_higher':lambda r:r['proj'],'snap_last':lambda r:r['snap1'],'snap_mean':lambda r:r['snapmean'],'snap_trend':lambda r:r['trend'],
 'opp_per_game':lambda r:r['oppg'],'opp_share':lambda r:r['oppsh'],'implied_total':lambda r:r['itt'],'home':lambda r:r['home'],'dome':lambda r:r['dome'],'resid':lambda r:r['resid']}
def binp(k,n):
  # two-sided exact
  from math import comb
  p=sum(comb(n,i) for i in range(n+1) if abs(i-n/2)>=abs(k-n/2))/2**n; return min(1,p)
def wilson(k,n,z=1.96):
  if n==0:return(0,0)
  p=k/n;d=1+z*z/n;c=p+z*z/(2*n);h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n));return((c-h)/d,(c+h)/d)
def test(P,f,weeks):
  k=n=0;pts=0
  for a,b in P:
    if a['wk'] not in weeks:continue
    x,y=f(a),f(b)
    if x is None or y is None or x==y:continue
    pick,oth=(a,b) if x>y else (b,a); n+=1; k+=pick['act']>oth['act']; pts+=pick['act']-oth['act']
  return k,n,pts
for scope in['team','league']:
  P=pairs(scope); print(f'\n== {scope} pairs gap<3, n={len(P)}')
  for nm,f in sig.items():
    for lab,wks in[('all2-4',{2,3,4}),('fit2-3',{2,3}),('test4',{4})]:
      k,n,pts=test(P,f,wks)
      if n: print(f"{nm:14s}{lab:8s} {k}/{n}={k/n:.3f} CI{tuple(round(v,3) for v in wilson(k,n))} p={binp(k,n):.3f} avgpts {pts/n:+.2f}")
