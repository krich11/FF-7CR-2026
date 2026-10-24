---
name: week.scorecard
description: >-
  Use Monday after Quantum Blitz games to build the comprehensive Week N
  scorecard and email Ken a short text summary with the markdown file attached.
---
# week.scorecard

Build and email the comprehensive Quantum Blitz Week N Scorecard. Does not change lineups or claim waivers.

## Writing rules (Ken, Oct 20 2026 — mandatory)
- Plain, standard English. Every line is a full sentence a casual reader understands.
- No fantasy-football or AI jargon or abbreviations (no FLEX mean, HOLD/KILL, CARD DIFF, delta, edge, shadow, variance, WO, AV, etc.). Say what happened in ordinary words. Position names (quarterback, running back, tight end, kicker, defense) are spelled out.
- No label:value lines, arrows, symbol shorthand, or headline fragments. Tables only for simple score lists, with plain column names.
- No showing off: no methodology talk, model names, confidence scores, or internal file and commit references in the body.
- Report only what happened and what it means. Never list what didn't happen, isn't a concern, or was ruled out.
- Keep it short: who won, the score, how our lineup did, what we got wrong, points we left on the bench, and what we will do differently.

## Paths
- Spec/template: `/workspace/fantasy/quantum-blitz/SCORECARD.md` (the writing rules above override any template wording)
- Output: `results/week-{N}-scorecard.md`
- Email: `preferences.json` → `scorecard.email_to` (default Ken self-mail)
- Inputs: `results/week-{N}.json`, `form.json`, `usage.json`, `sources.json`, `standings.json`, `decisions/week-{N}.json`, `roster.json`

## Steps
1. After box scores exist for week N, fill the scorecard from real data only (skip a section rather than invent numbers). Add team totals from the live slot scores.
2. Write `results/week-{N}-scorecard.md`.
3. Email via Gmail `send_message`:
   - `to`: `[scorecard.email_to]`
   - `subject`: `Quantum Blitz Week {N} Scorecard: {record}`
   - `body`: a short plain-English summary in full sentences, ending with "The full scorecard is attached."
   - `attachments`: one file, `week-{N}-scorecard.md`, `mimeType` `text/markdown`, `content` base64 of the markdown file
4. Post a short chat summary in the same plain style. Do not paste the full report in chat.
5. Log `SCORECARD_EMAILED week=N to=... attach=md` in `audit.log`.

## Hard stops
No ESPN writes. If box scores are missing, skip the email and say so in chat. If Gmail fails, save the md file and alert Ken.
