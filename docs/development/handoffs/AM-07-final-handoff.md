# AM-07 final handoff — source and standards standard

## Wave

AM-07: Source and standards standard

## Objective

Define source precedence, government and provincial regulatory sourcing, standards metadata, copyrighted-standard handling, and version/freshness controls before calculation standards or executable validation scale.

## Verdict

**READY** for AM-07. Source and standards contracts are defined and structurally validated. No source was fetched by the validator, no legal applicability decision was made, no standard text was copied, and no skill behavior was evaluated.

## Completion token

```text
AGENTMANUFACTURING_AM_07_SOURCE_STANDARD_READY
```

## Scope completed

- Defined five source-precedence ranks with conflict-preserving resolution rules.
- Defined a machine-readable source record schema covering source class, jurisdiction, scope, authority, rights, claims, and freshness.
- Defined metadata-first handling for copyrighted standards and a separate incorporation basis for standards that may be mandatory.
- Defined current, historical, superseded, stale, unknown, conflicting, and pending-review states without inventing a universal numeric expiry interval.
- Defined federal, Ontario, British Columbia, Alberta, and Quebec source-system metadata and province-specific sourcing requirements.
- Added six examples covering federal law, provincial registries, Alberta rights restrictions, Quebec metadata, and a licensed voluntary standard.
- Preserved AM-04 and AM-05 source registries as compatible legacy registries with a migration rule for refreshed records.
- Added twelve acceptance scenarios covering current and historical law, provincial authority, standards incorporation, rights limits, stale sources, conflicts, and unsupported jurisdictions.

## Files added

- `docs/architecture/source-standards-standard.md` — source selection, standards, rights, freshness, provincial routing, and safe-output standard.
- `docs/architecture/source-record-schema.json` — source, claim, rights, authority, and standards metadata contract.
- `docs/architecture/source-freshness-policy.json` — freshness states, policies, triggers, transitions, and blocking states.
- `docs/architecture/source-record-examples.json` — metadata-only examples and claim records.
- `scripts/validate-source-standards-standard.py` — dependency-free validator for AM-07 contracts and registry compatibility.

## Files modified

- `README.md` — AM-07 artifacts, current status, validator command, and AM-08 next-wave pointer.
- `ROADMAP.md` — version 0.9, AM-07 READY status, artifacts, and AM-08 next target.
- `docs/architecture/domain-contract.md` — AM-07 source and standards pointer and boundary statement.

## Research performed

Official source systems reviewed on 2026-09-07 included the Justice Laws Website and Canada Gazette, Ontario e-Laws, BC Laws, Alberta King’s Printer and Alberta Gazette, LégisQuébec, the Standards Council of Canada mandate, federal Crown copyright guidance, and CSA catalogue rights notices. The standard records the source URLs and limits; it does not copy protected standard text or infer site-specific applicability.

## Validation performed

```text
python scripts/validate-source-standards-standard.py
PASS: AM-07 source and standards standard; 9 source classes; 5 precedence ranks; 5 jurisdiction systems; 6 example records; 8 freshness states; 22 legacy AM-04/05 source records compatible; 12 acceptance scenarios; no source fetched or legal applicability evaluated.

python scripts/validate-skill-authoring-standard.py
PASS: AM-06 authoring standard; package layout, frontmatter, 16 ordered sections, host metadata, references, output contract, 4 validation layers, 11 scenario categories, and templates verified; no skill implementation or host installation evaluated.

python scripts/validate-safety-boundary-model.py
PASS: AM-05 model; 4 classes; 9 topic gates; 14 source records; 12 acceptance scenarios; AM-03 safety counts preserved (95/28/11/25); no safety approval, engineering signoff, or skill behavior evaluated.

python scripts/validate-jurisdiction-model.py
PASS: AM-04 model; 4 flags; 5 applicability states; 8 source records; 5 initial extensions; 7 acceptance scenarios; no legal applicability or skill behavior evaluated.

python scripts/validate-taxonomy.py
PASS: 159 accepted records; 162 drafts audited across eight criteria; 166 original names traced; 76 ordered evidence-reuse edges; core isolation, reference priorities, pending classifications and all document projections verified. No skill behavior evaluated.

python scripts/validate-candidate-register.py
PASS: 162 draft candidates; 20 families; 166 original names traced; fields, metadata, provenance, dependency references/cycles, core isolation, AM-10 priorities, and review index checked.
```

## Regulatory, safety, and governance review

The standard requires source identity, jurisdiction, as-of dates, rights status, and review handoffs before a source-dependent output. It explicitly separates official status from reproduction permission and separates standards metadata from mandatory applicability. It does not provide legal advice, engineering approval, certification, permit authority, or operational authorization.

## Known limitations

- The validator is offline and does not prove that a URL is reachable, current, authoritative for a particular claim, or legally applicable.
- The AM-04 and AM-05 registries remain legacy-shaped until a later migration; new records must use the AM-07 schema.
- Rights classification is metadata and governance evidence, not a legal opinion or licence grant.
- The source examples are contracts and test data, not a complete Canadian source catalogue.
- Standards, provincial rules, and government pages can change; current conclusions require the recheck triggers and review ownership defined by AM-07.

## Explicitly not completed

AM-08 calculation standard, AM-09 executable validation, AM-10 reference skills, family implementation, sector packages, professional skillsets, and public release work remain open. Mass authoring remains gated on AM-10.

## Recommended next wave

Proceed to AM-08. Define a unit-safe calculation record and output standard that composes with AM-04 jurisdiction, AM-05 safety, AM-06 package, and AM-07 source/freshness contracts. Keep formulas, assumptions, rounding, uncertainty, and refusal boundaries separate from source applicability and legal conclusions.
