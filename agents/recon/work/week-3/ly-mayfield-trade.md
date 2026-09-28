# LY Mayfield trade read + QB1 upgrade scan — 2026-09-25 ~8:50 PM CT
Recon intel only. No ESPN writes, no offers sent.

## Freshness / tx
- Re-pull **18:47:31 PT = 8:47 PM CT** (snapshot `snapshots/20260925-184730`). **tx_n = 39** (SP3, +2 vs 8:27).
- **The +2 are QBZ's own FA moves at 8:35 PM CT:** ADD **Rashod Bateman**, ADD **Jacoby Brissett**, DROP Zach Charbonnet. QBZ is now 17/17 (Dart IR).
  → **Bateman is already ours**, so there's no "add first" step. He's still pure add-and-flip value: zero acquisition cost beyond the Charbonnet slot.
  → Brissett is now QBZ's QB2 (ARI, bye 14, ESPN ROS ≈229 on the earlier pull).
- Full history pulled: mTransactions2 SP0–SP3 (`raw/tx_raw_sp{0..3}.json`). 192 DRAFT, 73 ROSTER, 27 WAIVER, 27 FREEAGENT, 2 FUTURE_ROSTER, **1 TRADE_DECLINE** (dedup).
- ROS = ESPN season projection (statSource 1, SP0), pulled 8:47 PM. Mixed-split caveat: absolute numbers differ slightly from the 8:27 pull, but they're internally consistent in this file.

