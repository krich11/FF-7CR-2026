# Close-call deep dive: is there a signal that beats "start the higher projection"?

Ken's question (Oct 11, 2026): find a pre-kickoff signal that turns close start/sit calls (projection gap under 3 PPR points) from coin flips into wins. This is the deeper follow-up to `close-call-heuristic.md` (commit 5036274).

## Bottom line

**No. Nothing we can know before kickoff beats the higher projection on close calls by a margin we can measure.** Across ~437,000 close pairs from 2021 to 2026, the best models land at 56.7 to 57.4% on games they never saw, against 56.6 to 56.9% for simply starting the higher projection. Every lift's 95% range includes zero.

The ceiling for close calls is about **57%**, and it depends almost entirely on the size of the gap:

| Projection gap | Higher projection wins (2025 + 2026 test) | Pairs |
|---|---|---|
| 0 to 1 pt | 52.4% | 36,689 |
| 1 to 2 pts | 57.3% | 33,835 |
| 2 to 3 pts | 60.9% | 30,065 |

When a choice is wrong, the average swing between the two players is about 7.5 points. That's PPR scoring noise, and no pregame data in this study predicted it.

## Data

- **Projections:** Sleeper public projections API, 2021 to 2026, weekly PPR, QB/RB/WR/TE. (ESPN doesn't publish past-season weekly projections openly, so the main study uses Sleeper. The 56% baseline matches the earlier ESPN-based study, 56.6% vs ~56%.)
- **Actual scores:** Sleeper stats API (PPR points, snaps, targets, carries).
- **Betting lines:** nflverse `games.csv` (spread and total, turned into each team's expected points), plus home, dome, rest days and wind.
- **Injuries:** nflverse injury reports (game status and practice status), 2021 to 2026.
- **Pairs:** in each week, every two players on different teams who are the same position (or both flex-eligible), both projected 6+ points, not ruled Out before the game, with projections under 3 points apart. Exact ties in actual points were dropped. 437,340 pairs.

## What we tested (21 signals, everything known before kickoff)

Projection gap, team expected points, the player's share of his team's expected points, home, dome, rest difference, point spread (game script), wind, opponent's points allowed to the position in earlier weeks, Questionable tag, limited/missed practice, carries and targets left behind by injured teammates (whole team and same position group), touches over the last 3 games, touch trend, snap share (last game and last 3), how far the player has beaten or missed his projections this season, the player's week-to-week volatility, the change in his projection from last week, and targets over the last 3 games.

**Honest validation:** trained on 2021 to 2023, checked against 2024, and tested once on 2025 plus 2026 Weeks 1 to 4. Confidence intervals resample whole weeks, because pairs within a week are linked.

## Results on games the models never saw (2025 + 2026 Wks 1 to 4, n = 100,589 pairs)

| Method | Win rate | 95% range | Lift over higher projection |
|---|---|---|---|
| Start the higher projection | 56.6% | | |
| Logistic model, all 21 signals | 56.8% | 55.9 to 57.6% | +0.2 pts (−0.4 to +0.7) |
| Gradient-boosted trees | 56.7% | 56.0 to 57.4% | +0.1 pts (−0.4 to +0.5) |
| 2026 Wks 1 to 4 only, logistic (n = 20,421) | 57.4% vs 56.9% | 56.4 to 58.6% | +0.5 pts (−0.2 to +1.3) |

The models overrule the projection in only 9 to 12% of pairs, and those overrides come out about even.

### Signals that carry some weight (but not enough to flip a call)

1. **Questionable tag on the higher-projected player.** He wins only 51.5% (training years) and 55.4% (test years), versus about 60% when the other player is the one tagged. The call drops toward a coin flip but doesn't reverse, so starting the Questionable player's backup would have lost more often. Use it as a confidence downgrade, not a flip.
2. **Recent volume (touches over the last 3 games, snap share last game).** The higher projection wins a bit more often when it also has the volume edge (57 to 58%) than when it doesn't (55 to 56%). That's a modest confidence nudge that never comes close to flipping a call. This is where Blitz's snap-count instinct comes from, and the data says it's a nudge, not a tiebreaker.
3. **Projection gap itself.** Most of the information is already in ESPN's or Sleeper's number.

### Signals that did NOT hold up

- **Team expected points from the betting line, home field, and dome.** As tiebreakers in near-ties (under 1.5 pts), they won 52.3% and 51.1%. That's noise, so the home/dome tiebreak in the earlier writeup is effectively worthless (harmless, but not an edge).
- **Teammate injuries (carries and targets left behind).** Training years said it helped; test years reversed it. ESPN and Sleeper already raise the backup's projection, so the edge is gone by the time you'd use it. (Blitz's "starter out for the year" exception is a narrower case that this doesn't directly test; treat it as unproven.)
- **Beating his projections lately, volatility, opponent points allowed, rest, spread, wind:** no stable effect.

## Multiple testing and leakage

- We tested 21 signals and 2 model types. With that many tries, one or two "hits" of about 1 point would show up by chance. Nothing survived the held-out test, so there's nothing to correct for.
- Every feature uses only earlier weeks or pregame reports. One caveat: Sleeper's stored historical projections may include last-minute updates (timestamps sometimes fall after kickoff). If anything, that makes the baseline look a little better than a Tuesday projection would.
- Weakness: injury reports were matched to about 90% of relevant players by name and team, not 100%.

## What to do with this for Week 6 and the rest of the season

- **Rule:** within 3 points, start the higher projection. Under 1 point, it's truly 52/48, so stop agonizing over those.
- **Confidence flag only:** if the higher-projected player is Questionable, call it a coin flip and grab the late-game swap if one exists. Don't flip it on the tag alone.
- **Where real points live:** the edge isn't in close calls. Close calls are worth about 0.1 expected points each. It's in avoiding zeros (inactives, Thursday/London timing, byes), waiver pickups, and lopsided calls where the projection is stale (confirmed season-ending injuries, role changes on the depth chart).
- **Weekly data needed if we ever re-run:** projections (ESPN or Sleeper), Friday injury report, betting lines. All are free. Re-check after Week 8 is optional; the result is unlikely to change with 4 more weeks.

Scripts: `/workspace/ccdeep/` on the box (build.py, vac.py, qfix.py, pairs.py, model.py).
