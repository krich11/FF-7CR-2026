> **SUPERSEDED by 2026-09-25 Blitz law — Blitz writes, specialists propose.** (Law: BLITZ.md + WAR.md win on any conflict.)
>
> **Superseded per issue 5 (Oct 6 2026):** Sigma references in this file are superseded. Sigma is retired. Assistant owns projections and the usage baseline. The shadow-edge lane is retired.

# Quantum Blitz Co-Manager
## Grok Bot Functional Specification

**Version:** 2.4  
**Target platform:** Grok Bot (named teammate on the persistent cloud computer)  
**Status:** Ready to install as Bot skills + routines  
**League:** 7 Creeks Armchair Quarterbacks · ESPN · 12-team · PPR  
**Team:** Quantum Blitz (Ken Rich)  
**Slots:** QB, 2 RB, 2 WR, TE, FLEX (RB/WR/TE), D/ST, K  
**Lock policy:** ESPN default — each player locks at *that player’s* kickoff, not at the first game of the week

---

## 0. Why this is a Bot job

Grok chat and Grok Automations can write a Friday card. They reset context and cannot open ESPN.

Grok Bot is the co-manager because it can:

- Keep a named identity and memory across the season
- Store roster, week cards, and availability files on its cloud filesystem
- Prefer ESPN Fantasy API for roster sync + lineup apply (verify after write; alert Ken on fail)
- Drive ESPN and injury pages with computer use when API auth fails or for screenshots
- Learn the ESPN click-path once via **Teach a task**, then reuse it as fallback
- Run **routines** while Ken’s laptop is closed
- Separate *set the week* from *Friday tweak* so Thursday games are not treated as unlocked

Chat remains the place for one-off arguments (“Goedert or Meyers?”). The Bot owns the weekly operating cadence.

---

## 1. Purpose

Produce legal, current start/sit advice for Quantum Blitz every NFL week, then optionally apply the lineup in ESPN **only after Ken approves**.

The Bot must know the week clock:

- An NFL week is **not** Sunday-to-Sunday.
- Games run Wednesday or Thursday through Monday (2026 Week 1 starts Wednesday, September 9).
- Friday work is an **injury-report tweak** for remaining Sunday/Monday players.
- Friday cannot change players whose games already kicked or are mid-game.

---

## 2. Goals and non-goals

### 2.1 Goals

- Sync the live ESPN roster into a local file before every decision.
- Recommend a full legal lineup before the week’s first kickoff.
- Re-optimize only still-unlocked slots after Friday reports and Sunday inactives.
- Explain each start and notable sit in one line.
- Keep a FLEX shortlist when the gap is small.
- Persist week-over-week memory (who was limited, who was stashed, what failed).
- Adjust next week’s ratings from *this roster’s* recent actual PPR vs what we expected: underperformers drop, bench players who beat them rise, with shrinkage so one game cannot overthrow a locked-in starter.

### 2.2 Non-goals / hard stops

- Do not invent players, injuries, projections, or opponents.
- Do not drop, add, or trade without approval. Auto-commit never claims waivers or drops players.
- Do not spend FAAB or claim waivers without approval.
- Do not write ESPN unless Ken said `yes, set it` **or** the §7.6 dead-man timer fired and every auto-commit gate passed.
- Do not treat “expected to be on the team” as “plays this week.”
- Do not reuse last week’s card if the live roster or injury file cannot be refreshed.
- Do not put ESPN passwords in skill text, chat, or recorded Teach-a-task video. Use Bot secure credential handoff.

---

## 3. Bot architecture

