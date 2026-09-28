# Quantum Blitz — W3 Matchup Pass (Sigma)
Written Fri Sep 25 2026 ~8:45 PM CT. Read-only research. ESPN PPR. Invent-nothing rules: every number cites a source below; `UNK` = not found.

**Sample-size warning:** all 2026 defense-vs-position data is 2 games (2 opponents). Treat as a soft signal.

## Legend / sources for columns
- **oppD vs pos (ESPN)** = ESPN `positionAgainstOpponent` (avg fantasy pts allowed per game to that position; rank 1 = fewest allowed/toughest, 32 = most allowed/easiest). Pulled from ESPN league API FA pool snapshot `recon/weekly/w03/raw/fa_pool.json` (20:20 CT today). [S1]
- **JKB** = Joe Knows Ball fantasy points allowed rank (1 = fewest PPG, 32 = most), 2026. Scoring format not stated on page. [S2]
- **Snaps** = nflverse/PFR snap_counts_2026 (refreshed 20:20 CT). **Targets/carries/share** = nflverse stats_player_week_2026 (`target_share`; carry share = player carries / team carries in that file). Matches results/week-1.json & week-2.json. [S3][S4]
- **Lines**: spread/total = CBS Sports Week 3 odds (current) with SportsLine/CBS table in (). **ITT** = Sharp Football Analysis implied team totals (odds as of Mon 9/21 8:11 PM ET). [S5][S6][S7]
- **Proj**: ESPN = projections.json (espn_api sp3, as of 4:02 PM CT) for rostered; ESPN FA = fa_pool.json stat proj sp3. FP = FantasyPros player-page PPR W3 projection (curl 8:22 PM CT). [S1][S8]

## Schedule check
All opponents in the brief match schedule.json and ESPN pro schedule: MIN @ TB, KC @ MIA, LV @ NO, NYJ @ DET, SEA @ WSH, CIN @ PIT, ARI @ SF, NE @ JAX. No corrections needed. Kyler Murray is on MIN (not ARI), and Allgeier is on ARI.

## Starters

| Slot | Player (opp) | Opp D vs pos (ESPN avg / rank; JKB rank) | Opp QB situation | Usage W1→W2 (snap% / tgt / car / share) | Spread / Total / ITT | Proj ESPN / FP | Script / verdict |
|---|---|---|---|---|---|---|---|
| QB | Kyler Murray (MIN @ TB) | TB vs QB 16.94 / #16; JKB 14 | TB: Baker Mayfield (100% snaps W1–2). Murray cleared protocol and starts (Vikings.com, CBS) | W1 17% (11 snaps, 3/5 18y 1 INT, left with concussion); W2 DNP (Wentz started) | MIN -1.5 / 42.5 / MIN 22.25 | 17.35 / 17.6 | Slight road favorite, neutral total. Middle-of-pack matchup. Hardly played in W1–2, so no 2026 usage baseline yet. START. |
| RB1 | De'Von Achane (vs KC) | KC vs RB 20.45 / #18; JKB 7 (sources disagree) | KC: Mahomes (100% snaps W1–2). MIA QB = Malik Willis | Snaps 86%→76%; car 11→20 (share 61%→69%); tgt 5→6 (18.5%→26.1%) | KC -10.5 (CBS now -11.5) / 45.5–46 / MIA 17.0 | 19.42 / 17.2 | Big home underdog with the 2nd-lowest ITT, so expect trailing-script passing. His target share rising to 26% protects his floor. START. |
| RB2 | Travis Etienne Jr. (vs LV) | LV vs RB 16.45 / #10; JKB 5 (tough) | LV: Kirk Cousins (100% W1–2) | Snaps 59%→54%; car 9→8 (36%→30%); tgt 9→2 (17.3%→6.3%). Kamara 29% snaps W2 | NO -3 / 43.5 / NO 23.25 | 11.93 / 11.2 | Home favorite, so a run lean. Matchup is below average and he is on hamstring watch, but no bench/FA RB beats him. START. |
| WR | Garrett Wilson (@ DET) | DET vs WR 42.95 / #31; JKB wide 30; DET also #32 vs QB. Branch & K. Joseph on PUP (FP) | DET: Goff | Snaps 75%→88%; tgt 7→7 (30.4%→19.4%) | DET -6.5 / 47.5–48 / NYJ 20.5 | 14.72 / 16.5 | Road underdog in a high total, so pass lean. Elite matchup. START. |
| FLEX | Rashid Shaheed (@ WSH) | WSH vs WR 39.4 / #24; JKB wide 22, slot 13 | WSH: **Mariota starts** (Daniels dislocated L elbow, OUT, week-to-week; CBS/Commanders Wire). SEA QB **Darnold starts**, off injury report (NFL.com/Seattle Times) | Snaps 66%→56%; tgt 3→6 (12.5%→23.1%); ST snaps 36–39% | SEA -7 (CBS table -7.5) / 40.5 / SEA 23.25 (WSH 16.75, lowest on the board) | 10.94 / 8.6 | Favorite facing a backup QB, which could mean a run-heavy late game script. Darnold's return is a plus for the passing game. START (see FLEX section below). |
| DST | Steelers (vs CIN) | CIN offense gives up 7.5 DST pts/g / #23 | CIN: **Joe Burrow healthy**, off the injury report (Bengals.com/NBC/FP) | W1 19.0, W2 8.0 actual | CIN -3.5 / 42.5 / CIN ITT 23.0 | 6.11 / FP UNK (not in FP's top-10 DST list, whose #10 is 6.8) | Home underdog against a healthy Burrow with a 23.0 ITT. Weakest slot. See DST FA flip below. |
| K | Eddy Pineiro (vs ARI) | ARI vs K 4.5 / #5 (tough, 2-game sample) | ARI: Jacoby Brissett (100% W1–2) | K: no snap usage signal | SF -8.5 / 47.5 / **SF 28.0** (T-3rd highest ITT) | 9.85 / 8.8 | Not on the 49ers Friday injury report. The W2 illness Q is resolved (49ers.com / Cardswire Fri IR). ITT is the A-grade K signal, and 28.0 is elite. START. |

