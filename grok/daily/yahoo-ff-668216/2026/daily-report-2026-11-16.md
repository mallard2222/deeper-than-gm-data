# Deeper Than daily intelligence — 2026-11-16 (CT)

- **Routine:** deeper-than-daily-intelligence-report (≈4:55–5:15 PM America/Chicago)
- **League:** yahoo-ff-668216 / Vaqueros team 8 (W10 matchup vs Wet Serapas, MNF still to play; W11 opponent inferred Deepest/Jeremy, unverified)
- **Collection status: PARTIAL FAILURE.** Yahoo again returned **302 to login** with both cookie jars at 4:56 PM CT (one retry; no login attempted). The seed file had re-synced at 4:55 PM, but the Yahoo session inside it is still invalid. See `evidence/daily-2026-11-16/yahoo-access-attempt.txt`. Public sources are OK: ESPN public API (4:56–4:58 PM CT), team sites/beat reporters, NFL.com Monday roundup.
- **Yahoo-dependent fields are STALE:** live matchup score/projection, ownership, FA status, FAAB, pending claims, W11 projections. Last values: lineup/roster 2026-11-15 11:27 AM CT; matchup/FA/transactions/projections 2026-11-14 ~5:05–5:31 PM CT; FAAB $34 (unverified since Nov 14 Worthy add). This morning's 10:59 AM CT pregame check also failed, and that routine is paused (per parent; no repo record from that run).
- **Previous daily:** 2026-11-15 ~5:00 PM CT (a223356, partial). Window: Nov 15 ~5:15 PM → Nov 16 ~5:10 PM CT.
- **No Yahoo transactions, lineup changes, claims or messages were made or authorized by this routine.**

## Andrew-facing summary
1. **Marks is effectively OUT for W11.** Ryans: "Woody was diagnosed with a concussion… Probably won't have him for Thursday night. Not enough time." This is a fact (coach quote); the official designation comes on the Texans' Wed/Thu reports. AP says Montgomery (Wet Serapas BN) is expected to miss a fifth straight game, while Ryans was "not certain" Monday. That leaves Emari Demercado as the likely HOU starter (report). **Don't plan Marks in any W11 slot.**
2. **W10 is still very likely a loss, even with CMC's huge night.** These are public-stat estimates; Yahoo is unavailable. CMC finished 13-62-1 rush and 4-161-2 rec (≈42.3). Mendoza finished 143 yds, 0 TD/INT, 6-22-1 rush (≈13.9). Gay went 2/2 FG (long 43) + 1 XP (≈8–9). That puts Vaqueros at **≈124 + Henry (MNF) + our DEF (not computed)**. Wet Serapas added JSN 8-171-1 (≈27.1), McBride 5-37 (≈6.2) and Rams DEF (6 pts allowed, 5 sacks, 2 INT ≈19), for **≈207**. Henry can't plausibly close an ≈80-pt gap (inference, high).
3. **Henry, MNF tonight 7:15 PM CT vs LAC: in progress/upcoming, no score.** He isn't on the Ravens' injury report (ESPN list, 4:58 PM CT). Official inactives are due ~5:45 PM CT, after this cutoff. LAC: McConkey OUT (Wet Serapas BN; no effect on their starters).
4. **Bowers (LV TE) is day-to-day:** "significant… not as bad as we thought" (Kubiak, Mon). PFT's source says he "should be good to go" at DEN. That matters for Mendoza's W11 (Sun 3:25 PM CT @DEN, outdoor).
5. **KC:** Reid says Wiley "looks like he fractured his ankle." Kelce's calf was minor ("I'm all good"). Schefter: Walker was shut down for "a week," so he's expected back W11 vs ARI. That cuts Emmett Johnson's (Good Strongs) role, and **Rice/Downs/Worthy target share is unchanged (inference).**
6. **W11 lineup holes (Andrew decides):** QB2 (Love on bye). Candidates are Caleb Williams (vs NO, Sun noon) and Nix (vs LV, Sun 3:25 PM). Both are coming off byes with no designation. WR2 (Golden bye) and W/R flex (Marks out; Judkins bye) can come from Odunze, McMillan (CAR vs BAL, Sun noon), Rice or Downs (vs ARI Sun noon). **The first lock is Thu 11/19 7:15 PM CT: Collins and Warren (HOU vs IND, indoor).**
7. **League-wide:** Maye feared fractured ankle; Vrabel doesn't expect him back after the bye. A.J. Brown (NE) is getting hamstring imaging; NE is on bye. Geno Smith is getting ankle imaging; Klubnik starts if he can't. Mayfield has a lower-leg injury and the Bucs signed Cooper Rush. Addison (MIN) needs thumb surgery and could go to IR. Darnold is "really optimistic" for W12. Njoku (LAC) is off IR. Hutchinson tore his ACL (IDP-irrelevant). **Deeper Than ownership of all of these is unknown (Yahoo stale).**

