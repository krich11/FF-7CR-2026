# Opponent study: Weeks 1–5 (7 Creeks Armchair Quarterbacks, ESPN PPR)

Pulled read-only from ESPN on Sun Oct 11, 2026, about 9 PM CT. Weeks 1–4 are final. Week 5 isn't final yet, so its lineups are left out of the lineup and luck numbers, but its transactions are counted. QBZ is in the tables only for comparison.

Data files in this folder:
- `team_summary.csv`: one row per team with every number in the table below.
- `transactions.csv`: every add, drop, waiver claim (won, lost, or canceled) and trade, with times in CT.
- `lineups_by_week.csv`: for each team and week, the actual score, the best possible score, the score of ESPN's projected-best lineup, and any starters with a zero projection.

## How to read the numbers
- **Bench pts left/wk**: the best possible lineup (in hindsight) minus the actual score, averaged over Weeks 1–4.
- **Starters = ESPN best**: how many of the team's starters were also in the lineup ESPN's own projections would have picked. Counted over 4 weeks × 9 slots = 36.
- **Dead starts**: a starter ESPN projected for 0 points, meaning he was on bye or ruled OUT before kickoff.
- **Chase adds**: how many of the team's pickups scored 15+ PPR points the week before. Shown as chases / pickups we have a prior week for.
- **All-play / Exp. W / Luck**: the team's record if it played every other team every week, the wins that record implies over 4 games, and actual wins minus expected wins. Positive luck means a team has won more than its scoring deserves.

## Key stats (Weeks 1–4, sorted by points for)
| Team | W-L | PF | PA | All-play | Exp. W | Luck | Adds (FA/WW) | Claims lost | RB adds | D/ST adds | K adds | Chase adds* | Bench pts left/wk | Starters = ESPN best | Dead starts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MBB | 4-0 | 555.4 | 401.3 | 36-8 | 3.27 | +0.73 | 2 (1/1) | 0 | 1 | 1 | 0 | 0/2 | 19.0 | 33/36 | 0 |
| PP | 3-1 | 531.7 | 465.4 | 35-9 | 3.18 | -0.18 | 4 (2/2) | 1 | 1 | 1 | 0 | 1/4 | 27.2 | 35/36 | 1 |
| TE | 4-0 | 520.4 | 386.5 | 31-13 | 2.82 | +1.18 | 11 (6/5) | 3 | 0 | 2 | 1 | 5/9 | 18.0 | 32/36 | 0 |
| FR | 3-1 | 510.2 | 436.5 | 27-17 | 2.45 | +0.55 | 6 (3/3) | 2 | 0 | 2 | 0 | 2/6 | 27.0 | 35/36 | 0 |
| CDS | 4-0 | 502.6 | 386.9 | 27-17 | 2.45 | +1.55 | 21 (11/10) | 10 | 3 | 6 | 2 | 2/15 | 9.5 | 34/36 | 0 |
| LL | 1-3 | 466.5 | 487.4 | 20-24 | 1.82 | -0.82 | 6 (5/1) | 0 | 1 | 3 | 0 | 0/5 | 23.3 | 31/36 | 0 |
| DDT | 0-4 | 447.6 | 549.7 | 20-24 | 1.82 | -1.82 | 4 (4/0) | 0 | 0 | 0 | 1 | 1/2 | 20.2 | 26/36 | 0 |
| GGT | 1-3 | 438.2 | 480.1 | 18-26 | 1.64 | -0.64 | 2 (2/0) | 0 | 0 | 0 | 0 | 1/2 | 18.2 | 33/36 | 0 |
| TCO | 1-3 | 436.0 | 503.0 | 18-26 | 1.64 | -0.64 | 7 (3/4) | 2 | 0 | 1 | 1 | 4/7 | 22.4 | 34/36 | 0 |
| LY | 2-2 | 418.0 | 474.9 | 16-28 | 1.45 | +0.55 | 6 (1/5) | 0 | 2 | 2 | 0 | 2/6 | 19.1 | 30/36 | 1 |
| QBZ | 1-3 | 395.2 | 506.3 | 12-32 | 1.09 | -0.09 | 10 (8/2) | 0 | 2 | 1 | 0 | 3/7 | 13.4 | 33/36 | 0 |
| BuB | 0-4 | 362.3 | 506.2 | 4-40 | 0.36 | -0.36 | 2 (2/0) | 0 | 0 | 2 | 0 | 0/2 | 32.0 | 31/36 | 0 |

