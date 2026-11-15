# Deeper Than daily intelligence — 2026-11-15 (CT)

- **Routine:** deeper-than-daily-intelligence-report (≈5:00–5:25 PM America/Chicago)
- **League:** yahoo-ff-668216 / Vaqueros team 8 (W10 matchup vs Wet Serapas; the NFL slate today is Week 10)
- **Collection status: PARTIAL FAILURE.** Yahoo returned **302 to login** with both cookie jars at 5:00 PM CT (one retry; no login attempted) → see `evidence/daily-2026-11-15/yahoo-access-attempt.txt`. Public sources OK: ESPN public API box scores (~5:01/5:15 PM CT), NFL.com gamebooks, team sites, ESPN/NFL.com injury reporting.
- **Yahoo-dependent fields are STALE:** live matchup score/projection, ownership, FA status, FAAB, claims. Last values: lineup/roster 2026-11-15 11:27 AM CT (pregame run); matchup/FA/transactions 2026-11-14 ~5:05–5:14 PM CT; FAAB $34 (not re-read since the Nov 14 Worthy add).
- **Previous successful daily:** 2026-11-14 ~5:04 PM CT (6bbc6a9). Window: Nov 14 ~5:15 PM → Nov 15 ~5:15 PM CT. Deduped against today's 11:00/11:26 AM pregame records (the 3:58 PM pregame failure left no repo record).
- **No Yahoo transactions, lineup changes, claims or messages made or authorized by this routine.**

## Andrew-facing summary
1. **Woody Marks (W/R starter): concussion, ruled out in Q3** at CLE (12-50 rush, 1-15 rec before exit; ≈7.0 pts est.). **HOU plays TNF W11 vs IND (Thu Nov 19)**, so he has to clear protocol on a short week, which makes him **doubtful-leaning for W11** (inference). Montgomery (opp bench, OUT W10) is also trying to return that night. Marks' W11+ value is down.
2. **The W10 swap cost about 3.7 pts:** Rice (bench) put up 5-82 on 6 targets (≈10.7) vs Marks ≈7.0 (my estimate from public stats; not Yahoo-confirmed). Worthy (added Fri) had 0 catches on 3 targets.
3. **W10 matchup is very likely lost** (inference from public box scores; Yahoo live score unavailable). We're at ≈92 pts with Mendoza/CMC live and Henry Mon. Wet Serapas are at ≈155 final + JSN/McBride/Rams DEF live (≈180+). Their starters blew up: Mahomes 348/5 TD, Gibbs 252 total yds/2 TD, P. Washington 7-152-1, D.J. Moore 4-90-1.
4. **Vaqueros starters, today:** all active (no starter inactive). Collins 9-94-1 on 16 targets (≈19.9). Love 220/1/1 and sacked 8× (≈10.8). Golden 5-70 (≈9.5). McMillan 3-35 (≈5.0). Warren 2-1 (≈1.4; NBC notes near-every-snap usage, so no injury). Live: Mendoza ≈11.8 (rush TD; LV TE Bowers left with an ankle injury, OUT), CMC ≈17.2 at half (74-yd TD), Gay 4.
5. **Bench:** Judkins scored the go-ahead TD (≈14.6). Downs scored a TD in his KC debut (4-53-1, ≈13.3). LaPorta 1-16. Wan'Dale Robinson 3-10. Freiermuth (dropped) plays SNF.
6. **W11 byes hit us: GB (Love, Golden), CLE (Judkins)**, plus ATL, LAR, NE and SEA. Caleb Williams, Bo Nix and Odunze come back from bye. Our W11 opponent is inferred to be **Deepest (Jeremy)**, which isn't verified on Yahoo.
7. **League-wide:** Drake Maye (ankle) and A.J. Brown (hamstring) were ruled out in Munich. Geno Smith (ankle) was ruled out. KC TE Jared Wiley has a fractured ankle (Reid); Kelce briefly exited with a calf injury. Hutchinson (knee) may be serious, but that's IDP-irrelevant here. Emmett Johnson (Good Strongs) had 22-101 rushing and 6-70-2 receiving with Walker out. Kaleb Johnson (FA as of Fri) went 10-42, and GB is on bye W11.

**Actions needed (recommendations only, nothing submitted):**
- **Act: restore Yahoo access.** Andrew needs to re-sign in to Yahoo in the box browser. Agents must not log in themselves. **Deadline: Tue Nov 17 afternoon CT**, so waiver/FA status and W11 projections can be pulled before Tuesday-night waivers. Waivers have run at about 3:45 AM CT Wed before; the exact time is unverified.
- **Prepare: W11 lineup (Andrew decides).** Fill QB2 for Love (Mendoza plus Caleb Williams or Nix), WR for Golden, and the W/R flex for Marks. For flex, consider Rice, Downs or Odunze; Judkins is on bye. **The first W11 lock is Thu Nov 19 7:15 PM CT (HOU–IND: Collins, Marks).** Don't start Marks unless he clears protocol (Texans Wed–Thu reports).
- **Prepare/monitor: RB depth and the roster spot.** Marks is concussed and Montgomery may return, and Worthy has been unproductive. Consider re-evaluating Worthy or Marks as drop candidates for a W11 add **once Yahoo FA lists are visible**. Any add/drop or FAAB bid needs Andrew's approval.
- **Monitor:** CMC and Mendoza in the second half (SF@DAL, SEA@LV), then Henry Mon 7:15 PM CT (BAL vs LAC, Brissett at QB).

