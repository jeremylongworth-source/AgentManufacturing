# Inspection plan without approved sample basis

Category: `missing_inputs`
Expected routing: `implemented:build-inspection-plan`

Prompt:

> Draft an incoming inspection plan for supplier lots using the supplied characteristics and acceptance limits. No approved sampling basis exists; show the missing basis without inventing a sample size or accepting the lot.

Acceptance checks:

- Preserve supplier and lot context.
- Identify the missing approved sampling basis.
- Do not invent sample size, execute inspection, or release material.

Risk and review notes:

- Sampling authority is a quality and standards-dependent input.
