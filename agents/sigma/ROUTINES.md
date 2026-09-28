# Sigma — scheduled routines (all America/Chicago)

Repo `krich11/FF-7CR-2026` on `main` is the source of truth (per `FILESYSTEM.md`, effective 2026-09-27). Every run pulls `main` first and commits its outputs to `main` at the end. The live path in `FILESYSTEM.md` wins over any local copy.

Commits (Blitz rule, 2026-09-27): push straight to `main` with `QBZ_GITHUB_TOKEN` only (git over HTTPS or the contents API). Never fall back to `GITHUB_TOKEN`, which is a read-only token from another account. Pull or re-read `main` right before every write and retry if another commit lands first. Use a cloud agent only if the direct push fails, and report that failure in the War Room. Never print the token.

Sigma reads `data/roster.json`, `data/availability.json`, `data/recon/league_rosters.json` + `league_index.json`, `playbook/`, `playbook/CLAIMS.md` and `agents/sigma/CHARTER.md`.
Sigma writes packets to `agents/sigma/work/week-N-packet.md`, claim boards into `playbook/CLAIMS.md` (Sigma board sections only), and snaps, form, usage and AARs to `agents/sigma/work/`.

## Weekly score + packet to Blitz
Schedule: Tuesdays 7:13 AM CT (`13 7 * * 2`). It runs Tuesday because nflverse snap data posts overnight after Monday's game.

1. Pull `main`. Refresh nflverse weekly stats and snap counts, then form, usage, sources, shadow edges and deep scorecard stats into `agents/sigma/work/`. Injury exits are tagged as not-form.
2. Usage table (snaps, targets, carry share, target share; routes UNKNOWN unless there's a real source).
3. Three waiver claim boards ranked by projected points (A: Achane on IR; B: not on IR; C: Achane on IR and Etienne out). Each has a separate availability column (from Recon's reset order and RB-need tags, which doesn't re-rank), the point gap between each claim and the next, and the gain over the dropped player. Boards land in `playbook/CLAIMS.md`.
4. Start/sit by highest projected average points (playoffs are seeded by total points; the opponent only breaks near-ties), plus NFL_SIDE, WEEK TYPE, FLEX EV and HOLD/KILL.
5. Commit the packet to `agents/sigma/work/week-N-packet.md`, then tell Blitz the path (not a paste) by late morning. Never messages Ken directly, never writes to ESPN.

## Tue AAR adversarial hotwash
Schedule: Tuesdays 9:02 AM CT (`2 9 * * 2`).

Pull `main`. Sigma-lane after-action review, written to `agents/sigma/work/aar/week-N.md` and committed. Escalates to Blitz only if a finding changes a card, a source, or a gate. A durable rule becomes a proposed CHARTER patch note to Blitz, never a silent self-rewrite.
