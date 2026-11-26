# Deeper Than daily intelligence — 2026-11-26 (CT, Thanksgiving)

- **Routine:** deeper-than-daily-intelligence-report (fired ~4:58 PM America/Chicago; collection ~4:58–5:10 PM CT). NFL **Week 12**. CHI@DET and GB@LAR are Final; PHI@DAL is live (Q2); **KC@BUF kicks off at 7:20 PM CT**.
- **League:** yahoo-ff-668216 / Vaqueros team 8. **W12 opponent: FFAmuseBouche** (inferred from the schedule rotation, not verified on Yahoo).
- **Collection status: PARTIAL. Yahoo FAILED.** 302 to login at 4:58:30 PM CT (jar built from the seed, seed mtime 4:58 PM CT). One attempt; no login, no retry. **16th consecutive Yahoo auth failure on record.** See `evidence/daily-2026-11-26/yahoo-access-attempt.txt`.
- **Not collected from Yahoo (UNKNOWN, NOT zero):** rosters and ownership, FAAB, pending claims, **whether the W12 waivers (~Wed early AM) processed anything for us** (no claim was submitted on record), waiver order, W11 result, W12 opponent, **live W12 score**, FA pool.
- **Public sources OK:**
  - Official: houstontexans.com (Wed/Thu table), raiders.com, giants.com, denverbroncos.com, packers.com recap, NWS Buffalo hourly forecast.
  - Team post: @Ravens Thursday report (image not readable; text taken from Hensley/Zrebiec).
  - Insiders and beat: Schefter, Rapoport, Garafolo, Hensley, Zrebiec, Kaye, Maiocco, Branch.
  - Feeds: ESPN scoreboard, box score and injuries JSON (secondary).
- **Gaps:**
  - I didn't fetch the official BAL, SF, CAR and IND Thursday tables directly. I used Hensley/Zrebiec, Maiocco/Branch, Kaye and the ESPN feed.
  - The Panthers' Thursday report is an **estimate**, because they were off.
  - I didn't fetch the official GB inactives list. Jacobs's inactive status is confirmed by the Packers recap, ESPN's feed (Pelissero) and the box score (no Jacobs line).
  - KC@BUF inactives post about 6:20 PM CT, after this collection.
  - No Yahoo data of any kind.
- **Window:** since daily 2026-11-25 (collection ended ~5:35 PM CT, 9f1309a), through ~5:10 PM CT 11/26. Deduped against the 11/25 report.
- **No Yahoo transactions, lineup changes, claims or messages were made or authorized by this routine.**

## Last-known Vaqueros roster (repo, not current Yahoo)
QB Love, Mendoza · RB Henry, McCaffrey · WR Collins, Golden · TE Warren · W/T McMillan · W/R Marks · BN Rice, C. Williams, LaPorta, Downs, Judkins, Nix, Odunze, Wan'Dale Robinson (season over), Worthy · IR Harvey · K Gay · DEF WAS. FAAB $34 (unverified since 11/14). Which of these were actually in the Wed/Thu lineup slots is **unknown** (no Yahoo since 11/15).

## Andrew-facing summary
1. **Henry is upgraded to FULL participation Thursday.** Hensley (4:42 PM CT) and Zrebiec (3:35 PM CT: "on way out of protocol"). ESPN feed still lists him Questionable.
   - **Fact:** FP Thursday. **Inference:** very likely plays Sun 12:00 PM CT @HOU.
   - **Caveat:** the formal protocol clearance and Friday's game status are still the gate. Keep Judkins as the contingency.
