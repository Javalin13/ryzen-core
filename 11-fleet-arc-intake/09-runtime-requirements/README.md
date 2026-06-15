# 09 — Runtime Requirements (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: runtime-requirements
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC runtime requirements**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *runtime requirements* for the Fleet ARC:
  - Performance requirements (latency, throughput, availability targets)
  - Integration requirements (which external systems the runtime must connect to: payment, CRM, notifications, etc.)
  - Concurrency requirements (how many concurrent bookings, drivers, customers)
  - State management requirements (what state is durable, what is ephemeral)
  - Failure recovery requirements (how the runtime recovers from crashes, network failures, payment failures)
  - Runtime requirements that emerge from real FleetConnect operations

## What does NOT belong here

- ❌ Runtime code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ The rebuild spec's R1–R4 phases (which live in `Javalin13/ryzen-continuity/RYZEN-REBUILD-SPECIFICATION-v1.0.md`). This folder is *Fleet ARC's* runtime-intelligence — discoveries that *inform* the future runtime, not duplicates of the rebuild spec.
- ❌ FleetConnect's own infrastructure requirements. The FleetConnect repo is the operational home; this folder is the *accumulation home*.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated).
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).
4. **Promotion rule:** A runtime-requirement discovery is *promoted* to the rebuild spec (R1–R4) or to the runtime roadmap (in `06-runtime-roadmap/ROADMAP.md`) only when the founder accepts the promotion via a new ADR. Per the continuity doctrine's "no implementation begins today" rule, promotions to runtime-requirement are the *first* step toward future implementation, not a commitment to implement.

## File Naming Convention

```
YYYY-MM-DD-NN-<short-slug>.md
```

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Runtime roadmap: `06-runtime-roadmap/ROADMAP.md`
- Rebuild spec: `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
