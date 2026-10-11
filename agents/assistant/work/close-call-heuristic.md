# Close-call heuristic: back-trace, Weeks 1-4 (2026)

Written by Assistant, Sun Oct 11 2026, 1:45 AM CT. Asked by Ken in the QBZ War Room.

## Bottom line
**Nothing we tested credibly beats a coin flip as a tiebreaker on close calls.** The best rule we have is the boring one: **when two players are within 3 points, start the one ESPN projects higher.** It wins about 56% of close pairs (95% range 53%-59%, n = 10,390 league-wide pairs). Every alternative signal we tried was either weaker, or looked good in Weeks 2-3 and fell apart in the Week 4 holdout.

That includes the "close calls go to whoever plays more snaps" rule we adopted after Week 4. It passed in Weeks 2-3 (54%-59%) and failed in Week 4 (49%-53%). I recommend dropping it as a hard rule.

## Data and method
- ESPN `mRoster` for each week (all 12 teams, every rostered QB/RB/WR/TE): lineup slot, ESPN weekly projection, actual PPR points.
- nflverse: 2026 snap counts, weekly player stats (targets, carries), and the schedule file (Vegas spread and total → implied team total, home/away, roof).
- Every signal uses **only information available before kickoff**: prior weeks' snaps, prior weeks' usage, and the pregame Vegas lines. There is no lookahead.
- A "close pair" means two rostered players in the same week who could fill the same slot (QB with QB; RB/WR/TE as flex), are both projected at 4 or more, and are less than 3 projected points apart. A signal "wins" a pair when the player it picks outscores the other. Signals start in Week 2 because they need a prior week.
- Two pools: **team pairs** (both players on the same fantasy roster, so a real start/sit choice; n = 762) and **league pairs** (any two rostered players; n = 10,390).
- Honesty guards:
  - **Fit/test split:** Weeks 2-3 were for finding a signal. Week 4 was held out to check it.
  - **Multiple testing:** we tried 10 signals, so at least one would look good by luck alone. Simple p-values overstate the evidence, especially on league pairs, because one player appears in many pairs.
  - **Clustering:** for the main results I used a bootstrap that resamples whole NFL team-weeks, which gives more honest ranges.

## 1) Our back-trace (QBZ, Weeks 1-4, bench player within 3 pts of a starter at an eligible slot)
| Wk | Slot | Started (proj/actual) | Benched (proj/actual) | Pts lost |
|---|---|---|---|---|
| 1 | TE | Goedert 10.9/23.7 | Pitts 9.8/0.0 | 0 |
| 1 | FLEX | Pittman 12.3/8.8 | Meyers 10.4/12.2 | 3.4 |
| 1 | FLEX | Pittman 12.3/8.8 | Brooks 10.7/7.2, Tucker 10.0/4.7, Pitts 9.8/0.0 | 0 |
| 2 | TE | Goedert 10.8/1.4 | Pitts 10.4/2.5 | 1.1 |
| 2 | FLEX | Tucker 9.9/22.9 | Pitts 10.4/2.5 (projected higher), Meyers 9.8/3.8, Shaheed 8.6/6.9, Brooks 8.7/2.1, Allgeier 7.1/3.9 | 0 |
| 3 | FLEX | Bateman 8.8/5.7 | Meyers 9.3/19.4 | 13.7 |
| 3 | FLEX | Bateman 8.8/5.7 | Pittman 11.3/3.6, Shaheed 10.9/3.4 | 0 |
| 4 | RB | Henderson 9.5/4.2 | Gordon 9.0/18.0 | 13.8 |
| 4 | FLEX | Meyers 10.8/6.3 | Gordon 9.0/18.0, Pittman 9.7/3.5 | 11.7 (same Gordon points as the row above, not extra) |
| 4 | RB | Harvey 10.1/19.3 | Gordon 9.0/18.0 | 0 |
| 4 | TE | Henry 8.9/11.2 | Pitts 7.4/7.7 | 0 |
| 4 | QB | Brissett 15.9/10.4 | Murray 19.2/11.5 (gap 3.3, just outside) | 1.0 |

The real damage came from 3 calls: Week 1 flex (3.4), Week 3 flex (13.7) and Week 4 Gordon (13.8). Total is about 31 points.