2. **GB@LAR (Wed night) is Final, LAR 26–13.** Box-score facts from the ESPN feed:
   - **Love:** 17/29, 198 yds, 1 TD, **2 INT**, 1 rush for 7.
   - **Golden:** 1 catch for 39 yds on 5 targets.
   - **Jacobs (FFAmuseBouche) was INACTIVE with a finger injury.** The Packers recap and ESPN's feed (Pelissero) say so, and he has no box-score line. This closes the 11/25 relay question.
   - **Kaleb Johnson** led the early downs: 8 carries for 13 yds, plus 1 catch for 19. Brooks was the receiving back, and Lloyd had 1 carry for 10.
   - **RotoWire/CBS (report):** Jacobs is expected back for GB's next game, Sun 12/6. That relegates Kaleb to a reserve role.
   - **Implication:** Kaleb has a very thin ROS case, and it is weaker than the $3–5 lean from 11/24. See Actions.
   - Love and Golden are done for W12.
3. **CHI@DET (Thu noon CT) is Final, CHI 39–35.** ESPN box score:
   - **Caleb Williams:** 30/44, 345 yds, 2 TD, 0 INT, 3 rushes for 15.
   - **Odunze:** 6 catches, 87 yds, **2 TD** on 9 targets.
   - **LaPorta:** 4 catches, 44 yds, 1 TD on 5 targets.
   - **Yahoo fantasy points aren't computed here.** League scoring wasn't re-applied, and I don't know who you started. Whether Caleb, Odunze and LaPorta were in your lineup is unknown (no Yahoo since 11/15); check the lineup once you're signed in.
   - Bears TE Loveland left with a knee injury (not on our roster).
4. **KC @ BUF (Thu 7:20 PM CT): keep Rice, Downs and Worthy benched** (same call as 11/25; inference).
   - **NWS hourly (updated 4:20 PM CT):** rain, PoP 96–100% through about 8 PM ET, 37°F, wind 13–16 mph. The earlier period forecast showed gusts to about 36 mph. @WeatherNFL radar shows a wet and windy game.
   - **Walker is OUT** (Chiefs.com). Emmett Johnson starts and is trade-only (last-known Good Strongs).
   - Rice, Downs and Worthy were not listed out. Inactives post about 6:20 PM CT. If Yahoo access returns before 7:20 PM CT, re-check inactives.
5. **CMC: FULL Thursday (rest, not injury)** (Niners Wire/Maiocco). Wednesday was DNP for rest. **Purdy: DNP again (ankle).**
   - Beat view: "day-to-day, not a high ankle" (Shanahan, via Maiocco). Mac Jones would start if Purdy is out. Schefter: second straight day without practice.
   - **Implication:** if Mac Jones starts, CMC volume is likely fine. I'm not asserting a points change.
   - Check Friday's practice and game status.
6. **McMillan (W/T): Thursday report is an ESTIMATE** (Panthers off). Kaye and @PanthersMagpie say McMillan is projected DNP (foot) along with M. Evans, P. Jones II and Okereke. The ESPN feed says Questionable. **This isn't a real practice absence**; Friday's report is the first actual one.
   - **Prepare:** Warren (Sun noon) is the W/T hedge. Decide by Sun 12:00 PM CT. McMillan plays Monday 7:15 PM CT, so a late McMillan call would conflict with the Sunday lock.
7. **Marks: FP Wednesday and Thursday** (official Texans table, concussion listed). HOU also lists Harrison Jr. FP/FP, and Montgomery LP (rest).
   - Marks hasn't had his clearance reported. FantasyPros expects him to play.
   - I hold the W/R lean at Judkins (SNF) unless Marks is cleared Friday. See lineup notes.
8. **DEN @ PIT Fri 2:00 PM CT:** Nix isn't listed on the Broncos report. Rodgers is inactive and Rudolph starts. Rain is forecast, 43°F (ESPN feed). Bench Nix per the 11/25 plan (QB2 lean).
9. **Other Sunday Vaqueros: clear.**
   - Mendoza and Gay (LV) aren't listed on the Raiders report. Judkins (CLE) isn't listed on the Browns estimate.
   - Warren: Colts Wed not listed, and the Thursday table wasn't captured. ARI starts **Josh Johnson** (Beck back spasms), which is neutral-to-positive for WAS DEF.
