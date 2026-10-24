---
name: lineup.set
description: >-
  Use for the Quantum Blitz set-the-week card on Tuesday at 2:03 PM CT (Wednesday
  12:13 PM CT backup) or when Ken says "set Week N".
---
# lineup.set

The week-opening start and sit card for Quantum Blitz.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Steps
1. Run roster.sync. Read `data/availability.json`, `data/recon/`, and Assistant's Tuesday brief in `agents/assistant/work/`.
2. Get ESPN projections for every rostered player and run projections.validate.
3. Fill all nine starting slots with the highest projection, unless ESPN's tag or an official list says otherwise. Mark every slot within 1.5 projected points of the best bench option as a close call; in MUST-WIN mode it goes to the higher-ceiling player facing the weaker defense.
4. Check any quarterback or play-caller change on a team we start, and compare our K, D/ST, and backup QB with the best free agent from `data/recon/`. No slot is ever "only X."
5. Add the adversarial check: each way the lineup could fail and the answer.
6. Write `weekly/cards/week-N.md` and `weekly/decisions/week-N.json`, then commit and push.
7. Post the card: lead with the call, list the lineup with kickoff times for starters only, and end with a direct question ("Set this lineup?").
8. On "yes, set it", apply with espn.api-apply. On "hold" or "stop", do nothing. There is no Tuesday autocommit; the only dead-man is Sunday at 9:53 AM CT.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.
