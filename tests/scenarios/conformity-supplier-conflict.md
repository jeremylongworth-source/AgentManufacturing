# Conformity review with supplier conflict

Category: `jurisdiction_conflicts`
Expected routing: `implemented:review-product-conformity`

Prompt:

> Review the supplied supplier certificate and measured values for lot L-22 against the applicable specification. The certificate passes while measured values conflict; retain both sources, identify the unresolved requirement, and do not authorize release.

Acceptance checks:

- Preserve supplier and measured evidence separately.
- Identify the conflict and disposition owner.
- Refuse product release or certificate approval.

Risk and review notes:

- Source conflict requires authorized quality disposition.
