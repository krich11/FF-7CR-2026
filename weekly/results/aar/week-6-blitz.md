# Week 6 adversarial AAR — Blitz
Date: Tue Oct 20, 2026, 9:00 CT standing hotwash (run started ~9:01 AM CT)
Bar: point maximization. Never miss a real signal; never promote noise.
Prior week: NFL Week 6 (through MNF WSH@SF, Mon Oct 19)
Result (ESPN final, from `weekly/results/week-6-scorecard.md`): **L 113.02–125.74** vs Buck up Buttercup! (BuB, team 6) · record 1-5 · 11th of 12 · PF 612.76
Sources read: `weekly/cards/week-6.md`, `weekly/decisions/week-6.json`, `weekly/results/week-6-scorecard.md`, `weekly/results/aar/week-5-blitz.md`, `data/recon/fa-week-6.md`, `weekly/audit/blitz-audit.log`, `playbook/LESSONS.md` (incl. Oct 8 "what counts as a mistake"), `playbook/WAR.md`, `playbook/CONSULT.md`, git log Oct 13–20, cached read-only ESPN pull `/workspace/w6/pool_rows.json` (Tue Oct 20 ~7:03 AM CT). No ESPN write from this hotwash.

Test applied to every item (Ken, Oct 8): a miss counts only if the fact was on disk before lock. A box score is not that fact.

## What went right
- **Every move we made scored.** Marks claim (10.1, 78% snaps as HOU RB1), Bernard FA add + FLEX (25.7, 94% snaps, 12 targets), Harvey Thursday start (14.6), Gay K (12.0 vs Pineiro 5.0). Waiver order spent once (Marks), FA used for the rest.
- **Saved branch re-scored instead of fired blind.** Friday, the Oct 12 "Henderson Q → FLEX" branch was re-checked against the live roster; Bernard held (25.7 vs 3.0, +22.7). Lesson already logged Oct 20.
- **W5 play-caller lesson held.** No new play-caller change on a QBZ starter's team went unflagged; Harvey's DEN split (40% vs Dobbins 52%) was on the card as a known split.
- **Availability clean.** Every starter played; 10:40 AM and 2:05 PM CT Sunday sweeps clean; Jacobs (Exempt) and Etienne (IR) stayed out.

## What we attacked
1. **Kicker stream sat on disk four days and never reached the card. Counts (fact on disk before lock).** Recon's FA dump (`data/recon/fa-week-6.md`, on main Wed Oct 14 3:53 PM CT) said in its own summary line: Zvada (NYG) 10.91 and Gay (LV) 10.71 vs Pineiro 8.97, both clear the 1.5-point line, "a one-week streamer move if Ken wants it." The Wed 8:19 PM, Thu and Fri card updates all kept **"K Pineiro — START (only K)"** with no FA line and no question to Ken. Ken found it himself and typed `claim Matt Gay drop Eddy Pineiro` Sun 7:50 AM CT. Result: Gay 12.0 vs Pineiro 5.0, **+7.0 kept by Ken, not by Blitz.** Root cause: the card treats single-occupant slots (K, D/ST, QB on a bye) as "only X, START" and never merges Recon's FA line into them. This breaks Blitz's merge job (Wire + Sigma + Recon) and the Oct 18 decision-card rule (end by asking Ken to approve the move).
2. **Team-total misstatement in the War Room, Sun Oct 18.** Blitz said QBZ projected ~124; the real figure was ~107 (92.3 for the eight unplayed starters plus Harvey's 14.6). Assistant caught it. Cause: total stated without adding the slots. Recorded in Blitz memory Oct 18 but **not yet in LESSONS.md** — appended today.
3. **TE: Goedert started, Pitts 23.0 / Henry 14.8 on the bench (−10.9).** On disk Friday: Hurts ruled out, McKee starting, TE gap 1.42. The card wrote "still the top TE projection, no change" without a CLOSE label or workload line. Already logged Oct 20 (QB change = role change). On workload the call stands (W5 Goedert 9 tgt / 69% vs Pitts 6 / 67%; W6 Goedert 8 tgt / 81% with McKee). The process gap is real; the 10.9 is mostly Pitts' two TDs.
4. **QB: Brissett 6.92 at LAR vs FA Penix 23.1.** Recon had Penix 15.16 (Q, ribs) vs Brissett 15.25 — a wash under the 1.5 line, and the card named the tough Rams spot. Not a train-on miss (coin flip, box score). Noise.
5. **WR2: G. Wilson 8.4 over Meyers 13.3.** 5.2-point projection gap. Box score. Noise.
6. **Ceiling.** Best possible lineup 131.42 would have beaten BuB by 5.68. Of the 18.40 left on the bench, only the TE slot traces to a fact on disk before lock, and workload still favored Goedert. The loss was swingable but not by a call the data supported.
7. **Decisions file stale through lock.** Already logged Oct 20; fixed in the makeup (final ESPN lineup now in `weekly/decisions/week-6.json`).
8. **Assistant inputs missing on main again.** `data/projections/week-6.json`, `data/usage/week-6-baseline.json`, the post-Monday usage packet and `week-6-brief.md` are absent for a second straight week. Second projection source and usage baseline were n/a in the scorecard. Blitz names the gap on cards; the fix is in Assistant's lane.
9. **Weather / roof / referee / travel / script.** ARI @ LAR at SoFi (fixed canopy). London trip (HOU @ JAX) handled by the 7:15 AM check. No verified weather, referee-crew or crowd signal in hand that would have flipped a starter; not researched further this run, nothing invented.

## Signal vs noise
- **SIGNAL:** Recon's own "clears the 1.5 line" FA flag on a single-occupant slot (K) — on disk Wednesday, worth +7.0, and caught only because Ken looked. Starting-QB change on a starter's team (Hurts out) as a role-change trigger (already ruled).
- **NOISE:** Pitts' two TDs, Brissett's 6.92 vs Penix 23.1 on a tied projection, Meyers over G. Wilson, Titans D/ST 19.0 (proj 4.94), Henry 14.8, Zvada 8.0 vs Gay 12.0.

## Method correction (one)
- **No "only X" slot on a card.** For K, D/ST, and QB when the backup is on bye, the card copies the best FA from Recon's Wednesday dump onto that slot's row with both ESPN projections. If the FA clears the 1.5-point line, the card adds one decision line that asks Ken directly (e.g., "claim Matt Gay drop Eddy Pineiro?") the same day the dump lands, not Sunday. FA moves cost no waiver order, so the cost of asking is zero. Week 6 cost of skipping it: +7.0 that Ken had to find himself.

## Consequential for Ken?
- Kicker stream: Recon flagged Gay/Zvada Wednesday; Blitz never put it on the card. Ken's own Sunday move kept +7.0. Rule now in LESSONS.
- Team-total misstatement (124 vs 107) now in LESSONS.
- No action needed from Ken. No ESPN write.
