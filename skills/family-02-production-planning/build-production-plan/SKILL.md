---
name: build-production-plan
description: Build a bounded production-plan draft from demand, dates, available quantities, and explicit capacity, material, and labor constraints.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Production Plan

## Overview

This reference skill allocates supplied demand across a stated planning horizon and returns a feasible draft with constraints and unmet demand. It does not release orders, schedule people in a live system, or invent capacity.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED` before AM-10 reference proof. Dependencies: `calculate-production-requirement`, `calculate-production-capacity`, `calculate-material-requirement`, `calculate-production-labor-requirement`. Audit distinction: produce one horizon-level allocation; sequencing and detailed staffing remain separate.

## Triggers

- The user provides demand, due dates, a planning horizon, available production quantities or capacity, and known material/labor constraints.
- The user asks for a production-plan draft, capacity allocation, or unmet-demand view.

## Non-Triggers

- Live ERP/MES order release, dispatching, labor assignment, procurement commitment, or customer promise.
- Detailed finite scheduling, routing design, material requirement calculation, or a safety-critical operating decision.

## Required Inputs

- Demand quantities, item identifiers, and due dates or priority rule.
- Planning horizon and time basis.
- Available production quantities or capacity by relevant resource.
- Known material, labor, and other hard constraints.

## Optional Inputs

- Setup/changeover assumptions, inventory and work-in-process evidence, lot sizes, approved priorities, and calendar availability.
- Dependency outputs from production requirement, capacity, material, or labor calculations.

## Assumptions

- Only supplied capacity, inventory, labor, and material facts are usable; missing capacity remains unknown.
- If no priority rule is supplied, preserve demand order and mark prioritization as an assumption requiring owner review.
- Allocations cannot exceed stated capacity or available material and do not imply a customer commitment.

## Core Workflow

1. Confirm scope, horizon, demand basis, priorities, resource units, and evidence dates.
2. Reconcile available capacity and hard constraints, then allocate demand in the stated priority order.
3. Return the feasible allocation, unmet demand, limiting constraints, assumptions, and owner handoff.

## Calculations

No manufacturing-rate formula is required. Use transparent subtraction for remaining demand and remaining capacity in common units. If a supplied dependency includes a formula, preserve its source, units, and intermediate values; do not recalculate it from missing facts.

## Validation

- Every allocation must map to an item, period, resource, and source quantity.
- Sum of allocations cannot exceed stated demand, available capacity, material, or labor.
- Demand beyond capacity must remain as unmet demand with the binding constraint identified.
- Dates, units, and horizon boundaries must be comparable; unknown values remain unknown.

## Exception Handling

- Missing demand, horizon, or capacity returns `NEEDS_INPUT`.
- Demand greater than capacity returns `PARTIAL` with unmet demand; it is never silently dropped or fulfilled by an invented shift.
- Conflicting priorities or constraints return `NEEDS_INPUT` with both claims preserved.
- Live release or commitment requests return `OUT_OF_SCOPE` with an operations-system handoff.

## Source Usage

- Use the supplied planning records and the dependency outputs named in the taxonomy record. Record source, effective date, and owner for each constraint.
- A current external standard is not needed for arithmetic; use external sources only to resolve a stated planning definition or jurisdictional requirement.
- Do not treat an inferred calendar, rate, or inventory balance as evidence.

## Output Contract

Return `status`, scope and horizon, demand inputs, capacity and constraint evidence, allocation table, unmet demand, assumptions, validation notes, missing/conflicting evidence, and review/handoff owner. Allowed statuses are `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. The result is a draft for review. Do not dispatch work, alter a machine schedule, assign unqualified labor, release a purchase or production order, or represent the draft as a customer promise. Escalate safety or regulated-production constraints.

## References

- `references/production-plan-evidence-checklist.md`
- `docs/architecture/dependency-map.md`
- `docs/architecture/scope-boundaries.md`

## Examples

Read `references/production-plan-evidence-checklist.md` for a partial-capacity example. The example demonstrates evidence treatment, not a live scheduling result.

## Testing

Cover correct invocation, incorrect invocation, missing inputs, bad inputs, ambiguous scenario, expected output structure, unsupported assumptions, and capacity-over-demand behavior. A deterministic acceptance case must show partial allocation and explicit unmet demand when demand exceeds capacity. Expected routing is not observed behavior.
