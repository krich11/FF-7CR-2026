# Sigma — Fantasy Kicker Strategy Research Notes (for Blitz)

**As of:** Sun Sep 20, 2026 ~11:15 AM CT  
**Scope:** What predicts fantasy kicker points; ESPN scoring; signal catalog; high-implied-total vs FG-volume/“Goldilocks” strategies; failure modes; weekly checklist.  
**Constraint:** No invented correlations. Weak/mixed evidence labeled plainly.  
**Not done:** No messages to Ken. No ESPN lineup writes.

---

## 1. Executive synthesis

1. **Opportunity (FG attempts/makes) dominates accuracy and distance skill** for fantasy points. Multiple independent analyses agree (4for4 Raybon; Subvertadown; Hayden Winks Yahoo 2026; Fantasy Nerds).
2. **Weekly #1 process signal is Vegas-implied team total + positive/neutral game script** (favorite / not trailing). Bucketed multi-season splits exist (4for4 2013–14; 4for4 2021–24 “≥27” double-rate for 10+ K games).
3. **Ken’s thesis is partially right, wrongly framed if taken as “bad offense.”** Best FG volume comes from offenses that **move the ball between the 20s but stall / convert poorly in the red zone**, often with **conservative fourth-down coaches** and/or **strong defenses** that keep games close. Truly mediocre/underperforming offenses **punt more**; they do not reliably create FG volume (Deuces Cracked; FantasyPros “5th–15th”; Fantasy Nerds top-K avg team ~26.7 PPG / ~8th–9th).
4. **Season-long year-to-year predictability is weak** (PFF Barrett 2018). Streaming or late-draft + weekly Vegas beats drafting “the best kicker” early.
5. **Weather that matters most is sustained wind ≥15–20 mph**; dome/roof closed is a soft positive; Denver altitude adds ~4–5 yards of *range* (not free fantasy points every week).

---

## 2. Scoring (ESPN default — verified)

**Source:** ESPN Fan Support “Scoring Formats,” updated **Aug 18, 2026**. Standard KICKING block:

| Event | Default pts |
|-------|-------------|
| FG made 60+ yards | **6** |
| FG made 50–59 yards | **5** |
| FG made 40–49 yards | **4** |
| FG made 0–39 yards | **3** |
| PAT made | **1** |
| FG missed (any distance) | **−1** |

**PAT missed:** Listed only under **custom** options (“Each PAT Missed”), not in the standard block. Third-party mirrors (e.g. fantasypointcalculators; ESPN value-calculator style charts) often show **0 for XP miss** unless the LM sets a penalty. **Do not assume −1 XP miss** without checking `league.json` / LM scoring. Blitz W2 memo recorded league items as FG distance buckets + XP=1 (confirm PAT miss separately if needed).

**Implication for strategy:** Distance bonuses (esp. 50+ / 60+) raise ceiling for long-leg / dome / DEN / aggressive long-attempt coaches, but **volume of makes** still drives most points. Missed FG (−1) is a real tax; accuracy is a **tie-breaker**, not the primary draft/stream filter.

---

## 3. What the evidence says predicts fantasy K points

### 3.1 Strong / well-supported

| Signal | Evidence | Strength |
|--------|----------|----------|
| **Field goals made / attempts** | Raybon 4for4 (2013–14): FGM **r=0.86**, FGA **r=0.73** vs fantasy PPG; FG% only **0.56**. Winks (3yr thru 2025): FGM corr **0.80** vs XPM **0.32**. Subvertadown: “sum of all FGs” highest predictive component of future K scoring among kick-stat components. | **Strong** |
| **Vegas-implied team total** | Raybon Table 3 (2013–14): monotonic rise in K pts by implied bucket (e.g. **≥29 → 9.17** avg K pts; 26–29 → 8.08; 23–26 → 7.57; &lt;17 → 5.94). 4for4 Eakins (2025): 10+ fantasy K games **more than double** when team total **≥27** vs **≤26**. PFF Barrett: if streaming, prefer **heavy favorites + high implied**. Sharp / ETR publish implied totals as weekly tools. | **Strong (weekly)** |
| **Positive / neutral game script (leading or tied)** | Raybon: FG attempt rate on 4th inside 35 — **87.5% leading/tied** vs **69.5% trailing**. NBC Denny Carter (2026): reliable Ks attached to lots of neutral/positive script (won’t abandon FGs while chasing). | **Strong directional** |
| **Conservative 4th-down coaching / “take the 3”** | Winks: optimal go-for-it rate corr **−0.13** to K fantasy PPG (weak magnitude, correct sign). Carter: maximize opportunity = FGAs; hyper-aggressive coaches remove easy FG tries. Concrete 2025–26 examples cited across sources: Houston/Ryans, LAC/Harbaugh, Seattle “take points,” vs Detroit/Campbell (Bates low FGA games). | **Moderate (sign clear; effect size small–moderate)** |

