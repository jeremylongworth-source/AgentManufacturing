---
name: build-control-chart
description: Structure a control chart from ordered process data while preserving subgroup, baseline, and limit assumptions.
license: PENDING_PROJECT_GOVERNANCE
---

# Build Control Chart

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Prepare a control-chart dataset and declared basis for review.

## Triggers
- Ordered observations, characteristic, sampling plan, and chart family are supplied.

## Non-Triggers
- Adjusting a process, changing limits, or declaring capability.

## Required Inputs
- Characteristic, units, time/order, subgroup basis, and data window.

## Optional Inputs
- Baseline exclusions, rational subgroup rationale, and software output.

## Assumptions
- Missing observation order prevents a defensible chronology.

## Core Workflow
1. Validate units, order, subgrouping, and population.
2. Declare chart family and baseline rules.
3. Calculate or transcribe limits with exclusions and evidence visible.

## Calculations
Use the declared chart equations and retain intermediate values; specification limits are not control limits.

## Validation
- Check data order, subgroup size, missingness, and limit basis.

## Exception Handling
- Missing order or chart basis returns `NEEDS_INPUT`.
- Process-adjustment requests return `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/control-chart-build-checklist.md` and AM-07 calculation/source rules.

## Output Contract
Return `status`, data scope, chart family, limits, exclusions, assumptions, and review handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct live process intervention.

## References
- `references/control-chart-build-checklist.md`

## Examples
Unordered readings cannot support a signal chronology.

## Testing
Cover correct invocation, missing order, unit mismatch, expected output structure, and intervention refusal. Expected routing is not observed behavior.
