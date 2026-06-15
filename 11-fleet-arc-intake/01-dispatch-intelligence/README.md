# 01 — Dispatch Intelligence (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: dispatch-intelligence
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC dispatch intelligence**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component* (it is not a dispatching system; it is a documentation accumulation layer).

## What belongs here

- Patterns, decisions, and learnings about *dispatching* in the Fleet ARC:
  - Driver assignment (which driver to assign to which booking)
  - Route optimization (the optimal path for a given booking)
  - Timeline coordination (when to dispatch, when to arrive, when to complete)
  - Real-time re-dispatching (handling cancellations, no-shows, exceptions)
  - Dispatch intelligence that emerges from operational reality

## What does NOT belong here

- ❌ Dispatching code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ FleetConnect's own dispatching logic. The FleetConnect repo is the operational home; this folder is the *accumulation home* for discoveries that emerge from FleetConnect but belong in the Ryzen continuity layer.
- ❌ Customer-facing dispatch interfaces. Those are FleetConnect's product surface, not the Ryzen continuity layer.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated) defined in `11-fleet-arc-intake/README.md`.
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).

## File Naming Convention

Each intake file is named:

```
YYYY-MM-DD-NN-<short-slug>.md
```

- `YYYY-MM-DD` — the date the intake was added.
- `NN` — a sequence number (01, 02, ...) for intakes added on the same day.
- `<short-slug>` — a kebab-case slug describing the discovery.

Example: `2026-07-15-01-driver-assignment-by-proximity.md`

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
