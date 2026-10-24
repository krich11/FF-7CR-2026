# Sigma AAR — Week 1 (adversarial)
**Date:** 2026-09-20 CT · **Bar:** point maximization · **Lane:** our roster only  
**Sources:** `results/week-1.json`, `results/week-1-scorecard.md`, `decisions/week-1.json`, `cards/week-1.md`, `edges/shadow/week-1-preds.json`  
**Invent nothing.**

## TLDR
W 132.9–102.22 (proj 118.81, Δ +14.09). Wins driven by Dart (+7.64), Goedert TE flip (+12.49), Steelers (+11.6). Scars: London (−8.86), Achane efficiency dud (−7.6), FLEX Pittman vs Meyers (−3.4). Shadow `vegas_flex` paper-won +3.4 (n=1).

## Model misses (what we didn’t see)
1. **London volume collapse under Rush** — card flagged ceiling down / still start; actual 4 targets / 5.5 PPR. Residual largely **QB-environment**, not pure “WR dud.” Pitts 1 tgt / 0.0 confirms environment. Predictable *direction* (backup QB) was known; **magnitude** of target starvation was under-modeled.
2. **Achane** — touches OK (11 car / 5 tgt) but ypc cold → points miss. Usage-positive / efficiency-negative; without snap% hard to separate role vs finishing.
3. **Meyers 12.2 on 2 targets + TD** — shadow FLEX flip correct on ITT; scoring was **TD luck** on low volume (do not promote from n=1 boom).
4. **Allgeier 17 carries on bench** — Love Q noted as dart only; committee spike not priced into FLEX debate (would not have beaten Pittman 8.8? Allgeier 9.0 — *would* have edged Pittman by +0.2; missed micro-FLEX alt).

## Predictable under/over?
| Residual | Predictable? | Covariate |
|----------|--------------|-----------|
| Goedert +12.49 | Partially | Backup-QB TE flip thesis (card had it) — TD variance still luck |
| Steelers +11.6 | Partially | PIT vs Rush/ATL script in card — DST boom still high variance |
| London −8.86 | Direction yes / size no | Tua OUT / Rush — need formal backup-QB target haircut |
| Achane −7.6 | No (efficiency) | Touches fine; finishing noise |
| Meyers +2.06 vs adj | Weak | ITT favored; TD on 2 tgt = noise |
| Dart +7.64 | No | SNF boom |

## Missing covariates (probed)
| Covariate | Used W1? | Gap |
|-----------|----------|-----|
| Weather / roof | No explicit | Melbourne K DONE outdoor AU — not modeled beyond lock |
| Referee tendencies | No | UNKNOWN impact |
| Crowd / 12th man | No | UNKNOWN |
| Travel | No | Dart SNF home — not flagged |
| Game script | DST/TE yes; WR/RB soft | Need post-game script tag on residuals before form (SPEC §7.5) — W1 form_add=0 so deferred |
| Pace | No | UNKNOWN |
| **Snap%** | **Missing** | `week-1.json` snap_note: ESPN fantasy + site boxscore APIs had **no snap%** → usage→role_mult loop incomplete |

## False edges / noise
- **vegas_flex +3.4** — correct paper flip, but Meyers outcome TD-driven on 2 targets → treat as **edge signal win**, not player-role confirmation. n_flips=1 ≪ promotion gate (≥6 / W8).
- Do **not** auto-elevate Meyers over Pittman from W1 alone.
- Goedert crush ≠ permanent TE lock if Tua returns — environment-conditional.

## Calc / process gaps
1. **Snap% hole** — blocks honest usage_gap / role_mult_next (Sigma-owned fix: find public snap source before W2 Monday packet).
2. **form_add W1 = 0** by SPEC — correct; bench-vs-starter (Meyers vs London +6.7 regret) flagged for W2 window, not applied yet.
3. **Fri `resource_exhausted`** — Blitz process miss; makeup Sat still landed Goedert TE (net +23.7 vs Pitts). Sigma lane: no action beyond noting dependency on timely IR→adj.
4. **DATA_QUALITY** — starter sum = team 132.9 (reconciled in scorecard). EXEMPT Jacobs / IR Charbonnet correctly zeroed.

## Next-week process fixes (Sigma-owned)
1. Wire a snap% source into `results/sigma/` usage pipeline (or document permanent degraded mode).
2. Add **backup-QB / emergency-QB environment flag** as research covariate on pass-catcher residuals (paper track input; not live §7 without Blitz).
3. Score `vegas_flex` honestly: count flip wins separate from “role confirmed.”
4. FLEX shortlist: if Love inactive / limited, price Allgeier carries explicitly in CARD DIFF.
5. Do not overweight W1 Meyers TD when building W2 form narrative.

## Consequential for Blitz?
1. **Snap% data hole** — usage loop cannot fully run until sourced (recurring point risk).
2. *(Borderline)* vegas_flex paper +3.4 — FYI only; **no promote**.

**Consequential count: 1** (snap source).
