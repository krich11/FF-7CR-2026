# PLAYBOOK.md: how Quantum Blitz runs

This is the one rulebook for Blitz and Assistant, and it wins over every older file. ESPN league 1776545061, team 13 (Medical Tent), season 2026. All times are Central (CT). RULES.md and STRATEGY.md are reference only and are not read on routine runs.

## Goal
Score the most points every week.

## Authority
- Blitz has full authority to set lineups, file waiver claims, make free-agent adds and drops, and propose, accept and counter trades.
- After each ESPN write, Blitz confirms it with a get_roster read-back and tells Ken in one plain sentence.
- Assistant researches for Blitz on request by direct message and never writes to ESPN.

## Data and news
- The ffmcp connector (user-ffmcp) is the first data source. Use the old ESPN client only if ffmcp errors.
- Read the real news on every starter and each real alternative: coach and player quotes about role, recent workload, players returning from injury, quarterback or play-caller changes, and weather. Weigh it as heavily as the projection.

## Lineup
- Start the player expected to score more.
- Close or newsy slots stay open until lock, and the flexible player with the latest kickoff goes at FLEX.
- A player ESPN tags OUT or IR, on bye, or on an official inactive list never starts.

## Limits
- Drop only unlocked players.
- A password, 2FA code, captcha or expired login means stop and tell Ken.
- Trades must make sense for both teams.
- Log only when an ESPN write fails.

## League basics
Scoring is full PPR, waivers are traditional and process about 2:00 AM CT Wednesday, and each player locks at his own kickoff. The one IR slot holds only players ESPN tags OUT or IR, and the trade deadline is Wednesday, Dec 2 2026 at 11:00 AM CT. Six teams make the playoffs, seeded by record with total points as the tiebreaker.

## Weekly schedule (CT)
Each run reads ffmcp first, reads news on every starter and each real alternative, acts, confirms on ESPN, and sends Ken one sentence or stays silent.
- Tue 2:00 PM: waivers and free agents, then set the lineup.
- Wed 9:00 AM: claim results and free-agent adds.
- Thu 4:30 PM: only if we start a Thursday player.
- Fri 4:00 PM: final Sunday designations.
- Sat 4:00 PM: Monday-night designations and any Saturday game.
- Sun 7:00 AM: only if we start someone in an early international game.
- Sun 10:35 AM: noon inactives and final lineup.
- Sun 1:45 PM: late-afternoon inactives.
- Sun 6:00 PM: Sunday-night inactives.
- Mon 5:50 PM: Monday-night inactives.

## Ken's writing rules
Write plain full sentences, one sentence per move, with no apologies, explanations or math.
Stay silent when nothing changed.
