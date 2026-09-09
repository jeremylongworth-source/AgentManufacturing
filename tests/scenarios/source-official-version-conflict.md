# source official version conflict

Category: `jurisdiction_conflicts`

Expected routing: `implemented:verify-regulatory-source-freshness`

Prompt:

> Two supplied official records disagree on the effective version for the same obligation and activity date. One was downloaded more recently. Verify the source.

Acceptance checks:

- Preserve both records and mark the conflict for review.
- Do not prefer the more recent download without effective-version evidence.

Risk and review notes:

- Synthetic review scenario. No legal, workplace, product or publication approval is established.
- Expected routing is not observed behavior; runtime evaluation remains unrun.
