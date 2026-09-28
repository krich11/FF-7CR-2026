# FUD — Fear, Uncertainty, Doubt

Competitive analysis of 7 Creeks Armchair Quarterbacks.

Playoffs are **6 of 12, seeded by total points, 14-week regular season, reseed each round**. Record is a vanity metric. FUD exists so the squad hunts PF leaders, waiver collisions, and trade holes instead of arguing about who is 3-0.

This folder is not a claim ticket and not a Ken vote. `ops/CLAIMS.md` (or Blitz's WAR/WAIVERS) is the ticket. FUD is the map underneath it.

## Who owns what

| Role | Writes | Does not |
|---|---|---|
| **Arbiter** | Posture, tiers, trade buttons, this README | ESPN clicks, invented scores |
| **Recon** | Roster blocks, waiver ranks, official W-L/PF after appliedTotals | Posture labels, QBZ add/drop recs |
| **Wire** | Injury tags that change a card (one line, sourced) | Rewriting the card |
| **Sigma** | Nothing in FUD | — |
| **Blitz** | Reads FUD before the Tuesday ticket and any trade | Silent posture edits |
| **Ken** | Veto on the ticket / trade only | Editing these files |

If two sentences disagree, fix the file. Do not paper over it in chat.

## How to use it this week

1. Open [BOARD.md](BOARD.md). Find the PF cut line and our rank.
2. Open this week's opponent card (Week 4 = [TE.md](TE.md)).
3. Open [WAIVER_THREATS.md](WAIVER_THREATS.md) before anyone files a claim.
4. Open [TRADE_MAP.md](TRADE_MAP.md) only if a live button still exists.
5. Do not start from a random team file.

## File map

| File | Job |
|---|---|
| [BOARD.md](BOARD.md) | PF table, W-L, waiver order, posture, tiers |
| [WAIVER_THREATS.md](WAIVER_THREATS.md) | Who is in front of us and whether they need the same name |
| [TRADE_MAP.md](TRADE_MAP.md) | Live buttons, dead buttons, walk-away prices |
| [QBZ.md](QBZ.md) | How the other 11 see us |
| [TE.md](TE.md) | Texas Endgame — Week 4 opponent |
| [PP.md](PP.md) | Patton's Posse |
| [FR.md](FR.md) | Fantasy Rookie No More |
| [CDS.md](CDS.md) | Charlie Don't Surf |
| [MBB.md](MBB.md) | Mitch's Badass Bunch |
| [LL.md](LL.md) | Louisiana Lightning |
| [TCO.md](TCO.md) | The Chosen Ones |
| [GGT.md](GGT.md) | The gg Team |
| [LY.md](LY.md) | Lazy Yorkie |
| [DDT.md](DDT.md) | David's Daring Team |
| [BuB.md](BuB.md) | Buck up Buttercup! |

One file per club. Abbreviation is the filename. Full ESPN name lives in the header.

## Card template

Keep this shape. Do not turn a card into a novel.

```md
# ABBR — Full ESPN name

teamId N · Waiver N · W-L · PF rank (Nth)

## Posture: LABEL

One paragraph. Record vs PF vs roster quality. Say if those three disagree.

## Starters

## Bench / IR

## Weakness

## Need / give
Need = hole that makes them claim or trade.
Give = surplus we might ask for.

## Waiver
Their pick and whether they collide with our board.

## Ambulance
T1/T2 → fill-in → rostered in this league? yes/no/UNKNOWN
```

## Posture labels (use these words only)

| Label | Means |
|---|---|
| CHALLENGING | PF and roster both threaten the field |
| SPIKING | Just printed a huge week or sits 1–2 in PF |
| STURDY | Safe seed / fat roster, not a weekly explosion |
| FRAGILE | Good pieces, one hole (usually RB or health) |
| FADING | PF in the mud; talent not converting |
| BLEEDING | Last in PF, process failure, or both |

A 3-0 team with a dead WR1 can be STURDY and FRAGILE at once. Put the record word first, the roster word in the paragraph.

## Sources

Facts come from, in order:

1. `lanes/recon/league_rosters.json`
2. `lanes/recon/league_index.json`
3. `data/standings.json` once it is current
4. Wire tags for injury lines

Sunday scores that ESPN has not applied yet are **unofficial**. Write that word on the BOARD until Recon's next appliedTotals pull. Never invent a starter, a claim, or "nobody wants that."

## Cadence

- **Sunday night:** unofficial W-N scores on BOARD. Opponent card for next week on top.
- **After appliedTotals:** Recon patches W-L, PF, waiver rank. Arbiter resets posture if the seed jumped a tier.
- **After any roster pull:** Recon patches the starter/bench block if it drifted.
- **T1 goes down:** Wire drops one sourced line; Arbiter updates Ambulance + WAIVER_THREATS the same night.
- **Wednesday AM after waivers:** mark who actually filed. That is how threats get proven.

## Hard no

- No QBZ add/drop list in these files.
- No passwords, cookies, ESPN IDs.
- No vote recaps.
- No guessing routes or usage. That is Sigma, elsewhere.
- Do not delete a card because a team is "irrelevant." LY and BuB are still waiver and trade pieces.

## Law this folder exists to enforce

Outscore the PF cut. Assume GGT files Gordon until Wednesday says otherwise. Talk to LL about Brissett. Do not shop London or Wilson. Do not reopen Mayfield.
