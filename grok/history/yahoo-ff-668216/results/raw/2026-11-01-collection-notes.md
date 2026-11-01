# Collection 2026-11-01 (America/Chicago)

Read-only Yahoo web pages via logged-in curl, ~6 s throttle, no 429/999 encountered.
- Matchups: `/{season}/f1/{league_id}?matchup_week=N&module=matchups&lhst=matchups` for 2013–2015 weeks 1–16, 2016 weeks 15–16, 2026 weeks 1–8.
- Standings: `?module=standings&lhst=stand` all seasons 2013–2026.
- Managers: `/{season}/f1/{league_id}/teams` all seasons (handles + Moves/Trades counters; emails dropped).
- 2016 week 15 re-capture matched existing rows exactly; week 16 appended.
- 2026 weeks 1–8 rebuilt from captures; weeks 5–7 match `daily/yahoo-ff-668216/2026/backfill-2026-10-05_to_2026-11-01/backfill.json` exactly; week 8 marked `in_progress`, winner null.
- Raw HTML was not retained; only parsed JSON in `raw/captures/`.
