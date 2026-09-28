# Quantum Blitz — Mayfield (TB) vs Murray (MIN) ROS + Meyers/Allgeier cost (Sigma)
Written Fri Sep 25 2026 ~9:00 PM CT. Read-only. Invent-nothing; `UNK` = not found.

**Roster note:** roster.json (ESPN sync 8:36 PM CT) now shows **Jacoby Brissett and Rashod Bateman added, and Zach Charbonnet dropped**. audit.log shows WAIVER_CLAIM entries at 20:35 CT. Mayfield is on another team's bench (league_rosters snapshot 20260925-182703).

**Scoring:** fantasy pts are nflverse `fantasy_points_ppr` (4-pt pass TD, 0.04/pass yd, -2 INT, 0.1/rush yd, 6/rush TD, -2 fumble lost). ESPN projections come from ESPN's public default-PPR player feed, weekly statSplitTypeId=1 rows, summed by week. [S1][S2][S3]

## 1) QB1 ROS

| QB | Season | G | PPR/g | Cmp% | YPA | TD/INT | Rush yd/g (TD) |
|---|---|---|---|---|---|---|---|
| Baker Mayfield TB | 2025 | 17 | 16.00 | 63.2 | 6.80 | 26/11 | 22.5 (1) |
| | 2026 YTD | 2 | 11.91 (11.64, 12.18) | 71.0 | 6.42 | 1/1 | 29.5 (1) |
| Kyler Murray MIN | 2025 (ARI) | **5** (W1–5 only; he had no stat rows W6–18) | 15.56 | 68.3 | 5.98 | 6/3 | 34.6 (1) |
| | 2026 YTD | 1 (11 snaps W1, 17%) | -0.38 | 60.0 | 3.60 | 0/1 | 9.0 (0) |

Murray 2026: left W1 with a concussion (11 snaps), missed W2 (Wentz started), cleared protocol 9/21, and starts W3 [S4][S5]. He was released by ARI in Mar 2026 and signed with MIN (availability.json). Reason for missing 2025 W6–18: UNK (nflverse only shows no rows).

### Supporting cast / OL
| | Top targets W1–2 (tgt / yds) [S1] | PFF OL rank (post-W2) [S6] | Receiver injuries |
|---|---|---|---|
| TB | Emeka Egbuka WR 11/79; Cade Otton TE 11/64; Bucky Irving RB 11/49; Ted Hurst III WR 10/63 | **#2** | UNK |
| MIN | Justin Jefferson WR 15/147; T.J. Hockenson TE 9/65; Jordan Addison WR 7/21 | #11 | UNK |
Note: Mike Evans is now on SF (FantasyPros W3 matchups article [S7]).

### Byes and W3 head-to-head
- **TB bye W10; MIN bye W6.** Both come from the ESPN pro schedule (pro_sched.json) [S8], and ESPN's weekly projections show 0.0 in exactly those weeks.
- **W3 is MIN @ TB** (same game): MIN -1.5, total 42.5; ITT MIN 22.25 / TB 20.75 (CBS, Sharp) [S9][S10]. TB D vs QB 16.94/#16. MIN D vs QB 14.68/#13.

### ROS schedule vs QB defense
Cells show ESPN QB fantasy pts allowed per game / rank (32 = most allowed = easiest). ESPN positionAgainstOpponent, **2-game sample** [S8].

| Wk | Mayfield (TB) | Murray (MIN) |
|---|---|---|
| 3 | vs MIN 14.68/#13 | @TB 16.94/#16 |
| 4 | vs GB 17.21/#17 | vs MIA 21.04/#26 |
| 5 | @DAL 25.04/#28 | @NO 15.62/#14 |
| 6 | vs PIT 6.87/#1 | **BYE** |
| 7 | @CAR 18.33/#20 | vs IND 26.97/#30 |
| 8 | vs ATL 18.11/#19 | @DET 32.01/#32 |
| 9 | @CHI 20.08/#24 | vs BUF 23.12/#27 |
| 10 | **BYE** | @GB 17.21/#17 |
| 11 | @DET 32.01/#32 | @SF 9.00/#5 |
| 12 | vs CAR 18.33/#20 | vs ATL 18.11/#19 |
| 13 | vs LAC 18.35/#21 | vs CAR 18.33/#20 |
| **14** | @BAL 15.71/#15 | @NE 8.79/#4 |
| **15** | vs NO 15.62/#14 | vs DET 32.01/#32 |
| **16** | @ATL 18.11/#19 | vs WSH 27.24/#31 |
| **17** | vs LAR 12.22/#6 | @NYJ 12.75/#9 |
| Avg W3–13 (10 games) | 18.90 | 19.84 |
| Avg W14–17 (4 games) | 15.41 | **20.20** |

### ESPN projections (public ESPN player feed, weekly rows summed) [S3]
| | W3–13 | W14–17 | W3–17 total | Playoff weeks |
|---|---|---|---|---|
| Murray | 185.9 | **72.5** | **258.4** | 16.5 / 19.4 / 19.8 / 16.9 |
| Mayfield | 168.3 | 64.3 | 232.6 | 15.0 / 16.7 / 17.1 / 15.5 |
ESPN W3 single-week: Murray 17.3, Mayfield 15.6.

