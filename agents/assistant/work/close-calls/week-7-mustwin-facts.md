# Week 7 must-win fact pack — Quantum Blitz (team 13) vs David's Daring Team (team 11)

FACTS ONLY. Built by Assistant, Sat Oct 24 2026, 6:25–6:45 AM CT. No ESPN writes. No lineup card. Status comes from ESPN's tag. An official NFL/team can't-play list can only bench a player. News below is notes only.

## Sources and pull times (all CT)
- ESPN fantasy (read client): mRoster/mMatchup/mMatchupScore/mSettings sp7 at 6:25 AM; weekly actuals at 6:26 AM; free agents (kona_player_info, FREEAGENT+WAIVERS) at 6:27–6:31 AM; ESPN defense-vs-position ratings (`positionAgainstOpponent`, season to date) at 6:31 AM. **Rank key: #1 = fewest fantasy points allowed to that position (toughest), #32 = most (easiest).**
- 2nd-source projection: data/projections/week-7.json (FantasyPros PPR consensus, pulled Fri Oct 23 9:22 AM).
- Ceilings: FantasyPros Week 7 PPR "high" projection (public page shows top 10 per position only, pulled 6:27 AM) where listed; otherwise ESPN 2026 weekly actuals best/worst (a 0.0 week can be a game not played).
- Vegas: DraftKings line as carried on ESPN's public scoreboard API, pulled 6:28 AM. Implied team total = total/2 ± spread/2.
- Weather: Open-Meteo hourly forecast at stadium coordinates, pulled 6:29 AM (temp, sustained wind, gusts, precip). ESPN/AccuWeather sky + temp from the same scoreboard pull.
- News: NFL.com, Steelers.com, Packers.com, Inquirer, NBC Sports, CBS/RotoWire, PhillyVoice, FantasyPros, PFN (fetched 6:30–6:45 AM).
- Blitz's card weekly/cards/week-7-must-win-analysis.md (f387ef0) was read for the current lineup. Not edited.
- **agents/assistant/work/espn-rules-canon.md does not exist on main (UNKNOWN).** League rules here come from ESPN mSettings and PLAYBOOK.md: traditional waivers with 24-hour wait, per-game locks, waivers run 11 AM on Mon/Wed–Sun, and no add or drop without Ken's command.

## 0. Matchup snapshot (ESPN, 6:25 AM)
- **ESPN projected totals: us 115.87, them 125.60.** They have 23.7 banked (Luther Burden, FLEX, played Thursday). We have 0 banked. Henry (14.1) and Henderson (4.3) scored on our bench and don't count. Drake Maye's 27.44 is on their bench and doesn't count.
- Sum of our starters' ESPN projections = 115.88 (matches ESPN). Their sum is 125.60, using Burden's actual.
- Locks: only Henry, Henderson (ours), Maye, and Burden (theirs) are lineupLocked/rosterLocked = true. Every other player on both rosters is false/false.

