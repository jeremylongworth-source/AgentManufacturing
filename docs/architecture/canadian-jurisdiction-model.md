# Canadian jurisdiction model

Status: **AM-04 model ready; no legal compliance determination or skill implementation**  
Model: `docs/architecture/canadian-jurisdiction-model.json`  
Source registry: `docs/architecture/canadian-source-registry.json`  
Access date for the registry: 2026-09-07

## Scope and audience

This document defines routing metadata for AgentManufacturing authors and validators. It helps a skill separate generic manufacturing analysis from a conclusion that depends on Canadian product, supplier, workplace, environmental, transport, labelling, contract, or standards authority. It does not state that a site complies, identify a worker's legal duty, certify a product, or replace current law, regulation, official guidance, a contract, or qualified review.

The AM-03 index remains the catalogue source of truth. Its existing `GENERIC_METHOD_ONLY` and `PENDING_CONTEXT` assessments map directly to the formal AM-04 states below, so the taxonomy freeze is preserved. AM-04 adds the decision mechanics and source registry; it does not silently reclassify 159 accepted records.

## Model overview

The routing record has five parts:

1. **Obligation domain**: product, supplier, workplace, environmental, transport, labelling, contract standard, or other.
2. **Context**: country, province or territory, facility/activity location, employer activity, sector/product class, requested activity, date, and authority evidence.
3. **Composable flags**: `CANADA_FEDERAL`, `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`, and `STANDARDS_DEPENDENT`.
4. **Applicability state**: a review state, never a compliance verdict.
5. **Evidence**: source key, publisher, URL, source class, scope, effective/page date, access date, and unresolved conflicts.

Flags answer which questions must be investigated. They do not answer those questions. A single request can carry more than one flag. For example, a Quebec facility handling a product covered by federal supplier rules can have `CANADA_FEDERAL`, `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`, and `STANDARDS_DEPENDENT` simultaneously.

## Formal flags and states

| Flag | Use when | Required context | Guardrail |
|---|---|---|---|
| `CANADA_FEDERAL` | A federal source may govern the requested obligation or product activity. | Country, obligation domain, requested activity, authority context. | A federal product rule does not establish federal workplace jurisdiction. |
| `PROVINCIAL_REQUIRED` | A province or territory must be identified and reviewed. | Province/territory, facility or activity location, domain, requested activity. | Never substitute Ontario or federal sources for a missing jurisdiction. |
| `SECTOR_REGULATED` | Employer activity, sector, product class, or undertaking can change authority or requirements. | Sector/product class, employer activity, requested activity, authority context. | A sector label proves neither certification nor regulated status. |
| `STANDARDS_DEPENDENT` | The conclusion depends on a named standard, edition, incorporation, contract, or manufacturer specification. | Identifier, edition/effective date, incorporation basis, licensed text status. | A standards reference is not proof of compliance or release authority. |

Applicability states are:

- `GENERIC_METHOD_ONLY`: unrelated generic method work can proceed.
- `PENDING_CONTEXT`: generic work can proceed, but the requested dependent conclusion needs context.
- `SOURCE_REVIEW_REQUIRED`: enough context exists to choose an authority family, but current source/effective-date review is still required.
- `COVERAGE_GAP`: the requested jurisdiction or authority is outside the supported registry; return a research handoff.
- `CONFLICT_REVIEW_REQUIRED`: supplied facts or sources conflict; preserve both and escalate.

Missing jurisdiction must not block unit-safe arithmetic that has no jurisdiction-dependent conclusion. It must block or keep unresolved the dependent legal, safety, permit, or applicability statement.

## Source hierarchy and evidence

Use the highest applicable source available:

1. Current official law, regulation, official consolidation, or regulator source.
2. Official government or regulator guidance for scope and interpretation.
3. An incorporated or licensed standard, only when the incorporation or contract basis is evidenced. Do not reproduce protected text.
4. Site, employer, permit, contract, SOP, or manufacturer evidence for facts and local obligations.
5. Secondary material for discovery only.