## How waivers actually work here (mSettings + observed)
- The league uses traditional waivers with no FAAB. Waiver order resets each week (`waiverOrderReset=true`), and dropped players sit on waivers for 24 hours.
- **Claims are processed at about 2:00–2:50 AM CT.** Out of 51 processed claims, 40 were processed Wednesday morning. The rest were processed Thu (6), Fri (4) and Sat (1), for players who were dropped during the week. The `waiverProcessHour: 11` value in the settings does not match these observed times. Trust the observed times.
- **Wednesday 5–8 AM CT is when opponents grab free agents.** Players who go unclaimed become free agents at about 2 AM Wednesday. CDS, TCO, LY, GGT and DDT have all made free-agent adds between 5:14 and 8:05 AM on a Wednesday.
- ESPN only shows when other teams' claims were processed, not when they were filed. Filing times are only visible for our own claims.

## League-wide patterns
1. **The Wednesday-morning claim run decides who gets the hot free agents.** The most contested players so far:
   - Vikings D/ST, Week 4: claimed by 5 teams (TCO won it; CDS, FR, PP and TE lost).
   - Devaughn Vele, Week 2: claimed by 3 teams with 4 claims (PP won it; TE lost twice and CDS once).
   - Chiefs D/ST, Week 2: TE won it; CDS and FR lost.
   - Denzel Boston, Week 3: TE won it; CDS lost.
   - Kenyon Sadiq, Week 4: CDS won it; TCO lost.
2. **Running backs are not the contested position.** Only 8 RB adds by other teams in Weeks 1–5. The only lost RB claim was TCO's for Ollie Gordon in Week 4, and we got him. CDS (Mixon) and TE (Bigsby) each canceled an RB claim before it was processed.
3. **Most of the league follows ESPN's projections.** 8 of the 11 opponents started ESPN's projected-best player in at least 33 of 36 slots. DDT (26/36) and LY (30/36) override ESPN the most. LL and BuB (31/36) override it a little.
4. **Defense streaming is common, kicker streaming is rare.** Other teams added 20 D/STs, led by CDS with 6 and LL with 3. They added only 5 kickers, 2 of them by CDS.
5. **Dead starts are rare.** There were only 2 in 44 team-weeks: PP started Nico Collins in Week 2, and LY started Rico Dowdle in Week 3.
6. **Trading is almost nonexistent.** Our two trades with LY are the only completed trades. Other offers were declined (2 to FR, 1 to PP), and TCO canceled an offer to FR (Hurts for Deebo).

## Team profiles
**TE – Texas Endgame (4-0, but scores more like a 2.8-win team, so +1.2 lucky).** Chases last week's points: 5 of his 9 pickups scored 15+ the week before (Vele, Boston, Brissett, Wicks, Cooper). He does a lot of free-agent work late in the week, Thursday and Friday evenings between 6:26 and 8:16 PM CT (Wicks, Reichard, Cooper, Geno Smith). He turns over QBs (Darnold, Brissett, Watson, Caleb Williams, Geno) and streams defenses. He follows projections closely (32/36). His pickups produced only 28 points as starters, so his record comes from his drafted roster and luck, not his moves.

**PP – Patton's Posse (3-1, all-play 35-9).** The second-strongest team on real scoring. He makes few moves (4 adds). He starts ESPN's projected-best lineup almost exactly (35/36), yet leaves 27 points a week on the bench, which is normal week-to-week swing for a deep roster. He had one dead start (Nico Collins, Week 2). He won Vele on waivers, which netted 6.9 points.

