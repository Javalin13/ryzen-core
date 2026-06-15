# 08 — Verification Requirements (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: verification-requirements
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC verification requirements**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *verification* in the Fleet ARC:
  - Reasoning patterns (how the system reasons about a booking, a dispatch decision, a pricing decision)
  - Critique patterns (how the system critiques its own reasoning, what it checks for)
  - Validation patterns (what must be validated before an action executes, who can override)
  - Recursion levels (which actions need 1-pass verification, which need 2-pass, which need 3-pass)
  - Failure modes (what kinds of failures are observed, what the recovery is)
  - Verification requirements that emerge from real FleetConnect operations

## What does NOT belong here

- ❌ Verification-engine code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ The 3-stage Recursive Verification pattern (which lives in the recovery archive's `RECOVERED-REUSABLE-CONCEPTS.md`, concept C3). This folder is *Fleet ARC's* verification intelligence — discoveries that *inform* the future verification engine, not duplicates of the concept.
- ❌ FleetConnect's own validation logic. The FleetConnect repo is the operational home; this folder is the *accumulation home*.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated).
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).
4. **Promotion rule:** A verification-requirement discovery is *promoted* to the rebuild spec's Verification Engine section only when the founder accepts the promotion.

## File Naming Convention

```
YYYY-MM-DD-NN-<short-slug>.md
```

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- C3 (3-stage Recursive Verification) in recovery archive: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` §"C3"
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
