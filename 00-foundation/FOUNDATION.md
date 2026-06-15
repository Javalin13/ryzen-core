# Ryzen Core Foundation — The Foundation Doctrine

```yaml
---
type: foundation
section: foundation-doctrine
version: 1.0
status: foundation-only
created: 2026-06-15
doctrine_layer: this is the implementation successor; ryzen-continuity is the canonical doctrine
classification: approved-architecture
amendable: true-additively
related_repo: Javalin13/ryzen-continuity
related_artifact: 2. Implementation-20260615T111401Z-3-001.zip
replaced_runtime: original Ryzen implementation repository (lost)
```

## Purpose

This document is the **foundation doctrine** for the `ryzen-core` repository. It establishes what this repository is, what it is not, and the constitutional constraints that govern every change to this repository.

This is **not** the canonical doctrine. The canonical doctrine lives in `Javalin13/ryzen-continuity` at:

- `01-founder/CANONICAL-FOUNDER-IDENTITY.md` — Founder Identity Profile v1.0
- `01-founder/CANONICAL-FOUNDER-CAPABILITY-MODEL.md` — Founder Capability Model v1.0
- `00-governance/INTERPRETATION-PROTOCOL.md` — Interpretation & Reality Anchoring Protocol v1.0
- `00-governance/GOVERNANCE.md` — the governance doctrine

This document is **a map to those canonicals, not the canonicals themselves.** The continuity repository is the source of truth. When the two repositories disagree, the continuity repository wins.

## The 10 Foundation Principles (mapped to the 8 continuity doctrine rules)

The continuity repo's `00-governance/GOVERNANCE.md` §3 codifies 8 doctrine rules. This foundation re-states them as 10 foundation principles, with the mapping to the continuity canonical explicit.

| # | Foundation principle | Continuity doctrine rule | Source |
|---|---|---|---|
| 1 | **Doctrine-continuity alignment.** This repository references the canonical doctrine; it does not duplicate it. | Rule 1: Additive-only evolution | `00-governance/GOVERNANCE.md` §3 |
| 2 | **Recovery-informed scaffolding.** Every empty directory in `07-runtime-scaffolding/` references the recovered concept(s) it will eventually implement. | Rule 1: Additive-only evolution | `00-governance/GOVERNANCE.md` §3 |
| 3 | **No implementation at this stage.** The runtime is *not* built in this foundation. | Rule 2: Continuity before scaling | `00-governance/GOVERNANCE.md` §3 |
| 4 | **Additive evolution.** Every change is additive, never destructive. | Rule 1: Additive-only evolution | `00-governance/GOVERNANCE.md` §3 |
| 5 | **Founder authority preserved.** Every change requires founder direction. | Rule 4: Founder authority | `00-governance/GOVERNANCE.md` §3 |
| 6 | **Interpretation Protocol in force.** Every claim is classified against the 5-tier reality hierarchy. | Rule 6: Interpretation Protocol | `00-governance/GOVERNANCE.md` §3 |
| 7 | **Token hygiene.** No credentials in the repository. | Rule 5: Operational realism | `00-governance/GOVERNANCE.md` §3 |
| 8 | **Naming discipline.** Files use kebab-case (per `AGENTS.md` pattern in continuity); folders use `NN-purpose` (zero-padded two-digit prefix). | Rule 7: Naming & structure | `00-governance/GOVERNANCE.md` §3 |
| 9 | **Tagging discipline.** Canonical and decision-accepted tags follow the pattern `canonical-<name>-v<major>.<minor>` and `decision-<NNNN>-accepted`. | Rule 8: Tagging | `00-governance/GOVERNANCE.md` §3 |
| 10 | **Commit discipline.** One artifact class per commit; clear, scoped, atomic. | Rule 3: Commit doctrine | `00-governance/GOVERNANCE.md` §3 |

## The 7 Execution Risks (from the Founder Capability Model)

The continuity repo's `01-founder/CANONICAL-FOUNDER-CAPABILITY-MODEL.md` codifies 7 execution risks. This foundation applies them as 7 foundation guards:

| # | Risk | Foundation guard |
|---|---|---|
| 1 | Opportunity overload | The scope is fixed by the founder direction. No new opportunities added. |
| 2 | Scope expansion | The "do not implement" list (Kernel runtime, Memory Federation, ARC Runtime, Governance Middleware, Agent Runtime) is a hard boundary. |
| 3 | Context switching | The 11-folder structure is the focus. The cadence templates are the rhythm. |
| 4 | Premature ecosystem expansion | The foundation is for Ryzen Core only. No ARCs, no multi-ARC, no ecosystem. |
| 5 | Over-architecture | The scaffolding is *minimal*. Each directory has a single purpose. Each placeholder README is concise. |
| 6 | Commercial delay | The foundation is the prerequisite for R3 (real execution). The foundation enables commercial delivery; it does not delay it. |
| 7 | Insufficient focus | The 4-phase rebuild sequence (in `06-runtime-roadmap/`) is the focus. The 11-folder structure serves the 4 phases. |

