# Data dictionary — close-call research

All files are gzip CSV unless noted. Open with `pandas.read_csv(path)` (gzip is detected automatically).
Scoring is ESPN/Sleeper full PPR throughout. Season = NFL regular season; week = 1-18.

## player_week_{2021..2026}.csv.gz — study 2 player-week table (31,788 rows total)
One row per Sleeper projection for a QB/RB/WR/TE in a week whose stats file was complete (>=200 players). Built by `scripts/study2-deep-2021-2026/build.py`, then `vac.py`, then `qfix.py`. All "lagged" features use only earlier weeks of the same season in which the player was active (no lookahead).

| Column | Meaning |
|---|---|
| season, week | NFL season and week |
| pid | Sleeper player id |
| pos | QB / RB / WR / TE |
| team, opp | NFL team and opponent (Sleeper abbreviations; LA mapped to LAR) |
| proj | Sleeper weekly projected PPR points (`pts_ppr`) |
| act | Actual PPR points (Sleeper stats `pts_ppr`; 0 if no stat line) |
| active | True if `gms_active`>0 or offensive snaps>0 |
| snp, tmsnp | Player offensive snaps; team offensive snaps (this week — outcome, not a feature) |
| tgt, car | Targets, rush attempts this week (outcome) |
| pyd | Pass attempts this week (column name is a legacy misnomer; outcome) |
| rz | Red-zone targets if Sleeper provided it, else blank (not used) |
| gsis | nflverse GSIS id (from Sleeper player DB), used for injury join |
| opp_vol | tgt + car this week (outcome) |
| snapsh | snp / tmsnp this week (outcome) |
| vol1, vol3 | Mean targets+carries over last 1 / last 3 prior active games |
| tgt3 | Mean targets over last 3 prior active games |
| snap1, snap3 | Snap share last prior active game / mean of last 3 |
| res | act − proj this week (outcome) |
| resid_std | Season-to-date mean of (act − proj) in prior active weeks ("running hot") |
| pts_sd | Season-to-date std dev of actual points in prior active weeks (volatility) |
| proj_prev, proj_trend | Last week's projection; proj − proj_prev |
| vol_trend | vol1 − vol3 |
| home | 1 home, 0 away (nflverse games.csv) |
| imp | Vegas implied team total = total/2 ± spread/2 |
| spread | Team's spread line from nflverse (positive = team favored, nflverse convention for home; sign flipped for away) |
| dome | 1 if roof is dome or closed |
| rest | Team rest days minus opponent rest days |
| wind | Wind mph for outdoor games, 0 indoors; blank if missing |
| temp | Temperature (not used as a feature) |
| proj_share | proj / imp |
| opp_allow | Opponent's mean PPR allowed to this position in earlier weeks of the season |
| q | 1 if Questionable on the final injury report (GSIS-id or name+team match) |
| out | 1 if Out/Doubtful (these rows are excluded from pairs) |
| lim | 1 if final practice status Limited or Did Not Participate |
| grp | Position group: QB, RB, REC (WR+TE) |
| vac_team, vac_grp | Sum of prior-3-game targets+carries of teammates ruled Out/Doubtful (whole team / same group) |
| nm | Normalized name key used for the injury name-match fix (helper) |

## close_pairs_{2021..2026}.csv.gz — study 2 close pairs (437,340 rows total)
Built by `pairs.py`. Within each week: players with proj ≥ 6, not Out/Doubtful, with a Vegas line; pairs on different NFL teams, same position or both flex (RB/WR/TE), projection gap > 0 and < 3. Player A is always the higher projection. Pairs with tied actual points dropped.

