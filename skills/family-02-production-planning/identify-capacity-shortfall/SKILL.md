---
name: identify-capacity-shortfall
description: Compare required production load with available capacity by operation using a common time and quantity basis.
license: MIT
---

# Identify Capacity Shortfall

## Overview

Produce a capacity-gap table by constrained operation from supplied load and capacity evidence. Normalize only supported units and preserve gaps; do not estimate capacity or promise recovery.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `calculate-production-capacity`, `CALC`. Audit distinction: compare required load with available capacity; capacity estimation remains separate.

## Triggers

- Required load and available capacity by operation are supplied with comparable time and quantity bases.

## Non-Triggers

- Capacity estimation, overtime authorization, hiring, order release, or detailed schedule optimization.

## Required Inputs

- Required production load by operation.
- Available capacity by operation and period.
- Common time and quantity units.

## Optional Inputs

- Calendar, downtime allowance, changeover, labor/material constraints, and source confidence.

## Assumptions

- Capacity is supplied evidence; unknown availability remains unknown.
- Unit conversion requires an explicit, valid conversion and period basis.

## Core Workflow

1. Align operation, period, time basis, quantities, and source definitions.
2. Calculate gap and utilization from supplied values; flag unit or scope conflicts.
3. Return constrained operations, assumptions, and planning handoff.

## Calculations

Use `capacity gap = required load - available capacity`; positive values are shortfalls. Preserve units, period, intermediate values, and rounding. Do not convert units without evidence.

## Validation

- Reject units such as units/day versus units/hour until normalized.
- Check non-negative load/capacity and operation identity.
- Do not infer overtime, parallel equipment, or recovery capacity.

## Exception Handling

- Missing capacity or period returns `NEEDS_INPUT`.
- Unsupported conversion returns `NEEDS_INPUT` with the required evidence.
- Requests to authorize recovery action return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/capacity-shortfall-formula.md` and supplied capacity records.
- Record source, period, unit, and owner; reuse a capacity calculation rather than redefining it.

## Output Contract

Return `status`, operation/period scope, required load, available capacity, formula, gap table, unit checks, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. No overtime, staffing, machine, or customer commitment is authorized.

## References

- `references/capacity-shortfall-formula.md`

## Examples

Read the formula reference for a units/day versus units/hour mismatch.

## Testing

Cover calculation correctness, unit mismatch, missing capacity, positive/negative gap, expected output structure, and recovery-action refusal. Expected routing is not observed behavior.
