---
name: week.scorecard
description: >-
  Use Tuesday morning after Quantum Blitz games to build the Week N scorecard and
  email Ken a short summary with the markdown file attached.
---
# week.scorecard

Builds and emails the Quantum Blitz Week N scorecard. Does not change the lineup or file claims.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Writing rules
Follow Ken's writing rules in PLAYBOOK.md and the template `playbook/SCORECARD.md`. Plain full sentences, the final score once, no math, no data-check notes, opponent by full team name.

## Steps
1. Fill the scorecard from real data only: `weekly/results/week-N.json`, `weekly/decisions/week-N.json`, `data/standings.json`. Skip a section rather than invent numbers.
2. Write `weekly/results/week-N-scorecard.md`, commit and push.
3. Send it directly with Gmail send_message (never leave it in Drafts): to kaalrich@gmail.com, subject "Quantum Blitz Week N Scorecard: W-L", a short plain body ending "The full scorecard is attached.", and the markdown file attached as text/markdown.
4. Log SCORECARD_EMAILED in `weekly/audit/blitz-audit.log`.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. All times CT.

## Hard stops
No ESPN writes. If results are missing, skip the email and say so. If Gmail fails, keep the file and tell Ken.
