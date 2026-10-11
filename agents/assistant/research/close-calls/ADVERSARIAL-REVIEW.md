# Adversarial Review — Close-Calls Research

**Reviewer:** Consultant (outside the war room)
**Date:** 2026-10-11
**Subject:** `agents/assistant/research/close-calls/` — the 437,000-pair study and the 21-signal model
**Verdict:** The headline finding survives. The study's blind spots are exactly where our real misses live.

---

## What holds up

- **Out-of-sample design is the strongest part.** Train on older seasons, test on games the model never saw, and the 56.6% result held. That is the one number I would trust.
- **The conclusion is the right conclusion.** Start the higher projection. Do not hunt for a secret edge on a coin flip. The study proves the projection is the best single number — not that it is a good number.

---

## What they got wrong or missed

### 1. Survivorship bias — the biggest miss

The 437,000 pairs are only the games where **both players actually played**. Every player ruled out, hurt, or benched before kickoff is missing from the sample. The study tested "which healthy player scores more" — not "which player is actually available."

That is exactly the Gordon miss. Achane was out for the season; the projection still showed last week's role; the study's sample never contains that case. The vacated-volume signal, the closest thing they tested, reversed out of sample — which tells you the study cannot see the failure mode that actually cost us.

**Rule this implies:** the study's findings apply only after the inactive list is clean. Availability is checked first. Projection is the tiebreaker, never the first check.

### 2. 56.6% is a coin flip with a slight tilt

Four of nine losses means the higher projection is wrong almost as often as it is right. The study proves the projection beats the alternatives. It does not prove the projection is reliable. A 56.6% edge is real and it is small — treat it as a tiebreaker, not a conviction.

### 3. Signals tested one at a time

Twenty-one signals, each alone. Nobody tested combinations. A Questionable tag plus a bad matchup plus a home game might move the needle together even if none of them does alone. The study never checked. Until someone runs the joint test, do not stack signals into a tiebreaker — the single-signal results give no license for it.

### 4. Sample era

2021 through this year. The league changed — pass-heavy offenses, new rules, different injury protocols. A model trained on older seasons may not hold for this one. The out-of-sample check partially covers this (it held on recent held-out games), but the training distribution is still the older era. Re-run when 2026 data is complete.

### 5. Position-level results are not in the study

The 56.6% is a blend across all positions. Quarterback volume and efficiency are stable — the projection is strongest there. Tight end is thin enough that the projection is mostly noise. Kicker depends on opponent field position and red-zone trips, which are noisy. Defense cannot see the opponent's quarterback health or script. Running back is mostly role, and role changes fast.

The study does not break the number down by position. Our operating rule — start the higher projection everywhere, attach position-dependent confidence — is a reasonable inference from the data, but it is an inference, not a finding. Label it as such.

---

## What this means for the system

1. **Availability before projection.** Inactive list first. The study cannot see this layer.
2. **Higher projection is the default, not the answer.** 56.6% means you are still wrong four times in nine. Size the confidence to the position.
3. **No stacked tiebreakers.** Single-signal tests give no license to combine signals.
4. **Re-run the study on 2026 data** when the season completes, with position-level splits and a joint-signal test.
5. **The Gordon lesson stands on its own.** It is outside the study's sample by construction. Do not wait for the study to validate it.

---

*This review does not overturn the study's headline. It bounds it.*