**Actions needed (recommendations only, nothing submitted):**
- **Act: restore Yahoo access.** Andrew re-signs in to Yahoo in the box browser. Agents must not log in. **Deadline: Tue Nov 17 ~3 PM CT**, so FA lists, W11 projections, FAAB and the matchup can be read before Tuesday-night waivers. Processing has historically been ~3:45 AM CT Wed; exact time unverified.
- **Prepare: W11 lineup (Andrew decides) before Thu 11/19 7:15 PM CT** for Collins and Warren. Marks must not occupy the W/R slot. Set the W/R fill (Rice/Downs/Odunze/McMillan) and QB2 (Caleb Williams or Nix) before Sun 12:00 PM CT. Any lineup change needs Andrew's OK unless it falls under the OUT/bye rule.
- **Prepare: roster-spot decision.** Marks (out W11, and his role shrinks once Montgomery is back) and Worthy (0 catches W10) are the drop candidates. A possible W11 RB add is Demercado (HOU TNF starter if Montgomery sits; ownership unknown). **Any add/drop or FAAB bid needs Andrew's explicit approval** and Yahoo access; claim deadline Tue night CT.
- **Monitor:** Henry MNF (inactives ~5:45 PM CT; kickoff 7:15 PM CT); Texans Mon–Wed reports (Marks/Montgomery); Raiders practice (Bowers, Wed); Kelce practice (Wed).

