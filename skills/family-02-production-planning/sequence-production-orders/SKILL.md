---
name: sequence-production-orders
description: Propose a non-overlapping production-order sequence from due dates, priorities, routing durations, resource availability, and changeover evidence.
license: MIT
---

# Sequence Production Orders

## Overview

Create a proposed order sequence for existing work under supplied precedence, resource, duration, and changeover constraints. Expose conflicts and infeasibility without dispatching or releasing orders.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Audit distinction: sequence existing work; demand quantity and plan feasibility have separate owners.

## Triggers

- Existing orders, due dates/priorities, routing durations, resource availability, and changeover evidence are supplied.

## Non-Triggers

- Demand calculation, live dispatch, resource assignment, unsafe compression of steps, or order release.

## Required Inputs

- Order due dates and priority rule.
- Routing durations, required resources, and resource availability.
- Changeover matrix or explicit absence of one.

## Optional Inputs

- Precedence constraints, setup windows, frozen commitments, maintenance windows, and planner preferences.

## Assumptions

- A proposed sequence is feasible only within supplied resources and dates.
- Missing priorities or changeover times remain open constraints.

## Core Workflow

1. Normalize orders, resources, durations, priorities, and horizon.
2. Build a non-overlapping sequence, checking precedence, availability, and changeovers.
3. Return conflicts, infeasible orders, assumptions, and planner handoff.

## Calculations

Use supplied durations and transparent start/finish arithmetic. Preserve units and overlap assumptions; do not shorten approved work or infer parallel resources.

## Validation

- No resource may run overlapping orders unless parallel capacity is supplied.
- Check due dates, precedence, changeover, and maintenance constraints.
- Mark infeasibility instead of moving an order silently.

## Exception Handling

- Missing duration or resource availability returns `NEEDS_INPUT`.
- Same-resource conflict returns `PARTIAL` with a non-overlapping alternative or explicit infeasibility.
- Live dispatch or release returns `OUT_OF_SCOPE`.

## Source Usage

- Use `references/order-sequencing-checklist.md` and supplied routing/calendar records.
- Record source version and owner; do not infer plant calendars.

## Output Contract

Return `status`, horizon, order sequence, resource assignments, start/finish basis, conflicts, infeasibility, assumptions, validation notes, and planner handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not dispatch work, change equipment settings, compress safety steps, or release an order.

## References

- `references/order-sequencing-checklist.md`

## Examples

Read the checklist for two orders competing for one machine.

## Testing

Cover correct invocation, same-resource conflict, missing durations, due-date infeasibility, expected output structure, and live-dispatch refusal. Expected routing is not observed behavior.
