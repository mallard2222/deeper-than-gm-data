# Yahoo Fantasy Football sample season: Deeper Than 2024

- League: Deeper Than
- Season league ID: 181730
- Custom route: `https://football.fantasysports.yahoo.com/league/deeperthan/2024`
- Yahoo route: `https://football.fantasysports.yahoo.com/2024/f1/181730`
- Andrew's team: **Vaqueros** (team ID 8); the team page visibly identifies the manager as **Andrew Allard**.

## Captured

- `league-home.yml` and `evidence-home-full.png`
- `settings-scoring.md` plus `settings-scoring.yml` and `evidence-settings.png`
- `final-standings.md` plus `final-standings.yml` and `evidence-standings.png`
- `playoff-results.md` plus `playoff-results.yml` and `evidence-playoffs.png`
- `draft-results.md`, `draft-results.yml`, and `evidence-draftresults.png`
- `transactions-trades-summary.md`, `transactions.yml`, `transactions-vaqueros.yml`, `trades.yml`, `evidence-transactions.png`, `evidence-transactions-vaqueros.png`, and `evidence-trades.png`
- `vaqueros-team.yml` and `evidence-vaqueros.png` for the Andrew/Vaqueros mapping and finish

## Gaps

- The all-teams transactions view is paginated; the raw capture is the first visible page (25 records). A Vaqueros-filtered raw capture is also saved as `transactions-vaqueros.yml`.
- Yahoo's trade filter exposes transaction-side rows, not a normalized trade ledger. The summary preserves the visible sides and does not infer unshown counterparties or a total trade count.
- Draft results are preserved in the full accessibility snapshot; no separate hand-transcribed complete draft table was added.
- No lineup, add/drop, trade, or save action was performed; all Yahoo access was read-only.
