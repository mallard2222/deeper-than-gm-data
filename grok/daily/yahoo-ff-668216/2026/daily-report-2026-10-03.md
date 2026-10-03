# Deeper Than daily intelligence — 2026-10-03 (CT)

- **Routine:** deeper-than-daily-intelligence-report (≈5:00 PM America/Chicago)
- **League:** yahoo-ff-668216 / Vaqueros team 8
- **Collection status:** **failure** (Yahoo Fantasy auth — HTTP 302 → login.yahoo.com). Public NFL news **did** collect. **Do not read this as “no league news.”**
- **Run at:** 2026-10-03 05:00 PM CT
- **Last successful daily batch:** 2026-10-02 05:00 PM CT (`batch_20261002T170000_daily-intel.json`, commit `a4e94c2`)
- **Collection window:** 2026-10-02 05:00 PM CT → 2026-10-03 05:00 PM CT
- **Yahoo:** cookie jar from `/home/box/agent-data/chrome-cookie-seed.json` (seed refreshed 16:39 CT today) still rejected. T/Y session ~Sep 18 vintage; same values that worked Fri. Roster / W4 matchup / league / transactions / standings / Deepest team 4 all login-redirect. Fantasy API 401. Pending-claims + tradehub not re-tried (auth fail; prior document-not-found quarantine stands). **No transactions executed by this routine.**
- **FAAB / waiver / IR / live proj:** **unknown Sat** — last known Fri: FAAB **$79**, WO ~**1**, IR **0/1** empty, W4 proj **146.81–138.13 (63%)**, Judkins locked **18.60**.
- **Matchup:** Week 4 vs **Deepest** (last known 2-1-0, 4th) — Yahoo live state not refreshed.

## Andrew-facing summary

1. **COLLECTION FAILURE — Yahoo auth dead.** Cannot refresh roster, matchup, transactions, FA, Reed W(Oct 3) claim results, or Deepest live status. **Needs cookie re-login / seed refresh** before Sunday early lock if possible. Public news below still actionable.
2. **NEW — Keenan Allen OUT** (groin) for Colts London — team/AP Sat (~11:52 am ET FOX). Concentrates targets toward **Tyler Warren** (Vaqueros TE, early lock ~8:30 AM CT) and **Josh Downs** (Vaqueros BN). Not recommending a Downs-over-Nico flex flip; Warren start already set.
3. **NEW — Terry McLaurin likely to miss** London (Ben Standig Sat AM via CBS/RotoWire). Still **officially Q** on Commanders/NFL.com — report, not confirmed OUT. Further Deepest WR downgrade alongside DeVonta OUT (Fri).
4. **Weather refresh GB@TB:** ~**87°F**, precip ~**43%** isolated thunderstorms, light SE wind (NFLWeather). Still a precip/heat/delay watch for **Love / Packers DEF / Golden** — default hold Love + Packers.
5. **Mayfield OUT** (Fri final / Sat CBS digest) — mild positive context for held Packers DEF vs Bucs backup QB.
6. **Unchanged / not re-reported as NEW:** Nico still cleared (Sat OC comments only); Caleb OUT W4; Judkins 18.60 locked; Wan'Dale add / Reed drop Oct 1; DeVonta OUT; Reed reclaim still not recommended. Reed W(Oct 3) processing **unverifiable** without Yahoo.
7. **Live W4 proj / FA churn / league txns since Fri 5pm:** **unknown** (auth failure).

**Actions needed from Andrew (docs only — routine will not move):** (A) **Re-auth Yahoo** (browser login → refresh `chrome-cookie-seed.json`) so Sunday routines can see lineup/waivers; (B) **London early lock ~8:30 AM CT** — leave Warren at TE; optional Downs flex only if you prefer vs Golden path (Nico stays preferred W/T); (C) **McLaurin** — watch London inactives for Deepest; (D) **Weather** — recheck GB@TB gameday; (E) Reed reclaim — still **no**.

## Current Vaqueros snapshot (LAST KNOWN Yahoo 2026-10-02 ~5:00 PM CT — NOT revalidated Sat)