```
Ken  ←→  Bot “Blitz” (this co-manager)
              │
              ├─ Skill /lineup.set        Tuesday–Wednesday
              ├─ Skill /lineup.tweak      Friday after injury report
              ├─ Skill /lineup.lock       Sunday morning inactives
              ├─ Skill /lineup.autocommit after silence deadline
              ├─ Skill /roster.sync       anytime
              └─ Files on Bot computer
                    /fantasy/quantum-blitz/
                      league.json
                      roster.json
                      availability.json
                      projections.json
                      cards/week-{N}.md
                      decisions/week-{N}.json
                      form.json
                      usage.json
                      sources.json
                      preferences.json
                      standings.json
                      results/week-{N}.json
                      audit.log
```

Optional second Bot (“Wire”) may only fetch news and write `availability.json`. Blitz owns decisions. All Bots share one user computer — treat ESPN login as visible to every Bot on this account.

---

## 4. League configuration (`league.json`)

```json
{
  "league_name": "7 Creeks Armchair Quarterbacks",
  "host": "espn",
  "scoring": "ppr",
  "slots": ["QB", "RB", "RB", "WR", "WR", "TE", "FLEX", "DST", "K"],
  "flex_eligible": ["RB", "WR", "TE"],
  "team_count": 12,
  "team_name": "Quantum Blitz",
  "timezone": "America/Los_Angeles",
  "display_timezone": "America/Chicago",
  "lock_policy": "player_kickoff",
  "te_flex_premium": 1.5,
  "flex_gap_threshold": 1.0,
  "qb_swap_threshold": 4.0
}
```

Human rules stored with the league file:

- Start healthy studs over matchup fades.
- TE2 is FLEX only if it beats the best WR/RB by `te_flex_premium` **or** both WR FLEX options are LIMITED/QUESTIONABLE.
- Never start Out / IR / PUP / Exempt / suspended.
- Start rostered DST and K unless a second one is rostered and better by ≥ 3.0.

---

## 5. Week clock (required knowledge)

### 5.1 Windows

| Window | NFL reality | Bot job | Unlocked pool |
|---|---|---|---|
| **Set** | Before first game of the NFL week | `/lineup.set` | Entire roster |
| **TNF/WNF** | Wed/Thu kickoff | No new card unless Ken asks | Everyone not in that game |
| **Tweak** | Friday official injury report | `/lineup.tweak` | Sun + Mon players only |
| **Lock** | ~90 min before 1:00 ET Sunday | `/lineup.lock` | Later Sunday + Mon only |
| **Done** | After a player’s kickoff | Log actuals Monday | None for that player |


### 5.0b Display timezone (Ken 2026-09-08)
Ken is **America/Chicago (CT)**. Every Ken-facing time on cards, check-ins, deadlines, and Games to watch **must be labeled CT** (convert from stored ISO / America/Los_Angeles lock math). Internal files may keep `America/Los_Angeles` offsets for ESPN lock comparisons. Never print bare PT times to Ken without converting.

### 5.2 Rules the Bot must print on every card

```
WEEK CLOCK
- First kickoff this NFL week: {day time opponent}
- Players already LOCKED or DONE: {list or none}
- This run may change: {set | sunday-monday | late-windows-only}
```

If Ken says “set my lineup” on Friday, the Bot still runs `/lineup.tweak`, not `/lineup.set`. It must say which slots are frozen.

### 5.3 2026 Week 1 exception

- Wed Sep 9, 7:20 PM CT — NE @ SEA (Shaheed / Darnold / Charbonnet universe)
- Thu Sep 10, 7:35 PM CT — SF vs LAR in Melbourne (Eddy Pineiro)
- Sunday Sep 13 — bulk slate
- Mon Sep 14 — DEN @ KC

Pineiro must be decided in the **Set** window, not Friday.

---

## 6. Persistent state

### 6.1 `roster.json`

Synced from ESPN before every skill run. Fields per player: name, pos, nfl_team, espn_id if known, acquisition note, `eligible_slots`.

Seed roster (replace on first successful ESPN sync):

