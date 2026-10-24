# Quantum Blitz — W3 QB2 Dossier + Hold/Drop + Panthers DST (Sigma)
Written Fri Sep 25 2026 ~8:50 PM CT. Read-only. Invent-nothing; `UNK` = not found. 2026 samples = 2 games.

## Scoring used
nflverse `fantasy_points_ppr`: 4-pt pass TD, 0.04/pass yd, -2 INT, 0.1/rush yd, 6/rush TD, -2 fumble lost, 2-pt conversions. This matches the core of ESPN standard QB scoring; ESPN's small bonuses are not included. "G" = games with a stat row, which includes relief appearances. [S1][S2]

## 1) QB2 table

| QB | Season | G (≥15 att) | Cmp% | YPA | TD/INT | Rush yd/g (rush TD) | PPR pts/g |
|---|---|---|---|---|---|---|---|
| Jameis Winston NYG | 2025 | 3 (2) | 56.1 | 8.59 | 2/2 | 7.7 (1) | 14.43 |
| | 2026 YTD | 1 (W2 relief, 88% snaps) | 40.7 | 4.11 | 0/1 | 1.0 (0) | 2.54 |
| Geno Smith NYJ | 2025 (LV) | 15 (15) | 67.4 | 6.75 | 19/17 | 7.3 (0) | 11.59 |
| | 2026 YTD | 2 | 70.8 | 7.11 | 1/0 | 12.0 (0) | 12.44 |
| Marcus Mariota WSH | 2025 | 10 (7) | 61.2 | 7.47 | 10/7 | 29.7 (1) | 12.55 |
| | 2026 YTD | 1 (W2 relief, 45% snaps) | 68.8 | 6.94 | 1/0 | 3.0 (0) | 8.74 |
| Aaron Rodgers PIT | 2025 | 16 (16) | 65.7 | 6.67 | 24/7 | 3.8 (1) | 14.19 |
| | 2026 YTD | 2 | 59.5 | 5.16 | 1/1 | 1.0 (0) | 8.26 |
| Jacoby Brissett ARI | 2025 | 14 (12) | 64.9 | 6.94 | 23/8 | 12.0 (1) | **16.25** |
| | 2026 YTD | 2 | 67.7 | 5.72 | 2/1 | 10.5 (0) | 11.49 |

All five are FREEAGENT in ESPN (fa_rows.json). ESPN W3 projections: Mariota 15.32, Geno 15.07, Winston 14.68, Rodgers 14.13, Brissett 13.65. ESPN ROS figure (fa_rows unlabeled column, very likely the ROS projection): Geno 234.0, Brissett 228.8, Rodgers 218.1, Winston 206.6, Mariota 51.3. [S3]

### MIN bye confirmation
**Minnesota bye = Week 6. Confirmed** via the ESPN pro schedule (recon/weekly/w03/raw/pro_sched.json, MIN byeWeek=6, no W6 game). schedule.json only covers W3, so it can't confirm this. None of the 5 QBs is on bye in W6. Their byes: NYG W8, NYJ W13, WSH W7, PIT W9, ARI W14. [S3]

### Weeks 3–8 opponent defense vs QB
Cells show ESPN average QB fantasy pts allowed per game / rank (32 = most allowed = easiest). Source is ESPN positionAgainstOpponent (2-game sample). **W6 = MIN bye week (bold).** [S3]

| QB | W3 | W4 | W5 | **W6** | W7 | W8 |
|---|---|---|---|---|---|---|
| Winston NYG | vs TEN 12.73/#8 | vs ARI 17.33/#18 | @WSH 27.24/#31 | **vs NO 15.62/#14** | @HOU 25.92/#29 | BYE |
| Geno NYJ | @DET 32.01/#32 | @CHI 20.08/#24 | vs CLE 18.99/#23 | **@NE 8.79/#4** | vs MIA 21.04/#26 | vs LV 12.29/#7 |
| Mariota WSH | vs SEA 8.16/#2 | vs IND 26.97/#30 | vs NYG 20.69/#25 | **@SF 9.00/#5** | BYE | vs PHI 18.84/#22 |
| Rodgers PIT | vs CIN 14.33/#12 | @CLE 18.99/#23 | vs IND 26.97/#30 | **@TB 16.94/#16** | @NO 15.62/#14 | vs CLE 18.99/#23 |
| Brissett ARI | @SF 9.00/#5 | @NYG 20.69/#25 | vs DET 32.01/#32 | **@LAR 12.22/#6** | vs DEN 13.91/#10 | @DAL 25.04/#28 |