## 1. Our players still to play
| Player | Pos | ESPN slot | ESPN status | Kickoff | Opp + ESPN rank vs pos | ESPN W7 proj | 2nd source (FP, data/projections) | Ceiling | Vegas (DraftKings via ESPN) |
|---|---|---|---|---|---|---|---|---|---|
| Drake London | WR | WR | ACTIVE | Sun Oct 25, 12:00 PM CT | SF #10 (29.8 pts/g to WR) | 17.16 | 16.50 | FantasyPros high 22.9; ESPN 2026 weekly actuals best 28.4 / worst 5.5 (wks 1–6: 5.5, 8.9, 28.4, 14.6, 18.8, 12.2) | SF -2.5 / O-U 49.5 / ATL implied 23.5 |
| Garrett Wilson | WR | WR | ACTIVE | Sun Oct 25, 12:00 PM CT | MIA #3 (23.2 pts/g to WR) | 15.09 | 15.80 | ESPN 2026 weekly actuals best 26.7 / worst 5.7 (wks 1–6: 13.9, 16.7, 26.7, 5.7, 23.4, 8.4) | NYJ -4.5 / O-U 39.5 / NYJ implied 22.0 |
| Kyle Pitts Sr. | TE | TE | ACTIVE | Sun Oct 25, 12:00 PM CT | SF #4 (9.2 pts/g to TE) | 9.82 | 8.80 | ESPN 2026 weekly actuals best 23.0 / worst 0.0 (wks 1–6: 0.0, 2.5, 1.5, 7.7, 15.2, 23.0) | SF -2.5 / O-U 49.5 / ATL implied 23.5 |
| Dallas Goedert | TE | Bench | QUESTIONABLE | Mon Oct 26, 7:15 PM CT | DAL #17 (12.8 pts/g to TE) | 11.33 | 10.90 | FantasyPros high 15.5; ESPN 2026 weekly actuals best 23.7 / worst 0.0 (wks 1–6: 23.7, 1.4, 0.0, 0.0, 9.8, 12.1) | DAL -4.5 / O-U 44.5 / PHI implied 20.0 |
| Josh Jacobs | RB | RB | DAY_TO_DAY | Sun Oct 25, 3:25 PM CT | DET #8 (18.7 pts/g to RB) | 12.64 | 12.70 | ESPN 2026 weekly actuals best 0.0 / worst 0.0 (wks 1–6: 0.0, 0.0, 0.0, 0.0, 0.0, 0.0) | DET -3 / O-U 53.5 / GB implied 25.25 |
| Steelers D/ST | D/ST | D/ST | n/a (D/ST) | Sun Oct 25, 8:30 AM CT | NO #20 (6.5 pts/g to D/ST) | 6.37 | 6.50 | ESPN 2026 weekly actuals best 19.0 / worst 1.0 (wks 1–6: 19.0, 8.0, 4.0, 5.0, 1.0, 11.0) | PIT -3 / O-U 44.5 / PIT implied 23.75 |
| Kyler Murray | QB | QB | ACTIVE | Sun Oct 25, 12:00 PM CT | IND #22 (18.4 pts/g to QB) | 18.00 | 17.60 | ESPN 2026 weekly actuals best 18.3 / worst -0.4 (wks 1–6: -0.4, 0.0, 10.4, 11.5, 18.3) | MIN -6.5 / O-U 41.5 / MIN implied 24.0 |
| Ollie Gordon II | RB | Bench | ACTIVE | Sun Oct 25, 12:00 PM CT | NYJ #19 (21.9 pts/g to RB) | 11.80 | 10.90 | ESPN 2026 weekly actuals best 18.0 / worst 0.0 (wks 1–6: 0.0, 0.7, 14.5, 18.0, 14.8) | NYJ -4.5 / O-U 39.5 / MIA implied 17.5 |
| RJ Harvey | RB | Bench | ACTIVE | Sun Oct 25, 3:05 PM CT | ARI #16 (20.6 pts/g to RB) | 11.43 | 10.40 | ESPN 2026 weekly actuals best 19.3 / worst 0.0 (wks 1–6: 8.1, 0.0, 10.7, 19.3, 0.7, 14.6) | DEN -4.5 / O-U 43.5 / DEN implied 24.0 |
| Germie Bernard | WR | FLEX | ACTIVE | Sun Oct 25, 8:30 AM CT | NO #16 (31.6 pts/g to WR) | 13.39 | 12.10 | ESPN 2026 weekly actuals best 25.7 / worst 0.0 (wks 1–6: 0.0, 7.5, 2.4, 3.1, 14.4, 25.7) | PIT -3 / O-U 44.5 / PIT implied 23.75 |
| Matt Gay | K | K | ACTIVE | Sun Oct 25, 3:25 PM CT | LAR #26 (10.2 pts/g to K) | 9.73 | 8.20 | FantasyPros high 9.7; ESPN 2026 weekly actuals best 16.0 / worst 5.0 (wks 1–6: 10.0, 8.0, 12.0, 16.0, 5.0, 12.0) | LAR -3 / O-U 48.5 / LV implied 22.75 |
| J.J. McCarthy | QB | Bench | ACTIVE | Sun Oct 25, 12:00 PM CT | HOU #21 (18.4 pts/g to QB) | 16.39 | 14.20 | ESPN 2026 weekly actuals best 16.3 / worst 0.0 (wks 1–6: 0.0, 0.0, 0.0, 0.0, 0.2, 16.3) | HOU -10.5 / O-U 42.5 / NYG implied 16.0 |
| Woody Marks | RB | RB | ACTIVE | Sun Oct 25, 12:00 PM CT | NYG #18 (21.7 pts/g to RB) | 13.68 | 13.40 | ESPN 2026 weekly actuals best 12.5 / worst 5.0 (wks 1–6: 5.0, 8.5, 9.1, 8.2, 12.5, 10.1) | HOU -10.5 / O-U 42.5 / HOU implied 26.5 |