## The 3 Founder Decisions (from the recovery archive)

The recovery archive in `ryzen-continuity/04-recovery-archive/OPEN-DECISIONS.md` codifies 3 founder decisions required to start R1:

| # | Decision | Status | Foundation action |
|---|---|---|---|
| 1 | **D1 — Real brain implementation strategy** | Open | Documented in `07-runtime-scaffolding/packages/brains/README.md` as a placeholder until the founder decides. |
| 2 | **D2 — Semantic memory implementation** | Open | Documented in `07-runtime-scaffolding/apps/memory-federation/README.md` as a placeholder until the founder decides. |
| 3 | **D3 — ARC creation boundary** | Open | Documented in `07-runtime-scaffolding/apps/fleet-arc/README.md` as a placeholder until the founder decides. |

The 3 open decisions are **in this foundation by design**. They are *the* blockers for R1; the foundation is the prerequisite for R1; therefore the foundation must surface the 3 decisions to the founder. **No silent decisions.**

## The 8 Reusable Concepts (mapped to the scaffolding)

The recovery archive's `RECOVERED-REUSABLE-CONCEPTS.md` codifies 8 reusable concepts. This foundation maps each concept to the scaffolding directory that will eventually implement it.

| # | Concept (C#) | Recovery archive reference | Scaffolding directory |
|---|---|---|---|
| 1 | **C1 — The 5-stage Cognition Loop pattern** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | `07-runtime-scaffolding/packages/core/` |
| 2 | **C2 — The 4-layer Memory Model** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | `07-runtime-scaffolding/apps/memory-federation/` |
| 3 | **C3 — The 3-stage Recursive Verification pattern** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | `07-runtime-scaffolding/packages/verification/` |
| 4 | **C4 — The Governance Middleware pattern** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | `07-runtime-scaffolding/apps/governance/` |
| 5 | **C5 — The 7-brain Fleet ARC topology** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | `07-runtime-scaffolding/apps/fleet-arc/` |
| 6 | **C6 — The 8-state Task Lifecycle** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | `07-runtime-scaffolding/packages/core/` |
| 7 | **C7 — The Action Authorization Matrix pattern** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | (R2 — not yet scaffolded) |
| 8 | **C8 — The Risk Classification pattern** | `04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` | (R2 — not yet scaffolded) |

## The 4-Phase Rebuild Sequence (mapped to the roadmap)

The continuity repo's `RYZEN-REBUILD-SPECIFICATION-v1.0.md` codifies the 4-phase rebuild sequence. This foundation maps each phase to the scaffolding layer that will be built in that phase.

| Phase | Phase objective | Foundation scaffolding |
|---|---|---|
| **R1** | Ryzen Core Kernel MVP | `07-runtime-scaffolding/` (all apps + packages + infrastructure) |
| **R2** | Production Governance Hardening | (R2 — adds Action Authorization Matrix + Risk Classification + governance observability to the R1 scaffolding) |
| **R3** | Real Execution & Adaptive Cognition | (R3 — adds real adapters to `apps/fleet-arc/`, real bookings/scheduling to `apps/fleet-arc/`, semantic memory to `apps/memory-federation/`, dashboards to `08-observability/`) |
| **R4** | Multi-ARC Foundations | (R4 — adds `apps/earth-arc/` and `apps/familiekompas-arc/` as siblings to `apps/fleet-arc/`, plus the cross-ARC federation protocol) |

The 4-phase roadmap is detailed in `06-runtime-roadmap/ROADMAP.md`. The runtime roadmap integration is in `04-rebuild-integration/RS-PHASES.md`.

## The 11-Folder Structure (one-line per folder)

| # | Folder | One-line role |
|---|---|---|
| 1 | `00-foundation/` | The foundation doctrine (this document + GOVERNANCE.md + INTERPRETATION-PROTOCOL.md) |
| 2 | `01-founder/` | Maps to the canonical Founder Identity and Capability Model |
| 3 | `02-ryzen/` | Maps to the canonical Ryzen definition and architecture |
| 4 | `03-recovery-integration/` | Integration points for the recovery archive |
| 5 | `04-rebuild-integration/` | Integration of the Rebuild Specification v1.0 |
| 6 | `05-adrs/` | Architectural Decision Records for this repository |
| 7 | `06-runtime-roadmap/` | The runtime roadmap for this repository |
| 8 | `07-runtime-scaffolding/` | Future implementation directories (scaffolded, not implemented) |
| 9 | `08-observability/` | Future observability stack (scaffolded, not implemented) |
| 10 | `09-cadences/` | Daily/weekly/monthly templates + lessons learned + idea backlog |
| 11 | `10-tools/` | Scripts and utilities |

