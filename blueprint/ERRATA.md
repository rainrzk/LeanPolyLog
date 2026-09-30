# PolyLog Integrals — verification report and errata

All 16 practice identities (A001–A016) and the two auxiliary integrals inside A015 were checked numerically in two independent ways (`verify_polylog.py`, mpmath at 80 digits):

1. **Direct evaluation.** Each left side was computed by tanh-sinh quadrature, or by mpmath's polylog for the Li₂ values, and compared with the stated closed form.
2. **PSLQ.** Each closed form was recovered from the numerical value alone, using a standard basis of constants of the same weight.

**Result.** 15 of the 16 are correct, agreeing to 76–81 digits. PSLQ independently recovers every closed form with small integer coefficients.

## Corrections

| Item | Where (printed page) | Now | Should be |
|---|---|---|---|
| **A004** | p. 6 (statement), p. 7 (last line of proof) | ∫₀¹ log(1+x²)/x dx = π²/12 | **π²/24**, since −½·Li₂(−1) = −½·(−π²/12) = π²/24. Numerically 0.411233516712…. The derivation in A005 already uses the correct value. |
| A002 | p. 6, second line of "We have" | … = −⅛log²2 + **π³/32** + i·π log2/8 | **π²/32**, a typo in an intermediate step; the final result is correct |
| A011 | p. 10, 4th and 5th lines of the proof | arcsin **x** | arcsin **y** (the integration variable is y) |
| A016 | p. 16, 4th and 5th lines of the proof | arcsin **x** | arcsin **y** (same typo) |

## Optional simplification

**A014** can be written with one fewer polylogarithm:

∫₀¹ log x·log(1+x)/(1+x²) dx = 11π³/128 + (3π/32)·log²2 − 2G·log2 − 3·Im Li₃((1+i)/2),

using Im Li₃(1+i) = 7π³/128 + (3π/32)·log²2 − Im Li₃((1+i)/2). Both the identity and the simplified form were checked to 80 digits.

## Numerical values (for readers who want to check)

| Item | Value |
|---|---|
| A004 | 0.4112335167120566 |
| A005 | 0.3420140195059118 |
| A007 | −0.05129762746913569 |
| A008 | 0.1416180808959892 |
| A009 | 0.6584723256996341 |
| A010 | 0.08379017909020487 |
| A011 | 2.039508278814096 |
| A012 | −0.1670235885827575 |
| A013 | 0.1908243934286577 |
| A014 | −0.1739231642169534 |
| A015 | 0.2796245358225169 |
| A016 | 1.747225447100916 |

Reproduce with `python3 verify_polylog.py` (needs mpmath).
