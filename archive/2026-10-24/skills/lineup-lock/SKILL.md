---
name: lineup.lock
description: >-
  Use Sunday morning to check inactives and emergency-swap Quantum Blitz 1:00 ET
  starters who are OUT.
---
# lineup.lock

Sunday morning inactives check for Quantum Blitz. Emergency swaps only when a recommended 1:00 ET starter is OUT and an unlocked replacement exists.


## Lessons first (feedback loop, Ken Oct 20 2026)

Also read `RULES.md` and `STRATEGY.md` (repo root) (league rules canon, Ken Oct 23 2026) before any recommendation and run its checklist. Never propose moving or dropping a player whose game has started; check rosterLocked/lineupLocked first.
Before building or changing anything, pull main and read every fix rule in `playbook/LESSONS.md`. Apply each one that touches this run, and check the finished card or post against them before it goes out. Rules that matter most right now: no slot is ever marked "only X" (list the best free agent at K, D/ST, and QB with a bye backup, and ask Ken the same day if he clears 1.5 points); when a starter's team changes starting QB or play-caller, re-check that slot against the bench; add up team totals from live ESPN numbers before quoting one (never show the math to Ken); rewrite the decisions file from ESPN after every lineup change; no backup plans without an ESPN tag or real news.

## Paths
`/fantasy/quantum-blitz/` — SPEC §§5, 8.4, 7.6, 11. Routine fires Sun 08:00 PT (= **10:00 AM CT**). Ken-facing times always CT.

## Steps
1. Run skill [roster.sync](sand-workflow:roster-sync) if roster is stale (>6h or missing).
2. **Wire handoff:** Read Sunday Wire refresh / latest `availability.json`; quote Wire’s one-liner (CT).
3. Check official inactives for early Sunday window (1:00 ET / **12:00 PM CT** games). Official inactive/OUT overrides projections and ESPN Q tags.
4. If a recommended 1:00 ET starter is OUT and an unlocked replacement exists, post an emergency LOCK card (§11) with the swap + Wire line — times in CT.
5. Do not touch already kicked games.
6. On apply: [espn.api-apply](sand-workflow:espn-api-apply); alert Ken on verify fail.

## Validation
No edits to DONE/LOCKED; legal replacements only; Ken-facing times CT.

## Approval / hard stops
`yes, set it` or Sunday dead-man (OUT gate) only. Do not invent OUT designations.
