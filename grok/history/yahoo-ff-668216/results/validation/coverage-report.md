# Deeper Than (yahoo-ff-668216) — coverage report

Generated 2026-11-01T14:54:30-06:00. Seasons covered: 2013–2025 complete; 2026 in progress. Nothing below is inferred; anything not captured is listed as missing.

## Matchups

- 2013–2025: 64 games/season (weeks 1–16), all final. 2026: weeks 1–7 final (28 games); Week 8: **in_progress** (last game Mon Nov 2, 2026; snapshots in `matchups/snapshots/`, excluded from records).
- Standings reconciliation (W-L-T, PF, PA vs Yahoo standings, regular season): 112/112 team-seasons match.
- Playoff categories standardized: `category` (regular_season / championship_bracket / consolation) + `round` (regular_season / semifinal / final / third_place / consolation_round). Original labels kept in `bracket_source` and `playoff_game_source`. Third-place games are championship_bracket in every season (2017–2025 source rows had them as consolation).

## Drafts (`drafts/{season}-draft-results.csv`)

| Season | Picks | Rounds | Complete grid |
|---|---|---|---|
| 2013 | 160 | 20 | yes |
| 2014 | 176 | 22 | yes |
| 2015 | 176 | 22 | yes |
| 2016 | 176 | 22 | yes |
| 2017 | 176 | 22 | yes |
| 2018 | 176 | 22 | yes |
| 2019 | 176 | 22 | yes |
| 2020 | 176 | 22 | yes |
| 2021 | 176 | 22 | yes |
| 2022 | 176 | 22 | yes |
| 2023 | 176 | 22 | yes |
| 2024 | 176 | 22 | yes |
| 2025 | 160 | 20 | yes |
| 2026 | 160 | 20 | yes |

## Transactions (`transactions/`) and trades (`trades/`)

All pages of the league-wide list (filter=all) paginated until Yahoo showed no "Next 25". Reconciliation: Yahoo Managers-page **Moves** = add transactions (add or add/drop) excluding commissioner adds; **Trades** = executed trades the team was in.

| Season | Pages | Transactions | Dupes removed | Trades | Kinds | Moves match (teams) | Trades match (teams) |
|---|---|---|---|---|---|---|---|
| 2013 | 11 | 256 | 0 | 21 | add+drop:199, drop:17, trade:21, add:19 | 8/8 | 8/8 |
| 2014 | 13 | 320 | 0 | 11 | add+drop:272, drop:21, add:12, trade:11, vetoed_trade:1, trading_list:3 | 8/8 | 8/8 |
| 2015 | 9 | 207 | 0 | 3 | add+drop:196, trade:3, add:4, drop:4 | 8/8 | 8/8 |
| 2016 | 9 | 202 | 0 | 5 | add+drop:196, trade:5, trading_list:1 | 8/8 | 8/8 |
| 2017 | 11 | 252 | 0 | 5 | add+drop:241, add:3, drop:3, trade:5 | 8/8 | 8/8 |
| 2018 | 10 | 229 | 0 | 6 | add+drop:213, add:5, drop:5, trade:6 | 8/8 | 8/8 |
| 2019 | 8 | 189 | 0 | 4 | add+drop:181, trade:4, add:1, drop:1, trading_list:2 | 8/8 | 8/8 |
| 2020 | 10 | 249 | 0 | 1 | add+drop:219, drop:14, add:15, trade:1 | 8/8 | 8/8 |
| 2021 | 12 | 284 | 0 | 0 | add+drop:241, drop:24, add:19 | 8/8 | 8/8 |
| 2022 | 10 | 231 | 0 | 2 | drop:5, add:2, add+drop:222, trade:2 | 8/8 | 8/8 |
| 2023 | 9 | 204 | 0 | 2 | add+drop:196, drop:4, trade:2, add:1, trading_list:1 | 8/8 | 8/8 |
| 2024 | 9 | 202 | 0 | 3 | add+drop:186, drop:7, add:6, trade:3 | 8/8 | 8/8 |
| 2025 | 9 | 210 | 0 | 4 | add+drop:175, drop:13, add:17, trade:4, trading_list:1 | 8/8 | 8/8 |
| 2026 | 5 | 111 | 0 | 1 | add+drop:100, add:7, drop:3, trade:1 | 8/8 | 8/8 |

Differences explained: drop-only moves are not counted by Yahoo's Moves counter; one 2013 commissioner add (Good Strongs, Geno Smith, Sep 1) is excluded by Yahoo; 'Added to Trading List' entries and the 2014 vetoed trade (Nov 3) appear in the list but are not moves/trades. The 2014 vetoed trade showed as two leg rows and was merged into one record. Trades: 68 executed (396 asset rows: 258 players, 138 draft picks). No FAAB or other assets appear in any trade. Dates show month/day/time only; the year is inferred from the season (`datetime_local_inferred`).

## Weekly rosters (`rosters/{season}-weekly-rosters-actual.csv` and `-projections.csv`)

One team page per team per week (`/{season}/f1/{lid}/{team}/team?week=N`). Actual points and Yahoo projections are in separate files. Validation: the sum of starter actual points must equal that team's matchup score.

| Season | Team-weeks expected | Captured & validated | Score mismatch | Inaccessible / no rows | Not collected |
|---|---|---|---|---|---|
| 2013 | 128 | 128 | 0 | 0 | 0 |
| 2014 | 128 | 128 | 0 | 0 | 0 |
| 2015 | 128 | 128 | 0 | 0 | 0 |
| 2016 | 128 | 128 | 0 | 0 | 0 |
| 2017 | 128 | 128 | 0 | 0 | 0 |
| 2018 | 128 | 128 | 0 | 0 | 0 |
| 2019 | 128 | 128 | 0 | 0 | 0 |
| 2020 | 128 | 128 | 0 | 0 | 0 |
| 2021 | 128 | 128 | 0 | 0 | 0 |
| 2022 | 128 | 95 | 33 | 0 | 0 |
| 2023 | 128 | 95 | 33 | 0 | 0 |
| 2024 | 128 | 106 | 22 | 0 | 0 |
| 2025 | 128 | 116 | 12 | 0 | 0 |
| 2026 | 64 | 56 | 0 | 0 | 8 |

