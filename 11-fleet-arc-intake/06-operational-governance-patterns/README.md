# 06 — Operational Governance Patterns (Fleet ARC Intake)

```yaml
---
type: intake
intake_type: operational-governance-patterns
status: active-as-intake-accumulator
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
```

## Purpose

This subdirectory is the **canonical intake location** for validated discoveries related to **Fleet ARC operational governance patterns**. It is *active as an intake accumulator* (it accepts new intake files) but *not implemented as a runtime component*.

## What belongs here

- Patterns, decisions, and learnings about *operational governance* in the Fleet ARC:
  - Validation gates (which actions require pre-execution validation, which don't)
  - Audit trails (which events are auditable, what fields are captured, retention period)
  - Escalation patterns (when to escalate, to whom, for what)
  - Risk classification (which actions are LOW/MEDIUM/HIGH/CRITICAL risk)
  - Constitutional patterns (the rules FleetConnect operates under; which rules were derived from operational reality)
  - Operational governance that emerges from real FleetConnect operations

## What does NOT belong here

- ❌ Governance code. The runtime is deferred; this folder holds *intake notes*, not code.
- ❌ The canonical governance (which lives in `Javalin13/ryzen-continuity/00-governance/`). This folder is *Fleet ARC's* governance intelligence — discoveries that *inform* the canonical governance, not duplicates of it.
- ❌ FleetConnect's own governance logic. The FleetConnect repo is the operational home; this folder is the *accumulation home*.

## The Intake Discipline

Every discovery in this directory follows:

1. The **intake template** at `09-cadences/fleet-arc-intake/TEMPLATE.md`.
2. The **5-state lifecycle** (Raw → Validated → Accepted → Promoted → Deprecated).
3. The **doctrine of accumulation** (one canonical location per discovery type, founder acceptance required, additive only).
4. **Promotion rule:** A governance-pattern discovery is *promoted* to the canonical governance (in `ryzen-continuity/00-governance/`) only when the founder explicitly accepts the promotion via a new ADR. Per the continuity doctrine's "recovery does not automatically imply adoption" rule applied to *new* governance patterns.

## File Naming Convention

```
YYYY-MM-DD-NN-<short-slug>.md
```

## Cross-References

- Parent folder: `11-fleet-arc-intake/README.md`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation governance (this repo): `00-foundation/GOVERNANCE.md`
- Canonical governance (continuity): `Javalin13/ryzen-continuity/blob/main/00-governance/GOVERNANCE.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
