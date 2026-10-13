# Week 5 adversarial AAR — Blitz
Date: Tue Oct 13, 2026, 9:00 CT standing hotwash (run started ~9:31 AM CT)
Bar: point maximization. Never miss a real signal; never promote noise.
Prior week: NFL Week 5 (through MNF Mon Oct 12)
Result (ESPN final): **L 104.58–174.56** vs Fantasy Rookie No More (FR, team 3) · record 1-4 · PF 499.74 (12th of 12)
Sources read: `weekly/cards/week-5.md`, `weekly/cards/week-5-sunday.md`, `weekly/decisions/week-5.json`, `weekly/handoff/week-5-consultant.md`, `weekly/results/aar/week-4-blitz.md`, `weekly/audit/blitz-audit.log`, `weekly/audit/espn-writes.log`, `agents/assistant/work/harvey-week5.md`, `agents/assistant/work/week-5-brief.md`, `data/recon/fa-week-5.md`, `playbook/LESSONS.md`, `playbook/CONSULT.md`, live ESPN `mMatchup`/`mMatchupScore` read Tue Oct 13 ~9:33 AM CT (no write), nflverse `snap_counts_2026.csv` Weeks 1–5.
Note: **No `weekly/results/week-5-scorecard.md` or `week-5.json` on main.** Monday review skip logged `2026-10-12T23:30:23+08:00 WEEK_REVIEW_SKIP week=5 reason=MNF_not_final game=BUF@LAR`. Actuals below are from the live ESPN read, not a written scorecard.