Not listed: Hunter Henry (played, 14.1, Bench, locked), TreVeyon Henderson (played, 4.3, Bench, locked), Jakobi Meyers (JAX bye, 0.0), Travis Etienne Jr. (IR slot, ESPN INJURY_RESERVE).

ESPN rest-of-season projections (last season-projection value in mRoster): Murray 202.3, McCarthy 192.7, London 188.5, Wilson 160.7, Gordon 149.4, Jacobs 144.1, Harvey 119.2, Meyers 119.5, Goedert 113.3, Pitts 107.8, Gay 104.2, Marks 97.4, Henry 88.1, Steelers 81.0, Henderson 79.8, Bernard 133.0 (only one value returned, so it may be full-season).

## 2. Games, lines, implied totals (DraftKings via ESPN, 6:28 AM CT)
| Game | Venue | Roof | Spread | O/U | Implied |
|---|---|---|---|---|---|
| PIT VS NO | Stade de France | OUTDOOR | PIT -3 | 44.5 | PIT 23.75 / NO 20.75 |
| SF @ ATL | Mercedes-Benz Stadium | dome/roof | SF -2.5 | 49.5 | SF 26.0 / ATL 23.5 |
| CLE @ TEN | Nissan Stadium | OUTDOOR | CLE -2.5 | 36.5 | CLE 19.5 / TEN 17.0 |
| IND @ MIN | U.S. Bank Stadium | dome/roof | MIN -6.5 | 41.5 | IND 17.5 / MIN 24.0 |
| MIA @ NYJ | MetLife Stadium | OUTDOOR | NYJ -4.5 | 39.5 | MIA 17.5 / NYJ 22.0 |
| TB @ CAR | Bank of America Stadium | OUTDOOR | CAR -3 | 44.5 | TB 20.75 / CAR 23.75 |
| CIN @ BAL | M&T Bank Stadium | OUTDOOR | CIN -1.5 | 48.5 | CIN 25.0 / BAL 23.5 |
| NYG @ HOU | Reliant Stadium | dome/roof | HOU -10.5 | 42.5 | NYG 16.0 / HOU 26.5 |
| DEN @ ARI | State Farm Stadium | dome/roof | DEN -4.5 | 43.5 | DEN 24.0 / ARI 19.5 |
| GB @ DET | Ford Field | dome/roof | DET -3 | 53.5 | GB 25.25 / DET 28.25 |
| LAR @ LV | Allegiant Stadium | dome/roof | LAR -3 | 48.5 | LAR 25.75 / LV 22.75 |
| KC @ SEA | Lumen Field | OUTDOOR | SEA -3 | 42.5 | KC 19.75 / SEA 22.75 |
| DAL @ PHI | Lincoln Financial Field | OUTDOOR | DAL -4.5 | 44.5 | DAL 24.5 / PHI 20.0 |

