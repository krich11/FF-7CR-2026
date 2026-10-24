---
name: lineup.lock
description: >-
  Use Sunday at 9:53 AM, 10:35 AM, and 2:05 PM CT to check inactives and swap out
  any Quantum Blitz starter who is officially inactive or OUT before his game locks.
---
# lineup.lock

Sunday inactives checks for Quantum Blitz at 9:53 AM (with the dead-man), 10:35 AM, and 2:05 PM CT.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Steps
1. Run roster.sync if the roster file is over six hours old.
2. Read `data/availability.json` and the official inactive lists for games that have not kicked off.
3. For each starter who is ESPN OUT or on an official inactive list, pick the best unlocked bench player who can fill that slot.
4. Apply the swap with espn.api-apply under Ken's standing Sunday dead-man authority (lineup only), then report it to Ken as verified or unverified. If Ken said "hold" or "stop", post the swap as a recommendation instead.
5. If nothing needs to change, say nothing.
6. Never touch a player whose game has started. Never invent an inactive.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.
