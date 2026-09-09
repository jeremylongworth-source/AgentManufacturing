# whmis readiness identifier mismatch

Category: `bad_inputs`

Expected routing: `implemented:review-whmis-readiness`

Prompt:

> Our product inventory and container label identify Blend A, but the supplied SDS identifies Blend B. Training attendance is the only program record. Review the evidence gaps.

Acceptance checks:

- Flag product/SDS/label identity mismatch and ask for reconciliation.
- Do not infer task competence from attendance or approve chemical use.

Risk and review notes:

- Synthetic review scenario. No legal, workplace, product or publication approval is established.
- Expected routing is not observed behavior; runtime evaluation remains unrun.
