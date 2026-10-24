---
name: waiver.board
description: >-
  Use when posting a Quantum Blitz waiver board (rolling priority or FAAB) —
  research and recommend only; never file a claim until Ken types the claim
  command.
---
# waiver.board

Post a Quantum Blitz waiver board for rolling/traditional leagues. Research and recommend only — never file ESPN claims without Ken’s typed command.


## Lessons first (feedback loop, Ken Oct 20 2026)

Also read `RULES.md` and `STRATEGY.md` (repo root) (league rules canon, Ken Oct 23 2026) before any recommendation and run its checklist. Never propose moving or dropping a player whose game has started; check rosterLocked/lineupLocked first.
Before building or changing anything, pull main and read every fix rule in `playbook/LESSONS.md`. Apply each one that touches this run, and check the finished card or post against them before it goes out. Rules that matter most right now: no slot is ever marked "only X" (list the best free agent at K, D/ST, and QB with a bye backup, and ask Ken the same day if he clears 1.5 points); when a starter's team changes starting QB or play-caller, re-check that slot against the bench; add up team totals from live ESPN numbers before quoting one (never show the math to Ken); rewrite the decisions file from ESPN after every lineup change; no backup plans without an ESPN tag or real news.

## Paths
`/workspace/fantasy/quantum-blitz/` — read `league.json` acquisition, `roster.json`, `availability.json`, `WAIVERS.md`.

## Steps
1. Confirm mode from `league.json` (`is_faab` false → priority language, not $ bids).
2. Sync roster if stale; note current `waiverRank` if available from ESPN.
3. Pull Wire / availability for injuries creating demand; scan free agents / WW (read-only).
4. Rank 3–7 targets with a real drop for each. Tiers: MUST / STRONG / WATCH / PASS.
5. **Label every add and drop** with `Pos · NFL team · depth/role` (e.g. `RB · ARI · RB2 behind Love`). Never post a bare name Ken would have to Google.
6. If any MUST: lead with **MUST-ACT** / **CAN’T-MISS**, deadline, rank, labeled add/drop, and a copy-paste `claim X drop Y` line — still do not submit.
7. Post using the template in `WAIVERS.md`. Keep it short.
8. Wait for Ken: `claim …`, `pass`, or `hold waivers`. Only then run ESPN waiver write + verify (separate apply path).

## Hard stops
No claim/drop/trade/IR without Ken’s exact command. No FAAB bid language when league is rolling. Do not bury a MUST inside a quiet board. Do not omit position/team/depth on adds or drops.
