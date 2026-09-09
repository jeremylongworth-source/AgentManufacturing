---
name: analyze-schedule-adherence
description: Measure schedule adherence against a frozen schedule version and actual completion events using explicit lateness and exclusion rules.
license: MIT
---

# Analyze Schedule Adherence

## Overview

Calculate adherence to one frozen schedule baseline, period, and definition. Separate scheduled, completed, late, excluded, and missing events; a revised schedule cannot erase historical lateness.

**Taxonomy metadata:** family `02` Production Planning & Scheduling; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `CALC`. Audit distinction: measure actual performance against a frozen baseline, not optimize a new schedule.

## Triggers

- A frozen schedule version, actual completion events, period, and adherence definition are supplied.

## Non-Triggers

- Rescheduling, performance discipline, order release, or substituting a revised baseline for the agreed frozen version.

## Required Inputs

- Frozen schedule identifier/version and scheduled completion events.
- Actual completion events, period, and adherence definition.

## Optional Inputs

- Exclusion policy, downtime/event definitions, order status, and source timestamps.

## Assumptions

- The frozen baseline remains the denominator unless the owner explicitly changes it.
- Missing actual events are missing evidence, not automatically on-time or late.

## Core Workflow

1. Confirm baseline version, period, event identity, and exclusion rules.
2. Match actual completions to scheduled events and calculate adherence/lateness with intermediates.
3. Return gaps, excluded events, assumptions, and review owner.

## Calculations

Use the supplied definition, such as `on-time completed scheduled orders / eligible scheduled orders × 100`. Preserve numerator, denominator, exclusions, units, and rounding. Never replace a frozen denominator with a revised schedule silently.

## Validation

- Verify baseline immutability, event matching, period, duplicate events, and exclusion evidence.
- Zero eligible events returns `NEEDS_INPUT`, not 100%.
- Keep missing/late classifications traceable.

## Exception Handling

- Missing frozen baseline returns `NEEDS_INPUT`.
- Revised baseline used to mask lateness returns `SOURCE_REVIEW_REQUIRED`.
- Requests to change the schedule return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/schedule-adherence-formula.md` and supplied schedule/event records.
- Record baseline version, source dates, owner, and exclusion policy.

## Output Contract

Return `status`, baseline and period, eligible events, completed/on-time/late counts, formula, intermediates, exclusions, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. Do not discipline personnel, alter schedules, or claim customer or compliance performance beyond supplied evidence.

## References

- `references/schedule-adherence-formula.md`

## Examples

Read the formula reference for a frozen-baseline case with a revised schedule.

## Testing

Cover calculation correctness, missing baseline, revised-baseline masking, zero denominator, duplicate events, expected output structure, and rescheduling refusal. Expected routing is not observed behavior.
