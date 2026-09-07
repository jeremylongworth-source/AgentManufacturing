---
name: assess-measurement-traceability
description: Assess whether measurement evidence identifies a defensible reference chain without certifying traceability.
license: PENDING_PROJECT_GOVERNANCE
---

# Assess Measurement Traceability

**Taxonomy metadata:** family `07` Metrology & Measurement Systems; tier `CORE`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `STANDARDS_DEPENDENT`, `SECTOR_REGULATED`; priority `P2`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`.

## Overview
Map reference links, certificates, and breaks in measurement traceability.

## Triggers
- Measurement results and calibration or reference certificates are supplied.

## Non-Triggers
- Issuing a certificate, declaring compliance, or selecting a reference standard.

## Required Inputs
- Result identity, certificate, reference standard, dates, and applicable criterion.

## Optional Inputs
- Uncertainty budget, laboratory scope, environmental controls, and transfer records.

## Assumptions
- A certificate without a reference chain leaves traceability unproven.

## Core Workflow
1. Link result, instrument, certificate, and reference.
2. Check dates, scope, uncertainty, and breaks in the chain.
3. Return evidence status and qualified review needs.

## Calculations
Preserve supplied uncertainty components; do not create an uncertainty budget.

## Validation
- Confirm identity, scope, revision, reference chain, and jurisdiction.

## Exception Handling
- Missing chain evidence returns `SOURCE_REVIEW_REQUIRED`.
- Certification requests return `ENGINEERING_REVIEW_REQUIRED`.

## Source Usage
- Apply `references/traceability-chain-checklist.md` and AM-07 source rules.

## Output Contract
Return `status`, chain map, evidence, breaks, assumptions, and qualified handoff.

## Safety Requirements
AM-05 class: `REGULATED`. Do not certify traceability or compliance.

## References
- `references/traceability-chain-checklist.md`

## Examples
A certificate lacking its reference chain is incomplete evidence even when dates appear current.

## Testing
Cover correct invocation, missing reference chain, jurisdiction gap, expected output structure, and certification refusal. Expected routing is not observed behavior.
