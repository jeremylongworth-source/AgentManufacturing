# Professional skillset composition

AM-28 implements the 18 roles preserved in the [initial framework](domain-framework.md#professional-skillsets). Each role has a workflow manifest and a short guide in [skillsets](../../skillsets/index.json). Atomic procedures and formulas stay in their existing packages.

## Selection and evidence semantics

Choose a workflow from the requested outcome, not merely the user's job title. A role is a capability menu; membership is not permission to run every skill. The resolver lists direct targets and their transitive evidence providers in dependency order. Providers are references for acquiring or checking evidence, not mandatory execution when compatible evidence already exists.

Workflow order is a presentation order. Frozen taxonomy evidence edges control prerequisite ordering. Missing or incompatible evidence must remain visible and block only dependent conclusions. Keep scope, units, product/process, time interval, source revision and uncertainty attached to each artifact. No aggregate READY state may erase an unresolved atomic gate.

Overlay routes are explicitly selected research, separate from automatic applicability. An EHS workflow may already include WHMIS targets because that is its named task; generic capacity work does not acquire Canadian legal dependencies by role membership. Sector-specific coverage remains AM-29 and later work.

## Manifest and resolver contract

[Composition contract](../../skillsets/composition-contract.json) holds conditional research routes, canonical package paths and shared output fields. [Role index](../../skillsets/index.json) lists exactly the preserved 18 roles. Role manifests use JSON syntax valid as YAML, with workflow IDs, triggers, evidence inputs, target skill names, outputs and review boundaries.

[Resolver](../../scripts/resolve-skillset.py) accepts a role, workflow and optional named overlays; returns selected targets, explicitly selected overlays, ordered skill references, evidence dependencies and safety classes. It only reads local files and emits JSON. It neither executes skills nor evaluates applicability or readiness.

Canonical mapping selects Family 09 nonconformance/CAPA and Family 11 manufacturing-safety packages for the two duplicated AM-10 names. Historical reference paths remain untouched; manifests refer to a skill name once and the resolver emits one canonical path.

## Validation and limits

The AM-28 gate verifies all role manifests, canonical paths, workflow targets and transitive dependencies, role scenario coverage, and resolver tests. Runtime model behavior remains NOT_RUN. Existing atomic validation is structural and deterministic where applicable, not professional certification, source currency, model adherence or release authority.

The local AgentSkills engineering-delivery and AgentLogistics warehouse-supervisor manifests were inspected as composition patterns on 2026-09-08. Their procedures, licensing and host-specific installation behavior are not imported. This wave adds no installer, live integration, role authorization or sector-specific requirement.