### Verdict
**Murray is the better ROS QB1 on the evidence.**
- ESPN ROS is higher by 25.8 pts, and higher by 8.2 in W14–17.
- His playoff slate is easier (avg 20.20 vs 15.41; W15 DET #32 and W16 WSH #31, while Mayfield has no top-10-easiest playoff matchup).
- He brings more rushing (34.6 vs 22.5 yd/g in 2025).

Mayfield's edges are durability (17 games in 2025 vs Murray's 5; Murray had a W1 2026 concussion), a 16.0 PPR/g 2025 floor, and PFF OL #2 vs #11. Acquiring Mayfield only makes sense as insurance. Brissett is already rostered as QB2, and he covers MIN's W6 bye.

## 2) Value cost

| Player | Role | Snap% W1→W2 | Tgt/car W1→W2 (share) | ESPN W3–17 proj | Bye |
|---|---|---|---|---|---|
| Jakobi Meyers JAX WR | WR3-4 behind Parker Washington (18 tgt) and Brian Thomas Jr. (11) | 65%→90% | tgt 2→1 (9.5%→3.6%) | 131.9 (W14–17 37.6) | W7 |
| Tyler Allgeier ARI RB | Snap leader, but Jeremiyah Love now leads carries; Conner (IR-DTR) eligible W5 | 59%→64% | car 17→5 (50%→29%); tgt 2→2 | 111.2 (W14–17 24.8; W14 = ARI bye) | W14 |
Sources: nflverse [S1][S2], ESPN feed [S3], ESPN pro schedule [S8], Conner IR (NBC [S11]). 2025 PPR/g: Meyers 10.99 (LV/JAX, 16 g); Allgeier 7.24 (ATL, 17 g) [S2].

**Allgeier:** he is our **only healthy backup RB**. Charbonnet has been dropped, Jacobs is on the Exempt list, and Etienne is on hamstring watch (availability.json snap_mult 0.9). Trading him leaves Achane and Etienne as the only active RBs until Jacobs returns (W7 at the earliest if the suspension is 6 games).

### WR depth test (roster.json confirms: London, Wilson, Shaheed, Meyers, Pittman [Q foot], Bateman)
| WR | Team / role / usage | ESPN W3–17 proj | Bye |
|---|---|---|---|
| Michael Pittman Jr. | PIT; W1 88% snaps, 3 tgt (8.1%); missed W2 (foot), **Q for W3** | **155.5** | W9 |
| Jakobi Meyers | JAX; see above | 131.9 | W7 |
| Rashod Bateman | BAL; snaps 78%→93%; tgt 1→9 (4.2%→31.0%); W2 7-88-1 = 21.8 with Zay Flowers (hamstring) out. ESPN outlook: "likely slide back to a supporting role" when Flowers returns. 2025: 4.26 PPR/g (13 g) | 104.4 | W13 |
| (starters) London ATL / Wilson NYJ / Shaheed SEA | — | — | W11 / W13 / W11 |

**WR bye collisions:** W11 = London + Shaheed; W13 = Wilson + Bateman. Covering those weeks takes 3 WR-eligible bodies (2 WR + FLEX; FLEX can also be an RB).
- With Meyers: W11 has Wilson, Pittman, Meyers, Bateman available; W13 has London, Shaheed, Pittman, Meyers.
- Without Meyers: W11 has Wilson, Pittman, Bateman (enough, but only if Pittman is healthy); W13 has London, Shaheed, Pittman (enough).

**WR depth verdict:** losing Meyers is a small hit. Pittman projects higher (155.5 vs 131.9) but carries foot risk. Bateman is 27.5 pts below Meyers ROS and his volume depends on Flowers staying out. Meyers' W7 bye doesn't collide with any other WR. Allgeier is the costlier piece to lose for roster function (RB depth), not for points.

## UNK
TB/MIN receiver injury statuses; reason Murray missed 2025 W6–18; future-week Vegas lines; Flowers' W3 status; Mayfield's trade price/owner intent.

## Sources
- [S1] nflverse stats_player_week_2026 / snap_counts_2026: https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2026.csv ; https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_2026.csv
- [S2] nflverse stats_player_week_2025: https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2025.csv
- [S3] ESPN public player projections (default PPR), kona_player_info: https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2026/segments/0/leaguedefaults/3?scoringPeriodId=3&view=kona_player_info (fetched 8:47 PM CT)
- [S4] https://www.vikings.com/news/kyler-murray-starting-quarterback-week-3-buccaneers-injury
- [S5] https://www.cbssports.com/nfl/news/vikings-kyler-murray-clears-concussion-protocol-starter-for-week-3/
- [S6] PFF OL rankings post-W2: https://www.pff.com/news/nfl-offensive-line-rankings-2026
- [S7] https://www.fantasypros.com/2026/09/fantasy-football-points-allowed-best-worst-matchups-week-3-2026/
- [S8] ESPN league API snapshot (local): recon/weekly/w03/raw/pro_sched.json, fa_pool.json (positionAgainstOpponent, Bateman outlook)
- [S9] https://www.cbssports.com/betting/news/week-3-nfl-betting-odds-lines-spreads-totals/
- [S10] https://www.sharpfootballanalysis.com/analysis/nfl-implied-team-totals/
- [S11] https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/cardinals-place-james-conner-on-ir-among-their-moves-to-53
- Local: roster.json (8:36 PM sync), availability.json, audit.log
