# Rebuild Spec Phase Map (this repository → canonical)

```yaml
---
type: rebuild-integration
section: rebuild-spec-phase-map
version: 1.0
status: foundation-only
created: 2026-06-15
classification: planning-artifact
canonical_ref: Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md
amendable: true-additively
```

## Purpose

This document is a **map** from this repository (`ryzen-core`) to the Rebuild Specification v1.0 in the `ryzen-continuity` repository. It captures *which rebuild phases* are relevant to this implementation-successor repository, and *how* this repository's structure serves the 4-phase rebuild sequence.

**The Rebuild Specification v1.0 is the source of truth for the rebuild plan.** This map is a *navigation aid*. When this map disagrees with the rebuild spec, the rebuild spec wins.

## The 4-Phase Rebuild Sequence (canonical)

The Rebuild Specification v1.0 defines a 4-phase rebuild sequence:

| Phase | Phase objective | Approximate duration | Status |
|---|---|---|---|
| **R1** | Ryzen Core Kernel MVP | ~1 month | Planned (not started) |
| **R2** | Production Governance Hardening | ~1 month | Planned (not started) |
| **R3** | Real Execution & Adaptive Cognition | ~3 months | Planned (not started) |
| **R4** | Multi-ARC & Civilization-Scale Foundations | ~6 months | Planned (not started) |

**Total time-to-multi-ARC MVP: ~12 months.** This is the *informed* estimate, not the *aggressive* one. The doctrine warns against rushing: "70–85% probability of building a real advanced AI infrastructure company" *if* discipline is maintained.

## How This Repository Serves the 4-Phase Rebuild Sequence

### R1 — Ryzen Core Kernel MVP (Phase 1, ~1 month)

**Phase objective:** Stand up the substrate. A working Ryzen Core Kernel MVP that implements the 5-stage Cognition Loop, the 4-layer Memory Federation, the 3-stage Recursive Verification, the 8-state Task Lifecycle, the 7-brain Fleet ARC topology, and the Governance Middleware.

**How this repository serves R1:**
- The 7-folder runtime scaffolding in `07-runtime-scaffolding/` is the *physical home* of R1's code.
- The 8 reusable concepts (C1–C6 in R1; C7–C8 in R2) are mapped to specific scaffolding directories.
- The 19-step build sequence (in the recovery archive) is the *what to build*; the rebuild spec is the *how*.
- The 3 open founder decisions (D1, D2, D3) must be *resolved* before R1 begins.

**R1 deliverables (per the rebuild spec):**
1. Repository structure (this foundation is the prerequisite)
2. Schemas (7 SQLAlchemy ORM models)
3. Governance Middleware (Concept C4)
4. Recursive Verification Engine (Concept C3)
5. Memory Federation (Concept C2) — with placeholder for semantic search
6. ARC Factory (creates ARC + brains from topology)
7. Brain contracts (BaseBrain + at least one concrete brain)
8. Structured Logging (JSON with trace_id, arc_id, brain_id)
9. Cognition Loop (Concept C1)
10. Structured Intent Parsing
11. Task Graph Engine (Concept C6, with the 5-node `schedule_booking` graph)
12. Adapter contract
13. Fleet ARC orchestrator (Concept C5, 7 brains)
14. Kernel API (5 endpoints)
15. Docker compose
16. Documentation
17. AGENTS.md
18. Tests (24+ tests, 40%+ test ratio)

**R1 success condition:** A local repository where `pytest` passes and the 7-brain Fleet ARC can be created and executed via the canonical airport-pickup input.

### R2 — Production Governance Hardening (Phase 2, ~1 month)

**Phase objective:** Make the kernel production-governed, not just MVP-governed. Implement the Action Authorization Matrix, Risk Classification, and (if founder promotes) the 2 recovered governance rules.

**How this repository serves R2:**
- The R2 deliverables are *added to* the R1 scaffolding, not new directories.
- The Action Authorization Matrix (Concept C7) is implemented in `07-runtime-scaffolding/apps/governance/` (extending the C4 Governance Middleware).
- The Risk Classification (Concept C8) is implemented in `07-runtime-scaffolding/apps/governance/`.
- The 2 recovered governance rules (R-GOV-1 feature branches, R-GOV-2 8-question review gate) are *optional* — they are NOT promoted to canonical. The founder must separately approve them via new ADRs.

**R2 deliverables (per the rebuild spec):**
1. Action Authorization Matrix (Concept C7)
2. Risk Classification (Concept C8)
3. Execution Constraints
4. Human Governance Interface
5. Operational Resilience
6. Governance Observability (extends `08-observability/`)
7. API expansion
8. [CONDITIONAL] Feature branch discipline (if R-GOV-1 is promoted)
9. [CONDITIONAL] 8-question architecture review gate (if R-GOV-2 is promoted)

**R2 success condition:** A Fleet ARC that cannot perform CRITICAL actions without human approval, cannot perform duplicate actions, can be stopped/paused/rolled back by a human, and produces a full governance audit trail.

### R3 — Real Execution & Adaptive Cognition (Phase 3, ~3 months)

**Phase objective:** Make the kernel execute *real* workflows and *adapt* based on operational patterns. Replace mock adapters with real ones. Implement semantic memory retrieval. Add dashboards and security.

