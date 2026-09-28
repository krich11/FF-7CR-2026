# Sigma — Week 2 K-swap analysis (black & white)

**As of:** Sun Sep 20, 2026 ~11:00 AM CT  
**Roster K:** Eddy Pineiro (SF) — official QUESTIONABLE (illness); beat reports say he **will kick** vs MIA (3:25 PM CT). Ken assumption for this memo: **LIMITED DUTY** (unlikely FG ≥50).  
**Decision bubble:** 1:45 PM CT · if silent, Blitz auto-executes on merits before late locks (~3:00–3:05 CT).  
**Early slate LOCKED after 12:00 CT:** cannot add Reichard / McLaughlin / Smack / Elliott / etc.  
**Late FA pool still unlocked at 1:45 CT:** Gay, Ryland, Stevens, Shrader, Patterson.  
**League K scoring (ESPN distance, from league settings):** FG 0–39 = 3 · 40–49 = 4 · 50+ = 5 · XP = 1.  
**SPEC rule:** start rostered K unless a second rostered K is better by **≥ 3.0**.  
**Swap threshold (this memo):** **SWAP only if Net EV ≥ +1.0**; else **HOLD**. Strong SWAP if raw (streamer − Pineiro_limited) ≥ +3.0 (SPEC-aligned).

---

## 1) Pineiro projection — full duty vs limited (no FG ≥50)

### Sources (full duty)

| Source | Week 2 proj | Notes |
|--------|-------------|-------|
| ESPN (4for4 ESPN mirror) | **8.5** | XP 3.2 · FG 1.8 · as of Sun Sep 20, 11:55 AM EDT · Q-illness tag |
| ESPN API (local `projections.json`, Fri) | 9.92 | Pre-Sun refresh; illness play_prob was 0.55 then |
| FantasyPros consensus | 8.8 | Updated Sep 20 · FG 1.9 · XPT 3.1 |
| CBS Sports | 9.2 (flat) | Distance buckets below |
| Footballguys | 9.6 | Maurile stack |

**Full-duty mean (ESPN 8.5 + FP 8.8 + CBS 9.2 + FBG 9.6) / 4 = 9.03.**  
**Primary ESPN figure for decision math: 8.5.**

### Vegas / FG environment (SF)

| Input | Value | Source |
|-------|-------|--------|
| SF implied team total | **29.0** | Sharp Football Analysis consensus, odds ~Sat Sep 19 9:43 PM ET |
| SF spread / total (spot checks) | SF −10.5 to −13.5 · O/U ~44.5–46.5 | ESPN odds page · NBC Sports DK Thu line −13.5 / 44.5 |
| MIA implied | 15.5 | Sharp |
| Weather Levi’s | ~70–72°F · wind 5–9 W · rain ~1–2% | Fantasy Alarm Week 2 weather · NFLWeather |

High SF implied total supports a **top-tier full-duty** kicker environment (XP volume + FG chances). Weather is not a drag.

### Limited-duty model (Ken assumption: no FG ≥50)

CBS distance buckets (Pineiro W2): **20–29: 0.5 · 30–39: 0.6 · 40–49: 0.6 · 50+: 0.4 · XP: 2.9**  
Under ESPN distance scoring:

| Scenario | Calc | Pts |
|----------|------|-----|
| Full (CBS buckets × ESPN pts) | 0.5×3 + 0.6×3 + 0.6×4 + 0.4×5 + 2.9 | **10.6** |
| Limited (zero 50+ bucket, XP + short FG unchanged) | 0.5×3 + 0.6×3 + 0.6×4 + 0 + 2.9 | **8.6** |
| Haircut | 0.4 × 5 | **−2.0** |

**Pineiro_limited (decision figure) = ESPN full 8.5 − 2.0 haircut = 6.5.**  
(Mean-path alternate: 9.03 − 2.0 = 7.03 — still used only as sensitivity.)

