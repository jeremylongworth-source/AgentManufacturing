---
name: identify-manufacturing-bottleneck
description: Identify an evidence-ranked manufacturing bottleneck from comparable operation rates, queues, downtime, demand, and period data.
license: PENDING_PROJECT_GOVERNANCE
---

# Identify Manufacturing Bottleneck

## Overview

Produce a bottleneck finding for one production flow and period when operation rates, queues or downtime, and demand rate are supplied. Show sensitivity to data gaps and do not convert a hypothesis into a production directive.

**Taxonomy metadata:** family `01` Manufacturing Fundamentals; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `calculate-production-capacity`, `analyze-equipment-downtime`. Audit distinction: identify one evidence-ranked bottleneck; constraints and downtime analysis remain reusable inputs.

## Triggers

- The user supplies comparable operation rates, queue or downtime records, demand rate, and a period and asks where flow is constrained.

## Non-Triggers

- A guess based on one anecdote, live dispatching, equipment repair, or an unsafe throughput change.

## Required Inputs

- Operation rates with units and scope.
- Queue and/or downtime records.
- Demand rate and common observation period.

## Optional Inputs

- Changeover, WIP, staffing, material availability, and sensitivity ranges.

## Assumptions

- Rates and demand must share a unit and period; if not, request conversion evidence.
- A bottleneck finding is conditional on supplied records and may be inconclusive.

## Core Workflow

1. Verify comparable rates, demand, queues, downtime, and period boundaries.
2. Rank candidate constraints and test whether the finding changes under stated data gaps.
3. Return the evidence-ranked finding, uncertainty, and review owner.

## Calculations

Use only transparent comparisons of supplied rates and demand; preserve units and intermediate comparisons. Route capacity or downtime formulas to their owning skills.

## Validation

- Reject mixed units or periods and identify missing queue/downtime evidence.
- Do not claim a bottleneck when evidence supports only a hypothesis.
- Check that the result does not imply an approved operating change.

## Exception Handling

- Missing comparable rates or period returns `NEEDS_INPUT`.
- Conflicting records return `PARTIAL` with sensitivity noted.
- Live throughput, staffing, or equipment-change requests return `OUT_OF_SCOPE` or `SAFETY_ESCALATION` as applicable.

## Source Usage

- Use `references/bottleneck-evidence-checklist.md` and supplied production records.
- Record source, owner, units, and freshness; do not infer plant facts from a generic benchmark.

## Output Contract

Return `status`, flow scope and period, evidence table, candidate comparison, bottleneck finding or hypothesis, sensitivity, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SAFETY_ESCALATION`.

## Safety Requirements

AM-05 class: `ROUTINE`. No live machine, staffing, bypass, or production-release instruction is permitted.

## References

- `references/bottleneck-evidence-checklist.md`

## Examples

Read the checklist for a rate comparison with incomplete downtime records.

## Testing

Cover correct invocation, missing inputs, unit/period mismatch, ambiguous bottleneck evidence, expected output structure, and unsafe change requests. Expected routing is not observed behavior.