```text
QB  Jaxson Dart, Sam Darnold
RB  De'Von Achane, Travis Etienne Jr., Josh Jacobs, Jonathon Brooks, Zach Charbonnet
WR  Drake London, Garrett Wilson, Michael Pittman Jr., Jakobi Meyers, Rashid Shaheed
TE  Kyle Pitts Sr., Dallas Goedert
DST Steelers
K   Eddy Pineiro
```

Known designations until disproven by a same-week official source:

- Josh Jacobs → `EXEMPT`
- Zach Charbonnet → `PUP` (minimum four games)

### 6.2 `availability.json`

One row per rostered player:

```json
{
  "player": "Michael Pittman Jr.",
  "state": "LIMITED",
  "play_prob": 0.80,
  "snap_mult": 0.70,
  "news": "Expected Week 1; Steelers easing him in after hamstring.",
  "source": "beat",
  "as_of": "2026-09-05T16:00:00-07:00",
  "kickoff": "2026-09-13T10:00:00-07:00",
  "lock_state": "UNLOCKED"
}
```

`lock_state` ∈ `UNLOCKED | LOCKED | DONE`.

### 6.3 `cards/week-{N}.md` and `decisions/week-{N}.json`

The published card plus machine-readable slot assignments, scores, and which skill produced them. Friday and Sunday runs patch the same week files; they do not start a new week.

### 6.4 Stale-data policy

If ESPN roster, schedule, or Friday injury report cannot be fetched, **do not** reuse last week’s numbers as if current. Post a failure note in the Bot thread and keep the last good card marked `STALE`.

---

## 7. Availability and scoring

Same model as v1.0, executed by the Bot after files are fresh.

### 7.1 Availability states

`ACTIVE | LIMITED | QUESTIONABLE | DOUBTFUL | OUT | PUP | IR | EXEMPT | BYE | UNKNOWN`

- `OUT`, `PUP`, `IR`, `EXEMPT`, `BYE` → start score 0, removed from pool
- `LIMITED` default `snap_mult = 0.70`
- `QUESTIONABLE` + “expected to play” → `play_prob = 0.75`
- Other `QUESTIONABLE` → `play_prob = 0.45`
- Source order: official report / inactives → same-day beat → national desk → projection sites (numbers only)

### 7.2 Adjusted points

```
adj = consensus_ppr × play_prob × snap_mult × weather_mult × role_mult
start_score = 0.70*adj + 0.20*floor + 0.10*ceiling - risk_penalty
```

Ceiling multipliers: TE 1.30, WR 1.50, RB1 1.40, committee RB 1.25.  
`risk_penalty = 1.5` when state is LIMITED/QUESTIONABLE and a healthy alt is within `flex_gap_threshold`.

If two projection sources disagree by > 3.0 PPR, trimmed mean and raise uncertainty.

If a source still projects an Exempt/PUP/IR player as a starter, discard that source for that player.

Then apply **roster form** from §7.4:

```
adj_form = adj + form_add
start_score uses adj_form in place of adj
```

### 7.3 Optimizer

Exhaustive assignment on ≤16 players.

1. Drop ineligible and `DONE`/`LOCKED` players from the editable pool.
2. Keep already-started players in their committed slots.
3. Fill remaining locked-role slots: QB, 2 RB, 2 WR, TE, DST, K.
4. FLEX from leftovers after TE2 premium.
5. Do not auto-swap a healthy overall stud (`adj` clearly RB1/WR1) for a 1-point matchup edge.
6. Form can flip FLEX and the last RB/WR starter. It cannot sit Achane/London/Wilson-class studs after one bad game unless availability or role also broke.

### 7.4 Roster form (prior-week performance)

This is intra-roster only. Compare players Ken actually owns. Do not import league-wide “hot lists.”

After each NFL week the Bot writes `results/week-{N}.json` (actual PPR, our `adj` going in, slot started or benched) and updates `form.json`.

**Lookback:** last 1 week if only one game exists; last 3 played games when available. Bye / OUT / EXEMPT / PUP weeks do not count.