**Cause of roster score mismatches (2022–2025), checked 2026-11-01 on 2022 t1 w7:** Yahoo's historical team page marks some started players as "Bye" in weeks when they actually played (e.g. Davante Adams, 2022 Week 7). For those rows it omits the fantasy-points cell, so `actual_points` is blank and the starter sum falls short of the official matchup score. Those rows are kept as captured, with blank points. The missing points were NOT inferred. Recovering them would need a different source, such as the matchup page or player game logs. The matchup scores themselves are unaffected and still reconcile 100% to standings.

## Remaining gaps (exact)

- 2026 Week 8 matchups not final (4 games in_progress); 2026 Weeks 9–16 not yet played.
- 2026 Week 8 rosters not archived (the live week renders different markup; capture after the games are final). 2026 Weeks 9–16 not played.
- 2022 rosters: t1 w7 (captured_score_mismatch), t1 w9 (captured_score_mismatch), t1 w10 (captured_score_mismatch), t1 w14 (captured_score_mismatch), t2 w7 (captured_score_mismatch), t2 w8 (captured_score_mismatch), t2 w9 (captured_score_mismatch), t2 w14 (captured_score_mismatch), t3 w6 (captured_score_mismatch), t3 w7 (captured_score_mismatch), t3 w8 (captured_score_mismatch), t3 w14 (captured_score_mismatch), t4 w6 (captured_score_mismatch), t4 w9 (captured_score_mismatch), t4 w10 (captured_score_mismatch), t4 w14 (captured_score_mismatch), t5 w6 (captured_score_mismatch), t5 w8 (captured_score_mismatch), t5 w9 (captured_score_mismatch), t5 w10 (captured_score_mismatch), t5 w13 (captured_score_mismatch), t6 w6 (captured_score_mismatch), t6 w7 (captured_score_mismatch), t6 w9 (captured_score_mismatch), t6 w14 (captured_score_mismatch), t7 w7 (captured_score_mismatch), t7 w8 (captured_score_mismatch), t7 w9 (captured_score_mismatch), t7 w14 (captured_score_mismatch), t8 w7 (captured_score_mismatch), t8 w9 (captured_score_mismatch), t8 w10 (captured_score_mismatch), t8 w14 (captured_score_mismatch)
- 2023 rosters: t1 w6 (captured_score_mismatch), t1 w9 (captured_score_mismatch), t1 w11 (captured_score_mismatch), t2 w6 (captured_score_mismatch), t2 w7 (captured_score_mismatch), t2 w10 (captured_score_mismatch), t2 w11 (captured_score_mismatch), t2 w14 (captured_score_mismatch), t3 w5 (captured_score_mismatch), t3 w10 (captured_score_mismatch), t3 w11 (captured_score_mismatch), t3 w13 (captured_score_mismatch), t4 w5 (captured_score_mismatch), t4 w7 (captured_score_mismatch), t4 w9 (captured_score_mismatch), t4 w10 (captured_score_mismatch), t4 w13 (captured_score_mismatch), t5 w6 (captured_score_mismatch), t5 w9 (captured_score_mismatch), t5 w10 (captured_score_mismatch), t5 w13 (captured_score_mismatch), t6 w6 (captured_score_mismatch), t6 w7 (captured_score_mismatch), t6 w9 (captured_score_mismatch), t6 w13 (captured_score_mismatch), t6 w14 (captured_score_mismatch), t7 w7 (captured_score_mismatch), t7 w11 (captured_score_mismatch), t7 w13 (captured_score_mismatch), t7 w14 (captured_score_mismatch), t8 w6 (captured_score_mismatch), t8 w10 (captured_score_mismatch), t8 w13 (captured_score_mismatch)
- 2024 rosters: t1 w12 (captured_score_mismatch), t1 w14 (captured_score_mismatch), t2 w6 (captured_score_mismatch), t2 w12 (captured_score_mismatch), t2 w14 (captured_score_mismatch), t3 w5 (captured_score_mismatch), t3 w10 (captured_score_mismatch), t3 w14 (captured_score_mismatch), t4 w7 (captured_score_mismatch), t4 w10 (captured_score_mismatch), t4 w12 (captured_score_mismatch), t5 w6 (captured_score_mismatch), t5 w11 (captured_score_mismatch), t5 w14 (captured_score_mismatch), t6 w6 (captured_score_mismatch), t6 w12 (captured_score_mismatch), t7 w6 (captured_score_mismatch), t7 w14 (captured_score_mismatch), t8 w6 (captured_score_mismatch), t8 w11 (captured_score_mismatch), t8 w12 (captured_score_mismatch), t8 w14 (captured_score_mismatch)
- 2025 rosters: t1 w8 (captured_score_mismatch), t1 w10 (captured_score_mismatch), t1 w14 (captured_score_mismatch), t2 w6 (captured_score_mismatch), t2 w11 (captured_score_mismatch), t2 w14 (captured_score_mismatch), t3 w6 (captured_score_mismatch), t3 w8 (captured_score_mismatch), t5 w5 (captured_score_mismatch), t5 w9 (captured_score_mismatch), t5 w12 (captured_score_mismatch), t6 w5 (captured_score_mismatch)
- Waiver priority/FAAB bids and per-transaction FAAB amounts are not shown in the league transaction list and were not captured.
