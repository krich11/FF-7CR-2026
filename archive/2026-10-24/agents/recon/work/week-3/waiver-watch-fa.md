# WAIVER WATCH — W3 FA hunt (1 open BE, QBZ n=16) · 2026-09-25 ~8:25 PM CT

**Ask (Blitz):** best **FREEAGENT** adds: immediately addable, not WAIVERS, usable W3 or strong W4+.
**Lane:** Recon intel only. No claim board, no ESPN writes, no availability.json.

## Data freshness / coverage
- Fresh read-only pull **2026-09-25 18:19:51 PT = 8:19 PM CT** (`recon/tools/refresh_dumps.py`; pre-refresh snapshot `snapshots/20260925-181950`).
- FA/WA pool + raw tx + pro schedule: `recon/tools/fa_pool.py` → `weekly/w03/raw/` (fa_pool.json, tx_raw_sp3.json, tx_raw_sp2.json, pro_sched.json, settings.json), same timestamp.
- **tx_n = 37** (SP3): 21 ROSTER, 7 FREEAGENT, 6 WAIVER exec, 1 WAIVER canceled, 1 WAIVER failed, 1 TRADE_DECLINE. **Rich, not lineup-only.** SP2 feed also pulled (n=49), so claimer history covers 09-15→09-25.
- Settings: WAIVERS_TRADITIONAL, waiverHours 24, process Mon/Wed–Sun hour 11, no FAAB. Dropped players go to WAIVERS for 24h, then FA.
- WO now (waiverRank): **BuB1 DDT2 LY3 GGT4 LL5 FR6 PP7 MBB8 TCO9 QBZ10 CDS11 TE12**.
- **Locked already:** ATL/GB played TNF (W3). Those FAs show WAIVERS/lineupLocked (Penix, Chris Brooks, Kaleb Johnson, Falcons D, Jonnu Smith, Hooper). Not W3-usable.

## Matchup sources (web, pulled 09-25 evening)
- DvP W3 table: nflfantasyedge.com W3 rankings. Its WR-generous list: **DAL 1st, TEN 2nd, IND 3rd, PIT 4th, CHI 5th**. RB-generous: ARI, NYJ, CAR, BUF, CIN. TE-generous: ARI, CIN, WAS. **Caveat:** the page says it's built on 2025-season points allowed. The 2026 sample is only 2 games.
- QB situations W3: NYG **Winston** (Dart out for season, giants.com); WSH **Mariota** (Daniels elbow, week-to-week, "multiple starts likely", PFR/ESPN 09-25); CHI **Keenum** likely (Caleb hamstring, Bagent concussion, CBS/Yahoo); SEA Darnold trending back; CLE **Watson** starts (Browns depth chart); LAC Herbert starts (Lance Q, backup only); ATL Penix back; MIN Kyler starts @TB.
- HOU: **Nico Collins OUT W3** (Texans report). Hutchinson 56 snaps/8 tgts W2, Boutte 51/5, Noel 41/4.
- BAL: Zay Flowers **Q** (limited Fri). Bateman 7-88-1 in W2 on 93% snaps.
- Byes: none W3/W4. W5 CAR, KC. W6 CIN, DET, MIA, **MIN (Kyler)**.

---

## 1) FA-race (FREEAGENT: first-come, no WO spend)