| Slot | Player | Flags / note |
|---|---|---|
| QB | Jordan Love | Fri proj 17.54 @ TB — Sat weather ~87F / ~43% precip |
| QB | Bo Nix | Fri proj 17.61 @ SF |
| RB | Christian McCaffrey | Fri proj 17.53 vs Den |
| RB | Derrick Henry | Fri proj 17.33 vs Ten |
| WR | Tetairoa McMillan | Fri proj 12.34 vs Det (SNF) |
| WR | Rashee Rice | Fri proj 12.47 @ LV (dome) |
| TE | Tyler Warren | Fri proj 10.40 @ Was London **~8:30 am CT** — **Allen OUT → target share up** |
| W/T | Nico Collins | Fri proj 15.15 — still cleared (no Sat designation change) |
| W/R | Quinshon Judkins | **Final 18.60** TNF |
| K | Cameron Dicker | Fri proj 6.95 @ Sea |
| DEF | Packers | Fri proj 8.72 @ TB — Mayfield OUT context |
| BN | Matthew Golden | Fri proj 10.76 — weather risk |
| BN | Caleb Williams | **O** / 0.00 |
| BN | Rome Odunze | Fri proj 8.02 |
| BN | Sam LaPorta | Fri proj 8.94 |
| BN | RJ Harvey | Fri proj 9.02 |
| BN | Michael Pittman Jr. | **Final 2.50** TNF |
| BN | Woody Marks | Fri proj 7.81 |
| BN | Josh Downs | Fri proj 11.12 — **Allen OUT → London target share up** (stays BN vs Nico) |
| BN | Wan'Dale Robinson | Fri proj 7.89 |
| IR | *(empty)* | 0 of 1 — last known |

## Material items

See JSON batch for full structured fields. Prioritized list (**new since Fri PM daily**):

### 2026-W04-yahoo-auth-failure-sat
- **Change:** Yahoo Fantasy session **invalid** — all league pages redirect to login. Cannot collect live roster/matchup/transactions/FA/standings/Deepest.
- **When:** Observed 2026-10-03 ~4:56–5:00 PM CT
- **Confidence:** **confirmed**
- **Response:** **act** · Deadline: ASAP / before Sun ~8:30 AM CT early lock if possible
- **Would change assessment:** Successful re-auth + fresh seed
- **Sources:**
  - Evidence `yahoo_auth_fail_*.html` + `SOURCE-NOTES.md` (retrieved 2026-10-03T17:00:00-05:00)

