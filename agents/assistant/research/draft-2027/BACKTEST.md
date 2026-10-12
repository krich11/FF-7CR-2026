# Draft strategy backtest on the 2026 league draft
*Mon Oct 12, 2026, about 2 AM CT. Script: `backtest.py`. Results: `backtest_fixed_slot12.csv` and `backtest_montecarlo.csv`. Data comes from read-only ESPN pulls.*

## Caveats (read first)
- **Small sample.** Scoring covers Weeks 1–5 only, and **Week 5 is partial** (pulled before Monday night). This is one season and one draft.
- **ADP is circular.** The ADP used for tie-breaks, and by the simulated opponents, is ESPN's current ADP pulled Oct 11, *after* the season started. Any strategy that leans on ADP gets a hindsight boost.
- **Limited player pool.** Only the 192 drafted players are available. Players no one drafted can't be picked, and in-season waiver moves aren't modeled.
- **Two ways of scoring.** **Best-ball** credits the best possible starting lineup each week in hindsight. **Projection-set** starts whoever has the highest ESPN weekly projection, then scores what they actually earned.
- **VBD was implemented crudely.** It uses Week 1 projections minus a replacement level (QB12, RB30, WR30, TE12). A single-week projection is a poor stand-in for a season projection, so **the VBD row tests that stand-in, not VBD itself.**
- **The Monte Carlo field is weak.** In the random-order runs, the 11 opponents draft by ADP with random noise (log-normal, sigma 0.39, calibrated to how far this league's real picks strayed from ADP). Because their picks are noisier than ADP, every ADP-based strategy beats the field by about 90 points. **Compare strategies with each other, not with the field.** With 300 runs per cell, each mean has a sampling error of about ±3. The real uncertainty, one season of results, is much larger.

## Strategies and what published sources claim
| Strategy | Source | Evidence claimed |
|---|---|---|
| Zero RB / Hero RB / Robust RB | [Fantasy Football Blueprint, 10-year backtest (2026)](https://www.fantasyfootballblueprint.com/2026/07/22/we-backtested-10-years-of-fantasy-drafts-2/) | 1,320 simulated drafts. Zero RB was the worst archetype in every format (21.7% top-3 rate in PPR). In PPR, Elite TE was best (26.7%), and Robust RB was among the worst (21.7%). "The spread between best and worst is smaller than one bad hamstring." |
| Zero/Hero/Robust (2025) | [Stathole Sports, 12,000 simulated teams](https://statholesports.substack.com/p/12000-snake-draft-simulated-fantasy) | Robust RB won 2025 and Zero RB lost badly. The authors attribute this to a season with heavy RB scoring. |
| Zero RB (2021) | [Fantasy Points, 2021 strategy review](https://www.fantasypoints.com/nfl/articles/season/2021/strategy-review-zero-rb) | Zero RB was slightly ahead in 2021 and Bell-Cow RB won 2020. Top-5-ADP RBs played 53 games versus 84 for top-5 WRs over two years. |
| Hero / Zero / balanced overview | [FanDuel Research](https://www.fanduel.com/research/fantasy-football-draft-strategy-zero-rb-vs-hero-rb-vs-balanced-builds), [Fantasy Football Almanac](https://thefantasyfootballalmanac.com/2026/03/09/fantasy-football-running-back-strategy/) | Opinion pieces with no quantified test. |
| Late-round QB | [RotoBaller (2025)](https://www.rotoballer.com/is-late-round-fantasy-football-quarterback-strategy-still-viable-expert-tips-analysis-2025/1640346), [FantasySP](https://www.fantasysp.com/news/nfl/3052790/late-round-quarterback-draft-strategy-for-2024-fantasy-football) | Started by JJ Zachariason (2012). Argues QB scoring is flat and top QBs are hard to predict. Elite rushing QBs have weakened the strategy. |
| Late QB/TE, streaming | [Fantasy Six Pack](https://fantasysixpack.net/late-round-quarterback-and-tight-end-strategy/) | Only 56% of the top-12 QBs by draft position finished as QB1s (3 seasons). Mid-round TEs "not worth the price." |
| VBD / VORP | [Footballguys, Joe Bryant (1996)](https://www.footballguys.com/article/bryant_vbd?article=bryant_vbd), [Footballguys (2026)](https://www.footballguys.com/article/2026-value-based-drafting-one-strategy-behind-every-strategy), [FantasyPros](https://support.fantasypros.com/hc/en-us/articles/115005868747-What-is-value-based-drafting-What-do-player-draft-values-mean-VORP-VONA-VOLS-VBD) | A player's value is how much he outscores a baseline player at the same position. Presented as a principle, not a backtest. |
| Stacking | [Fantasy Footballers](https://www.thefantasyfootballers.com/strategy/stick-to-stacking-exploring-the-classic-boom-bust-strategy-fantasy-football/), [FanDuel Research](https://www.fanduel.com/research/fantasy-football-stacking-guide-examining-hit-rates-and-correlations-in-breakout-games) | A QB-WR stack booms 15.3% of the time versus 12.0% unstacked, and busts 24.0% versus 18.8%. Higher variance, with no claim that it raises expected points. |
| Bimodal RB, Zero WR, WR-heavy | No quantified published study found in this search | Tested as variants. |

**How each strategy was coded** (ADP breaks every tie; all strategies cap QB at 2 and TE at 2, take D/ST and K in rounds 15–16, and take no second QB before round 12):
- **ADP/BPA:** lowest available ADP.
- **Zero RB:** no RB before round 6.
- **Hero RB:** RB in round 1, no RB in rounds 2–5.
- **Robust RB:** RB in rounds 1–2.
- **Bimodal RB:** RB in rounds 1–2, no RB in rounds 3–8, open after that.
- **Zero WR:** no WR before round 6.
- **WR-heavy:** WR in rounds 1–3.
- **Late-round QB:** no QB before round 10.
- **Elite TE early:** TE in round 2 or 3.
- **Late TE:** no TE before round 10.
- **Stacking:** WRs and TEs on our QB's team move up 15 ADP spots.
- **VBD:** highest Week 1 projection above replacement.
- **Playbook 2027:**
  - no confirmed already-out player before round 14;
  - QB or TE only at or past ADP;
  - 1 QB;
  - at least one RB by round 2.

## Results
**Fixed draft:** the other 11 teams' actual picks are held fixed and QBZ drafts from slot 12 using the strategy. **Monte Carlo:** draft order is randomized and the opponents use noisy ADP, with QBZ at slot 1, 6 or 12 (300 runs each). The other 11 real 2026 rosters averaged **678.2** best-ball and **582.4** projection-set.

| Strategy | Fixed draft, slot 12: best-ball W1–5 (rank vs other 11) | Fixed: projection-set (rank) | Missed player-games | Monte Carlo best-ball, slot 1 / 6 / 12 (mean rank) | MC average | vs Playbook |
|---|---|---|---|---|---|---|
| Bimodal RB | 735.9 (3) | 630.3 (4) | 14 | 791 / 744 / 754 (1.24 / 1.91 / 1.73) | 762.9 | +22.2 |
| Late-round QB | 694.0 (5) | 564.1 (6) | 11 | 775 / 731 / 744 (1.36 / 2.38 / 2.1) | 750.2 | +9.5 |
| Hero RB | 677.6 (6) | 602.8 (5) | 14 | 772 / 733 / 740 (1.34 / 2.23 / 2.02) | 748.6 | +7.9 |
| Elite TE early | 699.2 (5) | 635.4 (4) | 13 | 771 / 729 / 738 (1.46 / 2.6 / 2.24) | 746.1 | +5.5 |
| ADP/BPA | 683.4 (6) | 623.8 (5) | 14 | 769 / 733 / 731 (1.46 / 2.49 / 2.42) | 744.5 | +3.9 |
| Stacking | 683.4 (6) | 623.8 (5) | 14 | 770 / 730 / 733 (1.38 / 2.46 / 2.41) | 744.2 | +3.5 |
| Robust RB | 712.4 (5) | 613.7 (5) | 13 | 768 / 729 / 732 (1.43 / 2.45 / 2.49) | 743.1 | +2.5 |
| Playbook 2027 | 733.6 (3) | 613.7 (5) | 15 | 765 / 722 / 736 (1.52 / 2.87 / 2.2) | 740.7 | +0.0 |
| Late TE | 683.4 (6) | 623.8 (5) | 14 | 756 / 726 / 733 (1.68 / 2.62 / 2.4) | 738.6 | -2.1 |
| Zero WR | 725.8 (5) | 657.0 (3) | 14 | 763 / 715 / 707 (1.56 / 2.87 / 3.34) | 728.3 | -12.4 |
| Zero RB | 667.8 (6) | 588.7 (6) | 13 | 741 / 712 / 725 (2.07 / 3.14 / 2.55) | 725.9 | -14.8 |
| WR-heavy | 656.8 (6) | 575.4 (6) | 13 | 726 / 710 / 714 (2.49 / 3.2 / 2.99) | 716.9 | -23.8 |
| VBD | 583.1 (12) | 542.6 (7) | 16 | 619 / 559 / 547 (8.38 / 10.86 / 11.24) | 575.2 | -165.4 |
| QBZ actual 2026 | 464.7 (12) | 421.5 (12) | 25 | – | – | – |

## Verdict
- **Every simulated strategy except VBD beat our actual 2026 draft by 200–270 points** in the fixed-slot test. Our actual draft scored 464.7 best-ball, last in the league, with 25 missed player-games. Following almost *any* coherent rule at ADP would have avoided most of that.
- **Our playbook roughly equals plain ADP.** It averaged 740.7 against 744.5 for ADP/BPA in Monte Carlo (-3.8, within noise). In the fixed slot-12 run it scored 733.6 against 683.4 (+50), but that is a single draw. **The playbook does not reliably beat ADP**, which is Blitz's cut test. Its value is as a guardrail, mainly the already-out rule, not as an edge.
- **Strategies that beat the playbook:**
  - **Bimodal RB (+22.2 average; best at all 3 slots; 735.9 fixed).** In this season, mid-round RBs flopped: Etienne, Jacobs and Achane-tier backs. Skipping RBs in rounds 3–8 avoided them. That is a season-specific outcome found in hindsight, and no published study supports it. **Low confidence.**
  - **Late-round QB (+9.5)** and **Hero RB (+7.9).** Both are close to noise for a single season.
- **Within noise (±6):** Elite TE early, ADP/BPA, Stacking, Robust RB, Late TE.
- **Clearly worse in this league-season:**
  - **WR-heavy (-23.8)**
  - **Zero RB (-14.8)**, consistent with the [10-year Blueprint study](https://www.fantasyfootballblueprint.com/2026/07/22/we-backtested-10-years-of-fantasy-drafts-2/)
  - **Zero WR (-12.4)**
- **VBD (-165)** reflects the poor Week 1 projection stand-in, not VBD as a method. Re-test it on Jan 5 with real season projections.
- **What to adopt now:** nothing new with high confidence. Two medium/low-confidence additions go into the playbook:
  1. **Avoid Zero RB and WR-heavy builds in this league.** Both our backtest and the 10-year PPR study point the same way. *Medium.*
  2. **Treat the playbook as an ADP guardrail, not an edge.** The Jan 5 rework should test Bimodal RB, Late-round QB and Hero RB on full-season data and a pre-draft ADP before adopting any of them. *Low.*