| Rk | Player | Pos/Team | own% | Status | W3 | W4 | Why | Likely rival grabbers |
|---|---|---|---|---|---|---|---|---|
| 1 | **Rashod Bateman** | WR BAL | 32.3 | ACTIVE | @DAL (WR-gen #1) | vs TEN (#2) | Best 2-week WR slate on the wire. Seas 21.8, ESPN proj 7.6 (low vs role). WR1 role if Flowers sits | **LY** (only Lamb + Evans Q), **PP** (Nico OUT/AJB IR, won Vele), **TE** (owns Flowers = handcuff; won Boston; Vele fail ×2), **CDS** (vacuum; Boston/Vele fails; 3 FA adds tonight), DDT (Douglas OUT; FA-added Douglas) |
| 2 | **Xavier Hutchinson** | WR HOU | 5.0 | ACTIVE | @IND (#3) | vs DAL (#1) | Nico OUT → WR1-by-snaps. Proj 9.6 = top FA WR | **PP** (owns Nico, WR hole), LY, CDS, TE, DDT. Boutte (12.2%, CDS drop 09-23) is the alternate/pivot |
| 3 | **Brenton Strange** | TE JAX | 18.4 | ACTIVE | vs NE | @CIN (CIN = TE sieve) | TE stash for Goedert gap. Seas 14.0, ROS proj 135.7 = best FA TE | **BuB** (1 TE: Warren), **LL** (Bowers IR; FA-added Schultz), **CDS** (TE churn Gesicki/Okonkwo/Gadsden). Alt: **Sadiq** NYJ (33.5%, seas 15.1, @DET/@CHI) |
| 4 | **Jameis Winston** | QB NYG | 3.5 | ACTIVE | vs TEN | vs ARI | QB2 behind Kyler. **Starter for the rest of the season** (Dart out for season). Two soft home spots. Covers Kyler's W6 bye | **FR** (Daniels OUT, Stroud only healthy QB; history Stroud/Kyler churn), **LL** (Burrow solo), **TE** (Caleb D; churned Brissett→Watson→Caleb), CDS |
| 5 | **Braelon Allen** | RB NYJ | 13.7 | ACTIVE | @DET (RB-gen #2) | @CHI (CHI on backup QB Keenum) | Run-funnel W3, backup-QB opponent W4. Proj 6.6. Hall handcuff | **TE** (owns Breece Hall; Bigsby claim canceled 09-22), **GGT** (2 RBs only; Mason/Mitchell churn), CDS (White/Corum RB churn), MBB (FA Singletary) |

**Next tier FA (by bucket):**
- **QB2 alts:** Mariota WSH (proj 15.3; vs SEA, vs IND; temp 1–4 wks, rushing floor). Rodgers PIT (vs CIN, 3rd-most QB pts; @CLE W4 tough). Geno NYJ (best ROS proj 234; @DET, @CHI). Cam Ward TEN. Brissett ARI.
- **WR:** Malachi Fields NYG (vs TEN #2, vs ARI; Winston throwing, 10.5%). Boutte HOU. Antonio Williams WSH (W4 vs IND #3). **Marvin Harrison Jr.** ARI is FA at 79.7% (TCO drop 09-23) but has 1 catch in 2 games and is a W3 must-sit @SF. Name-value vacuum bait: **CDS/LY** most likely to grab. Not a W3 use.
- **RB:** Tyjae Spears TEN (Q; @NYG vs backup-QB NYG = positive script; proj 9.7). Keaton Mitchell LAC (@BUF, RB-gen #4). Woody Marks HOU (52%; Montgomery cuff, **PP owns Montgomery**; W4 vs DAL). Tank Bigsby PHI (Q; @CHI vs Keenum).
- **DST:** Panthers D (46%, proj 7.1; @CLE vs Watson, sack/TO-prone; W4 vs DET bad). Titans D (@NYG vs Winston). **Colts D** (W4 @WSH vs Mariota). Vikings D (43.7%, seas 21; @TB, vs MIA). **Jets D** (W4 @CHI vs Keenum/Bagent). QBZ's Steelers D already draws **@CLE (Watson) in W4**, so DST is low priority for QBZ. Grabbers: **CDS** (DST fail spam ×3, then Bears FA, Giants WAIVER), FR/TE/LL (DST claimers).

## 2) WO-contested (reference only; WAIVERS, would burn QBZ #10)
| Player | Why WA | Note |
|---|---|---|
| Wan'Dale Robinson WR TEN (65.5%) | CDS dropped 09-25 20:07 CT | Clears ≥24h. Next process is Sun 11:00, after TEN kickoff → **not W3-usable**. WO heat from LY/PP/DDT ahead of us |
| Rachaad White RB WSH (67.3%) | CDS dropped 09-25 19:56 CT (3rd CDS churn of him) | Same timing. vs SEA / vs IND. GGT RB-thin |
| Deshaun Watson QB CLE | TE dropped 09-25 02:34 | CLE starter W3 vs CAR, W4 vs PIT |
| Chig Okonkwo TE WSH | CDS dropped tonight | OUT (hamstring) |
| Jayden Reed WR GB | FR dropped 09-23 | OUT; GB played |
| Penix / Chris Brooks / Kaleb Johnson / Falcons D | ATL-GB played TNF | Locked for W3 |

## 3) IR-stash (FA, OUT/IR; intentional only)
- Jonathon Brooks RB CAR (INJURED, 59.3%; QBZ's own 09-21 drop). Jordan Mason RB MIN (IR, 57.6%). Jonah Coleman RB DEN (OUT, 39%). Tank Dell WR HOU (IR, 29%). Pacheco RB DET (IR). Njoku TE LAC (INJ). Tyreek Hill (OUT, no team).
- League IR/OUT demand spikes: **PP** Nico OUT + AJB IR (WR). **LL** Bowers IR (Q) + Pierce OUT (TE/WR). **CDS** Tyson IR + Puka D (WR). **GGT** Stribling IR. **DDT** Douglas OUT (WR). **LY** Dowdle OUT + Evans Q (RB/WR). **FR** Daniels OUT (QB). **TE** Caleb D + Flowers Q + Warren Q.

## 4) Vacuum-behavior
- **CDS (WO11) is live right now.** FA adds tonight: Corum 19:41, Gadsden 19:56, Tre Tucker 20:07 CT (Tucker = QBZ's 09-23 drop). Also Downs + White FA 09-23. Failed claims: Vele (09-16), 49ers/Chiefs/Chargers D (09-16/17/18), Boston (09-23). Churns bodies on and off: White, Okonkwo, Boutte, Gesicki. **Biggest first-come race risk tonight and overnight.** They shop names (MHJ-type bait) and DSTs.
- **TE (WO12):** heavy filer. Vele ×2 fail, Stroud cancel, Bigsby cancel (09-22). Won Boston, Watson, Caleb, Chiefs D. FA: Wicks, Brissett. Hunts WR/QB/RB.
- **FR:** Stroud, Chargers D (won), Chiefs D (fail), Malik Washington FA, TRADE_DECLINE 09-22. QB-needy now.
- **PP:** Vele (won), Kaelon Black FA. Quiet since 09-16.
- **GGT:** A.Mitchell FA, Cousins FA re-add 09-23. **LL:** Schultz FA, 49ers D. **DDT:** Douglas FA. **MBB:** Singletary FA. **TCO:** Mumpfield WAIVER (dropped MHJ). **BuB / LY:** no non-lineup adds in 09-15→09-25 feed.

---

## PP (Patton's Posse, teamId 2, 1–1, WO7): W3 opponent card
- **Holes:** Nico Collins **OUT W3** (now on BE, corrected from W2's OUT-in-slot). A.J. Brown **IR**. Healthy WRs: JSN + Vele (starting), Godwin + Sutton (BE). Ceiling is thin behind JSN. Only 1 DST (Ravens @DAL/vs TEN) and 1 K.
- **Depth:** RB glut (Montgomery, Stevenson, Kyren FLEX, Black, Monangai). TE Kelce + Hockenson covers Kelce's W5 bye (KC). QB Purdy + Shough (Shough is a hot waiver-list name).
- **Roster 17/17 with IR:** any add needs a drop. Easy cut candidates: Black or Monangai.
- **Chase odds:** **High on HOU WRs (Hutchinson/Boutte)**, since they own Nico and the WR hole is theirs. **Medium on Bateman.** Marks is a Montgomery cuff but low priority. Low on QB/TE/DST.

## Caveats
- FA status = FREEAGENT at 8:19 PM CT. CDS is actively adding. Re-check right before any add.
- ATL/GB (TNF) players are locked for W3.
- Bateman's value depends on Flowers (Q). Hutchinson depends on Nico staying OUT past W3. Spears and Bigsby are Q.
- DvP tables lean on 2025 baselines; the 2026 sample is 2 games.
- Goedert shows **DOUBTFUL** on ESPN (Blitz says OUT for weeks). Wire owns our tag.