W6 matchup order: Rodgers (#16) > Winston (#14) > Brissett (#6) > Mariota (#5) > Geno (#4).

### Supporting cast
Top targets W1–2 come from nflverse [S2]. OL rank is PFF's post-W2 ranking (Gordon McGuinness, 9/23) [S4].

| QB | Top 3 targets W1–2 (tgt / rec yds) | PFF OL rank |
|---|---|---|
| Winston | Isaiah Likely TE 18/111; Malik Nabers WR 13/70; Malachi Fields WR 10/55 | 21 |
| Geno | Adonai Mitchell WR 15/123; Garrett Wilson WR 14/136; Breece Hall RB 7/79 | 18 |
| Mariota | Stefon Diggs WR 15/102; Terry McLaurin WR 13/64; Dyami Brown WR 8/21 | 31 (Cosmi in concussion protocol) |
| Rodgers | DK Metcalf WR 19/67; Roman Wilson WR 12/54; Pat Freiermuth TE 10/78 (Pittman Q foot) | 12 |
| Brissett | Trey McBride TE 23/136; Michael Wilson WR 14/74; Kendrick Bourne WR 11/86 | 20 |

### Job security horizon
| QB | Status | Horizon | Source |
|---|---|---|---|
| Winston | Starter; Dart (knee surgery: MCL+PCL+meniscus) on IR, out for the rest of the regular season | Rest of 2026 | ESPN [S5]; NBC [S6] |
| Geno | Named starter ("No doubt about it... He's our guy," Glenn, 3/30) | Season | NewYorkJets.com [S7] |
| Mariota | Starting W3 only while Daniels (dislocated L elbow; no surgery, no IR) is week-to-week. Daniels could return as early as W4 (IND) | 1–3 weeks, then back to backup | CBS [S8]; Commanders Wire [S9] |
| Rodgers | PIT starter, age 42. Says 2026 is "zero debate" his final season. 96% snaps W2 | Season (age/injury risk) | AP [S10] |
| Brissett | ARI QB1. Murray was released by ARI in Mar 2026 and is now MIN's starter. Rookie Carson Beck is developing and "isn't taking Brissett's job yet"; Minshew is QB2 | Season, with some mid/late risk from Beck | CBS [S11]; azcardinals [S12]; availability.json |

### Ranked QB2 (evidence-only)
1. **Brissett**: best 2025 pts/g of the group (16.25 over 14 games), secure QB1 job, top target is TE McBride (23 tgt), W4–5 slate is soft (#25, #32). His W6 matchup is tough (#6).
2. **Geno**: named starter for the season, highest ESPN ROS figure (234.0), W3–5 soft (#32/#24/#23), 70.8% completions in 2026. His W6 @NE (#4) is the worst of the five.
3. **Rodgers**: secure job for the season, best W6 matchup (@TB #16), PFF OL #12. His 2026 YPA of 5.16 and 8.26 pts/g are poor.
4. **Winston**: starter for the rest of the season, decent W6 (vs NO #14) and W5/W7 are soft (#31/#29). His 2026 sample is ugly (40.7%, 4.11 YPA, 1 relief game), NYG has a W8 bye, and PFF OL is #21.
5. **Mariota**: short-term fill-in only while Daniels is week-to-week, PFF OL #31, W6 @SF #5, W7 bye.
If the pickup is only to cover MIN's W6 bye: Rodgers or Winston have the best W6 matchups; Brissett and Geno are better ROS holds.

## 2) Hold / drop (bench: Allgeier, Jacobs, Charbonnet, Goedert)
Statuses confirmed in roster.json and availability.json: Allgeier ACTIVE; Jacobs EXEMPT (ESPN DTD); Charbonnet PUP (ESPN OUT); Goedert OUT (ESPN DOUBTFUL). The league has **1 IR slot** (settings lineupSlotCounts 21:1), and Jaxson Dart is in it.

### ARI RB room (Allgeier)
- **James Conner**: placed on IR with a designation to return on Aug 30 (foot/ankle). Earliest return is W5 (Oct 11 vs DET). [S13][S14] RotoWire depth order: Jeremiyah Love, Allgeier, Bam Knight, Conner (IR-R), Trey Benson (IR). [S15]
- **"Love" = Jeremiyah Love** (rookie, #3 overall pick), not Trey Benson (Benson is on IR). [S15][S16]

| ARI RB | W1 snaps | W2 snaps | W1 car (share) | W2 car (share) | Tgt W1/W2 | PPR W1/W2 |
|---|---|---|---|---|---|---|
| Tyler Allgeier | 44 (59%) | 32 (64%) | 17 (50.0%) | 5 (29.4%) | 2/2 | 9.0/3.9 |
| Jeremiyah Love | 32 (43%) | 20 (40%) | 11 (32.4%) | 9 (52.9%) | 4/3 | 13.0/7.5 |
| Bam (Zonovan) Knight | 3 (4%) | 3 (6%) | 0 | 2 (11.8%) | 0/0 | –/2.4 |
Sources: nflverse snaps/stats [S1][S2]. Allgeier still leads in snaps, but Love took over as the lead ball-carrier in W2. Conner can return W5. ARI bye W14. ESPN/FP W3 projection: 7.52/7.1.

### Others
- **Josh Jacobs (GB)**: on the Commissioner's Exempt List since Aug 30 after misdemeanor battery and criminal-damage charges from a May 23 incident. He entered a no-contest plea in September; the NFL investigation is ongoing. A standard 6-game suspension would count time already served on the list, making him eligible **W7** (Oct 25 vs DET). The court declined to seal the video evidence, which adds uncertainty. [S17][S18][S19][S20] GB bye W11.
- **Zach Charbonnet (SEA)**: on reserve/PUP (ACL tear, Jan 17; surgery Feb 20). He must miss the first 4 games, so earliest game is **W5** (Oct 11 vs SF). Under the new PUP rules he can practice from W3. On 9/23 Macdonald said the practice window will NOT open this week. DraftSharks: "a long shot to be a fantasy factor before the second half." Rookie Jadarian Price and Emanuel Wilson are handling the backfield. [S21][S22][S23][S24] SEA bye W11.
- **Dallas Goedert (PHI)**: MCL sprain (W2 @TEN). Not going on IR, so he should miss fewer than 4 games; "a few weeks" per Fowler/ESPN. No specific date. Eagles TE depth is thin (Stowers on IR). [S25][S26][S27] PHI bye W10. W1 scored 23.7 PPR (results/week-1.json).

### Hold ranking
Expected availability windows below are inferred from the cited news, not official dates.
1. **Goedert (HOLD)**: back soonest (no IR, "a few weeks", roughly W5–6 if that holds). Proven TE1 output (23.7 in W1; 11 TD in 2025 per NBC Sports Philadelphia). Pitts has put up 0.0, 2.5, then 1-2-5 on TNF, so a real TE is needed.
2. **Jacobs (HOLD)**: likely GB RB1 on return, with W7 as the most likely return if the suspension is 6 games. The video evidence adds real downside risk.
3. **Allgeier (HOLD for now)**: our only active backup RB while Jacobs and Charbonnet are unavailable and Etienne is on hamstring watch. His role is shrinking (carry share 50%→29%) and Conner is eligible W5, so he becomes droppable once Jacobs or Goedert returns.
4. **Charbonnet → DROP**: no earliest-return date that's actually in play (practice window not opened; W5 is the eligibility floor, and DraftSharks projects the second half). Returns to a backfield with a rookie already producing (SEA ranks 9th in rushing without him). He can't go to IR because Dart holds the only slot. Fewest expected ROS weeks of the four.

## 3) Panthers DST (FREEAGENT; ESPN W3 7.15, FP 7.7)
Cells show the opponent offense's ESPN DST fantasy pts allowed per game / rank (32 = gives up the most to DSTs = best for us) [S3]. Opponent QB = W1–2 snap leader in nflverse [S1]; W3+ health not verified.

| Wk | Opp | Opp QB | Opp DST-allowed avg / rank | Opp ITT |
|---|---|---|---|---|
| W3 | @CLE | Deshaun Watson | 9.0 / #26 | 20.0 (Sharp) |
| W4 | vs DET | Jared Goff | 1.5 / #4 (bad) | UNK |
| W5 | **BYE** | — | — | — |
| W6 | @PHI | Jalen Hurts | 5.0 / #15 | UNK |
| W7 | vs TB | Baker Mayfield | 12.5 / #30 (great) | UNK |
| W8 | @GB | Jordan Love (GB OL PFF #32) | 6.5 / #21 | UNK |
| W9 | vs DEN | Bo Nix | 7.5 / #23 | UNK |
Verdict: good W3 and W7, bad W4, bye W5. It's a streaming add, not a hold. Steelers after W3: W4 @CLE (#26), W5 vs IND (#14), W6 @TB (#30), W9 bye.

## UNK
Future-week ITTs (W4+); FP DST projections beyond W3; exact Goedert return week; Jacobs suspension length/decision; Charbonnet practice-window date; W3 injury status of Watson, Goff, Hurts, Mayfield, J. Love and Nix; ESPN bonus-scoring adjustments (not applied); fa_rows column labels (ROS column inferred).

## Sources
- [S1] nflverse snap counts 2026: https://github.com/nflverse/nflverse-data/releases/download/snap_counts/snap_counts_2026.csv
- [S2] nflverse player stats 2025/2026: https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2025.csv ; https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_2026.csv
- [S3] ESPN league API snapshot (local): recon/weekly/w03/raw/{pro_sched.json, fa_pool.json (positionAgainstOpponent), fa_rows.json, settings.json}
- [S4] PFF OL rankings after W2: https://www.pff.com/news/nfl-offensive-line-rankings-2026
- [S5] https://www.espn.com/nfl/story/_/id/50013861/giants-qb-dart-knee-surgery-miss-rest-regular-season
- [S6] https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/giants-place-jaxson-dart-on-injured-reserve
- [S7] https://www.newyorkjets.com/news/geno-smith-named-starting-quarterback-jets-aaron-glenn-03-30-2026
- [S8] https://www.cbssports.com/nfl/news/jayden-daniels-injury-update-commanders-qb-elbow-2026/
- [S9] https://commanderswire.usatoday.com/story/sports/nfl/commanders/2026/09/25/commanders-gm-adam-peters-huge-update-jayden-daniels/91935073007/
- [S10] https://apnews.com/article/pittsburgh-steelers-aaron-rodgers-mike-mccarthy-909ae906eca44085ac0b1bda1bc95cc3
- [S11] https://www.cbssports.com/nfl/news/carson-beck-isnt-taking-jacoby-brissetts-job-yet-but-the-cardinals-like-what-theyre-seeing/
- [S12] https://www.azcardinals.com/news/cardinals-qb-jacoby-brissett-rich-with-teammate-currency-2026-season
- [S13] https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/cardinals-place-james-conner-on-ir-among-their-moves-to-53
- [S14] https://heavy.com/sports/nfl/arizona-cardinals/james-conner-injured-reserve-week-1/
- [S15] https://www.rotowire.com/football/player/james-conner-11691
- [S16] https://www.azcardinals.com/news/promising-outlook-for-jeremiyah-love-after-cardinals-elevate-cb-kalen-king
- [S17] https://www.nfl.com/news/nfl-places-packers-rb-josh-jacobs-commissioner-exempt-list
- [S18] https://www.usatoday.com/story/sports/nfl/packers/2026/09/24/josh-jacobs-update-plea-deal-suspension-packers/91912321007/
- [S19] https://www.si.com/onsi/fantasy/nfl/latest-ruling-in-josh-jacobs-case-could-cause-uncertainty-for-fantasy-football
- [S20] https://ftw.usatoday.com/story/sports/nfl/2026/09/24/josh-jacobs-coming-back-when-if-suspension-packers/91927582007/
- [S21] https://sports.yahoo.com/articles/seattle-seahawks-announce-zach-charbonnet-024404608.html
- [S22] https://www.cbssports.com/fantasy/football/news/seahawks-zach-charbonnet-wont-return-to-practice-this-week/
- [S23] https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/seahawks-rb-zach-charbonnet-not-ready-to-return-to-practice-this-week
- [S24] https://www.draftsharks.com/fantasy-football-news/82838/zach-charbonnet-not-ready-to-practice
- [S25] https://www.fantasypros.com/nfl/news/610420/dallas-goedert-knee-to-avoid-ir-expected-to-miss-few-weeks.php
- [S26] https://www.nbcsportsphiladelphia.com/nfl/philadelphia-eagles/dallas-goedert-out-a-few-weeks-with-knee-injury-mcl-sprain/752789/
- [S27] https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/dallas-goedert-sprained-his-mcl-will-miss-a-few-weeks
- [S28] Sharp ITT W3: https://www.sharpfootballanalysis.com/analysis/nfl-implied-team-totals/
