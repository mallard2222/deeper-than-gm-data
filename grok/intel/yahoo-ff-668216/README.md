# Deeper Than intelligence layer

This directory is the persistent intelligence layer for Yahoo league `yahoo-ff-668216` (Deeper Than / Vaqueros). It preserves sourced observations, reconciled league state, analysis, decisions, and outcomes as a durable record that can be extended by later runs.

## Operating rules

- **Quarantine first:** every incoming signal starts as `quarantined` until it is validated against a source, a capture, or a reproducible reconciliation step. Do not promote an unvalidated signal into a fact or recommendation.
- **Keep layers distinct:**
  - **Raw evidence** is an immutable capture or source observation (Yahoo UI/export, screenshot, article, or retrieval note).
  - **Reconciled facts** are validated, normalized state derived from one or more evidence items.
  - **Analysis** is interpretation, forecast, prioritization, or a proposed action based on the reconciled facts. It is not a source of fact by itself.
- **Stable IDs:** use durable IDs for runs, evidence, facts, decisions, executions, and outcomes. Prefer IDs that include the league, season/week, date, and sequence; do not identify records only by a mutable title.
- **Historical predictions are append-only:** never rewrite a historical prediction, recommendation, or execution record to match a later result. Add a reconciliation or outcome record that points back to the original record.
- **League boundary:** this layer covers Deeper Than / Yahoo league `668216` only. It does not ingest, modify, or expand **8Deep** material.

The W03 package in `grok/waivers/yahoo-ff-668216/2026/W03-2026-09-22/` remains the source package for the initial seeded decision and execution links.
