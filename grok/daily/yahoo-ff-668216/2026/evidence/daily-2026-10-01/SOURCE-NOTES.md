# Evidence source notes — daily 2026-10-01

- Retrieved: 2026-10-01T16:56:00–17:00:00-05:00 America/Chicago
- Method: curl + Netscape jar converted from `/home/box/agent-data/chrome-cookie-seed.json` (`/tmp/yahoo-netscape-all.txt`)
- Yahoo league 668216 / Vaqueros team 8
- HTML files are raw league UI captures; `*_text.txt` / `extract.json` are derived
- Auth: pages returned logged-in Deeper Than content (Vaqueros roster, Waiver Budget **$79**, Deepest W4 matchup, Oct 1 transactions)
- Pending-claims URL → Yahoo “The document you requested was not found” shell — quarantined (same class as prior dailies)
- Deepest team page: `/f1/668216/4` (team ID 4; initial `/5` was DUGASM — corrected)
- No Yahoo transactions executed by this routine
- Dedup note: Thu 2026-10-01 pregame lineup risk checks ~11:08–16:00 CT under `evidence/pregame-2026-10-01/` (Judkins W/R TNF; Pittman BN; NO_WINDOW; no actionable alerts) — **deduplicated**. This daily focuses on **NEW** deltas since Wed ~5:05 PM CT daily (Thu practice / FA claims / proj drift / opponent DeVonta Q)

## Public news fetches (primary / secondary)

| Item | Source | Published / noted | Class |
|---|---|---|---|
| Nico limited practice Thu (2nd straight) | CBS/RotoWire 5:00 pm ET; RotoBaller (cites Cody Stoots) 12:28 PM ET; SI OnSI quotes via KPRC2 Aaron Wilson | 2026-10-01 Thu | confirmed practice LP (team report / beat); player quotes secondary via Aaron Wilson |
| Caleb DNP Thu practice | Chicago Sun-Times Patrick Finley; CBS/RotoWire 4:08 pm ET; NBC Rotoworld Rivers McCown | 2026-10-01 Thu | confirmed DNP (team injury report / beat) |
| DeVonta Smith hamstring / Yahoo Q | Yahoo matchup UI Q; Mike Garafolo “legitimately questionable” (Yahoo Sports / Sporting News syndication); NBC10 Philly DNP Thu list | 2026-10-01 Thu | Yahoo Q confirmed; OUT not official as of this capture — Fri gate |
| Judkins TNF | Browns.com final outs Sep 30 (Jenkins/Wallace); Yahoo OK; inactives not yet posted ~5pm CT (~2+ hr to kick) | through 2026-10-01 ~5pm CT | continuity; not new injury |

## Yahoo UI facts (this run)

- Reed still Yahoo **IR** / **BN**; fantasy IR slot still **0/1** empty
- Nico still **Q** / proj **15.16** (was 15.12 Wed PM); Yahoo “New” player note flag
- Caleb still **D** / 0.00; Yahoo “New” note flag
- Judkins W/R starter proj **11.40** (was 10.72); Pittman BN TNF
- W04 proj **143.03–140.20**, Vaqueros **52%** (Wed PM daily 142.64–140.00 / 52%)
- **NEW txns Oct 1:** Good Strongs add **Ravens DEF** / drop Chris Bell (12:25 pm); FFAmuseBouche add Zach Charbonnet / drop Drew Lock (12:29 pm)
- **Ravens DEF no longer FA** (owned Good Strongs)
- Pending trade banner: Good Strongs ↔ DUGASM (composition not captured — quarantine)
- Packers DEF still rostered (8.72); Gainwell still FA (6.44)
- DeVonta Smith (Deepest WR) Yahoo **Q**