10. **League news:**
    - **Aiyuk officially signed with WAS** (Schefter, 11:25 AM CT). This resolves the 11/25 "practice squad, not signed" item. His ownership is unknown.
    - **Rodgers cleared waivers** (Rapoport/Schefter, 3:28–3:54 PM CT) and is a free agent.
    - **Herbert is in the concussion protocol**, and LAC signed Browning.
    - **Pittman was activated** from IR for PIT.
    - Tuten (FFAmuseBouche, inferred) was DNP Thursday, per the ESPN feed citing O'Halloran.
    - The trade deadline is **Sat 11/28**.

## Actions needed (recommendations only, nothing submitted; each needs your approval)
- **ACT (you): re-sign in to Yahoo in the box browser.** This is the 16th straight failure. I can't see the roster or lineup, W12 score, FAAB, or W12 waiver results.
- **PREPARE (your lineup, by lock; CT):**
  - **Thu 7:20 PM:** keep Rice, Downs and Worthy benched (rain, wind). If any WR slot sits empty, that's a decision for you.
  - **Fri 2:00 PM:** Nix stays benched.
  - **Sun 12:00 PM:**
    - Henry at RB, if he's cleared or listed Questionable-expected-to-play. Fallback Judkins.
    - CMC at RB. Purdy's status matters for game script only.
    - **W/R:** Judkins (SNF) lean. Revisit Marks only if cleared Friday.
    - **W/T:** McMillan vs Warren, decided after Friday's CAR report, no later than Sun noon.
    - **QB2:** Mendoza (SNF) is the only open QB2 option now that CHI is done. Caleb's game is over.
  - **Sun 3:25 PM / 7:20 PM:** nothing else for Vaqueros.
