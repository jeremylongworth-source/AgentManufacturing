---
name: build-automation-business-case
description: Compare supplied automation costs and benefits with explicit uncertainty without making an investment approval.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Automation Business Case

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure an economic comparison for an automation concept using supplied assumptions and sensitivity ranges.

## Triggers
- Automation proposal, evidence-based costs and benefits, time horizon, and sensitivity assumptions are supplied.

## Non-Triggers
- Selecting a vendor, approving capital, committing savings, or authorizing deployment.

## Required Inputs
- Concept scope, one-time cost, recurring cost, benefit basis, horizon, units, and uncertainty assumptions.

## Optional Inputs
- Ramp profile, maintenance, uptime, labor basis, quality effect, and scenario ranges.

## Assumptions
- An economic comparison is not an investment decision and unsupported benefits remain assumptions.

## Core Workflow
1. Align scope, time horizon, units, and baseline.
2. Compare supplied cost and benefit scenarios with visible intermediates.
3. Return sensitivity, missing evidence, and decision-owner handoff.

## Calculations
Use supplied units and formula basis for payback or net comparison; refuse incompatible or unsupported inputs.

## Validation
- Check baseline, cost/benefit denominator, horizon, recurring effects, uncertainty, and double counting.

## Exception Handling
- Missing baseline or benefit basis returns `NEEDS_INPUT`.
- A request to approve investment returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/automation-business-case-checklist.md` and AM-08 calculation rules.

## Output Contract
Return `status`, scenarios, assumptions, formulas, sensitivity, evidence gaps, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not approve capital, savings, vendor selection, or deployment.

## References
- `references/automation-business-case-checklist.md`

## Examples
Unsupported uptime gains remain sensitivity assumptions rather than committed savings.

## Testing
Cover correct invocation, missing baseline, unit mismatch, expected output structure, and investment-approval refusal. Expected routing is not observed behavior.
