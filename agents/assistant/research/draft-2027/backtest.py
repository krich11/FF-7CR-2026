"""Backtest draft strategies on the 2026 7CR league draft (read-only data, see README).
Pool = the 192 drafted players only. Scores Weeks 1-5 (W5 partial as of Oct 11-12 2026)."""
import json,csv,random,math,statistics as st,collections
random.seed(7)
POS={1:'QB',2:'RB',3:'WR',4:'TE',5:'K',16:'D/ST'}
W=[1,2,3,4,5]
picks=sorted(json.load(open('raw/draft.json'))['draftDetail']['picks'],key=lambda p:p['overallPickNumber'])
order=json.load(open('raw/draft.json'))  # pickOrder in base settings
P={p['player']['id']:p['player'] for p in json.load(open('raw/draft_players.json'))}
PR={}
for w in range(1,6):
    for t in json.load(open(f'raw/roster{w}.json'))['teams']:
        for e in t['roster']['entries']:
            for x in e['playerPoolEntry']['player'].get('stats',[]):
                if x['statSourceId']==1 and x['statSplitTypeId']==1 and x['seasonId']==2026 and x['scoringPeriodId']==w: PR[(e['playerId'],w)]=x['appliedTotal']
PL={}
for i,q in P.items():
    act={s['scoringPeriodId']:s['appliedTotal'] for s in q['stats'] if s['seasonId']==2026 and s['statSourceId']==0 and s['statSplitTypeId']==1}
    played={s['scoringPeriodId'] for s in q['stats'] if s['seasonId']==2026 and s['statSourceId']==0 and s['statSplitTypeId']==1 and (s.get('stats',{}).get('210') or q['defaultPositionId']==16)}
    projs=[PR[(i,w)] for w in W if (i,w) in PR]
    fill=st.mean(projs) if projs else 0
    PL[i]=dict(id=i,name=q['fullName'],pos=POS[q['defaultPositionId']],team=q.get('proTeamId'),adp=q.get('ownership',{}).get('averageDraftPosition') or 300,
       act={w:act.get(w,0) for w in W},proj={w:PR.get((i,w),fill if w in played else 0) for w in W},played=played,w1proj=PR.get((i,1),0))
OUT={i for i in PL if PL[i]['name'] in ('Josh Jacobs','Zach Charbonnet')}  # confirmed out at draft time
# VBD: value = W1 projection minus replacement (QB12, RB30, WR30, TE12, K12, DST12) among pool
rep={}
for pos,n in [('QB',12),('RB',30),('WR',30),('TE',12),('K',12),('D/ST',12)]:
    v=sorted([p['w1proj'] for p in PL.values() if p['pos']==pos],reverse=True); rep[pos]=v[min(n,len(v))-1]
for p in PL.values(): p['vorp']=p['w1proj']-rep[p['pos']]
SLOTS=[('QB',{'QB'}),('RB',{'RB'}),('RB',{'RB'}),('WR',{'WR'}),('WR',{'WR'}),('TE',{'TE'}),('FLEX',{'RB','WR','TE'}),('D/ST',{'D/ST'}),('K',{'K'})]
def lineup(roster,w,key):
    used=set();tot=0
    order=sorted(SLOTS,key=lambda s:s[0]=='FLEX')
    for s,el in order:
        c=[p for p in roster if p['id'] not in used and p['pos'] in el]
        if not c: continue
        b=max(c,key=lambda p:key(p,w)); used.add(b['id']); tot+=b['act'][w]
    return tot
def score(roster):
    bb=sum(lineup(roster,w,lambda p,w:p['act'][w]) for w in W)
    pj=sum(lineup(roster,w,lambda p,w:p['proj'][w]) for w in W)
    zeros=sum(1 for p in roster for w in W if w not in p['played'] and p['pos']!='D/ST')
    dead=sum(1 for p in roster if not p['played'] and p['pos']!='D/ST')
    return bb,pj,zeros,dead
CAP={'QB':2,'RB':7,'WR':7,'TE':2,'K':1,'D/ST':1}
def base_ok(p,roster,rnd,nleft):
    c=collections.Counter(x['pos'] for x in roster)
    if c[p['pos']]>=CAP[p['pos']]: return False
    need=[pos for pos in ('K','D/ST') if c[pos]==0]
    if p['pos'] in('K','D/ST') and rnd<15: return False
    if nleft<=len(need) and p['pos'] not in need: return False
    if p['pos']=='QB' and c['QB']>=1 and rnd<12: return False
    return True
def strat(name):
    def allow(p,roster,rnd,pick):
        c=collections.Counter(x['pos'] for x in roster); pos=p['pos']
        if name=='ADP/BPA': return True
        if name=='Zero RB': return pos!='RB' or rnd>=6
        if name=='Hero RB': return (pos=='RB') if rnd==1 else ((pos!='RB') if rnd<=5 else True)
        if name=='Robust RB': return pos=='RB' if rnd<=2 else True
        if name=='Zero WR': return pos!='WR' or rnd>=6
        if name=='WR-heavy': return pos=='WR' if rnd<=3 else True
        if name=='Late-round QB': return pos!='QB' or rnd>=10
        if name=='Elite TE early': return (pos=='TE') if (rnd in(2,3) and c['TE']==0) else True
        if name=='Late TE': return pos!='TE' or rnd>=10
        if name=='Bimodal RB': return pos=='RB' if rnd<=2 else (pos!='RB' if rnd<=8 else True)
        if name=='Playbook 2027':
            if p['id'] in OUT and rnd<14: return False
            if pos in('QB','TE') and pick<p['adp']: return False
            if pos=='QB' and c['QB']>=1: return False
            if rnd==2 and c['RB']==0 and pos!='RB': return False
            return True
        return True
    return allow
