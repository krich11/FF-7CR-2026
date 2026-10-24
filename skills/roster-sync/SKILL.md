---
name: roster.sync
description: >-
  Use when syncing the live ESPN Quantum Blitz roster into data/roster.json in the
  repo before any lineup decision, or after Ken says a claim was made.
---
# roster.sync

First step of every lineup skill. Read-only.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Steps
1. Run `python3 /workspace/fantasy/quantum-blitz/espn_api/cli.py sync`. It writes `data/roster.json` in the repo with lock flags. Never print auth values.
2. If auth fails, stop and tell Ken the ESPN login has expired.
3. Compare with the previous roster. If a player appeared or disappeared that Ken did not order, ask Ken before treating it as correct.
4. Update `data/schedule.json` with this week's kickoff times and record each player's lock state from ESPN's lineupLocked and rosterLocked flags.
5. Count the roster against ESPN's 17 spots and flag an empty spot.
6. Commit and push.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.

## Hard stops
No adds, drops, trades, IR moves, claims, or lineup changes.
