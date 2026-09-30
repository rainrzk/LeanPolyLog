# LeanPolyLog

A Lean 4 / Mathlib formalization of the sixteen identities in *PolyLog Integrals* (rainrzk, 2022; [`blueprint/Polylog.pdf`](blueprint/Polylog.pdf)). The integrals are log-trigonometric and polylogarithmic, with closed forms in π, log 2, Catalan's constant G, ζ(3), Li₄(½) and Im Li₃((1+i)/2).

Mathlib has neither polylogarithms nor Catalan's constant yet, so [`LeanPolyLog/Defs.lean`](LeanPolyLog/Defs.lean) defines them by their series:
- `Li s z`, with a real version `Lir s x`;
- `G`;
- `zeta3`.

All sixteen statements are in [`LeanPolyLog/Statements.lean`](LeanPolyLog/Statements.lean). Finished proofs are in [`LeanPolyLog/Proofs/`](LeanPolyLog/Proofs), one file per identity, and helper lemmas are in [`LeanPolyLog/Lemmas/`](LeanPolyLog/Lemmas). `Statements.lean` only references the proofs, so it remains a single list of everything claimed.

## How statements and proofs are checked
Lean checks proofs, not whether a statement says what was meant. So every formal statement also has a **numerical twin** in [`tests/check_statements.py`](tests/check_statements.py): the same formula, evaluated with mpmath at 80 digits. CI requires every twin to agree to at least 60 digits.

Finished proofs have their own check. [`tests/Axioms.lean`](tests/Axioms.lean) uses `#guard_msgs` to confirm that each one depends only on `propext`, `Classical.choice` and `Quot.sound`. If a proof ever falls back to `sorry`, CI fails.

## Status

| id | identity | statement | proof | prior appearances / credit |
|---|---|---|---|---|
| A001 | Li₂(i) = −π²/48 + iG | ✅ | ✅ | classical: Li_s(±i) = −2^{−s}η(s) ± iβ(s) |
| A002 | Li₂(1/(1+i)) | ✅ | ⏳ | classical (Landen at z = i); [MSE 2014](https://math.stackexchange.com/a/984371) |
| A003 | Li₂((√5−1)/2) = π²/10 − log²φ | ✅ | ⏳ | classical (Landen); see Zagier (2007) |
| A004 | ∫₀¹ log(1+x²)/x = π²/24 | ✅ | ✅ | classical (G&R 4.291.1 with t = x²); corrected value, see [ERRATA](blueprint/ERRATA.md) |
| A005 | ∫₀¹ log²(1+x²)/x³ | ✅ | ✅ | no prior appearance found |
| A006 | ∫₀^{π/4} log cos, log sin | ✅ | ✅ | classical (G&R 4.224) |
| A007 | ∫₀^{π/4} x log cos x | ✅ | ⏳ | [MSE 2019](https://math.stackexchange.com/a/3200545) |
| A008 | ∫₀^{π/4} x log(1+tan x) | ✅ | ⏳ | equivalent arctan form: [MSE 2019](https://math.stackexchange.com/a/3441045) |
| A009 | ∫₀^{π/2} x² cot x | ✅ | ⏳ | classical (Euler); [MSE 2015](https://math.stackexchange.com/a/1406313) |
| A010 | ∫₀^{π/4} x² tan² x | ✅ | ⏳ | equivalent form: [MSE 2014](https://math.stackexchange.com/q/629940) |
| A011 | ∫₀¹ Li₂(x)/(x√(1−x²)) | ✅ | ⏳ | [MSE 2019](https://math.stackexchange.com/a/3085474) |
| A012 | ∫₀¹ arctan x · log x/(1+x) | ✅ | ⏳ | [MSE 2016](https://math.stackexchange.com/q/1842284) |
| A013 | ∫₀¹ arctan x · log² x/(1+x) | ✅ | ⏳ | Vălean, *(Almost) Impossible Integrals, Sums, and Series* (2019) |
| A014 | ∫₀¹ log x · log(1+x)/(1+x²) | ✅ | ⏳ | [MSE 2018](https://math.stackexchange.com/a/2972249) (same simplified form) |
| A015 | ∫₀^{π/2} x log² sin x | ✅ | ⏳ | [MSE 2016](https://math.stackexchange.com/questions/1640940/#comment3346568_1640940); Borwein–Straub (2012), [arXiv:1103.3893](https://arxiv.org/abs/1103.3893) |
| A016 | ∫₀¹ Li₃(x)/(x√(1−x²)) | ✅ | ⏳ | [MSE 2020](https://math.stackexchange.com/a/3870374) |

In the statement column, ✅ means the statement typechecks and its numerical twin passes. In the proof column, ✅ means the Lean proof is complete: it has no `sorry`, and `#print axioms` lists only `propext`, `Classical.choice` and `Quot.sound`. ⏳ means the proof is still `sorry`. The tutorial's proofs were written independently in 2022. The credits column records earlier public appearances found afterwards.

## Build
```
lake exe cache get      # download Mathlib's prebuilt files
lake build
python3 tests/check_statements.py
```

## Disclosure
The definitions, statements and tests were written with the assistance of an AI assistant (Claude). The Lean kernel is the final judge of every proof, and each statement is cross-checked numerically.

## License
The Lean code and scripts are released under Apache-2.0 (see [LICENSE](LICENSE)). `blueprint/Polylog.pdf` is © 2022 rainrzk.