## Material items
| id | type | what / when (CT) | source (pub → retrieved) | owners | implication | response | deadline | conf. |
|---|---|---|---|---|---|---|---|---|
| marks-w11-out | fact (coach quote) / official desig. pending | Ryans: Marks in protocol, "probably won't have him for Thursday night" (postgame Sun; Texans Wire Mon 12:32 PM) | Texans Wire 11/16 12:32 PM → 5:00 PM; ESPN 11/15 2:50 PM | Vaqueros (BN/W-R candidate) | W11 zero; ROS shrinks when Montgomery returns | prepare (exclude from W11) | Thu 11/19 7:15 PM | high |
| montgomery-hou | report | Ryans "not certain" Mon; AP: expected to miss 5th straight; Demercado likely starter | FantasyGuru 11/16; AP recap | Wet Serapas (BN) Montgomery; FA? Demercado (unknown – Yahoo stale) | HOU backfield W11 = Demercado if Montgomery sits | monitor / prepare add idea | Tue night (claims) / Thu 7:15 PM | moderate |
| w10-final-sun | fact (stats) + inference (points) | CMC 13-62-1 + 4-161-2; Mendoza 143/0/0 + 6-22-1; Gay 2/2 FG + 1 XP; JSN 8-171-1; McBride 5-37; LAR D 6 PA/5 sk/2 INT | ESPN API 4:56–4:58 PM | Vaqueros vs Wet Serapas | ≈124 + Henry + DEF vs ≈207 → loss near-certain | none | — | high (direction) / moderate (pts) |
| henry-mnf | fact (status) | MNF LAC@BAL 7:15 PM CT not started at 4:58 PM; Henry not on injury list | ESPN API 4:58 PM; Ravens Wire 11/16 | Vaqueros (RB starter) | plays tonight; result next daily | monitor | 7:15 PM tonight | high |
| bowers-dtd | fact (coach) + report (source) | Kubiak Mon: day-to-day, "significant… not as bad as we thought"; PFT source "should be good to go" | PFT 11/16 4:07 PM (site time); ESPN 11/16 7:46 AM CT | owner unknown (Yahoo stale); affects our Mendoza | if Bowers sits, LV passing downgrade @DEN (inference) | monitor (Wed practice) | Sun 11/22 3:25 PM | high/moderate |
| kc-te-rb | fact (coach) + report | Wiley fx ankle; Kelce calf minor; Walker "shut down for a week" → likely back W11 | Arrowhead Pride 11/15 4:30 PM CT; Chiefs Wire 11/16 2:07 PM CT | Vaqueros Rice/Downs/Worthy; Good Strongs E. Johnson; Kelce owner unknown | KC WR shares steady; EJ falls back to RB2 | monitor | Sun 11/22 noon | moderate |
| cmc-health | fact (coach) | Shanahan Mon: only game injury CB R. Green; CMC no issue | 49ers Webzone 11/16 | Vaqueros | W11 SNF vs MIN (Mexico City, outdoor) start | start (prepare) | Sun 11/22 7:20 PM | high |
| qb2-w11 | fact (status) + inference | Caleb Williams, Odunze no designation post-bye; Nix no news | Bears Wire 11/16; Broncos Wire 11/15 | Vaqueros | QB2 = Caleb (vs NO) or Nix (vs LV); Love bye | prepare | Sun 11/22 12:00 PM | moderate |
| warren-collins-tnf | fact (schedule) / report (Warren not on report) | HOU vs IND Thu 7:15 PM CT, indoor | ESPN W11 scoreboard; colts.com | Vaqueros | first W11 lock | start (prepare) | Thu 11/19 7:15 PM | high (sched) / mod (status) |
| maye | report (Schefter) + coach | feared fractured ankle; Vrabel: not available out of bye | ESPN/PFT 11/16 AM | unknown (Yahoo stale) | QB-needy managers may chase FA QBs (inference) | monitor | Tue night | high |
| league-injuries | fact/report | A.J. Brown imaging; Geno Smith imaging (Klubnik); Mayfield lower leg (Rush signed); Addison thumb surgery/IR possible; Darnold W12 optimistic; Njoku off IR | NFL.com Mon roundup; Bucs Wire; ESPN | unknown (Yahoo stale) | waiver churn; no direct Vaqueros impact | monitor | Tue night | high (facts) |
| yahoo-auth | fact (collection) | 302 to login, both jars, 4:56 PM (2nd straight daily + 10:59 AM pregame) | local attempt | — | no ownership/FA/proj/FAAB/claims | act (Andrew re-auth) | Tue 11/17 ~3 PM | high |

## Would change the assessment
- Texans' official injury reports (Mon estimated/Tue/Wed) listing Marks as anything other than OUT, or Montgomery as a full go. A Montgomery return would kill the Demercado idea.
- Yahoo final W10 score differing from the public estimate (DEF, FG distances, stat corrections) or Henry's MNF line. Henry would need ≈80+ pts to flip it.
- Bowers missing Wed–Fri practice, which would push Mendoza toward the bench in favor of Caleb Williams or Nix.
- Yahoo FA lists showing a startable W11 RB/WR. Deepest's actual roster/projections once Yahoo is back.

## Not verified / gaps (quarantined)
- W10 point estimates come from public box scores × league settings. Our DEF wasn't computed, one Gay FG distance is unknown, and LAR DEF return TDs weren't checked. Henry is pending.
- The W11 opponent (Deepest) is a rotation inference, not read from Yahoo.
- Ownership of all newly relevant players (Demercado, Freiermuth, QBs) is unknown.
- Warren's "not on Monday report" comes from a search summary of colts.com/CBS, not a fetched official report.
- The 10:59 AM CT pregame failure is parent-reported only, with no evidence file in the repo.

## Evidence
- `grok/daily/yahoo-ff-668216/2026/evidence/daily-2026-11-16/` (sources.md, espn-boxscore-extract.txt, yahoo-access-attempt.txt)
- `grok/daily/yahoo-ff-668216/2026/batches/batch_20261116T170000_daily-intel.json`
- Quarantine: `grok/intel/yahoo-ff-668216/2026/quarantine/2026-11-16-daily-unvalidated.md`
