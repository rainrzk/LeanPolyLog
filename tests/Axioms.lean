import LeanPolyLog

/-!
# Axiom check for the finished proofs

Every theorem marked as proven in the README may use only the three standard axioms. A proof
that falls back to `sorry` would pick up `sorryAx`, and `#guard_msgs` would then fail this file.
CI runs it with `lake env lean tests/Axioms.lean`. Add a block here whenever a proof is finished.
-/

/-- info: 'LeanPolyLog.A001' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A001

/-- info: 'LeanPolyLog.A002' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A002

/-- info: 'LeanPolyLog.A003' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A003

/-- info: 'LeanPolyLog.A004' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A004

/-- info: 'LeanPolyLog.A005' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A005

/-- info: 'LeanPolyLog.A006_cos' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A006_cos

/-- info: 'LeanPolyLog.A006_sin' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A006_sin

/-- info: 'LeanPolyLog.A007' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A007

/-- info: 'LeanPolyLog.A008' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A008

/-- info: 'LeanPolyLog.A009' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A009

/-- info: 'LeanPolyLog.A010' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A010

/-- info: 'LeanPolyLog.A011' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A011

/-- info: 'LeanPolyLog.A012' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A012

/-- info: 'LeanPolyLog.A013' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A013

/-- info: 'LeanPolyLog.A014' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in #print axioms LeanPolyLog.A014
