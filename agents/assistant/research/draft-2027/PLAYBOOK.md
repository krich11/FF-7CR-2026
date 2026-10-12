# 2027 Draft Playbook: 7 Creeks Armchair Quarterbacks (ESPN PPR)
*Built Sun Oct 11, 2026, about 10 PM CT, from read-only ESPN data. 2026 points cover Weeks 1–4 (or 1–5 where labeled), so they're early-season samples. Anything marked **(opinion)** is judgment, not something the data proves.*

## What draft data exists
- **2026 (complete):** all 192 picks, a 12-team, 16-round snake draft held Thu Sep 3, 2026, about 9 PM CT, with 60 seconds per pick and no keepers (`keeperCount 0`). ESPN set the draft order at draft time (`orderType DRAFT_START`). **QBZ picked 12th**, at the turn, so we had picks 12/13, 36/37, 60/61 and so on. Every pick is in `draft_2026_full.csv` with its ESPN ADP, position, Week 1 projection, 2025 points, and Weeks 1–4 and 1–5 points.
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
- **Reaching hasn't paid off (2026, rounds 1–10). Caveat: this comparison is partly circular, because each pick is measured against the next 12 picks, which are partly defined by the same ADP gaps. Treat it as a direction, not proof of any cutoff:**
  - 58 picks taken **15 or more spots before ADP** averaged 35.6 points, **9.3 fewer** than the next 12 players drafted after them.
  - 53 picks within 15 spots of ADP averaged **+11.2** against the same comparison.
  - The 9 picks taken 15 or more spots *after* ADP averaged **+33.5**.
- **How well ADP predicted early scoring (Spearman correlation between ADP rank and Weeks 1–4 points):** RB 0.75, WR 0.71, TE 0.56, QB 0.50. ADP predicts RB and WR scoring well and QB and TE scoring only loosely.
- **QB and TE scoring by round (Weeks 1–4 average):**

  | Rounds | QB | TE |
  |---|---|---|
  | 1–3 | 73.6 | 58.7 |
  | 4–6 | 51.7 | 36.6 |
  | 7–9 | 70.0 | 46.9 |
  | 10–16 | 56.3 | 37.1 |

  Purdy (pick 95), Bryce Young (pick 190) and Shough (pick 146) are top-5 QB scorers so far. Small sample, but **QB is deep**.
- **Players drafted while already ruled out (Week 1 projection 0):** 11 picks across 7 teams, including QBZ with 2 (Jacobs and Charbonnet), DDT with 2, MBB with 2 and CDS with 2. Brock Bowers went in round 3 to LL. Appetite for injured players exists across the league; we're not the only ones.
- **Rookies:** taking "no 2025 stats" as a stand-in for rookies flags only 8 non-D/ST picks (GGT 3, CDS 2). That stand-in is weak, so **no conclusion**.

## 2. 2026 QBZ post-mortem: the shortfall split
Our 16 picks scored **208.9 points fewer** in Weeks 1–4 than players drafted at nearby picks (each pick compared with the average of the 6 picks before and after it; see `../opponents/ADVERSARIAL.md`). Each pick's gap is assigned to one bucket:

| Bucket | Points | Players |
|---|---|---|
| **Already out when drafted** | **-67.1** | Jacobs -39.4, Charbonnet -27.7 |
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
1. **No player who is already out before round 14.** That means anyone on the commissioner's exempt list, suspended, on PUP, NFI or IR, or with an ESPN Week 1 projection of 0. *Confidence: **high**. Evidence: our 2 such picks cost -67.1 points; 11 were drafted league-wide. This is the rule that matters most.*
2. **Reach default: take the player at or near his ADP. A pick more than about 12 spots early in rounds 1–6 (or about 20 in rounds 7–12) needs a stated exception:**
   - (a) a handcuff to our own starting RB;
   - (b) a scarcity miss, meaning ADP lags real news such as a role change or a confirmed starting job;
   - (c) an end-of-turn run: our next pick is 22+ away and 3 or more players from the same tier are already gone.

   *Confidence: **medium** on the direction. The cutoffs are judgment calls; the data does **not** prove them. Evidence: picks 15+ early averaged -9.3 against the next 12 drafted players; picks near ADP averaged +11.2 (partly circular).*
3. **Rounds 1–4: RB and WR first.** ADP predicted early scoring best for these positions (correlation 0.75 for RB and 0.71 for WR, against 0.50 for QB and 0.56 for TE), and RBs disappear fastest between our turns. *Confidence: **medium**.*
4. **Let other teams overpay for QB and TE.** Our lean is to take a QB in rounds 7–10 and a TE in rounds 8–10, unless a top TE falls to his ADP in round 3. *Confidence: **low**. This is single-year, round-average data with survivor bias (late-round winners like Purdy and Bryce Young look good in hindsight). Pending the full-season rework on **Jan 5, 2027**.*
5. **D/ST and K in rounds 15–16 only.** *Confidence: **medium**. Early D/ST/K gained only +3.1 points over late ones, at a cost of roughly 15–17 points per pick in the players passed up. Opponents also stream them heavily (20 D/ST adds).*
6. **Bench decision rule (replaces the old 5 RB / 5 WR rule):** leave the draft with **at least 4 RBs who can actually play in Week 1**. For the last 7 bench slots, use this priority order:
   1. A 4th playable RB, if we have fewer than 4.
   2. A handcuff to our RB1.
   3. A 4th WR.
   4. A backup QB, but only if our starting QB's bye week or injury risk isn't covered by waivers. QB depth is deep in this league.
   5. A 2nd TE, only if our TE1 is a round-8 or later pick.
   6. Upside stashes (injured players allowed only in rounds 14–16).

   Never carry 3 TEs or 3 QBs. *Confidence: **medium**. In Weeks 4–5 we had only 3 playable RBs and 3 TEs; the 4-RB minimum is a judgment call.*
7. **Bye weeks: no more than 2 starters sharing a bye week.** *Confidence: **low** (opinion).*

## 5. Pre-draft checklist (within 24 hours of the draft)
- [ ] Re-pull ESPN ADP and Week 1 projections. Flag any player projected at 0 or listed as exempt, suspended, PUP, NFI or IR (Rule 1).
- [ ] Check the news for each target in rounds 1–10: injuries, holdouts, legal cases, and play-caller or coordinator changes.
- [ ] Mark the backup RB for each RB we plan to take in rounds 1–6 (Rule 2a, Rule 6).
- [ ] Map our turn pairs and the expected position drain from Section 3.
- [ ] Build the bye-week grid.
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