```
expected_avg_i = mean(adj we assigned in those weeks)
actual_avg_i   = mean(actual PPR in those weeks)
residual_i     = actual_avg_i - expected_avg_i
```

**Shrinkage** so one explosion or dud is not a new identity:

```
form_add_i = clamp(0.35 * residual_i, -3.0, +3.0)
```

Week 1: `form_add = 0` for everyone (no prior 2026 game).  
Week 2: coefficient 0.35, cap ±3.  
Weeks 3+: same formula on the 3-game window.

**Bench-vs-starter boost (the rule Ken asked for):**

If a bench player `B` outscored a started player `S` at a FLEX-eligible position last week by ≥ 5.0 PPR, and `B` is ACTIVE or LIMITED with a real role next week:

```
form_add_B += 1.0
form_add_S -= 0.75
```

Still subject to the ±3.0 cap. Role gate is mandatory: a backup who scored on a fluke 80-yard TD while the starter was injured does **not** get the +1.0 if the starter is back and the backup returns to 8 snaps.

**Do not apply form when:**

- Player is now OUT / PUP / IR / EXEMPT / BYE
- Residual is from a game the player left injured (use availability, not form)
- Sample is one half of football
- The “underperformer” is a locked stud and the bench option is still a committee/WR3 with no role change

**Print on the card** when form changes a starter:

```
FORM: {bench player} +{n} vs {starter} {residual last week}. FLEX flipped.
```

If form does not flip anyone, omit the line.

`form.json` example:

```json
{
  "as_of_week": 3,
  "players": {
    "Jakobi Meyers": {
      "games": 3,
      "actual_avg": 14.2,
      "expected_avg": 10.1,
      "residual": 4.1,
      "form_add": 1.44,
      "beat_starter_last_week": true
    }
  }
}
```

### 7.5 Other feedback loops

Form is one loop. These also write files on Monday and change next week’s `adj` or rules. If the input is missing, skip that loop; do not guess.

**Usage (leading indicator, stronger than points).**  
Record carries, targets, routes, snap % for each rostered skill player. Compare to the role we assumed (`role_mult`, `snap_mult`).

```
usage_gap = actual_snap% - assumed_snap%
role_mult_next = clamp(role_mult * (1 + 0.5 * usage_gap), 0.50, 1.15)
```

A WR3 who scored 18 on 3 targets does not get a usage boost. A WR who scored 8 on 11 targets does. Update `usage.json`. If snap share falls two straight weeks, cut `role_mult` even if form still looks fine.

**Game script filter on form.**  
If the team was trailing/leading by 16+ at kick of the 4th and the residual is mostly that script (pass-heavy backup WR boom, or RB zeroed in a blowout), shrink that week’s residual by half before it enters `form_add`. Do not punish Etienne for a 35–7 hole the same way you punish a full-game 8-snap committee.

**Ken overrides (revealed preference).**  
Every time Ken starts someone the Bot sat, or replies “don’t sit X,” append `preferences.json`.

```
{ "week": 2, "bot": "Meyers", "ken": "Goedert", "reason": "want TE floor" }
```

After two overrides in the same direction, promote it to a human rule for the rest of the season (example: “prefer Goedert FLEX when the WR gap is < 2.0”). One override is a data point, not a new constitution.

**Projection-source weights.**  
For rostered players only, track abs(error) by source. Next week:

```
weight_s = 1 / (mean_abs_error_s + 1.0)
```

Normalize across sources. A source that still projected Jacobs as RB1 after Exempt is zeroed for legal-status cases, not just down-weighted.

**Play-prob calibration.**  
When a team says “expected to play” and the player is inactive, lower that team’s Q prior next time (`0.75 → 0.55` after two misses). When they say it and the player gets full snaps, keep 0.75.

**Standings mode.**  
Read ESPN record into `standings.json`.

