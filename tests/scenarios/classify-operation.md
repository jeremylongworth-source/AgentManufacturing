# Classify a transformation operation

Category: `correct_invocation`
Expected routing: `implemented:classify-manufacturing-operation`

Prompt:

> Classify this operation: components are assembled, tested, and finished into a sellable unit in a batch process. Separate the manufacturing boundary from adjacent warehouse transfers and list unresolved facts. Do not provide a legal industry code.

Acceptance checks:

- Identify the supplied assembly and finishing evidence as the manufacturing operation boundary.
- Separate warehouse movement from the classification.
- Preserve the distinction between operational routing and formal legal classification.

Risk and review notes:

- The result supports routing only and does not establish a NAICS or legal determination.
