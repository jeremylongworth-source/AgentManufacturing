# AM-04 final handoff — Canadian jurisdiction model

## Wave

AM-04: Canadian jurisdiction model

## Objective

Formalize the four Canadian jurisdiction flags, applicability states, context requirements, source hierarchy, and initial federal/Ontario/British Columbia/Alberta/Quebec extension pattern while preserving the AM-03 taxonomy freeze.

## Verdict

**READY** for AM-04. The model is source-backed and validator-checked. It is routing metadata and architecture, not a legal conclusion or an implemented skill.

## Completion token

```text
AGENTMANUFACTURING_AM_04_JURISDICTION_MODEL_READY
```

## Scope completed

- Defined `CANADA_FEDERAL`, `PROVINCIAL_REQUIRED`, `SECTOR_REGULATED`, and `STANDARDS_DEPENDENT` as composable investigation flags.
- Defined `GENERIC_METHOD_ONLY`, `PENDING_CONTEXT`, `SOURCE_REVIEW_REQUIRED`, `COVERAGE_GAP`, and `CONFLICT_REVIEW_REQUIRED` as explicit applicability states.
- Required context now distinguishes product/supplier from workplace, environmental, transport, labelling, contract-standard, and other domains.
- Specified unknown, not-applicable, and conflicting context behavior. Missing jurisdiction blocks only dependent conclusions; unrelated unit-safe arithmetic can continue.
- Defined a five-rank source hierarchy and evidence fields for publisher, URL, scope, access date, page/effective date, freshness, and unresolved applicability.
- Added source-bounded extension records for federal, Ontario, British Columbia, Alberta, and Quebec.
- Added seven acceptance scenarios covering generic arithmetic, Ontario workplace review, federal product/workplace separation, Quebec/Ontario substitution, unsupported territory coverage gaps, WHMIS supplier/workplace separation, and stale/conflicting dates.
- Reviewed the 159 accepted AM-03 records. Their existing `GENERIC_METHOD_ONLY` and `PENDING_CONTEXT` values map to the formal model, so no silent record reclassification was made and the AM-03 freeze remains valid.

## Files added

- `docs/architecture/canadian-jurisdiction-model.json` — canonical machine-readable model.
- `docs/architecture/canadian-jurisdiction-model.md` — architecture, decisions, boundaries, criteria, and limits.
- `docs/architecture/canadian-source-registry.json` — eight official source records with access and freshness metadata.
- `scripts/validate-jurisdiction-model.py` — structural validator.

## Files modified

- `README.md` — current wave, model entry points, and validation command.
- `ROADMAP.md` — AM-04 status, current target, and artifact links.

## Research performed

The registry records the official sources reviewed on 2026-09-07: federal regulated-industry routing and workplace OH&S scope; Health Canada WHMIS supplier guidance; Ontario OHSA overview; WorkSafeBC OHS Regulation; Alberta OHS Code; Quebec's official OHS Act; and Statistics Canada's manufacturing classification. The sources establish routing boundaries and source ownership. They do not establish a universal Canadian rule or replace current legal review.

## Validation performed

```text
python scripts/validate-jurisdiction-model.py
PASS: AM-04 model; 4 flags; 5 applicability states; 8 source records; 5 initial extensions; 7 acceptance scenarios; no legal applicability or skill behavior evaluated.

python scripts/validate-taxonomy.py
PASS: 159 accepted records; 162 drafts audited across eight criteria; 166 original names traced; 76 ordered evidence-reuse edges; core isolation, reference priorities, pending classifications and all document projections verified. No skill behavior evaluated.

python scripts/validate-candidate-register.py
PASS: 162 draft candidates; 20 families; 166 original names traced; fields, metadata, provenance, dependency references/cycles, core isolation, AM-10 priorities, and review index checked.
```

## Regulatory and safety review

The model explicitly separates federal product/supplier evidence from workplace jurisdiction and preserves the AM-01 qualified-review boundary. It does not classify a site, certify a product, select a standard edition without evidence, issue a permit, or authorize hazardous work. Safety mechanics remain AM-05 work.

## Known limitations

- The registry is an initial routing set, not complete coverage of every Canadian statute, regulation, municipality, sector, permit, or standard.
- Current source text and effective-date review remain required at skill execution time; `current_on_access` is a registry freshness label, not a legal guarantee.
- Provincial extension records are source paths and boundaries, not provincial skill packages.
- No skill behavior, calculation correctness, source freshness automation, or legal applicability was evaluated.

## Explicitly not completed

AM-05 safety boundary, AM-06 authoring standard, AM-07 source/standards standard, AM-08 calculation standard, AM-09 executable validation, AM-10 reference skills, all family implementation, and public release work remain open. Mass authoring remains gated on AM-10.

## Recommended next wave

Proceed to AM-05. Read this handoff, the AM-04 model and registry, the AM-01 scope boundaries, and the AM-03 index before formalizing safety and engineering boundary classes. Preserve the product/workplace separation and no-default-jurisdiction guardrails.