## Bench

| Player (opp) | Opp D vs pos | Opp QB | Usage W1→W2 | Spread / Total / ITT | Proj ESPN / FP | Verdict |
|---|---|---|---|---|---|---|
| Jakobi Meyers WR (vs NE) | NE vs WR 28.15 / #12; JKB wide 9 | NE: Drake Maye | Snaps 65%→90%; tgt 2→1 (9.5%→3.6%) | JAX -3 (CBS table -2.5) / 45.5 / JAX 24.25 | 9.29 / 9.7 | Off the injury report (thumb), full practice. Snaps rose but targets collapsed. Bench. |
| Tyler Allgeier RB (@ SF) | SF vs RB 20.6 / #19; JKB 19 | SF: Purdy (85% snaps W2). W3 status not verified here. SF Fri IR: Evans Q; Bosa, Robinson OUT | Snaps 59%→64%; car 17→5 (50%→29%); tgt 2→2. Jeremiyah Love 43%/40% snaps | SF -8.5 / 47.5 / ARI 19.5 | 7.52 / 7.1 | 8.5-pt road underdog, so he loses rushing work to game script. Bench. |
| Michael Pittman Jr. WR (vs CIN) | CIN vs WR 24.95 / #9; JKB wide 3 (tough) | CIN: Burrow | W1 88% snaps, 3 tgt (8.1%); W2 OUT (foot) | CIN -3.5 / 42.5 / PIT 19.5 | 11.36 / 10.3 (raw, assumes he plays) | **QUESTIONABLE** (foot, LP Wed/Thu/Fri, per Steelers.com/NBC in availability.json). Model play_prob 0.55 → adj 2.29. Kicks off at the same time as Shaheed (12:00 CT). Actives are out ~10:30 CT. |

## FLEX head-to-head (Shaheed vs Meyers vs Allgeier)