**FR – Fantasy Rookie No More (3-1, +0.55 lucky).** Follows projections (35/36). His moves have been about QBs and defenses: Stroud, then Mariota, then Watson, plus the Chargers and Bills D/STs. He lost the Chiefs and Vikings D/ST claims. He has declined 2 trade offers. Nothing unusual otherwise.

**CDS – Charlie Don't Surf (4-0, but scores like a 2.45-win team, so +1.55, the luckiest team in the league).** The most active manager by far: 21 adds and 22 waiver claims, 10 of which he lost. He streams defenses every week (6 D/ST adds plus 7 more lost D/ST claims) and has rotated 3 kickers. He also wastes moves: 3 free-agent adds in 26 minutes on Friday Sep 25 (7:41–8:07 PM CT), and Woody Marks dropped for Rachaad White, who was dropped again. Only 2 of his 15 pickups were chases. He sets the tightest lineup in the league, leaving 9.5 points a week on the bench. He is the most likely to regress.

**BuB – Buck up Buttercup! (0-4, all-play 4-40).** The weakest roster in the league, and his record isn't bad luck. He has made 2 moves, both Thursday free-agent D/ST swaps, and filed 0 waiver claims. He leaves 32 points a week on the bench, the most in the league. He's effectively inactive.

**LY – Lazy Yorkie (2-2, +0.55 lucky).** Our trade partner, who sent us Henderson and Harvey. Adds mostly through the Wednesday waiver run (5 of 6), winning all 5 claims, including RBs Braelon Allen and Tyler Allgeier. He overrides ESPN's projections the second-most (30/36, 21.6 projected points given up) and had one dead start (Dowdle, Week 3). He makes more avoidable lineup mistakes than any other active team.

**GGT – The gg Team (1-3, -0.64 unlucky).** Has made 2 free-agent adds, both on a Wednesday, and filed no waiver claims. Kirk Cousins scored 22.6 as a starter, his one useful pickup. Low effort and mostly random.

**TCO – The Chosen Ones (1-3, -0.64 unlucky).** All 7 adds were made on Wednesdays, early in the morning (5:14 AM CT) or right after waivers clear. Chases last week's points: 4 of 7 pickups had scored 15+ the week before (Shrader, Vikings D/ST, Raymond, Doubs). He churns receivers, for example dropping Doubs for Hollins and then claiming Doubs back. He offered Hurts for Deebo and then canceled. He filed the only RB claim we beat (Ollie Gordon).

**LL – La Lightning (1-3, -0.82 unlucky).** Mostly free-agent adds (5 of 6). Streams defenses (3) and TEs. None of his 5 pickups chased last week's points. His pickups produced 31.4 points as starters. He scores better than his record shows, so he is likely to improve.

**DDT – David's Daring Team (0-4, but should be about 1.8, the unluckiest team at -1.82).** Overrides ESPN's projections the most in the league (26/36, giving up 19.6 projected points), so he trusts his own reads. His best move was picking up kicker McPherson, who scored 47 points over 4 starts. He has filed no waiver claims; all 4 adds were free agents, made on scattered days. His scoring should bounce back, so don't treat him as an easy win.

**MBB – Mitch's Badass Bunch (4-0, all-play 36-8, the best team in the league).** Makes almost no moves: 2 adds, Singletary and the Cowboys D/ST. He follows projections (33/36). He wins with his drafted roster and doesn't need the waiver wire.

## Edges we can use
- **Running backs:** there's little competition. Only CDS (3 adds) and LY (2) regularly pick up RBs. If we want an RB, a waiver claim filed by Tuesday night should get him.
- **Contested defenses and the week's hot receiver:** expect 3–5 claims. Our 1-3 record should give us early waiver priority after the weekly reset. Use it on players worth fighting for, not on a defense.
- **Free agents after waivers clear:** CDS, TCO, LY, GGT and DDT pick between 5 and 8 AM CT on Wednesday. If a player goes unclaimed, add him at about 2:05 AM Wednesday, or file a claim the night before.
- **Who will regress:** CDS (+1.55) and TE (+1.18) are 4-0 on luck. MBB and PP are the teams that are actually strong.
- **Trade partners:** LY is the only manager who accepts trades. FR and PP have declined offers.