### 3.2 Moderate / conditional

| Signal | Evidence | Strength |
|--------|----------|----------|
| **“Goldilocks” offense: good drive success, mediocre RZ TD%** | FantasyPros (2026): top-5 Ks often on offenses that move the ball **but not** the absolute top TD scorers (2025: LAR/BUF/NE/DET led TDs; none of their Ks top-5). Target roughly **5th–15th** projected offenses. Deuces Cracked (props, 2026): value when team moves ball then stalls inside ~30; **bad offenses punt**. | **Moderate — supports “not flamethrower RZ,” not “bad offense”** |
| **Own-team defense quality / close games** | FantasyLabs citing RotoViz-era work: upside (5+ FGA) games disproportionately on above-avg defenses (DVOA / run D). Carter: Houston FG volume tied to elite D + suboptimal 4th downs. | **Moderate** |
| **Home / dome / roof closed** | Raybon: slight home bump (esp. XP). PFF: home ~8.5, dome ~8.7 vs overall ~8.3 FanDuel sample. FantasyPros: cold outdoor less common among top-10 finishers. | **Soft positive** |
| **Wind / extreme weather** | Raybon: avoid **15+ mph** wind or heavy snow. PFF: **≥20 mph** → ~7.7 vs 8.3. Deuces: wind most important weather variable; coaches punt instead of 48-yarders. RotoWire model discounts: 10–15 mph −3%, 15–20 −7%, 20+ −15% (prop model — illustrative, not fantasy gospel). | **Moderate when wind is high** |
| **Kicker career make% / long-leg (50+)** | Raybon: year-to-year FG% almost uncorrelated; career % better than single-season. Subvertadown: long FGs somewhat self-predictive; short “RZ stall” kicks **less** predictive than many assume. Winks: FG% corr **0.44** — matters on margin; Aubrey/Little “range expands attempt set.” Carter: accuracy secondary to opportunity. | **Tie-breaker** |
| **Pace / first downs / passing volume** | Winks: TDs corr **0.43**, first downs **0.41**. 4for4 Eakins: many top Ks from top-half pass-attempt offenses (mixed — Boswell/Dicker counterexamples). | **Moderate proxy for scoring opportunities** |

### 3.3 Weak, mixed, or overrated

| Signal | Evidence | Strength |
|--------|----------|----------|
| **Prior-week / prior-year fantasy points** | PFF Barrett: even best season-to-season corr still **weak**; weekly trailing FPPG near noise. Subvertadown: PATs more sticky than FGs. | **Weak for prediction** |
| **Opponent historical FG/XP allowed** | Fantasy Nerds (2018–22): defenses that allow many points allow more FG volume; but **own offense still primary**. Week-to-week opponent “K-friendly” ranks are noisy. | **Mixed / secondary** |
| **Sack / negative script on *own* offense** | Intuitive (drives stall → FG) but **negative team points and turnovers correlate negatively** with K fantasy in Raybon table (INT thrown −0.47, TO −0.41). Stalling after successful drives ≠ chaotic negative offense. | **Do not chase “bad offense”** |
| **Altitude (DEN)** | Burke Advanced Football Analytics (~2013): visitor FGs in Denver ~**+5 yards** range vs other outdoor (temp-controlled sample). Physics estimates ~4–5 yards. **Does not by itself guarantee more fantasy points** — needs attempts + make rate; cold/wind can offset. NBC Carter on Lutz: “not about thin air” — script/D. | **Real physics; secondary fantasy lever** |
| **Individual accuracy as primary ranker** | Multiple sources: opportunity ≫ accuracy. | **Weak as primary** |

