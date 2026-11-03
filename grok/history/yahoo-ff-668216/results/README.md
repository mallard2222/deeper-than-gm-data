# Deeper Than results archive (yahoo-ff-668216)

Underlying matchup records, identity drafts, summaries, evidence, and coverage/gaps.

**Status:** Seasons covered: 2013–2025 complete (weeks 1–16) + 2026 weeks 1–8 final (Week 8 finalized 2026-11-03). Not all-time until 2026 finishes and identity caveats clear — see `validation/coverage-report.md`.

Organization:
- `matchups/` — per-season JSONL + CSV (source of truth for scores)
- `identities/` — team/manager mappings by season
- `summaries/` — reproducible aggregates from matchup files
- `evidence/` — Yahoo screenshots
- `raw/` — scrape notes and URLs
- `validation/` — coverage and reconciliation reports (`coverage-report.md`, `coverage-gaps.json`, `standings-reconciliation.csv`)
- `h2h/` — head-to-head tables (manager-level and team-name-level) for regular, championship, consolation, combined
- `raw/captures/` — sanitized parsed captures (source URL + retrieval time + parsed data; projections as `proj_*`)

Exclude 8Deep. Yahoo access for collection is read-only.