| Column | Meaning |
|---|---|
| sw | season*100+week (cluster id for bootstrap) |
| season, week | |
| pos | "A_pos-B_pos" e.g. WR-RB |
| gap | proj_A − proj_B (0–3) |
| ya, yb | Actual PPR of A and B |
| d_<feature> | Feature of A minus feature of B for the 21 features: proj, imp, proj_share, home, dome, rest, spread, wind, opp_allow, q, lim, vac_team, vac_grp, vol3, vol_trend, snap3, snap1, resid_std, pts_sd, proj_trend, tgt3 (definitions above) |
| a_pos | Position of A |
| ta, tb | NFL teams of A and B |
| y | 1 if the higher projection (A) outscored B — the target |

## espn_2026_wk1-4_rostered.csv.gz — study 1 table (651 rows)
Every rostered QB/RB/WR/TE on all 12 teams of league 1776545061, weeks 1-4, from ESPN mRoster, with nflverse-derived pre-game features (built by `scripts/study1-espn-2026/build.py`).

| Column | Meaning |
|---|---|
| week | 2026 week |
| fantasy_team_id | ESPN team id (13 = QBZ) |
| pid, name, pos | ESPN player id, name, position |
| nfl_team | NFL team (nflverse abbreviation) |
| slot | ESPN lineupSlotId (0 QB, 2 RB, 4 WR, 6 TE, 23 FLEX, 20 bench, 21 IR) |
| slot_name | Decoded slot |
| espn_proj | ESPN weekly projection (statSourceId 1) |
| actual_ppr | ESPN actual points (statSourceId 0) |
| elig | ESPN eligibleSlots list, space-separated |
| snap1 | nflverse offense snap % last week |
| trend | snap % change between the two prior weeks |
| snapmean | mean snap % in prior weeks |
| oppg | mean targets+carries per prior game |
| oppsh | share of team targets+carries in prior weeks |
| itt | Vegas implied team total |
| home, dome | 1/0 |
| resid | Season-to-date mean (actual − ESPN projection) in prior weeks |

## espn_2026_wk1-4_all_rostered.csv.gz — ESPN accuracy check (all positions incl. K and D/ST)
week, fantasy_team_id, espn_player_id, name, default_pos_id (ESPN: 1 QB, 2 RB, 3 WR, 4 TE, 5 K, 16 D/ST), slot (as above; 16 D/ST, 17 K), espn_proj, actual_ppr. Starters = slot not in {20, 21}.

## qbz_backtrace_2026_wk1-4.csv.gz — QBZ back-trace (24 rows)
Every QBZ (team 13) starter vs. eligible bench player where starter_proj − bench_proj < 3.5 (includes cases where the bench player was projected higher).
Columns: week, slot, started, started_proj, started_actual, benched, benched_proj, benched_actual, proj_gap (started − benched), within_3, pts_lost (max(0, benched_actual − started_actual)), started_/benched_snap1, started_/benched_home, started_/benched_dome.

## raw/ — untouched source pulls (pulled Oct 11, 2026)
| File | Source |
|---|---|
| sleeper_proj_stats_{season}.tar.gz | `projections-{s}-{w}.json` and `stats-{s}-{w}.json` from `https://api.sleeper.app/{projections|stats}/nfl/{s}/{w}?season_type=regular&position[]=QB&position[]=RB&position[]=WR&position[]=TE` |
| sleeper_players.json.gz | `https://api.sleeper.app/v1/players/nfl` (player DB; gives gsis_id) |
| nflverse_games.csv.gz | `https://github.com/nflverse/nfldata/raw/master/data/games.csv` |
| nflverse_injuries_{s}.csv.gz | `https://github.com/nflverse/nflverse-data/releases/download/injuries/injuries_{s}.csv` |
| nflverse_player_stats_2026.csv.gz | `https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats_2026.csv` |
| nflverse_snap_counts_2026.csv.gz | `https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_2026.csv` |
| espn_mroster_2026_wk1-5.tar.gz | `r{wk}.json` = `https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2026/segments/0/leagues/1776545061?view=mRoster&scoringPeriodId={wk}` (private league; requires login cookies, none stored here) |