**numberFire / Establish The Run:** Public ETR content emphasizes **implied team totals** as a general fantasy tool (same math as Sharp). numberFire publishes weekly K projections (XPM/FGM/FGA/FP) but **did not surface a transparent public methodology paper** in this research pass — treat as black-box proj, not a cited causal study. **RotoViz:** “Kickers Are People Too” series exists (paywall/thin public body on fetch); FantasyLabs summary of related work stresses **defense + opportunity**. Do not invent RotoViz coefficients not visible in public text.

---

## 4. Strategy comparison: High implied total vs “mediocre offense / FG volume”

### 4.A — High implied team total (classic Vegas stream)

**How it works:** Prefer available K on the team with the highest (or top-tier) implied points, especially as a **favorite** (positive script).

**When it wins**
- Multi-season Raybon buckets: higher implied → higher average K fantasy points (clear monotonic pattern 2013–14).
- 4for4 2025: **≥27** implied associated with **&gt;2×** rate of 10+ fantasy K games vs ≤26.
- Provides **XP floor + FG chances**; does not require forecasting stalls.
- Aligns with PFF Barrett’s practical streaming advice despite overall randomness.

**When it fails**
- Elite RZ TD conversion → many XPs, few FGs (FantasyPros 2025 top-TD teams’ kickers missed top-5). Ceiling still often OK; **FG upside muted**.
- Blowout script: leading team kneels / runs clock → second-half FG drought.
- Aggressive 4th-down coach (Campbell-type) in high-total games.
- Extreme wind/cold outdoor despite high total (Vegas may partially bake this in late).

### 4.B — Mediocre / underperforming offense → FG volume (Ken’s framing)

**Strict reading (“bad offense = more FGs”): NOT supported.**
- Fantasy Nerds 2018–2022: top-5 fantasy Ks averaged **26.7 PPG** (~**8.6th** scoring rank); **64%** on top-10 offenses; almost never bottom-half. Bottom-5 Ks ~**20.2 PPG** / ~23rd.
- Deuces Cracked: “Bad offenses punt; they do not kick.”
- Raybon: team points scored corr **0.68** to K fantasy PPG — positive, not inverse.

**Refined reading (“competent offense, poor RZ TD%, take-the-3 coach”): PARTIALLY supported.**
- FantasyPros: target **~5th–15th** projected offenses — high enough to reach FG range often, not so efficient that everything is a TD.
- Props literature: same team total can imply very different FG/TD mixes based on RZ efficiency and midfield stall rate.
- 2025 anecdotes cited by FantasyPros/Carter: high FG-attempt teams (HOU, SEA) with defense + conservative 4th downs outperformed pure flamethrower kickers.

### 4.C — Head-to-head verdict

| Regime | Prefer |
|--------|--------|
| Weekly stream, limited research time | **High implied + favorite** (4.A) |
| Differentiating two similar implied totals | Add **RZ TD% (lower better for FG upside)**, **4th-down aggression (lower better)**, **own D / close-game likelihood**, **weather** |
| Season-long “set and forget” | Offense that scores **enough** + coach/D that sustains FGAs (Fairbairn/Dicker/Aubrey archetypes) — **not** bottom-quartile offenses |
| Ken thesis as stated | **Reject pure form**; **accept refined Goldilocks form** |

**No public multi-season study found that ranks “underperforming offenses” above average/good offenses for fantasy K PPG.** The closest support is **non-elite TD efficiency among otherwise competent offenses**.

---

## 5. Signal catalog (for Blitz weekly use)

