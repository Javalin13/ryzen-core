# Ryzen Core — Runtime Roadmap

```yaml
---
type: runtime-roadmap
section: runtime-roadmap
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
related_rebuild_spec: Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md
amendable: true-additively
```

## Purpose

This document is the **runtime roadmap** for the `ryzen-core` repository. It maps the 4-phase rebuild sequence (from the canonical Rebuild Specification v1.0 in continuity) to *this* repository's structure. It is the *how* of the rebuild, scoped to *this* repository.

**The Rebuild Specification v1.0 is the source of truth for the rebuild plan.** This roadmap is a *navigation aid* for future maintainers and agents. When this roadmap disagrees with the rebuild spec, the rebuild spec wins.

## The 4-Phase Rebuild Sequence (this repository's perspective)

| Phase | Phase objective | Approximate duration | Status | This repository's contribution |
|---|---|---|---|---|
| **Phase 0** (this foundation) | Establish the durable implementation home + the accumulation layer | 1 day | **In progress (refined per ADR 0002)** | The 12-folder structure + 12+ integration files + 10 scaffolding READMEs + ADR 0001 + ADR 0002 (clarify posture) + 10 intake subdirectories |
| **R1** | Ryzen Core Kernel MVP | ~1 month | **Deferred (not imminent)** | `07-runtime-scaffolding/apps/*` + `07-runtime-scaffolding/packages/*` + `07-runtime-scaffolding/infrastructure/*` |
| **R2** | Production Governance Hardening | ~1 month | **Deferred (not imminent)** | R2 extends R1 scaffolding with Action Authorization Matrix + Risk Classification + governance observability |
| **R3** | Real Execution & Adaptive Cognition | ~3 months | **Deferred (not imminent)** | R3 adds real adapters + semantic memory + dashboards + security |
| **R4** | Multi-ARC Foundations | ~6 months | **Deferred (not imminent)** | R4 adds `apps/earth-arc/` + `apps/familiekompas-arc/` + cross-ARC federation protocol |

**Per the founder's clarification 2026-06-15 (ADR 0002), the runtime phase is *deferred* and *not imminent*.** The foundation's active deliverable is the **accumulation layer** (`11-fleet-arc-intake/`), not the runtime.

**Active deliverable (per ADR 0002):** The 10 intake subdirectories in `11-fleet-arc-intake/` accumulate validated Fleet ARC discoveries. The 6th cadence (`09-cadences/fleet-arc-intake/`) provides the intake template. The 5-state lifecycle (Raw → Validated → Accepted → Promoted → Deprecated) governs the accumulation.

**Total time-to-multi-ARC MVP: ~12 months** (after R1 is separately authorized by the founder). R1 is not on any current timeline.

## Phase 0 — This Foundation (current state, refined per ADR 0002)

**Objective:** Establish the durable implementation home **+ the accumulation layer**.

