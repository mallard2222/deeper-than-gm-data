# W10 weekly package: Deeper Than (`yahoo-ff-668216`) / Vaqueros, 2026-11-10

- **Run id:** `intel-yahoo-ff-668216-2026-W10-2026-11-10-001`. Routine automation `42c782ff-cae1-5af6-a771-a1a964d6d0a0`, fired 2026-11-10T13:59:50Z (7:59:50 AM CT).
- **Collection:** Yahoo 8:01:23–8:06:48 AM CT including 4 Vaqueros player-list pages, 59 pages, every one HTTP 200. Read-only cookie-jar curl with 2 s spacing; no writes to Yahoo. Web news ~8:08–8:20 AM CT.
- **State:** W9 **won** 160.52–140.72 → 3-6 (6th). FAAB $64, priority 3, BN 9/9, IR 1/1 (Harvey), 0 open spots. W10 vs Wet Serapas: Yahoo 122.92 (QB2 = Caleb Williams **BYE**) vs 130.65.
- **No Yahoo actions were taken.**

## Files
- [RECOMMENDATION.md](RECOMMENDATION.md): QB2 claim plan (Brissett $5–9, Penix $2–4 fallback, Wed FA floor), drop Freiermuth, lineup notes, hold option, deadlines
- [research.md](research.md) (reports) · [opponents.md](opponents.md) · [learning-loop.md](learning-loop.md)
- [roster.csv](roster.csv): all 8 rosters (167 rows) with Yahoo IDs, W10 slot/game/proj/injury tags, W9 slot/actual/proj. Vaqueros rows also carry bye, ROS, N4W, L4W and season points
- [standings.csv](standings.csv) · [settings.json](settings.json) · [waivers.csv](waivers.csv) (335 unique FAs from 26 list pages)
- [weekly-package.json](weekly-package.json): structured summary · [source-manifest.json](source-manifest.json)
- [evidence/](evidence/): text extracts of every page (emails redacted), `MANIFEST.json` (raw HTML SHA-256, URL, HTTP code, retrieval time), `fetchlog.txt`

## Coverage
| Item | Status |
|---|---|
| Rosters 8/8 (W10 and W9 views), slots, injury tags, projections | collected. W9 starters reconcile exactly with scoreboard finals for all 8 teams. W10 starter sums reconcile with the scoreboard projections for all 4 matchups. TNF/dome tooltip rows were recovered from page text (flagged in `parse_note`) |
| Standings, FAAB, waiver priority, moves | collected (league home table, "Last standings update: Tue Nov 10 02:15am CST") |
| W9 final scores / W10 matchups | collected |
| Transactions | collected. New since Nov 4: FA adds only (Rodgers, Omar Cooper, Shedeur, Malik Washington, Sampson, Butker, Pineiro) plus the Penix $0 waiver (FFAmuseBouche, Nov 6). Only one league trade all season (Oct 1) |
| Pending claims (any team) | **unknown**. The waivers/pending filters return "No recent transactions", and Vaqueros' team page shows no waiver panel |
| FA pool | see research.md; deeper pages not fetched (top-50 QB, top-25 other positions by W10 proj) |
| Snaps, routes, targets, red zone | **not collected from Yahoo**; third-party reports only where cited |
| Keeper rules, traded picks | **unknown** (not on the settings page) |
| Exact waiver processing clock | **unknown** (Yahoo "W (Nov 11)"; past ~3:42–3:46 AM) |
| Downs NFL trade | pending at collection (deadline 3 PM CT) |
| W11–W14 opponents | inferred from rotation, not verified |
