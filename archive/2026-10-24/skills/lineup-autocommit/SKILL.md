---
name: lineup.autocommit
description: >-
  Use at dead-man deadlines to auto-apply the current legal Quantum Blitz card
  to ESPN unlocked slots only when every §7.6 gate passes. Always re-run
  roster.sync and injury/projection search first; if start/sit changes, post and
  apply the new card; if refresh fails, continue on the current card.
---
# lineup.autocommit

Dead-man apply of the current legal Quantum Blitz card when Ken is silent. Lineup slot moves only. Never waivers, drops, trades, IR, FAAB, or settings.


## Lessons first (feedback loop, Ken Oct 20 2026)

Also read `RULES.md` and `STRATEGY.md` (repo root) (league rules canon, Ken Oct 23 2026) before any recommendation and run its checklist. Never propose moving or dropping a player whose game has started; check rosterLocked/lineupLocked first.
Before building or changing anything, pull main and read every fix rule in `playbook/LESSONS.md`. Apply each one that touches this run, and check the finished card or post against them before it goes out. Rules that matter most right now: no slot is ever marked "only X" (list the best free agent at K, D/ST, and QB with a bye backup, and ask Ken the same day if he clears 1.5 points); when a starter's team changes starting QB or play-caller, re-check that slot against the bench; add up team totals from live ESPN numbers before quoting one (never show the math to Ken); rewrite the decisions file from ESPN after every lineup change; no backup plans without an ESPN tag or real news.

## Paths
`/fantasy/quantum-blitz/` — SPEC §7.6. Routines fire on America/Los_Angeles wall clock; **notify Ken in America/Chicago (CT)**. Read `preferences.json` for overrides.

## When (absolute LA → print CT)
- Set: Tue 20:00 PT → **Tue 10:00 PM CT** (or 3 hours before first kickoff if sooner)
- Set backup: Wed 14:00 PT → **Wed 4:00 PM CT**
- Friday tweak: Fri 20:00 PT → **Fri 10:00 PM CT**
- Sunday: Sun 08:40 PT → **Sun 10:40 AM CT** only if a 1:00 ET starter is OUT
- Or sooner under `away until {datetime}` (parse Ken’s CT unless he labels otherwise)

## Steps
1. **Pre-refresh:** Re-run [roster.sync](sand-workflow:roster-sync) plus injury/projection search. Prefer latest Wire `availability.json`. [projections.validate](sand-workflow:projections-validate). Re-optimize unlocked slots.
   - If start/sit **changes**, post a new card (CT times) and apply that.
   - If refresh **cannot** complete, continue on the **current** legal card; note the failed refresh.
2. Load apply-target card + decisions; abort if missing/STALE (unless just replaced).
3. Check thread for `hold` / `stop` after the apply-target card → cancel.
4. Run all §7.6 gates; if any fail, post `AUTO-COMMIT BLOCKED` and leave ESPN alone.
5. Apply via [espn.api-apply](sand-workflow:espn-api-apply). On `alert: true`, post `ESPN API VERIFY FAILED`.
6. On success: notify `AUTO-APPLIED {slots}` with CT timestamp.

## Commands
`yes, set it` | `hold`/`stop` | `away until {datetime}` | `home`

## Hard stops
Never waivers/drops/trades. Verify-fail always alerts Ken.
