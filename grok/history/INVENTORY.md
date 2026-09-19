# Yahoo Fantasy Football history inventory (read-only)

Account context: Andrew Allard's signed-in Yahoo Fantasy session. Checked Friday Sep 18, 2026 (UTC-5). No transactions were submitted or saved.

## How Yahoo exposes history

The current league home has a season combobox showing 2026 through 2005. Selecting a season changes the route to a season-specific league ID. The historical home exposes standings tabs (Standings, Schedule, Playoffs, Ratings & Levels, All Time), a transactions view (All Transactions, Added Players, Dropped Players, Trades, FAB Offers), and a Draft Results page. Settings is available by the season-specific `/settings` route.

Important separation: Deeper Than's custom route is `/league/deeperthan/<year>` for 2013–2025. For 2012 and earlier, that same custom route resolves to the separate  lineage (for example, 2012 displays ` (ID# 12800)`), so those years are not counted as Deeper Than.

## Deeper Than — current ID 668216; custom URL `/league/deeperthan`

All rows below were opened at the season custom home and showed the stated year/name/ID. `UI pages exposed` means the season home/UI exposes Home, Settings, Standings/Schedule/Playoffs tabs, Transactions, and Draft Results; the 2025 sample folder contains the deep captures. Older rows were not exhaustively downloaded.

| Season | Season league ID | Name shown | Andrew team/manager | UI pages exposed |
|---|---:|---|---|---|
| 2025 | 153816 | Deeper Than | Vaqueros — Andrew Allard (team /8 confirmed) | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results |
| 2024 | 181730 | Deeper Than | Vaqueros — team /8 title confirmed | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results |
| 2023 | 69639 | Deeper Than | Vaqueros — team /8 title confirmed | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results |
| 2022 | 59165 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2021 | 771925 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2020 | 26564 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2019 | 56453 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2018 | 16765 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2017 | 122934 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2016 | 79234 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2015 | 1044 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2014 | 76443 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |
| 2013 | 11558 | Deeper Than | Team route not separately deep-opened | Home; Settings; Standings; Schedule; Playoffs; Transactions; Draft Results exposed by UI |

### Deeper Than gaps / non-membership

- 2012–2005 are not Deeper Than seasons in the accessible custom history. Those routes resolve to a different Yahoo league lineage and are not counted as Deeper Than.
- 2026 is the current season, not a prior season; current league ID is 668216.
- For non-sample Deeper Than years, this inventory records the accessible home/selector and exposed page families, not a full content download of every page.

## Source URL patterns

- Current Deeper Than: `https://football.fantasysports.yahoo.com/f1/668216`
- Deeper Than historical: `https://football.fantasysports.yahoo.com/<YEAR>/f1/<SEASON_ID>`