| Situation | Weights |
|---|---|
| Default / .500 | 70 expected / 20 floor / 10 ceiling |
| Must-win or ≥2 games back after Week 6 | 55 / 15 / 30 |
| Two-game lead, Week 10+ | 60 / 30 / 10 |

Do not change weights before Week 6. Early record is noise.

**Process misses.**  
If a recommended starter was inactive, or ESPN apply did not match the approved card, log `PROCESS_MISS` and move the next Sunday routine 30 minutes earlier. Two process misses → Bot must preview the ESPN lineup screenshot before asking for `yes, set it`.

**DST/K loop.**  
If the rostered DST or K finishes outside the top 16 at the position two straight weeks *and* a replacement is already on the roster, allow the swap. Do not stream off waivers in this loop unless Ken asked.

**Do not add these loops:**

- League-wide hot-player lists
- One-week DST ranking chases
- Betting-line overreaction after a single Sunday
- Stacking Dart with Giant pass-catchers Ken does not own


### 7.5a Shadow edges (paper track only)

Ken 2026-09-05: keep §7 optimizer as-is. Weekly paper-track three optional signals in `edges/shadow/` + `EDGES.md`:

1. `vegas_flex` — Vegas/implied team total prior on **FLEX only**
2. `share_trend` — midweek target/carry share trend
3. `dst_k_script` — correlated DST/K game environment when streaming

Score vs SPEC picks on Monday (`week.review`). Do **not** change ESPN lineups from shadow alone. Midseason (~Week 8+): if one signal is clearly ahead with enough flips, offer promotion — Ken decides.


### 7.5b Sigma research tracks (paper only)

Ken skip-level 2026-09-05: Sigma paper-tracks additional signals (matchup-adjusted residuals, opp vs efficiency, intra-roster VORP-lite, handcuff/injury-tree EV, post–Week 6 standings leverage on FLEX/DST). Details in `SIGMA.md`. Scored like §7.5a shadow edges — **do not** change live §7 optimizer or ESPN without Blitz/Ken promotion.


### 7.6 Dead-man auto-commit

Ken can be gone for days. Silence is treated as approval of the **current legal card**, not as “leave last week’s ESPN lineup forever.”

This is a timer plus gates. It is not “always push whatever the Bot just thought.”

**Commands (thread, case-insensitive)**

| Ken says | Effect |
|---|---|
| `yes, set it` | Apply now |
| `hold` / `stop` | Cancel auto-commit for this window |
| `away until {datetime}` | Auto-commit each new card **60 minutes** after post (or 3 hours before next kickoff if sooner) until that datetime |
| `home` | Back to default timers |

Default when Ken says nothing: **away-safe on**. He asked for unattended apply.

**Deadlines (routines fire on America/Los_Angeles wall; print CT to Ken)**

| Card | Posted | Auto-commit if no `hold` |
|---|---|---|
| Set | Tue 12:00 | **Tue 20:00**, or **3 hours before first kickoff**, whichever is earlier |
| Set backup | Wed 10:00 | **Wed 14:00**, or 3 hours before first kickoff |
| Friday tweak | Fri 14:00 | **Fri 20:00** |
| Sunday lock | Sun 08:00 | **Sun 08:40** only if a 1:00 ET starter is OUT; else do not touch ESPN |

If Ken is still silent on Saturday, do **not** re-apply Tuesday’s card as if it were new. Only apply if ESPN starters still differ from the last good card and slots are unlocked.

**Gates — all must pass or Bot posts `AUTO-COMMIT BLOCKED` and leaves ESPN alone**

1. Card is this NFL week and not marked `STALE`
2. Confidence is High or Medium, never Low
3. `roster.json` synced in the last 6 hours and matches ESPN
4. No recommended starter is OUT / IR / PUP / EXEMPT / BYE
5. No unresolved name mismatch
6. Apply list is only `UNLOCKED` slots
7. Diff vs current ESPN starters is non-empty (no-op if already set)
8. Thread does not contain `hold` or `stop` after the card
9. ESPN editor shows the same player names before Save
10. Screenshot `before.png` saved

