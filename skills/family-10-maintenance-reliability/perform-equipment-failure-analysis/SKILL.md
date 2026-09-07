---
name: perform-equipment-failure-analysis
description: Assess physical and equipment failure hypotheses with qualified-review limits and no repair or certification authority.
license: PENDING_PROJECT_GOVERNANCE
---

# Perform Equipment Failure Analysis

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure evidence for physical or equipment hypotheses and qualified engineering review.

## Triggers
- Failure event, equipment identity, evidence, and candidate physical hypotheses are supplied.

## Non-Triggers
- Inspecting equipment, directing repair, certifying fitness, or declaring a cause without evidence.

## Required Inputs
- Failure boundary, asset identity, chronology, evidence, and operating context.

## Optional Inputs
- Photos, teardown results, environmental history, change records, and sector criteria.

## Assumptions
- A hypothesis remains unresolved until qualified evidence supports it.

## Core Workflow
1. Bound the event and evidence chain.
2. Compare physical hypotheses and missing tests.
3. Return engineering-review questions and safe handoff.

## Calculations
Preserve supplied loads, rates, or tolerances; do not perform unverified design analysis.

## Validation
- Check identity, chronology, evidence provenance, standards, and sector context.

## Exception Handling
- Missing evidence returns `NEEDS_INPUT`.
- Repair, teardown, or certification request returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/equipment-failure-analysis-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, event, hypotheses, evidence, gaps, engineering questions, and authority boundary.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not direct hazardous inspection, repair, or certification.

## References
- `references/equipment-failure-analysis-checklist.md`

## Examples
A fracture image can support a hypothesis list but cannot by itself certify a failure mechanism.

## Testing
Cover correct invocation, missing chronology, sector gap, expected output structure, and repair refusal. Expected routing is not observed behavior.
