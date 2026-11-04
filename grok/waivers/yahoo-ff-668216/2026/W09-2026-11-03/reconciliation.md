# Yahoo W09 waiver reconciliation — Deeper Than

**League:** Deeper Than (`yahoo-ff-668216`) · **Team:** Vaqueros (team ID `8`) · **Season / week:** 2026 / W09
**Reconciled:** Wed Nov 4, 2026, Yahoo checks **8:01:39–8:04:03 AM CT** (America/Chicago)
**Method:** curl + Netscape cookie jar (logged-in Yahoo HTML pages); read-only. **No Yahoo claims, bids, drops, IR moves, trades, or lineup changes were made by this run.**

Additive record. The Tue Nov 3 docs-only [RECOMMENDATION.md](./RECOMMENDATION.md) and all other W09 files are unchanged.

## Source of the submitted claim (no execution record)

There is **no W09 `execution-record`** in this folder or elsewhere under `grok/waivers/yahoo-ff-668216/`. The claim was submitted **outside a recorded execution record**. The only prior evidence is the Nov 3 evening daily report ([daily-report-2026-11-03.md](../../../../daily/yahoo-ff-668216/2026/daily-report-2026-11-03.md)), which saw the team-page panel *"Waiver 1 (Nov 4): Bid $15 for Mike Washington Jr."* at 4:57 PM CT. Who submitted it and when are not shown by Yahoo (**unknown**; not this or the Tuesday run). Nothing was recreated or resubmitted.

## Processing state

- **Processed.** Winning claims stamped **Nov 4, 3:46 am** on the transactions and FAB Offers pages (Yahoo says game times are CST; the timestamp itself is unlabeled). Matches the earlier pattern (Sep 23 3:46, Sep 30 3:42, Oct 28 3:42).
- **Pending claims remaining: none.** The team-page waiver panel present on Nov 3 (4:57 PM CT) is **gone** at 8:01 AM CT, the player is on the roster, and FAAB dropped by the bid amount. (The separate pending-claims URL is still treated as unusable; see [quarantine note](../../../../intel/yahoo-ff-668216/2026/quarantine/2026-09-30-pending-claims-ui-document-not-found.md). It was not re-fetched.)
- Post-processing FA activity: Wet Serapas added Adonai Mitchell (5:52 am) and Terrance Ferguson (5:54 am) as free agents.
- No retry needed (processing complete at first check).

## Vaqueros claims

| # | Add | Bid | Drop | Outcome | Paid | Competing bids shown |
|---|---|---:|---|---|---:|---|
| Waiver 1 | Mike Washington Jr. (LV RB, 42744) | $15 | none (open roster spot) | **SUCCESS** | **$15** | Baby Arm $6 (Lower Offer) |

- Failed: **none**. Still pending: **none**.
- Yahoo FAAB is first-price: paid the full $15; second-highest visible bid was $6 ($9 margin).

## Team state after processing (team page 8:01 AM CT)

- **FAAB:** **$64** (was $79; −$15). League home standings table also shows $64.
- **Waiver priority column:** 2 (league home; "Last standings update: Wed Nov 04 01:51am CST" — the priority column may predate processing; FAAB column already reflects spend). Unverified whether priority moved.
- **Waiver moves:** 10 (was 9).
- **Roster:** 20 active-roster players + Harvey on IR. Starting lineup is unchanged from Nov 3 evening; Washington landed on **BN**.
  - Starters: QB Love, Caleb Williams · RB Henry, McCaffrey (Q) · WR Collins, Golden · TE Warren · W/T Rice · W/R McMillan · K Gay · DEF Commanders
  - Bench (9/9): LaPorta, Downs, Judkins, Marks, Nix, Freiermuth (bye), Odunze, Wan'Dale Robinson (bye), **Mike Washington Jr.** (W9 proj 7.77, 36% rostered)
  - IR (1/1): RJ Harvey
- **Open roster spots: 0.** Any further add now needs a drop (or Harvey leaving IR changes nothing — IR is full).
- Record 2-6-0, 7th; W9 vs Big Balls, Yahoo proj 138.36–153.18.