## The Doctrine of Implementation Scaffolding

This foundation introduces a pattern that should be applied to every future addition: **"scaffolded, not implemented."** Every directory in `07-runtime-scaffolding/` and `08-observability/` has a `README.md` that:

1. **Names the recovered concept(s)** the directory will eventually implement.
2. **Names the rebuild phase(s)** in which the directory will be built.
3. **States "NOT IMPLEMENTED"** explicitly, so future maintainers (and agents) know the directory is *scaffolded, not built*.
4. **References the canonical source** of the design (recovery archive, rebuild specification, continuity doctrine).

This pattern is itself a doctrine: **empty directories are honest when they are explicitly empty for a reason.** A future maintainer who encounters `07-runtime-scaffolding/apps/memory-federation/` with a `README.md` saying "NOT IMPLEMENTED — implements C2 (4-layer Memory Model) in R1" knows exactly what to do.

## The Doctrine of Integration

The 11-folder structure is not arbitrary. The folders 0X, 1X, 2X, 3X, 4X, 5X, 6X correspond to the **integration layers**:

- 0X: Self-integration (this repo's own foundation doctrine)
- 1X: Founder integration (maps to continuity's canonical founder docs)
- 2X: Ryzen integration (maps to continuity's canonical Ryzen docs)
- 3X: Recovery integration (maps to continuity's recovery archive)
- 4X: Rebuild integration (maps to continuity's rebuild spec)
- 5X: ADR (this repo's own decision records)

The folders 7X, 8X, 9X, 10X correspond to the **operational layers**:

- 7X: Runtime scaffolding (where the future code will live)
- 8X: Observability (where the future observability stack will live)
- 9X: Cadences (the daily/weekly/monthly rhythm)
- 10X: Tools (the scripts that make this repo work)

This 0X-1X-2X-3X-4X-5X-6X-7X-8X-9X-10X pattern is the **integration then operation** pattern. Foundation first, integration second, operation third.

## What Comes Next

Per the founder's direction, this is **foundation only**. The next deliverables (after founder authorization) will be:

1. **Phase R1** — stand up the substrate in `07-runtime-scaffolding/` per the rebuild spec.
2. **Phase R2** — production governance hardening per the rebuild spec.
3. **Phase R3** — real execution & adaptive cognition per the rebuild spec.
4. **Phase R4** — multi-ARC foundations per the rebuild spec.

**No implementation begins today.** The foundation is the prerequisite. The foundation is doctrine-aligned. The foundation is the durable home. The runtime is the future.

## Cross-References

- `00-foundation/GOVERNANCE.md` — the foundation governance rules
- `00-foundation/INTERPRETATION-PROTOCOL.md` — the foundation interpretation protocol
- `01-founder/FOUNDER-IDENTITY-MAP.md` — map to the canonical Founder Identity
- `01-founder/CAPABILITY-MAP.md` — map to the canonical Capability Model
- `02-ryzen/CANONICAL-RYZEN-MAP.md` — map to the canonical Ryzen definition
- `02-ryzen/ARCHITECTURE-MAP.md` — map to the canonical architecture
- `03-recovery-integration/RECOVERY-MAP.md` — map to the recovery archive
- `04-rebuild-integration/RS-PHASES.md` — map to the rebuild spec's 4 phases
- `05-adrs/` — Architectural Decision Records (this repo)
- `06-runtime-roadmap/ROADMAP.md` — the runtime roadmap
- `07-runtime-scaffolding/*/README.md` — the per-directory scaffolding placeholders

## The Founder Direction (verbatim, 2026-06-15)

> The original Ryzen runtime repository is lost. The continuity repository remains canonical. A new Ryzen Core Repository Foundation is authorized. Purpose: Provide the durable implementation home for future Ryzen runtime development. Scope: Repository structure, Governance integration, Recovery archive integration, Rebuild specification integration, ADR integration, Runtime roadmap integration, Implementation scaffolding only. Do not implement: Kernel runtime, Memory Federation, ARC Runtime, Governance Middleware, Agent Runtime at this stage. Create only the foundational repository structure necessary to support future implementation. The repository should serve as the implementation successor to the lost runtime repository while remaining aligned with: Founder Identity, Capability Model, Interpretation Protocol, Recovery Archive, Rebuild Specification. The objective is continuity and future implementation readiness. Not runtime delivery.