- **MONITOR:**
  - BAL Fri (Henry's formal clearance).
  - CAR Fri/Sat (McMillan).
  - SF Fri (Purdy, CMC).
  - HOU Fri (Marks).
  - KC@BUF inactives (~6:20 PM CT).
  - GB: Watson's concussion and Jacobs's return date.
  - W13 waivers (Wed).
- **CONSIDER before Sat 11/28 (trade end):** I'm not recommending a specific trade without a current roster. Henry's FP Thursday helps his value, and Kaleb's weak outing doesn't change the Henry decision.
- **Kaleb Johnson claim (W13, docs-only):** after 8-13-0 and Jacobs's expected return, I'd lower the lean. **Hold / $0–2 at most** (inference). It needs your approval and a Yahoo session, with the next processing about Wed 12/2.
- **No action:** WAS DEF (@ARI Sun 3:25 PM CT, Josh Johnson starts), K Gay.

## Material items
| id | type | what / when (CT) | source (pub → retrieved) | owners (last-known) | implication (week / ROS / keeper) | response | deadline | conf. |
|---|---|---|---|---|---|---|---|---|
| henry-full | report (identifiable beat) + feed | Henry FULL Thu; "on way out of protocol" | Hensley 4:42 PM; Zrebiec 3:35 PM; @Ravens 3:32 PM → ~5:00 PM | **Vaqueros RB** | W12 start likely; clearance still a gate | prepare (Judkins fallback) | Sun 11/29 12:00 PM (Fri BAL status) | moderate-high |
| gb-lar-final | fact (ESPN box, official recap) | LAR 26–13; Love 198/1/2 INT; Golden 1-39; Jacobs inactive | packers.com 12:35 AM; ESPN feed → ~4:59 PM | **Vaqueros QB/WR** (done W12); Jacobs FFAmuseBouche | W12 closed for Love/Golden; opp RB hit | none | — | high |
| jacobs-confirmed | fact + report | Jacobs (finger) inactive; expected back next GB game 12/6 (RotoWire/CBS) | recap; CBS 12:32 AM ET; NBC 3:46 PM → ~5:07 PM | FFAmuseBouche | opp RB slot lost for W12; Kaleb reserve role ROS | monitor | Wed 12/2 waivers | high (inactive) / moderate (return) |
| kaleb-line | fact | 8-13-0 rush, 1-19 rec; Brooks receiving back | ESPN box; PFF → ~5:07 PM | unknown (Yahoo) | claim lean lowered to hold/$0–2 | prepare (docs only) | Tue/Wed 12/1–12/2 | moderate |
| chi-det-final | fact (ESPN box) | Caleb 345/2 TD, 15 rush; Odunze 6-87-2; LaPorta 4-44-1 | ESPN feed → ~4:59 PM | **Vaqueros BN (last-known)** | check what was started | no action | — | high |
| kc-buf-wx | fact (official forecast) | Rain 96–100% PoP, 37°F, wind 13–16 mph hourly | NWS 4:20 PM → ~4:59 PM | **Rice/Downs/Worthy (BN)** | keep benched | prepare | Thu 7:20 PM | moderate-high |
| walker-out | fact | Walker OUT; E. Johnson starts | Chiefs.com → ~5:08 PM | E. Johnson = Good Strongs | trade-only | no action | Thu 7:20 PM | high |
| cmc-fp-purdy-dnp | report (beat + insider) | CMC FP (rest); Purdy DNP x2 | Maiocco/Branch 4:39–4:43 PM; Schefter 4:10 PM → ~5:03 PM | **Vaqueros RB** | Mac Jones risk; volume neutral-positive | monitor | Fri SF report; Sun 3:25 PM | moderate |
| mcmillan-est | report (beat; estimate) | McMillan projected DNP foot (Thu estimate) | Kaye 3:20 PM; @PanthersMagpie 3:36 PM → ~5:00 PM | **Vaqueros W/T** | Warren hedge | prepare | Fri CAR report; Sun 12:00 PM | moderate-low |
| marks-fp | fact (official table) | Marks FP Wed/Thu, concussion listed | houstontexans.com → ~5:05 PM | **Vaqueros (W/R last-known)** | clearance not reported | monitor | Fri HOU; Sun 12:00 PM | moderate |
| sunday-clear2 | fact (official) | Mendoza/Gay/Judkins/Nix not listed | raiders.com 2:05 PM; denverbroncos.com 12:51 PM → ~5:06 PM | **Vaqueros** | none | none | Sun / Fri | high |
| aiyuk-signed | fact (insider) | Aiyuk signed with WAS | Schefter 11:25 AM → ~5:02 PM | unknown | minor | no action | — | high |
| rodgers-fa | fact (insiders) | Rodgers cleared waivers | Rapoport 3:28 PM; Schefter 3:54 PM → ~5:02 PM | n/a | none | no action | — | high |
| yahoo-auth | fact (collection) | 302 login 4:58 PM; 16th straight | local | — | blind on lineup/score/waivers | act (Andrew re-auth) | before Thu 7:20 PM | high |

## Would change the assessment
- Henry not cleared by Fri/Sat, or listed Doubtful/Out. That moves Judkins to RB.
- KC inactives showing Rice/Worthy/Downs active with a dry-weather turn. That brings the KC WRs back into flex consideration.
- McMillan DNP Friday (a real practice), or a CAR downgrade. That puts Warren at W/T.
- Purdy ruled out. That's a mild SF offense and CMC game-script change.
- Marks formally cleared Friday. That puts him in the W/R conversation.
- Yahoo showing a processed W12 claim, a different W12 opponent, or Kaleb/A. Williams on our roster.

## Not verified / gaps (quarantined)
- See `grok/intel/yahoo-ff-668216/2026/quarantine/2026-11-26-daily-unvalidated.md`.

## Evidence
- `grok/daily/yahoo-ff-668216/2026/evidence/daily-2026-11-26/`: sources.md, yahoo-access-attempt.txt, official-reports-extract.txt, espn-feed-extract.txt, espn-injuries-extract.txt, nws-buffalo-forecast.txt, x-search-extract-1..3.txt
- `grok/daily/yahoo-ff-668216/2026/batches/batch_20261126T165800_daily-intel.json`
