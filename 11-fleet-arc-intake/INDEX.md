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

The log is **additive only**: new intakes are appended; deprecated intakes are not removed; promoted intakes retain their history. The log now includes the **acceptance authority** (agent or founder) per intake, per the autonomous-acceptance doctrine (ADR 0003, [REVISED — 2026-06-15]).

## The Log

### 2026-06-15 — driver-assignment-by-proximity
  Intake type: `01-dispatch-intelligence`
  Subdirectory: `11-fleet-arc-intake/01-dispatch-intelligence/`
  File: `11-fleet-arc-intake/01-dispatch-intelligence/2026-06-15-01-driver-assignment-by-proximity.md`
  Status: **agent-accepted** (per ADR 0003, autonomous-acceptance doctrine)
  Agent acceptance: hermes (agent), 2026-06-15, agent-accepted
  Founder acceptance: null (not requested; the agent's acceptance is the default per ADR 0003)
  Founder override available: **yes** (the founder may deprecate, override, or promote at any time)
  Cross-references: recovery archive (C1, C5), rebuild spec (R3 §3.3), runtime roadmap (R3 deferred), foundation governance (Rule F-GOV-5)
  One-line summary: First agent-accepted Fleet ARC intake; inferred (not observed) baseline heuristic — proximity-default driver assignment with second-order filtering (capacity, rating, on-time). Seeded by the agent per ADR 0003. The founder may deprecate, override, or promote at any time.

## Template (per intake row)

```
YYYY-MM-DD — <short slug>
  Intake type: <one of 10 — see 11-fleet-arc-intake/README.md>
  Subdirectory: 11-fleet-arc-intake/0X-<intake-type>/
  File: 11-fleet-arc-intake/0X-<intake-type>/YYYY-MM-DD-NN-<short-slug>.md
  Status: raw | validated | accepted | promoted | deprecated
  Founder acceptance (deprecated criterion — see ADR 0003): <founder name, date, decision>
  Agent acceptance: hermes (agent), <date>, agent-accepted
  Founder override available: yes (the founder may deprecate, override, or promote this intake at any time)
  Cross-references: <recovery archive, rebuild spec, runtime roadmap, foundation governance, etc.>
  One-line summary: <one sentence>
```

## Cross-References

- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake folder: `11-fleet-arc-intake/`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Strategic posture clarification: ADR `0002-clarify-strategic-posture-deferred-accumulation-first.md`
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
