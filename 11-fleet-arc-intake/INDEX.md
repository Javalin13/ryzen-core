# Fleet ARC Intake — Log (Index of Accepted Intakes)

```yaml
---
type: intake-log
status: foundation-only
created: 2026-06-15
classification: research-and-exploration
amendable: true-additively
related: 11-fleet-arc-intake/
```

## Purpose

This document is the **index of all accepted Fleet ARC intakes**. It tracks every intake that has been *validated*, *accepted*, *promoted*, or *deprecated* — with the date, the founder's acceptance, the cross-references, and the current status.

The log is **additive only**: new intakes are appended; deprecated intakes are not removed; promoted intakes retain their history.

## The Log

*No intakes recorded at the foundation stage. The first intake will be added when a Fleet ARC discovery is validated, founder-accepted, and accumulated into the appropriate subdirectory.*

## Template (per intake row)

```
YYYY-MM-DD — <short slug>
  Intake type: <one of 10 — see 11-fleet-arc-intake/README.md>
  Subdirectory: 11-fleet-arc-intake/0X-<intake-type>/
  File: 11-fleet-arc-intake/0X-<intake-type>/YYYY-MM-DD-NN-<short-slug>.md
  Status: raw | validated | accepted | promoted | deprecated
  Founder acceptance: <founder name, date, decision>
  Cross-references: <recovery archive, rebuild spec, runtime roadmap, foundation governance, etc.>
  One-line summary: <one sentence>
```

## Cross-References

- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake folder: `11-fleet-arc-intake/`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Strategic posture clarification: ADR `0002-clarify-strategic-posture-deferred-accumulation-first.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
