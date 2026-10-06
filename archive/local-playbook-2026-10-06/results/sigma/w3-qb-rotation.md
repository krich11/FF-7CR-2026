# Quantum Blitz — QB rotation test: Murray + pocket QB (Mayfield or Brissett)
Written Fri Sep 25 2026 ~9:10 PM CT. Read-only. Invent-nothing; `UNK` = not found. Brissett is on our roster (roster.json 8:36 PM sync). Mayfield is on another team.

## Definitions (transparent)
- **Fantasy pts:** nflverse `fantasy_points_ppr` (4-pt pass TD, 0.04/pass yd, -2 INT, 0.1/rush yd, 6/rush TD, -2 fumble lost). Only games with **≥15 pass attempts** count (removes relief and injury-exit games). [S1][S2]
- **Funnel (per season, full-season defense, from nflverse player-week stats):**
  - Pass EPA allowed per dropback = opposing QBs' `passing_epa` / (attempts + sacks).
  - Rush EPA allowed per carry = all opponents' `rushing_epa` / carries.
  - Rank each 1 (best) to 32 (worst). **PASS funnel** if pass-EPA rank > rush-EPA rank (relatively weaker vs the pass), else **RUN funnel**.
  - 2025 uses the full 18-week season. 2026 uses only 2 games per defense, so the 2026 labels are noise-level.
  - 2025 PASS funnels: ARI, BAL, CAR, DAL, GB, IND, KC, LAC, LV, NO, NYJ, SEA, SF, TB, TEN, WAS.
- **Baseline FP/g** = 0.75 × 2025 PPR/g + 0.25 × 2026 PPR/g (≥15-att games only). Murray has no qualifying 2026 game, so he uses 2025 only.
  - Murray 15.56 (2025, n=5)
  - Mayfield 0.75×16.00 (n=17) + 0.25×11.91 (n=2) = **14.98**
  - Brissett 0.75×18.94 (n=12) + 0.25×11.49 (n=2) = **17.08**
