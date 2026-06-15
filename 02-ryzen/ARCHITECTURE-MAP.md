# Architecture Map (this repository → canonical)

```yaml
---
type: ryzen-integration
section: architecture-map
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
canonical_refs:
  - Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/HIERARCHY.md
  - Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/CONVERGENCE-LAYER.md
  - Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/GOVERNANCE-FRAMEWORK.md
amendable: true-additively
```

## Purpose

This document is a **map** from this repository (`ryzen-core`) to the canonical Ryzen architecture in the `ryzen-continuity` repository. It captures *which canonical architecture facts* are relevant to this implementation-successor repository, and *how* this repository honors them.

**The canonical architecture (HIERARCHY, CONVERGENCE-LAYER, GOVERNANCE-FRAMEWORK) is the source of truth.** This map is a *navigation aid*. When this map disagrees with the canonical, the canonical wins.

## The 5-Tier Hierarchy (canonical HIERARCHY.md)

The canonical `HIERARCHY.md` codifies a 5-tier hierarchy:

1. **Creator (founder)** — the top of the hierarchy; the will that drives everything.
2. **Ryzen** — the recursively governed, continuity-driven system.
3. **ARCs** — the operational units (FleetConnect, Earth, FamilieKompas).
4. **Brains** — the cognitive units within ARCs (Sales, Operations, Pricing, etc.).
5. **Agents** — the execution units within Brains.
6. **Execution** — the bottom of the hierarchy; the work that actually gets done.

**How this repository honors the hierarchy:**
- This repository sits at **Tier 2 (Ryzen)** in the hierarchy. It is the system, not the creator, not an ARC, not a Brain, not an Agent.
- The runtime in `07-runtime-scaffolding/` will *generate* ARCs (Tier 3) via the ARC Factory.
- The runtime will *instantiate* Brains (Tier 4) via the Brain contracts.
- The runtime will *execute* Agent operations (Tier 5) via the Adapter pattern.

## The Convergence Layer (canonical CONVERGENCE-LAYER.md)

The canonical `CONVERGENCE-LAYER.md` codifies the *convergence points* where multiple subsystems interact. The convergence layer is the *coordination* substrate, not the *execution* substrate.

**The 5 convergence points:**

1. **Governance ↔ Execution** — every action passes through governance validation.
2. **Memory ↔ Cognition** — cognition retrieves context from memory and persists results to memory.
3. **Verification ↔ Orchestration** — every orchestrated step passes through recursive verification.
4. **ARC ↔ ARC** — multi-ARC convergence (R4).
5. **Founder ↔ System** — the founder's intent enters the system via the Creator layer.

**How this repository honors the convergence layer:**
- The 11-folder structure is the *coordination substrate*: each folder is a convergence point with the runtime.
- The 4-phase rebuild sequence is the *convergence evolution*: R1 establishes the first 3 convergence points; R2 adds the governance hardening; R3 adds the execution substrate; R4 adds the multi-ARC convergence.
- The 5 convergence points are *not* implemented in the foundation. They will be *implemented* as the runtime is built in R1+.

## The Governance Framework (canonical GOVERNANCE-FRAMEWORK.md)

The canonical `GOVERNANCE-FRAMEWORK.md` codifies the governance architecture: the rules, the validation gates, the audit trail, the escalation paths.

**The 4 governance layers:**

