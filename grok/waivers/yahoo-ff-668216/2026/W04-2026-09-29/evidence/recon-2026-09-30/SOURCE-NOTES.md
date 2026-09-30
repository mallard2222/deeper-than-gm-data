# Evidence source notes — W04 Wednesday waiver reconciliation 2026-09-30

- Retrieved: 2026-09-30T08:03–08:05 America/Chicago
- Method: curl + Netscape jar converted from `/home/box/agent-data/chrome-cookie-seed.json`
- Cookie jar path used at runtime: `/tmp/yahoo-netscape-w04-recon.jar` (not committed)
- Yahoo league 668216 / Vaqueros team 8
- Auth: team/transactions/standings/players/settings returned logged-in Deeper Than content (HTTP 200, large HTML)
- Pending-claims URL (`/f1/668216/8/pendingclaims`): Yahoo “document not found” — treated as unusable pending UI; inferred from team roster + transactions + FAAB instead (quarantined)
- No Yahoo transactions executed by this run
- Derived extracts: `transactions_sep30_extract.json`, `roster_alts.json`
