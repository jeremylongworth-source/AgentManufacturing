---
name: triage-nonconformance
description: Prioritize an initial nonconformance report and identify the next evidence owner without deciding disposition.
license: PENDING_PROJECT_GOVERNANCE
---

# Triage Nonconformance

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P0`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Classify the issue, urgency, evidence state, and next owner.

## Triggers
- An observed deviation, complaint, audit finding, or suspected failure is supplied.

## Non-Triggers
- Closing a record, approving disposition, or declaring root cause.

## Required Inputs
- Observation, requirement or expected condition, time, scope, and reporter.

## Optional Inputs
- Product impact, containment status, recurrence, and customer context.

## Assumptions
- An observation is not automatically a confirmed nonconformance.

## Core Workflow
1. Separate observation from interpretation.
2. Screen urgency, scope, and missing evidence.
3. Assign a proposed next owner and handoff.

## Calculations
No calculation; counts and priority labels retain their supplied basis.

## Validation
- Check requirement, evidence, affected scope, urgency, and owner.

## Exception Handling
- Missing observation or requirement returns `NEEDS_INPUT`.
- Disposition or closure request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/nonconformance-triage-checklist.md`.

## Output Contract
Return `status`, observation, requirement, scope, urgency, evidence gaps, proposed owner, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize disposition, release, or corrective action.

## References
- `references/nonconformance-triage-checklist.md`

## Examples
A reported deviation with no requirement remains an evidence gap, not a confirmed finding.

## Testing
Cover correct invocation, missing requirement, ambiguous scope, expected output structure, and disposition refusal. Expected routing is not observed behavior.
