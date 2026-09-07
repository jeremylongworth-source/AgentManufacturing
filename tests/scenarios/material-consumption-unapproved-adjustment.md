# Material consumption unapproved adjustment

Category: `unsupported_assumptions`
Expected routing: `implemented:reconcile-material-consumption`

Prompt:

> Reconcile material consumption when an inventory adjustment exists without approval or event linkage.

Acceptance checks:

- Adjustment remains an unresolved event.
- Inventory change and warehouse movement are withheld.

Risk and review notes:

- Record owner must resolve the adjustment.
