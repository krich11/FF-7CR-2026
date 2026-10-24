---
name: roster.sync
description: >-
  Use when syncing the live ESPN Quantum Blitz roster into roster.json before
  any lineup decision, or after Ken says a claim was made.
---
# roster.sync

Sync the live ESPN roster for Quantum Blitz into local state. First step of every other lineup skill, or when Ken says a claim was made.

## Paths
Work under `/fantasy/quantum-blitz/` (or `/workspace/fantasy/quantum-blitz/`). Read `league.json` for leagueId, teamId, seasonId, timezone (`America/Los_Angeles`).

## Steps
1. **Prefer API:** run [espn.api-apply](sand-workflow:espn-api-apply) sync (`python3 /workspace/fantasy/quantum-blitz/espn_api/cli.py sync`). That writes `roster.json` from lm-api-reads using box-local cookies. Never print cookie values.
2. If API auth fails (401/403) or cookies missing: open ESPN Fantasy → Quantum Blitz roster in the box browser. Reuse saved session; if login required, secure box handoff — never ask for or store a password in chat. Dump rostered players and write `roster.json` with `source: espn_team_page`.
3. Diff against the previous `roster.json`. If a player appeared or disappeared, ask Ken before treating the change as correct.
4. Pull this NFL week’s schedule into `schedule.json` with kickoff timestamps in `America/Los_Angeles`.
5. Set each player’s `lock_state` in `availability.json` (`UNLOCKED` | `LOCKED` | `DONE`) from now vs kickoff (`lock_policy`: player kickoff).
6. If any espn_tag / API injuryStatus suggests injury/out, run or hand off to [status.resolve](sand-workflow:status-resolve) / [availability.refresh](sand-workflow:availability-refresh) before any start/sit decision — **do not treat ESPN tags as final legal status**.

## Validation
- Every player on the ESPN roster is in `roster.json`.
- No invented players.
- Schedule kickoffs are in PT.

## Output
Confirm sync in the Bot thread: player count, any roster diff, current NFL week, next kickoff, source (`espn_api` vs page), any espn_tag vs official conflicts already known.

## Approval
None for read-only sync. ESPN writes are out of scope for this skill.

## Hard stops
Do not drop, add, trade, IR-move, or claim waivers. Do not apply lineups here. Do not start someone solely because ESPN shows DTD/Q with a projection.
