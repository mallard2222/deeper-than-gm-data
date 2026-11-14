# Weekly usage table — Deeper Than / Vaqueros (yahoo-ff-668216)

Built 2026-11-14 (~5:15 PM CT) by `grok/tools/build_usage_table.py` from public nflverse data. Covers NFL 2026 regular season **W1–W9** (latest fully completed week; W10 had only TNF WAS@NYG when built).

## Rebuild (repeatable)
```
python3 grok/tools/build_usage_table.py --season 2026 --from-week 1 --through-week <N> \
  --players grok/tools/usage_players_yahoo-ff-668216.csv \
  --out grok/intel/yahoo-ff-668216/2026/usage/usage-2026-W01-W<NN>.csv --cache /tmp/nflverse
```
Run after nflverse refreshes the completed week (stats nightly; snap counts usually by Tuesday). Edit the players CSV when the roster or candidate list changes. Each run writes a new dated file; earlier files are kept.

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
| rz_targets, rz_carries | `play_by_play_2026.csv.gz`: plays with `yardline_100 <= 20`; targets = pass attempts with receiver id (no sacks), carries = rush attempts (no QB kneels); 2-pt tries and penalty-nullified plays (`play_type == no_play`) excluded. |
| record_status | `ok`, or which source had no row (`no_stats_row`, `no_snap_row`) |
| source, collected_at | provenance + CT build timestamp |

## Nulls (missing ≠ zero)
- A week with `no_stats_row;no_snap_row` means nflverse has no record (bye, inactive, injured, not yet on a roster). The reason is **not inferred**; all numeric fields are null.
- `no_stats_row` with a snap row (e.g. Rice W4, 6 snaps) = played but no recorded offensive stat; targets/carries left null rather than zero-filled. RZ counts are filled (0) whenever the player has any game record, because they come from play-level data.
- `routes` null everywhere.
- QBs: target/rz_target fields are 0 by construction where present; usage for QBs is mainly snaps/carries.

## Sources
- https://github.com/nflverse/nflverse-data/releases/tag/stats_player
- https://github.com/nflverse/nflverse-data/releases/tag/snap_counts
- https://github.com/nflverse/nflverse-data/releases/tag/pbp
- https://github.com/nflverse/nflverse-data/releases/tag/players
- https://github.com/dynastyprocess/data (db_playerids.csv, Yahoo id crosswalk)

Analysis: [analysis-W10.md](./analysis-W10.md).
