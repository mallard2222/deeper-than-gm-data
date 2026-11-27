# Deeper Than daily intelligence — 2026-11-27 (CT, Black Friday)

- **Routine:** deeper-than-daily-intelligence-report (fired ~4:58 PM America/Chicago; collection ~5:00–5:30 PM CT). NFL **Week 12**. Finals: GB@LAR, CHI@DET, PHI@DAL, KC@BUF, DEN@PIT. Next kickoff **Sun 12:00 PM CT** (11 early games incl. BAL@HOU).
- **League:** yahoo-ff-668216 / Vaqueros team 8. **W12 opponent: FFAmuseBouche** (inferred from the schedule rotation, not verified on Yahoo).
- **Collection status: PARTIAL. Yahoo FAILED.** 302 to login at 5:00:08 PM CT (jar built from the seed, seed mtime 4:59:54 PM CT, 57 yahoo cookies). One attempt; no login, no retry. **17th consecutive Yahoo auth failure on record.** See `evidence/daily-2026-11-27/yahoo-access-attempt.txt`.
- **Not collected from Yahoo (UNKNOWN, NOT zero):** rosters and ownership, FAAB, pending claims, W12 waiver outcome, waiver order, W11 result, W12 opponent, **live W12 score**, FA pool, transactions.
- **Public sources OK:**
  - Official: houstontexans.com (Wed–Fri table incl. Ravens), panthers.com, buccaneers.com, raiders.com (incl. Browns table), colts.com, nfl.com (Purdy).
  - Insiders (X API, read-only): Schefter, Rapoport, Wagoner, A. Wilson, Caplan (via RotoWire relay).
  - Feeds: ESPN scoreboard, box score and injuries JSON (secondary).