If any gate fails, keep the last successfully applied lineup. Missing data ≠ apply anyway.

**What auto-commit may do:** move players between bench and starting slots.

**What it may never do:** drop, add, trade, IR moves, FAAB, change settings.

**Notify twice:** at card post (“auto-applies {deadline} unless you reply hold”) and at apply time (“AUTO-APPLIED {slots}”).

**Multi-day absence:** Ken should send `away until Monday 8am` once. That is enough for Set + Friday tweak + Sunday lock to fire without him. If he sends nothing all season, default timers still fire. Safer than leaving Week 0’s lineup through Thursday.

**If first kickoff is during the silence window:** apply immediately when the 3-hour-before-kickoff mark hits, even if the Tue 20:00 timer has not.

---

## 8. Grok Bot skills

Install these as Bot skills. Ken types `/lineup.set` or routines call them.

Each skill states: when to use, inputs, steps, validation, output, approval.

### 8.1 Skill `roster.sync`

**When:** First step of every other skill, or on “I made a claim.”

**Steps:**

1. Open ESPN league → Quantum Blitz roster (computer use; reuse saved session).
2. Write `roster.json`. Diff against previous file.
3. If a player appeared or disappeared, ask Ken before assuming it is correct.
4. Pull this NFL week’s schedule into `schedule.json` with kickoff timestamps in `America/Los_Angeles`.
5. Set `lock_state` from now vs kickoff.

**Approval:** none for read. Login credentials via secure handoff only.

**Teach-a-task:** Ken should demonstrate ESPN login + roster page once (no password typed in the recording). Cap 10 minutes.

### 8.2 Skill `lineup.set` — week opener

**When:** Tuesday 12:00 PT or Wednesday 10:00 PT, always **before** the week’s first kickoff. Also on demand: “set Week N.”

**Steps:**

1. Run `roster.sync`.
2. Browse official injury page + beat reports + two PPR projection sources.
3. Write `availability.json` and `projections.json`.
4. Optimize the **full** lineup.
5. Post the card in the Bot thread.
6. Post the card with the auto-commit deadline in the header.
7. If Ken replies `yes, set it` before the deadline, apply immediately.
8. If Ken replies `hold`, do not apply this window.
9. Otherwise `/lineup.autocommit` runs at the deadline and applies only if §7.6 gates pass.

**Validation:** every recommended starter is on `roster.json`, eligible for the slot, and not EXEMPT/OUT/PUP/IR/BYE. Week-clock block is present. Pineiro-class midweek players are explicitly called out.

### 8.3 Skill `lineup.tweak` — Friday closer

**When:** Friday 14:00 America/Los_Angeles (after typical 13:00 PT / 16:00 ET injury reports).

**Steps:**

1. Run `roster.sync`.
2. Mark Wed/Thu players `LOCKED` or `DONE`. Do not recommend swapping them.
3. Refresh Friday practice/injury report only for unlocked players.
4. Re-optimize **unlocked slots only**. Default contested slot is FLEX; also RB2/WR2 if a starter is newly OUT.
5. Diff vs `cards/week-{N}.md`. Title the post `Friday tweak — Week {N}`.
6. Apply on `yes, set it`, or at the Friday 20:00 auto-commit if gates pass. Unlocked slots only.

**Validation:** card lists frozen players separately from recommended changes. No instruction to move a Thursday kicker after that game.

### 8.4 Skill `lineup.lock` — Sunday inactives

**When:** Sunday 08:00 PT.

**Steps:**

1. Check inactives for 10:00 PT / 1:00 ET games.
2. If a recommended 1:00 starter is OUT and an unlocked replacement exists, post an emergency swap.
3. Do not touch already kicked games.

### 8.5 Skill `week.review` — Monday learning

**When:** Monday 08:00 PT.

