# Evidence source notes — daily 2026-10-02

- Retrieved: 2026-10-02T16:59:00–17:05:00-05:00 America/Chicago
- Method: curl + Netscape jar converted from `/home/box/agent-data/chrome-cookie-seed.json` (`/tmp/yahoo-netscape-all.txt`)
- Yahoo league 668216 / Vaqueros team 8
- HTML files are raw league UI captures; `*_text.txt` / `extract.json` are derived
- Auth: pages returned logged-in Deeper Than content (Vaqueros roster, Waiver Budget **$79**, Deepest W4 matchup, Oct 1–2 transactions)
- Pending-claims URL → Yahoo “The document you requested was not found” shell — quarantined (same class as prior dailies)
- Tradehub URL → same document-not-found shell — quarantined
- Deepest team page: `/f1/668216/4`
- **No Yahoo transactions executed by this routine**
- Dedup note: Thu 2026-10-01 pregame lineup risk checks ~11:08–20:56 CT under `evidence/pregame-2026-10-01/` (Judkins W/R TNF; Pittman BN; NO_WINDOW / ACTIVE windows; no actionable alerts) — **deduplicated**. This daily focuses on **NEW** deltas since Thu ~5:00 PM CT daily (`batch_20261001T170000_daily-intel.json`).

## Public news fetches (primary / secondary)

| Item | Source | Published / noted | Class |
|---|---|---|---|
| Nico Collins FP Fri + cleared (no designation) vs DAL | CBS/RotoWire 4:07 pm ET; Houston Chronicle Jonathan M. Alexander; Texans Wire / Yahoo Sports | 2026-10-02 Fri | **confirmed** official — removed from injury report / FP Fri |
| Caleb Williams officially OUT vs Jets | ChicagoBears.com Larry Mayer 3:13 pm CT; SI OnSI Fri report; Bears Wire | 2026-10-02 Fri | **confirmed** team announcement / final injury report |
| DeVonta Smith OUT vs Rams (hamstring); multi-game risk | Inquirer 4:02 pm ET; ESPN; NBC Sports / PFT Myles Simmons | 2026-10-02 Fri | **confirmed** Eagles final injury report OUT |
| Judkins TNF CLE 27–24 PIT | Browns.com recap; NFL gamebook; StatMuse / Sleeper box | 2026-10-01 Thu night Final | **confirmed** box score — 17-53-1 rush, 6-43 rec |
| Goedert OUT (knee) Week 4 | ESPN / PFT alongside DeVonta outs | 2026-10-02 Fri | **confirmed** Eagles OUT (FA TE watch) |
| Week 4 weather (GB@TB precip/wind; BAL rain risk) | Yahoo in-UI forecasts; DK Network W4 weather secondary | 2026-10-02 | report / forecast — recheck gameday |

## Yahoo UI facts (this run)

- Roster **20** still: **Reed dropped** / **Wan'Dale added** (Oct 1, 6:04 pm — after prior daily)
- Fantasy IR still **0/1 empty** (Reed was dropped to waivers, not moved to fantasy IR)
- Nico **no longer Q** — cleared; now **W/T starter** proj **15.15** (was BN Q/15.16 Thu PM)
- Golden now **BN** (was W/T)
- Caleb Yahoo **O** / 0.00 (was D)
- Judkins **Final** 18.60 (proj 10.77); Pittman BN Final 2.50
- W04 embedded proj **146.81–138.13**, Vaqueros **63%** favorite (Thu PM daily 143.03–140.20 / 52%)
- Deepest WR **DeVonta Smith O**; matchup also shows Terry McLaurin **Q**
- **NEW txns since Thu 5pm daily:** Vaqueros Wan'Dale/Reed; trade Achane↔Ollie Gordon (Good Strongs↔DUGASM processed); Good Strongs Emanuel Wilson / drop Vele
- Packers DEF still rostered (8.72); Chiefs/Eagles DEF still FA (6.46 / 6.36)
- Reed now **W (Oct 3)** on waivers (Add Player affordance)
- Pending trade banner **gone** (trade processed)
