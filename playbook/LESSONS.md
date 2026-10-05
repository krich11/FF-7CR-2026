# Quantum Blitz — durable lessons (multi-season)

**Owner:** Blitz  
**Rule (Ken 2026-09-06):** We play the long game. Lessons from this year hone next year. Do not let insights die in chat.

## How to use
- After Monday week.review / scorecard: append anything that changed process, not just one-week noise.
- Tag: `PROCESS` | `STRATEGY` | `PERSONNEL` | `DATA` | `TEAM`
- Promote into SPEC / skills / TEAM.md only when proven (shadow/research ledgers, repeats, Ken OK for live optimizer).

## Season 2026

### Preseason / setup
- (2026-09-05) Dead-man autocommit = lineups only; waivers need typed claim; TEST boards need `for real` / confirm before ESPN write.
- (2026-09-05) Official EXEMPT/PUP/IR/OUT overrides ESPN soft tags — never soft-start ineligible.
- (2026-09-05) Org lanes: Blitz = Ken voice + claims; Wire = availability; Sigma = our stats; Recon = opponents + WAIVER WATCH.
- (2026-09-05) Paper edges + Sigma research tracks score vs SPEC; promote only after evidence (≈4–6 weeks / midseason briefs).
- (2026-09-05) Scorecard email = short text body + `.md` attach (not crude PDF).
- (2026-09-05) Hold waiver #1 pre-Week 1 unless true MUST / RB cuff; depth risk = Jacobs EXEMPT + Charbonnet PUP.
- (2026-09-08) Ken-facing times always America/Chicago (CT); convert from LA lock math / ISO. Games to watch kickoffs in CT.
- (2026-09-10) PROCESS: Proactively alert Ken same-day when QB status changes ripple to our pass-catchers (e.g. Tua limited → Rush → London/Pitts ceiling). Do not wait for Ken to connect it.
- (2026-09-09) PROCESS: Proactively surface empty-IR + IR-eligible bench stashes with a recommended add — never wait for Ken’s league mates. Prefer IR on multi-week PUP/IR (Charbonnet) over short/uncertain EXEMPT (Jacobs) when both eligible.

- (2026-09-10) PROCESS: Ripple assessments always use explicit categories — LIVE/LOCKED · FRIDAY CARD · BENCH UPSIDE · MULTI-WEEK TRACK · (optional) DST/SCRIPT — never a flat list.

- (2026-09-13) PROCESS: Blitz owns all specialist triggers; Wire/Sigma/Recon no self-cron; Ken gets compact human English from Blitz only; inter-bot shorthand OK to cut tokens.

### In-season (append below)
<!-- Monday reviews add here -->

- (2026-09-14) STRATEGY: Backup-QB TE flip is real — Goedert over Pitts under Rush (23.7 vs 0) won Week 1 TE slot; default Goedert when starter QB OUT and Pitts adj collapses.
- (2026-09-14) PROCESS: Fri tweak/autocommit `resource_exhausted` missed the scheduled window; makeup Sat still saved the TE flip, but treat Fri fail as PROCESS_MISS — alert Ken + retry earlier, do not wait for Monday.
- (2026-09-14) DATA: ESPN fantasy/site boxscores gave targets/carries/PPR but **no snap%**; Week 1 form_add stays 0; do not invent snaps.



- (2026-09-20) PROCESS/TEAM: Tuesday 9:00 CT adversarial AAR is standing for Blitz/Wire/Sigma/Recon (self-triggered). Always log in-bot chat. Durable findings → **same-day core prompt/charter patch** (not notes-only). Ops triggers still Blitz-owned; AAR is the exception.
- (2026-09-20) DATA: Snap% still missing from ESPN fantasy feeds — Sigma must degrade usage residuals / flag DATA_QUALITY until an alternate snap source is wired; never invent.

- (2026-09-22) PROCESS/DATA: Blitz-URGENT / named-player AV must still **full-roster scan** (bench in-game exits + Mon coach updates) before write — W2 miss left Brooks ACTIVE/stale after groin exit while Dart+Goedert were updated. Wire charter patched same day.

