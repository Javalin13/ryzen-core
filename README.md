# Ryzen Core Repository Foundation

```yaml
---
type: foundation
status: foundation-seeded
created: 2026-06-15
doctrine: ryzen-continuity repo is canonical; this repo is the implementation successor to the lost original runtime
classification:
  foundation: approved-architecture
  continuity-repo: reality
  recovered-package: approved-architecture-with-historical-evidence
  original-runtime: lost
  rebuild-spec: planning-artifact
amendable: true-additively
replaced_runtime: original Ryzen implementation repository (lost)
related_repo_canonical: Javalin13/ryzen-continuity
related_artifact: 2. Implementation-20260615T111401Z-3-001.zip
```

## What this repository is

This is the **Ryzen Core Repository Foundation** — the durable implementation home for future Ryzen runtime development.

The original Ryzen implementation repository was lost. The founder authorized (2026-06-15) the creation of this foundation as the **implementation successor** to that lost runtime, while the `ryzen-continuity` repository remains the **canonical doctrine, recovery archive, and rebuild specification** layer.

This repository is **NOT** the runtime itself. It is the **foundation that will hold the future runtime**.

## What this repository is NOT

- ❌ **NOT** the kernel runtime. The CognitionLoop, the Governance Middleware, the Recursive Verification Engine, the Memory Federation, the Brain contracts, the ARC Factory, the Fleet ARC, the Kernel API — **none of these are implemented here.** They are *scaffolded as empty directories with explicit "NOT IMPLEMENTED" placeholders* that point to the rebuild specification and the recovered evidence.
- ❌ **NOT** the canonical doctrine. The canonical doctrine (Founder Identity, Capability Model, Interpretation Protocol) lives in `ryzen-continuity/01-founder/` and `ryzen-continuity/00-governance/`. This repository contains *maps* to those canonicals, not the canonicals themselves.
- ❌ **NOT** a clone of the recovery archive. The recovery archive lives in `ryzen-continuity/04-recovery-archive/`. This repository contains *integration points* that reference the archive, not the archive itself.

## What this repository IS

This repository **IS**:
- ✅ The **durable implementation home** for future Ryzen runtime development.
- ✅ The **integration point** for the canonical doctrine (in continuity), the recovery archive (in continuity), the rebuild specification (in continuity), the ADRs (this repo), and the runtime roadmap (this repo).
- ✅ The **structural successor** to the lost runtime repository. When the future runtime is built, the source code lives here.
- ✅ **Doctrine-aligned.** Every file in this repository is consistent with the Founder Identity, the Founder Capability Model, and the Interpretation Protocol.
- ✅ **Recovery-informed.** The 8 reusable concepts, the 19-step build sequence, the 5 design decisions, and the 7 lessons (all in the recovery archive) inform the scaffolding here.
- ✅ **Rebuild-aligned.** The 4-phase rebuild sequence (R1 → R2 → R3 → R4) in the Rebuild Specification v1.0 (in continuity) is the runtime roadmap for this repository.

## Scope (per founder direction 2026-06-15)

**Scope:**
- Repository structure
- Governance integration
- Recovery archive integration
- Rebuild specification integration
- ADR integration
- Runtime roadmap integration
- Implementation scaffolding only

**Do NOT implement (at this stage):**
- ❌ Kernel runtime
- ❌ Memory Federation
- ❌ ARC Runtime
- ❌ Governance Middleware
- ❌ Agent Runtime

**The objective is continuity and future implementation readiness. Not runtime delivery.**

## The 11-Folder Structure

This foundation is organized into 11 top-level folders, each with a specific role:

| # | Folder | Role | Implementation status |
|---|---|---|---|
| 1 | `00-foundation/` | The foundation doctrine that grounds this repository (FOUNDATION.md, GOVERNANCE.md, INTERPRETATION-PROTOCOL.md) | Foundation-only |
| 2 | `01-founder/` | Maps to the canonical Founder Identity and Capability Model in `ryzen-continuity` | Maps only (no canonical) |
| 3 | `02-ryzen/` | Maps to the canonical Ryzen definition and architecture in `ryzen-continuity` | Maps only (no canonical) |
| 4 | `03-recovery-integration/` | Integration points for the recovery archive (in `ryzen-continuity/04-recovery-archive/`) | Cross-references only |
| 5 | `04-rebuild-integration/` | Integration of the Rebuild Specification v1.0 (in `ryzen-continuity/RYZEN-REBUILD-SPECIFICATION-v1.0.md`) | Cross-references only |
| 6 | `05-adrs/` | Architectural Decision Records for this repository's implementation decisions | Foundation-only |
| 7 | `06-runtime-roadmap/` | The runtime roadmap for this repository (mapped to the 4-phase rebuild sequence) | Roadmap-only |
| 8 | `07-runtime-scaffolding/` | Future implementation directories: `apps/`, `packages/`, `infrastructure/`, `docs/` | **SCAFFOLDED, NOT IMPLEMENTED** |
| 9 | `08-observability/` | Future observability stack: governance events, traces, dashboards | **SCAFFOLDED, NOT IMPLEMENTED** |
| 10 | `09-cadences/` | Daily snapshots, weekly reviews, monthly reviews, lessons learned, idea backlog | Templates-only |
| 11 | `10-tools/` | Scripts and utilities (e.g., `push-to-remote.sh`) | Tools-only |

