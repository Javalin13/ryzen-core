# 02 — Capacity Intelligence (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: capacity-intelligence
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC capacity intelligence**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *capacity* in the Fleet ARC:
  - Driver availability (who is available, when, where)
  - Vehicle availability (which vehicles are in service, which are in maintenance)
  - Supply matching (matching driver supply to customer demand)
  - Capacity forecasting (predicting capacity gaps, planning supply expansion)
  - Capacity intelligence that emerges from operational reality

## What does NOT belong here

- ❌ Capacity-management code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ FleetConnect's own capacity logic. The FleetConnect repo is the operational home; this folder is the *accumulation home*.
- ❌ Driver-facing capacity interfaces. Those are FleetConnect's product surface, not the Ryzen continuity layer.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated) defined in `11-fleet-arc-intake/README.md`.
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).

## File Naming Convention

```
YYYY-MM-DD-NN-<short-slug>.md
```

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
