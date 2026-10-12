# 2027 Draft Playbook: 7 Creeks Armchair Quarterbacks (ESPN PPR)
*Built Sun Oct 11, 2026, about 10 PM CT, from read-only ESPN data. 2026 points cover Weeks 1–4 (or 1–5 where labeled), so they're early-season samples. Anything marked **(opinion)** is judgment, not something the data proves.*

## What draft data exists
- **2026 (complete):** all 192 picks, a 12-team, 16-round snake draft that started Thu Sep 3, 2026, at **8:00 PM CT** (ESPN `draftSettings.date`), with 60 seconds per pick and no keepers (`keeperCount 0`). ESPN set the draft order at draft time (`orderType DRAFT_START`). **QBZ picked 12th**, at the turn, so we had picks 12/13, 36/37, 60/61 and so on. Every pick is in `draft_2026_full.csv` with its ESPN ADP, position, Week 1 projection, 2025 points, and Weeks 1–4 and 1–5 points.
- **2025 (complete):** reachable through the `leagueHistory` endpoint. It was a **10-team, 16-round** draft. Seven team IDs carry over (TE, PP, FR, BuB, TCO, LL, DDT). Team IDs 4, 7 and 8 belonged to different teams then (CTM, SST, LGO), and QBZ and MBB are new this year. ESPN doesn't provide 2025 ADP, so 2025 is used only for position and timing patterns.
- **2023–2024:** ESPN returns **404** for both. The league reports only 2025 as a prior season.
- **Roster settings (both years):** QB 1, RB 2, WR 2, TE 1, FLEX (RB/WR/TE) 1, D/ST 1, K 1, bench 7, IR 1. Scoring is head-to-head points, full PPR, 4 points per passing TD, and -2 per interception.

## 1. How this league drafts
- **Position runs by round (2026):**

  | Round | Picks |
  |---|---|
  | 1 | 6 RB, 6 WR |
  | 2 | 6 RB, 4 QB, 2 WR |
  | 3 | 4 WR, 4 RB, 2 QB, 2 TE |
  | 4 | 3 WR, 3 RB, 3 QB, 2 TE, 1 K |
  | 6–7 | 7 TEs total |
  | 10 | 3 D/ST, 1 K |

  By the end of round 5, **10 QBs** and **6 TEs** were gone.
- **QB timing:** the first QB went at pick 16, then 12 QBs were gone by pick 65 (early round 6). In 2025, with 10 teams, two QBs went in round 1. **This league takes QBs early.**
- **TE timing:** the first TE went at pick 25. Half the league had its starting TE by about round 6.
- **D/ST and K go early here:** the first D/ST went at pick 53 and the first K at pick 40. 2025 had the same pattern (D/ST in rounds 4–6, K in round 2). DDT took a D/ST in round 5, and LY and GGT took Ks in rounds 4 and 5.
- **Who reaches** (average of pick minus ADP for rounds 1–10; negative means picked earlier than ADP):

  | Team | Avg vs ADP | Where they reached |
  |---|---|---|
  | LY | -57.9 | QBs (Mayfield taken 151 picks early), TEs, Ks |
  | DDT | -31.2 | QB (Stafford, -74), D/ST, K |
  | QBZ | -30.2 | QB (Dart, -59), TE, RB |
  | GGT | -23.2 | K (-68), RB |

  The two teams closest to ADP were TE (-0.9) and LL (-6.4).
