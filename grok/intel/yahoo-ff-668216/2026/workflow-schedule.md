# Workflow schedule — 2026

These are the four active intelligence routines for `yahoo-ff-668216`. Cron expressions are in **America/Chicago (CT)**. Delivery for every routine is **this Grok Bot chat to Andrew**. All routines are read/reconcile/report only: **no auto transactions**, no automatic claims, drops, lineup changes, trades, or IR moves.

| Routine | Folder ID | Cron (CT) | Purpose | Delivery |
|---|---|---|---|---|
| Daily intelligence refresh | `deeper-than-daily-intel` | `0 8 * * 1-6` | Refresh Yahoo-visible league/team signals, validate sources, and append daily report state | This Grok Bot chat to Andrew |
| Tuesday waiver assessment | `deeper-than-weekly-waivers` | `0 19 * * 2` | Re-verify rules, scan available players, produce the weekly assessment and quarantine unvalidated signals | This Grok Bot chat to Andrew |
| Wednesday outcome check | `deeper-than-waiver-outcomes` | `15 8 * * 3` | Check waiver processing results and reconcile pending claims into outcomes without rewriting the decision | This Grok Bot chat to Andrew |
| Weekly matchup/reconciliation review | `deeper-than-weekly-review` | `0 18 * * 1` | Reconcile prior-week results, injuries, roster state, and open questions; identify next checks | This Grok Bot chat to Andrew |

Routine outputs should carry a `run-metadata.schema.json` record. A routine may report that an approved action is pending, but only Andrew can authorize any Yahoo transaction and any such action must be separately recorded.