| # | Signal | Direction for K | Numeric anchors (only where sourced) | Notes |
|---|--------|-----------------|--------------------------------------|-------|
| 1 | Implied team total | Higher better | Soft tiers from Raybon/4for4: **≥27** strong; **≥29** historically elite avg; **&lt;20** fade | Primary weekly |
| 2 | Spread / favorite | Favorite better | Leading/tied → much higher FG try rate inside 35 | Script |
| 3 | Game total (O/U) | Higher → more scoring chances | Use with spread to split implied | Not sufficient alone |
| 4 | Outdoor wind | Higher worse | Caution **≥15 mph**; clear problem **≥20 mph** | Worst weather lever |
| 5 | Precip / extreme cold | Mild negative | Cold alone weaker than wind; rain+wind compound | Late-season outdoor |
| 6 | Dome / roof closed | Soft positive | PFF dome sample ~+0.4 vs avg | Confirm retractable roof |
| 7 | Altitude (DEN) | Long-FG / range bump | ~**+4–5 yards** range (Burke / physics) | Secondary; not auto-start |
| 8 | Opponent FG/XP rates | Weak | Prefer soft scoring defenses as secondary | Noisy week-to-week |
| 9 | Opp / own red-zone TD% | Lower own RZ TD% → more FG upside *conditional on drives* | No universal threshold in sources | Needs drive success first |
| 10 | Sack / negative chaos | Avoid for *own* offense | Turnovers negatively correlated with K pts | Stall ≠ collapse |
| 11 | K career make% / 50+ | Tie-breaker | Career % &gt; single-year % (Raybon) | Expands attempt set if coach trusts leg |
| 12 | Pace / first downs | Higher better | Winks corr ~0.41 first downs | Proxy |
| 13 | Coaching FG aggression | Conservative better for volume | Winks go-for-it corr **−0.13** | Small but real |
| 14 | Own defense strength | Better D → more positive/close script | Upside FGA games skew to better D (FantasyLabs/RotoViz summary) | Pair with offense competence |

---

## 6. Failure modes

1. **Chasing “bad” offenses** expecting FG volume → low drive success → punts, not kicks.
2. **Blindly starting highest implied** on a hyper-efficient RZ team + aggressive HC → XP-heavy dud relative to expectation.
3. **Ignoring wind ≥15–20 mph** outdoors → fewer long attempts + lower make rates.
4. **Trusting last week’s 4-FG game** as sticky (FGs less predictive than PATs; season-long corr weak).
5. **Overweighting kicker brand / accuracy** over team environment.
6. **Blowout favorites**: high implied can still yield second-half FG drought.
7. **Assuming Denver = automatic K smash** without attempts/script.
8. **Assuming ESPN −1 XP miss** without league settings confirmation.
9. **Dropping roster capital for tiny K edges** (Blitz SPEC: don’t replace rostered K without clear EV; see W2 memo).
10. **Treating opponent “allows kickers” ranks as primary** — secondary at best.

---

## 7. Weekly checklist (numeric where supported)

Use in order; stop when a hard fade triggers.

1. **Implied team total** — Prefer available K with implied **≥24**; prioritize **≥27**; treat **≥29** as elite environment (historical avg K pts ~9+ in Raybon ≥29 bin). Fade **&lt;20** unless no alternatives.
2. **Spread** — Prefer **favorites** (or toss-up). Soft fade large underdogs (trailing script → fewer FG tries).
3. **Wind** — If outdoor and sustained wind **≥15 mph**, downgrade; **≥20 mph** = strong fade vs dome/calm alternatives.
4. **Roof** — Prefer dome / confirmed closed roof when outdoor alternatives are windy or fringy.
5. **Coach 4th-down profile** — Prefer known “take the 3” staffs; soft fade Campbell-tier aggression when choosing between equals.
6. **RZ / TD efficiency (tie-break)** — Among similar implied totals, slight lean to teams that **reach scoring range but convert TDs at a mediocre rate** (Goldilocks). Do **not** pick bottom-quartile offenses for this reason alone.
7. **Own defense / game competitiveness** — Prefer games likely to stay within one score more of the time (more FG decisions late).
8. **Kicker quality (last)** — Career FG% and 50+ willingness as tie-breakers only.
9. **Projection cross-check** — Consensus (FP/CBS/ESPN/FBG) should roughly agree with Vegas story; large disagreements warrant a second look (injury, weather not in early lines, etc.).

---

## 8. W2 implication — Pineiro vs late FA streamers

**Context (from `w2-k-swap.md`, same date):** Eddy Pineiro (SF) vs MIA; SF implied **~29.0** (Sharp); heavy favorite; calm Levi’s weather; Ken assumes limited duty (no FG ≥50) → decision figure **~6.5**; best late FA Drew Stevens (WAS @ DAL) adj proj **~7.35** on WAS implied **~23.25**; Net EV after drop cost **fails** swap thresholds.

