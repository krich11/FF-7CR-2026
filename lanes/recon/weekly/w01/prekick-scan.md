# RECON — Week 1 pre-kick scan
**as_of dumps:** 2026-09-05 ~14:19 PT (`league_rosters` / `league_index` / `transactions_recent`)  
**scope:** light watch list only (injury tags / post-draft FA / handcuff competition). Full opponent cards deferred.  
**source:** ESPN read dumps under `recon/` — no invented statuses.

## TLDR
- Only **1 executed WAIVER** post-draft: **CDS** (waiver #12) **added Jaguars D/ST**, dropped playerId `5083315` (now FA / not on any roster).
- Other non-DRAFT txs are **LINEUP** moves only (DDT, QBZ, TE) — not FA competition.
- ESPN `QUESTIONABLE` tags are **very dense** on opponent skill starters (preseason noise likely). Material flags worth tracking (not graded): TE’s Breece/Flowers/Kittle/Higgins Q; BuB CMC Q; FR Nabers Q; CDS Jeanty/Puka/Kraft Q; TCO Chase + Swift + LaPorta + Love + Egbuka Q; LY Wilson/Henderson/Evans Q.
- Handcuff / same-proTeam pressure on **our** depth: **Charbonnet OUT** on our bench; **CDS** starts **Jadarian Price** at FLEX (same ESPN `proTeamId` 26). **GGT** holds **MarShawn Lloyd** (same team id as Jacobs). **TE** holds **Chuba Hubbard** (same team id as Brooks).
- Waiver order unchanged: **QBZ #1** … **CDS #12**.

## Waiver order map
| Rank | Abbr | Team |
|-----:|------|------|
| 1 | QBZ | Quantum Blitz (us) |
| 2 | LL | Louisiana Lightning |
| 3 | TE | Texas Endgame |
| 4 | LY | Lazy Yorkie |
| 5 | GGT | The gg Team |
| 6 | BuB | Buck up Buttercup! |
| 7 | DDT | David's Daring Team |
| 8 | FR | Fantasy Rookie No More |
| 9 | TCO | The Chosen Ones |
| 10 | PP | Patton's Posse |
| 11 | MBB | Mitch's Badass Bunch |
| 12 | CDS | Charlie Don't Surf |

## (b) Post-draft FA / waiver / roster moves
From `transactions_recent.json` (file reports `n: 210`, dump holds **50** rows — mostly DRAFT):

| Type | Team | Notes |
|------|------|-------|
| WAIVER | CDS (teamId 4) | ADD Jaguars D/ST (`playerId` -16030); DROP `5083315` (not on any current roster) |
| ROSTER/LINEUP | DDT | Keenan Allen lineup move |
| ROSTER/LINEUP | QBZ | Pittman + Goedert lineup move |
| ROSTER/LINEUP | TE | Higgins + Jaylen Warren lineup move |

**No other ADD/DROP competition in this dump.** Re-pull txs if Blitz wants a fuller 210-row window.

## (a) Opponent skill-starter non-ACTIVE tags
DST `UNKNOWN` / null excluded. **Caveat:** Week-1 eve ESPN Q volume is high — treat as ESPN field values, not official OUT confirmation.

| Team | WR# | Slot | Player | ESPN status |
|------|----:|------|--------|-------------|
| TE | 3 | RB1 | Breece Hall | QUESTIONABLE |
| TE | 3 | WR2 | Zay Flowers | QUESTIONABLE |
| TE | 3 | TE | George Kittle | QUESTIONABLE |
| TE | 3 | FLEX | Tee Higgins | QUESTIONABLE |
| FR | 8 | WR2 | Malik Nabers | QUESTIONABLE |
| CDS | 12 | RB1 | Ashton Jeanty | QUESTIONABLE |
| CDS | 12 | WR2 | Puka Nacua | QUESTIONABLE |
| CDS | 12 | TE | Tucker Kraft | QUESTIONABLE |
| BuB | 6 | RB1 | Christian McCaffrey | QUESTIONABLE |
| BuB | 6 | TE | Tyler Warren | QUESTIONABLE |
| LY | 4 | RB1 | Emanuel Wilson | QUESTIONABLE |
| LY | 4 | RB2 | TreVeyon Henderson | QUESTIONABLE |
| LY | 4 | WR2 | Mike Evans | QUESTIONABLE |
| GGT | 5 | WR2 | DK Metcalf | QUESTIONABLE |
| GGT | 5 | FLEX | Carnell Tate | QUESTIONABLE |
| TCO | 9 | RB1 | D'Andre Swift | QUESTIONABLE |
| TCO | 9 | RB2 | Jeremiyah Love | QUESTIONABLE |
| TCO | 9 | WR2 | Ja'Marr Chase | QUESTIONABLE |
| TCO | 9 | TE | Sam LaPorta | QUESTIONABLE |
| TCO | 9 | FLEX | Emeka Egbuka | QUESTIONABLE |

**Bench IR note:** CDS has **Jordyn Tyson** on IR.

## (c) Handcuff / same-proTeam watch vs our roster
Crosswalk is ESPN `proTeamId` only (no invented NFL labels).

| Our player | Our ESPN status | Same-proTeam held elsewhere (notable) |
|------------|-----------------|----------------------------------------|
| Zach Charbonnet | **OUT** (BE) | **CDS Jadarian Price (FLEX)**; LY Emanuel Wilson (RB starter, same id); MBB Seahawks D/ST |
| Josh Jacobs | DAY_TO_DAY (BE) | **GGT MarShawn Lloyd (RB)**; BuB Jordan Love / Packers D/ST; FR Jayden Reed; LL Christian Watson; DDT Matthew Golden; CDS Tucker Kraft |
| Jonathon Brooks | QUESTIONABLE (BE) | **TE Chuba Hubbard (BE, Q)**; TCO Bryce Young / Jalen Coker; LL Darren Waller; MBB Tetairoa McMillan |
| Travis Etienne Jr. | ACTIVE | MBB Alvin Kamara (BE, Q); FR Chris Olave; TE Juwan Johnson; PP Tyler Shough |
| De'Von Achane | ACTIVE | GGT Malik Willis only (QB) — **no RB cuff rostered league-wide in dump** |
| Drake London / Kyle Pitts Sr. | ACTIVE | MBB Bijan Robinson; BuB Brian Robinson Jr. |
| Garrett Wilson | ACTIVE | TE Breece Hall (starter, Q) |
| Jaxson Dart | ACTIVE | FR Malik Nabers (starter, Q); GGT Cam Skattebo |

## Deferred
- Full ×11 opponent cards (await projections / post–Week 1)
- Official injury override pass (Wire / status-resolve) — Recon does not invent clears
- Week 1 fantasy matchup card (need schedule opponent from Blitz or ESPN scoreboard pull)

## Paths
- This note: `recon/weekly/w01/prekick-scan.md`
- Raw: `recon/league_rosters.json`, `recon/league_index.json`, `recon/transactions_recent.json`
