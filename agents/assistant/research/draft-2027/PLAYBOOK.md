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
- **Reaching hasn't paid off (2026, rounds 1–10):**
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

## 2. 2026 QBZ post-mortem (summary; full detail in `../opponents/ADVERSARIAL.md`)
- **Picking 12th:** the turn forces back-to-back picks with 22 picks in between.
- **Reaches:** we averaged 30 picks ahead of ADP in rounds 1–10, the 3rd-biggest reach in the league. Achane (ADP 45) went at 12 and Pitts (ADP 104) at 60.
- **Picks already out at draft time:** Jacobs (exempt list since Aug 30) in round 8 and Charbonnet (on PUP) in round 15.
- **Scoring:** our rounds 1–8 picks scored **168 points fewer** than the next 12 players drafted after each pick. Our drafted players also scored the lowest share of their projections in the league (79%).

## 3. 2027 rules
1. **No player who is already out in round 1–10.** If a player is on the commissioner's exempt list, suspended, on PUP, NFI or IR, or has an ESPN Week 1 projection of 0, he can only be taken in rounds 14–16 and only as a stash. *(Data: our 2 such picks cost about 67 points; 11 were taken league-wide.)*
2. **Reach cap: no more than 12 picks ahead of ADP in rounds 1–6, or 20 in rounds 7–12.** The only exception is a handcuff to our own starting RB. *(Data: reaches of 15+ averaged -9.3; picks near ADP averaged +11.2.)*
3. **Rounds 1–4: RB and WR only, unless an elite QB falls to his ADP.** *(Data: ADP predicts RB and WR scoring best, at 0.75 and 0.71.)*
4. **QB: let the league overpay.** About 10 QBs go by the end of round 5. Target a QB in rounds 7–10, plus a second QB in rounds 11–14 to cover bye weeks. *(Data: round 7–9 QBs averaged 70.0 points versus 51.7 for rounds 4–6. Opinion: one season of data.)*
5. **TE:** take a TE in round 3 only if he's at or past ADP. Otherwise wait until rounds 8–10 and carry no more than 2 TEs. *(Data: round 4–6 TEs averaged 36.6 points versus 46.9 for rounds 7–9. We carried 3 TEs this year while short on RBs.)*
6. **D/ST and K in the last two rounds only (rounds 15–16).** This league takes them as early as round 4; let it. We stream both off waivers anyway. *(Opinion, backed by how often teams stream them: 20 D/ST adds by opponents this year.)*
7. **Bench construction: leave the draft with at least 5 healthy RBs and 5 WRs,** with one RB as the handcuff to our RB1 if he's available by round 11. *(Data: in Weeks 4–5 we had only 3 RBs who could actually play.)*
8. **Bye weeks:** no more than 2 starters sharing a bye week. *(Opinion.)*

**Notes by draft slot (opinion):**
- **Picks 1–3:** take the top RB or WR at ADP, then the best player at the other position at the turn.
- **Picks 4–9:** balanced. Expect the QB run in round 2 and don't join it.
- **Picks 10–12 (the turn, like this year):** take two RB/WR at their ADP (don't reach for a third choice). Plan the 22-pick gap so the round 3–4 pair is the next tier of RB/WR. Our late-round QB will come from the turn picks in rounds 7–10.

## 4. Pre-draft checklist (within 24 hours of the draft)
- [ ] Re-pull ESPN ADP and Week 1 projections. Flag any player projected at 0 or listed as exempt, suspended, PUP, NFI or IR.
- [ ] Check the news for each target in rounds 1–10: injuries, holdouts, legal cases, and play-caller or coordinator changes. Changes like Payton's play-calling this season hit RB usage.
- [ ] Mark the backup RB for every RB we plan to take in rounds 1–6.
- [ ] Build our bye-week grid and set the 2-starter cap.
- [ ] Confirm the draft order (ESPN sets it at draft start), roster slots, scoring, and keepers (0 this year).
- [ ] Have the reach cap from rule 2 visible on screen during the draft.
