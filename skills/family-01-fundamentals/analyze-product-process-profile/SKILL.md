---
name: analyze-product-process-profile
description: Analyze how supplied product variants, demand mix, and process descriptions fit a manufacturing process profile while exposing evidence gaps.
license: MIT
---

# Analyze Product Process Profile

## Overview

Create a product/process fit profile for the supplied variants, volume, mix, and process descriptions. The result supports scoping and method selection; it does not approve a process or promise capacity.

**Taxonomy metadata:** family `01` Manufacturing Fundamentals; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `classify-manufacturing-operation`. Audit distinction: profile product/process fit, not a capacity or engineering design decision.

## Triggers

- The user supplies product variants, demand volume/mix, and process descriptions and requests a profile.

## Non-Triggers

- Detailed process capability, production scheduling, tooling design, product release, or market demand forecasting.

## Required Inputs

- Product variants and relevant attributes.
- Demand volume and mix over a stated period.
- Process descriptions and known operation boundaries.

## Optional Inputs

- Routing, changeover evidence, quality characteristics, equipment family, and customer-specific constraints.

## Assumptions

- Descriptions are evidence, not proof of capability or compliance.
- Missing mix, process, or variant facts remain gaps rather than inferred averages.

## Core Workflow

1. Confirm product/process scope and time basis.
2. Compare variation, volume, mix, and process characteristics; identify fit signals and gaps.
3. Return a reviewable profile with dependencies and next evidence owner.

## Calculations

No calculation required; preserve any supplied rates and units without deriving capacity.

## Validation

- Check that product variants, demand mix, and processes share a period and scope.
- Distinguish observed facts from hypotheses and avoid capability claims without evidence.

## Exception Handling

- Missing process or mix evidence returns `NEEDS_INPUT`.
- Conflicting variant definitions remain visible and return `PARTIAL`.
- Requests for an engineering design or production commitment return `OUT_OF_SCOPE`.

## Source Usage

- Use `references/product-process-profile-checklist.md` and supplied process records.
- External sources are needed only for a stated definition or sector overlay and must include provenance and freshness.

## Output Contract

Return `status`, product/process scope, variant and mix evidence, fit profile, gaps, assumptions, validation notes, dependencies, and handoff. Allowed statuses include `COMPLETE`, `PARTIAL`, `NEEDS_INPUT`, and `OUT_OF_SCOPE`.

## Safety Requirements

AM-05 class: `ROUTINE`. The profile does not authorize process changes, equipment operation, qualification, or release.

## References

- `references/product-process-profile-checklist.md`

## Examples

Read the checklist for a high-mix profile with missing changeover evidence.

## Testing

Cover correct invocation, missing inputs, ambiguous variants, expected output structure, unsupported capability assumptions, and adjacent scheduling requests. Expected routing is not observed behavior.
