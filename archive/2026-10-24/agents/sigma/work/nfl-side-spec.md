# NFL_SIDE feed spec (Ken, 2026-09-25 10:22 PM CT) — Sigma packets, our card only
Status: LIVE in Sigma packets from Week 4 (Tue 2026-09-29). SIGMA.md patch proposed to Blitz; Blitz writes the handbook.
Gates: our card only. No Ken MODE talk. No ESPN writes. No fantasy-opponent scouting (Recon). No availability ownership (Wire).

## Required on any CARD DIFF / REC line that changes a slot
- DVP: this NFL defense vs this position, last 3 games + season. Numbers, not adjectives.
  Source: computed from nflverse weekly player stats (PPR points allowed to the position, grouped by opponent_team). Cite N games. Early-season small sample = label it.
- Implied total / script: implied team total = total/2 - spread/2 from nflverse schedules (spread_line, total_line) or another named sportsbook source. Pass/run lean only from a number (implied total, spread, pass-rate). No number = UNKNOWN.
- OL / edge: starting LT/RT or primary edge rusher OUT/Doubtful, with effect on QB pressure or RB explosives. Source = Wire or official injury report.
  NONE only when a source confirms no such absence. Source silent = UNKNOWN (never write NONE from silence).
- WEEK TYPE (floor / toss-up / swing) must cite the matchup (DVP, implied totals, Recon's opponent script), not only our residual.

## Vacated work
Only when Wire named the replacement. Never invent target share for a committee; committee = "split, no share assigned."

## Same-game stack
If two QBZ names share an NFL game (QB+WR same team = positive correlation; our DST vs our offensive player = hedge; opposing skill players = shootout correlation), one line: helps or hedges.

## Missing personnel
Wire silent on opponent personnel = UNKNOWN. Still rank. Do not stall. Do not fabricate safeties or linemen.

## NFL_SIDE line for Blitz (one per changed slot, plus stack line)
NFL_SIDE: {opp unit} | missing: {from Wire or NONE/UNKNOWN} | tree: {from Wire or N/A} | script: {pass/run/UNKNOWN} | correlated: {list or NONE}