## QBZ (us) against the league
Same method as above. Ranks are out of 12 (1 = most, or best where marked). Weeks 1–4 unless noted.

| Metric | QBZ | Rank / context |
|---|---|---|
| Record, points for / against | 1-3, 395.2 / 506.3 | 11th in points for |
| All-play record, expected wins, luck | 12-32, 1.09, -0.09 | 11th in expected wins; luck is about zero (6th) |
| Adds (free agent / waiver) | 10 (8 / 2) | 3rd most (CDS 21, TE 11) |
| Waiver claims | 4 filed: 2 won (Murray, Gordon), 1 canceled (Darnold, Week 1), 1 still pending (Marks for Pittman, filed Oct 11 at 8:53 PM CT). 0 lost. | Middle of the pack |
| When we add | Fri 4, Wed 4, Sat 1, Sun 1. Three Friday-night adds in Week 3 between 8:35 and 9:55 PM CT. | A late-week mover, like TE |
| D/ST and K streaming | 1 D/ST (Panthers), 0 K | 10th in D/ST adds, tied last in K adds; we don't stream |
| Chase adds (pickup scored 15+ the week before) | 3 of 7 | Middle of the pack (TE 5/9, TCO 4/7) |
| Starters that match ESPN's projected-best lineup | 33/36 | Tied 5th–7th; projected points given up 6.3 |
| Bench points left (best possible minus actual) by week | W1 6.9, W2 1.1, W3 28.9, W4 16.8 (W5 so far 14.9) | 13.4 a week, **2nd best** (CDS 9.5) |
| Starters on bye or ruled out | 0 | Clean |
| Pickups' points as starters | 66.6 | **1st** (CDS 52.3, DDT 47.0) |
| Add-vs-drop swaps (points scored after the swap, through Week 4) | 6 swaps, add outscored drop in 4; adds 133.4 vs drops 71.8 = **+61.6** | **1st** (PP +50.9; TE -38.0; CDS -122.5) |
| Trades | 2 accepted, both with LY: Henderson for Shaheed, and Harvey for Bateman | Only manager with a completed trade. Week 4: we got 23.5, gave up 18.9 (Week 5 partial) |

The 6 add-for-drop swaps (points from the swap week through Week 4):
- Week 1: Tre Tucker 44.3 vs Sam Darnold 41.5 (win).
- Week 3: Jacoby Brissett 36.0 vs Zach Charbonnet 0.0 (win).
- Week 3: Kyler Murray 21.9 vs Jonathon Brooks 0.0 (win).
- Week 3: Panthers D/ST 2.0 vs Tyler Allgeier 17.8 (loss; Allgeier went on to LY).
- Week 4: Hunter Henry 11.2 vs Brenton Strange 16.5 (loss).
- Week 4: Ollie Gordon II 18.0 vs Panthers D/ST -4.0 (win).

**Verdict:** Our moves have been the best in the league, so the problem is the roster's scoring, not too many moves or too few. Pickups and lineup calls are both near the top: 1st in add-vs-drop gain, 1st in pickup points as starters, and 2nd-fewest bench points left. We are 1-3 because we score poorly, 11th in points and 11th in all-play, not because of bad luck. The two misses were churn: dropping Allgeier for a one-week defense, and swapping in Henry for Strange. We are a little tweaky late in the week, but not reckless.

## Why QBZ is 11th in points: draft, injuries, or underperformance? (Weeks 1–4)
Method: every team's 16 draft picks, credited to the team that drafted them, whether or not they are still on the roster.
- **Points** are each drafted player's actual PPR points.
- **A missed game** is any week with no game played (ESPN games-played stat). No team had a bye in Weeks 1–4, so every missed game is an injury, suspension or inactive week.
- **Points lost to an absence** use the player's ESPN Week 1 projection for each missed game. Josh Jacobs and Zach Charbonnet had no projection, so their missed games are valued at what other players taken near the same draft pick averaged per week.
- **Projected if healthy** adds the ESPN weekly projections for games played to the estimated points lost to absences.
- **ADP** is ESPN's average draft position, used to measure reaches.