Our players by game: PIT@NO (Paris, 8:30 AM): Bernard, Steelers D/ST. SF@ATL: London, Pitts. MIA@NYJ: Wilson, Gordon. IND@MIN: Murray. NYG@HOU: Marks, McCarthy. DEN@ARI: Harvey. GB@DET (highest total on the slate, 53.5): Jacobs. LAR@LV: Gay. DAL@PHI (Mon): Goedert.

## 3. QB and play-caller changes on teams where we have players still to play
- **PHI: QB change.** Jalen Hurts is on IR (ESPN tag INJURY_RESERVE; blood clots, expected out for the season per Inquirer and Cowboys.com). Tanner McKee starts his 2nd straight game (W6: 26-for-45, 215 yards, 1 TD). ESPN projects McKee at 14.7. Sean Mannion stays as play-caller (Sirianni endorsed him on Oct 19). Inquirer: "everything is on the table," and PHI ranks 30th in yards and 29th in points. **Affects Goedert.**
- **NYG: QB change.** J.J. McCarthy (ours, bench) starts Week 7 over Jameis Winston (NFL.com; Harbaugh confirmed Wed). Dart is on IR. We have no NYG pass catcher (Marks is HOU and faces this NYG offense, not in it). It affects McCarthy himself (ESPN 16.39).
- **DEN: play-caller change (Oct 8, already in effect).** Sean Payton took play-calling back from OC Davis Webb (NBC Sports and Schefter). **Affects Harvey** (no pass catcher of ours on DEN).
- **TB (not our team, but it sets the Panthers D/ST free-agent comparison):** Baker Mayfield starts vs CAR after missing three games (NFL.com, Bowles Friday). His ESPN tag is QUESTIONABLE.
- ATL (Penix starting since W3), NYJ (Geno Smith), MIN (Murray, rested off a W6 bye), PIT (Rodgers), MIA (Willis), GB (Love, back, full practice Thu/Fri), LV (Cousins), HOU (Stroud): no Week 7 QB change found. No play-caller change found for these teams in the search (NOT exhaustive; this is a no-result from one web search, not a confirmed "none").

## 4. Weather, outdoor games (Open-Meteo hourly, pulled 6:29 AM CT; kickoff hour onward)
- **PIT vs NO, Stade de France, Paris, 8:30 AM CT. WIND FLAG:** about 61°F, **sustained wind 15.5–16.4 mph, gusts 33–35 mph** from 13:00 to 15:00 UTC (8:00–10:00 AM CT), 0% precip. ESPN's scoreboard has no weather entry for this game. Affects Bernard (passing game) and Steelers D/ST. Note: Blitz's card calls it "light wind in Paris." This forecast does not say that.
- MIA @ NYJ, MetLife, 12:00 PM: 64–66°F, wind 2–5 mph, 0% precip (ESPN/AccuWeather: Sunny 64). Wilson, Gordon.
- DAL @ PHI, Lincoln Financial, Mon 7:15 PM: 59–62°F, wind 4–6 mph, gusts 13–17, 0% precip. Goedert.
- Opponent outdoor games: KC @ SEA, Lumen, 7:20 PM: 50–60°F, wind 2–5 mph, precip chance 22–27% (Worthy). CLE @ TEN, Nissan: 72–76°F, calm (Helm).
- Dome/roof (no weather factor; retractable-roof open/closed status not checked): ATL, MIN, HOU, ARI, DET, LV.

## 5. Free agents (ESPN W7 projection; unplayed players only. Bears and Patriots D/ST played Thursday and are excluded)
**K (our starter: Matt Gay 9.73 ESPN / 8.2 FP):**
1. Ryan Fitzgerald (CAR vs TB, outdoor) 9.48 ESPN / FP 8.17 (FP high 9.8). 2026 best/worst 15/8.
2. Chad Ryland (ARI vs DEN, roof) 9.46 ESPN. FP UNKNOWN. 2026 best/worst 19/1.
3. Trey Smack (GB @ DET, dome) 9.27 ESPN. FP UNKNOWN. 2026 best/worst 13/1.
None beats Gay on ESPN projection. Ryland's best week (19) is higher than Gay's best (16).

