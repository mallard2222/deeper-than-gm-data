# Yahoo Fantasy Football sample season: 8Deep 2022

- League: 8Deep
- Current league lineage: `yahoo-ff-135150` (kept separate from Deeper Than)
- Season league ID: `154513`
- Custom route: `https://football.fantasysports.yahoo.com/league/8deepleague/2022`
- Yahoo route: `https://football.fantasysports.yahoo.com/2022/f1/154513`
- Andrew's team: **Vaqueros** (team ID **8**); the team page visibly identifies the manager as **Andrew Allard**.

## Captured

- `league-home.yml` and `evidence-home-full.png`
- `settings-scoring.md`, `settings-scoring.yml`, and `evidence-settings.png`
- `final-standings.md`, `final-standings.yml`, and `evidence-standings.png`
- `playoff-results.md`, `playoff-results.yml`, and `evidence-playoffs.png`
- `draft-results.md`, `draft-results.yml`, and `evidence-draftresults.png`
- `transactions-trades-summary.md`, `transactions.yml`, `transactions-vaqueros.yml`, `trades.yml`, and the three transaction/trade evidence images
- `vaqueros-team.yml` and `evidence-vaqueros.png`

## Read-only status

All Yahoo pages were accessed read-only. No lineup, add/drop, trade, waiver, or save action was performed.

## Gaps

- The all-teams transactions view is paginated; `transactions.yml` preserves Yahoo's first visible 25-record page, not a complete season ledger.
- The Vaqueros-filtered view preserves the 15 visible rows Yahoo rendered (Sep 22–Dec 11); older or additional rows were not exposed in that view.
- Yahoo's trade filter exposes transaction-side rows rather than a normalized two-sided ledger; only the four visible sides/records are documented.
- `final-standings.yml` is Yahoo's visible Overall Points table; the markdown records the playoff finish separately from the raw table.
- The raw draft capture preserves the complete visible 20-round draft table; the markdown highlights all Vaqueros picks.
