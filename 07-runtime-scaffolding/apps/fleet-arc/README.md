# apps/fleet-arc/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: C5 (7-brain Fleet ARC topology)
rebuild_phase: R1 (scaffolding) + R3 (real adapters)
blocked_by: D3 (ARC creation boundary — what to do with Earth and FamilieKompas)
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The Fleet ARC will be added in **R1** (the 7-brain topology + mock adapters) and extended in **R3** (real adapters).

## What will go here (in R1 and R3)

This directory will contain the **Fleet ARC** — the first real ARC, with the canonical 7-brain topology.

### R1 (Concept C5 — The 7-brain Fleet ARC topology)

In R1, this directory will contain:

- `orchestrator.py` — the `FleetARC` class with the `TOPOLOGY` constant
- `brains/` — the 7 brain instances (or, in the clean-slate rewrite, generic brains with role-specific configuration)
- `adapters/` — the mock adapters (`MockBookingAdapter`, etc.) — to be replaced in R3
- `__init__.py` — the package init
- `tests/test_orchestrator.py` — the test suite

The 7 brains are:

| # | Name | Role | Specialization |
|---|---|---|---|
| 1 | Executive Orchestrator | orchestration | Decision routing |
| 2 | Operations | execution | Process execution |
| 3 | Sales | growth | Revenue generation |
| 4 | Customer Continuity | retention | Relationship preservation |
| 5 | Analytics | intelligence | Insight generation |
| 6 | Governance | alignment | Verification |
| 7 | Memory Continuity | preservation | Federated memory |

The 7-brain topology is the *canonical first-ARC*. It is the seed for FleetConnect's business operations.

### R3 (Real Adapters)

In R3, this directory will *extend* with real adapters:

- `adapters/booking.py` — real booking engine (replace `MockBookingAdapter`)
- `adapters/scheduling.py` — real scheduling engine
- `adapters/notifications.py` — real notification engine (email, SMS, WhatsApp)
- `adapters/crm.py` — real CRM integration
- `adapters/payment.py` — real payment infrastructure (Stripe)

The R3 extensions are the *real execution* — they connect the Fleet ARC to the real FleetConnect business.

## The D3 Open Decision

The recovery archive's `OPEN-DECISIONS.md` codifies the **D3 — ARC Creation Boundary** decision. The 4 options:

| Option | Description | Pros | Cons |
|---|---|---|---|
| **No new ARCs** | Focus on Fleet ARC; Earth and FamilieKompas deferred | Discipline, focus | The 3 first-gen ARCs are *promised* but not *built* |
| **Build all 3 first-gen** | Add Earth and FamilieKompas in R4 | Aligns with the conceptual architecture's 3 first-gen ARCs | More work, more risk of drift |
| **Define 3 conceptually + build 1** | Define Earth and FamilieKompas *contracts* in R4, build only Fleet | Disciplined, prepares for the future | The 3 first-gen ARCs are *defined* but not *operational* |
| **Defer the decision** | Founder decides later | Maximum flexibility | The 3 first-gen ARCs are *promised* but the *operational reality* lags |

**Hermes's recommendation:** Option 3 — define the 3 first-gen ARCs conceptually in the rebuild spec, build only Fleet in the rebuild itself, and defer Earth and FamilieKompas to a separate rebuild (or to the actual FleetConnect business becoming operational).

**Decision required from founder:** Which option? Or: which *trade-offs* are acceptable?

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: Kernel runtime, Memory Federation, **ARC Runtime**, Governance Middleware, Agent Runtime at this stage.

The Fleet ARC is the *first real ARC*, part of the ARC Runtime substrate. The ARC Runtime is on the "do not implement" list. This scaffolding README is the *placeholder*, not the implementation.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` §"C5" — the 7-brain Fleet ARC topology
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/OPEN-DECISIONS.md` — the 3 open decisions (D1, D2, D3)
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" and §"R3" and §"R4" — the rebuild spec
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
