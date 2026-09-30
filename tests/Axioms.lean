import LeanPolyLog

/-!
# Axiom check for the finished proofs

Every theorem marked as proven in the README may use only the three standard axioms. A proof
that falls back to `sorry` would pick up `sorryAx`, and `#guard_msgs` would then fail this file.
CI runs it with `lake env lean tests/Axioms.lean`. Add a block here whenever a proof is finished.
-/

/-- info: 'LeanPolyLog.A001' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A001

/-- info: 'LeanPolyLog.A004' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A004

/-- info: 'LeanPolyLog.A005' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A005

/-- info: 'LeanPolyLog.A006_cos' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A006_cos

/-- info: 'LeanPolyLog.A006_sin' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A006_sin
