# Yahoo W04 waiver reconciliation — Deeper Than

**League:** Deeper Than (`yahoo-ff-668216`)  
**Team:** Vaqueros (team ID `8`)  
**Season / week:** 2026 / W04  
**Reconciled:** Wed Sep 30, 2026, approximately **8:03–8:05 AM America/Chicago**  
**Reconciliation method:** curl + Netscape cookie jar (logged-in Yahoo UI); no Yahoo mutations.

This is an additive outcome record for Wednesday post-processing. The Tue Sep 29 docs-only [RECOMMENDATION.md](./RECOMMENDATION.md) remains unchanged as the historical recommendation. The prior Tue AM `reconciliation.*` state check (FAAB $79, no pending) is superseded by this Wed post-process file.

## Processing state

- League waiver processing **completed** — visible winning claims stamped **Sep 30, 3:42 am** (timezone unlabeled on Yahoo; consistent with prior W03 “3:46 am” pattern). One later FA add: Good Strongs Kenyon Sadiq / drop Chiefs DEF at **Sep 30, 7:11 am**.
- **Vaqueros submitted no W04 claims.** Tuesday desk was docs-only; there is no W04 `execution-record` with submitted bids. Recommended ≠ submitted ≠ failed.
- Pending claims remaining: **none inferred** (roster unchanged; FAAB unchanged; no Vaqueros rows on transactions). Pending-claims UI URL returned “document not found” (quarantined).

## Outcome summary

- **Vaqueros claims:** none submitted → **no success / no fail / no spend**.
- **FAAB:** still **$79** (unchanged from post-W03).
- **Roster deltas:** **none** — same 20 players as Tue capture (Packers DEF, Pittman, Caleb, Reed, etc. still rostered).
- **IR:** still **0 of 1**.
- **Record / rank (team page):** **0-3-0**, **8th** place.

## Claim-level reconciliation (recommended vs submitted vs outcome)

| Priority | Recommended (Tue docs-only) | Submitted? | Processed outcome | Spend |
|---|---|---|---|---:|
| P1 | Add Ravens DEF ~$4 (max $10); drop Packers DEF · fallback Bears DEF $2–6 | **Not submitted** | **not_submitted** — Ravens still **FA**; Bears DEF won by Wet Serapas $3 | $0 |
| P2 | Optional Jordan Addison ~$8 (max $18); drop Pittman or IR-free BN | **Not submitted** | **not_submitted** — Addison won by Good Strongs **$9** | $0 |
| P3 | Optional Braelon Allen / Kenny Gainwell $1–5 (max $8) | **Not submitted** | **not_submitted** — Allen won by Good Strongs **$30**; Gainwell still **FA** | $0 |
| IR ask | Caleb → IR (preferred) or Reed → IR | **Not submitted** | IR still empty (0/1); both still on BN | — |

## League-wide winning claims (verified Sep 30 transactions only)

Winning prices shown are the amounts Yahoo displayed on the transactions feed. Private losing bids are **not** visible and are not invented.

| Add | Bid | Drop | Team | When (Yahoo display) |
|---|---:|---|---|---|
| Kenyon Sadiq | FA | Chiefs DEF | Good Strongs | Sep 30, 7:11 am |
| Chris Bell | $0 | Brian Thomas Jr. | Good Strongs | Sep 30, 3:42 am |
| Keenan Allen | $3 | Kyle Pitts Sr. | Baby Arm | Sep 30, 3:42 am |
| Bears DEF | $3 | Dallas Goedert | Wet Serapas | Sep 30, 3:42 am |
| Kirk Cousins | $5 | Baker Mayfield | Good Strongs | Sep 30, 3:42 am |
| Jakobi Meyers | $7 | Chris Godwin Jr. | Good Strongs | Sep 30, 3:42 am |
| Jordan Addison | $9 | Dalton Schultz | Good Strongs | Sep 30, 3:42 am |
| Steelers DEF | $10 | Eagles DEF | Big Balls | Sep 30, 3:42 am |
| Braelon Allen | $30 | Tank Bigsby | Good Strongs | Sep 30, 3:42 am |

No Vaqueros transaction appears in this Sep 30 window.

## Notable newly dropped players + waiver-clear timing

From verified drop sides of Sep 30 transactions + FA list badges. Clear labels where shown.

| Player | Dropped by | Clear / status shown | Relevance to Vaqueros |
|---|---|---|---|
| Chiefs DEF | Good Strongs | **W (Oct 2)** | DEF stream watch only |
| Eagles DEF | Big Balls | **W (Oct 2)** | DEF stream watch only |
| Dallas Goedert | Wet Serapas | **W (Oct 2)** (also D) | TE depth; low need (Warren/LaPorta) |
| Brian Thomas Jr. | Good Strongs | **W (Oct 2)** | High-upside WR; watch when clears |
| Chris Godwin Jr. | Good Strongs | **W (Oct 2)** | WR depth watch |
| Dalton Schultz | Good Strongs | **W (Oct 2)** | TE; low need |
| Kyle Pitts Sr. | Baby Arm | To Waivers (Sep 30) | TE; low need |
| Baker Mayfield | Good Strongs | To Waivers (O) | QB; low need (Love/Nix) |
| Tank Bigsby | Good Strongs | **W (Oct 2)** | RB depth lottery |
| Ravens DEF | — (still pool) | **FA** | Top Tue DEF rec **still available** as FA |
| Kenny Gainwell | — (still pool) | **FA** | Optional low-priority RB still available |

No new Yahoo claims are authorized from this outcome note.

## Evidence

- [recon-2026-09-30/](./evidence/recon-2026-09-30/) — raw HTML + SOURCE-NOTES + extracts
- Related historical records preserved unchanged: [RECOMMENDATION.md](./RECOMMENDATION.md) (Tue docs-only plan)
