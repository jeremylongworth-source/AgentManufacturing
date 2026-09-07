---
name: review-spare-parts-criticality
description: Assess spare-part criticality from failure consequence and supply evidence without making purchasing or stock decisions.
license: PENDING_PROJECT_GOVERNANCE
---

# Review Spare Parts Criticality

**Taxonomy metadata:** family `10` Maintenance & Reliability; tier `CORE`; safety class `ROUTINE`; jurisdiction `GENERIC_METHOD_ONLY`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Compare consequence, lead time, substitutability, and evidence for a spare.

## Triggers
- Spare identity, asset linkage, failure consequence, lead time, and usage evidence are supplied.

## Non-Triggers
- Buying, stocking, substituting, or approving a part.

## Required Inputs
- Part/asset identity, consequence, lead time, interchangeability basis, and demand evidence.

## Optional Inputs
- Supplier risk, shelf life, cost, installed base, and service strategy.

## Assumptions
- Criticality is not the same as current inventory quantity.

## Core Workflow
1. Reconcile part identity and asset consequence.
2. Compare lead time, failure exposure, and substitutes.
3. Return criticality evidence and policy-owner handoff.

## Calculations
Use supplied scoring or exposure arithmetic; preserve definitions and units.

## Validation
- Check identity, consequence, lead time, substitute evidence, and population.

## Exception Handling
- Missing consequence or identity returns `NEEDS_INPUT`.
- Purchasing or stock instruction returns `OUT_OF_SCOPE`.

## Source Usage
- Apply `references/spare-parts-criticality-checklist.md`.

## Output Contract
Return `status`, part/asset map, consequence, lead time, evidence, gaps, and owner handoff.

## Safety Requirements
AM-05 class: `ROUTINE`. Do not order, substitute, or set stock policy.

## References
- `references/spare-parts-criticality-checklist.md`

## Examples
A long lead time is a criticality input, not a stocking decision.

## Testing
Cover correct invocation, missing consequence, substitute ambiguity, expected output structure, and purchasing refusal. Expected routing is not observed behavior.
