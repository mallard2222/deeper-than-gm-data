# Scoring validation — grok/tools/league_points.py vs Yahoo actuals (2026-11-24 ~08:05 CT)

Method: computed W9 league-scored points from nflverse `stats_player_week_2026.csv` / `stats_team_week_2026.csv` / `games.csv`
(retrieved 2026-11-24 08:00:59–08:01:04 CT; stats_team + dynastyprocess db_playerids ~08:02 CT) and compared them with the Yahoo
`w9_actual` column of the W10 all-team roster capture (`W10-2026-11-10/roster.csv`, Yahoo 2026-11-10 ~08:0x CT).

- Players and DEFs with a Yahoo W9 actual: **144**. Matches within ±0.05: **143**. Includes all 9 DEF rows (points-allowed tiers from final score matched every one).
- One mismatch: Rachaad White (WAS RB), Yahoo 5.90 vs computed 7.90 (+2.00). This could be a 2-pt or fumble attribution difference between the sources. It's unresolved; treat single-player values as ±2 when it matters.
- A player with no nflverse stat row is NULL, not 0. Yahoo shows 0.00 for inactive/bye players, and the comparison above counts those as matches only where nflverse also has no row.
- DEF caveat: points allowed = the opponent's final score. Yahoo may exclude defensive/ST TDs scored by the opponent, so DEF values are labelled `DEF_approx`.
- K: FG 0–39 = 3, 40–49 = 4, 50+ = 5; missed FG 0–19 −2, 20–29 −1; PAT +1, missed PAT −1 (settings captured 2026-11-10).

Conclusion: computed points reproduce Yahoo scoring closely enough for W10/W11 actuals while Yahoo is unreachable. They are **not** Yahoo-official. Official matchup scores remain unknown until Yahoo is read.