- **Reaching hasn't paid off, measured within position.** Following Blitz's method: regress Weeks 1–4 points on log(ADP) separately for QB, RB, WR and TE, then compare the leftover points (residuals) for rounds 1–10. Picks taken **15+ spots before ADP averaged -5.8** against **+5.0 for all others** (n=51 vs 59, SD about 17.7). The correlation between the residual and how early the pick was (Spearman) is 0.36. *I reproduced this exactly.* The sample is 4 weeks of one season (192 picks), so this is a direction, not a size, and it does not prove any particular cutoff. The earlier comparison against the next 12 players drafted is dropped: it mixed positions and used hindsight.
- **ADP source and timing:** the `adp` column is ESPN's `ownership.averageDraftPosition`, pulled **Sun Oct 11, 2026, about 9–10 PM CT, after our draft**. It is ESPN's current-season ADP, not a pre-draft snapshot. It probably includes drafts held after the preseason news (for example Jacobs on Aug 30) and after Week 1. This league's own 192 picks are a negligible share. **Every reach statistic here is therefore partly circular.** For 2027, save an ADP snapshot within 24 hours before the draft.
- **How well ADP predicted early scoring (Spearman correlation between ADP rank and Weeks 1–4 points):** RB 0.75, WR 0.71, TE 0.56, QB 0.50. ADP predicts RB and WR scoring well and QB and TE scoring only loosely.
- **QB and TE scoring by round (Weeks 1–4 average):**

  | Rounds | QB | TE |
  |---|---|---|
  | 1–3 | 73.6 | 58.7 |
  | 4–6 | 51.7 | 36.6 |
  | 7–9 | 70.0 | 46.9 |
  | 10–16 | 56.3 | 37.1 |

  Purdy (pick 95), Bryce Young (pick 190) and Shough (pick 146) are top-5 QB scorers so far. Small sample, but **QB is deep**.
