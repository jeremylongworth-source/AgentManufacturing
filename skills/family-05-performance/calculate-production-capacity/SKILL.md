---
name: calculate-production-capacity
description: Estimate production capacity from supplied available time, rates, loss assumptions, and product mix with limiting-resource evidence.
license: MIT
---

# Calculate Production Capacity

## Overview

Estimate output capacity for supplied resources and product mix. Preserve rate, time, loss, and mix assumptions and identify the limiting resource; do not present the estimate as guaranteed capacity.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: estimate resource output from rates and available time; utilization is a separate comparison.

## Triggers

- Available time, supplied rates, loss assumptions, product mix, and resource scope are provided.

## Non-Triggers

- Capacity authorization, staffing, machine-setting changes, order release, or a guarantee of future output.

## Required Inputs

- Available time by resource and period.
- Observed/supplied rates, loss assumptions, and product mix.

## Optional Inputs

- Changeover, downtime, yield, calendar, resource constraints, and sensitivity range.

## Assumptions

- Mixed-product rates remain mix-specific; incompatible rates are not averaged silently.
- Loss assumptions are supplied or clearly labeled assumptions.

## Core Workflow

1. Align resource, period, rate, units, mix, and loss definitions.
2. Calculate conditional capacity and identify limiting resource with intermediates.
3. Return assumptions, sensitivity, and planning/engineering handoff.

## Calculations

Use transparent supplied arithmetic such as `capacity = available time × rate × (1 - loss fraction)` per resource/product basis. Preserve mix weighting, units, intermediate values, and rounding.

## Validation

- Check rate and time dimensions, loss range, product mix, and resource identity.
- Flag capacity outside supplied bounds or dependent on unknown losses.
- Do not imply guaranteed output.

## Exception Handling

- Missing rate/time/mix returns `NEEDS_INPUT`.
- Mixed products with incompatible cycles return `NEEDS_INPUT` or `PARTIAL`.
- Authorization or setting changes return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/capacity-estimate-formula.md` and AM-08 calculation rules.
- Record source, period, loss basis, mix, and owner.

## Output Contract

Return `status`, resource/period, inputs and units, formula, intermediates, capacity estimate, limiting resource, assumptions, sensitivity, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. No staffing, overtime, machine, or customer commitment is authorized.

## References

- `references/capacity-estimate-formula.md`

## Examples

Read the reference for mixed-product cycles and loss assumptions.

## Testing

Cover calculation correctness, mixed-product mismatch, loss validation, missing rate, expected output structure, and capacity-guarantee refusal. Expected routing is not observed behavior.
