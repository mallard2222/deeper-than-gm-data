# Research notes — Deeper Than W04 (2026-09-29)

League `yahoo-ff-668216` · Vaqueros team 8 · Collection ~8:10–8:16 AM America/Chicago  
Method: curl + Netscape jar from chrome-cookie-seed.json · Auth success · **No transactions executed**

## League rules (Yahoo settings evidence)

- Scoring: H2H; pass TD **4**; rush/rec TD **6**; receptions **0.5**; pass yd 25/pt; rush/rec yd 10/pt; INT −2; FL −2; fractional + negative points Yes
- Roster: QB, QB, WR, WR, RB, RB, TE, W/T, W/R, K, DEF, **BN×9**, IR
- Waivers: FAB; Weekly **Game Time – Tuesday**; waiver time 1 day; tiebreak weekly rolling standings; injured cannot add directly to IR from waivers/FA
- Trade reject time: 2 days
- Playoffs: 4 teams, Weeks 15–16, no reseeding
- Keepers: **not listed** → unknown
- Traded picks: **unknown**

**Bench resolution:** Settings text lists nine `BN` tokens; Vaqueros HTML shows nine BN players. Prior open question (8-vs-9) → **9 BN (FACT)**.

## Standings (Yahoo update: Tue Sep 29 01:16am CDT)

| Rk | Team | Rec | PF | PA | Streak | FAAB | WO | Moves |
|---:|---|---|---:|---:|---|---:|---:|---:|
| 1 | DUGASM | 3-0-0 | 460.28 | 367.50 | W-3 | 97 | 8 | 2 |
| 2 | Baby Arm | 2-1-0 | 489.50 | 424.28 | W-2 | 97 | 7 | 4 |
| 3 | Big Balls | 2-1-0 | 430.14 | 367.12 | L-1 | 62 | 6 | 3 |
| 4 | Deepest | 2-1-0 | 422.68 | 475.68 | W-1 | 94 | 5 | 2 |
| 5 | Wet Serapas | 1-2-0 | 452.98 | 445.14 | W-1 | 76 | 4 | 4 |
| 6 | Good Strongs | 1-2-0 | 381.34 | 420.04 | L-2 | 83 | 3 | 9 |
| 7 | FFAmuseBouche | 1-2-0 | 330.06 | 379.76 | L-1 | 100 | 2 | 1 |
| 8 | Vaqueros | 0-3-0 | 393.14 | 480.60 | L-3 | 79 | 1 | 2 |

## Vaqueros roster flags (Tue AM)

| Slot | Player | Yahoo ID | Inj | W4 proj | Notes |
|---|---|---:|---|---:|---|
| QB | Jordan Love | 32696 | | 16.85 | @ TB |
| QB | Bo Nix | 40875 | | 17.26 | @ SF |
| RB | Christian McCaffrey | 30121 | | 15.64 | vs Den |
| RB | Derrick Henry | 29279 | | 16.47 | vs Ten |
| WR | Tetairoa McMillan | 41793 | | 12.08 | vs Det |
| WR | Rashee Rice | 40084 | | 11.28 | @ LV |
| TE | Tyler Warren | 41799 | | 10.21 | @ Was |
| W/T | Matthew Golden | 41808 | | 10.17 | @ TB |
| W/R | Quinshon Judkins | 41821 | | 10.38* | TNF vs Pit (*from matchup page) |
| K | Cameron Dicker | 34344 | | 7.25 | @ Sea |
| DEF | Packers | — | | 8.14 | @ TB |
| BN | Caleb Williams | 40900 | O | 0.00 | Grade 2 ham 3–4 wk |
| BN | Nico Collins | 33477 | O | 0.00 | Coach hopeful W4 |
| BN | Rome Odunze | 40901 | | 7.94 | |
| BN | Jayden Reed | 40063 | O | 0.00 | Neck |
| BN | Sam LaPorta | 40064 | | 9.00 | |
| BN | RJ Harvey | 41845 | | 9.02 | |
| BN | Michael Pittman Jr. | 32704 | | — | TNF @ Cle; parse gap |
| BN | Woody Marks | 41902 | | 7.27 | |
| BN | Josh Downs | 40126 | | 11.16 | W03 11/5–77 / 10.20 |
| IR | *(empty)* | | | | 0/1 |

## W03 Vaqueros scoring (Final)

Love 18.48 · Nix 24.14 · CMC 19.60 · Henry 21.40 · McMillan 2.70 · Rice 12.30 · Warren 10.20 · Golden 18.50 · Judkins 8.90 · Dicker 10.00 · Packers **−8.00** · **Total 138.22**  
BN notables: Downs **10.20**, Harvey 7.70, Marks 8.60, Odunze 5.90, LaPorta 5.90, Pittman 2.60, Caleb/Nico/Reed 0.

## Available-player coverage

Fetched status=A pages sorted by % rostered: QB/WR/RB/TE/K count=0 & 25; DEF p0 (~22 teams); ALL 0/25/50; plus proj-sorted p0 per skill/DEF.  
**Not** full FA universe. Top targets summarized in `waivers.csv` + RECOMMENDATION.

### Notable FA (Tue AM)
- WR: Addison 73%/10.46 W(Sep 30); Johnston 71%; Concepcion available; Shakir 49%
- RB: Lloyd 71%; Gainwell 64%; Braelon Allen 20%/8.45
- DEF: Ravens 9.35; Bears 8.05 vs NYJ; Bills 6.99 — all mostly W(Sep 30)
- TE: Ferguson 78%; Henry/Hockenson/Strange mid
- QB: Mariota/Brissett/Malik Willis streamers — low need in 2QB with Love/Nix

## Transactions observed (since W03)
Visible log includes W03 waiver batch (Downs/Packers/etc.), later FA moves (Tank Bigsby, Dobbins FA add by Big Balls Sep 26, Watson FA Wet Serapas Sep 24, Wicks add Good Strongs). No Vaqueros moves after Sep 23 claims.

## External news (quarantine→validate)
- Nico coach hopeful W4 (Aaron Wilson / Fantasy Footballers / prior CBS) — aligns with Yahoo O + 0 proj until practice clears.
- Bears DEF vs Jets widely streamed (RotoBaller / FanDuel Research).
- FantasyPros W4 waiver board emphasizes situational RB/TE; Geno stream less relevant for us.

## Collection limits
- Snaps/routes/RZ not scraped from dedicated advanced sources this run.
- ROS projections: Yahoo % started/owned only; no separate ROS provider table.
- Some non-Vaqueros NFL abbreviations may be HTML-contaminated — use player IDs as stable keys.
