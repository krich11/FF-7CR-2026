# Sigma — Fantasy Kicker Strategy Bible

**Audience:** Quantum Blitz (Ken Rich) · Sigma FF statistician desk  
**League context:** ESPN standard distance K scoring  
**Date context:** NFL 2026 · Week 2 Sunday Sep 20, 2026 (CT)  
**Hard rule:** Invent nothing. Every quantitative claim cites a public source. Gaps = UNKNOWN / insufficient evidence.

---

## 1) ESPN standard K scoring math — what drives variance

### Official ESPN standard kicking (public leagues / LM default)

Source: [ESPN Fan Support — Scoring Formats](https://support.espn.com/hc/en-us/articles/360003914032-Scoring-Formats) (updated Aug 18, 2026):

| Event | Points |
|-------|--------|
| FG made 0–39 yards | **+3** |
| FG made 40–49 yards | **+4** |
| FG made 50–59 yards | **+5** |
| FG made 60+ yards | **+6** |
| PAT made | **+1** |
| FG missed (any distance) | **−1** |

**PAT misses:** ESPN standard lists no default penalty for missed PAT (custom “Each PAT Missed” exists). Net effect of a miss = forgone +1 only unless the league enables the custom setting. ([ESPN Scoring Formats](https://support.espn.com/hc/en-us/articles/360003914032-Scoring-Formats); community confirmation of no default XP miss penalty on older threads is secondary.)

### Variance decomposition (published correlations)

Hayden Winks (Yahoo Sports, Aug 20, 2026), last-three-years kickers ≥10 games on one team:

| Component | Correlation to K fantasy PPG | Implication |
|-----------|------------------------------|-------------|
| Field goals **made** | **0.80** | Dominant driver |
| Extra points made | **0.32** | Floor / consistency, not upside |
| Team touchdowns scored | **0.43** | Offensive success matters |
| Team first downs | **0.41** | Drive volume / efficiency proxy |
| FG make % | **0.44** | Matters, secondary to opportunity |
| Optimal 4th-down go-for-it rate (RBSDM) | **−0.13** | Weak negative; aggressive coaches steal FGs |

Source: [Yahoo / Hayden Winks — 2026 kicker deep dive](https://sports.yahoo.com/fantasy/article/fantasy-football-yes-its-time-for-hayden-winks-kicker-deep-dive-for-2026-143423456.html)

**What this means for variance under ESPN distance scoring:**

1. **Attempt volume (esp. FGA)** dominates week-to-week swings — not raw accuracy alone (Winks; also Fantasy Nerds 2018–22 top vs bottom FGM gap ~40% vs FG% gap ~12%: [Fantasy Nerds — Fantasy kicker math](https://www.fantasynerds.com/news/article/694/fantasy-kicker-math)).
2. **Distance tier bonuses** amplify long-range volume: a made 50–59 is +5 vs +3 for 0–39 (+67%); 60+ is +6. RotoWire (Aug 27, 2026) notes indoor vs outdoor 50+ make rates of **0.380 vs 0.285** per game (ex-Aubrey/Fairbairn) → ~0.5 FP/game from the long tier alone under 5-pt scoring. ([RotoWire — 2026 K draft strategy](https://www.rotowire.com/football/article/2026-fantasy-football-draft-strategy-kickers-rankings-and-draft-strategy-130303))
3. **Misses** (−1) are a small expected drag; RotoWire estimates most kickers project ~5–6 misses/season under default −1, so miss penalties “don’t much matter” for ranking unless custom penalties are large.
4. **XP feast weeks** (blowout TD scripts) raise floor via +1s but have weak correlation (0.32) to total fantasy points vs FG weeks (0.80).

**Positional separation (context):** Winks — K1 ≈ 11.0 PPG, K2 ≈ 10.3, replacement-level 12-team starter ≈ 8.2 → ~2.5–3.0 PPG top-to-replacement gap.

---

## 2) Predictive signals — ranked by published / out-of-sample evidence strength

**Evidence grades**

| Grade | Meaning |
|-------|---------|
| **A** | Multi-year quantitative correlation / controlled study with clear direction |
| **B** | Repeated analyst methodology with supporting counts/tables; not fully OOS-validated in one paper |
| **C** | Mechanistic / academic support for make-rate or opportunity, weaker fantasy-point link |
| **D** | Narrative / thin samples / UNKNOWN magnitude for fantasy PPG |

### Ranked signal table

| Rank | Signal | Grade | Direction (for K fantasy pts) | Key cite + finding |
|------|--------|-------|-------------------------------|--------------------|
| 1 | **Implied team total (ITT) / Vegas team total** | **A** | Higher → more K pts; sharp threshold cited at **27+** | 4for4 Jennifer Eakins: past four seasons, solid correlation of team totals to K output; **10+ fantasy-point weeks more than double when team total ≥27 vs ≤26**. ([4for4 2025](https://www.4for4.com/2025/preseason/debunking-randomness-kickers-fantasy-football); [Yahoo reprint](https://sports.yahoo.com/article/2025-fantasy-football-strategy-tips-kicker-scoring-is-not-random--heres-why-143427882.html)). Fantasy Footballers: Vegas expected points = “most important indicator.” ([FFB 2023](https://www.thefantasyfootballers.com/analysis/the-art-of-streaming-fantasy-football-kickers-like-a-wall-street-trader/)). RotoViz formula leads with “high Vegas point totals.” ([RotoViz 2020](https://www.rotoviz.com/2020/09/streaming-kicker-week-1/)) |
| 2 | **Offensive scoring / drive success (PPG, TDs, first downs)** | **A** | Higher team scoring → higher K PPG | Fantasy Nerds (2018–22): top-5 Ks avg **26.7** team PPG (rank ~8.6) vs bottom-5 **20.2** (rank ~22.8); **64%** of top-5 on top-10 offenses; **no** top-5 K on a team outside top-20 scoring. ([Fantasy Nerds](https://www.fantasynerds.com/news/article/694/fantasy-kicker-math)). Winks: team TD corr **0.43**, first downs **0.41**. |
| 3 | **Favorite / win probability (spread-implied)** | **A–B** | Favorites / winners score far more K pts | Fantasy Index (2014–23): winning-team Ks **8.68** FP/g vs losing **5.49** (~3.2 gap); home vs away only **7.25 vs 6.93** (~0.3). ([Fantasy Index, May 2024](https://fantasyindex.com/2024/05/22/factoid/kickers)). RotoWire: among tested buckets, **favorites in dome/retractable** performed best; favorites in O/U **48+** also strong. ([RotoWire 2026](https://www.rotowire.com/football/article/2026-fantasy-football-draft-strategy-kickers-rankings-and-draft-strategy-130303)) |
| 4 | **Field-goal opportunity / FGA (incl. coach 4th-down philosophy)** | **A–B** | More FGA → more fantasy pts; hyper-aggressive 4th downs hurt | Winks: FGM corr 0.80; 4th-down go-for-it **−0.13**. NBC Sports Denny Carter: “maximize kicker opportunity… Not even accuracy matters as much as plain old kicker opportunity”; cites HOU 2.9 FGA/g (2025) under Ryans. ([NBC Sports Aug 2026](https://www.nbcsports.com/fantasy/football/news/fantasy-football-kicker-strategy-2026-rankings-tiers-and-how-to-find-an-edge)). FFB: Staley-era Chargers example — high O/U but few 10+ K weeks due to 4th-down aggression. |
| 5 | **Red-zone TD rate (own offense) — “TD cannibalization”** | **B** | Lower RZ TD% (given drives into RZ) → more FGA | RotoViz: combine high Vegas totals + high pass offense **with poor RZ TD rates**. FantasyPros Week 1–2 2026 K Score: RZ EFF scored **inverse** to offense RZ success — “struggles to score TDs in the red zone equates to more field goal opportunities.” ([FantasyPros W2 2026](https://www.fantasypros.com/2026/09/fantasy-football-kicker-rankings-start-sit-advice-week-2-2026/)). **Caveat:** Fantasy Nerds explicitly rejects “scores too many TDs → bad for K” as a reason to prefer weak offenses. |
| 6 | **Dome / retractable roof vs outdoor** | **B** | Indoor ↑ K fantasy pts (~0.6–0.9) | RotoWire last 3 years: **9.1** FP indoor/retractable vs **8.2** outdoor (outdoor **8.0** Nov–Jan); ex-Aubrey/Fairbairn **8.7 vs 8.1**; 50+ makes **0.380 vs 0.285**/g. FFB: dome games can “compensate for a not-so-high betting line.” Clark et al. (MIT, 2000–11): indoor/dome environments easier in stadium difficulty rankings (e.g., Superdome +0.046 vs mean on 45-yd difficulty). ([Clark PDF](https://aaronwj.engin.umich.edu/wp-content/uploads/sites/546/2021/09/Clark-Johnson-Stimpson-2013.pdf)) |
| 7 | **Weather: cold / wind / precipitation (make-rate)** | **A (make%) / B (fantasy)** | Cold, wind, precip ↓ make probability (esp. long kicks) | Clark et al. logistic model (11,896 FGs 2000–11): cold (<50°F) β=−0.341, wind ≥10 mph β=−0.140, precip β=−0.280 (all p≤0.011); turf + altitude help. Burke (Advanced NFL Stats): ~**30°F ≈ 5 yards** of distance; 52-yd ~55% moderate vs ~30% at ≤30°F. ([Burke temp](http://www.advancedfootballanalytics.com/2012/01/temperature-and-field-goals.html)). Lopez (StatsbyLopez): 50-yd success ~70%→50% in extreme cold; windchill −25 ≈ **10 yards** of difficulty. ([Lopez 2016](https://statsbylopez.com/2016/01/08/it-sucks-to-kick-in-the-cold/)). **Fantasy translation:** reduces long-tier EV and attempt willingness — magnitude of weekly fantasy delta is **not** cleanly published as a single FP number → grade B for fantasy pts. |
| 8 | **Altitude (Denver / ≥4000 ft)** | **B–C** | ↑ make range (~+5 yards); ↑ make odds | Burke: Denver visitor kicks ≈ **+5 yards** range vs other outdoor stadia (41–80°F). Clark: altitude β=+0.694. Fantasy impact for weekly streaming outside DEN is usually N/A. |
| 9 | **Passing volume / third-down conversion** | **B** | Higher pass volume & 3rd-down% associated with top-K finishes | 4for4: 2024 — 9 of top-13 Ks from top-half pass-attempt offenses; multi-year tables linking top-K finishes to top-half / top-10 3rd-down efficiency — with explicit caveat that **elite** 3rd-down offenses may convert TDs and leave only XP. |
| 10 | **Opponent points allowed / opponent FG fantasy pts allowed (aFPA)** | **B** | Weaker defenses → more opp K opportunity | Fantasy Nerds: bottom-5 defenses vs Ks allowed **33.6** FGA vs top-5 **20.1**; claims defense matchup gap (pts-allowed rank spread) slightly larger than offense gap. 4for4 weekly streaming uses **aFPA**. **Caution:** opponent “FG rate allowed” as a standalone residual after offense quality is **weakly documented** in public free sources → do not over-weight. |
| 11 | **Kicker make % / long-range skill** | **B** | Positive but secondary | Winks FG% corr **0.44**; RotoViz: accuracy as **tie-breaker**, skill “typically less predictive” than team measures. RotoWire: elite range expands coach trust for 50+ tries (Aubrey / Little / Reichard effect). |
| 12 | **Game total (O/U) as raw total** | **B** | Higher O/U helpful mainly via each side’s ITT | FFB Myers 2022 table: high O/U weeks often 10+ **unless** large underdog share of the total. Prefer **team** total over game total alone. |
| 13 | **Home / away** | **C–D** | Negligible for fantasy pts | Fantasy Index: **+0.32** home over 10 years; 2 of 10 seasons road higher. Clark: **away game not significant** for make probability (p=0.501). |
| 14 | **Pace of play** | **D** | UNKNOWN net fantasy effect | RotoWire notes Dallas pace/volume as Aubrey context, but **no published correlation coefficient** for pace → K fantasy PPG found in this research pass. Treat as speculative proxy for first downs / plays. |
| 15 | **Blowout script (XP feast vs FG volume)** | **C** | Mixed | Positive script / winning → more K pts overall (Fantasy Index win/loss). Extreme TD efficiency (Bills/Eagles profile per RotoWire) can be **PAT-heavy** and poor for fantasy despite wins. NBC: positive/neutral script good for FGA continuity; trailing chase scripts may abandon FGs. |
| 16 | **Short week / backup K / illness-limited range** | **D** | Backup / limited range usually ↓ EV | No rigorous multi-year study found quantifying Thursday-night or backup-K fantasy deltas. Process rule = treat as **haircut to distance tiers + attempt trust** (see §4). Label speculative. |

### ITT calculation (standard)

From Fantasy Footballers:

\[
\text{Favorite ITT} = \frac{O/U}{2} + \frac{|\text{spread}|}{2},\quad
\text{Dog ITT} = \frac{O/U}{2} - \frac{|\text{spread}|}{2}
\]

---

## 3) Ken mediocre-offense thesis vs high-ITT thesis

### Theses stated

| Thesis | Claim |
|--------|--------|
| **High-ITT** | Best weekly kickers attach to the **highest implied team totals** (esp. ≥27). |
| **Ken (mediocre / underperforming offense)** | Best fantasy kickers often sit on **mediocre / underperforming offenses**, not flamethrowers — because stalled drives → FGs, not only XPs. |

### What the evidence actually says

**High-ITT — SUPPORTED (primary).**

- 4for4: 10+ FP weeks **>2×** when ITT ≥27 vs ≤26 (multi-season claim).
- Fantasy Nerds: top fantasy kickers come from **high-scoring** teams (26.7 PPG avg); bottom from ~20.2; author **rejects** “too many TDs kills the kicker.”
- Fantasy Index: winners crush losers at K (+3.2 FP/g).
- Winks: offensive success metrics positively correlated (TD 0.43).

**Ken thesis — PARTIALLY SUPPORTED as a modifier, REJECTED as a substitute for high ITT.**

Supporting Ken-flavored evidence:

- Winks: **FGM corr 0.80 >> XP 0.32** → pure TD machines that never kick FGs underperform relative to FG volume.
- RotoViz / FantasyPros: **poor RZ TD rate** is an explicit positive when **paired with** high Vegas totals / drive volume.
- 4for4 caveat: “the very best offenses should be converting third downs to find that end zone, so sometimes you’ll only get one point instead of three or more.”
- NBC / Winks: **conservative 4th-down coaches** + solid defenses (HOU Fairbairn, LAC Dicker/Harbaugh, SEA Myers) create FGA volume without needing a historic offense.
- RotoWire: Bills/Eagles-type winners can be **fantasy-poor** PAT factories; ITT “don’t carry as much weight relative to even 3–4 years ago” vs indoor elite legs.

Contradicting a strong Ken reading (“prefer mediocre offenses over flamethrowers”):

- Fantasy Nerds: top-5 kickers **almost never** from bottom-half offenses; prefers good offense **and** notes bad defense matchups.
- Dead / truly low-ITT offenses fail the Fantasy Index win filter and the 4for4 27+ threshold.

### When each wins (operational)

| Environment | Prefer | Why (cited) |
|-------------|--------|-------------|
| ITT **≥27**, any offense quality | **High-ITT first** | 4for4 doubling rule for 10+ weeks |
| ITT **24–27**, poor RZ TD% / conservative HC | **Ken modifier wins** | RotoViz combo; FantasyPros inverse RZ; Winks FG>XP |
| ITT **≤20–21**, “mediocre” but never in FG range | **Neither — sit/stream elsewhere** | Fantasy Nerds bottom-K profile (~20 PPG teams); low win probability |
| Elite TD% + aggressive 4th downs + outdoor (Bills/Eagles archetype) | Fade relative to ITT peers | RotoWire PAT-heavy note |
| Elite long-range K + dome, ITT only low-20s | Can still be viable stream | RotoWire: indoor elite K “top fantasy play… even if… low 20s” |

### Verdict on Ken thesis

**MIXED.**

High-ITT has the strongest published quantitative weekly signal (4for4 ≥27 threshold; Fantasy Nerds scoring-team composition; Fantasy Index win/loss). Ken’s insight is **real but conditional**: among offenses that already generate scoring-range drives, **lower RZ TD conversion / less 4th-down aggression / FG-heavy philosophy** improves fantasy leverage because FGs dominate XP in correlation space (Winks 0.80 vs 0.32). Preferring a **genuinely mediocre offense that rarely enters FG range** over a high-ITT flamethrower is **not** supported and is contradicted by Fantasy Nerds and 4for4.

**Sweet spot (evidence-based):** Moderate-to-high ITT (**≳24–27**) + drive volume + **not**-elite RZ TD% + non-hyper-aggressive HC — not “bad offense” alone.

---

## 4) Stream vs season-hold decision rules

### Default posture (published consensus)

| Format | Default | Sources |
|--------|---------|---------|
| Redraft / seasonal with waivers | **Stream** weekly; draft K last round if at all | 4for4, RotoViz, Fantasy Footballers, Fantasy Nerds |
| Best ball | Season-hold by construction; draft volume/3rd-down/ITT proxies | 4for4 |
| Elite anchors (Aubrey / Fairbairn / Dicker / Myers tier) | Optional season-hold; RotoWire estimates streaming EV ≈ **9.0** Yahoo FP/w vs Aubrey ~**10.4** historical (~1.2–1.5 edge) | RotoWire 2026 |

### Stream rules (black/white where evidence supports)

1. **Primary filter:** Prefer available K with **highest ITT**; treat **≥27** as strong positive (4for4).  
2. **Secondary:** Favorite or likely winner (Fantasy Index).  
3. **Tertiary:** Dome/retractable (RotoWire ~0.6–0.9 FP); avoid severe cold/wind/precip when outdoor long kicks matter (Clark/Burke/Lopez).  
4. **Quaternary:** Poor own RZ TD% + conservative HC (RotoViz / FantasyPros / Winks −0.13).  
5. **Tie-breaker:** Individual FG% / proven range (RotoViz).  
6. **Do not** draft K early solely on name unless pursuing Aubrey/Dicker-class edge in standard scoring (RotoWire opportunity-cost discussion).

### Season-hold rules

Hold a rostered K week-to-week when:

- ITT still competitive with best available streamer **and**
- No hard failure mode (see §5) **and**
- League-specific swap threshold not cleared (Quantum Blitz prior memo: Net EV ≥ **+1.0** after drop cost; SPEC second-K ≥ **+3.0**).

### Illness / limited long-range (Pineiro-type) — how the calc changes

Published sources do **not** provide a calibrated “illness haircut” table. Process (transparent, assumption-labeled):

1. Start from **full-duty** projection consensus.  
2. If beat reports say **will kick** but range may be limited: zero or down-weight **50+** (and possibly 40–49) buckets in distance projections.  
3. Under ESPN scoring, each lost 50–59 make costs **5** projected points × P(attempt). Prior Sigma W2 memo used CBS buckets → **−2.0** haircut for zeroing 0.4 expected 50+ makes.  
4. Optional: slight XP haircut if offense game-scripts fewer TDs due to conservative play-calling with shaky K — **speculative** unless reported.  
5. Re-rank limited μ vs streamers; apply league Net EV threshold.

**Backup K:** Treat as unknown make%/range until sample exists; default to **large discount** vs starter projection. No published FP delta found → UNKNOWN magnitude.

---

## 5) Failure modes

| Failure mode | Mechanism | Evidence |
|--------------|-----------|----------|
| **High ITT → TDs not FGs** | Elite RZ TD% + 4th-down aggression → XP-heavy, low FGA | Winks FG vs XP corr; RotoWire Bills/Eagles; 4for4 elite-offense caveat; FantasyPros inverse RZ scoring |
| **Low ITT never enters FG range** | Drives stall before FG range; few XP too | Fantasy Nerds bottom-K ~20 PPG teams; 4for4 ≤26 halves 10+ rate |
| **Wind / cold / precip** | Lower make%; fewer long attempts attempted | Clark βs; Burke; Lopez; NBC caution on cold-weather Ks |
| **Backup / injured / limited-range K** | Miss risk + coaches decline 50+ / maybe 40+ | Logical; **quantitative fantasy delta UNKNOWN** |
| **Short week** | Less prep; weather volatility on TNF — | **Insufficient published fantasy-specific evidence** → UNKNOWN |
| **Hyper-favorite blowout** | Can be XP feast (good floor) or opponent collapse with weird script | Mixed; win still strong (Fantasy Index) but FG variance rises |
| **Opponent “good vs K” / elite defense** | Suppresses scoring-range drives | Fantasy Nerds defense table; don’t override dead own ITT |

---

## 6) Actionable weekly checklist

### Pre-lock checklist (ordered)

| Step | Check | Threshold | Evidence label |
|------|-------|-----------|----------------|
| 1 | Compute **ITT** for each candidate | **Prefer ≥27**; competitive band **24–26.5**; fade **≤20** unless elite indoor leg (RotoWire exception) | **Evidence-backed** (4for4 27+; Fantasy Nerds; FFB) |
| 2 | Note **spread / favorite** | Prefer favorite / likely winner | **Evidence-backed** (Fantasy Index) |
| 3 | Venue | **Dome/retractable > outdoor**; outdoor OK if mild | **Evidence-backed** (RotoWire split) |
| 4 | Weather (outdoor only) | Soft fade if **temp <50°F** and/or **wind ≥10 mph** and/or precip (Clark categories); hard fade extreme cold + long-kick dependency | **Evidence-backed for make%**; **SPECULATIVE FP cut** (e.g., −0.5 to −1.0) without league model |
| 5 | Own RZ TD% / HC aggression | Prefer stalled RZ + conservative 4th downs **given** Step 1 pass | **Evidence-backed as modifier** (RotoViz, FantasyPros, Winks) |
| 6 | Opp scoring defense / aFPA | Prefer soft defenses as tie-breaker | **Evidence-backed directional** (Fantasy Nerds); don’t override ITT |
| 7 | K health / range / long-range trust | Full duty > limited > backup | **Process rule**; haircut math **assumption-labeled** |
| 8 | Compare μ_streamer − μ_rostered − drop_penalty | League rule: Quantum Blitz **SWAP iff Net EV ≥ +1.0** | **League rule** (not universal literature) |
| 9 | Home/away | Ignore unless tie-break | **Evidence-backed weak** (Fantasy Index ~0.3) |
| 10 | Pace | Do not use as primary | **UNKNOWN / speculative** |

### Black/white ITT bands (for Blitz)

| ITT band | Action bias |
|----------|-------------|
| **≥27** | Strong stream / start candidate (4for4) |
| **24–26.5** | Viable if dome / FG-friendly HC / soft opp |
| **21–23.5** | Only with elite K traits + indoor or exceptional matchup |
| **≤20** | Default fade for streaming (Fantasy Nerds low-scoring profile) |

---

## 7) LIVE apply — Week 2 late slate (Sep 20, 2026 CT)

**Inputs are those already gathered for Sigma (do not invent new projs).**  
**Prior Sigma verdict:** HOLD Pineiro (streamer − limited − λ\*drop fails +1.0). Re-evaluate with this framework.

### Candidate board (given)

| Kicker | Venue / slate | Blend μ | ITT (given) | Framework flags |
|--------|---------------|---------|-------------|-----------------|
| **Eddy Pineiro (SF)** | vs MIA · 3:25 CT · outdoor | Full **9.36** (ESPN 9.92, FP 8.8); limited no-FG≥50 **8.15**; no50+ & −1XP **7.15** | **SF ~29.5** / MIA ~16.0 (Sharp) | ITT **≫27** (A-signal); favorite implied; mild outdoor assumed from prior memo weather — not re-fetched here |
| Drew Stevens (WAS) | @ DAL 3:25 CT | **7.35** | WAS **~18–19** | ITT **≤20** fade band; dog-ish total |
| Spencer Shrader (IND) | @ KC 7:20 outdoor | **7.00** | IND **~20** | ITT border fade; outdoor @ Arrowhead (Clark: harder stadium historically) |
| Matt Gay (LV) | @ LAC 3:05 outdoor | **5.85** | LV **18.25** | Low ITT |
| Riley Patterson (MIA) | @ SF 3:25 | **5.75** | MIA **16.0** | Very low ITT |
| Chad Ryland (ARI) | vs SEA 3:25 dome | **5.40** | ARI **18.5** | Dome helps (RotoWire) but ITT still low; μ lowest |

### Checklist pass

1. **ITT:** Only Pineiro clears **≥27** (29.5). All FA streamers sit at **≤20** — Fantasy Nerds / 4for4 fade territory for offense quality.  
2. **Favorite/win:** SF heavy favorite vs MIA (spread context from FantasyPros W2 table: SF −12.5 in their sheet) → Fantasy Index win filter favors Pineiro side.  
3. **Dome:** Only Ryland; insufficient to overcome 18.5 ITT + 5.40 μ.  
4. **Ken modifier:** Does **not** rescue Stevens/Shrader/Gay/Patterson/Ryland — low ITT means the “mediocre offense FG feast” path lacks drive-to-scoring-range volume. Ken thesis would require mid/high ITT + poor RZ TD%; these ITTs fail the volume gate.  
5. **Pineiro limited duty:** Even **worst given** limited μ (**7.15**) vs best FA Stevens (**7.35**) → raw edge **+0.20**. Versus limited **8.15**, Stevens is **−0.80**. No streamer clears **+1.0** raw, let alone after any drop penalty.  
6. **Failure-mode check on HOLD:** High SF ITT could cannibalize into TDs (Ken risk). Mitigant: Winks still gives TD corr +0.43 and Fantasy Nerds prefers scoring teams; XP floor from ~3 projected TDs still supports mid/high single digits. Limited long range removes 50+ upside but SF ITT 29.5 still implies multiple XP + short/mid FG chances.

### Verdict

# **HOLD — Eddy Pineiro**

**One line:** Framework re-affirms HOLD — SF ITT ~29.5 is the only A-grade environment on the late board; best FA (Stevens 7.35 @ WAS ITT ~18–19) cannot clear +1.0 vs even worst-case limited Pineiro (7.15), and Ken’s mediocre-offense lean does not apply when streamer ITTs never clear the volume gate.

**Do not revise** prior HOLD absent new injury ruling that Pineiro **will not kick** (then stream Stevens as least-bad FA by μ, accepting low-ITT risk).

---

## Sources actually used (URLs)

1. https://support.espn.com/hc/en-us/articles/360003914032-Scoring-Formats — ESPN standard K scoring  
2. https://sports.yahoo.com/fantasy/article/fantasy-football-yes-its-time-for-hayden-winks-kicker-deep-dive-for-2026-143423456.html — Winks correlations (FG 0.80, XP 0.32, TD 0.43, FG% 0.44, 4th −0.13)  
3. https://www.4for4.com/2025/preseason/debunking-randomness-kickers-fantasy-football — ITT correlation; ≥27 → 10+ weeks >2×; pass volume; 3rd down  
4. https://www.4for4.com/2024/preseason/debunking-randomness-kickers-fantasy-football — prior-year same methodology  
5. https://sports.yahoo.com/article/2025-fantasy-football-strategy-tips-kicker-scoring-is-not-random--heres-why-143427882.html — Yahoo/4for4 reprint  
6. https://www.thefantasyfootballers.com/analysis/the-art-of-streaming-fantasy-football-kickers-like-a-wall-street-trader/ — Vegas primary; ITT formula; dome; coaching aggression  
7. https://www.rotoviz.com/2020/09/streaming-kicker-week-1/ — high Vegas + pass + poor RZ TD formula; stream over draft  
8. https://www.fantasynerds.com/news/article/694/fantasy-kicker-math — top/bottom K offense PPG 26.7 vs 20.2; rejects TD-cannibalization as reason to prefer bad offenses; defense matchup tables  
9. https://fantasyindex.com/2024/05/22/factoid/kickers — home 7.25 vs away 6.93; win 8.68 vs loss 5.49 (2014–23)  
10. https://www.rotowire.com/football/article/2026-fantasy-football-draft-strategy-kickers-rankings-and-draft-strategy-130303 — dome 9.1 vs outdoor 8.2; streaming ~9.0; Bills/Eagles PAT-heavy; indoor elite K @ low-20s ITT  
11. https://www.nbcsports.com/fantasy/football/news/fantasy-football-kicker-strategy-2026-rankings-tiers-and-how-to-find-an-edge — FGA opportunity; coach aggression; positive script; Pineiro/Shanahan note  
12. https://www.fantasypros.com/2026/09/fantasy-football-kicker-rankings-start-sit-advice-week-2-2026/ — K Score; inverse RZ EFF definition; W2 lines context  
13. https://aaronwj.engin.umich.edu/wp-content/uploads/sites/546/2021/09/Clark-Johnson-Stimpson-2013.pdf — Clark et al. logistic FG model (distance, cold, wind, precip, turf, altitude; home/pressure NS)  
14. http://www.advancedfootballanalytics.com/2012/01/temperature-and-field-goals.html — Burke temperature ≈5 yards / 30°F  
15. http://www.advancedfootballanalytics.com/2013/01/altitude-and-field-goals.html — Burke Denver ≈+5 yards range  
16. https://statsbylopez.com/2016/01/08/it-sucks-to-kick-in-the-cold/ — Lopez cold/windchill distance equivalence  
17. https://conormclaughlin.net/2025/01/visualizing-nfl-kicker-accuracy-trends-1999-2024/ — long-range make-rate improvement context (1999–2024)  
18. https://www.4for4.com/2026/w1/fantasy-football-kicker-streaming-week-2-bass-fantasy-points-please — W2 streaming practice; aFPA usage  

**Internal prior (numbers only, not literature):** `/workspace/fantasy/quantum-blitz/results/sigma/w2-k-swap.md` — cross-check; **W2 apply in §7 uses the user-delegated projection set**, not a re-pull.

---

## Gaps / unknowns (do not fill)

1. **Pace → K fantasy PPG:** no published correlation coefficient found.  
2. **Short-week (TNF) fantasy delta:** insufficient evidence.  
3. **Backup-K expected FP haircut:** no calibrated study found.  
4. **Illness / limited-leg haircut:** assumption-based (zero 50+ bucket); not a published medical-kicking model.  
5. **Exact OOS R² for ITT vs K points:** 4for4 states “solid” correlation and the ≥27 doubling rule but does not publish r in free text.  
6. **Opponent FG% allowed as residual predictor** after controlling for opponent offense quality: directional only.  
7. **Play-calling aggressiveness continuous metric → FP:** only Winks −0.13 on optimal go-for-it rate.  
8. **Home/away make%:** Clark finds NS; Fantasy Index small FP gap — do not treat as edge.  
9. **Sharp Football Analysis long-form K thesis article:** not retrieved beyond ITT line usage in prior Sigma memo.  
10. **NumberFire / PFF / Establish The Run dedicated K correlation papers:** not successfully retrieved with usable numbers this pass.  
11. **2024–25 league-wide FG% by ESPN distance tiers:** PFR fetch timed out; Conor McLaughlin shows trend improvement but not a single 2024 bucket table transcribed here.

---

*Sigma desk · k-strategy.md · 2026-09-20 CT · invent-nothing research pass*