### 2026-W04-keenan-allen-out-london
- **Change:** Colts WR **Keenan Allen ruled OUT** Sat (groin) for London vs WAS. Was Q after Fri DNP; downgraded Sat. Elevates **Warren** + **Downs** target share (Pierce already IR).
- **When:** Team announcement Sat 2026-10-03 (~11:52 am ET AP/FOX)
- **Confidence:** **confirmed** (team)
- **Ownership:** Warren Vaqueros TE; Downs Vaqueros BN; Allen not rostered
- **This week:** Start Warren with higher confidence. Downs BN unless Andrew explicitly prefers flex over Golden path — **do not** demote Nico.
- **Response:** **prepare** · Deadline: London lock ~8:30 AM CT Sun
- **Would change assessment:** Allen unexpectedly active; Warren inactive
- **Sources:**
  - [FOX/AP — Allen ruled out](https://www.foxsports.com/articles/nfl/colts-wr-keenan-allen-ruled-out-of-london-game-because-of-groin-injury) (2026-10-03 11:52 am ET; retrieved 2026-10-03T17:00:00-05:00)
  - [ESPN — Allen out](https://www.espn.com/nfl/story/_/id/50090624/colts-wr-keenan-allen-groin-vs-commanders-london)
  - [CBS Week 4 injury digest](https://www.cbssports.com/nfl/news/nfl-week-4-injury-report-justin-jefferson-aaron-donald-terry-mclaurin/) (2026-10-03 12:30 pm ET)

### 2026-W04-mclaurin-likely-miss-london
- **Change:** Deepest WR **Terry McLaurin** still official **Q**; Sat beat (Ben Standig) says **likely to miss** London (hamstring). Not yet official OUT.
- **When:** Standig report Sat AM 2026-10-03; CBS/RotoWire 10:42 am ET
- **Confidence:** **report** (beat) / official status still Q
- **Ownership:** Deepest (opponent)
- **This week:** Opponent WR ceiling further down if sits (DeVonta already OUT Fri). Helps Vaqueros.
- **Response:** **monitor** · Deadline: London inactives
- **Would change assessment:** Officially active
- **Sources:**
  - [CBS/RotoWire — likely to miss](https://www.cbssports.com/fantasy/football/news/commanders-terry-mclaurin-likely-to-miss-sundays-game/) (2026-10-03 10:42 am ET)
  - [Yahoo Sports / Standig context](https://sports.yahoo.com/articles/no-terry-london-commanders-wr-152121280.html)
  - [Commanders.com game status](https://www.commanders.com/news/game-status-commanders-colts-2026) (still Q)
  - [NFL.com injuries](https://www.nfl.com/injuries/) (Q)

### 2026-W04-weather-gb-tb-sat-refresh
- **Change:** GB@TB forecast refresh — kickoff ~**87°F**, precip ~**43%** isolated T-storms, wind ~7 mph SE (NFLWeather). Heat/humidity + lightning-delay risk.
- **When:** Forecast retrieved 2026-10-03 ~5:00 PM CT
- **Confidence:** **confirmed** (forecast product; subject to change)
- **Ownership:** Love / Packers DEF / Golden
- **Response:** **monitor** · Deadline: Sun kick ~12:00 PM CT
- **Sources:**
  - [NFLWeather GB@TB](https://www.nflweather.com/games/2026/week-4/packers-at-buccaneers)

### 2026-W04-mayfield-out-packers-def-context
- **Change:** Bucs QB **Baker Mayfield OUT** W4 — Packers DEF faces backup (Jalon Daniels context per CBS). Mild positive for held Packers DEF.
- **When:** Fri final injury report; restated in Sat CBS Week 4 digest
- **Confidence:** **confirmed**
- **Response:** **monitor** (hold Packers default; no stream authorized; FA alternatives unverifiable Sat)
- **Sources:**
  - CBS Week 4 injury digest; NFL.com injuries; Packers.com Week 4 IR

### 2026-W04-reed-waiver-day-unverifiable
- **Change:** Reed was **W(Oct 3)** as of Fri daily. Sat is processing day — **claim results unknown** (Yahoo auth fail). Reclaim still **not recommended** (season-ending neck surgery).
- **When:** Through 2026-10-03 ~5:00 PM CT
- **Confidence:** **inference** (cannot verify league UI)
- **Response:** **monitor**
- **Sources:** Fri daily report; NFL.com Reed season-ending surgery

## FA / DEF notes

- **Packers DEF:** Still held per last-known Fri. Mayfield OUT = mild stream-context positive. Chiefs/Eagles/Bills FA status **unknown Sat**.
- **Godwin:** Last known FA Fri; Bucs FP / no designation on NFL.com — still a watchlist name; claim status unknown.
- **Goedert:** Last known FA + OUT this week — don’t chase W4.
- **Reed:** W(Oct 3) result unknown; no reclaim.
- **No claim authorized** by this routine.

## Evidence paths

- `grok/daily/yahoo-ff-668216/2026/batches/batch_20261003T170000_daily-intel.json`
- `grok/daily/yahoo-ff-668216/2026/evidence/daily-2026-10-03/`
- Prior Fri daily: `grok/daily/yahoo-ff-668216/2026/daily-report-2026-10-02.md`
- Quarantine: `grok/intel/yahoo-ff-668216/2026/quarantine/2026-10-03-yahoo-auth-failure.md`

## Open questions / next checks

1. **Yahoo re-auth** — unblock live collection before Sunday early lock.
2. London early lock: Warren ~8:30 AM CT; confirm Allen OUT + McLaurin inactive trend.
3. Weather: GB@TB gameday recheck for Love / Packers / Golden.
4. Reed W(Oct 3) claim result once Yahoo works.
5. Live W4 proj drift / Deepest roster once Yahoo works.
6. Keepers / private FAAB / pending-claims UI — still unknown/broken (carried).