- **Gaps:**
  - The 49ers table is via 49erswebzone/NFL.com relay, not fetched from the club directly.
  - Colts: Warren's "not listed" is inferred from the club's ruled-out/questionable article (the table wasn't captured).
  - No official Packers source captured for Jacobs's Friday status.
  - Waiver/FAAB aggregator lists are low quality (quarantined).
  - No Yahoo data of any kind. The collection is a point-in-time snapshot, not continuous monitoring.
- **Window:** since daily 2026-11-26 (collection ended ~5:10 PM CT, d7cb447), through ~5:30 PM CT 11/27. Deduped against the 11/26 report.
- **No Yahoo transactions, lineup changes, claims or messages were made or authorized by this routine.**

## Last-known Vaqueros roster (repo, not current Yahoo)
QB Love, Mendoza · RB Henry, McCaffrey · WR Collins, Golden · TE Warren · W/T McMillan · W/R Marks · BN Rice, C. Williams, LaPorta, Downs, Judkins, Nix, Odunze, Wan'Dale Robinson (season over), Worthy · IR Harvey · K Gay · DEF WAS. FAAB $34 (unverified since 11/14). Which of these were in the W12 lineup slots (Thu/Fri games) is **unknown** (no Yahoo since 11/15).

## Andrew-facing summary
1. **Henry is CLEARED: no injury designation for Sun noon CT @HOU.**
   - **Fact (official):** Texans' official table (2:42 PM CT) lists BAL Henry LP Wed / FP Thu / FP Fri, game status not listed.
   - **Report (identifiable original):** Caplan (SiriusXM) via RotoWire, 2:49 PM CT: no designation, cleared protocol, practiced without limitation Thu/Fri. Aaron Wilson (BAL beat), 3:06 PM CT: "clearing NFL concussion protocol."
   - **Inference:** he starts and has a normal workload. Judkins is no longer needed as the RB fallback.
2. **Marks (HOU): FP Wed/Thu/Fri, no designation** (official Texans table). The Texans haven't announced "cleared protocol" in words I could find. No-designation is strong evidence, but formal clearance is inferred. That makes Marks a live W/R option against Judkins (SNF).
3. **McMillan (CAR, MNF 7:15 PM CT): LIMITED Friday.** The first real practice report came from the official panthers.com (2:52 PM CT).
   - **Fact:** he was DNP on Thursday as a projection only (no practice). He was limited Friday. Person (The Athletic) via RotoWire: out of the team-stretch period, then suited up. Evans, Brooks and Young were full.
   - **Report:** Canales expressed optimism this week (Kaye).
   - **Inference:** probable but not certain. Saturday is the last report, and a designation is possible. See Actions for the Warren hedge.
4. **Purdy is OUT (ankle). Mac Jones starts for SF vs SEA.**
   - **Fact:** Schefter 4:21 PM CT, Rapoport 4:22 PM CT, NFL.com. Shanahan said the sprain was "more mid than low," no surgery, and he's "optimistic" about Week 13.
   - **Fact (official table via relay):** CMC was FP on Friday (rest). He is not on the injury list.
   - **Inference:** CMC volume is likely fine or better in a Jones game. This is not a points projection.
5. **KC@BUF is Final: BUF 13, KC 10.**
   - **Facts (ESPN box):** Rice 2-19 on 5 targets. Downs 1-13 on 4 targets (16 offensive snaps per NBC). Worthy 0 catches on 3 targets.
   - **Fact:** E. Johnson 17-72-1 rushing, 4-24 receiving.
   - **Inference:** benching Rice, Downs and Worthy was correct. Lineup use is unknown.
   - **Report (RotoWire/CBS):** Worthy has averaged 3.3 targets per game since Downs arrived. An SI analyst suggests dropping him. ROS value for Worthy and Downs is low-to-uncertain.
6. **DEN@PIT is Final: PIT 27, DEN 5.**
   - **Facts (ESPN box):** Nix 22/40, 169 yds, 0 TD, **2 INT** (a T.J. Watt fumble recovery and a Ramsey pick-six, per PFT), 3 sacks. Rudolph threw 1 TD.
   - **Inference:** Nix was benched per the plan, so the bad line costs nothing in W12. It lowers his QB2 and ROS appeal.
7. **Sunday starters are clear.**
   - **Mendoza and Gay (LV@CLE SNF):** not listed on the Raiders report (official, 1:45 PM CT).
   - **Judkins (CLE):** not listed. RB Sanders is Questionable (hip, LP x3). That could modestly raise Judkins's workload (inference).
   - **Warren (IND vs NYG):** not among the Colts' ruled-out or questionable players. He has no injury designation (absence-based).
   - **WAS DEF @ARI:** **Josh Johnson starts** (Beck out, back spasms). Fact: Schefter 11:29 AM CT and Rapoport 11:32 AM CT, plus the Cardinals report. Mild positive for the defense (inference).
8. **League news (not on our roster, last-known):**
   - **Herbert** is out vs NE. **DJ Uiagalelei** makes his first start, with Browning as backup. Fact: Schefter 4:15 PM CT, Rapoport 4:19 PM CT.
   - **Tuten (JAX, FFAmuseBouche inferred)** is OUT vs TEN. Fact: Schefter 3:29 PM CT.
   - **Walker (KC)** has a Grade-2 groin strain (ESPN/PFN). The Thu 12/3 return at LAR is an aggregator view, not an official statement. Johnson is the starter if Walker is out.
   - **Loveland (CHI)** is week-to-week per Bears (1:05 PM CT).
   - **Rodgers** remains a free agent. A second-hand claim that he was "barred" (Al Michaels relay) is quarantined.
   - **Jacobs (FFAmuseBouche):** next GB game is Sun 12/6 at NO. I couldn't capture an official Friday status. An aggregator says Out for 12/6, which is unreliable. **Kaleb claim lean is unchanged: hold / $0–2 docs-only.**

## Actions needed (recommendations only, nothing submitted; each needs your approval)
- **ACT (you): re-sign in to Yahoo in the box browser.** This is the 17th straight failure. I can't see the roster, lineup, W12 score, FAAB, waivers or trade offers.
- **ACT/CONSIDER before Sat 11/28 (league trade end; exact hour not recorded):** with no Yahoo data I'm not recommending a trade. Henry's clearance and Mendoza's captaincy don't change that. If you want to trade, it needs a live roster view first.
- **PREPARE (your lineup; CT):**
  - **Sun 12:00 PM:**
    - Henry and CMC at RB.
    - **W/R:** Judkins (SNF) vs Marks (HOU, noon). Marks is the cleaner volume option if you want a noon player. Judkins's SNF slot lets you wait. This is your call; the relevant fact is that Marks has no designation.
    - **W/T:** McMillan (MNF) vs Warren (Sun noon). **Decide by Sun 12:00 PM CT** after Saturday's CAR report. A McMillan "Questionable" designation, or any downgrade, means Warren.
    - **QB2:** Mendoza (SNF) is the only QB2 choice. Love's game is over.
  - **Sun 3:25 PM:** WAS DEF @ARI. No action.
- **MONITOR:**
  - CAR Saturday report (McMillan designation).
  - Sunday inactives (~11:30 AM CT for noon games, ~2:30 PM CT for 3:25).
  - Walker (KC) and Jacobs (GB) updates.
  - Wed W13 waivers (~12/2): Emmett Johnson (an aggregator says he remained available after W12 waivers; ownership disputed/unknown), Kaleb (hold), Hurst (aggregator only).
- **No action:** K Gay, Collins, Golden, Love (W12 done for GB), LaPorta/Odunze/Caleb (W12 done).

## Material items
| id | type | what / when (CT) | source (pub → retrieved) | owners (last-known) | implication (week / ROS / keeper) | response | deadline | conf. |
|---|---|---|---|---|---|---|---|---|
| henry-cleared | fact (official table) + report (Caplan, Wilson) | Henry no designation; FP Thu/Fri | houstontexans.com 2:42 PM; RotoWire/Caplan 2:49 PM; Wilson 3:06 PM → ~5:10 PM | **Vaqueros RB** | starts Sun noon; Judkins fallback not needed | prepare (start) | Sun 12:00 PM | high |
| marks-fp3 | fact (official) | Marks FP x3, not listed | houstontexans.com 2:42 PM → ~5:10 PM | **Vaqueros W/R** | W/R candidate vs Judkins; formal protocol clearance not stated | prepare | Sun 12:00 PM | moderate-high |
| mcmillan-lp | fact (official) | McMillan LP Fri (foot); Sat last report | panthers.com 2:52 PM; buccaneers.com 3:11 PM → ~5:12 PM | **Vaqueros W/T** | MNF; Warren hedge | prepare/monitor | Sun 12:00 PM | moderate |
| purdy-out | fact (insiders + NFL.com) | Purdy OUT; Mac Jones starts | Schefter 4:21 PM; Rapoport 4:22 PM → ~5:14 PM | CMC **Vaqueros** | CMC game script only; Purdy W13 optimistic | monitor | Sun 3:25 PM | high |
| cmc-fp | fact (club report via relay) | CMC FP Fri (rest) | 49erswebzone (~4:30 PM) → ~5:14 PM | **Vaqueros RB** | available | none | — | high |
| kc-buf-final | fact (ESPN box) | BUF 13–10; Rice 2-19, Downs 1-13, Worthy 0-3 tgt; E. Johnson 17-72-1 | ESPN feed → ~5:05 PM | Rice/Downs/Worthy **Vaqueros bench**; E. Johnson owner disputed | KC WRs low ROS; Worthy drop-candidate (analyst) | no action (W12 closed) | W13 waivers ~12/2 | high |
| den-pit-final | fact (ESPN box) | PIT 27–5; Nix 22/40 169 0/2 INT | ESPN feed; PFT → ~5:19 PM | Nix **Vaqueros bench** | QB2/ROS dip | no action | — | high |
| sun-clear | fact (official) | Mendoza/Gay/Judkins not listed; Warren not listed (absence-based) | raiders.com 1:45 PM; colts.com 1:24 PM → ~5:17 PM | **Vaqueros** | none | none | Sun | high / mod (Warren) |
| was-def | fact (insiders) | ARI: J. Johnson starts | Schefter 11:29 AM → ~5:21 PM | **Vaqueros DEF** | mild positive | none | Sun 3:25 PM | high |
| herbert-out | fact (insiders) | Herbert out; Uiagalelei starts | Schefter 4:15 PM → ~5:25 PM | n/a (QB market) | LAC passing downgrade | monitor | Sun | high |
| tuten-out | fact (Schefter) | Tuten OUT vs TEN | Schefter 3:29 PM → ~5:25 PM | FFAmuseBouche (inferred) | opp. RB loss; Rodriguez lead (aggregator) | monitor | Sun noon | high (status) / low (ownership) |
| walker-groin | report (ESPN/PFN) | Grade-2 groin; Thu 12/3 return is aggregator view | ESPN, PFN → ~5:18 PM | Walker/E. Johnson owner unknown | E. Johnson hold value | monitor | KC Thu 12/3 | moderate |
| jacobs-gb | unverified | GB next game 12/6; Friday status not captured | aggregators → ~5:22 PM | FFAmuseBouche | Kaleb hold/$0–2 | monitor | W13 waivers ~12/2 | low |
| yahoo-auth | fact (collection) | 302 login 5:00 PM; 17th straight | local | — | blind on lineup/score/waivers | act (Andrew re-auth) | before Sun 12:00 PM | high |

## Would change the assessment
- McMillan designated Questionable/Doubtful Saturday, or a late DNP: Warren at W/T.
- Henry or Marks inactive (the 11:30 AM CT inactives list), or any in-game concussion: Judkins moves to RB, or W/R changes.
- Yahoo showing a processed W12 claim, a different W12 opponent, or Kaleb, Emmett Johnson or A. Williams on our roster.
- Walker formally ruled out for 12/3: Emmett Johnson's value up.
- Official Packers word that Jacobs is out for 12/6: Kaleb's value up.
- Trade-deadline hour or keeper rules found in Yahoo league settings.

## Not verified / gaps (quarantined)
- See `grok/intel/yahoo-ff-668216/2026/quarantine/2026-11-27-daily-unvalidated.md`.

## Evidence
- `grok/daily/yahoo-ff-668216/2026/evidence/daily-2026-11-27/`: sources.md, yahoo-access-attempt.txt, official-reports-extract.txt, espn-feed-extract.txt, rotowire-caplan-extract.txt, x-search-extract-1.txt
- `grok/daily/yahoo-ff-668216/2026/batches/batch_20261127T165800_daily-intel.json`
