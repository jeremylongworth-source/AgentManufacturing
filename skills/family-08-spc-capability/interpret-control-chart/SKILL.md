---
name: interpret-control-chart
description: Interpret control-chart signals while separating statistical signal from assignable cause and operational action.
license: MIT
---

# Interpret Control Chart

**Taxonomy metadata:** family `08` SPC & Capability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Classify observed chart signals and evidence gaps without claiming root cause.

## Triggers
- A chart, limits, ordered data, and signal rule are supplied.

## Non-Triggers
- Naming a root cause, changing limits, or directing process adjustment.

## Required Inputs
- Chart basis, limits, ordered observations, and signal rule.

## Optional Inputs
- Change history, maintenance, material, staffing, and environmental events.

## Assumptions
- A signal without change history is a signal, not a root cause.

## Core Workflow
1. Reconstruct the signal against declared limits and rules.
2. Separate signal evidence from event chronology.
3. Return hypotheses and evidence requests.

## Calculations
Recompute only from supplied limits and ordered data; preserve rounding.

## Validation
- Check chart family, limit basis, chronology, and rule revision.

## Exception Handling
- Missing chronology returns `NEEDS_INPUT`.
- Action request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/control-chart-interpretation-checklist.md`.

## Output Contract
Return `status`, signal, rule, chronology, hypotheses, gaps, assumptions, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not direct process intervention.

## References
- `references/control-chart-interpretation-checklist.md`

## Examples
A run rule can be reported without selecting a cause.

## Testing
Cover correct invocation, signal without cause, missing limits, expected output structure, and action refusal. Expected routing is not observed behavior.
