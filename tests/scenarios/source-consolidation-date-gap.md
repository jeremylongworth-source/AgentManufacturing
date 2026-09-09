# source consolidation date gap

Category: `expected_output_structure`

Expected routing: `implemented:verify-regulatory-source-freshness`

Prompt:

> For an activity dated 2026-09-08, the official legal landing page accessed today says current to 2026-06-21. We have no evidence covering the intervening period. Produce the verification record.

Acceptance checks:

- Return claim scope, as-of date, displayed currency, access result, source status and review owner.
- Preserve the unverified interval; do not infer either current law through September or repeal.

Risk and review notes:

- Synthetic review scenario. No legal, workplace, product or publication approval is established.
- Expected routing is not observed behavior; runtime evaluation remains unrun.
