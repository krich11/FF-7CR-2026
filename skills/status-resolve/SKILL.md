---
name: status.resolve
description: >-
  Use when an injury or news report disagrees with ESPN's status tag for a Quantum
  Blitz player. ESPN is the only status source; reports are notes only and get
  flagged to Blitz the same day.
---
# status.resolve

ESPN's tag is the only status source (Ken, Oct 15 2026). An official NFL or team can't-play list (inactives, IR, PUP, suspension, Commissioner's Exempt) sets `official_block`, which benches a player even if ESPN lags; it never starts one, clears an ESPN OUT, or triggers an add. News is notes only.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Rules
- Set `state` in `data/availability.json` from ESPN's tag.
- Put any disagreeing report in `notes` with its source and time.
- Log STATUS_CONFLICT (player, ESPN tag, report, source) in `agents/assistant/work/assistant-audit.log` and tell Blitz the same day by direct message.
- Never start a player who is OUT, IR, on bye, suspended, or under official_block. Projections never change status.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. Name the inputs used (ESPN pull time, availability file time, Assistant's Friday files and latest close-call file where relevant) and name any missing or late file. All times CT.
