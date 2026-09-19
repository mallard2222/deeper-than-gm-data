# Yahoo Fantasy Football sample season: Deeper Than 2021

- League: Deeper Than
- Season league ID: 771925
- Custom route: `https://football.fantasysports.yahoo.com/league/deeperthan/2021`
- Yahoo route: `https://football.fantasysports.yahoo.com/2021/f1/771925`
- Andrew's team: **Vaqueros** (team ID 8); the archived team page visibly identifies the manager as **Andrew Allard**.

## Captured

- `league-home.yml` and `league-home-custom.yml`, plus `evidence-home-full.png`
- `standings-league.yml` and `evidence-standings-league.png`
- `settings-scoring.md` plus `settings-scoring.yml` and `evidence-settings.png`
- `final-standings.md` plus `final-standings.yml` and `evidence-standings.png`
- `playoff-results.md` plus `playoff-results.yml` and `evidence-playoffs.png`
- `draft-results.md` plus `draft-results.yml` and `evidence-draftresults.png`
- `transactions-trades-summary.md`, transaction/trade YAML captures, and evidence screenshots
- `vaqueros-team.yml` and `evidence-vaqueros.png`

## Gaps

- Yahoo's all-teams transaction view exposes Previous 25/Next 25 pagination; `transactions.yml` preserves only the first visible page, not a complete season ledger.
- The Vaqueros-filtered view exposes 19 visible activity rows (Sep 9–Dec 19); Yahoo provides no normalized transaction export here.
- Both the all-teams trade filter and Vaqueros-filtered trade view report “No recent transactions.” This does not establish that no historical trade ever occurred beyond Yahoo's visible archive.
- `final-standings.yml` is Yahoo's direct standings page; the league standings table and championship panel are preserved separately in `standings-league.yml` and the home snapshot.

No lineup, add/drop, trade, or save action was performed; Yahoo access was read-only.
