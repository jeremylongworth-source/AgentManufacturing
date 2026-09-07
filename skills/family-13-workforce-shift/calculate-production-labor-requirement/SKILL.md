---
name: calculate-production-labor-requirement
description: Convert declared production workload into labor-hours or equivalents using supplied standards without approving staffing or overtime.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate Production Labor Requirement

**Taxonomy metadata:** family `13` Workforce & Shift Operations; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Calculate labor requirement from production quantity and a declared labor standard.

## Triggers
- Product quantity, labor standard, units, period, and population are supplied.

## Non-Triggers
- Hiring, assigning workers, approving overtime, or setting a labor standard.

## Required Inputs
- Quantity, labor per unit, units, period, and standard revision.

## Optional Inputs
- Product mix, yield, learning, breaks, and indirect labor treatment.

## Assumptions
- A calculated requirement is not a staffing decision.

## Core Workflow
1. Validate quantity, labor standard, units, and revision.
2. Calculate labor-hours/equivalents with intermediates.
3. Return assumptions and workforce-owner handoff.

## Calculations
`labor requirement = production quantity × labor standard per unit`; preserve units and factors.

## Validation
- Check standard revision, quantity, units, mix, yield, and period.

## Exception Handling
- Missing standard or units returns `NEEDS_INPUT`.
- Hiring or overtime request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/production-labor-requirement-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, inputs, formula, intermediates, requirement, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not hire, assign, or approve overtime.

## References
- `references/production-labor-requirement-checklist.md`

## Examples
An outdated labor standard must be flagged before its result informs staffing.

## Testing
Cover correct invocation, mixed units, stale standard, expected output structure, and staffing refusal. Expected routing is not observed behavior.
