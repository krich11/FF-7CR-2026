---
name: projections.validate
description: >-
  Use after fetching Quantum Blitz week projections to confirm PPR scoring, flag
  big source gaps, and zero out OUT, IR, PUP, or Exempt players before optimizing.
---
# projections.validate

Checks projection numbers before they reach a Quantum Blitz lineup decision.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Inputs
ESPN projections from the live pull, and Assistant's `data/projections/week-N.json` (due Friday 12:00 PM CT). If Assistant's file is missing or says AV FAIL, use ESPN alone and say so.

## Steps
1. Confirm every source is PPR. If a total leaves out catches, it is standard scoring; add one point per catch.
2. If two PPR sources differ by more than 3.0 points for a player, use the average and note that the number is uncertain.
3. Any player ESPN tags OUT, IR, or bye, or who has an official_block, projects to zero.
4. Write the checked numbers to `data/projections.json` in the repo and push. Never invent a number; leave it empty instead.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.