**Research mapping**
- SF **29.0** sits in Raybon’s **≥29** bucket (historically highest avg K fantasy). This is **Strategy 4.A at maximum**, not a Goldilocks bet.
- Even if SF is “too efficient” (XP-heavy), high implied + favorite script still supports **XP floor + some FGAs**. Limited-leg only removes the 50+ bucket — does not erase environment.
- Late FA pool (Stevens/Shrader/Ryland/Gay/Patterson) clusters at **implied ~15.5–23.25** — below the **≥27** “double rate of 10+ games” band from 4for4 2025. None offer a clearer “stall-heavy competent offense” edge that would overturn a ~29 implied favorite environment on research alone.
- Goldilocks thesis does **not** recommend swapping off a 29-implied favorite kicker for a ~23-implied streamer.

**Implication for Blitz:** Research **supports HOLD Pineiro** over late FA streamers for W2, consistent with the W2 swap memo’s Net EV fail. A stream would need either (a) Pineiro ruled out / severely limited beyond Ken’s −2.0 haircut, or (b) a streamer environment that approaches SF’s implied/script — **not present in the late FA pool as documented**.

---

## 9. Sources (fetched / searched this pass)

1. ESPN Fan Support — Scoring Formats (updated Aug 18, 2026) — default K distance + FG miss  
2. FantasyPros — How to Draft Kickers 2026 (Evan Tarracciano, Aug 11, 2026) — 5th–15th offense band; FG &gt; XP; 2025 TD-leader counterexamples  
3. NBC Sports — Fantasy Football Kicker Strategy 2026 (Denny Carter, Aug 25, 2026) — script, 4th downs, opportunity ≫ accuracy; Pineiro note  
4. 4for4 — Daily Fantasy Playbook 2015: Kicker Strategy (Chris Raybon) — correlation table; FG try% by script; Vegas implied buckets  
5. 4for4 — Debunking the Randomness of Kickers (Jennifer Eakins, May 2025) — ≥27 implied vs 10+ K games; volume/3rd-down notes  
6. Hayden Winks / Yahoo Sports — Kicker deep dive 2026 (Aug 20, 2026) — FGM 0.80 vs XPM 0.32; TD/1st-down corrs; go-for-it −0.13; FG% 0.44  
7. Subvertadown — Components Contributing to Kicker Predictability (May 2022 / updated 2026) — FG sum predictive; RZ stall less sticky than assumed  
8. PFF — Metrics that Matter: Kickers (Scott Barrett, 2018) — weak year-to-year/weekly corr; stream high implied favorites; wind/dome samples  
9. Fantasy Nerds — Fantasy kicker math (Daniel Hepner, 2023) — 2018–22 top/bottom K vs team PPG; rejects “too many TDs” as a reason to fade good offenses  
10. Deuces Cracked — NFL Kicker and Field Goal Props guide (Sep 6, 2026) — stalled drives not bad offenses; wind; 4th-down analytics  
11. Sharp Football Analysis — NFL Implied Team Totals tool (Week 2 / ROS 2026)  
12. Establish The Run — NFL Average Implied Team Totals 2026 (tooling/context; implied-total philosophy)  
13. Advanced Football Analytics (Brian Burke, 2013) — Denver altitude ~+5 yards FG range  
14. RotoWire — Kicker prop model notes (wind multipliers; Vegas scaling) — betting, used cautiously  
15. Football Weblog — How to Stream a Fantasy Football Kicker (2025) — Vegas implied as primary stream method  
16. Internal: `results/sigma/w2-k-swap.md` — Pineiro vs late FA numbers for W2 implication  

**Not strongly available in open fetch this pass:** full public RotoViz Giffen FGA model coefficients; numberFire proprietary K methodology write-up; Harvard Sports Analysis 2014 article body (fetch timeout/empty).

---

## 10. One-line for Blitz ops

**Process:** Rank streamers by implied total + favorite script first; apply wind/dome and coach aggression; use Goldilocks RZ only as a tie-break among competent offenses — never as a reason to start a weak offense’s kicker over a 27–29+ implied favorite.
