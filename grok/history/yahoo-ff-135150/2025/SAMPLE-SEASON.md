# Yahoo Fantasy Football sample season: 8Deep 2025

- League: 8Deep
- Current league lineage: `yahoo-ff-135150`
- Season league ID: `117956`
- Custom route: `https://football.fantasysports.yahoo.com/league/8deepleague/2025`
- Yahoo route: `https://football.fantasysports.yahoo.com/2025/f1/117956`
- Andrew's team: **Vaqueros** (team ID **8**); the team page visibly identifies the manager as **Andrew Allard**.

## Captured

- `league-home.yml` and `evidence-home-full.png`
- `settings-scoring.md`, `settings-scoring.yml`, and `evidence-settings.png`
- `final-standings.md`, `final-standings.yml`, and `evidence-standings.png`
- `playoff-results.md`, `playoff-results.yml`, and `evidence-playoffs.png`
- `draft-results.md`, `draft-results.yml`, and `evidence-draftresults.png`
- `transactions-trades-summary.md`, `transactions.yml`, `transactions-vaqueros.yml`, `trades.yml`, `evidence-transactions.png`, `evidence-transactions-vaqueros.png`, and `evidence-trades.png`
- `vaqueros-team.yml` and `evidence-vaqueros.png`

## Read-only status

All Yahoo pages were accessed read-only. No lineup, add/drop, trade, waiver, or save action was performed.

## Gaps

- The all-teams transactions view is paginated; `transactions.yml` is the first visible 25-record page. The Vaqueros-filtered capture preserves the visible team-history slice Yahoo rendered.
- Yahoo's trade filter exposes transaction-side rows rather than a normalized two-sided ledger; no unshown counterparties or exhaustive trade count is inferred.
- Draft results are preserved in the full accessibility snapshot; only selected Vaqueros picks are repeated in `draft-results.md`.
- Yahoo's standings page reports the final update timestamp shown in the raw capture; all accessed views were read-only.
