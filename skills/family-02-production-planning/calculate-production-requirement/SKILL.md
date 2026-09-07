---
name: calculate-production-requirement
description: Calculate net production need by product and period from demand, usable finished quantity, committed receipts, yield, and inventory-policy evidence.
license: PENDING_PROJECT_GOVERNANCE
---

# Calculate Production Requirement

## Overview

Calculate a traceable net production quantity for each supplied product and period. Preserve hold status, source quantities, yield assumptions, and unresolved policy decisions; do not create a release order.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: compute product-level net need; component/BOM expansion belongs elsewhere.

## Triggers

- Demand, usable finished quantity, committed receipts, and supplied yield or inventory policy are provided for a product and period.

## Non-Triggers

- BOM explosion, capacity allocation, order release, inventory adjustment, or customer promise.

## Required Inputs

- Demand by product and period.
- Usable finished quantity and committed receipts.
- Yield basis and inventory policy, or an explicit statement that they are unavailable.

## Optional Inputs

- Safety stock, lot size, scrap/rework definition, source timestamps, and planner priority.

## Assumptions

- Finished quantity on hold is excluded unless an authorized policy explicitly permits use.
- Yield is applied only when its basis, unit, and period are supplied.
- Missing policy is not silently replaced with zero safety stock or perfect yield.

## Core Workflow

1. Normalize product, period, units, hold status, and source definitions.
2. Calculate net need from demand less usable supply and committed receipts, with explicit yield/policy treatment.
3. Return intermediate values, assumptions, validation notes, and a planning handoff.

## Calculations

Use `net need = demand + policy reserve - usable finished quantity - committed receipts`, then adjust for a supplied yield basis only when its definition supports that operation. Preserve numerator, denominator, units, period, and rounding. Negative net need is reported as surplus or zero only according to the supplied policy; never hide it.

## Validation

- Reject mixed product, period, or units; exclude held quantities from usable supply.
- Check non-negative counts and defined yield/policy basis.
- Keep all intermediate terms visible and do not imply capacity or release feasibility.

## Exception Handling

- Missing yield or inventory policy returns `NEEDS_INPUT` or `PARTIAL` with conditional arithmetic.
- Held, conflicting, or stale inventory evidence returns `SOURCE_REVIEW_REQUIRED`.
- Order-release or inventory-write requests return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/production-requirement-formula.md` and supplied planning records.
- Record source, effective date, policy owner, and freshness; do not infer inventory from a dashboard screenshot.

## Output Contract

Return `status`, product/period scope, demand, usable supply, receipts, policy/yield basis, formula, intermediates, net need, assumptions, validation notes, gaps, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. No production, purchase, inventory, or customer commitment is issued.

## References

- `references/production-requirement-formula.md`

## Examples

Read the reference for a held-finished-quantity case.

## Testing

Cover calculation correctness, held inventory, missing policy, unit mismatch, expected output structure, and order-release refusal. Expected routing is not observed behavior.