## 1) LY (Lazy Yorkie, teamId 7, 1–1, WO3)
### Activity — the name fits
- **Zero adds, drops, claims, or trades all season.** The current 16 = the **exact 16 drafted** 09-03. (Correction: the 09-15 rolling note's "LY dropped Darnold" is **not supported** by the feed or the draft list.)
- Lineup moves only: 09-09 (×4), 09-15 (×3), 09-17 (×2). **No LY lineup activity in SP3 at all.**
- **Current lineup holes (8:47 PM):** **Dowdle OUT in FLEX** (PIT, toe). Evans **Q** in WR2. Only **2 WRs rostered** (Lamb, Evans). If Evans sits, their WR2/FLEX options are RB/TE bench (Harvey, Perine, Barner, Otton).
- League trade history: **no executed trades**. One TRADE_DECLINE by **FR** 09-22 4:53 PM CT (the proposer isn't visible in the feed). LY has never proposed, accepted, or declined anything.
- **Read:** LY is a low-engagement owner. The biggest risk is **no response** (offer expires), not rejection. A deal has to be self-evidently good for them and fix a visible hole.

### LY roster / needs
| Pos | Players (NFL, bye) | Need |
|---|---|---|
| QB | Goff (DET b6) · **Baker (TB b10)** | Baker is Goff's **W6 bye cover**. After a trade, W6 is a hole for them (they'd need to add a QB; low-effort owner may not) |
| RB | E.Wilson (SEA b11), Henderson (NE b11), Dowdle **OUT** (PIT b9), Harvey (DEN b10), Perine (CIN b6) | Deep-ish; **W11 both starters on bye** |
| WR | Lamb (DAL b14), Evans **Q** (SF b8) | **Acute. Only 2 WRs** |
| TE | Andrews (BAL b13), Barner, Otton | Surplus |
| DST/K | Bucs + Cowboys D (both bad W3), Bass + Aubrey | Surplus |

### Mayfield value
- **own 49.9%**, ESPN W3 proj 15.6, **ROS 248** (vs Kyler 278, Brissett ~229). Seas 23.8 through 2.
- W3 **v MIN** (tough: TB on the "avoid QB" list v MIN). W4 **v GB**. Bye W10.
- For QBZ he's a **QB2 only** (−30 ROS vs Kyler). Upgrade over the just-added Brissett is roughly **+20 ROS pts**.

### Accept read
| Offer | LY view | Accept odds (if they respond) |
|---|---|---|
| **Bateman 1-for-1** | Fills the WR hole (WR2/FLEX while Evans is Q, Dowdle OUT). Bateman own 32%, @DAL/v TEN is a great 2-week slate. Costs QBZ ~nothing (FA add tonight) | **Med-High.** Value is close to even for a WR-starved team |
| **Allgeier 1-for-1** | RB they don't need much (Dowdle OUT, but 4 other RBs). Allgeier own 33%, ROS 119 | **Low-Med**; underpay vs Baker's positional value to them |
| **Allgeier + Bateman** | Fixes FLEX and WR2 at once | **High**, but that's an overpay for a QB2 |
| **Meyers 1-for-1** | Real WR2 (own 70.5%, ROS 142). ESPN rank 111 vs Baker 174 | **High.** Slight overpay by ESPN ranks |

**Recommended ladder** (cheapest first; each rung only if the previous one gets no reply or is declined):
1. **Bateman for Baker.** Flip the free add while his @DAL/v TEN narrative is hot, before Sunday (value drops if Flowers returns).
2. **Bateman + Pittman (Q) or Allgeier for Baker.** Only if LY counters.
3. **Meyers 1-for-1 as the ceiling.** Don't add sweeteners on top of Meyers.
- Timing: send it early Saturday so a passive owner has 24h+ before Sunday lock. Lineup-driven owners notice when a lineup hole shows up (Dowdle OUT in FLEX). They may not log in at all.
- Sanity check for Blitz: with Brissett now rostered, Baker is only a ~+20 ROS upgrade at QB2. That's worth Bateman; it's arguably **not** worth Meyers.

## 2) QB1 upgrade scan vs Kyler (MIN, ROS **278**, bye W6; W3 @TB, W4 v MIA)
| Rk | Team | QB | ROS (Δ vs Kyler) | W3 / W4 | Bye | Team need | Likely price | Plausibility | Role for QBZ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | DDT (0–2) | **Drake Maye** (BE, own 98.7) | **287 (+9)** | @JAX / @BUF | 11 | WR (Douglas OUT); 3 QBs | Meyers + Allgeier, maybe + Bateman | **Low-Med.** 98.7% name; DDT may value him as a Stafford successor | **Only real upgrade.** Starts over Kyler (marginal) |
| 2 | TCO (0–2) | **Patrick Mahomes** (BE) | 274 (−4) | @MIA / @LV | **5** | Thin RB (3), 0–2 desperate; QB surplus ×2 | Meyers + Allgeier | **Med.** They bench him | ≈ par / coin-flip start. Premium QB2; covers Kyler W6 |
| 3 | MBB (2–0) | Dak Prescott (BE) | 268 (−10) | v BAL / @HOU | 14 | None (deep) | Meyers + Allgeier | **Low.** Contender, no need | QB2 |
| 4 | DDT | Matthew Stafford (starter) | 265 (−13) | @DEN / @PHI | 11 | as above | Meyers (they'd then start Maye) | **Med** | QB2 |
| 5 | MBB | Trevor Lawrence (starter) | 266 (−12) | v NE / @CIN | 7 | — | n/a | **Very low** (their starter) | QB2 |
| 6 | LY | Baker Mayfield | 248 (−30) | v MIN / v GB | 10 | WR | Bateman → Meyers | **Med** (non-response risk) | QB2 |
| 7 | TCO | Bryce Young (BE) | 254 (−24) | @CLE / v DET | **5** | RB | Allgeier (+Bateman) | **Med** | QB2 |
| 8 | DDT | Daniel Jones (BE) | 221 (−57) | v HOU / @WSH | 13 | WR | Allgeier or Bateman | **High** | QB2 ≈ Brissett (lateral) |
| 9 | GGT | Malik Willis (BE) | 221 (−57) | v KC / @MIN | **6 (same as Kyler: useless for bye cover)** | RB (only 2) | Allgeier | **High** | Lateral to Brissett |
| — | GGT | Kirk Cousins (BE) | 54 | @NO / v KC | 13 | RB | — | — | Not a starter. Skip |

**Bottom line:** Kyler's ESPN ROS (278) is **top-of-market** for anything gettable at Meyers/Allgeier prices. **Only Maye starts over Kyler** on projection, and he's the hardest ask. Mahomes is a luxury QB2 at par. Everything else (Dak, Stafford, Baker, Young, Jones, Willis) is **QB2-only**. Dak and Stafford are the best QB2 quality, but at a Meyers-level price. With Brissett now rostered, the cheapest real QB2 upgrades are **Baker for Bateman** or **Stafford for Meyers** (if DDT wants to promote Maye).

## Caveats
- ESPN ROS projections only; Kyler's seas −0.38 reflects the W1 concussion exit (cleared, starts W3).
- The TRADE_DECLINE proposer is hidden by the feed; don't read it as LY/QBZ.
- LY hasn't touched anything since 09-17. Offers may simply sit.
- Bateman/Flowers: if Flowers (Q) plays W3, Bateman's flip value drops after Sunday.
- QBZ roster is **17/17 full** after the 8:35 moves. Any 2-for-1 frees a slot; any 1-for-2 needs a drop.
