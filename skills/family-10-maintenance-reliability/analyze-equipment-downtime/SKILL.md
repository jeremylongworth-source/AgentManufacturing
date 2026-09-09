---
name: analyze-equipment-downtime
description: Classify and total equipment downtime on a declared event and exposure basis without inferring failure cause.
license: MIT
---

# Analyze Equipment Downtime

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Reconcile downtime events, categories, duration, and exposure for one asset or population.

## Triggers
- Event records, asset identity, time basis, and downtime categories are supplied.

## Non-Triggers
- Declaring failure cause, changing maintenance policy, or directing operations.

## Required Inputs
- Asset/population, event timestamps, duration units, category rules, and exposure window.

## Optional Inputs
- Planned/unplanned flags, production impact, shift calendar, and source quality.

## Assumptions
- Failure events and downtime loss are distinct measures.

## Core Workflow
1. Normalize event boundaries and categories.
2. Reconcile overlaps and exposure denominator.
3. Return totals, exclusions, and evidence gaps.

## Calculations
Total downtime is the sum of non-overlapping event durations on one declared time basis.

## Validation
- Check timestamps, overlaps, units, planned/unplanned rule, and exposure.

## Exception Handling
- Missing event basis returns `NEEDS_INPUT`.
- Repair instruction returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/downtime-analysis-checklist.md` and AM-08 rules.

## Output Contract
Return `status`, population, event map, totals, denominator, exclusions, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct equipment operation or repair.

## References
- `references/downtime-analysis-checklist.md`

## Examples
Overlapping downtime events cannot be summed without an overlap rule.

## Testing
Cover correct invocation, overlapping events, unit mismatch, expected output structure, and repair refusal. Expected routing is not observed behavior.