- **Players already ruled out at draft time** (official status as of the Sep 3 draft, checked against the news; ESPN keeps no history of player status):
  - **Confirmed: 2, both ours.** Josh Jacobs went on the commissioner's exempt list Aug 30 ([USA Today](https://www.usatoday.com/story/sports/nfl/2026/08/30/josh-jacobs-commissioners-exempt-list-nfl-packers/91538596007/)). Zach Charbonnet started the season on PUP ([SI](https://www.si.com/betting/zach-charbonnet-injury-update-betting-impact-for-49ers-vs-seahawks-in-nfl-week-5-2026)).
  - The other 9 picks with a Week 1 projection of 0 were **not** out at draft time, or are unverified:
    - Brock Bowers had meniscus surgery on Tue Sep 8, after the draft ([NBC](https://www.nbcsports.com/fantasy/football/news/2026-nfl-week-1-injury-report)).
    - TreVeyon Henderson was ruled out for Week 1 with an ankle injury; I couldn't confirm when that became known.
    - Kamara was questionable and played.
    - Justin Tucker (0 games) is unverified.
    - Stroud, Cam Ward, Darnell Washington, Travis Hunter and Sadiq all played all 5 weeks. Their 0 projections were artifacts.
  - **Conclusion:** taking players who were already out was a QBZ problem, not a league-wide habit. (ADVERSARIAL.md has been corrected to match.)
- **Rookies:** taking "no 2025 stats" as a stand-in for rookies flags only 8 non-D/ST picks (GGT 3, CDS 2). That stand-in is weak, so **no conclusion**.

## 2. 2026 QBZ post-mortem: the shortfall split
Our 16 picks scored **208.9 points fewer** in Weeks 1–4 than players drafted at nearby picks (each pick compared with the average of the 6 picks before and after it; see `../opponents/ADVERSARIAL.md`). Each pick's gap is assigned to one bucket:

| Bucket | Points | Players |
|---|---|---|
| **Already out when drafted** | **-67.1 (estimate)** | Jacobs -39.4, Charbonnet -27.7. Both scored 0. The cost is measured against what players drafted at nearby picks scored (the average of the 6 picks before and after each pick), so it depends entirely on that baseline. |
| **Injuries during the season** (estimated points lost to missed games, capped at the pick's total shortfall) | **-95.4** | Brooks 21.4, Achane 18.2, Dart 17.0, Etienne 15.1, Pittman 12.3, Goedert 11.4 |
| **Underperformance on picks taken 15+ spots before ADP** (left after removing injury) | **-57.6** | Pitts -32.7, Achane -17.5, Etienne -7.4 (Dart and Goedert are 0 once their injuries are removed) |
| **All other picks, net** | **+11.2** | Wilson +14.4, Meyers +11.0, Darnold +9.4, against London -5.5, Pittman -8.4 and others |

**Which rule matters most:** Rule 1 (no players who are already out) carries the most weight. It addresses the largest *avoidable* bucket (-67), with no noise in the evidence. The reach default (Rule 2) addresses -58, but that number is noisier: one season, one month, and Pitts makes up more than half of it. The in-season injury bucket (-95) is mostly variance, and no draft rule fixes it.

## 3. Exploiting the league's habits (2026 + 2025)
- **The league spends early picks on QB, TE and K.**
  - **2026:** 33 of the first 96 picks (rounds 1–8) were QB, TE, D/ST or K (15 QB, 13 TE, 3 K, 2 D/ST). 26 of those 33 went before their ADP.
  - **2025 (10 teams):** 24 of 80 in rounds 1–8 (9 QB, 8 TE, 5 D/ST, 2 K).
- **The pay-off is real but small.**
  - 10 of the 29 RB/WR taken in rounds 5–8 of 2026 went after their ADP.
  - 4 fell 12 or more spots: Zay Flowers (taken 58th, ADP 36), Davante Adams (73rd, ADP 46), Tee Higgins (87th, ADP 58), and Bhayshul Tuten (92nd, ADP 74).
  - Those 4 averaged **65.8 points**, **+22.1** above the next 12 players drafted after them.
  - Small sample (n=4). **Confidence: medium on direction, low on size.**
- **Early D/ST and K picks barely helped the teams that made them.**
  - The 6 D/ST and K taken by round 9 (LY Aubrey round 4, DDT Texans D/ST round 5, GGT Myers round 5, GGT Broncos D/ST round 8, MBB Fairbairn round 8, BuB Dicker round 9) averaged **27.5 points**. The 14 taken in rounds 13 and later averaged 24.4, so early picking gained only **+3.1**.
  - The players taken in the 12 picks right after each early D/ST/K averaged **44.8**, so each of those picks gave up roughly **15–17 points** in Weeks 1–4.
  - **Confidence: medium.**
- **What disappears between our turn picks (2026, picking 12th):**

  | Gap between our picks | RB | QB | WR | TE | D/ST | K |
  |---|---|---|---|---|---|---|
  | Picks 14–35 | **9** | 6 | 5 | 2 | – | – |
  | Picks 38–59 | 6 | 4 | 6 | 3 | 1 | 2 |
  | Picks 62–83 | 6 | 2 | 8 | 6 | – | – |
  | Picks 86–107 | 4 | 4 | **10** | 1 | 1 | 2 |

  RBs drain fastest early; WRs go fast in rounds 6–9.
- **Turn-planning rule (confidence: medium; one season of draft order):**
  - At each turn pair, take the position that will be thinnest in the next 22 picks first.
  - **Rounds 1–2: take at least one RB.** About 9 RBs are gone before our round-3 pick.
  - **Rounds 3–5:** take whichever RB or WR ADP shows falling furthest. Expect about 8 QB/TE picks between our turns that shield RB/WR fallers.
  - **Rounds 6–9:** lock in the WR depth first; ~10 WRs went in picks 86–107.
  - **Never** use a turn pick on a D/ST or K before round 15.

## 4. 2027 rules (each labeled with confidence and evidence)
1. **No player who is already out before round 14.** That means anyone officially on the commissioner's exempt list, suspended, or on PUP, NFI or IR as of draft day. *Confidence: **high**. Evidence: our 2 confirmed already-out picks scored 0 points; the estimated cost is -67.1 against nearby picks. This is the rule that matters most.*
2. **Reach default: take the player at or near his ADP.** Taking a player more than about 12 spots early in rounds 1–6 (about 20 in rounds 7–12) needs a stated exception:
   - (a) a handcuff to our own starting RB;
   - (b) a scarcity miss, where ADP lags real news;
   - (c) an end-of-turn run, where our next pick is 22+ picks away and 3 or more players from the same tier are already gone.

   *Confidence: **medium** on the direction (within-position residuals: -5.8 vs +5.0, n=51/59, Spearman 0.36). The cutoffs are **opinion**, and the ADP used is post-draft, so the evidence is partly circular.*
3. **Rounds 1–4: best player available within the reach cap. Take a QB or TE only at or past his ADP.** *Confidence: **medium** (opinion that follows from Rule 2). ADP predicts RB and WR scoring best (Spearman 0.75 and 0.71), which argues for taking those positions at ADP, not for avoiding QB or TE.*
4. **QB and TE timing, a lean:** let other teams overpay. Lean toward a QB around rounds 7–10 and a TE around rounds 8–10, unless one falls to his ADP earlier. **Draft one QB only.** We stream a bye-week QB off traditional waivers. *Confidence: **low**. Single-year opinion, pending the Jan 5, 2027 rework.*
5. **D/ST and K in rounds 15–16 only.** *Confidence: **medium**. Early D/ST and K (n=6) scored only +3.1 more than late ones (n=14), and opponents stream them heavily.*
6. **Roster math (all 16 picks): 1 QB, 6 RB, 5 WR, 2 TE, 1 D/ST, 1 K = 16.**
   - **Leave the draft with at least 4 RBs who can play in Week 1.**
   - **Require the handcuff to our RB1** (one of the 6 RBs).
   - **RB injury-history screen for every RB in rounds 1–6:** flag significant prior injuries such as ACL tears, repeated soft-tissue injuries, or recent surgery. **Take at most one high-risk RB in our first four picks.**
   - If the board forces a tradeoff, fill in this order: 4th playable RB, then the RB1 handcuff, then the 5th WR, then a 2nd TE (only if our TE1 came in round 8 or later), then upside stashes. Injured players go only in rounds 14–16.

   *Confidence: **medium** (opinion shaped by 2026: 5 of our 16 picks are on IR, and we had only 3 playable RBs in Weeks 4–5).*
7. **Bye weeks: no more than 2 starters sharing a bye week.** This can't be applied until the **2027 NFL schedule** comes out (usually in May). *Confidence: **low** (opinion).*

**Scope note:** the draft wasn't the whole story in 2026. In-season management also lost a lot of points: bench calls, the Gordon/Henderson, Bateman/Meyers and Murray/Brissett lineup decisions, dropping Allgeier and Tucker, and dead roster spots (see `../opponents/ADVERSARIAL.md`, Sections 4–6). This playbook fixes the draft, not the whole season.

**Draft-day board:** `tier_board_TEMPLATE.csv` lists each player's ADP rank, position rank, ADP round, the earliest pick allowed without an exception (the reach cap), and columns for 2027 bye week, injury flag, RB injury-history risk and handcuff. It is filled with **2026 post-draft ADP as a template only** and **must be rebuilt from a 2027 pre-draft ADP snapshot.** Tiers are left blank to fill in.

**Jan 5, 2027 rework plan:**
- Recompute everything on 2026 full-season data instead of Weeks 1–4.
- Get a pre-draft ADP source.
- **Simulate a draft using these rules against plain best-available-by-ADP and against a VBD draft** (value over a replacement baseline of RB24/WR24 plus a flex share, for 12 teams). **Cut any rule that doesn't beat ADP.**
- Re-check the QB/TE timing lean, with survivor bias in mind.

## 5. Pre-draft checklist (within 24 hours of the draft)
- [ ] Re-pull ESPN ADP and Week 1 projections. Flag any player projected at 0 or listed as exempt, suspended, PUP, NFI or IR (Rule 1).
- [ ] Check the news for each target in rounds 1–10: injuries, holdouts, legal cases, and play-caller or coordinator changes.
- [ ] Mark the backup RB for each RB we plan to take in rounds 1–6 (Rule 2a, Rule 6), and run the RB injury-history screen.
- [ ] Save a pre-draft ADP snapshot and rebuild `tier_board_TEMPLATE.csv` from it.
- [ ] Map our turn pairs and the expected position drain from Section 3.
- [ ] Build the bye-week grid from the 2027 schedule.
- [ ] Confirm the draft order (ESPN sets it at draft start), roster slots, scoring, and keepers (0 this year).

## 6. Consultant critique and response
| Critique | Response |
|---|---|
| Only Rule 1 is clean | **Agreed.** Rule 1 is now labeled high-confidence and the rule that matters most (-67.1 points); everything else is medium or low. |
| Round rules rest on a Weeks 1–5 sample | **Agreed.** QB and TE timing is now a low-confidence lean, pending the Jan 5 full-season rework. |
| The reach analysis is circular by construction | **Partly agreed.** The comparison to the next 12 players drafted is shaped by the same ADP gaps. The hard caps are replaced with a default plus exceptions, and the cutoffs are no longer claimed as proven. |
| QB/TE round averages have survivor bias | **Agreed.** This is noted in Rule 4. |
| The 5/5 bench rule reacts to one bad week and conflicts with other rules | **Agreed.** It is replaced by a minimum of 4 playable RBs plus a priority order (Rule 6). |
| League behavior is described but not exploited | **Addressed in Section 3:** counts of RB/WR fallers (4 fell 12+ spots, worth +22.1), the cost of early D/ST/K (about 15–17 points per pick), and a turn-planning rule. |
| The post-mortem doesn't split already-out picks from reaches | **Addressed in Section 2:** already out -67.1, in-season injuries -95.4, reach-linked underperformance -57.6, other picks +11.2. |

## 7. Blitz review and response (REVIEW-blitz.md, written against version 63a1ddf0)
| Blitz item | Response |
|---|---|
| Draft time should be 8:00 PM CT | **Fixed.** `draftSettings.date` = Thu Sep 3, 2026, 8:00 PM CDT. |
| The already-out count contradicts ADVERSARIAL.md | **Fixed in both documents.** Using official status at draft time, only 2 picks were confirmed already out, both ours. The other 9 zero-projection picks were injured after the draft, unverified, or projection artifacts. |
| The $67 cost isn't reproducible | **Partly agree.** It can be reproduced from `../opponents/draft_players.csv` (`slot_expected`), but it depends on the baseline, so it is now labeled an estimate and the baseline is named. |
| Use a within-position residual reach test | **Adopted and reproduced exactly** (-5.8 vs +5.0, n=51/59, Spearman 0.36). The next-12-picks comparison is dropped. |
| Possible ADP leakage | **Confirmed.** The ADP is ESPN's current value pulled Oct 11, after the draft. It is flagged as partly circular. |
| Rule 3 wording; drop "Data:" from QB/TE timing | **Adopted.** |
| Close the roster math, drop QB2, add an RB injury screen and require the RB1 handcuff | **Adopted.** 1 QB / 6 RB / 5 WR / 2 TE / D/ST / K = 16. *Minor disagreement:* Blitz says Achane, Etienne and Brooks "all carried known risk." I can support that for Brooks (prior ACL history, not re-verified here) but have no draft-time evidence for Achane or Etienne, so the screen is a forward-looking rule, not a claim that those two were foreseeable. |
| The bye cap needs the 2027 schedule; in-season losses matter | **Adopted** (Rule 7 and the scope note). |
| Build a tier board | **Built:** `tier_board_TEMPLATE.csv`. |
| Simulate the rules against ADP and VBD; cut losers | **Added** to the Jan 5 rework plan. |
| Waivers "processed 11 AM CT" | **Disagree.** See the note below. |

**Waiver processing time:** ESPN's `mSettings` contains `waiverProcessHour: 11`. **That is not 11 AM CT.** Every processed claim in the transaction log carries a timezone-free epoch timestamp (`processDate`). All 51 processed claims fell between **2:05 and 2:51 AM CT**, 40 of them on Wednesday. That includes our own Week 3 and Week 4 claims, which processed Wed 2:51 AM and Wed 2:05 AM CT. No standard timezone turns hour 11 into roughly 2 AM CT (11 UTC is 6 AM CT, and 11 ET is 10 AM CT), so the field can't be read as a run time. **Plan around claims processing at about 2 AM CT.**
