---
name: status.resolve
description: >-
  Use when an injury/news report disagrees with ESPN's status tag for a Quantum
  Blitz player. ESPN is the single source of truth for status (Ken, Oct 15
  2026); reports are notes only and get flagged to Blitz the same day.
---
# status.resolve

Rule (Ken, Oct 15 2026): **ESPN is the single source of truth for player status.** News, beat writers, national insiders and projection sites are notes only and never change a player's status.

**Bench-only exception (Ken approved Oct 15 2026, 8:48 PM CT):** if an official NFL or team list says a player can't play (game-day inactives, IR, PUP, suspension, Commissioner's Exempt), set `official_block` with source and time; that player does not start, even if ESPN still shows him playable. An official list can only bench a player. It never starts a player, clears an ESPN OUT, or triggers an add. Example: Jacobs is on the Exempt list while ESPN shows DAY_TO_DAY.

## Paths
`/workspace/fantasy/quantum-blitz/` — updates fields on `availability.json` (and notes on `roster.json` / `projections.json`). Append conflicts to `audit.log`.

## Rules
- Set `state` from ESPN's injury/roster status (ACTIVE, QUESTIONABLE, DOUBTFUL, OUT, INJURY_RESERVE, DAY_TO_DAY, BYE, etc.).
- Put any disagreeing report in `news` / `note` with its source and time, e.g. `"state": "QUESTIONABLE", "note": "Schefter: high ankle, out several weeks (Oct 14)"`.
- When a report disagrees with ESPN, log `STATUS_CONFLICT player=... espn=... report=... source=...` and flag it to Blitz the same day.
- **Never recommend or apply** a player whose ESPN state is OUT / IR / BYE / suspended, or who has an `official_block`, into a starting slot.
- Projection numbers never change status.

## When
Run during [availability.refresh](sand-workflow:availability-refresh), after [roster.sync](sand-workflow:roster-sync), and before optimizing inside lineup.set / tweak / lock / autocommit pre-refresh.

## Hard stops
Do not overwrite an ESPN status with a news or injury report. Do not invent statuses.
