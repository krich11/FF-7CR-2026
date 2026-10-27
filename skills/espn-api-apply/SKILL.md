---
name: espn.api-apply
description: >-
  Use when applying or verifying a Quantum Blitz ESPN lineup via the fantasy API,
  including the post-write ESPN read-back and a Ken alert on any failure.
---
# espn.api-apply

The only ESPN lineup write path for Quantum Blitz: a REST lineup transaction followed by a fresh ESPN read-back.

## Setup (every run)
1. Pull main in the repo checkout: `cd /workspace/ff-repo && git -c credential.helper= pull -q --rebase https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git main`. Never echo the token.
2. Read `PLAYBOOK.md` (the rulebook), plus `RULES.md` and `STRATEGY.md` when making a recommendation. All data and rules live in the repo; the old folder `/workspace/fantasy/quantum-blitz/` is used only for the ESPN client (`espn_api/`) and its auth file, which is never printed.
3. After writing, commit and push: `git -c credential.helper= push -q https://x-access-token:${QBZ_GITHUB_TOKEN}@github.com/krich11/FF-7CR-2026.git HEAD:main` (rebase-pull and retry once if rejected).
4. If ESPN auth fails at any point, stop and tell Ken that the ESPN login has expired. Never re-export cookies.

## Paths
- CLI: `python3 /workspace/fantasy/quantum-blitz/espn_api/cli.py {sync|plan|apply|verify|starters}` (league 1776545061, team 13, season 2026 are built in).
- The CLI reads its target lineup from `/workspace/fantasy/quantum-blitz/decisions/week-N.json`. Before plan or apply, copy the repo's `weekly/decisions/week-N.json` there so the CLI uses the repo card.
- Auth: the existing auth file in the old folder's secrets directory. Never print, copy, or refresh it.
- Write log: the client appends to `weekly/audit/espn-writes.log` in the repo; commit it.

## Auth failure
If any read or write returns 401 or 403, stop. Tell Ken: "The ESPN login has expired, so I could not read or change the lineup. Please sign in again." Do not open the browser to re-export cookies, and do not fall back to clicking the page.

## Apply (lineup only)
Only after Ken's "yes, set it" or a valid Sunday 9:53 AM CT dead-man (see PLAYBOOK.md).
1. Check every slot to be moved is unlocked (lineupLocked false).
2. `cli.py plan --week N` and confirm the moves match the card.
3. `cli.py apply --week N`.
4. Read the result. `noop: true` means ESPN already matched. `alert: true` means the write did not verify: tell Ken right away which slots do not match, log ESPN_API_VERIFY_FAIL in `weekly/audit/blitz-audit.log`, and never call it done.
5. Always finish with `cli.py verify --week N` (a fresh ESPN read). Report the change to Ken as verified or unverified, naming the players who moved.
6. Rewrite `weekly/decisions/week-N.json` from that fresh read, then commit and push.

## Sync (read)
`cli.py sync` writes `data/roster.json` in the repo (and a local cache). Commit it.

## Output
Plain standard English in full sentences, per Ken's writing rules in PLAYBOOK.md. All times CT.

## Hard stops
Never print auth values. Lineup moves only: never waivers, adds, drops, trades, or IR moves. Never apply without approval or a valid dead-man. Never report a write without a verified read-back.
