---
name: calculate-production-lead-time
description: Estimate production lead time from supplied queue, setup, run, transfer, routing, and overlap evidence with measured and assumed components separated.
license: MIT
---

# Calculate Production Lead Time

## Overview

Calculate a transparent lead-time estimate for one routing and period. Show queue, setup, run, transfer, and overlap treatment separately; do not promise a delivery date or hide uncertainty.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: aggregate routing time components; process-map and individual cycle statistics remain separate.

## Triggers

- Queue, setup, run, and transfer times, routing order, units, and overlap assumptions are supplied.

## Non-Triggers

- Customer promise, schedule release, capacity estimate, or inferring a queue from a target date.

## Required Inputs

- Routing order and time components.
- Time units and explicit overlap assumptions.

## Optional Inputs

- Percentiles, observed period, WIP, resource calendar, and source confidence.

## Assumptions

- Components are additive only where no overlap is supplied; overlap rules must be explicit.
- Measured and assumed components remain separate.

## Core Workflow

1. Normalize routing, component definitions, units, period, and overlap convention.
2. Sum or overlap components transparently and preserve measured versus assumed values.
3. Return the estimate, sensitivity, gaps, and planning handoff.

## Calculations

Use `lead time = queue + setup + run + transfer` for non-overlapping components, subtracting only explicitly supported overlap. Preserve each intermediate, unit, and rounding; avoid double counting.

## Validation

- Check units, routing order, duplicate components, and overlap definitions.
- A missing component or zero/negative unsupported value returns a gap, not an invented duration.
- The estimate is not a customer commitment.

## Exception Handling

- Missing units or overlap convention returns `NEEDS_INPUT`.
- Conflicting route records return `SOURCE_REVIEW_REQUIRED`.
- Promise or release requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/lead-time-formula.md` and supplied routing records.
- Record source, observation period, units, and owner.

## Output Contract

Return `status`, routing scope, components, overlap convention, formula, intermediates, estimate, assumptions, validation notes, sensitivity, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not promise delivery, release an order, or change a process based on the estimate.

## References

- `references/lead-time-formula.md`

## Examples

Read the formula reference for overlapping setup and queue time.

## Testing

Cover calculation correctness, overlap/double-counting, missing units, conflicting routing, expected output structure, and delivery-promise refusal. Expected routing is not observed behavior.
