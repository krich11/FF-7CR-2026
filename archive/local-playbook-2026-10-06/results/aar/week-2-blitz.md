# Week 2 adversarial AAR — Blitz
Date: 2026-09-22 (Tue 9:00 CT standing hotwash)
Bar: point maximization / next-season training
Prior week: NFL Week 2 (through MNF 2026-09-21)
Result (ESPN settled): **L 83.1–104.02** vs Charlie Don't Surf (CDS) · record 1–1
Note: `results/week-2-scorecard.md` missing — Mon `WEEK_REVIEW_SKIP` (MNF live); actuals reconstructed from ESPN `mMatchup` scoringPeriodId=2 (not invented).

## What went right
- **Fri dead-man:** AUTO-APPLIED FLEX Pitts → Tucker Fri 10:11 PM CT; gates 1–10 pass; no `resource_exhausted` (W1 contrast).
- **Wed set_backup:** FLEX Pittman → Pitts after Pittman LIMITED (foot) — correct path; Pittman later official OUT.
- **Tucker FLEX:** TE2 premium fail (0.52 < 1.5) + Bowers Doubtful → START. Actual **22.9** vs Pitts bench **2.5** (**+20.4**). Process win, not pure luck.
- **Pineiro HOLD:** Sigma `w2-k-swap.md` Net EV best −0.25 < +1.0; K_SWAP_DEADMAN STOOD_DOWN; Pineiro ACTIVE official; scored **5.0**. Correct vs FA stream.
- **IR / eligibility:** Charbonnet PUP on IR; Jacobs EXEMPT never soft-started; Pittman OUT benched; Sun AM LINEUP_LOCK NO_SWAP (1pm starters clear).
- **Wilson** 16.7 vs 15.86 adj — on/above card.

## What we attacked
1. **Goedert TE through knee (1.4 vs 11.24 adj, −9.84)** — In-game QTR @TEN (Inquirer/beat ~1:59 CT Sun); pre-game ACTIVE, no Fri/Sun designation to sit him. Only TE alt = Pitts (2.5) → counterfactual TE swap **+1.1** only. Not a predictable start/sit miss from data we had. Post-game MCL “few weeks” (Schefter/Rapoport Mon) → W3 TE = Pitts is the real signal. Class: injury luck / post-week IR geometry — not Fri card error.
2. **Tucker flip quality** — Edge was thin on proj (Pitts 10.38 vs Tucker 9.86; premium rule forced flip). Outcome boom validates rule + Bowers inactive. Shadow `share_trend` would have kept Pitts (`flip_vs_spec: true`) and lost **20.4** — anti-promotion for that paper signal.
3. **Pineiro Q illness only-K** — Correct HOLD; illness resolved ACTIVE. No process miss. Actual 5.0 soft vs proj 7.02 — noise vs limited-duty fear.
4. **Dart MNF @ LAR (0.8 vs 18.23)** — Sole rostered QB; no sit/start vs bench QB. Post-SNF trail ~82.3–104 needing 21.8+ was real; Dart left opening drive L knee → Winston. Failure mode = injury, not LAR matchup fade we should have sat. Murray claim Mon night was Ken-typed after injury (process OK; waivers never auto). Sole-QB depth was the structural risk.
5. **Fri/Sun automations** — Fri apply success; Sun autocommit skip correct (`no_1pmET_starter_OUT`). No W2 `resource_exhausted`.
6. **Monday week.review SKIP** — PROCESS_MISS. `WEEK_REVIEW_SKIP` Mon 10:37 AM CT (MNF pending) never resumed after settle → no scorecard, standings stale at W1. AAR had to reconstruct. Weather/roof/ref/12th-man: no verified ignored signal that would have flipped a starter (Dart @ SoFi roof irrelevant once knee ended the game).

## Signal vs noise
- SIGNAL: TE2 premium FLEX rule paid; Fri dead-man healthy; week.review must not die on MNF SKIP; Goedert MCL → multi-week TE plan; shadow share_trend wrong this week (stay paper); sole-QB = catastrophic MNF path.
- NOISE: “should have benched Goedert” from in-game knee; Dart vs LAR as a start/sit lesson; Tucker single-game boom as permanent FLEX dogma; Achane/Etienne under (Kamara haircut already on card) as optimizer rewrite.

## Method corrections
- **One fix:** `week.review` SKIP for live/incomplete MNF is **not terminal** — mandatory resume after final game settles (same night or Tue AM before AAR) and write `results/week-N-scorecard.md`. Do not leave `WEEK_REVIEW_SKIP` as the last word.

## Consequential for Ken?
- AAR log only this hour. Goedert OUT (MCL few weeks) + Dart Q/OUT path + Murray claim pending already on Mon AV / Ken-typed waiver — no new claim/lineup apply from this hotwash.
- Scorecard still absent — Blitz may run week.review makeup separately (not emailed from AAR).