| | Shaheed | Meyers | Allgeier |
|---|---|---|---|
| ESPN proj | **10.94** | 9.29 | 7.52 |
| FP proj (live 8:22 PM) | 8.6 | **9.7** | 7.1 |
| Consensus (projections.json) | **9.75** | 9.55 | 7.31 (adj 6.94) |
| Team ITT | 23.25 | **24.25** | 19.5 |
| Spread | SEA -7/-7.5 | JAX -3 | ARI +8.5 |
| Opp D vs pos (ESPN rank, 32 = easiest) | WSH #24 | NE #12 | SF #19 |
| Target/carry share trend | tgt 12.5%→**23.1%** | tgt 9.5%→3.6% | car 50%→29% |
| Snap trend | 66→56% | 65→90% | 59→64% |

**Recommendation: keep Shaheed at FLEX.** He has the highest consensus projection and the best share trend, Darnold is back, and his matchup rank is the easiest of the three. Meyers has the slightly higher ITT and FP's edge, but his W2 target share was 3.6%. Allgeier is a large road underdog whose carries are shrinking. The margin over Meyers is small (0.2 consensus pts).

## Flags
- **Bench-over-starter:** none clear. The only conditional is Pittman, if active at 10:30 CT. His raw projections (ESPN 11.36 / FP 10.3) beat Shaheed's (10.94 / 8.6), but he is coming off a foot injury, had only an 8% target share in W1, has a tougher matchup (CIN #9 vs WR) and a lower ITT (19.5 vs 23.25). Lean Shaheed unless there are no-limit reports.
- **Pineiro:** healthy, no W3 designation. SF ITT 28.0. Hold.
- **FA-over-starter:** DST: Panthers over Steelers is a modest upgrade (ESPN 7.15 vs 6.11; FP 7.7 vs Steelers UNK, below 6.8). No other FA beats a starter.

## FA candidates (vs W3 matchup)

