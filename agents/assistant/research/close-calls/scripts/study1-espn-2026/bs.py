import json,itertools,numpy as np
exec(open('an.py').read().split("print('== QBZ")[0])
R2=[r for r in R if r['wk']>=2 and r['proj']>=4]
idx={id(r):i for i,r in enumerate(R2)}
# game cluster: nfl team-week
cl={};cid=[]
for r in R2: cid.append(cl.setdefault((r['nfl'],r['wk']),len(cl)))
cid=np.array(cid)
P=[(a,b) for w in range(2,5) for a,b in itertools.combinations([r for r in R2 if r['wk']==w],2) if ok(a,b) and abs(a['proj']-b['proj'])<3 and a['act']!=b['act']]
def rule(nm):
  def f(a,b):
    if nm=='proj':x,y=a['proj'],b['proj']
    elif nm=='home':x,y=a['home'],b['home']
    elif nm=='dome':x,y=a['dome'],b['dome']
    elif nm=='itt':x,y=a['itt'],b['itt']
    elif nm=='home_then_proj':x,y=(a['home'],a['proj']),(b['home'],b['proj'])
    elif nm=='venue(home+dome)_then_proj':x,y=(a['home']+a['dome'],a['proj']),(b['home']+b['dome'],b['proj'])
    elif nm=='snap_last':x,y=a['snap1'],b['snap1']
    if x is None or y is None or x==y:return None
    return 1 if (x>y)==(a['act']>b['act']) else 0
  return f
rng=np.random.default_rng(1)
for nm in['proj','home','dome','itt','snap_last','home_then_proj','venue(home+dome)_then_proj']:
  f=rule(nm);res=[]
  for a,b in P:
    v=f(a,b)
    if v is not None:res.append((v,cid[idx[id(a)]],cid[idx[id(b)]],a['wk']))
  v=np.array([x[0] for x in res]);c1=np.array([x[1] for x in res]);c2=np.array([x[2] for x in res]);wk=np.array([x[3] for x in res])
  bs=[]
  for _ in range(2000):
    w=rng.poisson(1,len(cl));ww=w[c1]*w[c2];bs.append((v*ww).sum()/max(1,ww.sum()))
  lo,hi=np.percentile(bs,[2.5,97.5])
  print(f"{nm:28s} n={len(v)} win={v.mean():.3f} clusterCI=({lo:.3f},{hi:.3f}) w2-3={v[wk<4].mean():.3f} w4={v[wk==4].mean():.3f}")
