import pandas as pd,numpy as np,warnings;warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.pipeline import make_pipeline;from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
P=pd.read_pickle('pairs.pkl');D=[c for c in P.columns if c.startswith('d_')]
tr=P[P.season<=2023];va=P[P.season==2024];te=P[P.season>=2025]
def boot(win,base,sw,n=1000):
  df=pd.DataFrame({'w':win,'b':base,'sw':sw}).groupby('sw').agg(['sum','count'])
  ws,bs,c=df[('w','sum')].values,df[('b','sum')].values,df[('w','count')].values
  rng=np.random.default_rng(1);r=[];a=[]
  for _ in range(n):
    i=rng.integers(0,len(c),len(c));r.append((ws[i].sum()-bs[i].sum())/c[i].sum());a.append(ws[i].sum()/c[i].sum())
  return np.percentile(a,[2.5,97.5]),np.percentile(r,[2.5,97.5])
print('== univariate: when the higher-projected player is ALSO lower on signal, flip? rate the higher-proj wins split by sign of signal diff (train 21-23 / test 25-26)')
for c in D[1:]:
  s=[]
  for X in(tr,te):
    m=X[c].notna()&(X[c]!=0);z=X[m]
    s.append((round(z[z[c]>0].y.mean(),3),round(z[z[c]<0].y.mean(),3),len(z)))
  print(c,s)
res={}
for name,mdl in[('logit',make_pipeline(SimpleImputer(),StandardScaler(),LogisticRegression(C=0.1,max_iter=2000))),
                ('gbm',HistGradientBoostingClassifier(max_iter=200,learning_rate=0.05,max_depth=3,min_samples_leaf=500))]:
  mdl.fit(tr[D],tr.y)
  for nm,X in(('val2024',va),('test25-26',te),('test2026',te[te.season==2026])):
    p=mdl.predict_proba(X[D])[:,1];pick=(p>0.5).astype(int);win=(pick==X.y).astype(int)
    ci,dci=boot(win.values,X.y.values,X.sw.values)
    print(name,nm,'n',len(X),'model',round(win.mean(),4),'base',round(X.y.mean(),4),'CI',ci.round(4),'lift CI',dci.round(4),'flips%',round((pick==0).mean()*100,1))
    if nm=='test25-26':
      X=X.assign(p=p);X['dec']=pd.cut(X.p,[0,.4,.45,.5,.55,.6,.65,.7,1]);print(X.groupby('dec').y.agg(['size','mean']))
  if name=='logit':print(dict(zip(D,mdl[-1].coef_[0].round(3))))
