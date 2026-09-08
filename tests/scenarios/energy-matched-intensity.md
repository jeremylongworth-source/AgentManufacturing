# energy matched intensity

Category: `calculation_correctness`
Expected routing: `implemented:analyze-energy-consumption`

Prompt:

> Analyze 1.2 MWh interval consumption and 400 good parts for the same line and month, with a dedicated line meter and matched production scope.

Acceptance checks:

- Show 1200 kWh divided by 400 parts equals 3.0000 kWh per part.
- Do not convert the result into emissions, money, or a causal improvement claim.

Risk and review notes:

- Expected routing is not observed behavior. Evidence gaps and responsible review remain visible.