## What went right
- **Gordon at RB (Wed apply on Ken "Put Gordon in").** 14.8 vs Henderson 4.8 and Meyers 5.7. The Week 4 close-call / reopen miss is corrected on the card and on ESPN. Workload rule held.
- **QB Brissett over Murray.** 25.28 vs 18.26, **+7.02 kept**. Both sources favored Brissett; just outside the 1.5 close line. Right call.
- **Goedert TE swap executed clean.** Official Eagles inactives ~7:05 AM CT (no Goedert), Ken yes-if-active, ESPN apply ~7:27 AM CT before London lock, verify ok. Process held under Consultant weekend cover.
- **Eligibility / dead seats.** Jacobs EXEMPT and Etienne IR sat at 0. Pittman 0 (IR-bound). Nobody ineligible was started.
- **Saturday-card shape.** `week-5.md` listed every rostered player, marked CLOSE slots, and named the Stevenson Friday flip for RB2/FLEX. Matches the Week 5 Saturday-card law from the Week 4 miss.
- **Open 17th spot filled.** Roster went 16→17 (Roman Wilson on the Week 5 roster read). Empty-spot lesson from W4 AAR was acted on (add timing was Ken/FA recon, not this card's job).

## What we attacked
1. **FLEX Harvey 11.12 proj → 0.7 actual. Predictable signal we missed.** Sean Payton took the Broncos call sheet back from OC Davis Webb. First reported Wed Oct 7 (Brandon Stokley, 104.3 The Fan); Payton announced it after Thu Oct 8 practice (Denver Gazette, AP). Public **days before** Sunday 3:05 CT lock. J.K. Dobbins got the work: 18 carries / 68 yards / TD + 2 catches (20 touches), **32 snaps (52%)**. Harvey: 3 carries / 7 yards, 1 target / 0 catches, **23 snaps (37%)**, 0.7 PPR. No injury, no demotion quote on the record — the new factor was the play-caller (`harvey-week5.md`). Neither Blitz nor Assistant put the OC change on the Week 5 card, the Thu handoff, or the Sunday plan. Bots were paused for the weekend (Ken Thu 7:33 PM CT); that does not excuse the gap — the news was already public when the handoff went up Thu 7:35 PM CT, and Stokley's report was Wed. **Cost vs best FLEX on the roster:** Pitts 15.2 − Harvey 0.7 = **−14.5**. This is the miss Ken already named; verified.
2. **No play-caller / coordinator sweep on any starter's team.** DEN (Harvey), MIA (Gordon), NE (Henderson/Henry), PHI (Goedert/Meyers), NYJ (Wilson), ATL (London/Pitts), ARI (Brissett), PIT (Steelers/Pittman), SEA (Pineiro). Only Harvey's team had a live change this week, and it was the one that mattered. The Saturday card checked injury tags and Stevenson status; it never asked "who is calling plays?"
3. **Stevenson Friday branch never closed in writing.** nflverse Week 5: Stevenson **53 snaps (71%)**, Henderson **12 (16%)**. Card + handoff said: if Stevenson is a full Friday participant and Harvey is clean, Harvey→RB and Meyers→FLEX before 8:30 AM CT. Sunday plan left Henderson at RB / Harvey at FLEX with no written Friday-report outcome. Net if the branch had fired (Meyers FLEX, Harvey RB, Henderson bench): Meyers 5.7 vs Henderson 4.8 = **+0.9** — noise next to the Harvey collapse. Still a process hole: OPEN close call with no recorded resolve.
4. **TE Goedert 9.8 vs Henry 13.4 (−3.6).** Ken-approved if-active; Goedert was active; swap was correct process. Projection favored Goedert (10.89 vs Henry blend 8.79). Per Ken Oct 8 rule (miss counts when the job had already changed on disk, not when the box score wins), this is **not** a train-on miss. Logged for completeness.
5. **Ceiling check.** Best possible lineup from the roster: Brissett / Gordon / Henderson / London / Wilson / Henry / Pitts / Steelers / Pineiro = **122.68**. Still loses to FR's **174.56** by 51.88. Result was out of reach; the Harvey miss is still ours. Left on the bench vs actual: Pitts over Harvey **+14.5**, Henry over Goedert **+3.6** (= 18.1).
6. **Weather / roof / referee / travel / script.** DEN @ LAC at SoFi (fixed roof) — no weather edge. No verified referee-crew or 12th-man signal in hand that would have flipped a starter. Not researched further this run; nothing invented.
7. **Monday scorecard still missing.** Same SKIP→resume pattern as Week 4. Rule on main (Sep 22 / Oct 6): SKIP is not terminal; write the scorecard after MNF settles. MNF is final as of this hotwash; scorecard write is out of scope for this AAR but the gap is real.

## Signal vs noise
- **SIGNAL:** Head-coach / OC play-caller change on a team with a QBZ starter (Payton reclaiming DEN calls) is a role-risk flag before lock — especially for a pass-down rookie sharing a backfield with a veteran early-down back. Harvey's FLEX was treated as locked; it should have been reopened once the call-sheet news was public. Gordon workload start = correct application of the W4 close-call rule.
- **NOISE:** Goedert vs Henry box-score gap (−3.6) after a correct if-active process. Stevenson-branch net (+0.9) if flipped. Murray vs Brissett either way after Brissett's big game (Brissett won). Steelers 1.0, Pineiro 6.0. Losing to FR's 174.56. Roman Wilson 0 on the new bench seat.

## Method correction (one)
- **Play-caller / coordinator check.** Every lineup card (Tue set, Fri tweak, Sunday plan) lists, for each team that has a QBZ starter or CLOSE candidate, whether the play-caller or OC/DC changed since the prior week (beat report, team release, or coach presser). If yes, mark that player's slot **ROLE-RISK**, reopen it against the bench on workload (not projection), and write one line naming the change and the evidence. Assistant's weekly refresh owns the scan; Blitz owns putting it on the card. Cost of skipping it in Week 5: Harvey 0.7 as FLEX while Pitts (15.2) and Henry (13.4) sat.

## Consequential for Ken?
- **Durable fix:** play-caller/coordinator sweep is now in `playbook/LESSONS.md` (dated Oct 13). Already previewed in Week 6 early-moves notes; this AAR makes it standing.
- **Harvey Week 6:** not a count-on RB (TNF vs SEA). See `harvey-week5.md` and CONSULT Week 6 order — separate from this hotwash.
- No ESPN write from this hotwash.
