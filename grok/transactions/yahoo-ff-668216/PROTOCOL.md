# Transaction recording protocol — Deeper Than (`yahoo-ff-668216`), Vaqueros (team 8)

Adopted 2026-11-14 (CT) at Andrew's request. Applies to every Yahoo change: waiver/FAAB claims, claim edits or cancellations, free-agent adds, drops, trades, IR moves, and lineup changes. All times America/Chicago (CT).

## Authorization
- Every Yahoo transaction requires Andrew's explicit approval. The only standing exception is a **current-week start/sit swap** when a starter is OUT, on IR, or on bye and a healthy same-position bench player is available. Such swaps are still recorded (approval_ref = "standing bye/OUT start-sit rule").
- A recommendation, desk package, routine output, or this protocol is **not** an approval.

## Stage 1 — Recommendation (before asking)
Record in the weekly package and as a `recommendation` row in `2026/ledger-2026.csv`: player add, drop, bid range/max, rationale link, author (routine or FF GM), timestamp.

## Stage 2 — Pre-submission record (before touching Yahoo)
Write a `submission` row **before** the Yahoo action with:
- `approval_ref` — where/when Andrew approved (chat message or card answer, with CT timestamp)
- `approval_text` — Andrew's **exact words** or card answer, verbatim
- exact proposed action: `player_add`, `player_drop`, `bid_usd`, claim order if relevant
- `actor` — who will submit (e.g. "FF GM via computerUse in box browser", or "Andrew (manual)" only if Andrew confirms he did it)
- `timestamp_ct` and `timestamp_precision`
Edits (bid raise, cancel) get their own `submission_amendment` / `cancellation` row with their own approval.

## Stage 3 — Submission confirmation
Right after submitting, save confirmation evidence: Yahoo pending-claims text extract (preferred, committed under `2026/evidence/`) and/or screenshot reference. Never commit cookies, crumbs, GUIDs, session IDs, emails, or raw logged-in HTML. Set `status=submitted` and fill `evidence`.

## Stage 4 — Processed outcome
After Yahoo processes (Wednesday reconcile for waivers), add an `outcome` row: won / lost (winning team + price if visible) / cancelled_before_processing / failed (reason only if Yahoo shows it), FAAB before→after, drop executed or not, Yahoo timestamp as displayed.

## Integrity rules
- Recommendations, submissions, and completed moves stay in separate rows; never merge them.
- If actor or approval cannot be established, write `unknown` — never reconstruct authorization from a completed transaction.
- A manual move by Andrew is recorded as such only when he confirms it.
- Never rewrite or delete historical records; correct them with dated addenda under `2026/corrections/` and link both ways.
- Distinguish "not collected" (unknown) from "no change".
