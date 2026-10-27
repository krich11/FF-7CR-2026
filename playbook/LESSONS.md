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

- (2026-10-06) PROCESS: A failed Monday review rides along with the next review run as a scorecard labeled MAKEUP. Don't park it waiting on a new routine. The Week 3 scorecard sat 8 days (Sep 28 → Oct 6) because the makeup was handed to a routine that a routine run can't create.
- (2026-10-06) DATA: A snap source now exists. nflverse `snap_counts_2026.csv` (release tag `snap_counts` on nflverse/nflverse-data) loads from the box and had 2026 Weeks 1–4 on Oct 6. MNF games post a day late. Use it for snap% instead of n/a. ESPN fantasy feeds still have no snaps.
- (2026-10-06) DATA: Take matchup scores from ESPN `mMatchupScore` totals, never from a handoff or memory. The Week 3 handoff said the opponent scored 129.54. ESPN says Patton's Posse scored 136.84, and their starters sum to that.

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

- (2026-10-06) PROCESS (W4 AAR): Count the roster against ESPN's 17 (9 starters, 7 bench, 1 IR) every week. QBZ carried 16 through Week 4 with an empty bench slot beside two dead ones. An empty spot goes into the next waiver request.

## 2026-10-08 — Ken: what counts as a mistake

Read this before the next AAR. Blitz and Assistant both.

A miss counts only if the fact was on the disk before lock. A box score is not that fact.

Preventable, and the one to train on: Week 4, Henderson started over Gordon. Achane was already out for the year. Gordon was on the roster because of that. The Sunday check never reopened the running-back slot. Gordon 18.0, Henderson 4.2. Rule: a season-ending injury ahead of a rostered player is a role change. Reopen that slot before lock and pick on workload.

Do not train on these. They were not knowable before lock:
- Week 3 Brissett 25.6 on the bench. That game is what made him the starter. Before it he had one good week and one bad one.
- Week 4 Brissett 10.4 started, Murray 11.5 on the bench. A wash after the correction.
- Week 4 opponent 163. Schedule.
- Week 3 Bateman started over Meyers on a gap under a point. Coin flip. The winner is the box score.

Do not add a rule because a bench player had one big game. Add a rule when the job had already changed and the card did not move.

- (2026-10-13) PROCESS/STRATEGY (W5 AAR): Every lineup card checks play-caller and OC/DC changes for every team that has a QBZ starter or CLOSE candidate. Public change → mark the slot ROLE-RISK, reopen on workload, write one evidence line. Assistant scans; Blitz puts it on the card. Week 5 miss: Payton took DEN play-calling back (public Wed–Thu Oct 7–8); Dobbins got 20 touches / 52% snaps; Harvey scored 0.7 as FLEX; neither bot caught it. Cost vs Pitts on the bench: −14.5.
- (2026-10-13) PROCESS (W5 review): The Monday week.review has skipped on a live MNF in Weeks 2, 4 and 5 and only ran when someone asked for a makeup. A SKIP must schedule its own one-shot rerun for Tuesday morning CT at the moment it skips, so the scorecard lands without a reminder.
- 2026-10-13 miss: W6 card omitted the Marks claim-failure contingency (Consultant caught it). Fix rule: every weekly card carries an Adversarial check section naming each failure point and its answer before posting.

