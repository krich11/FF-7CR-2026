# RECON — Week 1 competitor strength
**as_of:** ESPN read `mRoster` projections (scoringPeriodId=1, statSourceId=1) + `mMatchupScore` schedule
**method:** Sum of ESPN projected fantasy points for each team’s 9 starters (QB/RB/RB/WR/WR/TE/FLEX/DST/K). League PPR.
**caveat:** ESPN still projects many QUESTIONABLE players at near-full; injury tags are narrative risk on top of the number — not official OUT clears (Wire owns ours).
**matchup:** Week 1 — **The Chosen Ones (TCO, teamId 9) @ Quantum Blitz (home)**.

## TLDR
- **Scariest W1:** **TCO** (123.3) — also our opponent. CDS/TE/BuB right behind (~122).
- **Exploitable:** **DDT** (88.0) and **LY** (89.3) — clear Soft tier (~30 pts below the pack).
- **Us:** QBZ starters sum **119.1** (6th of 12) — slight underdog vs TCO on pure proj.
- Mid pack (LL/PP/GGT/MBB/FR) bunched 116–120 — any can spike; FR RB duo is the punchiest of that group.

## Table (other 11)
| Tier | Team | WR# | ESPN starter Σ | One-line why |
|------|------|----:|---------------:|--------------|
| Elite | TCO The Chosen Ones | 9 | 123.3 | Hurts+Chase+Pickens ceiling; RB/TE/FLEX mostly Q — paper elite, fragile if tags bite |
| Elite | CDS Charlie Don't Surf | 12 | 123.2 | Puka+Jeanty+Walker stack; Price FLEX pops; Jeanty/Puka/Kraft Q — FA-hungry #12 still scary W1 |
| Elite | TE Texas Endgame | 3 | 122.2 | Lamar+JJ+Hampton core; Hall/Flowers/Kittle/Higgins all Q — elite if healthy |
| Elite | BuB Buck up Buttercup! | 6 | 121.9 | CMC+Saquon+Herbert hammer; CMC/Warren/Dicker Q — top-tier when CMC plays |
| Strong | FR Fantasy Rookie No More | 8 | 120.2 | Gibbs+Henry+Daniels smash; Nabers Q; Loop/Eagles middling — Strong with RB juice |
| Strong | MBB Mitch's Badass Bunch | 11 | 118.6 | Bijan+McBride+McMillan clean ACTIVE card; Pollard/Fannin softer — sturdy Strong |
| Strong | LL Louisiana Lightning | 2 | 116.6 | Burrow+Bowers+Cook/Brown balanced; Watson/Folk softer — Strong, fewer injury flags |
| Strong | PP Patton's Posse | 10 | 116.3 | JSN+Nico+AJB receiving; Monty/Kyren mid RB; Purdy fine — Strong, no Q tags |
| Strong | GGT The gg Team | 5 | 116.1 | Allen+ARSB carry; Skattebo/Lloyd RB committee; Metcalf/Tate Q — Strong but RB risk |
| Soft | LY Lazy Yorkie | 4 | 89.3 | Lamb alone can’t cover Wilson ~1.6 at RB1 + Henderson/Evans Q — Soft floor |
| Soft | DDT David's Daring Team | 7 | 88.0 | Taylor/Javonte fine but Tucker proj 0, Washington TE ~4.5, thin WRs — Soft overall |

## Our Week 1 opponent — TCO
| Slot | Player | ESPN proj | ESPN injury |
|------|--------|----------:|-------------|
| RB1 | D'Andre Swift | 12.3 | QUESTIONABLE |
| RB2 | Jeremiyah Love | 14.7 | QUESTIONABLE |
| WR1 | George Pickens | 14.7 | ACTIVE |
| WR2 | Ja'Marr Chase | 19.9 | QUESTIONABLE |
| TE | Sam LaPorta | 10.9 | QUESTIONABLE |
| DST | Rams D/ST | 6.2 | None |
| K | Harrison Mevis | 9.4 | ACTIVE |
| FLEX | Emeka Egbuka | 14.1 | QUESTIONABLE |
| QB | Jalen Hurts | 21.1 | ACTIVE |
| **Σ** | | **123.3** | |

## Notes
- Soft tier gap is structural (LY RB1 Wilson 1.6; DDT K Tucker 0.0 + TE Washington 4.5), not just noise.
- Elite cluster is tight (121.9–123.3); small lineup flips or a single OUT can reshuffle scariest.
- Full machine dump: `recon/weekly/w01/competitor-strength.json`