1. Pull actual PPR, snaps, targets/carries from ESPN box scores.
2. Write `results/week-{N}.json`.
3. Recompute `form.json` (§7.4) and `usage.json`, `sources.json` (§7.5).
4. Apply game-script filter before form.
5. Record Ken overrides into `preferences.json`.
6. Update `standings.json` and process-miss flags.
7. Append at most three memory bullets. Numeric loops live in the files, not the bullets.

---

## 9. Routines

Create these on Bot **Blitz**. Routines use `CRON_TZ=America/Los_Angeles` (absolute cadence); Ken-facing times always `America/Chicago` (CT).

| Routine | Cadence | Skill | If source missing |
|---|---|---|---|
| Set the week | `Every Tuesday at 12:00` | `/lineup.set` | Fail visible; do not reuse stale card as current |
| Set-week backup | `Every Wednesday at 10:00` | `/lineup.set` only if Tuesday card is missing or `STALE` | Fail visible |
| Friday tweak | `Every Friday at 14:00` | `/lineup.tweak` | Fail visible |
| Sunday inactives | `Every Sunday at 08:00` | `/lineup.lock` | Fail visible |
| Set autocommit | `Every Tuesday at 20:00` | `/lineup.autocommit` | Block; do not apply stale |
| Set autocommit 2 | `Every Wednesday at 14:00` | `/lineup.autocommit` | Block; do not apply stale |
| Friday autocommit | `Every Friday at 20:00` | `/lineup.autocommit` | Block; do not apply stale |
| Sunday autocommit | `Every Sunday at 08:40` | `/lineup.autocommit` | Only if a 1:00 starter is OUT |
| Monday review | `Every Monday at 08:00` | `/week.review` | Skip quietly |

Routine creation prompt to paste into the Bot:

```text
You own Quantum Blitz weekly lineup.
Timezone America/Los_Angeles.
Create routines:
- Tuesday 12:00 run skill lineup.set
- Wednesday 10:00 run skill lineup.set only if this week's card is missing or STALE
- Friday 14:00 run skill lineup.tweak
- Sunday 08:00 run skill lineup.lock
- Monday 08:00 run skill week.review
Post each card in this conversation.
Never change the ESPN lineup unless Ken replies "yes, set it" in thread.
If ESPN, schedule, or injury data cannot be fetched, report failure. Do not pretend last week's card is current.
```

Limits: one Bot may own ≤50 routines; the app keeps 20 recent runs per routine. Test runs do real work — test with approval-required so ESPN is not written during rehearsal.

---

## 10. ESPN apply playbook

**Preferred:** Fantasy API via `/workspace/fantasy/quantum-blitz/espn_api/` ([espn.api-apply] skill).
- Auth: box-local `secrets/espn_cookies.json` (`SWID`, `espn_s2`) — never paste into chat
- Read: `lm-api-reads` → `cli.py sync` / `starters`
- Write: `lm-api-writes` `/transactions/` LINEUP moves → `cli.py apply --week N`
- **Always re-read after write.** If verify mismatches or HTTP fails: alert Ken `ESPN API VERIFY FAILED` and do not claim success

**Fallback:** saved browser session on the Bot computer + [espn.lineup-shots].

1. espn.com/fantasy/football → league 7 Creeks Armchair Quarterbacks → Quantum Blitz
2. Roster page → dump names/positions (only if API sync unavailable)
3. Lineup editor → read current starters vs bench
4. On approved apply: drag recommended players into slots, **stop before Save** if Ken asked for preview-only; Save only on `yes, set it`
5. Screenshot `before.png` / `after.png` into `/fantasy/quantum-blitz/cards/`

If the ESPN DOM changes, stop and ask Ken to re-teach the path. Do not click randomly.

Projection/news pages (read-only): ESPN injury report, team official IR, FantasyPros PPR week projections, named beat reporters.

---

## 11. Output contract

Every Set / Tweak / Lock post uses this shape.

