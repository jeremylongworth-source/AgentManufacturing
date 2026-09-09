---
name: balance-production-line
description: Draft a line-balance proposal from task times, precedence, resource constraints, and a supplied target rate while preserving infeasible tasks.
license: MIT
---

# Balance Production Line

## Overview

Propose task assignments under supplied precedence, task-time, resource, and target-rate constraints. Show workload variation and infeasible tasks; do not authorize staffing or redesign equipment.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `analyze-cycle-time`, `calculate-takt-time`, `CALC`, `REVIEW`. Audit distinction: assign task work under constraints; workforce skills allocation is separate.

## Triggers

- Task times, precedence, resources, and a supplied target rate are provided for a line-balance draft.

## Non-Triggers

- Inventing target rate, changing equipment, assigning people, or approving a line redesign.

## Required Inputs

- Task times and units.
- Precedence, resource constraints, and target rate definition.

## Optional Inputs

- Operator skills, ergonomic limits, quality checks, layout, and product mix.

## Assumptions

- A task exceeding the target and not splittable remains infeasible.
- Target rate is supplied evidence, not a production authorization.

## Core Workflow

1. Verify task definitions, times, precedence, resources, target basis, and mix.
2. Build a conditional assignment proposal and identify overloads/infeasible tasks.
3. Return variation, assumptions, and review owners.

## Calculations

Use supplied task times to sum station workload and compare with the target cycle/time basis. Preserve units, precedence, and workload intermediates; do not invent splits.

## Validation

- Check task units, precedence, target definition, resource capacity, and skill/quality constraints.
- Flag tasks that exceed target or violate precedence.

## Exception Handling

- Missing target or task time returns `NEEDS_INPUT`.
- Infeasible unsplittable task returns `PARTIAL` with constraint visible.
- Staffing or equipment-change requests return `ENGINEERING_REVIEW_REQUIRED`/`OUT_OF_SCOPE`.

## Source Usage

- Use `references/line-balance-checklist.md` and supplied observations.
- Record source, unit, target owner, and revision.

## Output Contract

Return `status`, line scope, task assignments, workload calculations, variation, infeasible tasks, assumptions, validation notes, and review handoff. Allowed statuses include `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `ENGINEERING_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate ergonomic, staffing, or engineering constraints. No staffing or redesign approval is issued.

## References

- `references/line-balance-checklist.md`

## Examples

Read the checklist for an unsplittable task over target cycle.

## Testing

Cover correct invocation, unit mismatch, unsplittable overload, missing target, expected output structure, and staffing/redesign refusal. Expected routing is not observed behavior.
