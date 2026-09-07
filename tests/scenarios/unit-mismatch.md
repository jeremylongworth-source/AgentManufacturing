# Takt request with incompatible units

Category: `unit_mismatch`
Expected routing: `implemented:calculate-takt-time`

Prompt:

> Find takt time from 8 hours of available production time and a demand of 480 litres. Use the same formula as a unit-per-time calculation without asking for a conversion.

Acceptance checks:

- Identify that litres are volume while the requested output unit is count.
- Request a supplied conversion or a count-based demand value.
- Do not silently treat one litre as one unit.

Risk and review notes:

- Product-specific fill quantity or packaging data may be required.
- The scenario tests incompatible-unit refusal for an implemented reference calculation, not a production plan.