**Counterfactuals on these calls:**
- *Always start the higher projection:* Week 2 flex goes to Pitts instead of Tucker (−20.4). Week 3 flex goes to Pittman instead of Bateman (−2.1). Everything else is unchanged. **Net −22.5 points vs. what we actually did.**
- *Always start the higher prior-week snap share:* Weeks 2-3 are unchanged (Tucker and Bateman had the most snaps). Week 4 puts Gordon (84% snaps) in over Henderson (37%). **Net about +13.8 points.** This is the single anecdote behind the snaps rule.
- We have about 5 genuine close choices in total. That sample is far too small to judge any rule on our own team. The league-wide pairs below are the real test.

## 2) League-wide signal tests (Weeks 2-4, close pairs)
Win rate = how often the player the signal picks outscores the other. 50% is a coin flip.

| Signal (pick the player with more/higher…) | Team pairs Wk2-4 | League Wk2-3 (fit) | League Wk4 (test) | League, honest 95% range |
|---|---|---|---|---|
| ESPN projection (baseline) | 54.3% (n=762) | 56.9% | 53.8% | **53.4%-58.7%** |
| Last week's snap share | 57.3% (n=695) | 54.1% | **49.2%** | 48.4%-56.9% |
| Season snap share | 56.4% | 54.2% | 51.2% | — |
| Snap share trend (rising) | 52.1% | 47.8% | 46.4% (*worse* than chance) | — |
| Opportunities per game (targets+carries) | 48.1% | 48.2% | 58.1% (flips sign) | — |
| Share of team opportunities | 47.0% | 47.4% | 57.9% (flips sign) | — |
| Vegas implied team total | 51.7% | 52.4% | 52.9% | 48.5%-56.6% |
| Home team | 54.8% (n=365) | 53.6% | 55.7% | 47.4%-60.9% |
| Dome game | 54.8% (n=230) | 53.3% | 57.6% | 46.7%-62.2% |
| Season actual minus projection ("running hot") | 49.5% | 51.6% | 48.9% | — |
| Combined: home, then projection | — | 55.8% | 54.4% | 51.4%-59.2% |
| Combined: home+dome, then projection | — | 55.4% | 55.2% | 51.5%-59.3% |

How to read this:
- **Snap share is a mirage so far.** It looked good in Weeks 2-3 and failed the Week 4 test. Some of its apparent edge is just ESPN already pricing snaps into the projection.
- **Usage (targets/carries) flips direction** between the fit and test weeks. That is a sign of noise, not signal.
- **"Running hot" (scoring above projection so far) has no predictive value.** ESPN already adjusts for it.
- **Home and dome point the same way in every slice (about 54-57%),** but their honest ranges include 50%. They are consistent with a small real edge and also with luck. The combined home/dome rules come out a hair *below* plain projection.

## 3) Recommendation
**Heuristic: inside a 3-point gap, start ESPN's higher projection, and only use "home game, then dome" to break near-exact ties (under about 0.5 points). Do not override the projection on snap share alone.**

- **Evidence:** higher projection wins 56% of close pairs (n = 10,390, honest range 53%-59%). It held in both the fit weeks and the holdout week. No alternative beat it.
- **Confidence:** moderate that the projection beats chance on close calls. Low that any tiebreaker adds anything; the home/dome lean is a weak prior, not a proven edge.
- **What it means in practice:** close calls are mostly luck. Expect to "lose" about 4 of every 9 of them no matter what. Spend effort on things with bigger edges: injury news before kickoff, avoiding zeros (inactive players, byes), and waiver adds.
- **Effect on our past calls:** it would have cost about 22.5 points in Weeks 1-4 (the Tucker and Bateman calls went our way against the projection). That is luck in a sample of about 5. It does not show that overriding projections is a skill.

## Caveats
- Only 3 weeks are usable (Week 1 has no prior data). The holdout is a single week. Everything here should be rechecked after Weeks 5-8.
- Pairs overlap: the same player appears in many pairs, so naive p-values would overstate evidence. The bootstrap ranges are the ones to trust.
- 10 signals were tested. With that many, one or two "significant" results at the 5% level are expected by chance.
- Weather and red-zone usage were not tested. The roof flag stands in for weather.
- Players who were inactive or got hurt mid-game are counted as-is. That is deliberate, since that risk is part of a real start/sit decision.
- Player names were matched between ESPN and nflverse by name and team. 3 relevant player-weeks did not match and were dropped from the snap signals.
