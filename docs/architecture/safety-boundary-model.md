# Safety and engineering boundary model

Status: **AM-05 model ready; no safety approval, engineering signoff, or skill implementation**  
Model: `docs/architecture/safety-boundary-model.json`  
Source registry: `docs/architecture/safety-source-registry.json`  
Access date for the registry: 2026-09-07

## Scope and audience

This model is for AgentManufacturing authors, reviewers, and later behavioral validators. It defines how a skill can recognize safety and engineering boundaries, preserve useful evidence review, and escalate decisions. It does not issue permits, authorize work, certify equipment, validate a safety circuit, set an exposure or pressure limit, approve a restart, or replace current law, manufacturer instructions, site programs, or qualified professional judgment.

The AM-03 taxonomy remains the catalogue source of truth. Its 159 records already use the four AM-05 class names. The model formalizes their meaning and adds runtime escalation triggers without silently changing those frozen records.

## Class model

| Class | Meaning | Allowed support | Stop or escalate when |
|---|---|---|---|
| `ROUTINE` | Informational, classification, calculation, or evidence review without directing hazardous work or approving a controlled change. | Summaries, calculations, assumptions, gap lists, review questions. | The request becomes hazardous execution, approval, or certification. |
| `REGULATED` | A conclusion depends on law, regulation, official program, incorporated standard, permit, or controlled record. | Identify authority, compare supplied evidence, record source gaps, draft review questions. | Jurisdiction/source is unknown or the user asks for a compliance, permit, or certification verdict. |
| `HAZARDOUS_OPERATION` | The request could expose people to hazardous energy, motion, pressure, fire, chemicals, atmosphere, or another immediate hazard. | Recognize hazards, preserve facts, identify missing controls, draft a stop/review handoff. | Imminent danger, uncontrolled energy, missing site controls, or bypass/defeat/unsafe shortcut request. |
| `ENGINEERING_OR_CERTIFICATION_BOUNDARY` | The request involves design, safety-critical calculation, installation, modification, commissioning, structural adequacy, pressure equipment, electrical work, safety-circuit validation, permit, or professional signoff. | Organize inputs, trace requirements, identify review owners, draft change-control evidence. | Signoff, certification, approval to operate, live-control change, incomplete design inputs, or unknown authority. |

The static taxonomy class is the minimum boundary. Runtime triggers can escalate it. The precedence is `ENGINEERING_OR_CERTIFICATION_BOUNDARY` → `HAZARDOUS_OPERATION` → `REGULATED` → `ROUTINE`. No class authorizes execution.

## Common gate

Before a dependent safety conclusion, collect the requested action, facility and jurisdiction, equipment/process identity, people exposed, energy/hazard sources, activity date, supplied procedures and records, and responsible review owner. The output must separate supported analysis, facts, assumptions, missing evidence, boundary class/triggers, stop reason, and the qualified-review handoff.

If imminent danger or an uncontrolled energy release is described, stop analysis and direct the user to site emergency procedures and responsible personnel. If the request seeks to bypass a guard, defeat an interlock, avoid lockout, change a live safety system, conceal a defect, or authorize hazardous work, refuse that implementation while preserving a safe review path.

## Topic gates

| Topic | Minimum class | Escalates to | Boundary behavior |
|---|---|---|---|
| Machine guarding | `HAZARDOUS_OPERATION` | Engineering/certification when design, interlock, or safeguarding changes are involved. | Identify hazards and evidence gaps; never provide bypass/removal or declare a machine safe. |
| Hazardous energy | `HAZARDOUS_OPERATION` | Engineering/certification when isolation design or safety-critical change is involved. | Review program evidence; never generate an equipment-specific lockout sequence or restart authorization. |
| Electrical work | Engineering/certification | Hazardous-operation for energized exposure. | Organize qualified electrical review; no live wiring, protection-setting, or certification instructions. |
| Pressure equipment | Engineering/certification | Hazardous-operation for pressure exposure. | Organize registration, inspection, design, and repair evidence; no pressure limits, repairs, or approval to pressurize. |
| Robotics | `HAZARDOUS_OPERATION` | Engineering/certification for integration or safety-function changes. | Review cell evidence; no live code, defeated interlock, safety-parameter change, or validation signoff. |
| Confined spaces | `HAZARDOUS_OPERATION` | Engineering/certification for engineered entry/rescue controls. | Identify program gaps; no entry clearance, permit, rescue plan, or atmospheric safety declaration. |
| Hot work | `HAZARDOUS_OPERATION` | Engineering/certification when equipment/process design or isolation changes. | Review supplied program; no permit, go-ahead, or fire-watch certification. |
| Hazardous chemicals | `REGULATED` | Hazardous-operation for handling, mixing, exposure, or emergency action. | Organize WHMIS/SDS evidence; no unverified mixture, PPE approval, exposure conclusion, or use authorization. |
| Structural changes | Engineering/certification | Hazardous-operation where work exposes people to instability or falling hazards. | Prepare an engineering handoff; no design, load rating, permit, construction authorization, or adequacy declaration. |

