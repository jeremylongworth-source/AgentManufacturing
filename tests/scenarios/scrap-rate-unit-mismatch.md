# Scrap rate with mass and unit-count mismatch

Category: `unit_mismatch`
Expected routing: `implemented:calculate-scrap-rate`

Prompt:

> Calculate scrap rate from 20 kilograms of scrap and a denominator of 500 units. Require a supported conversion or separate the measures; do not divide mass by count.

Acceptance checks:

- Identify incompatible mass and unit-count dimensions.
- Request a supported conversion or separate denominator.
- Do not make a disposal or environmental conclusion.

Risk and review notes:

- Scrap rate requires a defined comparable population.
