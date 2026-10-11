# Close start/sit calls: is there a signal that beats the higher projection?

Written for Ken by Assistant. Sun Oct 11, 2026. For review by the Consultant.
This document combines two studies:
- **Study 1:** our own league, ESPN projections, 2026 Weeks 1–4. Earlier writeup: `agents/assistant/work/close-call-heuristic.md`
- **Study 2:** Sleeper projections plus nflverse data, 2021 through 2026 Week 4, about 437,000 close pairs. Earlier writeup: `agents/assistant/work/close-call-deep.md`

Every dataset, raw source pull and script is in this folder, so the numbers can be checked without fetching anything. Column definitions are in `data/DICTIONARY.md`.

## Bottom line
- On a close call (projections less than 3 PPR points apart), **start the higher projection**. It wins about **56.6%** of close pairs on games the models never saw. The best model using 21 pre-kickoff signals wins **56.8%**, and the 95% range of that lift includes zero.
- The win rate is set almost entirely by the size of the gap. Under 1 point it's 52%, 1–2 points it's 57%, 2–3 points it's 61%.
- **Questionable tag on the higher-projected player:** lower your confidence to a coin flip and keep a later-game swap open. Do not flip the call on the tag alone.
- **More recent volume (touches over the last 3 games, last week's snap share):** a small confidence nudge (57–58% vs 55–56%). It's never enough to flip a call.
- Snap share as a tiebreaker, home/dome, implied team total, "running hot", teammates' vacated volume, matchup, rest, spread and wind: **no stable edge**.
- Real points come from avoiding zeros (inactives, early kickoffs, byes), waiver pickups, and lopsided calls where the projection hasn't caught up to news yet.

## 1. The question
Ken asked whether any information known before kickoff can turn close start/sit calls from coin flips into wins, and asked for "deep statistical analysis" after Study 1 came back negative.

## 2. Data sources (all pulled Sun Oct 11, 2026)
| Data | Endpoint | Used in |
|---|---|---|
| ESPN league rosters, slots, weekly projection and actual | `https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2026/segments/0/leagues/1776545061?view=mRoster&scoringPeriodId={1..5}` (private, needs login cookies) | 1, ESPN check |
| nflverse snap counts 2026 | `https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_2026.csv` | 1 |
| nflverse weekly player stats 2026 | `https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats_2026.csv` | 1 |
| nflverse schedule and Vegas lines | `https://github.com/nflverse/nfldata/raw/master/data/games.csv` | 1, 2 |
| nflverse injury reports 2021–2026 | `https://github.com/nflverse/nflverse-data/releases/download/injuries/injuries_{season}.csv` | 2 |
| Sleeper weekly projections | `https://api.sleeper.app/projections/nfl/{season}/{week}?season_type=regular&position[]=QB&position[]=RB&position[]=WR&position[]=TE` | 2 |
| Sleeper weekly stats (actual PPR, snaps, targets, carries) | `https://api.sleeper.app/stats/nfl/{season}/{week}?season_type=regular&position[]=...` (same filters) | 2 |
| Sleeper player database (Sleeper id to GSIS id) | `https://api.sleeper.app/v1/players/nfl` | 2 |

Copies of every raw pull are in `data/raw/`. The ESPN files contain league roster data only, with no credentials.
Note: the exact nflverse download commands for Study 1 weren't saved at the time. The URLs above are the standard nflverse release paths, and the column layout of the saved files matches them. The saved files in `data/raw/` are the ones actually used.

## 3. Quick ESPN accuracy check (league starters, 2026 Weeks 1–4)
Every starter on all 12 teams, including K and D/ST: **430 starter-weeks, correlation of ESPN projection with actual points 0.528, mean absolute error 6.04 points.**
How often the starter ESPN projected higher outscored the other, across all starter pairs in the same week:

| Projection gap | Higher projection wins |
|---|---|
| < 1.5 | 52.5% |
| 1.5 – 3 | 59.1% |
| 3 – 5 | 65.1% |
| 5+ | 79.4% |

Reproduction note: the original quick check was an ad-hoc calculation and its script wasn't saved. `scripts/study1-espn-2026/espn_accuracy.py` rebuilds it from the raw ESPN pulls and gets **432 starter-weeks, correlation 0.534, MAE 6.01**, with gap bins of 53.6% / 59.8% / 65.6% / 79.3% (pair counts 4,034 / 3,897 / 4,660 / 10,392). The small difference probably comes from 2 rows treated differently (for example, an empty slot or a projection that changed). The conclusion is the same. Data: `data/espn_2026_wk1-4_all_rostered.csv.gz`.

## 4. Study 1: our league, ESPN, 2026 Weeks 1–4
**Close pair:** two rostered players in the same week who could fill the same slot (QB with QB, RB/WR/TE as flex), both projected at 4 or more, projections less than 3 points apart, actual points not tied. Weeks 2–4 only, because the signals need a prior week.
**Two pools:** team pairs (same fantasy roster, a real choice, n = 762) and league pairs (any two rostered players, n = 10,390).
**Honesty guards:** signals were fit on Weeks 2–3, and Week 4 was held out. 10 signals were tested, so some will look good by chance. The 95% ranges come from a bootstrap that reweights whole NFL team-weeks with Poisson weights (`bs.py`), because one player appears in many pairs.

| Signal (pick the player with more/higher…) | Team pairs Wk2–4 | League Wk2–3 (fit) | League Wk4 (test) | League 95% range |
|---|---|---|---|---|
| ESPN projection (baseline) | 54.3% (n=762) | 56.9% | 53.8% | 53.4–58.7% |
| Last week's snap share | 57.3% | 54.1% | 49.2% | 48.4–56.9% |
| Season snap share | 56.4% | 54.2% | 51.2% | – |
| Snap share trend | 52.1% | 47.8% | 46.4% | – |
| Targets+carries per game | 48.1% | 48.2% | 58.1% | – |
| Share of team targets+carries | 47.0% | 47.4% | 57.9% | – |
| Vegas implied team total | 51.7% | 52.4% | 52.9% | 48.5–56.6% |
| Home team | 54.8% | 53.6% | 55.7% | 47.4–60.9% |
| Dome | 54.8% | 53.3% | 57.6% | 46.7–62.2% |
| Actual minus projection so far ("running hot") | 49.5% | 51.6% | 48.9% | – |
| Home, then projection | – | 55.8% | 54.4% | 51.4–59.2% |
| Home+dome, then projection | – | 55.4% | 55.2% | 51.5–59.3% |

Full outputs: `results/study1_an_output.txt`, `results/study1_bootstrap_output.txt`. (The rerun bootstrap output differs from the table in the third decimal because of random draws.)

### QBZ back-trace (Weeks 1–4)
Full table: `data/qbz_backtrace_2026_wk1-4.csv.gz` (24 starter-vs-bench rows within 3.5 points). The calls that cost points:

| Wk | Slot | Started (proj/actual) | Benched (proj/actual) | Pts lost |
|---|---|---|---|---|
| 1 | FLEX | Pittman 12.3/8.8 | Meyers 10.4/12.2 | 3.4 |
| 2 | TE | Goedert 10.8/1.4 | Pitts 10.4/2.5 | 1.1 |
| 3 | FLEX | Bateman 8.8/5.7 | Meyers 9.3/19.4 | 13.7 |
| 4 | RB | Henderson 9.5/4.2 | Gordon 9.0/18.0 | 13.8 |
| 4 | FLEX | Meyers 10.8/6.3 | Gordon 9.0/18.0 | 11.7 (same Gordon points, not extra) |
| 4 | QB | Brissett 15.9/10.4 | Murray 19.2/11.5 (gap 3.3) | 1.0 |

- Always starting the higher projection would have gone **−22.5 points** against what we actually did: Pitts over Tucker in Week 2 (−20.4) and Pittman over Bateman in Week 3 (−2.1).
- Always starting the higher prior-week snap share would have gone **about +13.8**, all from Gordon (84%) over Henderson (37%) in Week 4.
- There are about 5 real close choices here. That's far too few to judge any rule, which is why the league-wide and multi-season tests matter.

## 5. Study 2: 2021 to 2026, Sleeper and nflverse
**Close pair:** same week, different NFL teams, same position or both flex-eligible (RB/WR/TE), both projected at 6 or more, neither ruled Out or Doubtful before the game, Vegas line available, projections more than 0 and less than 3 points apart, actual points not tied. **437,340 pairs.** Sleeper is used because ESPN doesn't openly publish past-season weekly projections. The baseline matches Study 1 (56.6% vs about 56%).

**21 pre-kickoff signals.** Each pair uses the higher-projected player's value minus the other player's:
projection gap, implied team total, the player's share of that total, home, dome, rest difference, spread, wind, opponent's points allowed to the position in earlier weeks, Questionable, limited/missed practice, teammates' vacated targets+carries (whole team and same position group), touches over the last 3 games, touch trend, snap share (last game and last 3), running hot, volatility, change in projection, and targets over the last 3 games. Every lagged signal uses only earlier active weeks.

**Method:** train on 2021–23, validate on 2024, test once on 2025 plus 2026 Weeks 1–4 (n = 100,589). The models are an L2 logistic regression (C = 0.1, standardized, mean-imputed) and gradient-boosted trees (200 iterations, depth 3, minimum 500 samples per leaf). The 95% ranges come from a bootstrap over whole weeks (1,000 resamples), because pairs within a week are linked.

### Results on games the models never saw
| Method | Win rate | 95% range | Lift over projection (95% range) | Calls flipped |
|---|---|---|---|---|
| Higher projection (2025–26) | 56.6% | – | – | 0 |
| Logistic, 21 signals | 56.8% | 55.9–57.6% | +0.2 (−0.4 to +0.7) | 11.8% |
| Gradient-boosted trees | 56.7% | 55.9–57.5% | +0.1 (−0.4 to +0.6) | 10.7% |
| Logistic, 2026 Weeks 1–4 only | 57.4% vs 56.9% | 56.4–58.6% | +0.5 (−0.2 to +1.3) | 9.3% |
| Validation 2024, logistic | 56.3% vs 56.0% | 55.3–57.3% | +0.3 (−0.4 to +1.0) | 13.1% |

**By gap (test 2025–26):** under 1 point, 52.4% (36,689 pairs). 1–2 points, 57.3% (33,835). 2–3 points, 60.9% (30,065).

### Signal by signal
Each cell shows how often the higher projection wins when it is also higher on the signal / when it is lower on the signal, for the training years (2021–23) and the test years (2025–26). If a signal were real, the gap would be large and the same in both periods.

| Signal | Train: higher / lower | Test: higher / lower | Verdict |
|---|---|---|---|
| Implied team total | 56.6 / 56.1 | 58.7 / 54.3 | Unstable |
| Share of implied total | 56.9 / 55.3 | 55.9 / 58.2 | Reverses |
| Home | 57.4 / 55.3 | 57.7 / 55.7 | Consistent but tiny, and no help breaking near-ties (52%) |
| Dome | 57.6 / 55.1 | 57.8 / 54.7 | Same as home |
| Rest | 55.6 / 56.8 | 58.0 / 55.5 | Reverses |
| Spread | 56.2 / 56.5 | 57.9 / 55.3 | Unstable |
| Wind | 54.8 / 57.6 | 54.4 / 58.4 | Consistent: more wind is slightly worse. Small |
| Opponent points allowed | 56.0 / 56.8 | 55.6 / 57.7 | None |
| **Questionable** | **51.5 / 60.6** | **55.4 / 60.1** | Real: downgrade confidence, don't flip |
| Limited practice | 54.2 / 58.8 | 54.5 / 58.6 | Consistent, smaller cousin of Questionable |
| Vacated volume, team | 55.0 / 57.6 | 57.5 / 56.7 | Reverses |
| Vacated volume, position group | 54.2 / 57.7 | 57.0 / 57.2 | Reverses |
| **Touches over last 3 games** | **58.2 / 53.6** | **57.1 / 55.7** | Small nudge |
| Touch trend | 56.8 / 56.0 | 56.6 / 56.8 | None |
| Snap share, last 3 games | 57.4 / 55.1 | 57.4 / 55.6 | Small nudge |
| **Snap share, last game** | **57.7 / 54.8** | **57.5 / 55.7** | Small nudge |
| Running hot | 56.5 / 56.3 | 56.7 / 56.6 | None |
| Volatility | 57.1 / 55.5 | 56.4 / 57.2 | Reverses |
| Projection trend | 55.0 / 57.7 | 56.1 / 57.2 | Small (rising projection slightly worse) |
| Targets over last 3 games | 56.0 / 56.9 | 56.7 / 56.6 | None |

Pair counts per cell and the model coefficients are in `results/study2_model_output.txt`.

**Near-ties (gap under 1.5) broken by implied total / home+dome:** 52.3% / 51.1%. That's noise, so the home/dome tiebreaker from Study 1 is withdrawn.

### Multiple testing and leakage
- 21 signals and 2 model types were tried. About one false hit of around 1 point would be expected by chance. No lift survived the single held-out test, so there's nothing that needs a correction.
- No lookahead in the features. The one caveat is that Sleeper's stored past projections may include late updates, some time-stamped after kickoff. If anything, that flatters the baseline.
- Injury reports are joined by GSIS id, with a name+team fallback (`qfix.py`). The match rate wasn't measured. 5.4% of relevant player-weeks are tagged Questionable, so some tags are probably missed.

## 6. Final rule
1. If the gap is under 3 points, start the higher projection, whatever the source (ESPN or Sleeper did equally well).
2. If the higher-projected player is Questionable (or limited in practice), treat it as a coin flip and keep a later-kickoff swap open. Don't flip on the tag alone.
3. If he also has more recent volume, you can be a little more confident. Volume never flips a call.
4. **Exception:** if the starter in front of a player is confirmed out for the season, the backup inherits the role, and the projection may be stale. This is Blitz's Gordon case. It is not directly tested here: the vacated-volume signal covered week-to-week Out tags, and that edge reversed. Treat it as unproven until it has been tested.
5. Expect to lose about 4 of every 9 close calls no matter which rule you use.

## 7. Caveats
- Study 1 has 3 usable weeks and a 1-week holdout. Study 2 is the real test.
- Pairs overlap, so naive p-values overstate the evidence. Use the cluster-bootstrap ranges.
- Study 2 pairs are drawn league-wide, not from QBZ's actual roster decisions. Projection floor is 6 (Study 1 used 4).
- Inactive players and mid-game injuries count as they happened, because that risk is part of a real start/sit decision. Players ruled Out before kickoff are excluded.
- Study 1 matched ESPN to nflverse by name+team. 3 relevant player-weeks didn't match.

## 8. Reproduce
Python 3 with pandas, numpy, scikit-learn and requests.
```bash
# Study 2 (from an empty dir; or skip dl.sh and untar data/raw/sleeper_*.tar.gz, gunzip nflverse_injuries_*/sleeper_players/nflverse_games, renaming to inj_{s}.csv, players.json, games.csv)
bash scripts/study2-deep-2021-2026/dl.sh
python3 scripts/study2-deep-2021-2026/build.py   # -> players.pkl
python3 scripts/study2-deep-2021-2026/vac.py     # vacated-volume fix
python3 scripts/study2-deep-2021-2026/qfix.py    # injury name+team fallback
python3 scripts/study2-deep-2021-2026/pairs.py   # -> pairs.pkl
python3 scripts/study2-deep-2021-2026/model.py   # -> results/study2_model_output.txt
python3 scripts/study2-deep-2021-2026/export.py  # -> player_week_*.csv.gz, close_pairs_*.csv.gz

# Study 1 (untar data/raw/espn_mroster_2026_wk1-5.tar.gz, gunzip nflverse files to snaps26.csv, ps.csv, games.csv)
# or re-pull: ESPN_S2=... SWID=... python3 scripts/study1-espn-2026/pull.py ; bash scripts/study1-espn-2026/dl_nflverse.sh
python3 scripts/study1-espn-2026/build.py        # -> rows.json
python3 scripts/study1-espn-2026/an.py           # signal table + QBZ back-trace
python3 scripts/study1-espn-2026/bs.py           # cluster bootstrap
python3 scripts/study1-espn-2026/espn_accuracy.py
```
To shortcut the Study 2 pipeline, load the published CSVs and run model.py on them: `pd.concat(pd.read_csv(f) for f in glob('data/close_pairs_*.csv.gz'))`.
