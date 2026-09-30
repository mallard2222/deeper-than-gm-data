# Quarantine — pending-claims UI document not found (2026-09-30)

- **URL pattern:** `/f1/668216/8/pendingclaims` (and related pending UI)
- **Observed:** Yahoo returned “The document you requested was not found” (HTTP 200 HTML error page)
- **Impact:** Cannot use pending-claims UI as authority for W04 pending state
- **Mitigation used:** Infer from team roster (unchanged), FAAB ($79 unchanged), and league transactions (no Vaqueros Sep 30 rows)
- **Do not treat** the missing pending page as proof of pending claims or as proof of submission
- Related prior note: pending URL has been flaky in this league; keep quarantined until a working pending UI capture exists
