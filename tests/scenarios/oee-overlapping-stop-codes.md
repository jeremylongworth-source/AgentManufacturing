# OEE overlapping stop codes

Category: `calculation_correctness`
Expected routing: `implemented:analyze-oee-data`

Prompt:

> Reconcile OEE inputs where planned shutdown is also included in an unplanned stop code and the same interval appears in both exports.

Acceptance checks:

- Overlapping time classification is flagged.
- OEE arithmetic is withheld until the basis is resolved.

Risk and review notes:

- OEE input reconciliation is distinct from calculating OEE.
