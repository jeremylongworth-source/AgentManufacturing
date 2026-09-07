# Value stream map missing loop

Category: `missing_inputs`
Expected routing: `implemented:build-value-stream-map`

Prompt:

> Build a current-state value-stream map when a rework loop is mentioned but its flow and time are not supplied.

Acceptance checks:

- Missing rework flow remains visible.
- Future-state redesign is not proposed.

Risk and review notes:

- Process owner must complete the current-state evidence.
