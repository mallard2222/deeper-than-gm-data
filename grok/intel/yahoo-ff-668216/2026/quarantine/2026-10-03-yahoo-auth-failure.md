# Quarantine — Yahoo Fantasy auth failure (2026-10-03)

- **Signal:** All Deeper Than league URLs return HTTP 302 → `login.yahoo.com` when fetched with Netscape jar from `/home/box/agent-data/chrome-cookie-seed.json`.
- **Observed:** 2026-10-03 ~4:56–5:00 PM America/Chicago during daily intelligence routine.
- **Cookie seed:** `savedAt` 2026-10-03 16:39 CT; T/Y session internal timestamp ~2026-09-18 (~356h). Values match Fri 2026-10-02 jar that previously succeeded.
- **Not evidence of:** empty waiver wire, “no transactions,” or stable roster — those pages were simply unreachable.
- **Chrome Cookies DBs:** encrypted (value length 0); cannot re-extract from profile sqlite.
- **Fantasy API:** 401 without OAuth.
- **Action needed:** User/browser re-login to Yahoo Fantasy → refresh `chrome-cookie-seed.json` → re-run collection.
- **Evidence:** `grok/daily/yahoo-ff-668216/2026/evidence/daily-2026-10-03/yahoo_auth_fail_*.html`
- **Related prior quarantines:** pending-claims UI document-not-found (unchanged; not re-tested under auth fail).

## Update 2026-10-04 ~5:00 PM CT (daily)
- Still failing after seed refreshes at 10:58, 12:32, and 16:57 CT (team 302, matchup 302, API 401). Fourth consecutive scheduled failure (Sat daily, Sun 11:08 + 12:34 pregame, Sun daily).
- Pregame routine paused; daily routine paused after this run. Resume both after Andrew re-logs into Yahoo in the box browser and a test fetch returns 200.

## Update 2026-10-06 ~8:00 AM CT (Tuesday intelligence desk, W05)
- Seed refreshed 07:54 CT today; test fetch of `/f1/668216/8` still HTTP 302 → `login.yahoo.com` (src=ats-fantasysports). Fifth consecutive scheduled failure.
- Box browser screenshot shows Yahoo sign-in stuck at a passkey challenge for account `ogdru22` ("Passkey not found"; QR-code passkey flow). Needs Andrew to complete sign-in (e.g. "Try signing in another way").
- W05 Tuesday desk did NOT collect league state, FAAB, waiver pool, or transactions; no W05 waiver package written. Nothing here is evidence of an empty wire or unchanged rosters.
- Tuesday desk routine paused pending re-login; Wednesday reconciliation is also Yahoo-dependent.
- Carry-forward asks for the next successful desk: Bigsby / Shipley and Rice contingency (from 2026-10-04 daily), Reed→fantasy IR, DEF stream vs Packers hold.
