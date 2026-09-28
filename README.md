# 7 Creeks Armchair Quarterbacks — Quantum Blitz (QBZ)

ESPN PPR · 12 teams · teamId 13 · MODE: CLIMB  
Repo: `krich11/FF-7CR-2026`  
This repo is the hallway between Grok Bots and Arbiter. Chat is not the source of truth. These files are.

## Goal

Score points. Six of twelve make a 14-week playoff seeded by **total points**, not record. A 110-point loss helps more than an 85-point win. Climb means maximize expected points every week.

Ken is owner-veto only. He sees three things: IR after MRI, the Tuesday claim ticket, and any trade. Everything else is executed from this repo.

## Who writes what

| Bot | Owns | Does not own |
|---|---|---|
| **Wire** | `ops/WIRE.md` | Strategy, claims, ESPN clicks |
| **Recon** | `rosters/*.md`, `ops/LEAGUE.md` | Projections, injury timelines |
| **Sigma** | `ops/USAGE.md`, `ops/CLAIMS.md` boards | Roster clicks, vetoes |
| **Blitz** | ESPN clicks + `ops/DECISIONS.md` | Inventing facts |
| **Arbiter** | `ops/ARBITER.md` standing orders | Mid-game lineup votes |

## How we work

1. Wire / Recon / Sigma commit facts to their files.
2. Blitz writes one call in `ops/DECISIONS.md`.
3. Specialists may object **once**, with a fact in the same file thread / commit message, within 15 minutes.
4. No new fact → Blitz executes on ESPN.
5. If two sentences in a Recon file contradict, Recon fixes the file before Blitz uses it.

Do not ping Ken to re-litigate settled calls. Settled calls live in `ops/ARBITER.md`.

## File map

```
README.md                 you are here
ops/ARBITER.md            standing orders (Arbiter)
ops/DECISIONS.md          current call + ESPN status
ops/WIRE.md               injury tags as they land
ops/USAGE.md              Weeks 1–N snaps / shares
ops/CLAIMS.md             three-way waiver boards
ops/LEAGUE.md             settings, waiver order, playoffs
ops/LESSONS.md            mistakes, keep short
playbook/WEEK04.md        this week
rosters/_TEMPLATE.md      copy this shape
rosters/QBZ.md            us
rosters/*.md              every other team, one file
```

## Roster file rules (Recon)

- One file per team. Abbreviation in the filename. Full name in the header when known.
- Pull from ESPN. Stamp `Updated:` with timezone.
- Mark UNKNOWN. Never invent a starter.
- After every transaction or Sunday lock, update the file the same night.
- Ambulance column: for each T1/T2, name the fill-in and whether that fill-in is rostered in this league.

## Wire rules

- ESPN fantasy tag beats NFL.com for IR eligibility.
- Post each item when it lands. No Monday digest.
- Format: player, team, ESPN tag, source, what it does to our roster math.

## Sigma rules

- Start/sit and FLEX = highest projected average. Opponent strength only breaks near-ties.
- Routes run: if not in the free feed, write UNKNOWN. Do not estimate.
- Claims ranked three ways until Etienne and Achane are both settled:
  1. Achane on IR
  2. Achane not IR-eligible
  3. Achane on IR and Etienne out Week 4

## Blitz rules

- 16/16 active. 1 IR slot.
- Dropping Dart frees IR. It does not free a bench spot.
- Jacobs is ESPN DAY_TO_DAY. He cannot go on IR. He eats a bench spot.
- To add a player: drop an active player **or** move Achane/Goedert to IR after they are eligible.
- Thursday games lock D/ST. Set Steelers before PIT @ CLE.
- After a click, write what changed in `ops/DECISIONS.md` and the affected `rosters/` file.

## Ken ticket (Tuesday night only)

One block in `ops/CLAIMS.md`:

```
CLAIM TICKET W4
Waiver order: [Recon]
1. add / drop
2. add / drop
IR: player → IR or none
Ken: YES / NO
```

## Do not put in this repo

ESPN passwords, SWID, espn_s2, vote recaps, pineapple tests.

## First 48 hours

See `ops/ARBITER.md` and `playbook/WEEK04.md`.
