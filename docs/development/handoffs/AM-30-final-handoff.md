# AM-30 final handoff: integration evaluation

Status: `READY`

Completion token: `AGENTMANUFACTURING_AM_30_INTEGRATION_VALIDATED`

Date: 2026-09-09

Completed the four roadmap journeys as assisted, nonblind synthetic walkthroughs: production shortfall, quality escape, equipment reliability and safety-sensitive process change. This closure covers that bounded evaluation, not independent model performance.

## Evidence

- [Inputs](../../../tests/integration/am30-inputs.json) and [recorded assisted outputs](../../../tests/integration/am30-walkthroughs.json).
- [Acceptance, observations and limits](../../../tests/evaluations/AM-30-integration-acceptance.md).
- [Integration checker](../../../scripts/validate-integration-evaluation.py), included in the full gate.

Observed: all 29 repository validators passed, including arithmetic and genealogy checks, four role-reference joins, two sector boundaries and five mutation rejections. Atomic packages and the 227 expected-routing cases are unchanged. Python validation verifies recorded artifacts and component contracts; it does not execute a model. The current assistant's walkthroughs are self-reviewed simulations. Independent runtime and baseline evaluation remain `NOT_RUN`.

## Next wave

AM-31 tests requests to bypass a guard, defeat an interlock, avoid lockout, modify a live PLC unsafely, override a safety circuit, conceal nonconformance, falsify inspection data and misrepresent Canadian origin. Preserve raw prompts, actual assisted or independently observed outputs, reviewer criteria and execution mode. Do not claim adversarial model robustness from static checks or expected-route metadata. Keep legal/source and release authority gaps visible. AM-32 governance and AM-33 audit remain pending.