| FA | W3 opp | ESPN / FP proj | Spread / ITT | Opp D vs pos (ESPN) | Usage W1→W2 | Verdict vs our starter |
|---|---|---|---|---|---|---|
| Geno Smith QB NYJ | @ DET | 15.07 / 15.4 | +6.5 / 20.5 | DET vs QB 32.01 / **#32** (FP: most allowed; Shough 25, Allen 40) | 100%/100% snaps; 24→41 att; 9.3→15.58 PPR | Best FA QB and a great pass-script spot, but still below Murray (17.35/17.6). Keep Murray. |
| Marcus Mariota QB WSH | vs SEA | 15.32 / 14.0 | +7 / 16.75 (lowest) | SEA vs QB 8.16 / **#2** | W2 relief 45% snaps, 11/16 111y 1TD | Starting (Daniels OUT), but faces the 2nd-toughest QB matchup with the lowest ITT. No. |
| Xavier Hutchinson WR HOU (not ambiguous: the only Hutchinson in the FA pool; Aidan Hutchinson is a DET DE) | @ IND | 9.55 / 8.9 | HOU -2.5 / 23.0 | IND vs WR 42.45 / #29 | Snaps 56%→81%; tgt 6→9 (16.2%→18.0%) with Nico Collins out (hamstring). Collins' W3 status UNK | Close to Shaheed (10.94/8.6) and a strong matchup, but not clearly better. Would need Collins OUT. No swap. |
| Tyjae Spears RB TEN | @ NYG | 9.74 / 8.6 | +3 / 18.25 | NYG vs RB 25.75 / #25 | Snaps 50%→36%; car 3→7; tgt 4→2. ESPN status QUESTIONABLE | Below Etienne (11.93/11.2). No. |
| Woody Marks RB HOU | @ IND | 8.75 / 8.0 | -2.5 / 23.0 | IND vs RB 34.2 / #30 | Snaps 51%→48%; car 9→8; tgt 1→6 | Below Etienne. ESPN outlook expects Montgomery to reclaim the lead role. No. |
| Kenyon Sadiq TE NYJ (not Oronde Gadsden or Ben Sinnott; the NYJ rookie TE is in waivers.json & the ESPN FA pool) | @ DET | 8.42 / 8.4 | +6.5 / 20.5 | DET vs TE 29.35 / #32 | Snaps 42%→36%; tgt 3→3 | TE slot (Pitts) already played on TNF. As FLEX he trails Shaheed. Upside only if Mason Taylor (thumb) sits; Taylor's status UNK. No. |
| Panthers DST | @ CLE | 7.15 / **7.7** (FP #1 DST) | CAR -2.5 / CLE 20.0 | CLE gives up 9.0 DST pts/g / #26 | — | **Best DST option, +1.0 ESPN over Steelers.** Modest upgrade. |
| Saints DST | vs LV | 6.60 / 6.8 | NO -3 / LV 20.25 | LV gives up 5.0 / #15 | — | Slightly better than Steelers on projection only. Marginal. |
| Vikings DST | @ TB | 6.49 / 6.8 | MIN -1.5 / TB 20.75 | TB gives up 12.5 / #30 | — | Marginal over Steelers. Big DST-allowed profile from TB. |
| Bengals DST | @ PIT | 6.37 / UNK | CIN -3.5 / PIT 19.5 | PIT gives up 13.5 / #31 | — | Roughly equal to Steelers on projection. Opposite side of our own Steelers game. |

## UNK
FP DST projection for Steelers & Bengals (below FP's top-10 cutoff of 6.8); FantasyPros FP-allowed/game table (JS-rendered, not retrievable); Mahomes, Purdy & Mayfield formal W3 status (not checked; all played 85–100% of snaps W2); Nico Collins & Mason Taylor W3 status; FA W3 %rostered/waiver-vs-FA status (fa_rows says FREEAGENT for all listed); line values are a mix of Mon (Sharp ITT) and Fri (CBS), so ITT may be off by ≤0.5.

## Sources
- [S1] ESPN league API snapshot: recon/weekly/w03/raw/fa_pool.json (positionAgainstOpponent, FA sp3 projections, outlooks); projections.json (espn_api sp3)
- [S2] Joe Knows Ball FPA by position: https://www.joeknowsball.com/nfl/fantasy-points-allowed
- [S3] nflverse snap counts: https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_2026.csv
- [S4] nflverse player stats: https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2026.csv
- [S5] CBS W3 odds: https://www.cbssports.com/betting/news/week-3-nfl-betting-odds-lines-spreads-totals/
- [S6] CBS/SportsLine W3 table: https://www.cbssports.com/betting/news/nfl-odds-picks-predictions-lines-spreads-best-bets-week-3-2026/
- [S7] Sharp implied team totals: https://www.sharpfootballanalysis.com/analysis/nfl-implied-team-totals/
- [S8] FantasyPros player projection pages, e.g. https://www.fantasypros.com/nfl/projections/geno-smith.php?scoring=PPR&week=3 ; FP DST W3: https://www.fantasypros.com/nfl/projections/dst.php?week=3&scoring=PPR
- [S9] FantasyPros W3 points-allowed matchups: https://www.fantasypros.com/2026/09/fantasy-football-points-allowed-best-worst-matchups-week-3-2026/
- [S10] Daniels out / Mariota starts: https://www.cbssports.com/nfl/news/jayden-daniels-injury-update-commanders-qb-elbow-2026/ ; https://commanderswire.usatoday.com/story/sports/nfl/commanders/2026/09/25/commanders-gm-adam-peters-huge-update-jayden-daniels/91935073007/
- [S11] Darnold starts: https://www.nfl.com/news/sam-darnold-glute-seahawks-commanders
- [S12] Burrow off IR: https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/joe-burrow-is-no-longer-on-the-bengals-injury-report ; https://www.bengals.com/news/steelers-bengals-injury-report-week-3-2026
- [S13] Murray starts: https://www.vikings.com/news/kyler-murray-starting-quarterback-week-3-buccaneers-injury ; https://www.cbssports.com/nfl/news/vikings-kyler-murray-clears-concussion-protocol-starter-for-week-3/
- [S14] 49ers Fri IR (Pineiro not listed): https://cardswire.usatoday.com/story/sports/nfl/cardinals/2026/09/25/49ers-injury-report-mike-evans-questionable-vs-cardinals/91944823007/
- [S15] ESPN xFPA by position (WR table snippet): https://www.espn.ph/fantasy/football/story/_/id/49869463/2026-fantasy-football-expected-points-xfpa-position-qb-rb-wr-te
- Local: availability.json (Pittman Q, Meyers off IR, Etienne active), results/week-1.json, week-2.json, results/sigma/snaps/*
