---
name: lineup.tweak
description: >-
  Use for the Quantum Blitz close-call checks on Friday about 3:30 PM, Saturday
  about 8:30 PM, and Sunday about 8:30 AM CT to re-check unlocked lineup slots.
---
# lineup.tweak (close-call check)

Replaces the old Friday tweak. Runs Friday about 3:30 PM, Saturday about 8:30 PM, and Sunday about 8:30 AM CT. Only unlocked Sunday and Monday slots.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Steps
1. Run roster.sync. Read `data/availability.json`, Assistant's Friday files (`data/projections/week-N.json`, `data/usage/week-N-baseline.json`), and Assistant's latest file in `agents/assistant/work/close-calls/`. Note any file that is missing or late.
2. Run projections.validate on fresh ESPN projections.
3. Re-check every unlocked starting slot and start the player expected to score more, with news weighed as heavily as the projection.
4. Re-check any quarterback or play-caller change on a team we start.
5. Compare our K, D/ST, and backup QB with the best free agent. If a free agent is expected to score more, ask Ken the same day ("Pick up X and drop Y?"), after checking that Y is unlocked.
6. If a move is worth making, update the card and decisions file, commit and push, and ask Ken directly. If nothing changed, say nothing.
7. Apply only on "yes, set it".

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. All times CT.
