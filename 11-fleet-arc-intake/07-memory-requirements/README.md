# 07 — Memory Requirements (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: memory-requirements
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC memory requirements**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *memory* in the Fleet ARC:
  - Operational memory (what needs to be remembered for the duration of a single booking)
  - Strategic memory (what needs to be remembered across bookings, across drivers, across customers)
  - Creator memory (what needs to be remembered about the founder, the doctrine, the system)
  - Governance memory (what needs to be remembered for audit, compliance, post-mortem analysis)
  - Memory layer requirements (which discoveries belong in which of the 4 layers)
  - Memory retention requirements (how long, why, what triggers deletion)
  - Memory requirements that emerge from real FleetConnect operations

## What does NOT belong here

- ❌ Memory-federation code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ The 4-layer memory model (which lives in the recovery archive's `RECOVERED-REUSABLE-CONCEPTS.md`, concept C2). This folder is *Fleet ARC's* memory intelligence — discoveries that *inform* the future memory federation, not duplicates of the concept.
- ❌ FleetConnect's own data storage. The FleetConnect repo is the operational home; this folder is the *accumulation home*.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated).
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).
4. **Promotion rule:** A memory-requirement discovery is *promoted* to the rebuild spec's Memory Federation section only when the founder accepts the promotion. Per the continuity doctrine's "recovery does not automatically imply adoption" rule applied to *new* memory requirements.

## File Naming Convention

```
YYYY-MM-DD-NN-<short-slug>.md
```

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- C2 (4-layer Memory Model) in recovery archive: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` §"C2"
- D2 (semantic memory implementation) open decision: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/OPEN-DECISIONS.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