**Deliverables (committed this turn, refined per ADR 0002):**
- ✅ The 12-folder structure (37 directories, including `11-fleet-arc-intake/` and its 10 subdirectories)
- ✅ The foundation doctrine (`00-foundation/FOUNDATION.md`) — now with the **Strategic Posture** section per ADR 0002
- ✅ The 10 foundation governance rules (`00-foundation/GOVERNANCE.md`)
- ✅ The foundation interpretation protocol (`00-foundation/INTERPRETATION-PROTOCOL.md`)
- ✅ The 2 founder integration maps (`01-founder/FOUNDER-IDENTITY-MAP.md`, `01-founder/CAPABILITY-MAP.md`)
- ✅ The 2 ryzen integration maps (`02-ryzen/CANONICAL-RYZEN-MAP.md`, `02-ryzen/ARCHITECTURE-MAP.md`)
- ✅ The recovery integration map (`03-recovery-integration/RECOVERY-MAP.md`)
- ✅ The rebuild spec integration map (`04-rebuild-integration/RS-PHASES.md`)
- ✅ The ADR foundation (`05-adrs/TEMPLATE.md`, `05-adrs/INDEX.md`, `05-adrs/0001-establish-...md`, `05-adrs/0002-clarify-strategic-posture-...md`)
- ✅ The runtime roadmap (this document, `06-runtime-roadmap/ROADMAP.md`) — now with deferred status per ADR 0002
- ✅ The 7+ scaffolding placeholders in `07-runtime-scaffolding/` (each with a README that states "NOT IMPLEMENTED" and references the recovered concept + rebuild phase)
- ✅ The 5 operational cadence templates (`09-cadences/`) — including the new `09-cadences/fleet-arc-intake/` (6th cadence)
- ✅ The first tools folder (`10-tools/`)
- ✅ **[ADDITIVE — 2026-06-15, per ADR 0002]** The Fleet ARC Intake folder: `11-fleet-arc-intake/` with 10 subdirectories (parent README + 10 per-intake-type READMEs + INDEX log)
- ⏳ The runtime index (`00-foundation/CLASSIFICATION-INDEX.md`) — will be created as files are added

**Not deliverables (deferred):**
- ❌ The runtime itself (R1+)
- ❌ The recovery archive *content* (lives in continuity)
- ❌ The rebuild spec *content* (lives in continuity)
- ❌ The canonical doctrine *content* (lives in continuity)

