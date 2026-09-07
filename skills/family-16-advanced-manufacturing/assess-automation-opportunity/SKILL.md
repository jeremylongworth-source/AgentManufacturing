---
name: assess-automation-opportunity
description: Screen an automation opportunity from supplied process evidence while preserving engineering, sector, and review boundaries.
license: PENDING_PROJECT_GOVERNANCE
---

# Assess Automation Opportunity

**Taxonomy metadata:** family `16` Automation & Advanced Manufacturing; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Assess whether a bounded process problem is sufficiently evidenced for an automation concept review.

## Triggers
- Process problem, observed workload or losses, candidate concept, constraints, and readiness evidence are supplied.

## Non-Triggers
- Selecting technology, approving deployment, changing controls, or issuing operating instructions.

## Required Inputs
- Process boundary, current method, stable evidence, constraints, affected people, and sector context.

## Optional Inputs
- Readiness findings, candidate technologies, quality impact, and preliminary economics.

## Assumptions
- A manual loss without stable process evidence is an opportunity hypothesis, not an automation case.

## Core Workflow
1. Bound the problem and evidence period.
2. Separate observed losses from proposed automation benefits.
3. Return readiness gaps, review questions, and qualified next owner.

## Calculations
No savings or capacity result is invented; supplied measures retain their denominator and uncertainty.

## Validation
- Check process stability, evidence quality, constraints, sector context, and human impact.

## Exception Handling
- Missing process evidence returns `NEEDS_INPUT`.
- A deployment or safeguard request returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/automation-opportunity-checklist.md` and AM-07 source controls.

## Output Contract
Return `status`, problem scope, evidence, opportunity hypothesis, gaps, review needs, and handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not select, deploy, or provide operating or bypass steps.

## References
- `references/automation-opportunity-checklist.md`

## Examples
Unstable manual losses produce a readiness gap rather than a claim that automation will solve them.

## Testing
Cover correct invocation, missing readiness evidence, sector gap, expected output structure, and deployment refusal. Expected routing is not observed behavior.
