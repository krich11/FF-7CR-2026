---
name: lineup
description: >-
  Use whenever choosing or re-checking the Quantum Blitz starting lineup:
  Tuesday set, designation checks, and game-day inactives.
---
# lineup
1. Pull get_matchup and get_roster from ffmcp. Fall back to the old ESPN client only if ffmcp errors.
2. Any starter who is ESPN OUT, IR, on bye, or officially inactive comes out now for the best unlocked replacement.
3. Read the news on every starter and each real alternative with get_news and a web search if needed: coach and player quotes on role, recent workload and snaps, players returning from injury, QB or play-caller changes, and game weather. Weigh it as heavily as the projection.
4. On close calls, also get:
   - a betting-market second opinion from Prediction Markets Picks (user-predictionmarketspicks): start_sit for the 2 to 4 players in question, player_outlook for one player, sleepers_and_busts for a quick scan;
   - recent weekly carries, targets, receptions and PPR points from Big Balls Data (user-bigballsdata): find_players, then get_player_stats with season 2026. The limit is 500 calls a day, so use it only on the players in the close call.
   Weigh recent workload as heavily as the projection, especially for RB and FLEX.
5. Start the player you expect to score more. No fixed point-gap rule. Keep close or newsy slots open until lock when a later player can still be swapped in, and put the latest-kicking flexible player at FLEX.
6. Make the changes with espn-write and confirm on ESPN.
7. Tell Ken in one plain sentence what changed. If nothing changed, say nothing.
