---
name: lineup
description: >-
  Use whenever choosing or re-checking the Quantum Blitz starting lineup:
  Tuesday set, designation checks, and game-day inactives.
---
# lineup
1. Pull get_matchup and get_roster from ffmcp. Fall back to the old ESPN client only if ffmcp errors.
2. Any starter who is ESPN OUT, IR, on bye, or officially inactive comes out now for the best unlocked replacement.
3. For close or flagged slots, read the news with get_news and a web search if needed: coach and player quotes on role, recent workload and snaps, players returning from injury, QB or play-caller changes, and game weather. Weigh it as heavily as the projection.
4. Start the player you expect to score more. No fixed point-gap rule. Keep close or newsy slots open until lock when a later player can still be swapped in, and put the latest-kicking flexible player at FLEX.
5. Make the changes with espn-write and confirm on ESPN.
6. Tell Ken in one plain sentence what changed. If nothing changed, say nothing.
