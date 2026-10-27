---
name: waiver.board
description: >-
  Use when posting a Quantum Blitz waiver or free-agent recommendation. Research and
  recommend only; never file a claim until Ken types the claim command.
---
# waiver.board

Waiver and free-agent recommendations for Quantum Blitz. The league uses traditional waiver priority, not a bidding budget.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Steps
1. Run roster.sync. Read Assistant's waiver watch and the free-agent dump in `data/recon/`.
2. Free agents first: they are instant and free. Use a claim only for a player who would start or fill a real hole for several weeks.
3. For each add, name the drop. Check the drop is unlocked, the add does not break a position cap, and the drop is our lowest rest-of-season value given byes and role.
4. Always compare our K, D/ST, and backup QB with the best free agent.
5. Describe each player with position, NFL team, and role, in plain sentences.
6. Lead with the most urgent move and its deadline, and end with the exact command for Ken ("claim X drop Y?").
7. Write the request to `playbook/CLAIMS.md`, commit and push. File nothing until Ken types the command; then file it and verify on a fresh ESPN read.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. All times CT.
