# SAMPLE/MOCK — Week 0 Sigma Appendix (packet v2)

> **SAMPLE/MOCK ONLY.** Fake box scores from `mock-week-0-boxscores.json`. Not Week 1. Not ESPN. Do not promote into live `form.json` / `usage.json` / `edges/shadow/ledger.json`.

## DATA_QUALITY
File `team_score` **128.4** vs sum of starter `actual` rows **121.6** (gap **6.8** unexplained). Required check on real Mondays — do not invent the missing points; reconcile or flag before Ken-facing totals.

| Metric | Value |
|--------|-------|
| File `team_score` | 128.4 |
| Sum of starter `actual` rows | 121.6 |
| Gap | 6.8 unexplained in mock file |
| File `proj_total` | 119.2 |
| Sum of starter `adj` rows | 114.3 |

Player residuals use **row-level** `adj`/`actual`. Headline W/L and opponent use **file-level** fields.

## Bench regret (both definitions)
| Def | Formula | Result |
|-----|---------|--------|
| **(a) SCORECARD** | best benched FLEX-eligible − worst started FLEX-eligible | **18.2 − 8.1 = 10.1** (Meyers − Pitts) |
| **(b) Same-position** | Meyers − Wilson (WR) | **18.2 − 9.4 = 8.8** |

Lead TLDR with (a); mention (b).

## Player residuals (actual − adj) — form_add to 2 decimals
| Player | Slot | Adj | Actual | Residual | form_add pre-boost | form_add final |
|--------|------|-----|--------|----------|--------------------|----------------|
| Jaxson Dart | QB | 18.2 | 22.4 | +4.20 | +1.47 | +1.47 |
| De'Von Achane | RB | 17.5 | 19.1 | +1.60 | +0.56 | +0.56 |
| Travis Etienne Jr. | RB | 14.3 | 11.2 | −3.10 | −1.08 | −1.08 |
| Drake London | WR | 15.0 | 16.8 | +1.80 | +0.63 | +0.63 |
| Garrett Wilson | WR | 13.9 | 9.4 | −4.50 | −1.57 | **−2.32** |
| Kyle Pitts Sr. | TE | 10.0 | 8.1 | −1.90 | −0.66 | −0.66 |
| Dallas Goedert | FLEX | 10.4 | 14.6 | +4.20 | +1.47 | +1.47 |
| Steelers D/ST | DST | 7.1 | 12.0 | +4.90 | +1.72 | +1.72 |
| Eddy Pineiro | K | 7.9 | 8.0 | +0.10 | +0.03 | +0.03 |
| Jakobi Meyers | BE | 6.2 | 18.2 | +12.00 | +3.00 (cap) | **+3.00** |
| Michael Pittman Jr. | BE | 5.0 | 7.1 | +2.10 | +0.73 | +0.73 |
| Jonathon Brooks | BE | 6.0 | 6.0 | 0.00 | 0.00 | 0.00 |
| Tre Tucker | BE | 8.0 | 5.2 | −2.80 | −0.98 | −0.98 |
| Rashid Shaheed | BE | 8.3 | 4.1 | −4.20 | −1.47 | −1.47 |
| Josh Jacobs | BE | 0.0 | 0.0 | — | EXEMPT | — |
| Zach Charbonnet | BE | 0.0 | 0.0 | — | PUP | — |

Formula: `form_add = round(clamp(0.35 × residual, ±3), 2)`.  
Boost: Meyers +1.00 (still capped **+3.00**); Wilson −0.75 → **−2.32**.

## Usage (assumed present in mock for bench only)
| Player | Assumed snap% | Actual snap% | Gap | Targets | role_mult_next | Flag |
|--------|---------------|--------------|-----|---------|----------------|------|
| Jakobi Meyers | 0.55 | 0.88 | +0.33 | 11 | **1.15** (cap) | **buy_usage** |
| Michael Pittman Jr. | 0.65 | 0.70 | +0.05 | 6 | 1.025 | — |
| Jonathon Brooks | 0.40 | 0.35 | −0.05 | 1 | 0.975 | — |
| Tre Tucker | 0.55 | 0.60 | +0.05 | 3 | 1.025 | — |
| Rashid Shaheed | 0.50 | 0.45 | −0.05 | 2 | 0.975 | — |

Starters: no assumed_snap_pct in mock → no invented `usage_gap`.

## Sources MAE → weights
| Source | MAE | Normalized weight |
|--------|-----|-------------------|
| ESPN | 3.8 | 0.467 |
| FantasyPros | 3.2 | 0.533 |

## Shadow (0 flips)
| Signal | SPEC | Shadow | Δ PPR | Flip |
|--------|------|--------|-------|------|
| vegas_flex | Dallas Goedert | Dallas Goedert | 0.0 | No |
| share_trend | — | N/A | — | No |
| dst_k_script | Steelers D/ST | Steelers D/ST | 0.0 | No |

## Artifact paths
- `results/sigma/mock-form.json` (v2)
- `results/sigma/mock-usage.json`
- `results/sigma/mock-shadow-score.json`
- `results/sigma/week-0-mock-scorecard-deep.md`
