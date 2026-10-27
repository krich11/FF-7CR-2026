---
name: lineup.lock
description: >-
  Use Sunday at 9:53 AM, 10:35 AM, and 2:05 PM CT to check inactives and swap out
  any Quantum Blitz starter who is officially inactive or OUT before his game locks.
---
# lineup.lock

Sunday inactives checks for Quantum Blitz at 9:53 AM (with the dead-man), 10:35 AM, and 2:05 PM CT (recommend and wait), plus the inactive dead-man at 11:45 AM and 2:50 PM CT.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Steps
1. Run roster.sync if the roster file is over six hours old.
2. Read `data/availability.json` and the official inactive lists for games that have not kicked off.
3. For each starter who is ESPN OUT or on an official inactive list, pick the best unlocked bench player who can fill that slot.
4. At 9:53 AM, apply the swap under the Sunday dead-man. At 10:35 AM and 2:05 PM, do not apply: message Ken in the War Room with the recommended swap and ask "swap X out for Y?", and save it to `weekly/pending/week-N-inactive-swap.json` with the deadline (11:45 AM CT for noon games, 2:50 PM CT for 3:05 and 3:25 PM games). If Ken says yes, apply it at once with espn.api-apply. If Ken has not answered by the deadline, the inactive dead-man applies it, verifies it, and tells Ken. A no or hold from Ken cancels it.
5. If nothing needs to change, say nothing.
6. Never touch a player whose game has started. Never invent an inactive.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. All times CT.
