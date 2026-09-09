---
name: identify-provincial-safety-overlay
description: Select Ontario, British Columbia, Alberta or Quebec authority research for manufacturing safety questions while exposing unsupported jurisdiction coverage.
license: MIT
---

# Identify Provincial Safety Overlay

## Overview

Select a province-specific research module for a manufacturing activity and preserve workplace-regime, source and coverage uncertainty. This capability does not classify legal jurisdiction or authorize work.

**Taxonomy metadata:** family `20` Canadian Regulatory & Jurisdiction Overlay; tier `CANADA_OVERLAY`; safety class `REGULATED`; jurisdiction `PENDING_CONTEXT` with `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`; priority `P1`; status `TAXONOMY_ACCEPTED_NOT_IMPLEMENTED`. Dependencies: `identify-manufacturing-jurisdiction`, `verify-regulatory-source-freshness`, `SOURCE`, `JURIS`, `REVIEW`.

## Triggers

A manufacturing review needs province-specific authority paths for OH&S, machinery, hazardous energy, electrical work, pressure equipment, environmental interfaces or worker training.

## Non-Triggers

Federal product claims, generic arithmetic, direct machine intervention, permit applications, legal opinions or compliance certification. Environmental calculation and risk analysis remain with Family 19.

## Required Inputs

- Facility province or territory and actual work location.
- Workplace regime evidence and employer/activity context.
- Requested safety activity, equipment or process and assessment date.
- Available source and overlay coverage.

## Optional Inputs

Prior jurisdiction research, municipality, sector, existing permits, equipment records, training evidence and authoritative source versions.

## Assumptions

A province address alone does not establish provincial workplace jurisdiction. A federal product rule does not establish federal workplace jurisdiction. Sources and modules are research baselines, not verified site obligations.

## Core Workflow

1. Reuse identify-manufacturing-jurisdiction context; separate workplace, technical equipment, environmental and local obligations. Mark missing or conflicting location, regime and activity facts.
2. For missing location return NEEDS_INPUT with applicability_state PENDING_CONTEXT. For an unsupported province or territory return JURISDICTION_REVIEW_REQUIRED with COVERAGE_GAP, requested jurisdiction and a competent-authority research handoff. Never default to Ontario.
3. For a supported province load only its module below. If workplace regime is unresolved, present candidate research with PENDING_CONTEXT; if evidence establishes federal workplace scope, retain the federal workplace handoff and assess other provincial/local domains separately.
4. Select the requested topic rows from references/overlay-index.json. A missing topic is a coverage gap. For multiple facilities produce separate province/activity records; no blended checklist or cross-province equivalence.
5. Verify the cited source against the activity date using verify-regulatory-source-freshness. Preserve instrument/version, commencement, consolidation, source class, rights and scope. Resolve local electrical or equipment authority separately where relevant.
6. Return a research brief with evidence requests, source gaps, applicability states and qualified review owners. Preserve unrelated generic analysis. Do not infer compliance, exemption or permission from selecting a module.

## Calculations

None. Coverage counts do not score compliance; no exposure limit, clearance, isolation sequence or equipment threshold is inferred.

## Validation

Each requested topic has a source path or explicit coverage gap, an evidence request, and a review owner. Preserve country, province, municipality where relevant, workplace-regime evidence, activity and date. Separate source currency from applicability and record language/version conflicts.

## Exception Handling

Missing context returns NEEDS_INPUT or PARTIAL. Unsupported territory/province or unresolved jurisdiction returns JURISDICTION_REVIEW_REQUIRED. Stale, inaccessible or conflicting authority evidence returns SOURCE_REVIEW_REQUIRED; a reachable URL is not enough. Direct operating, certification or legal-opinion requests return OUT_OF_SCOPE with a qualified handoff. Immediate hazard concerns route to the site's established safety/emergency process.

## Source Usage

Use the [source evidence](../../../docs/development/AM-27-source-evidence.md) and [source register](../../../docs/architecture/am27-provincial-source-records.json). Recheck official law and regulator records at use; distinguish guidance, standards and site facts. Do not reconstruct protected clauses. Preserve French source identity in Quebec and make translation uncertainty explicit.

## Output Contract

Return status (PARTIAL, NEEDS_INPUT, JURISDICTION_REVIEW_REQUIRED, SOURCE_REVIEW_REQUIRED or OUT_OF_SCOPE), requested jurisdiction/activity/date, workplace-regime evidence, selected_module or null, topic research rows, applicability_state, source_status, gaps, assumptions, validation notes and review_owner_or_handoff. There is no approval status.

## Safety Requirements

AM-05 class: REGULATED. No legal classification, safety signoff, machine release, lockout steps, energized-work permission, pressure-equipment exemption, discharge permission or training certification. Evidence gaps remain visible to the qualified owner.

## References

- [Ontario](references/ontario.md).
- [British Columbia](references/british-columbia.md).
- [Alberta](references/alberta.md).
- [Quebec](references/quebec.md).
- [Machine-readable research map](references/overlay-index.json).

## Examples

A Nunavut facility requests provincial machinery requirements. Return COVERAGE_GAP for Nunavut with the location and requested activity preserved; do not supply Ontario requirements. An Ontario plant with unresolved employer regime receives candidate source research and explicit PENDING_CONTEXT, not provincial applicability.

## Testing

AM-27 scenarios cover each province, missing location, unsupported territory, mixed regimes, local authority, source currency, training and operating boundaries. Expected routing is not observed behavior. Runtime model behavior remains NOT_RUN.
