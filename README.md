# LeanPolyLog

A complete Lean 4 / Mathlib formalization of the sixteen identities in *PolyLog Integrals* (rainrzk, 2022; [`blueprint/Polylog.pdf`](blueprint/Polylog.pdf)). The identities are log-trigonometric and polylogarithmic integrals, with closed forms in π, log 2, Catalan's constant G, ζ(3), Li₄(½) and Im Li₃((1+i)/2).

All sixteen are proven. There is no `sorry`, and every proof depends only on the standard axioms (`propext`, `Classical.choice`, `Quot.sound`).

## Layout
- [`Defs.lean`](LeanPolyLog/Defs.lean): Mathlib has no polylogarithms or Catalan's constant yet, so `Li s z` (and its real version `Lir s x`), `G` and `zeta3` are defined by their series.
- [`Statements.lean`](LeanPolyLog/Statements.lean): all sixteen statements, in one readable list.
- [`Proofs/`](LeanPolyLog/Proofs): one file per identity.
- [`Lemmas/`](LeanPolyLog/Lemmas): the shared machinery, including dilogarithm identities, Fubini kernels, and a radial substitute for the half-disc Cauchy theorem.

## How it is checked
- The Lean kernel checks every proof.
- [`tests/Axioms.lean`](tests/Axioms.lean) fails CI if any proof picks up `sorry` or a non-standard axiom.
- Lean cannot check that a statement says what was meant. So each statement also has a **numerical twin** in [`tests/check_statements.py`](tests/check_statements.py), evaluated with mpmath at 80 digits. CI requires agreement to 60 digits.

## The identities
| id | identity | prior appearances |
|---|---|---|
| A001 | Li₂(i) = −π²/48 + iG | classical: Li_s(±i) = −2^{−s}η(s) ± iβ(s) |
| A002 | Li₂(1/(1+i)) | classical (Landen at z = i); [MSE 2014](https://math.stackexchange.com/a/984371) |
| A003 | Li₂((√5−1)/2) = π²/10 − log²φ | classical (Landen); see Zagier (2007) |
| A004 | ∫₀¹ log(1+x²)/x = π²/24 | classical (G&R 4.291.1 with t = x²) |
| A005 | ∫₀¹ log²(1+x²)/x³ | none found |
| A006 | ∫₀^{π/4} log cos, log sin | classical (G&R 4.224) |
| A007 | ∫₀^{π/4} x log cos x | [MSE 2019](https://math.stackexchange.com/a/3200545) |
| A008 | ∫₀^{π/4} x log(1+tan x) | equivalent arctan form: [MSE 2019](https://math.stackexchange.com/a/3441045) |
| A009 | ∫₀^{π/2} x² cot x | classical (Euler); [MSE 2015](https://math.stackexchange.com/a/1406313) |
| A010 | ∫₀^{π/4} x² tan² x | equivalent form: [MSE 2014](https://math.stackexchange.com/q/629940) |
| A011 | ∫₀¹ Li₂(x)/(x√(1−x²)) | [MSE 2019](https://math.stackexchange.com/a/3085474) |
| A012 | ∫₀¹ arctan x · log x/(1+x) | [MSE 2016](https://math.stackexchange.com/q/1842284) |
| A013 | ∫₀¹ arctan x · log² x/(1+x) | Vălean, *(Almost) Impossible Integrals, Sums, and Series* (2019) |
| A014 | ∫₀¹ log x · log(1+x)/(1+x²) | [MSE 2018](https://math.stackexchange.com/a/2972249) (same simplified form) |
| A015 | ∫₀^{π/2} x log² sin x | [MSE 2016](https://math.stackexchange.com/questions/1640940/#comment3346568_1640940); Borwein–Straub (2012), [arXiv:1103.3893](https://arxiv.org/abs/1103.3893) |
| A016 | ∫₀¹ Li₃(x)/(x√(1−x²)) | [MSE 2020](https://math.stackexchange.com/a/3870374) |

The tutorial's proofs were written independently in 2022. The last column lists earlier public appearances that were found afterwards.

## Authorship
The proofs are the author's, from the 2022 tutorial, and the formalization follows them. The main differences:
- **A004** uses the corrected value π²/24 (see [ERRATA](blueprint/ERRATA.md)).
- **A013** evaluates its double integral by symmetrising it over the square.
- **A014** uses complex primitives that stay inside the unit disk, where the series `Li` is defined, instead of passing through Li₃(1+i). Its statement uses the equivalent simplified form.
- **A015** differentiates in the radius instead of integrating over a half-disc contour, because Mathlib has no half-disc Cauchy theorem.

The Lean code was written with AI assistance (Claude). The author reviewed and verified every statement and proof, in addition to the machine checks above.

## Build
```
lake exe cache get      # download Mathlib's prebuilt files
lake build
lake env lean tests/Axioms.lean
python3 tests/check_statements.py
```

## License
The Lean code and scripts are released under Apache-2.0 (see [LICENSE](LICENSE)). `blueprint/Polylog.pdf` is © 2022 rainrzk.
