# Evidence source notes — W09 Wednesday waiver reconciliation 2026-11-04

- Retrieved: 2026-11-04 08:01:39–08:04:03 America/Chicago (per-URL times in `fetchlog.txt` / `MANIFEST.json`)
- Method: curl with the existing Netscape cookie jar (built from `chrome-cookie-seed.json` by earlier runs); ~2–3 s spacing; 16 GETs total
- Auth: all pages HTTP 200 with logged-in Deeper Than content
- Pages: Vaqueros team (8), teams 1–7, league home (standings/FAAB), transactions (all, add filter, FAB Offers filter), players status=A (O by added, RB by W9 proj), players status=W (O)
- Committed files are text extracts with script/style removed; raw HTML (with SHA-256 in MANIFEST) is kept on the box at `/home/box/agent-data/yahoo-raw/recon-2026-11-04/` and not committed
- The pending-claims URL was not fetched (known document-not-found); pending state determined from the team-page waiver panel (absent), roster, transactions, and FAAB
- No Yahoo transactions executed by this run