- (2026-09-22) PROCESS: week.review SKIP for live/incomplete MNF is not terminal — resume after final settle (same night or Tue AM before AAR) and write the week scorecard; do not leave WEEK_REVIEW_SKIP as last word.
- (2026-09-22) STRATEGY: TE2 premium FLEX rule validated in W2 (Tucker 22.9 vs Pitts 2.5, +20.4); shadow share_trend disagreed and lost — keep share_trend paper-only.

- (2026-09-22) PROCESS/STRATEGY: **Tight-spot contingency protocol** (sole QB OUT / multi-week hole). On trigger, Blitz proactively bubbles — don't wait for Ken:
  1) **Waiver ladder** before process: ranked #1 claim + #2 seatbelt (same drop OK); claims are private; process time + rank called out.
  2) **Bridge vs hold**: compare 3-week slate Σ vs ROS; only recommend cheaper bridge if it *beats* the hold on the short window *and* Dart-return timeline is real.
  3) **FA devil's-advocate**: check *our league* availability first; global%-owned ≠ free here.
  4) **Trade scout**: map every club's surplus starter-quality backup → their injury itch → our surplus chips; rank by (a) upgrade quality (b) **threat** (PF + when we play them — never arm this week's opponent pre-games) (c) chip cost.
  5) **Timing**: Plan A waiver before binding trade; soft-touch trades OK pre-process; finalize trade after claim result unless Ken prefers lock-now certainty.
  6) **Dual-QB matchup flex** only if long-term hole justifies bench cost; else start better QB / trade spare.
  7) Always end with **recommend / no-recommend** and what Ken must type. No ESPN write without command.

### Carry into 2027
<!-- End-of-season rollup -->

## 2026-09-25 (W3 Fri) — Recommend only after homework
- Sent Ken pickup/claim commands (Geno, then Winston) off ESPN projections before checking the player's actual stats, matchups, job security, or asking Sigma/Recon/Wire. Ken called it out twice.
- RULE: No add/drop recommendation or paste line until (1) Sigma matchup + per-game stats, (2) Wire news/job-security, (3) Recon market are in and merged. Show evidence with the call. Interim status updates carry no pick.

## 2026-09-26 — Allgeier drop / Steelers-drop rec
The Allgeier drop left QBZ with no healthy backup RB. A follow-up rec then proposed dropping the long-term Steelers D/ST for a one-week rental, got Etienne's team wrong, got waiver timing wrong, and ranked the WR drop by fill order instead of usage. The root cause was judging each move on its own. Fix: the PRE-MOVE GATE in BLITZ.md.

- (2026-09-27) PROCESS: Blitz proposed dropping the Steelers D/ST in the Gordon claim, and all three specialists voted for it. That contradicted the standing Week 4 plan to drop the Panthers as a one-week streamer. Ken caught it. Rule: before naming any drop, check it against WAR.md and cards/week-N.md standing plans and cite the plan line.
- 2026-09-27 6:32 PM CT: We voted 4-0 to swap Brissett for Mayfield using two weeks of data while both QBs were still playing Week 3. Brissett then scored 25.6 and Mayfield 11.28, and the trade went on hold. Rule: no player-swap vote while either player's game is live or unscored; wait for final boxes.

- 2026-09-27: Players stay locked through the scoring period after their game; ESPN standalone drop = type ROSTER + item DROP (FREEAGENT requires ADD). Check lock before promising a drop.

- (2026-10-04) PROCESS: When Ken asks about the lineup, the answer covers every rostered player, not only the slots already in the discussion. Deadline is his lock, not kickoff. Week 4 miss: Sunday checks stayed on quarterback and tight end and never put Gordon back on the table. He scored 18.0 (9 carries, 100 yards, a touchdown, 2 catches) while Henderson scored 4.2. A Saturday sit is not final. "The other guy is active" is not a reason to skip a back who just had the workload, especially when the injured starter is out for the year.
