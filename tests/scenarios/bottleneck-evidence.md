# Identify a bottleneck from comparable evidence

Category: `calculation_correctness`
Expected routing: `implemented:identify-manufacturing-bottleneck`

Prompt:

> Compare the supplied operation rates, queue records, downtime records, and demand rate for one shift. Identify the evidence-ranked bottleneck, preserve units and period, and state sensitivity to missing downtime data. Do not change the schedule.

Acceptance checks:

- Compare only rates with aligned units and period.
- Distinguish a measured finding from a hypothesis when downtime evidence is incomplete.
- Return the review owner without issuing a production change.

Risk and review notes:

- The scenario tests evidence handling rather than a live throughput decision.
