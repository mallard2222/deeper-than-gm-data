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
