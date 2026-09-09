# Sector medical-devices

Category: `calculation_correctness`
Expected routing: `implemented:calculate-scrap-rate`

Prompt:

> For a medical-device production batch, calculate scrap percentage from 10 scrapped units among 200 total units. No release or sector compliance conclusion is requested.

Acceptance checks:

- Return 5 percent with the supplied unit-count basis; missing sector coverage does not block generic arithmetic.
- No planned specialization is represented as implemented coverage.

Risk and review notes:

- Core routes support generic analysis or a coverage/source handoff only.
- Expected routing is not observed behavior.
