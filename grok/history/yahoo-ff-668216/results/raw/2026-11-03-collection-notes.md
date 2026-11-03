# 2026-11-03 collection notes — 2026 Week 8 finalized

- Matchups: `https://football.fantasysports.yahoo.com/2026/f1/668216?matchup_week=8&module=matchups&lhst=matchups` retrieved 2026-11-03T06:38:25-06:00; section header "Week 8 Matchups Final results". Parsed to `raw/captures/2026/matchups-week-08-final.json` (actual scores in score_*, Yahoo projections in proj_*; projections not used in results).
- Final scores: Vaqueros 137.70 – Good Strongs 163.28; Wet Serapas 162.82 – Deepest 99.82; Baby Arm 137.20 – DUGASM 99.06; Big Balls 170.52 – FFAmuseBouche 142.04.
- The four Week 8 rows in `matchups/2026-matchups.{jsonl,csv}` changed from `in_progress` to `final` (replaced in place, so there are no duplicate games). The earlier in-progress captures are unchanged: `raw/captures/2026/matchups-week-08.json` (2026-11-01T12:40:20-06:00) and `matchups/snapshots/2026-week-08-in-progress-*.json`.
- Standings: `https://football.fantasysports.yahoo.com/2026/f1/668216?module=standings&lhst=stand` retrieved 2026-11-03T06:38:30-06:00, saved to `raw/captures/2026/standings-after-week-08.json`. The regular-season W-L-T, PF, and PA from matchups reconcile 8/8 with that capture.
- Week 8 weekly rosters: team pages `/2026/f1/668216/{team}/team?week=8` were captured for all 8 teams. In all 8, the starter actual-point sums equal the final matchup scores.
