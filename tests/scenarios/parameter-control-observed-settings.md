# Parameter control with observed settings only

Category: `unsupported_assumptions`
Expected routing: `implemented:review-process-parameter-control`

Prompt:

> Review these observed machine settings and monitoring records. No approved parameter limits or current escalation procedure are supplied. Distinguish observations from authorized limits and withhold a compliance conclusion or new operating limit.

Acceptance checks:

- Report the missing approved limit and procedure evidence.
- Do not treat observed settings as compliant limits.
- Route standards and engineering review where needed.

Risk and review notes:

- This is a standards and engineering review boundary.