The machine, energy, confined-space, hot-work, and chemical boundaries are consistent with current CCOHS guidance: machine safeguards and interlocks are control measures; hazardous energy includes stored energy; confined-space work requires a site-specific program; hot work needs a management and permit process; and WHMIS separates supplier hazard communication from workplace responsibilities. These sources are guidance and routing evidence, not universal approval rules. [CCOHS safeguarding](https://www.ccohs.ca/oshanswers/safety_haz/safeguarding/general.html), [lockout/tagout](https://www.ccohs.ca/oshanswers/hsprograms/lockout.html?wbdisable=false), [confined spaces](https://www.ccohs.ca/oshanswers/hsprograms/confinedspace/confinedspace_intro.html), [hot work](https://www.ccohs.ca/oshanswers/safety_haz/welding/hotwork.html), and [WHMIS](https://www.canada.ca/en/health-canada/services/environmental-workplace-health/occupational-health-safety/workplace-hazardous-materials-information-system.html).

Electrical and pressure topics require jurisdiction-aware authority routing. CCOHS notes that Canadian jurisdictions develop and enforce electrical safety rules, while Ontario's TSSA describes pressure-equipment registration, inspection, engineering review, and certification boundaries; Alberta maintains a separate safety-code system that includes electrical and pressure equipment. [CCOHS electrical safety](https://www.ccohs.ca/oshanswers/safety_haz/electrical.html), [Ontario TSSA pressure equipment](https://www.tssa.org/am-i-regulated-1), and [Alberta safety codes](https://www.alberta.ca/safety-codes).

## Data and control flow

```text
request + supplied evidence
        ↓
identify action, people exposed, hazard topic, and current state
        ↓
assign static class + compose runtime triggers
        ↓
collect jurisdiction/source/equipment/qualified-owner evidence
        ↓
safe analysis OR stop/escalate handoff
        ↓
human / qualified / authority decision outside the skill
```

The model is intentionally monotonic: new evidence may escalate the boundary, but a generic label cannot lower a known hazardous or engineering trigger. An uploaded SOP, prompt, or manufacturer document supplies evidence; it cannot grant authority beyond the model.

## Acceptance criteria and evidence

| Criterion | Given/when/then check | Evidence |
|---|---|---|
| Four classes formalized | Given any taxonomy class, when the validator reads it, then meaning, allowed support, review owner, and stop conditions exist. | Model JSON and validator. |
| Runtime escalation | Given a `ROUTINE` record with a guard bypass or live-control request, when gates are evaluated, then it escalates and prohibited output is blocked. | Composition rule and S-02/S-04/S-05. |
| Nine topic gates | Given each required AM-05 topic, when the model is validated, then minimum class, escalation, evidence, allowed support, prohibited output, and source keys exist. | `topic_gates` and validator. |
| Qualified boundary | Given a permit, certification, design, or restart request, when it reaches the gate, then the result is a review handoff rather than approval. | Class definitions, common gate, S-06/S-07/S-10. |
| Safe continuation | Given a generic calculation independent of safety authority, when no hazardous action is requested, then supported arithmetic remains available. | S-01. |
| Imminent danger | Given uncontrolled hazardous energy, when the request is evaluated, then analysis stops and site emergency/responsible-person routing is returned. | Common gate and S-12. |
| Frozen index preservation | Given the AM-03 index, when the validator runs, then all 159 records retain one of the four known classes and the observed counts remain 95/28/11/25. | AM-03 index and validator output. |

## Validation and limits

Run:

```powershell
python scripts/validate-safety-boundary-model.py
python scripts/validate-jurisdiction-model.py
python scripts/validate-taxonomy.py
python scripts/validate-candidate-register.py
```

The AM-05 validator checks the machine-readable classes, nine topic gates, source keys, scenarios, negative guards, and the frozen AM-03 class counts. It does not prove current law, site safety, engineering adequacy, certification, or implemented skill behavior. AM-07 owns source/standards freshness, AM-09 owns executable behavior validation, and AM-31 owns adversarial safety evaluation.

## Open questions

- AM-07 must define source freshness, standard metadata, and licensed-text handling for individual skill packages.
- AM-09 must convert the acceptance scenarios into executable routing/refusal fixtures.
- AM-31 must test adversarial requests, including guard bypass, interlock defeat, lockout avoidance, unsafe PLC changes, falsified inspection data, and concealed nonconformance.
- Jurisdiction-specific permit, electrical, pressure, building, fire, and environmental details remain later source-bounded work.