- 2026-10-15 rule change (Ken, War Room): ESPN is the single source of truth for player status. Cause: Blitz labeled TreVeyon Henderson OUT from Schefter/Globe reports while ESPN showed DOUBTFUL, then QUESTIONABLE, and the card and Assistant disagreed. Fix rule: card, availability.json, and routines use ESPN's tag; news reports go in as notes only, never as the status.
- 2026-10-15 8:48 PM CT rule (Ken approved, War Room): ESPN decides status. Bench-only exception: an official NFL/team can't-play list (game-day inactives, IR, PUP, suspension, Commissioner's Exempt) benches a player even if ESPN lags. It never starts a player, clears an ESPN OUT, or triggers an add. News is notes only. Example: Jacobs is on the Exempt list while ESPN shows him DAY_TO_DAY.
- 2026-10-18 7:36 AM CT miss: Blitz's Friday answer and the Sunday pre-London post both laid out a London-inactive backup (Meyers, then Bernard/Pitts) when London had no designation and ESPN had him ACTIVE. Ken called it out. Cause: broke the Oct 7 rule against no-news backup plans. Fix rule: no backup plan for a player unless ESPN tags him or real news raises doubt. The Sunday sweep handles surprises silently.
- 2026-10-20 (W6 review) PROCESS: Re-check a saved branch against the current roster before it runs. Player: TreVeyon Henderson vs Germie Bernard. Cause: the Oct 12 "Henderson Q → FLEX" branch was written before Bernard was rostered; Blitz re-scored it Friday (ESPN 9.89 vs 8.70, snaps 92% vs 16%) and kept Bernard, who scored 25.7 to Henderson's 3.0 (+22.7). Fix rule: any saved branch older than the latest roster move gets re-scored against the live roster and projections before it fires; if it no longer wins, log why and hold.
- 2026-10-20 (W6 review) PROCESS: The decisions file records what is actually on ESPN. Players: Woody Marks, Germie Bernard, Matt Gay. Cause: `weekly/decisions/week-6.json` stayed at the Tuesday paste (Pitts FLEX, Henderson RB, Pineiro K) through lock and never logged the Wednesday waiver, the Bernard FLEX write, or the Sunday kicker add. Fix rule: after every ESPN write and at each lock window, rewrite `weekly/decisions/week-N.json` with the live ESPN lineup re-read from the API.
- 2026-10-20 (W6 review) STRATEGY/PROCESS: A starting-QB change on a starter's team counts like a play-caller change. Player: Dallas Goedert (TE) vs Kyle Pitts Sr. Cause: Friday Oct 16 the Eagles ruled out Jalen Hurts (Tanner McKee started) and the TE gap was 1.42 (Goedert 10.11, Pitts 8.69); the card kept Goedert without marking the slot CLOSE or writing the workload line. Fix rule: when a QBZ starter's team changes starting QB, mark the slot ROLE-RISK, run the 1.5-point CLOSE check against the bench, and write one workload evidence line before lock.
- 2026-10-20 (W6 AAR) PROCESS: No "only X" slot on a card. Players: Eddy Pineiro (K) vs Matt Gay / Dominic Zvada. Cause: Recon's `data/recon/fa-week-6.md` (main, Wed Oct 14 3:53 PM CT) flagged Zvada 10.91 and Gay 10.71 vs Pineiro 8.97, both clearing the 1.5-point line, but every Week 6 card update kept "K Pineiro — START (only K)" with no FA line; Ken found it and typed the claim himself Sun 7:50 AM CT (Gay 12.0 vs Pineiro 5.0, +7.0). Fix rule: for K, D/ST, and QB when the backup is on bye, the card carries the best FA from Recon's dump with both ESPN projections; if the FA clears 1.5, the card asks Ken directly ("claim X drop Y?") the day the dump lands. FA moves cost no waiver order.
- 2026-10-18 miss (logged W6 AAR Oct 20): Blitz told the War Room QBZ projected ~124; the real figure was ~107 (92.3 for the eight unplayed starters plus Harvey's 14.6). Assistant caught it. Cause: a total stated without adding it up. Fix rule: sum the slot projections from the live ESPN API before citing any team total. Do the math privately; Ken sees only the result in a sentence (Oct 20).

## 2026-10-23 Week 7: proposed dropping a locked player
- What happened: Blitz proposed adding Marks and dropping Hunter Henry, but Henry had already played Thursday night and ESPN locks a player once his game starts. Ken caught it; Assistant agreed with the wrong plan first.
- Fix rule: read RULES.md and STRATEGY.md (repo root) before every recommendation, check rosterLocked on mRoster before naming a drop, and propose only unlocked players.

## 2026-10-27 Week 7 review (lost 99.8 to 102.1 to David's Daring Team, now 1-6)
- Preventable misses: none. Every starter kept his expected role (nflverse W7 snaps: Wilson 85%, Bernard 91%, Marks 89%, Goedert 73%); the loss came from starters' box scores, and Gordon 17.3 / Harvey 14.0 / Henry 14.1 on the bench are not trained on (rule 7).
- STRATEGY (TE, Goedert vs Pitts): the Saturday card gap was 1.51 on ESPN (11.33 vs 9.82) and 1.5 at one decimal, so it was treated as a clear edge, not a coin flip; Pitts 13.2, Goedert 9.8, a 3.4-point swing in a 2.3-point loss. Fix rule: the 1.5-point CLOSE line is inclusive and read at one decimal (a gap of 1.5 or less is CLOSE), and in MUST-WIN mode a CLOSE slot goes on the card with its workload line (Goedert QUESTIONABLE most of the week under a new QB; Pitts snaps rising 51/67/78%) before Ken is asked.
- PROCESS (inputs): Assistant's post-Monday usage packet for Week 7 was not in agents/assistant/work/ at the Tuesday 7:30 AM CT review (also missing in Week 6). The review ran on ESPN plus nflverse snaps directly. Fix rule: Assistant posts the post-Monday packet by Tuesday 7:00 AM CT; if it is missing, the review pulls nflverse snaps itself, names the gap, and still sends the scorecard.