**D/ST (our starter: Steelers 6.37 ESPN / 6.5 FP; 2026 best 19):**
1. Panthers (vs TB, Mayfield returning) 6.12. 2026 best/worst 24/−8.
2. Buccaneers (@ CAR) 4.70. Best/worst 8/4.
3. Dolphins (@ NYJ) 4.67. Best/worst 6/−4.
None beats the Steelers on projection. The Panthers' best week (24) is higher than the Steelers' best (19).

**Backup QB (our backup: McCarthy 16.39):** Geno Smith (NYJ) 15.99 (best 26.0), Baker Mayfield (TB, QUESTIONABLE) 15.12, Michael Penix Jr. (ATL) 14.58 (best 23.1), Jacoby Brissett (ARI) 14.24 (best 25.6). None beats Murray (18.00) or McCarthy on projection. Geno's (26.0) and Brissett's (25.6) best weeks are higher than Murray's best (18.3).

**Other positions vs the starter he'd replace:**
- RB: top FA Bam Knight (ARI) 8.06. Below Jacobs 12.64 and Marks 13.68. Jacobs has no 2026 games, so a ceiling comparison is UNKNOWN.
- WR/FLEX: top FA Ted Hurst III (TB) 10.55, Darius Cooper (PHI) 9.85, Makai Lemon (PHI) 9.10, Jaylin Noel (HOU) 8.48 (best 20.7). All below Bernard 13.39 on projection and on best week (Bernard 25.7).
- TE (Pitts 9.82): Colby Parkinson (LAR) 9.29, Mark Andrews (BAL, FREEAGENT, not waivers) 8.81, Darnell Washington (PIT) 8.58, Dalton Schultz (HOU) 8.55 (best 26.0, higher than Pitts' best 23.0), Tyler Higbee (LAR) 8.37. None beats Pitts on projection.
- **Result: no free agent at any position projects above the starter he'd replace (ESPN).** Ceiling-only beats (2026 best week): Ryland > Gay, Panthers > Steelers, Geno/Brissett > Murray, Schultz > Pitts.

**Drop candidates and lock status** (all rosterLocked = false unless noted): Jakobi Meyers (bye, ROS 119.5; in the Barkley offer per Blitz's card), J.J. McCarthy (backup QB, ROS 192.7), Ollie Gordon II (ROS 149.4; in the Barkley offer per Blitz's card), RJ Harvey (ROS 119.2; in the Tuesday Goff offer). Locked and can't be dropped this week: Hunter Henry (in the Goff offer), TreVeyon Henderson. No add or drop happens without Ken's command (PLAYBOOK.md).

## 6. Opponent (team 11) projected starting lineup
| Slot | Player | ESPN status | Kickoff | Opp + ESPN rank vs pos | ESPN W7 proj / actual |
|---|---|---|---|---|---|
| RB | Jonathan Taylor (IND) | ACTIVE | Sun Oct 25, 12:00 PM CT | MIN #1 (14.3 pts/g to RB) | 15.23 |
| RB | Javonte Williams (DAL) | ACTIVE | Mon Oct 26, 7:15 PM CT | PHI #15 (20.5 pts/g to RB) | 16.63 |
| QB | Matthew Stafford (LAR) | ACTIVE | Sun Oct 25, 3:25 PM CT | LV #27 (20.5 pts/g to QB) | 18.59 |
| D/ST | Texans D/ST (HOU) | n/a (D/ST) | Sun Oct 25, 12:00 PM CT | NYG #22 (6.8 pts/g to D/ST) | 7.20 |
| WR | Matthew Golden (GB) | ACTIVE | Sun Oct 25, 3:25 PM CT | DET #30 (40.8 pts/g to WR) | 16.89 |
| WR | Xavier Worthy (KC) | ACTIVE | Sun Oct 25, 7:20 PM CT | SEA #2 (22.7 pts/g to WR) | 12.41 |
| FLEX | Luther Burden III (CHI) | ACTIVE | Thu Oct 22, 7:15 PM CT | NE #17 (31.7 pts/g to WR) | ACTUAL 23.70 (played, locked) |
| TE | Gunnar Helm (TEN) | ACTIVE | Sun Oct 25, 12:00 PM CT | CLE #20 (14.8 pts/g to TE) | 4.13 |
| K | Dominic Zvada (NYG) | ACTIVE | Sun Oct 25, 12:00 PM CT | HOU #28 (10.8 pts/g to K) | 10.82 |

Their total is 125.60 (23.70 actual + 101.90 still projected). Ours is 115.87. ESPN injury tags on their starters: all ACTIVE (D/ST has no tag). Their notable bench: Maye (played, 27.44, locked), Keenan Allen 8.95, McPherson K 7.43, Lions D/ST 4.42, Tuten (JAX bye).

## 7. Close calls: bench player within 1.5 ESPN points of the starter (ESPN projections, 6:25 AM)
| Slot | Starter (ESPN / FP) | Bench option (ESPN / FP) | Gap |
|---|---|---|---|
| RB2 | Jacobs 12.64 / 12.70 | **Gordon 11.80 / 10.90** | 0.84 within |
| RB2 | Jacobs 12.64 / 12.70 | **Harvey 11.43 / 10.40** | 1.21 within |
| TE | Pitts 9.82 / 8.80 | Goedert 11.33 / 10.90 | Bench is **1.51 HIGHER** (just outside 1.5, bench above starter) |
| QB | Murray 18.00 / 17.60 | McCarthy 16.39 / 14.20 | 1.61 (outside) |
| FLEX | Bernard 13.39 / 12.10 | Gordon 11.80 | 1.59 (outside) |
| RB1 | Marks 13.68 / 13.40 | Gordon 11.80 | 1.88 (outside) |
K, D/ST: no bench option. WR: only bench WR is Meyers (bye).

## 8. Blitz's three focus items

### A. Jacobs vs Gordon vs Harvey (RB2)
- **Jacobs (GB @ DET, Sun 3:25 PM CT).** ESPN tag DAY_TO_DAY. ESPN 12.64, FP 12.70. **No 2026 games played** (six 0.0 weeks), so his ceiling from weekly actuals is UNKNOWN. ROS 144.1. DET is #8 vs RB (18.7 pts/g allowed). Line DET −3, O/U 53.5 (highest total on the slate), GB implied 25.25. Dome. Notes only: he returned this week from a six-week stay on the **Commissioner's Exempt List**. NBC/PFT (Oct 23 12:27 PM ET) said he "is currently exempt from the 53-man roster." LaFleur says he's on track to play pending Friday practice. FantasyPros (Oct 23 11:35 PM ET): practiced all week, no injury designation, workload in doubt, maybe 10–12 touches. **Rule note:** the Commissioner's Exempt List is one of the official can't-play lists. If GB has not activated him to the 53-man roster by kickoff, that alone benches him. Check the NFL transaction wire or GB inactives (around 1:55 PM CT). Activation not confirmed in my sources as of 6:45 AM CT (UNKNOWN).
- **Gordon (MIA @ NYJ, Sun 12:00 PM CT).** ACTIVE. ESPN 11.80, FP 10.90. 2026 best 18.0 / worst 0.0 (14.5, 18.0, 14.8 in W3–W5; MIA bye W6). Snaps 84/56/65% W3–W5 (data/usage). NYJ is #19 vs RB (21.9). NYJ −4.5, O/U 39.5 (lowest total among our games), MIA implied 17.5. Outdoor, calm, 64°F. He locks at noon, before GB's inactives come out.
- **Harvey (DEN @ ARI, Sun 3:05 PM CT).** ACTIVE. ESPN 11.43, FP 10.40. 2026 best 19.3 / worst 0.0. Snaps 36–44% W3–W6 in a committee with Dobbins. ARI is #16 vs RB (20.6). DEN −4.5, O/U 43.5, DEN implied 24.0. Roof. Payton has called plays since Oct 8. His kickoff (3:05) is before GB-DET (3:25), so he locks before Jacobs.

### B. Goedert and the Eagles' injury report
- ESPN tag: **QUESTIONABLE**. ESPN 11.33, FP 10.90, FP high 15.5. 2026 best 23.7, with 0.0 in W3–W4 (missed with a right MCL sprain per CBS/RotoWire). Plays Mon Oct 26, 7:15 PM CT vs DAL (#17 vs TE, 12.8 pts/g). DAL −4.5, O/U 44.5, **PHI implied 20.0**. Outdoor, 59–62°F, wind 4–6 mph.
- Practice: **DNP Thursday, DNP Friday (knee)** (Inquirer, NBC Sports Philadelphia, PhillyVoice). CBS/RotoWire: may be tied to the earlier MCL sprain. NBC: as of Thursday the Inquirer's McLane reported "optimism." **The Eagles practice Saturday and issue final game designations Saturday afternoon** (Inquirer). Zach Ertz is a possible practice-squad elevation if Goedert sits (Inquirer).
- Other PHI pass catchers: DeVonta Smith (hamstring) DNP/DNP, Dontayvion Wicks (ankle) DNP/DNP, Barkley (hamstring) limited/limited. QB is McKee (Hurts on IR). PHI ranks 30th in yards and 29th in points.
- Timing fact: Goedert's game is Monday night. Every bench alternative will have locked by then.

### C. Bernard and the Steelers (PIT vs NO, Paris, Sun 8:30 AM CT)
- **Bernard:** ACTIVE, FLEX. ESPN 13.39, FP 12.10. 2026 best 25.7 (W6: 11 catches, 87 yards, game-winning OT TD per Steelers.com) / worst 0.0. Snaps 92% W5, 94% W6. NO is #16 vs WR (31.6 pts/g). PIT −3, O/U 44.5, PIT implied 23.75. Steelers WR room: Roman Wilson and Michael Pittman Jr. on IR, Ben Skowronek OUT (calf). Steelers.com's official report does not list DK Metcalf.
- **Steelers D/ST:** ESPN 6.37, FP 6.5. 2026 best 19 / worst 1. NO is #20 vs D/ST (6.5 pts/g allowed to D/ST). NO QB Tyler Shough (left hand) was full participant Fri. Steelers: CB Brandin Echols OUT, S DeShon Elliott Q. Jalen Ramsey, Watt, Highsmith, and Heyward were all full participants Friday (estimated report).
- **Paris wind (Open-Meteo): sustained 15–16 mph, gusts 33–35 mph** during the game window.
- Timing: this game kicks off at 8:30 AM CT and locks before the 9:53 AM dead-man. Inactives come out about 7:00 AM CT (90 minutes before kickoff). The best FA D/ST (Panthers 6.12) plays at noon.

## UNKNOWNs
- agents/assistant/work/espn-rules-canon.md: not on main.
- FantasyPros high projections: the public page shows only the top 10 per position. Highs are missing for Wilson, Pitts, Murray, Gordon, Harvey, Bernard, Marks, McCarthy, the Steelers, and Jacobs. ESPN weekly actuals are used instead, and Jacobs has none.
- Jacobs' 53-man activation from the Commissioner's Exempt List: not confirmed as of 6:45 AM CT.
- Goedert's final game designation: due Saturday afternoon (Eagles).
- Play-caller changes: one web search only. Not an exhaustive check.
- Retractable roofs (ATL, HOU, ARI): open/closed status not checked.
