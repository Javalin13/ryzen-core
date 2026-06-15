# 05 — Supply Intelligence (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: supply-intelligence
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC supply intelligence**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *supply* in the Fleet ARC:
  - Driver onboarding (how drivers join, vetting, training, activation)
  - Vehicle procurement (how vehicles are added to the fleet, vehicle types, vehicle economics)
  - Supply expansion (growing the fleet in new cities, new regions, new vehicle types)
  - Driver retention (what keeps drivers active, what causes churn)
  - Supply intelligence that emerges from operational reality

## What does NOT belong here

- ❌ Supply-management code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ FleetConnect's own supply logic. The FleetConnect repo is the operational home; this folder is the *accumulation home*.
- ❌ Driver-facing onboarding flows (those are FleetConnect's product surface).

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated).
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