## Recommended vs submitted vs outcome

| Item | Tue desk (docs only) | Submitted (outside execution record) | Outcome |
|---|---|---|---|
| Mike Washington Jr. | $12–18 (max ~$22) | $15, no drop | **Won**, $15 paid; next bid $6 (Baby Arm) |
| Kenny Gainwell | optional $3–6 | not submitted | **not_submitted**; still FA (W9 proj 6.70, 43%) |
| Justice Hill | optional $1–3 | not submitted | **not_submitted**; still FA (4.88, 5%) |
| Malik Washington | pass | — | still FA |
| Harvey → IR | recommended | done before Nov 3 4:57 PM CT | IR 1/1 |
| Lineup reset | recommended | done before Nov 3 4:57 PM CT | still set |

Bid was inside the recommended range. In hindsight $7 would have won against the visible bids, but other managers' bids were not known beforehand; Baby Arm ($79 FAAB at the time) could have bid more.

## League-wide winning claims (Nov 4, 3:46 am)

| Add | Price | Drop | Team | Competing bids shown on FAB Offers |
|---|---:|---|---|---|
| Mike Washington Jr. (LV RB) | $15 | — | Vaqueros | Baby Arm $6 |
| Geno Smith (NYJ QB) | $11 | — | Baby Arm | "Baby Arm $3 (Lower Offer)" — a second, lower Baby Arm claim as displayed (not interpreted further) |
| Seth McGowan (IND RB) | $3 | Kyle Pitts Sr. | Baby Arm | none listed |
| Keenan Allen (IND WR) | $3 | Baker Mayfield | DUGASM | none listed |
| Saints DEF | $2 | J.K. Dobbins | Big Balls | none listed |

FA adds after processing: Wet Serapas — Adonai Mitchell (drop Rams DEF, 5:52 am); Terrance Ferguson (IR) (drop Jake Bates, 5:54 am).
FAB Offers lists only claims with more than one bid; "none listed" means Yahoo shows no competing bid, not that competing bids were checked another way. No unseen bids are inferred.

FAAB check (league home, before → after): DUGASM $74→$71, Big Balls $14→$12, Baby Arm $79→$65, Vaqueros $79→$64; Wet Serapas $67, Good Strongs $29, Deepest $92, FFAmuseBouche $90 unchanged. Every change matches the winning prices above.

## Notable newly dropped players

| Player | Dropped by | Status shown | Relevance to Vaqueros |
|---|---|---|---|
| J.K. Dobbins (DEN RB) | Big Balls | **W (Nov 6)**, W9 proj 7.54, 77% | Highest-projected RB in pool; DEN backfield with Coleman leading and Harvey on IR. Possible add only with a drop (0 open spots). |
| Baker Mayfield (TB QB) | DUGASM | **W (Nov 6)**, 14.84 | QB depth; low need (Love/Caleb/Nix) |
| Kyle Pitts Sr. (ATL TE) | Baby Arm | **W (Nov 6)**, 7.90 | TE; low need (Warren/LaPorta/Freiermuth) |
| Jake Bates (DET K) | Wet Serapas | To Waivers (status not on pulled lists) | K; low need |
| Rams DEF | Wet Serapas | To Waivers (status not on pulled lists) | DEF stream option only |

Waiver-clear times are as Yahoo shows (W (Nov 6)); exact clock not shown.

## Evidence

- [evidence/recon-2026-11-04/](./evidence/recon-2026-11-04/) — text extracts (scripts removed) of each page, `MANIFEST.json` (URL, fetch time CT, raw SHA-256), `transactions_nov4_extract.json`, `fab_offers_extract.json`, `player-lists.json`, `fetchlog.txt`, `SOURCE-NOTES.md`
- Raw HTML kept on the box only (not committed): `/home/box/agent-data/yahoo-raw/recon-2026-11-04/`
- Machine-readable: [reconciliation.json](./reconciliation.json)