**Status note (not invented):** Maiocco / NBC Bay Area — 49ers expect Pineiro to kick; tryouts of Joseph/Koo **not signed** (USA Today player update Sep 19; X RTs of Maiocco Sep 19–20). Official designation still Q. Limited-leg is **Ken’s assumption**, not a published restriction.

---

## 2) Late FA kickers — Week 2 proj + outdoor factors

All five confirmed **FA** in `recon/league_rosters.json` (no team owns them). Early-window streamers (Reichard, McLaughlin, Smack, Elliott) **excluded** (locked after 12:00 CT).

| Rank | Kicker | Team · game | CBS | FBG | Consensus base | Outdoor / venue | Weather adj | **Adj proj** | Team implied |
|------|--------|-------------|-----|-----|----------------|-----------------|-------------|--------------|--------------|
| 1 | **Drew Stevens** | WAS @ DAL 3:25 CT | 7.3 | 7.4 | 7.35 | AT&T **roof CLOSED** | 0 | **7.35** | WAS 23.25 (Sharp) |
| 2 | Spencer Shrader | IND @ KC 7:20 CT | 6.9 | 6.6 | 6.75 | Arrowhead outdoor | **−0.75** (rain ~59%, wind ~7 N — Fantasy Alarm) | **6.00** | IND 20.0 |
| 3 | Chad Ryland | ARI vs SEA 3:25 CT | 6.4 | 6.0 | 6.20 | State Farm **roof CLOSED** | 0 | **6.20** | ARI 18.5 |
| 4 | Matt Gay | LV @ LAC 3:05 CT | 5.6 | 6.0 | 5.80 | SoFi fixed canopy, ~80°F, wind 5–10, 0% rain | 0 | **5.80** | LV 18.5 |
| 5 | Riley Patterson | MIA @ SF 3:25 CT | 6.2 | 5.2 | 5.70 | Levi’s calm outdoor (same game as Pineiro) | 0 | **5.70** | MIA 15.5 |

**Best streamer = Drew Stevens (7.35).**  
RotoBaller ranks Stevens K22; Shrader K25; Gay K26; Ryland K30; Patterson K31 — same ordinal band.

---

## 3) Drop cost table (bench · ROS 0–10 · opponent-gift)

Label format: **Pos · Team · role**. Gift risk from rival roster counts in `recon/league_rosters.json` (thin: Lazy Yorkie WR=2; gg Team RB=2; Buck up Buttercup TE=1; several RB=3).

| Player | Label | ROS 0–10 (us) | Gift risk | Gift why | Drop penalty* |
|--------|-------|---------------|-----------|----------|---------------|
| Tyler Allgeier | RB · ARI · RB2 committee (Love active) | **3.0** | M | gg Team RB=2; Chosen Ones / FRNM / Lighting / DDT RB=3 | **1.1** |
| Jonathon Brooks | RB · CAR · RB2 behind Hubbard | **3.5** | M | same RB-thin pool | **1.2** |
| Rashid Shaheed | WR · NO · WR2/3 boom | **4.5** | M | Lazy Yorkie WR=2 | **1.4** |
| Jakobi Meyers | WR · JAX · WR2 | **5.5** | H | Lazy Yorkie WR=2 | **2.1** |
| Kyle Pitts Sr. | TE · ATL · TE1 | **6.5** | H | Buck up Buttercup TE=1 | **2.3** |
| Michael Pittman Jr. | WR · PIT · WR1 · **OUT** W2 (foot) | **7.5** | H | Lazy Yorkie WR=2; high ROS when healthy | **2.5** |
| Josh Jacobs | RB · GB · RB1 · **EXEMPT** | **9.0** | VH | elite return asset; do not gift | **3.3** |
| Zach Charbonnet (IR) | RB · SEA · PUP | n/a | — | IR slot — **not a legal claim drop** without activate | — |

\*Drop penalty = `(ROS/10)×2.0 + gift{L:0, M:0.5, H:1.0, VH:1.5}` — week-equivalent cost for Net EV.

**Preferred drop if forced to stream:** Tyler Allgeier (lowest ROS + moderate gift). **Never:** Jacobs · Pittman · Pitts.

