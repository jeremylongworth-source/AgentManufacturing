---
name: perform-root-cause-analysis
description: Evaluate evidence-backed causal hypotheses for one problem while separating correlation, cause, and corrective action.
license: MIT
---

# Perform Root-Cause Analysis

**Taxonomy metadata:** family `09` Nonconformance, RCA & CAPA; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Adjudicate candidate causes against evidence for a bounded problem.

## Triggers
- One problem statement, timeline, evidence set, and candidate hypotheses are supplied.

## Non-Triggers
- Brainstorming without evidence, selecting CAPA, or assigning blame.

## Required Inputs
- Problem definition, timeline, evidence, hypotheses, and boundary conditions.

## Optional Inputs
- Replication, comparison cases, change history, and expert review.

## Assumptions
- Correlation alone does not establish a root cause.

## Core Workflow
1. Bound the problem and timeline.
2. Test hypotheses against confirming and disconfirming evidence.
3. Return supported, unresolved, and rejected hypotheses.

## Calculations
Use declared counts or comparisons only; do not assign causal probability without a method.

## Validation
- Check chronology, evidence provenance, alternatives, and reproducibility.

## Exception Handling
- Missing evidence returns `NEEDS_INPUT`.
- CAPA approval or blame request returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/root-cause-analysis-checklist.md`.

## Output Contract
Return `status`, problem, timeline, hypothesis matrix, evidence, uncertainty, and handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not authorize corrective action or attribute fault.

## References
- `references/root-cause-analysis-checklist.md`

## Examples
A coincident parameter change is a candidate cause until evidence distinguishes it from alternatives.

## Testing
Cover correct invocation, missing timeline, correlation-only evidence, expected output structure, and CAPA refusal. Expected routing is not observed behavior.
