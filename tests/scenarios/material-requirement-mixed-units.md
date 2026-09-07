# Material requirement mixed units

Category: `unit_mismatch`
Expected routing: `implemented:calculate-material-requirement`

Prompt:

> Calculate gross component need when the BOM quantity is in kilograms and product quantity is in pieces without a conversion basis.

Acceptance checks:

- Incompatible units are not silently converted.
- Net requirement and warehouse replenishment remain out of scope.

Risk and review notes:

- A unit owner must supply the conversion basis.
