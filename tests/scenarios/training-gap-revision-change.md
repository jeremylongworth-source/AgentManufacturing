# Training gap revision change

Category: `unsupported_assumptions`
Expected routing: `implemented:identify-training-gap`

Prompt:

> Identify a training gap after a work instruction changed revision but the learning record still cites the old revision.

Acceptance checks:

- Revision conflict is exposed.
- Qualification is not revoked or granted automatically.

Risk and review notes:

- Training owner review is required.
