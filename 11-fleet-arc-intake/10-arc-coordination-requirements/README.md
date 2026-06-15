# 10 — ARC Coordination Requirements (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: arc-coordination-requirements
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC coordination requirements** with future ARCs (Earth, FamilieKompas). It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *ARC coordination* that the Fleet ARC needs:
  - Cross-ARC intelligence convergence (when does Fleet ARC need to share intelligence with Earth? With FamilieKompas?)
  - Cross-ARC memory sharing (what memory is shared across ARCs, what is ARC-local, what is creator-local)
  - Cross-ARC governance (which governance rules apply across ARCs, which are ARC-specific)
  - Cross-ARC workflows (workflows that span multiple ARCs, e.g., a FleetConnect customer who is also a FamilieKompas family member)
  - Constitutional boundaries (what Fleet ARC can do, what it cannot do, what it must defer to another ARC)
  - ARC coordination requirements that emerge from real FleetConnect operations

## What does NOT belong here

- ❌ ARC coordination code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ The R4 multi-ARC plan (which lives in the rebuild spec). This folder is *Fleet ARC's* coordination intelligence — discoveries that *inform* the future multi-ARC architecture, not duplicates of the rebuild spec.
- ❌ Earth ARC or FamilieKompas ARC canonicals (which live in `Javalin13/ryzen-continuity/05-earth/` and `Javalin13/ryzen-continuity/06-familiekompas/`). This folder is *Fleet ARC's* view of coordination, not the other ARCs' views.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated).
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).
4. **Promotion rule:** An ARC-coordination-requirement discovery is *promoted* to the canonical multi-ARC convergence protocol (in `Javalin13/ryzen-continuity/02-ryzen/architecture/CONVERGENCE-LAYER.md`) only when the founder accepts the promotion. Per the continuity doctrine's "no new ARCs created unless 4 validation triggers met" rule applied to *cross-ARC* intelligence.

## File Naming Convention

```
YYYY-MM-DD-NN-<short-slug>.md
```

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Canonical convergence layer: `Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/CONVERGENCE-LAYER.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
- Earth canonical: `Javalin13/ryzen-continuity/blob/main/05-earth/EARTH-CANONICAL.md`
- FamilieKompas canonical: `Javalin13/ryzen-continuity/blob/main/06-familiekompas/FAMILIEKOMPAS-CANONICAL.md`