def keyf(name,roster):
    if name=='VBD': return lambda p:-p['vorp']
    if name=='Stacking':
        qbt={x['team'] for x in roster if x['pos']=='QB'}
        return lambda p:p['adp']-(15 if p['pos'] in('WR','TE') and p['team'] in qbt else 0)
    return lambda p:p['adp']
def choose(name,avail,roster,rnd,pick,nleft):
    al=strat(name); k=keyf(name,roster)
    c=[p for p in avail if base_ok(p,roster,rnd,nleft) and al(p,roster,rnd,pick)]
    if not c: c=[p for p in avail if base_ok(p,roster,rnd,nleft)] or list(avail)
    return min(c,key=k)
NAMES=['ADP/BPA','VBD','Zero RB','Hero RB','Robust RB','Bimodal RB','Zero WR','WR-heavy','Late-round QB','Elite TE early','Late TE','Stacking','Playbook 2027']
# --- fixed-others sim at QBZ slot
ours=[k['overallPickNumber'] for k in picks if k['teamId']==13]
taken_at={k['playerId']:k['overallPickNumber'] for k in picks if k['teamId']!=13}
def sim_fixed(name):
    roster=[]
    for n,pk in enumerate(ours):
        rnd=n+1
        avail=[PL[i] for i in PL if (i not in taken_at or taken_at[i]>pk) and PL[i] not in roster]
        roster.append(choose(name,avail,roster,rnd,pk,16-n))
    return roster
teams=collections.defaultdict(list)
for k in picks: teams[k['teamId']].append(PL[k['playerId']])
league={t:score(r) for t,r in teams.items()}
rows=[]
def rank(v,idx): 
    others=[league[t][idx] for t in league if t!=13]; return 1+sum(1 for x in others if x>v)
for nm in NAMES+['QBZ actual 2026']:
    r=teams[13] if nm=='QBZ actual 2026' else sim_fixed(nm)
    bb,pj,z,d=score(r)
    rows.append(dict(strategy=nm,bestball_w1_5=round(bb,1),rank_bestball_vs_11=rank(bb,0),projset_w1_5=round(pj,1),rank_projset_vs_11=rank(pj,1),missed_player_games=z,players_zero_games=d,
       first4=' / '.join(p['name']+' '+p['pos'] for p in r[:4]),roster=' | '.join(f"{p['pos']} {p['name']}" for p in r)))
lg_bb=st.mean(v[0] for t,v in league.items() if t!=13); lg_pj=st.mean(v[1] for t,v in league.items() if t!=13)
# --- Monte Carlo: others draft by noisy ADP (lognormal sigma calibrated to observed |log(pick/adp)|)
obs=[math.log(k['overallPickNumber']/PL[k['playerId']]['adp']) for k in picks if PL[k['playerId']]['adp']<300]
SIG=st.pstdev(obs)
def sim_mc(name,slot,nsim=300):
    res=[]
    for s in range(nsim):
        noisy={i:PL[i]['adp']*math.exp(random.gauss(0,SIG)) for i in PL}
        avail=set(PL); rosters=collections.defaultdict(list); pk=0
        for rnd in range(1,17):
            seq=range(1,13) if rnd%2 else range(12,0,-1)
            for sl in seq:
                pk+=1; R=rosters[sl]; nleft=16-len(R); al=[PL[i] for i in avail]
                if sl==slot: p=choose(name,al,R,rnd,pk,nleft)
                else:
                    c=[x for x in al if base_ok(x,R,rnd,nleft)] or al
                    p=min(c,key=lambda x:noisy[x['id']])
                R.append(p); avail.discard(p['id'])
        mine=score(rosters[slot]); oth=[score(rosters[t])[0] for t in rosters if t!=slot]
        res.append((mine[0],mine[1],1+sum(1 for x in oth if x>mine[0]),st.mean(oth)))
    return res
mc=[]
for nm in NAMES:
    for slot in (1,6,12):
        r=sim_mc(nm,slot)
        bb=[x[0] for x in r]; mc.append(dict(strategy=nm,slot=slot,mean_bestball=round(st.mean(bb),1),sd=round(st.pstdev(bb),1),mean_minus_field=round(st.mean(x[0]-x[3] for x in r),1),mean_rank=round(st.mean(x[2] for x in r),2),mean_projset=round(st.mean(x[1] for x in r),1)))
with open('bt/backtest_fixed_slot12.csv','w') as f:
    c=csv.DictWriter(f,rows[0].keys()); c.writeheader(); c.writerows(rows)
with open('bt/backtest_montecarlo.csv','w') as f:
    c=csv.DictWriter(f,mc[0].keys()); c.writeheader(); c.writerows(mc)
print('league other-11 avg bestball',round(lg_bb,1),'projset',round(lg_pj,1),'SIG',round(SIG,3))
for r in sorted(rows,key=lambda r:-r['bestball_w1_5']): print({k:r[k] for k in list(r)[:8]})
for m in mc: print(m)
