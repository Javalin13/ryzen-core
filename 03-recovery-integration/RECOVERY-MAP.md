# Recovery Archive Map (this repository → canonical)

```yaml
---
type: recovery-integration
section: recovery-archive-map
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture-with-historical-evidence
canonical_ref: Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERY-INDEX.md
related_artifact: 2. Implementation-20260615T111401Z-3-001.zip
amendable: true-additively
```

## Purpose

This document is a **map** from this repository (`ryzen-core`) to the Recovery Archive in the `ryzen-continuity` repository. It captures *which recovered knowledge* is relevant to this implementation-successor repository, and *how* this repository honors it.

**The Recovery Archive is the source of truth for the lost original runtime's recovered knowledge.** This map is a *navigation aid*. When this map disagrees with the recovery archive, the recovery archive wins.

## The Recovery Archive (canonical, 11 files)

The recovery archive in `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/` contains 11 files:

1. `RECOVERY-INDEX.md` — entry point + constitutional constraints
2. `RECOVERED-PACKAGE-INVENTORY.md` — 49 files in the recovered ZIP
3. `RECOVERED-CODE-INVENTORY.md` — 33 code files inventoried
4. `RECOVERED-DESIGN-DECISIONS.md` — 5 durable, 5 deferred, 3 rejected
5. `RECOVERED-IMPLEMENTATION-SEQUENCE.md` — 19-step build order
6. `RECOVERED-REUSABLE-CONCEPTS.md` — 8 reusable concepts
7. `RECOVERED-LESSONS.md` — 7 lessons from the build
8. `RECOVERED-GOVERNANCE-RULES.md` — 2 rules, NOT promoted to canonical
9. `LOST-ARTIFACTS.md` — 8 categories that do NOT survive
10. `OPEN-DECISIONS.md` — 3 founder decisions required for R1
11. `RECOVERY-ASSESSMENT-REPORT-v1.0.md` — the integrated assessment (canonical archive document)

**How this repository uses the recovery archive:** As the *design reference* for the runtime that will be built in R1–R4. The recovery archive is the *what to build*; the rebuild spec (in continuity) is the *how to build it*; this repository is the *where to build it*.

## The 8 Reusable Concepts (mapped to the scaffolding)

The recovery archive's 8 reusable concepts are the *load-bearing design patterns* for the future runtime. This repository maps each concept to the scaffolding directory that will eventually implement it:

| # | Concept | Canonical reference | Scaffolding directory | Rebuild phase |
|---|---|---|---|---|
| 1 | **C1 — The 5-stage Cognition Loop pattern** | `RECOVERED-REUSABLE-CONCEPTS.md` §1 | `07-runtime-scaffolding/packages/core/` | R1 |
| 2 | **C2 — The 4-layer Memory Model** | `RECOVERED-REUSABLE-CONCEPTS.md` §2 | `07-runtime-scaffolding/apps/memory-federation/` | R1 |
| 3 | **C3 — The 3-stage Recursive Verification pattern** | `RECOVERED-REUSABLE-CONCEPTS.md` §3 | `07-runtime-scaffolding/packages/verification/` | R1 |
| 4 | **C4 — The Governance Middleware pattern** | `RECOVERED-REUSABLE-CONCEPTS.md` §4 | `07-runtime-scaffolding/apps/governance/` | R1 |
| 5 | **C5 — The 7-brain Fleet ARC topology** | `RECOVERED-REUSABLE-CONCEPTS.md` §5 | `07-runtime-scaffolding/apps/fleet-arc/` | R1 |
| 6 | **C6 — The 8-state Task Lifecycle** | `RECOVERED-REUSABLE-CONCEPTS.md` §6 | `07-runtime-scaffolding/packages/core/` | R1 |
| 7 | **C7 — The Action Authorization Matrix pattern** | `RECOVERED-REUSABLE-CONCEPTS.md` §7 | (R2 — not yet scaffolded) | R2 |
| 8 | **C8 — The Risk Classification pattern** | `RECOVERED-REUSABLE-CONCEPTS.md` §8 | (R2 — not yet scaffolded) | R2 |

## The 5 Design Decisions (relevant subset)

The recovery archive's 5 design decisions that *survive* the loss (and are not deferred or rejected):

| # | Design decision | Scaffolding impact |
|---|---|---|
| 1 | **Modular Python monorepo with `apps/` and `packages/` split** | The `07-runtime-scaffolding/apps/` and `07-runtime-scaffolding/packages/` directories are the physical embodiment of this decision. |
| 2 | **FastAPI + SQLAlchemy + PostgreSQL/pgvector + Redis** | The runtime stack. (Not yet implemented in this foundation; will be specified in R1 ADRs.) |
| 3 | **The 5-stage Cognition Loop pattern** | Already mapped to `packages/core/` (C1). |
| 4 | **The 4-layer Memory Model** | Already mapped to `apps/memory-federation/` (C2). |
| 5 | **The 7-brain Fleet ARC topology** | Already mapped to `apps/fleet-arc/` (C5). |

