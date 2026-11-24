# Sources — W12 Tuesday desk 2026-11-24 (retrieved 08:00–08:15 CT)

| # | source | published | retrieved (CT) | class / use |
|---|---|---|---|---|
| 1 | Yahoo league 668216 team 8 page (cookie-jar curl) | — | 08:00:33, ~08:01 | **FAILED** 302 → login (see yahoo-access-attempt.txt) |
| 2 | nflverse-data releases: stats_player_week_2026.csv, snap_counts_2026.csv, play_by_play_2026.csv.gz, players.csv, schedules/games.csv | nflverse nightly (W11 incl. MNF CIN@WAS present; W11 pbp 13/13 games) | 08:00:59–08:01:04 (304 revalidated 08:0x) | public stat feed (unofficial); usage table + league-scored points |
| 3 | nflverse-data stats_team/stats_team_week_2026.csv | nightly | ~08:02 | DEF scoring inputs |
| 4 | dynastyprocess db_playerids.csv (GitHub) | — | ~08:02 | Yahoo↔GSIS id map (2026 rookies missing → name+position fallback, flagged `gsis_match`) |
| 5 | ESPN injuries JSON (site.api.espn.com …/nfl/injuries) | entries 2026-11-15…11-24 UTC | 08:03 | secondary; extract in espn-injury-feed-extract.txt (LaPorta ankle limited Mon walkthrough — new; Hurleman reverted to PIT practice squad — new) |
| 6 | AP NFL injury report (apnews.com/article/nfl-injury-report-f76ea0ed77b9646f964071c1972d7ceb) | W12 Mon estimates | ~08:10 | official-league text via AP: KC DNP Walker (groin), Gray, Moore, VanSumeren; FULL Rice (knee), Mahomes |
| 7 | heavy.com (Chiefs) quoting OC Bieniemy 11/23 ("Kenneth is the starter. If Kenneth is to play, he'll remain the starter") | 11/23 1:49 PM / 9:40 PM | ~08:10 | secondary quoting coach on record |
| 8 | CBS Sports / RotoWire (Jacobs not expected to play Wed; Kaleb Johnson lead early-down) — cbssports.com/fantasy/football/news/packers-josh-jacobs-practicing-but-not-expected-to-play-wednesday/ | 11/23 12:05 PM CT | ~08:10 | secondary citing LaFleur / Bill Huber |
| 9 | NBC Sports (Denver Post Parker Gabriel): Harvey "widely expected" to practice when first eligible (W13) | 11/23 | ~08:11 | secondary citing beat |
| 10 | Broncos Wire: Harvey eligible W13; misses W12 | 11/24 6:01 AM MT | ~08:11 | secondary |
| 11 | Repo: W10-2026-11-10/roster.csv, waivers.csv, standings.csv, settings.json; transactions extract 2026-11-14; ledger-2026.csv; 2026-matchups.csv (W1–W8) | Yahoo captures 11/10, 11/14 | — | last-known Yahoo state (STALE: 10–14 days) |

Quarantined / not used as evidence: SI/Verdexed fantasy opinion pieces (used only as pointers), sportcrow/exa aggregator injury tables, earlier Grok recommendations (not independent evidence).
