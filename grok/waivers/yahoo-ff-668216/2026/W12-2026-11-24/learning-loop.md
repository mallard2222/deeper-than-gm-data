# Learning loop: W12 package (2026-11-24 CT)

Earlier recommendations, forecasts and execution records are **unchanged**; this file only adds outcomes. All points are **computed league-scored points** from public nflverse stats (`grok/tools/league_points.py`, validated 143/144 vs Yahoo W9 actuals; see `evidence/scoring-validation.md`). They are **not Yahoo-official**. Official W10/W11 matchup scores are **unknown** because Yahoo has been blocked since 11/15. Lines marked **hindsight** use information that wasn't available at decision time.

## 1-week horizon
### W10 (vs Wet Serapas)
- **Started lineup**, verified on Yahoo 11/14 ~5:50 PM CT after the approved Marks swap: Love 10.80, Mendoza 13.92, Henry 16.50, CMC 44.30, Collins 19.90, Golden 9.50, Warren 1.40, McMillan (W/T) 5.00, Marks (W/R) 7.00, Gay 8.00, WAS DEF 5.00. **Computed total 141.32.** It's unverified whether anything changed between 11/14 and Sunday's locks.
- **Opponent:** Wet Serapas's Tuesday 11/10 lineup computes to ≥160.78, with Barkley missing from the data and their K/DEF swapped 11/11. **Result: very likely L** (consistent with the 11/16 daily). Official result unknown.
- **Marks → W/R, Rice → BN (approved 11/14, ledger 2026-W10-05):** Marks 7.00 vs Rice 10.70, so **−3.70** (hindsight). Pre-game reasoning was a Montgomery absence and RB volume. Marks got 12 carries on 45% of snaps, so the opportunity showed up but the efficiency didn't. **Sound but unlucky / small sample.**
- **Worthy add / Freiermuth drop (approved 11/14, ledger 2026-W10-06):** Worthy 0.00 W10 (bench; 88% snaps, 3 targets) and 10.80 W11 (lineup use unknown). Freiermuth 10.50 W10 and 6.50 W11 (5 targets, 1 RZ target). Over one week, the dropped player outscored the added one by 10.5 → 6.5 − 10.8. The TE slot was never short (Warren/LaPorta), so the **lineup impact is about 0**. Verdict: too early.
- **Mendoza $30 (Andrew-directed W10 claim):** 13.92 in W10 as the QB2 started for bye-week Caleb. The alternatives in hindsight were Brissett (lost at $21 to FFAmuseBouche) 11.80 and Penix (cancelled) 12.34. W11: **22.88** (3 TD; lineup use unknown). **The decision looks good** on production and keeper intent (keeper rules unknown).

### W11 (vs Deepest, inferred)
- **Started lineup unknown** (Yahoo blocked). Computed W11 values for our players: Mendoza 22.88, Caleb 14.34, Nix 11.50, Henry 17.10, CMC 13.20, Collins 13.30, McMillan 16.10, Worthy 10.80, Rice 8.30, Downs 7.90, LaPorta 7.70, Odunze 6.50, Warren 2.70, Gay 6.00, WAS DEF 7.00 (approx). Love, Golden and Judkins were on bye. Marks was OUT, and Robinson was on NFL IR.
- If the lineup followed the dailies (Mendoza + Nix at QB, Rice WR2, Marks moved out of W/R before TNF): a W/R fill of Odunze/Downs/Worthy gives roughly **124.6–128.9** (add 2.84 if Caleb started instead of Nix). If Marks stayed in W/R (0), the total is about **118.1**. **Unverified scenario range**, not a result.
- **QB2 call (11/21–11/23 dailies leaned Nix over Caleb for weather):** Caleb 14.34 vs Nix 11.50, a **−2.84 hindsight** gap if Nix started. The reasoning (CHI rain 84%) was documented. **Sound process with an adverse outcome**, one-week sample.
- **WR2 call (Rice > Downs > Odunze):** Rice 8.30, Downs 7.90, Odunze 6.50. The ranking held, but the margins were small. **Worthy (10.80) beat all three (hindsight).**

## ~4-week horizon (W8–W11)
- **Results:** W8 L 137.70–163.28 (Good Strongs), W9 W 160.52–140.72 (Big Balls), W10 likely L (computed 141.32), W11 unknown. Record is about 3-7 or 4-7 (unverified).
- **FAAB:** $79 (11/3) → $64 (W9 Washington $15) → **$34** (W10 Mendoza $30). Nothing spent since (last read 11/14). Total 2026 spend is **$66**: Downs $18, Packers DEF $3, Washington $15, Mendoza $30.
- **Mike Washington Jr. ($15, W9; actor FF GM; approval received but text unknown, per ledger 2026-W09-01):** −0.30 in W9 (bench), then dropped 11/11. Since the drop: W10 3.20, W11 4.20 (21–29% snaps). **Lineup contribution: 0. Outcome poor.** The bet was on Jeanty-injury upside, and that contingency didn't happen. The price was high for a contingency RB in an 8-team league. **Lesson (not hindsight):** cap contingency-only RB bids at about 10% of the remaining budget unless the role is already confirmed.
- **Downs ($18, W03):** last 4 games averaged 8.85 (W8–W11). Snap share since the KC trade is 17–24%. Mostly bench. Now a drop candidate.
- **Dropped-player tracking:** Freiermuth (see above). Washington (above). Earlier October moves are still unreconciled (FAAB ledger note).

## Forecast errors
- No Yahoo projections were captured for W10/W11, so a projection-error calculation isn't possible. The 11/16 daily's W10 estimate (≈124 + Henry + DEF ≈ 145.5) vs the computed 141.32 gives an error of about **−4**, after correcting for the DEF having already played.

## Calibration notes for W12+
- Henry: 16.50 and 17.10 in W10–W11, with 49–55% of snaps. The "Yahoo projection optimistic" caution from W9 didn't hold in the last two weeks (small sample).
- Warren under Richardson: 1.40 and 2.70 (14–19% target share). Treat as a TE floor play only.
- CMC: 13.20 in W11 after 44.30 in W10. His snap share held at 60–65%.