Every source-dependent record preserves the source key, publisher, URL, scope, access date, page/effective date where available, freshness state, and unresolved applicability. If two sources differ, record the time, scope, language, or authority difference and route the conflict for qualified review. Do not average or silently choose one.

## Initial extension pattern

The registry intentionally starts with one federal path and four provincial paths:

| Extension | Source path | Boundary |
|---|---|---|
| Federal | Canada Labour Code Part II workplace-scope guidance, then current Code/regulations and product/supplier sources as needed. | Federal workplace status is activity/undertaking-specific. |
| Ontario | Ontario OHSA framework, e-Laws Act, and applicable sector/hazard regulations. | The Ontario framework does not replace federal routing or other provincial sources. |
| British Columbia | WorkSafeBC OHS Regulation and update stream. | The source describes WorkSafeBC inspectional jurisdiction and exclusions that require separate routing. |
| Alberta | OHS Act, Regulation, and Code with in-force version tracking. | Confirm amendments and activity date; do not use a stale Code snapshot. |
| Quebec | Official Quebec Act and applicable regulations, preserving official-language source identity and consolidation date. | French/English rendering does not remove the need to check the official current text. |

The pattern is extensible to the remaining provinces and territories by adding a source-registry entry, scope, freshness policy, authority boundary, and acceptance scenarios. A missing entry is a coverage gap, not permission to reuse an existing province.

## Decision procedure

1. Separate the requested obligation domain.
2. Normalize each context field as known, unknown, not applicable, or conflicting.
3. Select the authority family from activity and employer/product context.
4. Compose flags and assign an applicability state.
5. Review current source, effective date, edition, incorporation basis, and provenance.
6. Preserve source conflicts and route them for qualified review.
7. Return generic supported work plus a clear research handoff when context or coverage is missing.

## Acceptance criteria and evidence

| Criterion | Observable check | Evidence |
|---|---|---|
| Flag definitions | All four flags have meaning, required context, and guardrail. | Model JSON and validator. |
| Domain separation | Product, supplier, workplace, environmental, transport, labelling, contract-standard, and other are distinct values. | `obligation_domain` enum and J-03/J-06 scenarios. |
| No default jurisdiction | Unknown or unsupported province/territory produces `PENDING_CONTEXT` or `COVERAGE_GAP`, never Ontario substitution. | Negative guards and J-04/J-05. |
| Generic continuation | Jurisdiction-free arithmetic remains available. | J-01. |
| Source hierarchy | Five ordered source classes and evidence fields are present. | `source_hierarchy`, source registry, validator. |
| Initial extensions | Federal, Ontario, B.C., Alberta, and Quebec each have a source key, scope, and boundary. | `extension_pattern` and registry. |
| Conflict handling | Conflicting facts or effective dates produce `CONFLICT_REVIEW_REQUIRED`. | Negative guards and J-07. |
| No compliance overclaim | The model states that flags, standards, sector labels, and guidance do not prove compliance or authority. | Scope, guardrails, and validator checks. |

## Validation and limits

Run:

```powershell
python scripts/validate-jurisdiction-model.py
python scripts/validate-taxonomy.py
```

The validator checks the machine-readable model, source keys, required scenarios, extension coverage, and the AM-03 mapping. It does not prove current law, source completeness, legal applicability, or skill behavior. AM-07 owns the broader source/standards freshness standard, AM-05 owns safety classification mechanics, and AM-09 owns executable behavioral validation.

## References

The source registry contains the current URLs and access metadata. Key official references are the federal regulated-industries list, federal workplace-safety scope, WHMIS supplier guidance, Ontario OHSA overview, WorkSafeBC OHS Regulation, Alberta OHS Code, Quebec's official OHS Act, and Statistics Canada's manufacturing classification.