**How this repository serves R3:**
- The R3 deliverables extend the R1 + R2 scaffolding with real adapters, real memory, and real observability.
- The real adapters live in `07-runtime-scaffolding/apps/fleet-arc/adapters/` (a new subdirectory created in R3).
- The semantic memory retrieval is implemented in `07-runtime-scaffolding/apps/memory-federation/` (replacing the placeholder from R1).
- The dashboards live in `08-observability/` (new subdirectories).
- The security layer lives in `07-runtime-scaffolding/apps/kernel-api/security/`.

**R3 deliverables (per the rebuild spec):**
1. Real Execution Infrastructure (booking, scheduling, notifications, CRM, payment)
2. Real Tool Execution Layer (real adapters for FleetConnect operations)
3. Long-Horizon Memory (semantic retrieval, customer continuity, operational continuity, strategic memory)
4. Operational Dashboards (extends `08-observability/`)
5. Adaptive Cognition (within bounded, deterministic, governed bounds)
6. Security & Access Control (JWT, RBAC, ARC permission isolation)

**R3 success condition:** A real FleetConnect deployment, governed by Ryzen, with a measurable operational improvement over manual operation.

### R4 — Multi-ARC & Civilization-Scale Foundations (Phase 4, ~6 months)

**Phase objective:** Prove the *multi-ARC* pattern by adding the next two first-generation ARCs (Earth and FamilieKompas). Establish the cross-ARC intelligence convergence protocols.

**How this repository serves R4:**
- The R4 deliverables are *new* sibling directories to `07-runtime-scaffolding/apps/fleet-arc/`.
- The Earth ARC lives in `07-runtime-scaffolding/apps/earth-arc/` (new).
- The FamilieKompas ARC lives in `07-runtime-scaffolding/apps/familiekompas-arc/` (new).
- The cross-ARC federation protocol is implemented as a new module (location TBD in R3 / R4 design).

**R4 deliverables (per the rebuild spec):**
1. Earth ARC (with the 7+ brains appropriate for commerce intelligence)
2. FamilieKompas ARC (with the 7+ brains appropriate for human-relational intelligence)
3. Cross-ARC Intelligence Convergence Protocol
4. Multi-ARC Federation Layer
5. Constitutional boundaries (each ARC's constitution)

**R4 success condition:** Three real ARCs (Fleet, Earth, FamilieKompas) operating under the same Ryzen kernel, each with its own topology and its own operational domain, with the protocols for cross-ARC intelligence convergence in place.

## The Foundation's Role in the 4-Phase Sequence

This foundation is **Phase 0** of the rebuild. It is the *prerequisite* for R1. It contains:

- The 10 foundation governance rules
- The 3 operational rules from the Interpretation Protocol
- The 5-tier classification discipline
- The 11-folder structure (the physical home for the runtime)
- The 7 foundation discipline READMEs in the scaffolding (the *what will go here* documentation)
- The 4 cadence templates (daily, weekly, monthly, lessons)
- The first ADR (the foundation establishment ADR)

**The foundation is not part of R1, R2, R3, or R4.** It is the *enabler* for R1. R1 begins *after* the foundation is committed and pushed.

## The 5 Non-Build Actions (per the rebuild spec)

The rebuild spec's §8.4 codifies 5 non-build actions. This foundation honors them all:

1. **Do not rebuild the 25-layer conceptual architecture in code.** The 25 layers are *strategic vision*. The runtime implements the *subset* (Layers 0–15) in R1–R4. ✅ Honored.
2. **Do not build the Nexus UI / visualization.** The runtime has a *Kernel API*; the visualization is a *consumer* of that API. ✅ Honored (no UI directories scaffolded).
3. **Do not build multi-ARC ecosystem in R1–R3.** R4 is the multi-ARC phase. ✅ Honored (Earth and FamilieKompas are NOT scaffolded at this stage).
4. **Do not build consciousness research, self-modification, or recursive self-spawning.** Explicitly forbidden by the doctrine. ✅ Honored.
5. **Do not build production auth, distributed runtime, or advanced optimization in R1–R2.** These are R3+ concerns. ✅ Honored (no auth/scaling directories scaffolded in R1/R2 scope).

## What This Map Does NOT Do

This map does **not**:

- ❌ Duplicate the rebuild spec. The spec is in continuity.
- ❌ Add new rebuild phases that are not in the spec.
- ❌ Resolve the 3 open founder decisions (D1, D2, D3) — those are the founder's decisions.
- ❌ Start R1. R1 begins only after the founder authorizes it and the 3 open decisions are resolved.

The map is **observational**, not **additive**. It maps; it does not extend.

## Cross-References

- `02-ryzen/CANONICAL-RYZEN-MAP.md` — the map to the canonical Ryzen definition
- `03-recovery-integration/RECOVERY-MAP.md` — the map to the recovery archive
- `06-runtime-roadmap/ROADMAP.md` — the runtime roadmap (this repo, with R1–R4 details)
- `07-runtime-scaffolding/*/README.md` — the per-directory scaffolding placeholders
- Canonical Rebuild Specification: `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`
