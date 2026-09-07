# OEE deterministic fixture request

Category: `calculation_correctness`
Expected routing: `implemented:calculate-oee`

Prompt:

> Run the reference OEE calculation for planned time 480 minutes, runtime 420 minutes, ideal cycle 0.5 minutes per unit, total count 780, and good count 744. Show the expected intermediate ratios and verify the final raw ratio within the declared tolerance.

Acceptance checks:

- Match AM08-F05 availability, performance, quality, and OEE values.
- Preserve the ratio and any percentage display as separate values.
- Use the fixture tolerance rather than prose similarity.

Risk and review notes:

- This is deterministic fixture coverage, not evidence of model behavior.
- The fixture does not prove that the OEE definition fits a particular site.
