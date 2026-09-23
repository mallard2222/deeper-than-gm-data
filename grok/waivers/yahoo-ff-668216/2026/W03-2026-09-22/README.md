# Deeper Than — Week 3 waiver assessment package

| Field | Value |
|---|---|
| League | Deeper Than (Yahoo FF **668216**) |
| Team | Vaqueros (team id **8**) |
| Season / week | **2026** / **W03** |
| Package date | **2026-09-22** |
| Collection window (America/Chicago) | **Tue Sep 22, 2026 ~7:42–7:50 PM CT** (Yahoo UI ~7:45 PM CT; pages labeled CDT) |
| Scope | **Deeper Than ONLY** — no 8Deep |
| Actions | Read-only assessment; **no** Yahoo add/drop/claim/lineup submission |

## Coverage

- Vaqueros Week 3 roster + projections + injury letters (Yahoo)
- League settings / scoring / FAB waiver rules
- Standings + visible FAAB / waiver order
- Public opponent roster samples
- Available players by position (filtered lists)
- External injury/usage evidence (Collins, Reed, Downs, Pittman) + DEF stream consensus
- Ranked FAAB claim plan (`RECOMMENDATION.md`)

## Known gaps / missing data

- **Available-player export incomplete** (top ~**25** per position filter, **not** full pagination).
- **Exact waiver processing clock not shown** on Yahoo settings UI this collection.
- **No private claims seen** (team page showed no pending Vaqueros claims; not an assertion that none exist elsewhere).
- **Keepers not listed** on Yahoo settings page.
- Injured-to-IR-from-waivers/FA blocked by league rule; rostered→IR eligibility for Reed must be confirmed in UI.
- Screenshot set covers roster, settings, standings, players filters, and one RB available list — not every position page screenshoted.

## Files

| File | Role |
|---|---|
| [research.md](./research.md) | Full Yahoo read-only research notes |
| [roster.csv](./roster.csv) | Vaqueros Week 3 roster export |
| [waivers.csv](./waivers.csv) | Visible available-player leaders by position |
| [settings.json](./settings.json) | League settings snapshot |
| [standings.csv](./standings.csv) | Standings + FAAB + waiver order |
| [opponents.md](./opponents.md) | Public opponent roster samples |
| [evidence-notes.md](./evidence-notes.md) | Sourced injury/usage facts (FACT vs INTERPRETATION) |
| [RECOMMENDATION.md](./RECOMMENDATION.md) | Claim plan / interpretation (docs only) |
| [source-manifest.json](./source-manifest.json) | Source URLs + local artifact list |
| [changes-since-last-run.md](./changes-since-last-run.md) | Diff vs prior weekly waiver folder |
| [roster-overview.png](./roster-overview.png) | Roster screenshot |
| [settings.png](./settings.png) | Settings screenshot |
| [standings.png](./standings.png) | Standings screenshot |
| [players-filters.png](./players-filters.png) | Players / filters screenshot |
| [waiver-rb-list.png](./waiver-rb-list.png) | Available RB list screenshot |

## Move summary (docs only)

1. Prefer Reed → IR (confirm eligibility) to free BN.  
2. Add Packers DEF ($5 / max $12), drop Chargers; fallback Panthers then Giants.  
3. Add Josh Downs ($22 / max $40), drop Concepcion; fallback Addison/Shakir/Vele; never drop Collins.  
4. Optional Shakir/Boutte if second slot freed. Skip WR if only fringe left above $40; still stream DEF.
