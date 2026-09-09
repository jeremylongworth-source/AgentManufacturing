---
name: classify-manufacturing-operation
description: Classify a requested operation against the manufacturing boundary using supplied transformation, assembly, batch, or continuous-process evidence.
license: MIT
---

# Classify Manufacturing Operation

## Overview

Produce a bounded operational classification that distinguishes manufacturing work from logistics, service, extraction, or another adjacent activity. Preserve unresolved facts and do not make a legal industry classification.

**Taxonomy metadata:** family `01` Manufacturing Fundamentals; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Audit distinction: classify one operation boundary, not an enterprise or NAICS registration.

## Triggers

- The user provides a requested activity and product/transformation description and asks whether it is manufacturing.

## Non-Triggers

- Company-wide industry coding, legal classification, warehouse movement, distribution, or a detailed process-capability assessment.

## Required Inputs

- Requested activity, product or component flow, and transformation/assembly evidence.
- Unit, batch, continuous, or service context when relevant.

## Optional Inputs

- Ownership of materials, contract-production context, process records, and adjacent logistics steps.

## Assumptions

- Physical transformation alone does not decide a legal classification; missing context remains unresolved.
- A warehouse or transfer step is not manufacturing merely because it occurs near a line.

## Core Workflow

1. Separate the requested operation from the enterprise and adjacent handoffs.
2. Identify transformation, assembly, blending, finishing, or absence of those elements.
3. Return a classification, evidence basis, unresolved facts, and handoff.

## Calculations

No calculation required.

## Validation

- Check the activity, output, transformation evidence, and boundary owner.
- Verify that the result is operational routing guidance rather than a legal or statistical determination.

## Exception Handling

- Missing transformation evidence returns `NEEDS_INPUT`.
- Mixed manufacturing/logistics requests are split and routed by responsibility.
- Legal, tax, or formal NAICS requests return `OUT_OF_SCOPE` with qualified review.

## Source Usage

- Use `references/operation-classification-checklist.md` and `docs/architecture/domain-contract.md`.
- Cite external classification sources only when needed for the stated question; record source and freshness.

## Output Contract

Return `status`, requested operation, evidence, classification, boundary rationale, unresolved facts, assumptions, validation notes, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, `OUT_OF_SCOPE`, and `SOURCE_REVIEW_REQUIRED`.

## Safety Requirements

AM-05 class: `ROUTINE`. This classification grants no operating, engineering, safety, or compliance authority.

## References

- `references/operation-classification-checklist.md`
- `docs/architecture/domain-contract.md`

## Examples

Read the checklist for a transformation versus warehouse-transfer example.

## Testing

Cover correct invocation, incorrect logistics invocation, missing transformation evidence, ambiguous scope, expected output structure, and unsupported legal assumptions. Expected routing is not observed behavior.
