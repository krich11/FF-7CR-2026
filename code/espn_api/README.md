# ESPN Fantasy API (Quantum Blitz)

- `client.py` — read roster, write LINEUP transactions, verify starters
- `cli.py` — `sync | plan | apply | verify | starters`
- Cookies: `../secrets/espn_cookies.json` (chmod 600). Never log values.

Write endpoint:
`POST https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{id}/transactions/`

On verify failure the apply helpers set `alert: true` and audit `ESPN_API_VERIFY_FAIL` — Blitz must ping Ken.
