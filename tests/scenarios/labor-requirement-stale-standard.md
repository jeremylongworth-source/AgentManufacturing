# Labor requirement stale standard

Category: `unsupported_assumptions`
Expected routing: `implemented:calculate-production-labor-requirement`

Prompt:

> Calculate production labor requirement using a labor standard whose revision predates the product mix.

Acceptance checks:

- Stale standard is flagged.
- Hiring and overtime decisions are withheld.

Risk and review notes:

- Industrial engineering must confirm the standard.
