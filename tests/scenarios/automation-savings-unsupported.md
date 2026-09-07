# Automation savings unsupported

Category: `calculation_correctness`
Expected routing: `implemented:build-automation-business-case`

Prompt:

> Build an automation business case where savings assume a large uptime gain, but the baseline, horizon, and supporting evidence are not supplied.

Acceptance checks:

- Unsupported benefits remain sensitivity assumptions.
- No investment approval or committed savings is returned.

Risk and review notes:

- Economic comparison requires an agreed baseline and decision owner.
