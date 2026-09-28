# Sigma — scheduled routines (all America/Chicago)

## Weekly score + packet to Blitz
Schedule: Tuesdays 7:13 AM CT (`13 7 * * 2`). It runs Tuesday because nflverse snap data posts overnight after Monday's game.

What it does:
1. Refresh nflverse weekly stats and snap counts into `results/sigma/snaps/`, then form/usage/sources/shadow edges and the deep scorecard. Injury exits are tagged as not-form.
2. Usage table (snaps, targets, carry share, target share; routes UNKNOWN unless there's a real source) for the positions in play.
3. Three waiver claim boards ranked by projected points: Achane on IR / not on IR / Achane on IR and Etienne out. Each board has a separate availability column (from Recon's reset order and RB-need tags, which doesn't re-rank) and the point gap between each claim and the next, so the ticket can be cut at the right place. Protected from drops: Meyers, Brissett, Steelers D/ST.
4. Week 4 start/sit by highest projected average points. Playoffs are seeded by total points, so the opponent only breaks near-ties. Also NFL_SIDE, WEEK TYPE (context), FLEX EV, and HOLD/KILL with the Week 11 byes.
5. SIGMA REC packet to Blitz by late morning. Never messages Ken directly, never writes to ESPN.

## Tue AAR adversarial hotwash
Schedule: Tuesdays 9:02 AM CT (`2 9 * * 2`).

Sigma-lane after-action review. Findings go to `results/sigma/aar/`. Escalates to Blitz only if a finding changes a card, a source, or a gate. A durable rule becomes a proposed SIGMA.md patch to Blitz, never a silent self-rewrite.
