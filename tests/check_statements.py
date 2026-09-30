"""Numerical twins of the Lean statements in LeanPolyLog/Statements.lean.

Lean checks proofs, not meaning, so each formal statement is re-evaluated here, formula for
formula, at 80 significant digits. The left side comes from quadrature (or the defining series);
the right side is the stated closed form. The script exits with status 1 if any identity agrees
to fewer than 60 digits.

Keep this file in sync with Statements.lean: same identities, same closed forms.
"""
import sys

import mpmath as mp

mp.mp.dps = 80
pi, L2 = mp.pi, mp.log(2)
G = mp.catalan
zeta3 = mp.zeta(3)
Li = mp.polylog                                  # series definition agrees on the closed unit disk
q = lambda f, a, b: mp.quad(f, [a, (a + b) / 2, b])
I = mp.mpc(0, 1)

STATEMENTS = {
    "A001": (lambda: Li(2, I), lambda: -pi**2 / 48 + G * I),
    "A002": (lambda: Li(2, 1 / (1 + I)), lambda: 5 * pi**2 / 96 - L2**2 / 8 + (pi / 8 * L2 - G) * I),
    "A003": (lambda: Li(2, (mp.sqrt(5) - 1) / 2), lambda: pi**2 / 10 - mp.log((1 + mp.sqrt(5)) / 2)**2),
    "A004": (lambda: q(lambda x: mp.log(1 + x**2) / x, 0, 1), lambda: pi**2 / 24),
    "A005": (lambda: q(lambda x: mp.log(1 + x**2)**2 / x**3, 0, 1), lambda: pi**2 / 12 - L2**2),
    "A006_cos": (lambda: q(lambda x: mp.log(mp.cos(x)), 0, pi / 4), lambda: G / 2 - pi / 4 * L2),
    "A006_sin": (lambda: q(lambda x: mp.log(mp.sin(x)), 0, pi / 4), lambda: -G / 2 - pi / 4 * L2),
    "A007": (lambda: q(lambda x: x * mp.log(mp.cos(x)), 0, pi / 4),
             lambda: pi * G / 8 - pi**2 / 32 * L2 - mp.mpf(21) / 128 * zeta3),
    "A008": (lambda: q(lambda x: x * mp.log(1 + mp.tan(x)), 0, pi / 4),
             lambda: pi**2 / 64 * L2 - pi * G / 8 + 21 * zeta3 / 64),
    "A009": (lambda: q(lambda x: x**2 * mp.cot(x), 0, pi / 2), lambda: pi**2 / 4 * L2 - mp.mpf(7) / 8 * zeta3),
    "A010": (lambda: q(lambda x: x**2 * mp.tan(x)**2, 0, pi / 4),
             lambda: -G + pi**2 / 16 - pi**3 / 192 + pi / 4 * L2),
    # A011/A016: substitute x = sin t (dx / (x sqrt(1-x^2)) = dt / sin t) for full precision
    "A011": (lambda: q(lambda t: Li(2, mp.sin(t)) / mp.sin(t), 0, pi / 2),
             lambda: mp.mpf(3) / 8 * pi**2 * L2 - mp.mpf(7) / 16 * zeta3),
    "A012": (lambda: q(lambda x: mp.atan(x) / (x + 1) * mp.log(x), 0, 1), lambda: -pi**3 / 64 + G / 2 * L2),
    "A013": (lambda: q(lambda x: mp.atan(x) / (x + 1) * mp.log(x)**2, 0, 1),
             lambda: -pi**2 / 24 * G - pi**3 / 32 * L2 + 21 * pi / 64 * zeta3),
    "A014": (lambda: q(lambda x: mp.log(x) * mp.log(x + 1) / (x**2 + 1), 0, 1),
             lambda: 11 * pi**3 / 128 + 3 * pi / 32 * L2**2 - 2 * G * L2 - 3 * mp.im(Li(3, (1 + I) / 2))),
    "A015": (lambda: q(lambda x: x * mp.log(mp.sin(x))**2, 0, pi / 2),
             lambda: Li(4, 0.5) - 19 * pi**4 / 2880 + L2**4 / 24 + pi**2 * L2**2 / 12),
    "A016": (lambda: q(lambda t: Li(3, mp.sin(t)) / mp.sin(t), 0, pi / 2),
             lambda: Li(4, 0.5) / 2 + 41 * pi**4 / 5760 + L2**4 / 48 + pi**2 * L2**2 / 6),
}

failed = []
for name, (lhs, rhs) in STATEMENTS.items():
    a, b = lhs(), rhs()
    d = abs(a - b)
    digits = 80 if d == 0 else int(-mp.log10(d / max(abs(b), mp.mpf(1))))
    ok = digits >= 60
    print(f"{name:<9} agree to {digits:>3} digits   {'ok' if ok else 'FAIL'}")
    if not ok:
        failed.append(name)
print("all statements confirmed numerically" if not failed else f"FAILED: {failed}")
sys.exit(1 if failed else 0)
