---
name: week.review
description: >-
  Use Monday after games to learn from Quantum Blitz results: form, usage,
  sources, preferences, standings, email the Week N scorecard, and append
  durable lessons to LESSONS.md.
---
# week.review

Monday learning loop for Quantum Blitz after the NFL week, run once the last game is final. It updates form, usage, sources, preferences, and standings, and it never invents missing stats. It builds and **emails** the full Week N Scorecard and appends durable lessons.


## Lessons first (feedback loop, Ken Oct 20 2026)

Also read `RULES.md` and `STRATEGY.md` (repo root) (league rules canon, Ken Oct 23 2026) before any recommendation and run its checklist. Never propose moving or dropping a player whose game has started; check rosterLocked/lineupLocked first.
Before building or changing anything, pull main and read every fix rule in `playbook/LESSONS.md`. Apply each one that touches this run, and check the finished card or post against them before it goes out. Rules that matter most right now: no slot is ever marked "only X" (list the best free agent at K, D/ST, and QB with a bye backup, and ask Ken the same day if he clears 1.5 points); when a starter's team changes starting QB or play-caller, re-check that slot against the bench; add up team totals from live ESPN numbers before quoting one (never show the math to Ken); rewrite the decisions file from ESPN after every lineup change; no backup plans without an ESPN tag or real news.

## Paths
Operating disk is GitHub `krich11/FF-7CR-2026` on `main`. Pull before reading or writing, and push with `QBZ_GITHUB_TOKEN` only. Timezone is America/Chicago. Scorecard: `SCORECARD.md` template + [week.scorecard](sand-workflow:week-scorecard), output under `weekly/results/`. Lessons: `playbook/LESSONS.md`. Audit: `weekly/audit/blitz-audit.log`.

## Inputs (from Assistant, per issue 5, Oct 6 2026)
- Second projection source: `data/projections/week-N.json`, due Friday 12:00 PM CT. If it says `AV FAIL` or is missing, hold last week's source weights and say so.
- Pre-week snap/role baseline: `data/usage/week-N-baseline.json`, due Friday 12:00 PM CT. Use it for usage_gap and role_mult. Missing means n/a.
- Actual snaps: nflverse snap counts.
- Assistant's post-Monday usage packet under `agents/assistant/work/` when present.

## Steps
1. Confirm on ESPN (read-only) that the matchup is final. If not, log WEEK_REVIEW_SKIP and stop. Never score a live week.
2. Pull actual PPR, targets, and carries from ESPN for every rostered player, starters and bench, and snaps from nflverse.
3. Write `weekly/results/week-{N}.json` with actual PPR, our adj going in, and the slot started or benched.
4. Score form, usage, and sources from the inputs above. Shadow-edge picks are retired, so scorecard section 6 stays empty.
5. Update `data/standings.json` and the process-miss flags.
6. Run [week.scorecard](sand-workflow:week-scorecard) and email the short summary with the `.md` attached to the scorecard address.
7. **Lessons:** append 0–3 durable bullets to `playbook/LESSONS.md`, only for things that should change next week or next year.
8. Log WEEK_REVIEW and SCORECARD_EMAILED in the audit log and push.
9. Chat gets a short TLDR only.

## Validation
- Form is intra-roster only. Nothing here auto-applies to ESPN.
- Every number traces to ESPN, nflverse, or an Assistant file. Anything else is n/a.
- The email body is short, and the full report is the attachment.

## Approval
Read-only for ESPN. The email send is expected when data exists. No lineup apply, waivers, drops, or trades.

## Hard stops
If box scores can't be fetched, skip and log it. Don't email a fake scorecard. Don't ping retired Wire, Sigma, or Recon.
