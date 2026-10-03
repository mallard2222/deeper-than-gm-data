# Evidence source notes — daily 2026-10-03

- Retrieved: 2026-10-03T16:56:00–17:00:00-05:00 America/Chicago
- Method: curl + Netscape jar converted from `/home/box/agent-data/chrome-cookie-seed.json` (`/tmp/yahoo-netscape-all.txt` and prior `/tmp/yahoo-netscape-all-domains.txt`)
- Yahoo league 668216 / Vaqueros team 8
- **Yahoo auth: FAILURE** — all core league URLs returned HTTP 302 → `login.yahoo.com` (“Sign in” / manage_account). Cookie seed `savedAt` 2026-10-03 16:39 CT still carries T/Y session stamped ~2026-09-18; same jar that worked Fri 2026-10-02 now rejected. Chrome profile Cookie DBs encrypted (values length 0). Fantasy API also 401 without OAuth.
- Auth-fail HTML saved as `yahoo_auth_fail_*.html` (roster/matchup/league/transactions/standings/deepest) — login shells only; not usable league state.
- Pending-claims / tradehub **not re-fetched** (prior runs already document-not-found; auth would fail first anyway) — carried quarantine.
- Public NFL news collected via WebSearch/WebFetch + curl into `news_*.html` / `*_text.txt`.
- **No Yahoo transactions executed by this routine**
- Dedup: Fri daily `daily-report-2026-10-02.md` + batch `batch_20261002T170000_daily-intel.json` + Thu pregame `evidence/pregame-2026-10-01/`. Do not re-report Fri items as NEW unless status changed.
- Window: Fri 2026-10-02 ~5:00 PM CT → Sat 2026-10-03 ~5:00 PM CT. News after this cutoff belongs in next report.