Week 5 is not final, so it is left out. Per-player data is in `draft_players.csv` and team totals are in `draft_injury_by_team.csv`.

| Team | PF | Drafted pts | Draft-return rank | Projected if healthy | Games missed (all / rd 1–8) | Injury rank | Est. pts lost to absences | Vs. projection when playing | Avg pick − ADP, rd 1–8 |
|---|---|---|---|---|---|---|---|---|---|
| TE | 520.4 | 812.9 | 1 | 807.3 | 3 / 3 | 9 | 47.8 | +53.5 | 1.0 |
| PP | 531.7 | 806.4 | 2 | 764.3 | 5 / 5 | 5 | 73.7 | +115.7 | -9.6 |
| MBB | 555.4 | 783.6 | 3 | 716.5 | 1 / 0 | 10 | 8.3 | +75.4 | -18.3 |
| TCO | 436.0 | 769.2 | 4 | 780.1 | 1 / 0 | 11 | 9.2 | -1.7 | -6.1 |
| CDS | 502.6 | 713.8 | 5 | 656.6 | 3 / 2 | 8 | 51.0 | +108.1 | -13.5 |
| LL | 466.5 | 710.1 | 6 | 755.0 | 5 / 3 | 7 | 62.3 | +17.5 | -6.0 |
| FR | 510.2 | 694.3 | 7 | 800.7 | 6 / 3 | 4 | 82.4 | -23.9 | -15.2 |
| GGT | 438.2 | 646.1 | 8 | 769.7 | 8 / 2 | 3 | 90.4 | -33.3 | -26.2 |
| BuB | 362.3 | 634.1 | 9 | 762.8 | 0 / 0 | 12 | 0.0 | -128.7 | -14.2 |
| DDT | 447.6 | 602.1 | 10 | 687.3 | 8 / 0 | 2 | 62.5 | -22.9 | -32.5 |
| LY | 418.0 | 599.1 | 11 | 621.4 | 5 / 2 | 6 | 61.0 | +38.6 | -65.3 |
| QBZ | 395.2 | 436.5 | 12 | 761.7 | 18 / 10 | 1 | 207.0 | -118.2 | -34.5 |

**Where QBZ's drafted points went.** Our 16 picks scored 436.5 points against a league average of 684.0, last in the league (gap -247.5). That gap splits exactly into three parts:
- **Draft quality: +21.4.** If healthy, ESPN projected our picks for 761.7, 7th of 12 and slightly above the 740.3 average. On paper the draft was fine, though we reached on picks (rounds 1–8 averaged 34.5 picks earlier than ESPN ADP, the 2nd-biggest reach after LY's 65.3).
- **Injuries: -144.0.** Our drafted players missed 18 games, the most in the league (average 5.2; next most 8). 10 of those were by players from rounds 1–8 (average 2.5). That cost an estimated 207 points against a league average of 63:
  - Josh Jacobs: 4 games
  - Jaxson Dart: 2
  - Dallas Goedert: 2
  - Jonathon Brooks: 2
  - Zach Charbonnet: 4 (drafted in round 15, outside the 10)
  - Achane, Etienne, Pittman and Darnold: 1 each
- **Underperformance when they did play: -124.9.** We're 11th, at -118.2 versus +6.7 on average. The biggest misses:
  - De'Von Achane: -30.2
  - Kyle Pitts: -25.8
  - Michael Pittman: -17.5
  - Rashid Shaheed: -13.1
  - Jonathon Brooks: -10.1

**Verdict.** We aren't 11th because of a bad draft. Our picks were projected about average. We're 11th because those players got hurt (18 games missed, the most in the league) and played below projection when healthy (11th). Of the 247.5-point shortfall, injuries account for about 58% and underperformance about 50%, with the draft slightly helping (+9%). Our moves made up some of the gap: pickups scored 66.6 points as starters, 1st in the league against an average of 26.2. That's why our points for (395.2) are only 70 below the league average (465.3), not 250.
