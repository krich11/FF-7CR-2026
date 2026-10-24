---
name: availability.refresh
description: >-
  Use when refreshing Quantum Blitz player availability into
  data/availability.json in the FF-7CR-2026 repo. ESPN's tag sets status; news
  is notes. Never picks lineups or writes ESPN. Tell Blitz every run; ping Ken
  only on a status change.
---
# availability.refresh

Refresh availability for Quantum Blitz rostered players only. Do **not** optimize lineups or touch ESPN.

## Paths
Repo `krich11/FF-7CR-2026`, branch `main`. Pull before reading. Read `data/roster.json`, `RULES.md`, and `PLAYBOOK.md`. Write `data/availability.json`. The read-only ESPN client lives at `/workspace/fantasy/quantum-blitz/espn_api/` (not a repo). Always apply [status.resolve](sand-workflow:status-resolve).

## Steps
1. Read the live roster from ESPN (mRoster, teamId 13). If ESPN fails, use `data/roster.json` on main and note it. Never invent players.
2. Read each rostered player's ESPN status and lock flags. Then gather news: official injury report and inactives, then same-day beat, then national desk. Never invent injuries.
3. Run status.resolve: **ESPN sets `state`**; reports go in `news`/`note`. A report that disagrees with ESPN is logged as `STATUS_CONFLICT` and flagged to Blitz the same day. An official can't-play list (inactives, IR, PUP, suspension, Exempt) sets `official_block`, which benches only.
4. For each starter's NFL team, check for a QB change or play-caller change since the last file and note it.
5. Map states with `play_prob`, `snap_mult`, `news`, `source`, `as_of` (CT), `kickoff`, `lock_state`. Defaults: LIMITED 0.70; QUESTIONABLE and expected to play 0.75; other QUESTIONABLE 0.45; OUT/IR/BYE 0.
6. Write the file, commit, push, and re-read main to confirm.
7. Report: always a short DM to Blitz with the commit and any changes. Message Ken only when a rostered player's ESPN status or official_block changed, or when Blitz says relay Ken. Post in the War Room only when Ken has a decision to make.

## Hard stops
- No start/sit recommendations, ESPN edits, waivers, drops, trades or IR moves.
- No fabricated news. A news report never overwrites ESPN's status.
- If sources fail twice, leave prior rows, mark the refresh failed, and tell Blitz AV FAIL. Never empty the file.
