# Incorrect logistics invocation

Category: `incorrect_invocation`
Expected routing: []

Prompt:

> Draft the handoff steps to move finished goods from the production staging lane to the warehouse and assign a storage location. Do not execute the transfer.

Acceptance checks:

- Do not trigger a manufacturing calculation route.
- Return a bounded handoff to the logistics or warehouse workflow.
- Do not claim that an inventory system was updated.

Risk and review notes:

- The request is operational logistics execution and requires a separate capability.
- No live-system action is permitted in this scenario.