---

## 4) Net EV = streamer − Pineiro_limited − drop_penalty

**Pineiro_limited = 6.5** · **Best streamer = Stevens 7.35**

| Claim | Drop | Streamer | − Limited | − Drop pen | **Net EV** | vs +1.0 threshold |
|-------|------|----------|-----------|------------|------------|-------------------|
| Stevens | Allgeier | 7.35 | −6.5 | −1.1 | **−0.25** | FAIL |
| Stevens | Brooks | 7.35 | −6.5 | −1.2 | **−0.35** | FAIL |
| Stevens | Shaheed | 7.35 | −6.5 | −1.4 | **−0.55** | FAIL |
| Stevens | Meyers | 7.35 | −6.5 | −2.1 | **−1.25** | FAIL |
| Stevens | Pitts | 7.35 | −6.5 | −2.3 | **−1.45** | FAIL |
| Stevens | Pittman | 7.35 | −6.5 | −2.5 | **−1.65** | FAIL |
| Stevens | Jacobs | 7.35 | −6.5 | −3.3 | **−2.45** | FAIL |
| Shrader (weather-adj 6.0) | Allgeier | 6.00 | −6.5 | −1.1 | **−1.60** | FAIL |
| Ryland 6.2 | Allgeier | 6.20 | −6.5 | −1.1 | **−1.40** | FAIL |
| Gay 5.8 | Allgeier | 5.80 | −6.5 | −1.1 | **−1.80** | FAIL |
| Patterson 5.7 | Allgeier | 5.70 | −6.5 | −1.1 | **−1.90** | FAIL |

**Raw edge (Stevens − Pineiro_limited) = +0.85** — well below SPEC’s **+3.0** second-K bar and below this memo’s **+1.0** Net EV bar.

### Sensitivity
- If limited haircut only −1.2 (flat 3 pts × 0.4 FG): Pineiro_limited = 7.3 → best Net EV ≈ **−1.05** (worse).  
- If use full-duty mean path limited 7.03: best Net EV ≈ **−0.78**.  
- If ignore drop penalty entirely (illegal for roster math): Stevens − 6.5 = **+0.85** — still **< +1.0**.  
- No path clears **+1.0 Net EV** with cited numbers.

---

## 5) Verdict

# **HOLD — Eddy Pineiro**

- Best late FA (Drew Stevens) does **not** clear Net EV ≥ **+1.0** after drop cost.  
- Raw streamer edge (+0.85) also fails SPEC-aligned **≥ 3.0** bar for replacing a rostered K.  
- SF implied **29.0** + calm Levi’s weather keep even **limited** Pineiro competitive with every late FA.  
- **No claim line.** Do not drop Allgeier/Brooks/etc. for a K stream at 1:45 CT.

### If SWAP had cleared (counterfactual only)
`claim Drew Stevens drop Tyler Allgeier`  
— **not recommended** under current numbers.

---

## Sources
1. ESPN K projections via 4for4 ESPN Week 2 table (Sun Sep 20, 2026 11:55 AM EDT)  
2. Local `projections.json` ESPN API Fri values  
3. FantasyPros K consensus projections (updated Sep 20, 2026)  
4. CBS Sports Week 2 K projections (distance buckets) — sportsfly.cbsistatic.com  
5. Footballguys Week 2 PK projections / rankings  
6. Sharp Football Analysis implied team totals (odds ~Sat Sep 19 9:43 PM ET)  
7. Fantasy Alarm NFL Week 2 weather report; NFLWeather (Levi’s)  
8. Matt Maiocco / NBC Sports Bay Area via USA Today + X — Pineiro expected to kick; Joseph/Koo not signed  
9. `recon/league_rosters.json` — K ownership + rival position counts  
10. `league.json` / SPEC — DST/K ≥3.0 second-copy rule; ESPN distance K scoring items  
11. RotoBaller Week 2 K rankings (weekend update)

---

**Sigma → Blitz:** HOLD Pineiro. No auto-claim. Path: `results/sigma/w2-k-swap.md`
