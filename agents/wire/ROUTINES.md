# Wire — scheduled routines (all America/Chicago)

| Routine | Schedule | Purpose |
|---|---|---|
| Wire daily 8am CT NEW digest | Daily 8:00 AM | NEW-only injury/news digest to Ken, copy Blitz |
| Wire Fri 12pm CT availability refresh | Fri 12:00 PM | `availability.json` refresh before Blitz's Friday tweak |
| Wire Sunday AV + inactives + NFL_SIDE | Sun 7:00 AM, 10:35 AM, 2:00 PM, 5:50 PM; Mon 5:45 PM | Pre-lock availability refresh, inactives, game-window lock_state |
| Wire Tue 9am CT lane AAR | Tue 9:00 AM | Wire-lane after-action review, written to `wire/aar/`; durable rules go to Blitz as proposed patches |
