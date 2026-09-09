---
name: analyze-production-constraints
description: Build an evidence-ranked register of production constraints while separating measured bottlenecks from hypotheses.
license: MIT
---

# Analyze Production Constraints

## Overview

Create a constraint register for a stated production objective, observation period, and supplied material, labor, equipment, and policy evidence. Rank evidence and uncertainty without declaring a bottleneck from assumption alone.

**Taxonomy metadata:** family `01` Manufacturing Fundamentals; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Audit distinction: distinguish constraints and hypotheses; a measured bottleneck is a separate result.

## Triggers

- The user provides a production objective, observed period, and known constraints and asks what limits output.

## Non-Triggers

- Live schedule changes, equipment diagnosis, safety authorization, or a final bottleneck claim without observation evidence.

## Required Inputs

- Production objective and observation period.
- Material, labor, equipment, policy, and demand constraints that are known.

## Optional Inputs

- Rates, queues, downtime, changeover records, staffing plan, and constraint owner.

## Assumptions

- A reported constraint is not measured proof of a bottleneck.
- Rates and records are comparable only when units, period, and scope align.

## Core Workflow

1. Normalize objective, period, unit, resource, and evidence source.
2. Separate hard constraints, observations, hypotheses, and unknowns; rank confidence.
3. Return the register, evidence gaps, and next measurement or owner.

## Calculations

No calculation required. Preserve supplied rates; route rate arithmetic to the relevant calculation skill.

## Validation

- Check scope, time basis, units, and source dates.
- Ensure every constraint has evidence or is labeled a hypothesis.
- Do not call a constraint a bottleneck without comparative evidence.

## Exception Handling

- Missing observation period or objective returns `NEEDS_INPUT`.
- Conflicting records return `PARTIAL` with both versions preserved.
- Requests to alter operations or commit resources return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/production-constraint-register.md` and supplied records.
- Record source owner and freshness; external standards are not inferred from generic constraints.

## Output Contract

Return `status`, objective and period, constraint register, evidence basis, confidence, hypotheses, unknowns, validation notes, and next owner. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not instruct bypasses, unsafe staffing, or live equipment changes; escalate any safety constraint to the qualified owner.

## References

- `references/production-constraint-register.md`

## Examples

Read the register reference for a measured queue constraint versus a hypothesis.

## Testing

Cover correct invocation, missing periods, conflicting evidence, unsupported bottleneck claims, expected output structure, and unsafe operating requests. Expected routing is not observed behavior.