## Material items
| id | type | what / when (CT) | source (pub → retrieved) | owners | implication | response | deadline | conf. |
|---|---|---|---|---|---|---|---|---|
| marks-concussion | fact (official/beat) | Marks concussion, ruled out Q3 (~1:45–2:15 PM) | ESPN DJ Bien-Aime 2:50 PM → 5:10 PM; NFL.com roundup | Vaqueros (W/R starter) | W10 ≈7.0; W11 TNF short week → likely OUT/at risk; ROS role shrinks if Montgomery returns | prepare (W11 flex alt) | Thu 11/19 7:15 PM | high (fact) / mod (W11 inference) |
| swap-cost | inference (public stats) | Rice ≈10.7 (BN) vs Marks ≈7.0 (W/R) | gamebooks/ESPN API 5:01 PM | Vaqueros | ≈ −3.7 vs not swapping | none (sunk) | — | moderate (est. scoring) |
| w10-outlook | inference | Vaqueros ≈92 + live/MNF vs opp ≈155 final + live | ESPN API 5:01–5:15 PM; TNF scores from Yahoo 11/14 | both | W10 loss very likely | none | — | high (direction) |
| starters-active | fact (official) | no Vaqueros starter inactive | team inactives 10:30 AM; FantasyPros/ESPN | Vaqueros | as set | none | — | high |
| collins-volume | fact | Collins 9-94-1, 16 tgts; HOU W11 TNF vs IND | gamebook; CBS 5:17 PM ET | Vaqueros | locked WR1 W11 (Thu) | start (prepare) | Thu 7:15 PM | high |
| warren-dud | fact + report | 2-1 rec on 3 tgts, near every snap | NBC/Rotoworld 11/15 | Vaqueros | volume concern, no injury; W11 @HOU Thu | monitor | Thu 7:15 PM | high |
| kc-roles | fact | Rice 6 tgt 5-82; Downs 5 tgt 4-53-1; Worthy 3 tgt 0 rec; E. Johnson 22 car + 7 tgt 2 TD; Wiley fx ankle, Kelce calf (brief) | KC@ATL gamebook; NFL.com | Vaqueros (Rice, Downs, Worthy); Good Strongs (E. Johnson) | Downs viable W/T-W/R option; Worthy lowest of the three | monitor | Sun 11/22 noon | high (stats) |
| love-sacks | fact | 220/1/1, sacked 8×, 30-10 loss | gamebook; NBC | Vaqueros | GB bye W11 | none | — | high |
| w11-byes | fact (schedule) | ATL, CLE, GB, LAR, NE, SEA | NFL.com schedule | Love, Golden, Judkins (ours) | need QB2, WR, flex fills | prepare | Thu/Sun locks | high |
| judkins-td | fact | 10-38-1 + 3-33 (BN), GW TD | Browns.com 4:25 PM ET | Vaqueros BN | bye W11 | none | — | high |
| mendoza-bowers | fact | Mendoza rush TD; Bowers (ankle) OUT in-game | ESPN API; NFL.com | Vaqueros (Mendoza) | Bowers loss hurts LV passing if extended (inference) | monitor | W11 | high/low |
| opp-boom | fact | Mahomes 5 TD, Gibbs 2 TD, P. Washington 152-1, DJ Moore 90-1 | gamebooks/ESPN API | Wet Serapas | W10 result | none | — | high |
| league-injuries | fact (official) | Maye ankle, A.J. Brown hamstring, Geno Smith ankle ruled out | NFL.com roundup | ownership unknown (Yahoo down) | possible QB/WR waiver churn | monitor | Tue waivers | high (fact) |
| yahoo-auth | fact (collection) | 302 to login, both jars, 5:00 PM | local attempt | — | no live ownership/FA/proj/FAAB | act (Andrew re-auth) | Tue 11/17 PM | high |

## Would change the assessment
- Texans Wed/Thu reports showing Marks cleared protocol (he'd go back in flex consideration) or Montgomery ruled out again.
- Yahoo final W10 score differing from the public-stat estimate (stat corrections; DEF/K scoring).
- Yahoo FA lists showing a starting-caliber RB/QB free for W11.

## Not verified / gaps (quarantined)
- W10 point estimates are computed from public box scores with league settings. Fumbles lost, 2-pt conversions and FG distances are only partly captured, and DEF scores weren't computed.
- W11 opponent (Deepest) is inferred from rotation, not read from Yahoo.
- Ownership of newly relevant FAs is unknown today (Yahoo down).
- The 3:58 PM CT pregame failure is known only from the parent; no evidence file is in the repo.

## Evidence
- `grok/daily/yahoo-ff-668216/2026/evidence/daily-2026-11-15/` (sources.md, espn-boxscore-extract.txt, yahoo-access-attempt.txt)
- `grok/daily/yahoo-ff-668216/2026/batches/batch_20261115T170000_daily-intel.json`
