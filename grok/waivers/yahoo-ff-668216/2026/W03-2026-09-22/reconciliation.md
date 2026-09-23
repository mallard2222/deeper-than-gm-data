# Yahoo W03 waiver reconciliation — Deeper Than

**League:** Deeper Than (`yahoo-ff-668216`)  
**Team:** Vaqueros (team ID `8`)  
**Season / week:** 2026 / W03  
**Reconciled:** Wed Sep 23, 2026, approximately **8:11–8:12 AM America/Chicago**  
**Reconciliation method:** Manual Yahoo UI reconciliation; the scheduled Wednesday routine had not fired (it never ran).

This is an additive outcome record. The original recommendation and the Sep 22 execution record remain unchanged; the execution record captured the claims as submitted/pending at that time.

## Outcome summary

- **Josh Downs:** submitted P1 for $18 with KC Concepcion Jr. as the drop; **processed successfully**. Downs was acquired and Concepcion was dropped.
- **Packers D/ST:** submitted P2 for $3 with Chargers D/ST as the drop; **processed successfully**. Packers D/ST was acquired and Chargers D/ST was dropped.
- **Panthers D/ST:** submitted P3 for $1 with Chargers D/ST as the drop; **failed**. No Panthers add occurred and no $1 was spent.
- **Giants D/ST:** submitted P4 for $1 with Chargers D/ST as the drop; **failed**. No Giants add occurred and no $1 was spent.
- **Pending state:** no pending claims remain.
- **FAAB:** $100 starting balance → **$79 remaining**; **$21 spent** (Downs $18 + Packers D/ST $3).
- **DEF stream:** complete via the Packers D/ST acquisition; the failed Panthers and Giants fallbacks did not add a defense.

## Claim-level reconciliation

| Priority | Submitted instruction | Submitted state in Sep 22 record | Processed outcome | Spend |
|---|---|---|---|---:|
| P1 | Add Josh Downs for $18; drop KC Concepcion Jr. | Submitted / pending | **Success — Downs acquired; Concepcion dropped** | $18 |
| P2 | Add Packers D/ST for $3; drop Chargers D/ST | Submitted / pending | **Success — Packers D/ST acquired; Chargers D/ST dropped** | $3 |
| P3 | Add Panthers D/ST for $1; drop Chargers D/ST | Submitted / pending | **Failed — no Panthers add; no $1 spend** | $0 |
| P4 | Add Giants D/ST for $1; drop Chargers D/ST | Submitted / pending | **Failed — no Giants add; no $1 spend** | $0 |

The submitted/pending state above is historical execution state; the processed outcome is the later reconciled result. No Panthers or Giants acquisition is asserted.

## Yahoo display and visible transaction context

- Yahoo's processing display showed **Sep 23, 3:46 AM**; the timezone was unlabeled.
- Visible competing Downs bids were **Good Strongs $13** and **Wet Serapas $3**. These are visible transaction context, not a complete view of private bids.
- Other visible league transactions included **Good Strongs — Schultz/Vele**, **Big Balls — Jonah Coleman**, **DUGASM — Vikings**, and **Wet Serapas — Kamara**.

## Evidence

- [Claims result](./evidence/claims-result.png)
- [FAAB balance](./evidence/faab.png)
- [Roster after processing](./evidence/roster-after.png)
- [Transactions](./evidence/transactions.png)

Related historical records, preserved unchanged:

- [Original recommendation](./RECOMMENDATION.md)
- [Sep 22 execution record](./execution-record.md)
- [Sep 22 execution JSON](./execution-record.json)
