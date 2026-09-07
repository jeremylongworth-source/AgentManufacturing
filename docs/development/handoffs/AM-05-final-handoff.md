# AM-05 final handoff — safety and engineering boundary

## Wave

AM-05: Safety and engineering boundary

## Objective

Formalize `ROUTINE`, `REGULATED`, `HAZARDOUS_OPERATION`, and `ENGINEERING_OR_CERTIFICATION_BOUNDARY`, then define explicit gates for machine guarding, hazardous energy, electrical work, pressure equipment, robotics, confined spaces, hot work, hazardous chemicals, and structural changes.

## Verdict

**READY** for AM-05. The boundary model is source-grounded and validator-checked. It is an authoring and routing control, not safety approval, engineering signoff, certification, permit issuance, or implemented skill behavior.

## Completion token

```text
AGENTMANUFACTURING_AM_05_SAFETY_BOUNDARY_READY
```

## Scope completed

- Formalized all four safety classes with meaning, allowed support, review owner, and stop conditions.
- Defined monotonic runtime escalation: engineering/certification → hazardous operation → regulated → routine.
- Preserved the AM-03 taxonomy freeze and verified existing class counts: 95 routine, 28 regulated, 11 hazardous-operation, 25 engineering/certification-boundary.
- Added a common gate requiring action, site, jurisdiction, equipment, people exposed, hazards/energy, date, supplied controls, and review owner.
- Added topic-specific minimum class, escalation target, required evidence, allowed support, prohibited output, and source keys for all nine AM-05 gate topics.
- Added explicit stop behavior for imminent danger, uncontrolled energy, bypass/defeat requests, unsafe shortcuts, live-system changes, permits, certification, and restart authorization.
- Added 14 source records covering CCOHS safeguarding, machinery, hazardous energy, lockout, electrical, arc flash, robots/cobots, confined spaces, hot work, hazard identification, WHMIS, Ontario pressure equipment, and Alberta safety-code pathways.
- Added 12 acceptance scenarios spanning generic arithmetic, all major hazardous/engineering requests, regulated program review, and imminent danger.

## Files added

- `docs/architecture/safety-boundary-model.json` — canonical machine-readable model.
- `docs/architecture/safety-boundary-model.md` — architecture, gates, criteria, source rationale, and limits.
- `docs/architecture/safety-source-registry.json` — official guidance and authority metadata.
- `scripts/validate-safety-boundary-model.py` — structural validator preserving AM-03 counts.

## Files modified

- `README.md` — current wave, safety artifacts, and validation command.
- `ROADMAP.md` — AM-05 status, current target, and artifact links.

## Research performed

Reviewed current official or authoritative Canadian sources on 2026-09-07. CCOHS guidance covers safeguarding, machinery hazard assessment, lockout and hazardous energy, electrical safety, arc flash, robots/cobots, confined spaces, hot work, and hazard identification. Health Canada covers WHMIS roles and coordination. Ontario TSSA and Alberta safety-code sources establish pressure-equipment and safety-code authority boundaries. These sources ground routing and evidence requirements; they do not provide a universal site-specific approval rule.

## Validation performed

```text
python scripts/validate-safety-boundary-model.py
PASS: AM-05 model; 4 classes; 9 topic gates; 14 source records; 12 acceptance scenarios; AM-03 safety counts preserved (95/28/11/25); no safety approval, engineering signoff, or skill behavior evaluated.

python scripts/validate-jurisdiction-model.py
PASS: AM-04 model; 4 flags; 5 applicability states; 8 source records; 5 initial extensions; 7 acceptance scenarios; no legal applicability or skill behavior evaluated.

python scripts/validate-taxonomy.py
PASS: 159 accepted records; 162 drafts audited across eight criteria; 166 original names traced; 76 ordered evidence-reuse edges; core isolation, reference priorities, pending classifications and all document projections verified. No skill behavior evaluated.

python scripts/validate-candidate-register.py
PASS: 162 draft candidates; 20 families; 166 original names traced; fields, metadata, provenance, dependency references/cycles, core isolation, AM-10 priorities, and review index checked.
```

## Regulatory and safety review

The model preserves the AM-01 refusal boundary for guard bypass, interlock defeat, lockout avoidance, unsafe PLC or robot changes, concealed defects, and unsupported chemical or pressure instructions. It supports recognition, evidence organization, and escalation only. Current jurisdiction, source edition, site procedure, manufacturer instructions, and qualified review remain required for any dependent decision.

## Known limitations

- CCOHS materials are guidance and do not replace the applicable provincial, territorial, federal, municipal, fire, building, electrical, pressure, environmental, or sector rules.
- The source registry is an initial set, not exhaustive Canadian coverage.
- The model does not execute behavioral routing, refusal, emergency, or adversarial tests; AM-09 and AM-31 own those checks.
- No equipment-specific procedure, design, code change, permit, certification, or restart decision is produced.

## Explicitly not completed

AM-06 authoring standard, AM-07 source/standards standard, AM-08 calculation standard, AM-09 executable validation, AM-10 reference skills, family implementation, and public release work remain open. Mass authoring remains gated on AM-10.

## Recommended next wave

Proceed to AM-06. Read this handoff, the AM-05 model and source registry, AM-04 jurisdiction model, AM-01 scope boundaries, and AM-03 taxonomy before defining the portable `SKILL.md`, `agents/openai.yaml`, references, assets, and test fixture standard.
