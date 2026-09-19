# Yahoo Fantasy Football sample season: 8Deep 2020

- League: 8Deep
- Current league lineage: `yahoo-ff-135150` (kept separate from Deeper Than)
- Season league ID: `622076`
- Custom route: `https://football.fantasysports.yahoo.com/league/8deepleague/2020`
- Yahoo route: `https://football.fantasysports.yahoo.com/2020/f1/622076`
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

- The all-teams transactions view is paginated; `transactions.yml` preserves Yahoo's first visible 25-record page.
- The Vaqueros-filtered view exposes 23 visible add/drop rows (Sep 5–Dec 13); older or additional rows were not exposed in that view.
- The trade filter rendered **No recent transactions**; no trade ledger is inferred.
- The playoff URL `/standings?stype=playoff` rendered the same visible Overall Points table rather than a bracket; `playoff-results.md` does not infer a bracket finish beyond the Vaqueros team page's 5th Place.
- `final-standings.yml` is Yahoo's visible Overall Points table.
- The raw draft capture preserves the complete visible 20-round, 8-team draft table; rounds 18–20 for Vaqueros are visibly empty.