**Success condition:** A local `ryzen-core` repository that is:
- Doctrine-aligned (consistent with the canonical Founder Identity, Capability Model, Interpretation Protocol)
- Recovery-informed (the 8 reusable concepts are mapped to scaffolding)
- Rebuild-aligned (the 4 phases are mapped to the runtime roadmap, *deferred* per ADR 0002)
- **Accumulation-active** (the 10 intake subdirectories are the canonical intake point for Fleet ARC discoveries)
- Additive (no existing canonical modified)
- Founder-authorized (the founder's direction is reflected in the design — including the strategic posture clarification)
- Token-hygienic (no credentials in any file)
- Ready for accumulation (the 3 open founder decisions are surfaced but do *not* block the accumulation phase)

## Phase R1 — Ryzen Core Kernel MVP (DEFERRED, not imminent)

**Objective:** Stand up the substrate. A working Ryzen Core Kernel MVP.

**Pre-conditions (must be met before R1 begins):**
1. ✅ Phase 0 (this foundation) is accepted.
2. ⏳ The founder resolves the 3 open decisions (D1, D2, D3) per `00-foundation/FOUNDATION.md` and the recovery archive's `OPEN-DECISIONS.md`.
3. ⏳ The founder separately authorizes R1 via a new ADR (e.g., ADR 0003: "Begin R1 — Ryzen Core Kernel MVP"). R1 is **NOT imminent** per the founder's clarification (ADR 0002).

**Deliverables (per the rebuild spec's §3.1):**
1. `07-runtime-scaffolding/infrastructure/docker/docker-compose.yml` — PostgreSQL+pgvector + Redis (recovered evidence in `ryzen-continuity/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` shows this was the original stack)
2. `07-runtime-scaffolding/packages/schemas/` — 7 SQLAlchemy ORM models (ARC, Brain, MemoryEntry, Task, Customer, Booking, ExecutionTrace)
3. `07-runtime-scaffolding/apps/governance/` — Governance Middleware (Concept C4)
4. `07-runtime-scaffolding/packages/verification/` — Recursive Verification Engine (Concept C3)
5. `07-runtime-scaffolding/apps/memory-federation/` — Memory Federation (Concept C2) with 4 layers + placeholder for semantic search
6. `07-runtime-scaffolding/apps/arc-factory/` — ARC Factory
7. `07-runtime-scaffolding/packages/brains/` — Brain contracts (BaseBrain + at least one concrete brain)
8. `07-runtime-scaffolding/packages/shared/` — Structured Logging (JSON with trace_id, arc_id, brain_id)
9. `07-runtime-scaffolding/packages/core/` — Cognition Loop (Concept C1), Structured Intent Parsing, Task Graph Engine (Concept C6)
10. `07-runtime-scaffolding/packages/core/adapters.py` — Adapter contract (ExecutionAdapter ABC + MockBookingAdapter)
11. `07-runtime-scaffolding/apps/fleet-arc/` — Fleet ARC orchestrator (Concept C5, 7 brains)
12. `07-runtime-scaffolding/apps/kernel-api/` — Kernel API (5 endpoints: /health, /kernel/execute, /arcs/create, /fleet/initialize, /fleet/request, /governance/audit)
13. `07-runtime-scaffolding/docs/` — 4 READMEs (architecture, canonical, governance, implementation)
14. `07-runtime-scaffolding/AGENTS.md` — agent directive for future AI implementers
15. Tests — 24+ tests, 40%+ test ratio, one test file per load-bearing pattern

**Success condition:** A local `ryzen-core` repository where:
- `pytest` passes
- The 7-brain Fleet ARC can be created via `POST /arcs/create` or `FleetARC.initialize(creator_id)`
- The canonical airport-pickup input can be processed via `POST /fleet/request` or `FleetARC.operational_request(text)`
- The output is a structured `{"status": "success", "trace_id": ..., "result": ...}` or `{"status": "governance_blocked", "reason": ...}`
- The Kernel API is reachable at `http://localhost:8000`
- No production deployment yet

## Phase R2 — Production Governance Hardening (DEFERRED, not imminent)

**Objective:** Make the kernel production-governed, not just MVP-governed.

**Pre-conditions:** R1 is complete and accepted (separately authorized by the founder).

**Deliverables (per the rebuild spec's §3.2):**
1. Action Authorization Matrix (Concept C7) — every brain, adapter, and engine declares CAN/CANNOT explicitly
2. Risk Classification (Concept C8) — every operational action is classified by risk level (LOW/MEDIUM/HIGH/CRITICAL)
3. Execution Constraints — recursion limits, duplicate workflow prevention, execution collision detection, rate limiting, safe degradation policies
4. Human Governance Interface — approval queues, workflow intervention, escalation dashboard backend
5. Operational Resilience — retry classification, rollback safety graphs, failure persistence, recovery escalation
6. `08-observability/` — governance observability (governance_events.py with trace_id, arc_id, brain_id, workflow_id, governance_state, risk_level)
7. API expansion — governance endpoints, resilience endpoints, operational governance queries
8. [CONDITIONAL] Feature branch discipline (if R-GOV-1 is promoted)
9. [CONDITIONAL] 8-question architecture review gate (if R-GOV-2 is promoted)

**Success condition:** A Fleet ARC that:
- Cannot perform CRITICAL actions without human approval
- Cannot perform duplicate actions
- Can be stopped/paused/rolled back by a human
- Produces a full governance audit trail for every action
- Survives operational failures gracefully

## Phase R3 — Real Execution & Adaptive Cognition (DEFERRED, not imminent)

**Objective:** Make the kernel execute *real* workflows and *adapt* based on operational patterns.

**Pre-conditions:** R2 is complete and accepted (separately authorized by the founder).

**Deliverables (per the rebuild spec's §3.3):**
1. Real Execution Infrastructure — booking engine, scheduling engine, notification engine, CRM integration, payment infrastructure (Stripe)
2. Real Tool Execution Layer — replace `MockBookingAdapter` with real adapters
3. Long-Horizon Memory — semantic retrieval with pgvector, customer continuity, operational continuity, strategic memory
4. Operational Dashboards — ARC health, governance, task graph visualization, fleet operations
5. Adaptive Cognition — workflow optimization, continuity optimization, cognitive efficiency (within bounded, deterministic, governed bounds)
6. Security & Access Control — JWT, RBAC, ARC permission isolation, secure execution boundaries, audit trails

**Success condition:** A real FleetConnect deployment, governed by Ryzen, with a measurable operational improvement over manual operation.

## Phase R4 — Multi-ARC & Civilization-Scale Foundations (DEFERRED, not imminent)

**Objective:** Prove the *multi-ARC* pattern by adding the next two first-generation ARCs.

**Pre-conditions:** R3 is complete and accepted (separately authorized by the founder).

**Deliverables (per the rebuild spec's §3.4):**
1. `07-runtime-scaffolding/apps/earth-arc/` — Earth ARC (with the 7+ brains appropriate for commerce intelligence)
2. `07-runtime-scaffolding/apps/familiekompas-arc/` — FamilieKompas ARC (with the 7+ brains appropriate for human-relational intelligence)
3. Cross-ARC Intelligence Convergence Protocol — the 4-tier authority hierarchy
4. Multi-ARC Federation Layer — the protocol for inter-ARC synchronization
5. Constitutional boundaries — each ARC's constitution, what it can do, what it cannot do, how it interacts with the other ARCs

**Success condition:** Three real ARCs (Fleet, Earth, FamilieKompas) operating under the same Ryzen kernel, each with its own topology and its own operational domain, with the protocols for cross-ARC intelligence convergence in place.

## The Roadmap's Relationship to the Doctrine

The 4-phase roadmap is a *deliberate* choice. The doctrine warns against:
- "70–85% probability of building a real advanced AI infrastructure company" *if* discipline is maintained
- The 7 execution risks (opportunity overload, scope expansion, context switching, premature ecosystem expansion, over-architecture, commercial delay, insufficient focus)
- Architecture drift: "Phase 3 is where architecture drift becomes dangerous"

The 4-phase roadmap is the *disciplined* response to these warnings:
- **R1** is the *substrate* — no intelligence, no execution, just the foundation
- **R2** is the *hardening* — production governance, no new features
- **R3** is the *execution* — real workflows, real adapters, real observability
- **R4** is the *expansion* — multi-ARC, but *foundations* only, not full ecosystem

Each phase is a *durable asset* that compounds. R1's substrate enables R2's hardening. R2's hardening enables R3's execution. R3's execution enables R4's expansion.

## What Comes Next (per ADR 0002 — Accumulation-First)

The next deliverable is **Phase 0 acceptance** (ADR 0001 + ADR 0002 are accepted by the founder). The deliverable after that is **accumulation begins** — Fleet ARC discoveries are validated, founder-accepted, and added to the appropriate subdirectory in `11-fleet-arc-intake/`.

The deliverable after that is the **runtime phase authorization** — a new ADR begins R1 (separately, when the founder decides). The 3 open founder decisions (D1, D2, D3) must be resolved *before* R1 begins.

**Until the founder explicitly authorizes the runtime phase, the foundation's active deliverable is accumulation, not implementation.** This is the doctrine of accumulation, codified in ADR 0002.

## The Doctrine of Accumulation (re-stated from ADR 0002)

1. **One canonical location per discovery type.** The 10 subdirectories in `11-fleet-arc-intake/` are the canonical locations.
2. **Founder acceptance is required for accumulation.** Raw and validated discoveries are *candidates*; accepted discoveries are *assets*.
3. **Additive only.** Intakes are never deleted, never overwritten. Deprecated intakes are preserved for continuity.
4. **Cross-ARC future-proofing.** The 10th intake type (`10-arc-coordination-requirements/`) captures Fleet ARC's intelligence about how it will interact with future ARCs.

The accumulation is the *present*; the runtime is the *future*.

## Cross-References

- `04-rebuild-integration/RS-PHASES.md` — the integration with the rebuild spec
- `03-recovery-integration/RECOVERY-MAP.md` — the integration with the recovery archive
- `05-adrs/0001-establish-ryzen-core-repository-foundation.md` — the foundation ADR
- Canonical Rebuild Specification: `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`
- Recovery Archive: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/`