**Why 11 folders (and not the same 11 as continuity)?** The continuity repo is the *canonical doctrine* layer; this repo is the *implementation successor* layer. The folder numbering is aligned (both start with 0X) so cross-references are easy, but the *content* is different. Continuity has 0X=governance, 1X=founder, 2X=ryzen, 3X=hermes, 4X=fleetconnect, 5X=earth, 6X=familiekompas, 7X=architecture, 8X=roadmaps, 9X=decisions, 10X=lessons, 11X=daily-snapshots. This repo has 0X=foundation, 1X=founder-map, 2X=ryzen-map, 3X=recovery-integration, 4X=rebuild-integration, 5X=adrs, 6X=runtime-roadmap, 7X=runtime-scaffolding, 8X=observability, 9X=cadences, 10X=tools.

## The Constitutional Constraints (in force from the first commit)

1. **Doctrine-continuity alignment.** This repository references the canonical doctrine in `ryzen-continuity`. The doctrine is *not* duplicated here; it is *referenced*.
2. **Recovery-informed scaffolding.** Every empty directory in `07-runtime-scaffolding/` has a `README.md` that names which recovered concept (C1–C8) and which rebuild phase (R1–R4) the directory will eventually implement.
3. **No implementation at this stage.** The runtime is *not* built in this foundation. The runtime is *planned* in `06-runtime-roadmap/` and *scaffolded* in `07-runtime-scaffolding/`.
4. **Additive evolution.** Every change to this repository is additive, never destructive. The 7 doctrine rules from continuity apply.
5. **Founder authority preserved.** Every change requires founder direction. The 7 execution risks from the Capability Model apply.
6. **Interpretation Protocol in force.** Every claim in this repository is classified against the 5-tier reality hierarchy (Reality / Active Execution / Approved Architecture / Strategic Vision / Research & Exploration). The runtime index will live at `00-foundation/CLASSIFICATION-INDEX.md`.
7. **Token hygiene.** No credentials, tokens, or secrets are committed to this repository. All credentials are stored in the OS credential store and used transiently.

## Cross-References

- **Canonical doctrine:** `Javalin13/ryzen-continuity` (this repo's older sibling; the canonical)
- **Recovery archive:** `Javalin13/ryzen-continuity/tree/main/04-recovery-archive` (the durable home for recovered knowledge)
- **Rebuild specification:** `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` (the 4-phase rebuild plan)
- **ADR template (continuity):** `Javalin13/ryzen-continuity/blob/main/09-decisions/TEMPLATE.md` (the ADR template this repo follows)
- **Implementation Package (recovered):** `2. Implementation-20260615T111401Z-3-001.zip` (the historical evidence in the continuity repo's recovery archive)

## What Comes Next

Per the founder's direction, this is **foundation only**. The next deliverables (after founder authorization) will be:

1. **Phase R1 of the rebuild** — stand up the substrate in `07-runtime-scaffolding/` (CognitionLoop, Governance Middleware, Memory Federation, Verification Engine, ARC Factory, Brain contracts, Structured Logging, Kernel API, Fleet ARC).
2. **Production governance hardening (R2)** — Action Authorization Matrix, Risk Classification, governance observability.
3. **Real execution & adaptive cognition (R3)** — real adapters, long-horizon memory, dashboards, adaptive cognition, security.
4. **Multi-ARC foundations (R4)** — Earth ARC, FamilieKompas ARC, cross-ARC intelligence convergence.

**No implementation begins today.** The foundation is the prerequisite. The foundation is doctrine-aligned. The foundation is the durable home. The runtime is the future.

## License

All Rights Reserved. License terms: same as `Javalin13/ryzen-continuity` (the canonical).
