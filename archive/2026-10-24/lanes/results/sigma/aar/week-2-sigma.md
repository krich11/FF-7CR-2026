# Sigma AAR — Week 2 (adversarial)
**Date:** 2026-09-22 CT · **Bar:** point maximization · **Lane:** our roster only  
**Sources:** ESPN `mRoster` scoringPeriodId=2 (settled), `decisions/week-2.json`, `cards/week-2.md`, `edges/shadow/week-2-preds.json`, `results/sigma/w2-k-swap.md`, nflverse `snap_counts_2026`, Blitz/Wire W2 AARs (process context only)  
**Invent nothing.** Wrote `results/week-2.json` + `results/sigma/snaps/week-2.csv` + usage-join from those sources (Mon `WEEK_REVIEW_SKIP` left them missing).

## TLDR
L 83.1–104.02 vs CDS (proj adj 109.52, Δ −26.42). Record 1–1. Wins on card: Tucker FLEX (+13.04 / +20.4 vs Pitts), Wilson (+0.84), Steelers (+1.66), Pineiro HOLD. Scars: Dart knee (−17.43), Goedert knee (−9.84), Achane/Etienne/London soft. Shadow `share_trend` paper-lost −20.4 (n_flips=1). Starter-sum 83.1 = team (reconciled).

## Model misses (what we didn’t see)
1. **Dart @ LAR (0.8 vs 18.23)** — Sole rostered QB; left opening drive L knee → Winston. Failure mode = **injury**, not SoFi roof / LAR defense fade we should have sat. Snap% 0.12 (7 snaps) confirms exit. No sit/start alt on roster.
2. **Goedert @ TEN (1.4 vs 11.24)** — Pre-lock ACTIVE; in-game QTR knee; Mon MCL “few weeks.” Only TE alt Pitts (2.5) → counterfactual **+1.1** only. Not a Fri card miss. Residual is injury luck, not TE model.
3. **Achane (12.3 vs 17.12)** — Snaps 0.76 / 6 targets — **usage OK / efficiency soft** (same class as W1 finishing noise). Do not rewrite RB role from points alone.
4. **Etienne (7.1 vs 11.0 adj)** — Kamara-active haircut already on card (consensus 12.22 → adj 11.0). Snaps 0.54. Residual partly script/committee, partly finishing; haircut direction correct, size still short.
5. **London (8.9 vs 12.85)** — Rush starts known; 5 tgt / 4 rec / snaps 0.62. Second straight week under **backup-QB environment** — direction predictable, magnitude still under-modeled vs stud WR baseline.
6. **Tucker boom (22.9 vs 9.86)** — Bowers Doubtful→inactive was on Fri card; TE2 premium rule forced FLEX. Outcome validates process; single-game TD efficiency ≠ permanent FLEX dogma.

## Predictable under/over?
| Residual | Predictable? | Covariate |
|----------|--------------|-----------|
| Tucker +13.04 | Partially | Bowers inactive / TE2 premium rule — TD variance still luck |
| Dart −17.43 | No (pre-lock) | In-game knee; SoFi roof irrelevant once exit |
| Goedert −9.84 | No (pre-lock) | In-game knee → MCL |
| London −3.95 | Direction yes / size no | Backup QB (Rush) — W1 lesson continues |
| Achane −4.82 | Weak | Usage fine; efficiency |
| Etienne −3.90 | Partial | Kamara debut haircut on card |
| Pineiro −2.02 | No | Illness resolved ACTIVE; HOLD correct vs stream Net EV −0.25 |
| Wilson +0.84 | — | On card |
| Steelers +1.66 | Partial | Porter OUT on card |

## Missing covariates (probed)
| Covariate | Used W2? | Gap |
|-----------|----------|-----|
| Weather / roof | K memo yes (Levi’s calm; SoFi canopy for Tucker) | Dart @ SoFi roof — irrelevant after knee |
| Referee tendencies | No | UNKNOWN |
| Crowd / 12th man | No | UNKNOWN |
| Travel / short week | No explicit | Dart MNF — not a sit signal |
| Game script | DST/Porter + Kamara haircut + Bowers yes | Post-game script tags still soft for form (form deferred) |
| Pace | No | UNKNOWN |
| Backup-QB env | Yes (Rush on London/Pitts rows) | Magnitude still under-modeled |
| **Snap%** | **Wired** | nflverse W2 extract OK for skill players; W1 hole mitigated for this week |

## False edges / noise
- **share_trend would keep Pitts** — lost **20.4** vs SPEC Tucker. Anti-promotion. Ledger: cum_delta −20.4, n_flips=1, n_wins=0. Stay paper; do not elevate TE-scarcity over TE2 premium when premium fails.
- **vegas_flex** — skipped (no verified W2 implied totals); correct discipline.
- Do **not** treat Tucker 22.9 as permanent FLEX lock or Goedert W1 crush as permanent TE when MCL sidelines him.
- “Should have benched Goedert/Dart” from in-game injuries = noise for start/sit calibration.

## Calc / process gaps
1. **Mon `WEEK_REVIEW_SKIP`** (MNF live 10:37 CT) never resumed → no scorecard, no form/usage update before Tue AAR. Sigma **backfilled** `results/week-2.json` + snaps/usage-join this run from ESPN settle. **Still owed:** `week-2-scorecard.md`, form.json application, Ken email (Blitz week.review makeup).
2. **form_add_next** left **null** in week-2.json — do not invent; W1 form was all 0 so W2 card correctly had form.applied=false.
3. **EXEMPT/OUT zeros** — Jacobs EXEMPT, Pittman OUT, Charbonnet PUP correctly 0 / benched.
4. **DATA_QUALITY** — starter-sum = team 83.1 OK. PFR lists Shaheed as SEA W1–W2 while Wire/schedule often frame NO context — flag only; did not change a start.
5. **Research tracks** — still unscored for W1–W2 (methodology_ready, n_flips=0). Not a live-card miss; paper cadence lag.

## Next-week process fixes (Sigma-owned)
1. After any `WEEK_REVIEW_SKIP`, treat settle as mandatory trigger to write `results/week-N.json` (done for W2) and push Blitz for scorecard/form closeout before Tue AAR.
2. Keep **backup-QB environment** haircut explicit in CARD DIFF for London/Pitts while Rush/Tua path unsettled; do not restore stud WR baseline without starter QB.
3. Score `share_trend` honestly: W2 = large loss; promotion gate untouched (need ≥6 flips / W8).
4. W3 TE default → Pitts while Goedert MCL (personnel signal for Blitz card — not Sigma ESPN write).
5. Sole-QB depth is structural risk (Dart exit); Sigma ranks add value only if Blitz asks — Murray path already Ken-typed.

## Consequential for Blitz?
1. **week.review makeup still owed** — scorecard + form/usage loop + Ken email. Sigma wrote `results/week-2.json` so residuals exist; without makeup, W3 form_add stays blind.
2. *(FYI, not promote)* share_trend −20.4 vs Tucker — stay paper.
3. *(Cleared)* W1 snap% hole — W2 nflverse extract OK.

**Consequential count: 1** (week.review makeup / Monday stack closeout).
