> **SUPERSEDED by 2026-09-25 Blitz law — Blitz writes, specialists propose.** (Law: BLITZ.md + WAR.md win on any conflict.)
>
> **Superseded per issue 5 (Oct 6 2026):** Sigma references in this file are superseded. Sigma is retired. Assistant owns projections and the usage baseline. The shadow-edge lane is retired.

# Waivers — Quantum Blitz

**Owner (claim board / ESPN):** Blitz  
**League WAIVER WATCH:** Recon → Blitz  
**League mode:** traditional / rolling priority (not FAAB)  
**Rule:** no ESPN claim, drop, trade, or IR move unless Ken types an explicit command below.


## Team split (Ken-approved 2026-09-05)
- **Recon** owns league **WAIVER WATCH** (competition intel) → briefs Blitz → files under `recon/`.
- **Blitz** owns the Quantum Blitz **claim board**, MUST-ACT, and ESPN writes after Ken’s typed command.
- **Sigma** may rank *our* add value if Blitz asks — never posts boards to Ken or files claims.
- **Wire** supplies injury context only — does not write the waiver board.

See `TEAM.md`.

## Ken commands (case-insensitive)

| Ken types | Blitz does |
|-----------|------------|
| `claim {add} drop {drop}` | File that one claim (**live**). If the last board was marked TEST, Blitz confirms first or waits for `for real`. |
| `claim {add} drop {drop} for real` | Force live claim even after a TEST board |
| `claim {add}` | Claim add only if roster has an open spot; else ask which drop |
| `drop {player}` | Drop only (rare; confirm once if it opens a hole before next claim) |
| `cancel claim {add}` | Cancel pending claim for that add if ESPN allows |
| `pass` / `pass waivers` | No claims this window; stand down |
| `hold waivers` | Freeze boards/claims until Ken says otherwise |
| `IR {player}` | Move eligible player to IR slot (frees a roster spot) |
| `activate {player}` | Move player off IR onto bench (may need a drop) |

Ambiguous names → Blitz asks once before any ESPN write.
When offering a command for Ken to copy, put it in a **separate message alone** (Ken 2026-09-09).  
Never invent a drop. Never claim “for” Ken from a board alone.

## IR / roster-spot alerts (Ken 2026-09-09)
Blitz must **proactively** flag when an IR-eligible stash (PUP/IR/OUT/EXEMPT) sits on bench while the IR slot is empty — especially before waiver windows — with a recommended IR + add. Ken should not hear this first from a league mate.

## Tight-spot contingencies
When a startable hole appears (sole QB OUT, etc.), follow `CONTINGENCY.md` — bubble waiver ladder + trade/FA eval **proactively** (Ken 2026-09-22).

## Can’t-miss / must-act

If Blitz rates a move **MUST** (league-winning stash, your starter’s replacement gone, top-priority WW with you at #1 and short window):

1. Lead the message with **`🚨 MUST-ACT`** (or **`CAN’T-MISS`**)
2. State **deadline** (next process time) + **your waiver rank**
3. One recommended claim line Ken can copy: `claim X drop Y`
4. Still **wait** for Ken’s typed command — never auto-submit

Priority tiers on boards: `MUST` > `STRONG` > `WATCH` > `PASS`

## Board template (post in this thread)

Every add **and** drop must show: **Pos · NFL team · depth/role** (e.g. `RB · ATL · RB2 behind Bijan`). Ken should never need to Google a name to know who it is.

```markdown
# Week {N} WAIVERS — Quantum Blitz

**Mode:** rolling priority · **Your rank:** #{r} · **Next process:** {day} ~{time} ET
**Wire:** {one-liner or n/a}

## MUST-ACT
- **ADD** {name} — {Pos} · {TEAM} · {depth}
- **DROP** {name} — {Pos} · {TEAM} · {depth}
- why ≤140 chars · deadline {when}
- copy-paste: `claim {add} drop {drop}`

## Board
| Pri | Tier | Add (pos · team · depth) | Drop (pos · team · depth) | Why |
|-----|------|--------------------------|---------------------------|-----|
| 1 | STRONG | … | … | … |

## Glance
- {name} — {Pos} · {TEAM} · {depth} — one line

## Standing down
Reply `pass` or type `claim X drop Y`. Nothing hits ESPN until you do.
```

## Cadence (America/Los_Angeles)

- **Tue ~10:00** — main board after Mon games / early week wire (before Tue lineup.set if useful)
- **Wed ~09:00** — refresh if injuries / rank changed / MUST appeared
- Midweek **interrupt** — MUST-ACT only (don’t spam full boards)

Optional: Blitz may write `waivers.json` for *our* board state; Recon writes competition notes under `recon/` — still no transactions without Ken’s claim command.

## ESPN

- Prefer API transaction type `WAIVER` only after typed claim (same cookie path as lineup API)
- After submit: re-read pending transactions; confirm to Ken
- On fail: `WAIVER CLAIM FAILED` alert — do not claim success
