---
name: review-component-substitution
description: Assess component substitution compatibility and evidence gaps without approving a design or production change.
license: MIT
---

# Review Component Substitution

**Taxonomy metadata:** family `12` Materials, BOM & Traceability; tier `CORE`; safety class `ENGINEERING_OR_CERTIFICATION_BOUNDARY`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Structure equivalence, compatibility, effectivity, and validation questions for a proposed substitute.

## Triggers
- Original/substitute identity, intended use, requirements, evidence, and change context are supplied.

## Non-Triggers
- Approving substitution, editing BOM, or releasing production.

## Required Inputs
- Original and substitute, function, requirements, material/specification, and evidence.

## Optional Inputs
- Supplier, qualification, test, regulatory, and inventory context.

## Assumptions
- Similar identity or nominal dimensions do not prove equivalence.

## Core Workflow
1. Compare function, requirements, materials, interfaces, and evidence.
2. Identify validation, standards, and effectivity gaps.
3. Return qualified engineering and quality handoff.

## Calculations
Preserve supplied tolerance or fit arithmetic; do not infer equivalence.

## Validation
- Check requirements, units, material, interfaces, validation, and sector context.

## Exception Handling
- Missing requirements or evidence returns `NEEDS_INPUT`.
- Approval or release request returns `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/component-substitution-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, original/substitute comparison, evidence, gaps, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `ENGINEERING_OR_CERTIFICATION_BOUNDARY`. Do not approve or activate a substitution.

## References
- `references/component-substitution-checklist.md`

## Examples
A dimensional match without material or validation evidence remains unresolved.

## Testing
Cover correct invocation, missing requirements, unit mismatch, expected output structure, and approval refusal. Expected routing is not observed behavior.
