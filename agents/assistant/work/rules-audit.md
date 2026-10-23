# Audit of RULES.md and STRATEGY.md (repo root, commit 4473fab)

Written by Assistant, Fri Oct 23 2026, about 9:30 AM CT. Each line is checked against our league's ESPN settings (mSettings, pulled read-only today) and ESPN Fan Support pages. Marks: CORRECT, WRONG, PARTLY WRONG, MISSING, or UNSOURCED. Every WRONG item comes with a fix.

## Sources
- S1, league settings: ESPN mSettings for league 1776545061, season 2026, pulled Oct 23 2026.
- S2, live standings: ESPN mTeam/mStandings, pulled Oct 23 2026 (includes ESPN's own current playoffSeed for each team).
- S3, live roster: ESPN mRoster for team 13, scoring period 7, plus proTeamSchedules for bye weeks.
- Seeding: https://support.espn.com/hc/en-us/articles/47190901074708-H2H-Points-League-Playoff-Seeding-Tiebreakers
- Seeding tiebreakers: https://support.espn.com/hc/en-us/articles/360036952471-Playoff-Seeding-How-Regular-Season-Standings-Tiebreakers-Work
- Playoff ties: https://support.espn.com/hc/en-us/articles/4669390376852-Playoff-Scoring-Tiebreakers
- Lock times: https://support.espn.com/hc/en-us/articles/360055424451-Lineup-and-Roster-Lock-Times
- Locked players: https://support.espn.com/hc/en-us/articles/4669616628500-Roster-Adjustments-After-Players-Have-Locked
- Waivers: https://support.espn.com/hc/en-us/articles/360000036711-Claim-a-Player-Off-Waivers
- Waiver period: https://support.espn.com/hc/en-us/articles/360012531592-Waiver-Period
- Waiver order: https://support.espn.com/hc/en-us/articles/360000066171-Waiver-Order-Overview-and-Salary-Cap-Tiebreakers
- Failed claims: https://support.espn.com/hc/en-us/articles/360029528571-Reasons-Why-a-Waiver-Pickup-May-Not-Process
- IR: https://support.espn.com/hc/en-us/articles/115003849911-Players-on-Injured-Reserve-IR
- IR and waivers: https://support.espn.com/hc/en-us/articles/360060861691-How-does-the-Injured-Reserve-Injury-List-impact-Waivers
- Trade review: https://support.espn.com/hc/en-us/articles/360000071412-Trade-Review
- Vetoes: https://support.espn.com/hc/en-us/articles/360000097512-Veto-or-Protest-a-Trade
- Trade deadline: https://support.espn.com/hc/en-us/articles/360000959192-How-does-the-Trade-Deadline-work
- Older ESPN rules page (freezes and weekly rollover): https://www.espn.in/ffl/ffl/story?page=fflruleswaiverwalk

## The big error: playoff seeding

ESPN seeds the playoffs by record (winning percentage). Total points scored is only the first tiebreaker between teams with the same record.

- S1: scheduleSettings.playoffSeedingRule = TOTAL_POINTS_SCORED. This is the league's seeding tiebreaker setting. The espn-api library calls it playoff_seed_tie_rule.
- ESPN help (H2H Points seeding page above): "Winning Percentage — Among non-division-winner seeds, the team with the best winning percentage earns the higher seed." Tiebreakers apply only "when two or more teams finish the regular season with identical winning percentages."
- S2 proves it in our own league today. ESPN's current seeds put Charlie Don't Surf (6-0, 727.5 points) first, ahead of Fantasy Rookie No More (5-1, 787.6). Lazy Yorkie (2-4, 574.9) is ninth, ahead of us (1-5, 612.8). Points only break ties. The Chosen Ones (3-3, 719.0) are sixth ahead of La Lightning (3-3, 711.6), and The gg Team (1-5, 638.9) is tenth ahead of us.
- Correct picture today: the sixth seed is 3-3. We are 1-5, two games back with eight regular-season games left (Weeks 7 to 14). If we finish tied on record with the sixth team, total points decide it, and we trail The Chosen Ones by about 106. In practice we need to pass them on wins.
- Last-place race: David's Daring Team is 0-6 with 678.0 points. If we lose this week, we are both 1-6, and he wins a points tiebreak by about 65.

## RULES.md, line by line

| Line | Mark | Finding and fix |
|---|---|---|
| 3 | CORRECT | Header. |
| 6 | CORRECT | S1: scoringType H2H_POINTS. Receptions are worth 1 (stat 53). Size 12, one division ("League Standings", 12 teams). |
| 7 | CORRECT, MISSING | The values match S1. Add the kicker values: PAT 1, field goal 0-39 yards 3, 40-49 yards 4, 50-59 yards 5, 60+ yards 6, missed field goal -1. S1 has no penalty for a missed PAT. Add the D/ST values from S1. Points allowed: 0 = 5, 1-6 = 4, 7-13 = 3, 14-17 = 1, 28-34 = -1, 35-45 = -3, 46+ = -5. Yards allowed: under 100 = 5, 100-199 = 3, 200-299 = 2, 350-399 = -1, 400-449 = -3, 450-499 = -5, 500-549 = -6, 550+ = -7. Sack 1, interception 2, fumble recovery 2, blocked kick 2, safety 2, any defensive or return TD 6. (The stat IDs are mapped to ESPN's standard stat list, which is how ESPN numbers them.) |
| 8 | PARTLY WRONG | The regular-season part is correct: S1 matchupTieRule = NONE, so ties stand. The playoff part is wrong. ESPN help says that if a playoff matchup ends tied, "the higher-seeded team advances" by default, and the league manager has final say (Playoff ties URL). Fix: "Regular-season ties stand. In the playoffs, the higher seed advances on a tie." |
| 9 | CORRECT | S1: matchupPeriodCount 14, matchupPeriodLength 1. |
| 10 | WRONG | Fix: "Six teams make the playoffs, seeded by record. Total points scored is the first tiebreaker between teams with the same record. Seeds are re-set each round (playoffReseed = true)." Points still matter as the tiebreaker and for winning each week, but they do not set seeds. See the seeding section above. |
| 11 | CORRECT | S1: matchupPeriods 15, 16 and 17, playoff length 1, 6 teams (so the top two get a bye), consolationLadderDisabled = false. |
| 14 | CORRECT | S1 lineupSlotCounts: QB 1, RB 2, WR 2, TE 1, FLEX 1, D/ST 1, K 1. S1 also has allowOutOfPositionScoring = false. |
| 15 | CORRECT, UNCONFIRMED | S1 shows 7 bench slots and 1 IR slot. S1 also shows isBenchUnlimited = true, and I could not confirm what ESPN means by it. Our roster today has exactly 7 on the bench. Treat 7 as the limit. |
| 16 | CORRECT, MISSING | S1 positionLimits: QB 4, RB 8, WR 8, TE 3, K 3, D/ST 3. Add a warning: we are at the TE cap now (Pitts, Goedert and Henry). Any TE add needs a TE drop, and Henry is locked until the week rolls over. ESPN rejects a claim that would break a position cap (Failed claims URL). |
| 19 | CORRECT | S1: lineupLocktimeType = INDIVIDUAL_GAME and rosterLocktimeType = INDIVIDUAL_GAME. Confirmed by the Lock times URL. Add one caution: that page also says "Any moves involving trades, add/drops or IR moves will be locked at the first scheduled game of the day." Always trust the player's rosterLocked flag on ESPN over the clock. |
| 20 | CORRECT | Locked players URL: "Once a player's slot is locked, only your League Manager (LM) can make roster changes." S3 today shows Henry and Henderson with lineupLocked and rosterLocked both true. |
| 21 | CORRECT | Good practice that matches S3's flags. |
| 22 | CORRECT | Follows from per-game locks. |
| 25 | CORRECT | S1: acquisitionType WAIVERS_TRADITIONAL, isUsingAcquisitionBudget = false. Waivers URL: free-agent adds "do not affect waiver priority." |
| 26 | PARTLY WRONG | The days and 24 hours are correct (S1: waiverHours 24, waiverProcessDays Mon, Wed, Thu, Fri, Sat, Sun, with no Tuesday run). The time range is too narrow. S1's run log shows runs from about 2:00 to 2:52 AM CT; the latest was Fri Oct 23 at 2:00 AM CT. ESPN help says runs start around 3 to 5 AM ET. Fix: "about 2:00 to 4:00 AM CT." S1 also shows waiverProcessHour = 11, which I could not match to a clock time. The run log is the evidence to use. |
| 27 | CORRECT | Waiver period URL: a player added and dropped the same day stays a free agent. The Waivers URL words it as rostered "less than 24 hours." |
| 28 | CORRECT | S1: acquisitionLimit -1, matchupAcquisitionLimit -1, moveLimit -1, trade max -1 (all unlimited). |
| 29 | CORRECT | S1: isUsingUndroppableList = true. The Waivers URL mentions the "Can't Drop" label. |
| 32 | PARTLY UNSOURCED | One IR slot (S1) and OUT or IR eligibility are correct, and so is the line on suspended players (IR URL). I found no ESPN page about Commissioner's Exempt players. Mark that part "team rule, not ESPN." Note that the IR-and-waivers URL says only IR-tagged players qualify, while the main IR URL says OUT or IR. Follow the main IR page and ESPN's slot check. |
| 33 | CORRECT, MISSING | Matches the IR URL. Add three things. A healthy player in IR also blocks waiver claims and trades (Failed claims URL and IR-and-waivers URL). A claim made while IR was legal still processes if the player gets healthy before the run. If we activate an IR player after making a claim, the claim can fail for lack of a roster spot. |
| 36 | CORRECT, MISSING | S1: deadlineDate is Wed Dec 2 2026 at 11:00 AM CT, revisionHours 24, vetoVotesRequired 4. Add three things. The trade must be accepted, and all voting done, before the deadline (Trade deadline URL). Traded players arrive on the bench (Vetoes URL). Adds and drops continue after the deadline. |
| 39 | CORRECT | |
| 40 | CORRECT | Team rule from Ken (Oct 15). It is not an ESPN rule. |
| 41 | UNSOURCED | These are NFL practices, not ESPN rules. I did not verify them today. |
| 42 | CORRECT | |
| 43 | CORRECT | |
| 46 | PARTLY WRONG (missing players) | The listed weeks match S3. Missing players: Bernard (PIT, Week 9, our FLEX starter), Goedert and Harvey (Week 10), Henderson and Henry (NE, Week 11), and Gay (LV, Week 13, our only K). Murray and Gordon already had byes in Week 6. Etienne is in IR, so his Week 8 bye costs us nothing. |
| 49-53 | CORRECT, MISSING | Add the checks listed at the bottom of this file. |

## RULES.md is missing these rules

1. Seeding is by record, with total points as the tiebreaker (see the seeding section).
2. Waiver order resets every week to the inverse of the standings (S1: waiverOrderReset = true). The worst record picks first. The reset happens when the new week begins (Waiver order URL). A successful claim still drops that team to the bottom until the next reset. We are 1-5, so our priority is high, and spending it costs little because it resets.
3. Weekly rollover: the week ends after the Monday night game. ESPN's older rules page puts the unlock at about Tuesday 3 AM ET (2 AM CT). The waiver-order page says the new week begins Monday at 3 AM ET. The two pages disagree, so check the player's lock flag on ESPN.
4. Free agents freeze too. A free agent whose game has started cannot be added until the week rolls over. After the rollover, all unrostered players sit on waivers until the first run (Older ESPN rules page). Always add a free agent before his kickoff.
5. When a drop clears waivers. A drop goes to waivers and clears at the first run at least 24 hours later (Waiver period URL). Example: Montgomery was dropped about 9:19 AM CT Fri Oct 23. The Saturday run is less than 24 hours later, so he should clear around the early-morning Sunday Oct 25 run, about 2 to 4 AM CT. Other teams can claim him until then.
6. Lineups lock per game (INDIVIDUAL_GAME, S1), and roster moves lock per game too. Both are set in S1.
7. A transaction log entry that says "dropped to Waivers" may still mean the player is a free agent (Waiver period URL). Check the Players page.
8. There are no keepers (S1: keeperCount 0), no FAAB, and no transaction fees.
9. Playoff ties go to the higher seed (Playoff ties URL).
10. Standings tiebreakers between teams with the same record: total points is first (S1). In ESPN's general order, head-to-head, points for, division record, points against and a coin flip follow (Seeding tiebreakers URL). I could not confirm whether our league uses anything after total points.
11. S1 shows isAutoReactivate = true. I could not confirm what it does. It may move IR players back automatically, so check the IR slot after any status change.

## STRATEGY.md, line by line

| Line | Mark | Finding and fix |
|---|---|---|
| 6 | WRONG (seeding error) | Fix: "Playoff seeding is by record. Total points scored breaks ties between teams with the same record. Wins are the goal; points are the tiebreaker and decide each week's game." |
| 7 | WRONG (seeding error) | The record, the points total and the gap to The Chosen Ones are accurate facts, but they don't measure the playoff race, and "11th of 12 in points" is also wrong. Lazy Yorkie has fewer points (574.9), so we are 10th in points. "Outscore the sixth-place team by about 13 points a week" is the wrong target. Fix: "1-5 and 11th by ESPN's seeding. The sixth seed (The Chosen Ones) is 3-3. We are two games back with eight games left. We lose a points tiebreak with them by about 106, so we need more wins than them. Last place: David is 0-6 with 678.0, and he wins a points tie with us." |
| 8 | DEPENDS ON SEEDING ERROR | Taking the higher-ceiling player when two are close is still a fine way to win a single game, but the reason given is the false points-race gap. Fix: base it on this week's matchup (for example, when we're projected to lose, prefer the higher ceiling). |
| 11 | PARTLY WRONG | The week ends after Monday night. Players unlock at about 2 AM CT Tuesday per ESPN's older rules page, not on Monday night (see missing rule 3). |
| 12 | CORRECT | This is a work routine, not a rule. |
| 13 | PARTLY WRONG | Waivers run every night except Monday night into Tuesday (S1 days: Mon, Wed, Thu, Fri, Sat, Sun), not only on Wednesday. The Wednesday run is the big one, when most players from the weekly freeze clear (Waiver period URL: "Most players will clear Wednesday mornings"). Fix the time to about 2 to 4 AM CT. |
| 14 | CORRECT | Per-game locks. |
| 15-16 | UNSOURCED | NFL report timing, not checked today. |
| 17 | PARTLY WRONG | Inactives come out 90 minutes before kickoff: about 10:30 AM for noon games, 1:35 PM for 3:05 games, and 1:55 PM for 3:25 games, not 1:35 for both. Add Sunday night (about 5:50 PM for a 7:20 kickoff) and Monday night games. |
| 20-24 | CORRECT | |
| 27 | CORRECT | Waivers URL. |
| 28 | PARTLY DEPENDS | Waiver priority resets weekly to the inverse of the standings (S1 waiverOrderReset). At 1-5 we keep getting it back, so a claim costs less than this line implies. Add that. |
| 29 | CORRECT | Add a check of position caps (we're at TE 3). |
| 30-31 | CORRECT | |
| 34-35 | CORRECT | Team guidance. |
| 38-39 | CORRECT | S3: Murray (MIN) had his bye in Week 6, and McCarthy is on the bench. Note that McCarthy (NYG) is on bye in Week 8, so in Week 8 we have no backup QB. |
| 42-43 | CORRECT | Matches the IR URL. Add that a healthy player in IR blocks claims, adds and trades. |
| 46 | CORRECT | S1. |
| 47-48 | CORRECT | |
| 51 | CORRECT | |
| 52 | PARTLY WRONG | Missing: Week 9 Bernard (our FLEX), Week 10 Goedert and Harvey, Week 11 Henderson and Henry, Week 13 Gay (our only K). Etienne's Week 8 bye doesn't matter because he's in IR. |
| 55-58 | CORRECT | |

## Checks before any move (add to both files)
1. Is the player locked right now? Read rosterLocked and lineupLocked on ESPN, not the schedule.
2. Is the player I'm adding a free agent (green, instant, no priority) or on waivers (yellow, overnight claim)? Has his game already started? If so, he is frozen until the week rolls over.
3. Where does my drop go? Usually to waivers for at least 24 hours, so other teams can claim him.
4. Is the IR slot legal (player tagged OUT or IR)? If not, every add, claim and trade is blocked.
5. Does the add break a position cap? We are at TE 3 now.
6. Does every starter have a game this week? Check byes. Week 8: Marks and McCarthy, so start Murray and replace Marks. Week 9: Bernard and the Steelers D/ST.
7. Does a later-week starter have a backup whose game locks first?
8. Is it before the trade deadline (Wed Dec 2, 11:00 AM CT), and will voting finish before it?