1. **Constitutional layer** — the doctrine (Founder Identity, Capability Model, Interpretation Protocol). Non-negotiable.
2. **Operational layer** — the governance rules applied at runtime (the 10 foundation governance rules in this repo's `00-foundation/GOVERNANCE.md`).
3. **Enforcement layer** — the runtime mechanisms that enforce the rules (governance middleware in `07-runtime-scaffolding/apps/governance/`, action authorization matrix in R2, risk classification in R2).
4. **Audit layer** — the immutable audit trail of every governance decision.

**How this repository honors the governance framework:**
- The foundation governance rules in `00-foundation/GOVERNANCE.md` are the **operational layer** for this repository.
- The constitutional layer is the *continuity repo's* canonicals (Founder Identity, Capability Model, Interpretation Protocol).
- The enforcement layer will be implemented in R1 (governance middleware) and R2 (action authorization, risk classification).
- The audit layer will be implemented in R2 (governance observability) and R3 (production observability stack).

## The 8 Reusable Concepts (from the recovery archive, mapped to the architecture)

The recovery archive's 8 reusable concepts are *architecture concepts*. This repository maps each concept to the architectural layer it will be implemented in:

| # | Concept | Architecture layer | Scaffolding directory |
|---|---|---|---|
| 1 | **C1 — The 5-stage Cognition Loop pattern** | Tier 2 (Ryzen) | `07-runtime-scaffolding/packages/core/` |
| 2 | **C2 — The 4-layer Memory Model** | Tier 2 (Ryzen) | `07-runtime-scaffolding/apps/memory-federation/` |
| 3 | **C3 — The 3-stage Recursive Verification pattern** | Tier 2 (Ryzen) | `07-runtime-scaffolding/packages/verification/` |
| 4 | **C4 — The Governance Middleware pattern** | Tier 3 (Convergence: Governance ↔ Execution) | `07-runtime-scaffolding/apps/governance/` |
| 5 | **C5 — The 7-brain Fleet ARC topology** | Tier 3 (ARC) | `07-runtime-scaffolding/apps/fleet-arc/` |
| 6 | **C6 — The 8-state Task Lifecycle** | Tier 2 (Ryzen) | `07-runtime-scaffolding/packages/core/` |
| 7 | **C7 — The Action Authorization Matrix pattern** | Tier 3 (Convergence: Governance ↔ Execution) | (R2 — not yet scaffolded) |
| 8 | **C8 — The Risk Classification pattern** | Tier 3 (Convergence: Governance ↔ Execution) | (R2 — not yet scaffolded) |

## The 25-Layer Conceptual Architecture (from the canonical)

The canonical `02-ryzen/architecture/` directory references a 25-layer conceptual architecture (Layers 0–25). These layers are *strategic vision*, not *implementation*. The 25 layers cover:

- **Layer 0**: Identity persistence
- **Layer 1**: Orchestration substrate
- **Layer 2**: Governance middleware
- **Layer 3**: Recursive verification
- **Layer 4**: ARC registry
- **Layer 5**: Memory continuity
- **Layer 6–10**: Cognition, intent parsing, task graph, brain contracts, structured logging
- **Layer 11–15**: ARC generation, Fleet ARC, kernel API, observability, observability events
- **Layer 16–20**: Multi-ARC convergence, cross-ARC intelligence, ARC interoperability, ARC creation governance, ARC synchronization
- **Layer 21–25**: Operational resilience, execution quality, ecosystem maturity, civilization-scale, ultimate convergence

**How this repository honors the 25-layer architecture:**
- The 25 layers are *not* implemented in this foundation. They are *strategic vision* in the canonical.
- The R1–R4 rebuild sequence implements a *subset* of the 25 layers (approximately Layers 0–15).
- The R4+ multi-ARC foundations begin Layers 16–20.
- Layers 21–25 are *post-rebuild* (Year 3+ of the master plan).

## What This Map Does NOT Do

This map does **not**:

- ❌ Duplicate the canonical architecture. The canonical is in continuity.
- ❌ Add new architecture layers, convergence points, or governance layers that are not in the canonical.
- ❌ Promote the 25-layer architecture from "Strategic Vision" to "Active Execution" without an explicit founder decision and an ADR in continuity.
- ❌ Re-classify the recovery archive, the rebuild spec, or the original runtime.

The map is **observational**, not **additive**. It maps; it does not extend.

## Cross-References

- `02-ryzen/CANONICAL-RYZEN-MAP.md` — the sibling map to the canonical Ryzen definition
- `03-recovery-integration/RECOVERY-MAP.md` — the map to the recovery archive
- `04-rebuild-integration/RS-PHASES.md` — the map to the rebuild spec
- `06-runtime-roadmap/ROADMAP.md` — the runtime roadmap (this repo)
- `07-runtime-scaffolding/*/README.md` — the per-directory scaffolding placeholders
- Canonical architecture: `Javalin13/ryzen-continuity/blob/main/02-ryzen/architecture/HIERARCHY.md`, `CONVERGENCE-LAYER.md`, `GOVERNANCE-FRAMEWORK.md`
