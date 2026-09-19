# Yahoo Fantasy Football sample season: Deeper Than 2022

- League: Deeper Than
- Season league ID: 59165
- Custom route: `https://football.fantasysports.yahoo.com/league/deeperthan/2022`
- Yahoo route: `https://football.fantasysports.yahoo.com/2022/f1/59165`
- Andrew's team: **Vaqueros** (team ID 8); the archived home and team pages visibly identify the manager as **Andrew Allard**.

## Captured

- `league-home.yml`, `standings-league.yml`, and home/standings evidence screenshots
- `settings-scoring.md`, `settings-scoring.yml`, and `evidence-settings.png`
- `final-standings.md`, `final-standings.yml`, and `evidence-standings.png`
- `playoff-results.md`, `playoff-results.yml`, and `evidence-playoffs.png`
- `draft-results.md`, `draft-results.yml`, and `evidence-draftresults.png`
- `transactions-trades-summary.md`, transaction/trade YAML captures, and evidence screenshots
- `vaqueros-team.yml` and `evidence-vaqueros.png`

## Gaps

- Yahoo's all-teams transaction view is paginated; `transactions.yml` preserves the first visible page (25 records), not a complete season ledger.
- The Vaqueros-filtered capture preserves the visible archived activity (20 transaction rows, Sep 22–Dec 21); Yahoo provides no normalized transaction export here.
- The all-teams trade filter exposes destination-side rows only: four visible destination records, all to other teams. The Vaqueros-filtered trade capture says “No recent transactions”; no inference is made about unshown counterparties.
- Draft results are preserved in the full accessibility snapshot; the markdown lists Vaqueros' visible draft order only (Yahoo marks Mark Andrews with its keeper icon).

No lineup, add/drop, trade, or save action was performed; Yahoo access was read-only.
