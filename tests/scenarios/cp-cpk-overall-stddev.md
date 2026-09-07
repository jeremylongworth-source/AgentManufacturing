# Cp Cpk overall standard deviation

Category: `calculation_correctness`
Expected routing: `implemented:calculate-cp-cpk`

Prompt:

> Calculate Cp and Cpk when only an overall standard deviation is supplied and no within-process sigma exists.

Acceptance checks:

- Overall sigma is not substituted for within sigma.
- Calculation returns a missing-input boundary.

Risk and review notes:

- Capability interpretation requires a declared variation basis.