## The 7 Lessons (operationalized as foundation disciplines)

The recovery archive's 7 lessons are the *operational guidance* for the future build. This repository operationalizes each lesson as a foundation discipline:

| # | Lesson | Foundation discipline |
|---|---|---|
| 1 | **The most dangerous stage is the transition from infrastructure to intelligence** | The foundation is *infrastructure only* — no intelligence (no runtime, no cognition, no execution). R1 begins the intelligence build, with discipline. |
| 2 | **Governance must be embedded in the execution substrate, not bolted on** | The foundation governance is the *first* layer. The runtime will follow the same pattern. |
| 3 | **Tests are how infrastructure projects survive their own complexity** | The 4-phase rebuild sequence mandates 40%+ test ratio. The foundation placeholders reference this. |
| 4 | **Architectural discipline is more important than architectural completeness** | The 11-folder structure is *disciplined*, not *complete*. The foundation is the discipline. |
| 5 | **Use feature branches from the threshold where architecture integrity matters** | The rebuild spec references this. (The 2 recovered governance rules in the archive are NOT promoted to canonical; they are *candidates* for separate review.) |
| 6 | **Architecture drift is the silent killer of ambitious systems** | The Interpretation Protocol's 5-tier classification is the *drift detector*. The runtime index is the *drift evidence*. |
| 7 | **A coherent architecture at MVP depth is more valuable than a complete architecture at any depth** | R1 produces a *coherent MVP* (substrate + cognition + first ARC). R2–R4 *harden* it. The foundation is the *coherent* part of the MVP. |

## The 8 Lost Artifacts (acknowledged in the scaffolding)

The recovery archive's 8 lost artifacts are what the original runtime *had* but this foundation does *not* have. This repository acknowledges them in the scaffolding placeholders:

| # | Lost artifact | Foundation acknowledgement |
|---|---|---|
| 1 | **The working Ryzen Core Kernel Runtime** | The runtime is *scaffolded* in `07-runtime-scaffolding/`. It is not running. It is not deployed. It is not implemented. |
| 2 | **Production Deployment Infrastructure** | Deferred to R3+. |
| 3 | **Real Brain Implementations** | Acknowledged in `07-runtime-scaffolding/packages/brains/README.md` (the 3 open founder decisions, including D1). |
| 4 | **Real Tool Integrations** | Deferred to R3. |
| 5 | **Long-Horizon Memory Retrieval** | Acknowledged in `07-runtime-scaffolding/apps/memory-federation/README.md` (D2). |
| 6 | **Multi-ARC Ecosystem** | Deferred to R4+. |
| 7 | **Production Observability Stack** | Deferred to R3. |
| 8 | **Real Customer Data, Bookings, Operational History** | Acknowledged as a *post-foundation* concern; R3 will acquire real data as part of the FleetConnect business. |

## The 3 Open Founder Decisions (the blockers for R1)

The recovery archive's 3 open founder decisions are *the* blockers for R1. This foundation surfaces them in 3 scaffolding READMEs:

- **D1 — Real brain implementation strategy** → `07-runtime-scaffolding/packages/brains/README.md`
- **D2 — Semantic memory implementation** → `07-runtime-scaffolding/apps/memory-federation/README.md`
- **D3 — ARC creation boundary** → `07-runtime-scaffolding/apps/fleet-arc/README.md`

When the founder makes these 3 decisions, R1 can begin. Until then, the foundation is the *prerequisite* for R1.

## The 2 Recovered Governance Rules (NOT promoted)

The recovery archive's 2 recovered governance rules (R-GOV-1 feature branches, R-GOV-2 8-question review gate) are *documented and preserved* in the archive, but **NOT promoted to canonical governance** in the continuity repo's `00-governance/GOVERNANCE.md`. Per the founder's direction: "Recovery does not automatically imply adoption."

**How this repository honors the non-promotion:** This foundation's `00-foundation/GOVERNANCE.md` does *not* include the 2 recovered rules. The rules are *referenced* in the rebuild spec as a *recommended discipline* (conditional on founder promotion), but the foundation does not mandate them.

## What This Map Does NOT Do

This map does **not**:

- ❌ Duplicate the recovery archive. The archive is in continuity.
- ❌ Add new recovered knowledge that is not in the archive.
- ❌ Re-classify the recovery archive's 11 files against the 5-tier hierarchy.
- ❌ Promote the 2 recovered governance rules to canonical (per founder direction).
- ❌ Resolve the 3 open founder decisions (D1, D2, D3) — those are the founder's decisions.

The map is **observational**, not **additive**. It maps; it does not extend.

## Cross-References

- `02-ryzen/CANONICAL-RYZEN-MAP.md` — the sibling map to the canonical Ryzen definition
- `04-rebuild-integration/RS-PHASES.md` — the map to the rebuild spec
- `06-runtime-roadmap/ROADMAP.md` — the runtime roadmap (this repo)
- `07-runtime-scaffolding/*/README.md` — the per-directory scaffolding placeholders
- Canonical Recovery Archive: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERY-INDEX.md`