```markdown
# Week {N} {SET|TWEAK|LOCK} — Quantum Blitz

**Week clock:** first kickoff {when} · this run may change {pool}
**Already locked/done:** {list or none}
**Confidence:** High | Medium | Low
**Scoring:** PPR · 2WR + FLEX

## Start
- QB: ...
- RB: ...
- RB: ...
- WR: ...
- WR: ...
- TE: ...
- FLEX: ...
- D/ST: ...
- K: ...

## FLEX shortlist
1. {name} — {adj} — START|ALT|SIT — {why}
2. ...
3. ...

## Sit
- {name} — {why}

## Tweaks vs last card
- {change or "no change"}

## Watch before next lock
- {bullet}

## Games to watch (SET cards — Ken 2026-09-08)
Chronological list of NFL games this week that include **any Quantum Blitz rostered player**. End of card only; required on SET (optional on TWEAK/LOCK if kickoffs shifted).
- {kickoff CT} · {AWAY @ HOME} — {Player (slot/BENCH), …}

Reply `yes, set it` to push unlocked slots to ESPN.
```

`why` ≤ 140 characters. Core card ≤ 400 words; **Games to watch** does not count toward that cap.

---

## 12. Conflict and safety matrix

| Conflict | Winner |
|---|---|
| Official inactive vs projection | Official; score 0 |
| Beat snap-count vs consensus proj | Beat + `snap_mult` |
| Optimizer vs human rule | Human rule; show both scores |
| Friday request vs Thursday player | Thursday stays frozen |
| LLM story vs file number | File number |
| Ken verbal start vs optimizer | Ken, after the Bot states the point cost |
| Any ESPN write | Blocked until `yes, set it` |

Shared-computer warning: do not store league-mate private messages or extra logins on this VM.

---

## 13. Evaluation

A week succeeds if:

1. Set card posted before first kickoff
2. No ineligible starter recommended
3. Friday card did not try to move a locked player
4. FLEX choice within 1.0 projected point of the best legal option, or forced by a human rule
5. ESPN writes happened only after approval
6. Zero invented facts

Track FLEX regret (≥5 PPR left on bench) in Monday review. Target < 35% of weeks.

---

## 14. Install sequence

1. Create Bot **Blitz**. Give it this spec file on the computer at `/fantasy/quantum-blitz/SPEC.md`.
2. Ask: “Save skills lineup.set, lineup.tweak, lineup.lock, roster.sync, week.review from SPEC.md.”
3. Teach ESPN roster navigation once.
4. Run `/lineup.set` once while Ken watches. Do not enable routines until that card is correct.
5. Create the five routines in §9.
6. Keep the existing Grok Automation “Quantum Blitz Friday lineup” as a backup phone card only. Bot is source of truth.

---

## 15. Seed Week 1 behavior

Until live data changes it:

- Do not start Jacobs (`EXEMPT`) or Charbonnet (`PUP`).
- Set Pineiro in the **Set** window; Friday must list him LOCKED/DONE after Thursday.
- Default Sunday core: Dart; Achane; Etienne; London; Wilson; Pitts; FLEX = Pittman if full-go, else Goedert if both WRs limited, else Meyers; Steelers; Pineiro if not already played.
- TE-as-FLEX is allowed only under §4 human rules.
- `form_add = 0` until Week 1 box scores exist. First form pass is Monday Sep 14 after Week 1.

---

## 16. Open questions for first live week

- Confirm ESPN league lock is still per-player kickoff (default).
- Confirm whether Exempt players can sit in an IR slot.
- Decide if Ken wants Bot to draft waiver names only, or also submit claims after approval.

---

## 17. Acceptance

Installed when:

- `/lineup.set` produces a legal card with a week-clock block
- `/lineup.tweak` refuses to move Thursday players
- ESPN apply requires `yes, set it`
- Routines are visible with next-run times; Ken-facing copy always CT
- `roster.json` matches the live ESPN roster after sync
