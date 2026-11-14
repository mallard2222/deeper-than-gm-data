# Pregame lineup-check routine — status as of 2026-11-14 (CT)

Source for routine settings: FF GM's inspection of the live routine configuration on 2026-11-14 (FF GM conversation/action history). This sub-task could not open the routine store directly; settings below are as reported by FF GM. Kickoff times were verified independently (below).

## Configuration
| Item | Value |
|---|---|
| Status | **Enabled** |
| Schedule | Hourly Sun, Mon, Thu 10:54 AM–8:54 PM CT — cron `54 10-20 * * 0,1,4` (America/Chicago) |
| Next run | **Sun 2026-11-15 10:54 AM CT** |
| Delivery | Reports to FF GM, who relays actionable alerts to Andrew's Grok Bot chat. Not a direct message to Andrew. |
| Authority | Read/check only. May make a current-week start/sit swap only under the standing OUT/IR/bye rule; anything else requires Andrew's explicit approval. |

Other routines (as reported by FF GM, CT): daily report every day 4:54 PM; Tuesday desk Tue 7:54 AM; Wednesday reconcile Wed 7:54 AM; Finalize Week 8 one-time (paused; already ran). The older [workflow-schedule.md](./workflow-schedule.md) lists a previous routine set and is superseded by this file (kept for history).

## Why there was no saved pregame evidence after Oct 4
- The routine historically wrote a Git note **only when it found something actionable**. Quiet runs left no record, so "no file" did **not** mean "no run" or "no change". Collection between Oct 5 and Nov 14 is therefore **incomplete/unknown**, not "no changes".
- Thursday Nov 12 runs mostly decided from the schedule alone (no live Yahoo pull).
- **Fix (prompt updated 2026-11-14):** every active-window run must pull Yahoo live and write a run record under [`pregame-runs/`](./pregame-runs/) even when nothing is actionable.

## This week's kickoff windows (W10) vs coverage
Verified against Yahoo team 8 page (read-only, ~5:10 PM CT Nov 14; Yahoo displays CST) and nflverse `games.csv` (ET, converted). All matched; no corrections needed.

| Game (CT) | Our players | Covering runs | Coverage |
|---|---|---|---|
| Thu Nov 12 7:15 PM WAS@NYG | Commanders DEF (final 24-21 W) | Thu runs (schedule-only, see above) | past |
| **Sun 8:30 AM NE@DET (Munich)** | LaPorta (BN) | none — first run 10:54 AM | **NOT covered (unsupported by schedule)**. No starter affected this week. |
| Sun 12:00 PM slate (MIN@GB, KC@ATL, HOU@CLE, MIA@IND, CAR@NO, …) | Love, Collins, Golden, Warren, Rice, McMillan; BN Downs, Judkins, Marks, Wan'Dale Robinson | 10:54 AM (after ~10:30 AM inactives; ~66 min before kick) | covered (one run only) |
| Sun 3:05 PM SEA@LV, LA@ARI | Mendoza, Gay | 1:54 PM, 2:54 PM | covered |
| Sun 3:25 PM SF@DAL | McCaffrey | 1:54 PM, 2:54 PM | covered |
| Sun 7:20 PM PIT@CIN (SNF) | Freiermuth (BN, Q illness) | 5:54 PM, 6:54 PM | covered |
| Mon 7:15 PM LAC@BAL (MNF) | Henry | Mon 5:54 PM, 6:54 PM | covered |

Unsupported/limits: any kickoff before ~11:00 AM CT (international/early games) and Saturday games (late season) are outside the cron. Only one run precedes the noon lock, so a late noon inactive after ~10:54 AM would not be caught by the routine.
