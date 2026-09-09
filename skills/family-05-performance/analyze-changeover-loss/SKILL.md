---
name: analyze-changeover-loss
description: Break down measured changeover losses from timestamps and task observations while separating overlap, baseline, and improvement proposals.
license: MIT
---

# Analyze Changeover Loss

## Overview

Analyze changeover timestamps, task observations, event definitions, and an approved baseline. Expose overlap and measurement gaps without scheduling work, changing a safety step, or approving an improvement.

**Taxonomy metadata:** family `05` Manufacturing Performance & Efficiency; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: measure changeover task/time loss; scheduling and improvement actions are downstream.

## Triggers

- Changeover timestamps, internal/external task observations, approved baseline, and event definitions are supplied.

## Non-Triggers

- Changeover scheduling, SMED implementation, safety-step reduction, or live process change.

## Required Inputs

- Start/end timestamps and approved baseline.
- Task observations, internal/external classification, and event definitions.

## Optional Inputs

- Resource, product pair, operator, overlap evidence, and quality/cleaning boundaries.

## Assumptions

- Overlapping tasks are not summed twice without an explicit convention.
- Improvement proposals remain hypotheses, not approved actions.

## Core Workflow

1. Verify event definitions, timestamps, baseline, units, and overlap.
2. Break down measured loss and identify data-quality or classification gaps.
3. Return analysis, sensitivity, and improvement-owner handoff.

## Calculations

Use supplied timestamps and task durations; sum only non-overlapping loss or disclose the overlap rule. Preserve intermediates, units, and baseline.

## Validation

- Check timestamp order, overlap, internal/external definitions, and baseline revision.
- Do not convert a loss measurement into a safety or productivity instruction.

## Exception Handling

- Missing event definition returns `NEEDS_INPUT`.
- Overlap or baseline conflict returns `SOURCE_REVIEW_REQUIRED`.
- Safety-step removal or live-change requests return `SAFETY_ESCALATION`/`OUT_OF_SCOPE`.

## Source Usage

- Use `references/changeover-loss-checklist.md` and supplied records.
- Record source, baseline, observer, period, and owner.

## Output Contract

Return `status`, changeover scope, baseline, event table, loss calculation, overlap rule, gaps, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, `SOURCE_REVIEW_REQUIRED`, and `SAFETY_ESCALATION`.

## Safety Requirements

AM-05 class: `ROUTINE`; escalate any request to remove or bypass approved safety/quality steps.

## References

- `references/changeover-loss-checklist.md`

## Examples

Read the checklist for overlapping internal and external tasks.

## Testing

Cover calculation correctness, overlap, missing definitions, baseline conflict, safety-step reduction request, expected output structure, and improvement approval refusal. Expected routing is not observed behavior.
