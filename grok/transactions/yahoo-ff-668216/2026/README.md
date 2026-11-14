# 2026 transaction execution ledger — Deeper Than / Vaqueros

`ledger-2026.csv` — one row per stage per transaction (`txn_id` groups rows):

| stage | meaning |
|---|---|
| recommendation | what the desk/FF GM recommended (not an approval) |
| submission / submission_amendment / cancellation | what was actually entered in Yahoo, by whom, when, under which approval |
| outcome | what Yahoo processed (won / lost / cancelled_before_processing / verified_in_place) |

Key columns: `approval_received` (yes / unknown / standing rule), `approval_ref`, `approval_text` (verbatim or `unknown`), `actor`, `timestamp_ct` + `timestamp_precision`, `evidence`, `source`.

Backfill (created 2026-11-14): rows for W09 and W10 were reconstructed from **FF GM conversation/action history** (timestamps in the rows) plus Yahoo transaction evidence. Known gaps:
- **W09 approval wording: unknown.** Andrew answered a choice card between 08:05:55 and 08:07:02 CT on 2026-11-03 approving the lineup reset, Harvey to IR, and the Washington claim; the card text is not retrievable. `approval_received=yes`, `approval_text=unknown`.
- **W09 submission confirmation evidence: none saved.**
- W10 screenshots live in the FF GM agent asset store (not committed to Git); referenced by hash prefix.
- Brissett $12 raise time is bounded (after the ~5:04 PM CT observation of $8, before the ~5:22 PM CT Mendoza card), not exact.
- Transactions before W09 (W03 has its own execution record) are not backfilled here.

Rules: [PROTOCOL.md](../PROTOCOL.md). Corrections: [corrections/](./corrections/). Evidence extracts: [evidence/](./evidence/).

| txn_id | summary | outcome |
|---|---|---|
| 2026-W09-01 | Mike Washington Jr. $15, no drop | won (FAAB 79→64) |
| 2026-W10-01 | Brissett $8→$12, drop Freiermuth | lost to FFAmuseBouche $21 |
| 2026-W10-02 | Penix $3, drop Freiermuth | cancelled before processing (verified) |
| 2026-W10-03 | Mendoza $30, drop Washington (Andrew-directed, not desk-recommended) | won (FAAB 64→34) |
| 2026-W10-04 | Mendoza into QB for bye Caleb Williams (standing rule) | verified in place 2026-11-14 ~5:10 PM CT |