- **Expected pts** = baseline × defense multiplier.
  - **Raw:** multiplier = opponent's 2026 ESPN QB FP allowed per game / league avg (17.05). ESPN positionAgainstOpponent, 2 games. [S3]
  - **Regressed:** multiplier = 0.3 × raw + 0.7 × (opponent's 2025 full-season QB PPR allowed per game from nflverse / league avg 16.30). This is ~70% regression toward the 2025 prior. [S2]
  - **ESPN:** ESPN public weekly projections (default PPR, kona_player_info, fetched 9:05 PM CT). [S4]
- **Rule:** start whichever QB has the higher expected pts. **Gain** = Σ(chosen − Murray) over weeks where both play. Excluded weeks:
  - MIN bye W6: the pocket QB starts regardless, so it's reported separately.
  - Pocket-QB byes: TB W10, ARI W14 (Murray starts by default).

## 1) Splits vs funnel (≥15-att games; same-season defense label)
| QB | Season | PASS-funnel: n · FP/g · pass yd · pass TD · rush yd | RUN-funnel: n · FP/g · pass yd · pass TD · rush yd |
|---|---|---|---|
| Murray | 2025 | **5** · 15.56 · 192.4 · 1.20 · 34.6 | **0** · — |
| Murray | 2026 | 0 (W1 exit, 5 att) | 0 |
| Mayfield | 2025 | 8 · 14.95 · 210.5 · 1.12 · 27.8 | 9 · 16.93 · 223.2 · 1.89 · 17.8 |
| Mayfield | 2026 | 1 · 11.64 · 216 · 0 · 30 | 1 · 12.18 · 182 · 1 · 29 |
| Brissett | 2025 | 6 · 21.04 · 311.8 · 2.00 · 15.7 | 6 · 16.83 · 249.2 · 1.83 · 12.0 |
| Brissett | 2026 | 1 · 16.48 · 277 · 1 · 14 | 1 · 6.50 · 95 · 1 · 7 |
| **Mayfield both yrs** | | 9 · 14.58 · 211.1 · 1.00 · 28.0 | 10 · 16.45 · 219.1 · 1.80 · 18.9 |
| **Brissett both yrs** | | 7 · 20.39 · 306.9 · 1.86 · 15.4 | 7 · 15.36 · 227.1 · 1.71 · 11.3 |

Reading: Murray's entire sample is 5 games, all against PASS-funnel defenses, so he has no run-funnel split. Brissett scored +5.0 FP/g better vs pass funnels (n=7 vs 7). Mayfield was actually better vs RUN funnels (+1.9, n=10 vs 9), so the "pocket QB for weak pass D" story fits Brissett's history, not Mayfield's. Every cell is n ≤ 10, which is small.

## 2) W4–W17 grid
Byes: MIN W6, TB W10, **ARI W14** (ESPN pro schedule [S3]). Pick codes: M = Murray, P = pocket QB, P* = Murray on bye.

| Wk | Murray (MIN) opp · d26 avg/rk · d25 FP/g · 2025 funnel · E raw / E reg / ESPN | Mayfield (TB) same | Brissett (ARI) same | Pick M+May (raw/reg/ESPN) | Pick M+Bris (raw/reg/ESPN) |
|---|---|---|---|---|---|
| 4 | vs MIA · 21.04/#26 · 18.16 · RUN · 19.2 / 17.89 / 20.27 | vs GB · 17.21/#17 · 15.01 · PASS · 15.12 / 14.19 / 17.03 | @NYG · 20.69/#25 · 18.25 · RUN · 20.72 / 19.6 / 14.61 | M/M/M | P/P/M |
| 5 | @NO · 15.62/#14 · 14.0 · PASS · 14.25 / 13.63 / 17.36 | @DAL · 25.04/#28 · 23.33 · PASS · 21.99 / 21.6 / 16.21 | vs DET · 32.01/#32 · 18.23 · RUN · 32.06 / 22.99 / 16.04 | P/P/M | P/P/M |
| 6 | BYE | vs PIT · 6.87/#1 · 18.79 · RUN · 6.03 / 13.9 / 15.63 | @LAR · 12.22/#6 · 15.16 · RUN · 12.24 / 14.79 / 12.88 | P*/P*/P* | P*/P*/P* |
| 7 | vs IND · 26.97/#30 · 16.9 · PASS · 24.61 / 18.67 / 19.29 | @CAR · 18.33/#20 · 13.82 · PASS · 16.1 / 13.72 / 17.05 | vs DEN · 13.91/#10 · 14.2 · RUN · 13.93 / 14.59 / 13.23 | M/M/M | M/M/M |
| 8 | @DET · 32.01/#32 · 18.23 · RUN · 29.2 / 20.94 / 18.5 | vs ATL · 18.11/#19 · 16.32 · RUN · 15.91 / 15.27 / 17.92 | @DAL · 25.04/#28 · 23.33 · PASS · 25.08 / 24.63 / 14.35 | M/M/M | M/P/M |
| 9 | vs BUF · 23.12/#27 · 13.09 · RUN · 21.09 / 15.07 / 19.52 | @CHI · 20.08/#24 · 18.13 · RUN · 17.64 / 16.95 / 17.04 | @SEA · 8.16/#2 · 14.0 · PASS · 8.17 / 12.72 / 12.11 | M/P/M | M/M/M |
| 10 | @GB · 17.21/#17 · 15.01 · PASS · 15.7 / 14.74 / 17.55 | BYE | vs LAR · 12.22/#6 · 15.16 · RUN · 12.24 / 14.79 / 13.69 | M/M/M | M/P/M |
| 11 | @SF · 9.0/#5 · 17.11 · PASS · 8.21 / 13.89 / 17.21 | @DET · 32.01/#32 · 18.23 · RUN · 28.12 / 20.16 / 17.08 | @KC · 8.42/#3 · 15.08 · PASS · 8.43 / 13.59 / 13.77 | P/P/M | P/M/M |
| 12 | vs ATL · 18.11/#19 · 16.32 · RUN · 16.52 / 15.86 / 19.43 | vs CAR · 18.33/#20 · 13.82 · PASS · 16.1 / 13.72 / 17.87 | vs WSH · 27.24/#31 · 19.56 · PASS · 27.28 / 22.53 / 16.35 | M/M/M | P/P/M |
| 13 | vs CAR · 18.33/#20 · 13.82 · PASS · 16.72 / 14.25 / 19.4 | vs LAC · 18.35/#21 · 12.58 · PASS · 16.12 / 12.93 / 16.82 | vs PHI · 18.84/#22 · 14.53 · RUN · 18.87 / 16.32 / 13.86 | M/M/M | P/P/M |
| 14 | @NE · 8.79/#4 · 14.7 · RUN · 8.02 / 12.23 / 16.45 | @BAL · 15.71/#15 · 17.71 · PASS · 13.8 / 15.53 / 14.97 | BYE | P/P/M | M/M/M |
| 15 | vs DET · 32.01/#32 · 18.23 · RUN · 29.2 / 20.94 / 19.39 | vs NO · 15.62/#14 · 14.0 · PASS · 13.72 / 13.12 / 16.71 | vs NYJ · 12.75/#9 · 19.95 · PASS · 12.77 / 18.46 / 14.52 | M/M/M | M/M/M |
| 16 | vs WSH · 27.24/#31 · 19.56 · PASS · 24.85 / 20.52 / 19.76 | @ATL · 18.11/#19 · 16.32 · RUN · 15.91 / 15.27 / 17.11 | @NO · 15.62/#14 · 14.0 · PASS · 15.64 / 14.96 / 14.05 | M/M/M | M/M/M |
| 17 | @NYJ · 12.75/#9 · 19.95 · PASS · 11.63 / 16.82 / 16.9 | vs LAR · 12.22/#6 · 15.16 · RUN · 10.73 / 12.97 / 15.54 | vs LV · 12.29/#7 · 16.09 · PASS · 12.31 / 15.49 / 15.59 | M/M/M | P/M/M |

### Gains (Σ chosen − Murray, weeks both play; W6 excluded)
| Pair | Raw 2026 D | Regressed D | ESPN weekly |
|---|---|---|---|
| Murray + Mayfield | **+33.43** (pocket W5, W11, W14) | **+19.42** (W5, W9, W11, W14) | **0.00** (Murray higher every week) |
| Murray + Brissett | **+33.14** (W4, W5, W11, W12, W13, W17) | **+23.55** (W4, W5, W8, W10, W12, W13) | **0.00** |

W6 (MIN bye) fill-in, Mayfield vs Brissett: raw 6.03 vs 12.24 (Mayfield hosts PIT, #1 vs QB) · regressed 13.90 vs 14.79 · ESPN 15.63 vs 12.88.

Matchup-specific pocket starts (both defense versions agree):
- W5: Murray @NO (#14) vs Mayfield @DAL (#28) or Brissett vs DET (#32).
- W11: Murray @SF (#5) vs Mayfield @DET (#32).
- W12–13: Brissett vs WSH (#31) and PHI (#22).
- W14: Murray @NE (#4) vs Mayfield @BAL. Brissett is on bye W14.

ESPN's own projections never pick the pocket QB over Murray in W4–17 (min Murray edge: W14 16.45 vs Mayfield 14.97).

## 3) Mayfield's edge over Brissett vs Meyers' cost
**Edge = gain(M+Mayfield) − gain(M+Brissett):**
| | Raw | Regressed | ESPN |
|---|---|---|---|
| Excluding W6 | +0.29 | −4.13 | 0.00 |
| Including W6 fill-in | −5.92 | −5.02 | +2.75 |

**Meyers' marginal value (ESPN weekly):** I ran a weekly lineup optimizer on our roster. Slots: 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE). Pool: Achane, Etienne, Allgeier, Jacobs, London, Wilson, Shaheed, Meyers, Pittman, Bateman, Pitts, Goedert. I compared the ESPN-projected lineup total W4–17 with and without Meyers (Bateman is the next body in).
- Pittman healthy: **+1.84** (only W11, when London and Shaheed are both on bye)
- Pittman OUT ROS: **+1.95**
- Jacobs out ROS (with or without Pittman): same +1.84 / +1.95
- The raw ROS gap Meyers − Bateman (131.9 − 104.4 = 27.5) mostly doesn't reach our lineup, because Shaheed out-projects Meyers every week (10.0–10.9 vs 9.1–9.9).
- Not modeled: injury-replacement value if a starting WR gets hurt.

**Verdict:** Mayfield's edge over Brissett is between −5.9 and +2.8 pts ROS depending on method, i.e. about zero. Meyers' modeled cost is ~2 pts, which is also about zero. The rotation itself adds something only under the matchup models (+19 to +34 pts ROS for either pocket QB). ESPN's projections add 0. We already have Brissett, and his splits fit the pocket-vs-pass-funnel idea better than Mayfield's. **Giving up Meyers (and especially Allgeier, our only healthy backup RB) for Mayfield buys nothing measurable.** If the plan is a rotation, use Brissett.

**Noise caveat (plain):** these defense numbers are 2 games old, Murray's baseline is 5 games from 2025, and every split cell has 10 or fewer games. Differences under ~10 pts ROS are well inside the noise. The regressed column is the most defensible of the matchup versions, and ESPN's own projections see no week where either pocket QB beats Murray.

## UNK
Opponent-QB injury effects and weather (not modeled); 2026 funnel labels (2 games, not used for the grid); exact Murray 2025 absence reason; Jacobs' return date (ESPN assumes W7); injury-replacement value of Meyers.

## Sources
- [S1] nflverse stats_player_week_2026: https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2026.csv
- [S2] nflverse stats_player_week_2025: https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2025.csv
- [S3] ESPN league API snapshot (local): recon/weekly/w03/raw/pro_sched.json (schedules/byes), fa_pool.json positionAgainstOpponent (2026 QB FP allowed)
- [S4] ESPN public weekly projections: https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2026/segments/0/leaguedefaults/3?scoringPeriodId=3&view=kona_player_info
- Local: roster.json, audit.log (Brissett/Bateman claims, Charbonnet drop 8:35 PM CT); prior file w3-mayfield-vs-murray.md
