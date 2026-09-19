# Yahoo Fantasy Football sample season: Deeper Than 2023

- League: Deeper Than
- Season league ID: 69639
- Custom route: `https://football.fantasysports.yahoo.com/league/deeperthan/2023`
- Yahoo route: `https://football.fantasysports.yahoo.com/2023/f1/69639`
- Andrew's team: **Vaqueros** (team ID 8); the team page visibly identifies the manager as **Andrew Allard**.

## Captured

- `league-home.yml`, `standings-league.yml`, and `evidence-home-full.png`
- `settings-scoring.md`, `settings-scoring.yml`, and `evidence-settings.png`
- `final-standings.md`, `final-standings.yml`, `evidence-standings.png`, `evidence-standings-league.png`
- `playoff-results.md`, `playoff-results.yml`, and `evidence-playoffs.png`
- `draft-results.md`, `draft-results.yml`, and `evidence-draftresults.png`
- `transactions-trades-summary.md`, `transactions.yml`, `transactions-vaqueros.yml`, `trades.yml`, `trades-vaqueros.yml`, and transaction/trade evidence screenshots
- `vaqueros-team.yml` and `evidence-vaqueros.png`

## Gaps

- Yahoo's all-teams transaction view is paginated; the saved all-teams capture is the first visible page (25 records), not a complete season ledger.
- The Vaqueros-filtered capture exposes the visible 2023 team activity, but Yahoo's transaction UI is transaction-side rather than a normalized ledger.
- The trade filter exposes destination-side rows. No Vaqueros trade row was visible; no inference is made about unshown counterparties.
- Draft results are preserved in the full accessibility snapshot; the markdown lists Vaqueros' visible draft order only.

No lineup, add/drop, trade, or save action was performed; Yahoo access was read-only.
