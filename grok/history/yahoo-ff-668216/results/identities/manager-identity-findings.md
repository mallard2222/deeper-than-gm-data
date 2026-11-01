# Deeper Than manager identity findings (2013–2026)

Method: for each season, the Yahoo Managers page `https://football.fantasysports.yahoo.com/{season}/f1/{league_id}/teams` was read (2026-11-01, read-only). Each team row links the manager's Yahoo profile; the **profile handle** is the identity key. Team names and team IDs were not used to infer continuity. Parsed data (no emails) in `raw/captures/managers-all-seasons.json`; table in `managers-by-season.csv`.

## James / Wet Serapas 2021 — VERIFIED
2021 league 771925, team 1 "Wet Serapas": manager link text **James**, profile handle **james396127**, flagged Commissioner. Same handle manages Wet Serapas in every season 2013–2026. Confidence: high (direct Yahoo manager record, not inferred).

## Manager handles
| Manager | Handle | Teams / seasons |
|---|---|---|
| Andrew Allard | andrewallard1 | Vaqueros 2013–2026 |
| James | james396127 | Wet Serapas 2013–2026 |
| Jeremy | jeremy82341 | Deepest 2013–2026 |
| Tyler | tyler156834 | Dezbians 2013–2023 (not in league 2024+) |
| Ryan | ryan512974 | DUGASM 2013–2026 |
| Jonah | jonah11636 | FFAmuseBouche 2013–2026 |
| Framp | framp5 | Good Strongs 2013–2026 |
| Brad | brad95652 | bigballs 2013–2021 |
| Brandon | brandon128978 | Bigballs 2022–2023 (team 2), Baby Arm 2024–2026 |
| Brad | brad58794 | Big Balls 2024–2026 |

## Caveats
- The two "Brad" profiles are different Yahoo accounts; no evidence links them, so they stay separate in H2H. If Andrew confirms they are the same person, merge keys.
- "Bigballs" in 2022–2023 was Brandon, so the prior Vaqueros-vs-"Big Balls" name-based H2H mixed two managers.
- The Managers page reflects the manager of record at season end; mid-season ownership changes would not show.
- Yahoo team IDs are reassigned each season (e.g., Vaqueros was team 2 in 2013, 4 in 2014, 7 in 2015, 8 from 2016).
