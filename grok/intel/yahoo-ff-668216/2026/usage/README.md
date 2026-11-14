# Weekly usage table — Deeper Than / Vaqueros (yahoo-ff-668216)

Built 2026-11-14 (~5:15 PM CT) by `grok/tools/build_usage_table.py` from public nflverse data. Covers NFL 2026 regular season **W1–W9** (latest fully completed week; W10 had only TNF WAS@NYG when built).

## Rebuild (repeatable)
```
python3 grok/tools/build_usage_table.py --season 2026 --from-week 1 --through-week <N> \
  --players grok/tools/usage_players_yahoo-ff-668216.csv \
  --out grok/intel/yahoo-ff-668216/2026/usage/usage-2026-W01-W<NN>.csv --cache /tmp/nflverse
```
Use a persistent `--cache` dir if you like; it is revalidated every run (see Fix 1). `--offline` uses the cache without network and flags every source `stale_unvalidated`. Run after nflverse refreshes the completed week (stats nightly; snap counts usually by Tuesday). Edit the players CSV when the roster or candidate list changes. Each run writes a new dated file; earlier files are kept.

## Columns
| column | source / rule |
|---|---|
| season, week | nflverse |
| group | `roster` (Vaqueros, Yahoo team 8 as of 2026-11-14) or `candidate` |
| player_name, position | players CSV |
| gsis_id | nflverse / NFL GSIS id (stable key) |
| pfr_id | nflverse players.csv (join key for snap counts) |
| yahoo_player_id | roster: Yahoo team 8 page 2026-11-14; candidates: repo Yahoo evidence or dynastyprocess `db_playerids.csv` (see `yahoo_id_source` in players CSV); empty = not found |
| team, opponent | team that week (Downs shows IND for W1–W9) |
| snaps, snap_pct | `snap_counts_2026.csv` offense snaps / offense pct (PFR-derived) |
| routes | **always null** — routes run are not in nflverse (PFF/NGS paid data not used) |
| targets, carries, target_share | `stats_player_week_2026.csv` |
| game_id | nflverse game id for that player-week (from stats, else snap row) |
| pbp_coverage | `complete`, `no_game_record`, `game_id_unknown`, `pbp_game_missing`, `pbp_partial_missing_team`, `pbp_partial_not_through_final`, `schedule_not_final`, `pbp_game_not_in_schedule` |
| rz_targets, rz_carries | `play_by_play_2026.csv.gz`: plays with `yardline_100 <= 20`; targets = pass attempts with receiver id (no sacks), carries = rush attempts (no QB kneels); 2-pt tries and penalty-nullified plays (`play_type == no_play`) excluded. |
| record_status | `ok`, or which source had no row (`no_stats_row`, `no_snap_row`) |
| source | provenance text |
| stats_retrieved_at, snaps_retrieved_at, pbp_retrieved_at | when that source file was actually downloaded (CT) — **not** the build time |
| sources_validation | per-source result of this run's revalidation (`downloaded_200`, `not_modified_304`, `stale_unvalidated (...)`) |
| built_at | when the CSV was built (CT) |

## Nulls (missing ≠ zero)
- A week with `no_stats_row;no_snap_row` means nflverse has no record (bye, inactive, injured, not yet on a roster). The reason is **not inferred**; all numeric fields are null.
- `no_stats_row` with a snap row (e.g. Rice W4, 6 snaps) = played but no recorded offensive stat; targets/carries left null rather than zero-filled. RZ counts are filled (including 0) only when that game's play-by-play coverage is verified `complete`; otherwise null with the reason in `pbp_coverage`.
- `routes` null everywhere.
- QBs: target/rz_target fields are 0 by construction where present; usage for QBs is mainly snaps/carries.

## Sources
- https://github.com/nflverse/nflverse-data/releases/tag/stats_player
- https://github.com/nflverse/nflverse-data/releases/tag/snap_counts
- https://github.com/nflverse/nflverse-data/releases/tag/pbp
- https://github.com/nflverse/nflverse-data/releases/tag/players
- https://github.com/dynastyprocess/data (db_playerids.csv, Yahoo id crosswalk)

Analysis: [analysis-W10.md](./analysis-W10.md).

## Revision 2026-11-14 ~5:30 PM CT (two fixes)
**Fix 1 — cache revalidation and source times.** Each run sends a conditional GET (`If-None-Match` ETag / `If-Modified-Since`) for every source file. A 200 re-downloads it; a 304 means the server confirmed the cached copy is still current. If the network fails, the cached copy is used but flagged `stale_unvalidated` and keeps its original retrieval time. Per-source `source_retrieved_at`, `source_validated_at`, ETag, Last-Modified and sha256 go into `<output>-sources.json` (here [usage-2026-W01-W09-sources.json](./usage-2026-W01-W09-sources.json)); retrieval times and validation results are also CSV columns, separate from `built_at`. The old `collected_at` column (build time only) is gone.
Tested: first run `downloaded_200` for all five sources (17:30 CT); immediate rerun `not_modified_304`; `--offline` run `stale_unvalidated`.

**Fix 2 — play-by-play coverage before RZ zeros.** For every game the script checks: (a) the game is in the 2026 schedule, (b) pbp has offensive plays for both scheduled teams, (c) pbp runs through the end (an `END GAME` row or clock at 0:00), (d) the schedule has a final score. Only then are RZ counts (including 0) written; otherwise RZ fields are null and `pbp_coverage` says why. Tested by truncating one game (2026_09_NYJ_KC) in a scratch copy: the KC rows became null / `pbp_partial_not_through_final`. Current data: all 258 player-weeks with a game record have `complete` coverage (137 W1–W9 games); the 66 rows with no game record stay null.
