# Yahoo Fantasy Football sample season: Deeper Than 2019

- League: Deeper Than
- Season league ID: 56453
- Custom route: `https://football.fantasysports.yahoo.com/league/deeperthan/2019`
- Yahoo route: `https://football.fantasysports.yahoo.com/2019/f1/56453`
- Andrew's team: **Vaqueros** (team ID 8). The archived team page visibly identifies the manager as **Andrew Allard**.

## Captured

- `league-home.yml`, `league-home-custom.yml`, and `evidence-home-full.png`
- `standings-league.yml` and `evidence-standings-league.png`
- `settings-scoring.md`, `settings-scoring.yml`, and `evidence-settings.png`
- `final-standings.md`, `final-standings.yml`, and `evidence-standings.png`
- `playoff-results.md`, `playoff-results.yml`, and `evidence-playoffs.png`
- `draft-results.md`, `draft-results.yml`, and `evidence-draftresults.png`
- `transactions-trades-summary.md`, transaction/trade YAML captures, and evidence screenshots
- `vaqueros-team.yml` and `evidence-vaqueros.png`

## Gaps

- Yahoo's all-teams transaction view exposed only the first visible page (25 rows); the UI offers no normalized season export here.
- The Vaqueros-filtered activity view exposed 20 visible rows, Sep 11–Dec 11; this is not established as a complete season ledger.
- The all-league trade filter exposed 8 visible records (Aug 27–Nov 9). The Vaqueros-filtered trade view reports “No recent transactions”; this does not prove no other historical activity exists outside Yahoo's visible archive.
- Yahoo's league standings panel exposes the team table and championship panel; the captured direct `/standings` page is preserved separately as `final-standings.yml` (player overall points view).
- The archived home/playoffs panel labels the championship bracket “TBD” even though the championship summary shows Vaqueros first, DUGASM second, and bigballs third.

No lineup, add/drop, trade, or save action was performed; Yahoo access was read-only.
