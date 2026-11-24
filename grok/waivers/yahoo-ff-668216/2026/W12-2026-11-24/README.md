# Deeper Than W12 Tuesday intelligence desk — 2026-11-24 (CT) — PARTIAL (Yahoo auth failed)

- **Run id:** intel-yahoo-ff-668216-2026-W12-2026-11-24-001. Scheduled fire ~7:57 AM CT. Collection and analysis ran 8:00–8:20 AM CT.
- **League:** yahoo-ff-668216 (Deeper Than), team 8 Vaqueros. **NFL week:** W11 is complete (MNF CIN 20 @ WAS 22 final 11/23). **W12 is upcoming** and runs Wed 11/25 to Mon 11/30, with no byes.
- **Status: PARTIAL. Yahoo FAILED.** 302 to login at 8:00:33 AM CT. The browser-equivalent noprompt redirect ended on the Yahoo sign-in page. That's two requests total, with no login and no circumvention, and it is the **13th consecutive Yahoo failure**. See `evidence/yahoo-access-attempt.txt`.
  - **Needed:** Andrew signs in to Yahoo in the box browser, then the desk can be re-run read-only before the waiver run.
- **No Yahoo claims, bids, drops, IR moves, trades or lineup changes were made.**

## Not collected from Yahoo (UNKNOWN, not zero)
Current rosters of all 8 teams, starters/bench/IR, injury tags, standings, official W10/W11 scores, FAAB balances, waiver order, transactions since 11/14 5:10 PM CT, FA pool and pagination, pending claims, Yahoo projections, settings re-verification.

## Last-known Yahoo state used instead (STALE, labelled)
- **All-team rosters:** W10 capture from 11/10 ~8:0x AM CT, plus 17 transactions from the 11/14 ~5:10 PM CT extract. File: `data/rosters-lastknown-all-teams-with-league-points-W01-W11.csv` (`roster_basis` column per row). Yahoo IDs are stable. GSIS mapping uses Yahoo id where available, otherwise name+position (`gsis_match`).
- **FA pool:** 11/10 FA/W list (336 rows, as paged then), minus 11/11–11/14 adds, plus 11/11–11/14 drops. File: `data/fa-pool-lastknown-with-league-points.csv`. Current status is unknown for every row.
- **Standings / FAAB / waiver order:** as of 11/10 (`W10-2026-11-10/standings.csv`). FAAB as of 11/11: DUGASM $56, Big Balls $4, Wet Serapas $67, Baby Arm $65, Good Strongs $22, Deepest $92, Vaqueros **$34**, FFAmuseBouche $69. W9 waiver priority: FFAmuseBouche 1 … DUGASM 8 (rolling).
- **Rules (Yahoo settings 11/10, not re-verified today):**
  - Scoring: 0.5 PPR; 4-pt pass TD; −2 INT/FL.
  - Roster: QB, QB, WR, WR, RB, RB, TE, W/T, W/R, K, DEF, **BN×9**, IR×1. The bench-slot 8-vs-9 question is resolved: settings and the roster count both show 9 BN.
  - Waivers: FAB, weekly game-time–Tuesday, 1-day waiver time; processing seen Wed ~3:42–3:53 AM.
  - Trades: end date Nov 28, 2-day reject window, commissioner review.
  - Playoffs: 4 teams, W15–16.
  - **Keepers and traded picks: UNKNOWN** (not on the settings page).

## Collected this run (public)
- **nflverse W1–W11** (stats, snaps, play-by-play including MNF; W11 PBP 13/13 games):
  - Usage table `grok/intel/yahoo-ff-668216/2026/usage/usage-2026-W01-W11.csv`: 42 players × 11 weeks. Routes are always null. Red-zone is filled only where PBP coverage is complete.
  - League-scored points for every last-known rostered player and FA (new tool `grok/tools/league_points.py`, validated 143/144 vs Yahoo W9 actuals).
- **ESPN injuries feed (8:03 AM CT), AP official W12 Monday estimates, coach quotes via secondary sources.** See `evidence/sources.md`.

## Headlines
1. **The Emmett Johnson waiver plan from 11/23 is superseded.** Last Yahoo evidence (11/10) has him on **Good Strongs' bench**, so he's trade-only unless Yahoo shows a drop. The KC OC says Walker remains the starter when healthy; Walker was DNP on Monday's estimate.
2. **Best W12 add (docs only): Kaleb Johnson (GB RB), $3–8, drop Wan'Dale Robinson.** Jacobs is not expected to play Wednesday. FFAmuseBouche (our inferred W12 opponent) owns Jacobs and had the most FAAB plus likely top priority. WR alternatives: Caleb Douglas (target share 25%→30%) or Ted Hurst III. See `RECOMMENDATION.md`.
3. **Playoff odds are very low (inference).** We were 3-6 after W9, W10 was likely a loss, and the top three teams play each other W12–14. Weigh keeper/2027 value, but keeper rules are unknown. The trade window closes **Sat 11/28**.
4. **Lineup risks for W12:**
   - **LaPorta** (ankle) was limited Monday. New.
   - **Marks** is still in the concussion protocol.
   - **Warren** is producing very little (3.6 pts/g over his last 4 games).
   - **Wan'Dale Robinson** is a dead bench spot.
   - Early locks start Wed 7:00 PM CT (Love, Golden), then Thu noon (Caleb, Odunze, LaPorta) and Thu 7:20 PM (Rice, Downs, Worthy).
5. **W12 opponent, inferred from the schedule rotation:** FFAmuseBouche. Burrow is averaging 30.5 pts over his last 4 games.
6. **Harvey** can practice in W13 (expected to). His Yahoo IR slot will need a decision then.
7. **Hurleman reverted to the PIT practice squad.** He's off the watchlist.

## Files
- `RECOMMENDATION.md`: options A / A-alt / B / C (trade) / Hold, the W12 lineup table and deadlines.
- `learning-loop.md`: 1-week and ~4-week reviews (W10 computed 141.32, likely L; Washington, Mendoza, Worthy, Marks swap).
- `weekly-package.json`: structured summary.
- `data/`: last-known rosters and FA pool with W1–W11 league points; W12 points-allowed-by-position matchup table; the league-points subset.
- `evidence/`: the Yahoo attempt, sources, ESPN injury extract, scoring validation.
