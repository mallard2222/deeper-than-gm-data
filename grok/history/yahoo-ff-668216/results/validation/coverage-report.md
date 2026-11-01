# Deeper Than coverage report
Generated 2026-11-01T12:50:45-06:00 (America/Chicago). Seasons covered: 2013-2025 complete + 2026 weeks 1-7 final (week 8 in progress). NOT all-time (2026 unfinished; see identity caveat).

## Matchups
| Season | Matchups | Status |
|---|---|---|
| 2013 | 64 | matchups_complete_weeks_1_16 |
| 2014 | 64 | matchups_complete_weeks_1_16 |
| 2015 | 64 | matchups_complete_weeks_1_16 |
| 2016 | 64 | matchups_complete_weeks_1_16 |
| 2017 | 64 | matchups_complete_weeks_1_16 |
| 2018 | 64 | matchups_complete_weeks_1_16 |
| 2019 | 64 | matchups_complete_weeks_1_16 |
| 2020 | 64 | matchups_complete_weeks_1_16 |
| 2021 | 64 | matchups_complete_weeks_1_16 |
| 2022 | 64 | matchups_complete_weeks_1_16 |
| 2023 | 64 | matchups_complete_weeks_1_16 |
| 2024 | 64 | matchups_complete_weeks_1_16 |
| 2025 | 64 | matchups_complete_weeks_1_16 |
| 2026 | 32 | in_season_weeks_1_7_final_week_8_in_progress |

Regular season = weeks 1-14; weeks 15-16 split into championship (top 4) and consolation brackets. 2013-2016 bracket labels derived from the 4 playoff teams (Yahoo `*` playoff marker / final rank 1-4) and verified: every week 15-16 pairing stayed within one bracket and each final winner equals Yahoo final rank 1. `playoff_game` marks semifinal/final/third_place/consolation rounds for 2013-2016. Scores are actual points; Yahoo projections are kept only in `raw/captures/` as `proj_*`.

## Reconciliation
0 mismatches: regular-season W-L-T, PF and PA from matchup rows equal Yahoo standings for all 8 teams in every season 2013-2025 and 2026 through week 7. See `validation/standings-reconciliation.csv`.

## Manager identities
Resolved for every season from the Yahoo Managers page; see `identities/managers-by-season.csv` and `identities/manager-identity-findings.md`.

## Completeness audit (drafts, transactions, trades, weekly rosters)

| Season | Draft | Transactions | Trades | Weekly rosters |
|---|---|---|---|---|
| 2013 | complete pick grid captured (all rounds x 8 picks) in 2013/draft-results.yml | PARTIAL: Yahoo Managers page counts 217 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~192+ league moves not archived | Yahoo counter implies ~21 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2014 | complete pick grid captured (all rounds x 8 picks) in 2014/draft-results.yml | PARTIAL: Yahoo Managers page counts 284 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~259+ league moves not archived | Yahoo counter implies ~11 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2015 | complete pick grid captured (all rounds x 8 picks) in 2015/draft-results.yml | PARTIAL: Yahoo Managers page counts 200 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~175+ league moves not archived | Yahoo counter implies ~3 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2016 | complete pick grid captured (all rounds x 8 picks) in 2016/draft-results.yml | PARTIAL: Yahoo Managers page counts 196 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~171+ league moves not archived | Yahoo counter implies ~5 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2017 | complete pick grid captured (all rounds x 8 picks) in 2017/draft-results.yml | PARTIAL: Yahoo Managers page counts 244 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~219+ league moves not archived | Yahoo counter implies ~5 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2018 | complete pick grid captured (all rounds x 8 picks) in 2018/draft-results.yml | PARTIAL: Yahoo Managers page counts 218 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~193+ league moves not archived | Yahoo counter implies ~6 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2019 | complete pick grid captured (all rounds x 8 picks) in 2019/draft-results.yml | PARTIAL: Yahoo Managers page counts 182 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~157+ league moves not archived | Yahoo counter implies ~4 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2020 | complete pick grid captured (all rounds x 8 picks) in 2020/draft-results.yml | PARTIAL: Yahoo Managers page counts 234 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~209+ league moves not archived | Yahoo counter implies ~1 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2021 | INCOMPLETE: 2021/draft-results.yml has the 22-round header but only 8 pick cells and no player links; full draft board needs re-capture | PARTIAL: Yahoo Managers page counts 260 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~235+ league moves not archived | Yahoo counter shows 0 trades — nothing missing | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2022 | complete pick grid captured (all rounds x 8 picks) in 2022/draft-results.yml | PARTIAL: Yahoo Managers page counts 224 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~199+ league moves not archived | Yahoo counter implies ~2 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2023 | complete pick grid captured (all rounds x 8 picks) in 2023/draft-results.yml | PARTIAL: Yahoo Managers page counts 197 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~172+ league moves not archived | Yahoo counter implies ~2 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2024 | complete pick grid captured (all rounds x 8 picks) in 2024/draft-results.yml | PARTIAL: Yahoo Managers page counts 191 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~166+ league moves not archived | Yahoo counter implies ~3 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2025 | complete pick grid captured (all rounds x 8 picks) in 2025/draft-results.yml | PARTIAL: Yahoo Managers page counts 192 moves; history captures only the first 25-row page of All Transactions (+ Vaqueros-filtered page). ~167+ league moves not archived | Yahoo counter implies ~4 trades; captured trades.yml is first visible page only — not asserted complete | MISSING for all teams/weeks; only Vaqueros end-of-season team page snapshot (vaqueros-team.yml / andrew-team-page.yml) |
| 2026 | NOT CAPTURED in history/ (2026 draft results not archived) | PARTIAL: 107 moves on Yahoo; backfill.json holds transactions page snapshots from 2026-11-01 (see daily/.../backfill-2026-10-05_to_2026-11-01) | Yahoo counter implies ~1 trades; captured trades.yml is first visible page only — not asserted complete | Vaqueros weekly lineups weeks 5-8 in backfill.json; weeks 1-4 Vaqueros in daily reports; other 7 teams MISSING |

## Exact remaining gaps
- 2026 weeks 8 (in progress) through 16
- 2021 draft board re-capture
- 2026 draft results not archived
- League-wide transaction logs beyond first 25 rows for every season 2013-2025
- Trade logs beyond first visible page (seasons with >0 trades)
- Weekly rosters for all non-Vaqueros teams, all seasons; Vaqueros weekly rosters for 2013-2025
- 2025 Week 17/18: Yahoo shows no matchups (season ended week 16) — not a gap
