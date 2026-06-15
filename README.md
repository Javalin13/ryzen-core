# Ryzen Core Repository — Continuity & Accumulation Foundation

```yaml
---
type: foundation
status: foundation-only, accumulation-active
created: 2026-06-15
doctrine: ryzen-continuity repo is canonical; this repo is the accumulation layer for validated Fleet ARC discoveries
strategic_posture: deferred, accumulation-first (per ADR 0002)
classification:
  foundation: approved-architecture
  continuity-repo: reality
  recovered-package: approved-architecture-with-historical-evidence
  original-runtime: lost (implementation successor role preserved but deferred)
  rebuild-spec: planning-artifact
  intake-folder: research-and-exploration (active as accumulation layer)
amendable: true-additively
replaced_runtime: original Ryzen implementation repository (lost)
related_repo_canonical: Javalin13/ryzen-continuity
related_arc: FleetConnect (primary execution priority #1)
related_artifact: 2. Implementation-20260615T111401Z-3-001.zip
```

## What this repository is

This is the **Ryzen Core Repository — Continuity & Accumulation Foundation** — the *long-term accumulation layer* that receives validated intelligence from Fleet ARC (the first operational ARC domain) and future ARC domains.

Per the founder's clarification 2026-06-15 (ADR 0002):

> A Ryzen Core Foundation Repository is authorized. This authorization is not based on immediate Ryzen runtime implementation. This authorization exists for **continuity, accumulation, and future implementation readiness**.
>
> The objective is not to build Ryzen today. The objective is to ensure that every future Fleet ARC discovery has a canonical location where it can accumulate and compound.
>
> The repository should therefore be designed as: A continuity and implementation foundation. Not as an active runtime development project.
>
> FleetConnect remains execution priority #1.
> Ryzen Core acts as the long-term accumulation layer that receives validated intelligence from Fleet ARC and future ARC domains.

This repository is **NOT** the runtime itself. It is the **foundation that will hold the future runtime** *and* the **accumulation layer** for validated Fleet ARC discoveries.

## What this repository is NOT

- ❌ **NOT** the kernel runtime. The CognitionLoop, the Governance Middleware, the Recursive Verification Engine, the Memory Federation, the Brain contracts, the ARC Factory, the Fleet ARC, the Kernel API — **none of these are implemented here.** They are *scaffolded as empty directories with explicit "NOT IMPLEMENTED" placeholders* that point to the rebuild specification and the recovered evidence.
- ❌ **NOT** the canonical doctrine. The canonical doctrine (Founder Identity, Capability Model, Interpretation Protocol) lives in `ryzen-continuity/01-founder/` and `ryzen-continuity/00-governance/`. This repository contains *maps* to those canonicals, not the canonicals themselves.
- ❌ **NOT** a clone of the recovery archive. The recovery archive lives in `ryzen-continuity/04-recovery-archive/`. This repository contains *integration points* that reference the archive, not the archive itself.

## What this repository IS

This repository **IS**:
- ✅ The **continuity and implementation foundation** for future Ryzen runtime development. *(Per ADR 0002: deferred, not imminent.)*
- ✅ The **active accumulation layer** for validated Fleet ARC discoveries (`11-fleet-arc-intake/`). *(Per ADR 0002: this is the present deliverable.)*
- ✅ The **integration point** for the canonical doctrine (in continuity), the recovery archive (in continuity), the rebuild specification (in continuity), the ADRs (this repo), and the runtime roadmap (this repo).
- ✅ The **structural successor** to the lost runtime repository. *(Latent purpose, preserved but deferred.)* When the future runtime is built, the source code will live here.
- ✅ **Doctrine-aligned.** Every file in this repository is consistent with the Founder Identity, the Founder Capability Model, and the Interpretation Protocol.
- ✅ **Recovery-informed.** The 8 reusable concepts, the 19-step build sequence, the 5 design decisions, and the 7 lessons (all in the recovery archive) inform the scaffolding here.
- ✅ **Rebuild-aligned.** The 4-phase rebuild sequence (R1 → R2 → R3 → R4) in the Rebuild Specification v1.0 (in continuity) is the runtime roadmap for this repository — *deferred* per ADR 0002.

## Scope (per founder direction 2026-06-15, refined by ADR 0002)

**Scope:**
- Repository structure
- Governance integration
- Recovery archive integration
- Rebuild specification integration
- ADR integration
- Runtime roadmap integration
- Implementation scaffolding only
- **Fleet ARC Intake accumulation** *(added per ADR 0002)*

**Do NOT implement (at this stage):**
- ❌ Kernel runtime
- ❌ Memory Federation
- ❌ ARC Runtime
- ❌ Governance Middleware
- ❌ Agent Runtime

**Strategic posture (per ADR 0002):** The runtime implementation is *deferred* and *not imminent*. The foundation's active deliverable is the **accumulation layer** (`11-fleet-arc-intake/`) for validated Fleet ARC discoveries. The runtime phase will be *separately* authorized by the founder when the time comes.

**The objective is continuity and accumulation readiness. Not runtime delivery.**

## The 12-Folder Structure (refined per ADR 0002)

This foundation is organized into 12 top-level folders, each with a specific role:

| # | Folder | Role | Implementation status |
|---|---|---|---|
| 1 | `00-foundation/` | The foundation doctrine that grounds this repository (FOUNDATION.md, GOVERNANCE.md, INTERPRETATION-PROTOCOL.md) | Foundation-only |
| 2 | `01-founder/` | Maps to the canonical Founder Identity and Capability Model in `ryzen-continuity` | Maps only (no canonical) |
| 3 | `02-ryzen/` | Maps to the canonical Ryzen definition and architecture in `ryzen-continuity` | Maps only (no canonical) |
| 4 | `03-recovery-integration/` | Integration points for the recovery archive (in `ryzen-continuity/04-recovery-archive/`) | Cross-references only |
| 5 | `04-rebuild-integration/` | Integration of the Rebuild Specification v1.0 (in `ryzen-continuity/RYZEN-REBUILD-SPECIFICATION-v1.0.md`) | Cross-references only |
| 6 | `05-adrs/` | Architectural Decision Records for this repository's implementation decisions | Foundation-only |
| 7 | `06-runtime-roadmap/` | The runtime roadmap for this repository (mapped to the 4-phase rebuild sequence, **deferred** per ADR 0002) | Roadmap-only |
| 8 | `07-runtime-scaffolding/` | Future implementation directories: `apps/`, `packages/`, `infrastructure/`, `docs/` | **SCAFFOLDED, NOT IMPLEMENTED** |
| 9 | `08-observability/` | Future observability stack: governance events, traces, dashboards | **SCAFFOLDED, NOT IMPLEMENTED** |
| 10 | `09-cadences/` | Daily snapshots, weekly reviews, monthly reviews, lessons learned, idea backlog, **fleet-arc-intake** | Templates-only |
| 11 | `10-tools/` | Scripts and utilities (e.g., `push-to-remote.sh`) | Tools-only |
| 12 | **`11-fleet-arc-intake/`** *(new per ADR 0002)* | **The canonical intake point for validated Fleet ARC discoveries** (10 subdirectories, one per intake type) | **Active as accumulation layer** |

**Why 12 folders (and not 11)?** The first 11 folders were created in the initial foundation (ADR 0001). The 12th folder (`11-fleet-arc-intake/`) was added in ADR 0002 to provide the *active accumulation layer* that the founder's clarification requires. The numbering is *historical* (the 0X-10X pattern is preserved); the 12th is added *additively*. The numbering inconsistency is *honest* — it reflects the additive evolution and the founder's strategic-posture clarification.

**The 0X-1X-2X-3X-4X-5X-6X-7X-8X-9X-10X-11X pattern is the *integration then operation then accumulation* pattern:**
- 0X-5X: Self-integration (foundation, founder, ryzen, recovery, rebuild, ADRs)
- 6X-10X: Operational (roadmap, scaffolding, observability, cadences, tools)
- 11X: **Accumulation (the active deliverable, per ADR 0002)**

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

## What Comes Next (per ADR 0002)

Per the founder's clarification 2026-06-15, this is **foundation + accumulation layer only**. The next deliverables (after founder authorization) will be:

1. **Phase 0 acceptance** (ADR 0001 + ADR 0002 are accepted by the founder).
2. **Accumulation begins** — Fleet ARC discoveries are validated, founder-accepted, and added to the appropriate subdirectory in `11-fleet-arc-intake/`.
3. **Runtime phase authorization** *(separately, when the founder decides)* — a new ADR begins R1. The 3 open founder decisions (D1, D2, D3) must be resolved *before* R1 begins.

**No implementation begins today.** The foundation is the prerequisite. The accumulation is the present deliverable. The runtime is the future.

## License

All Rights Reserved. License terms: same as `Javalin13/ryzen-continuity` (the canonical).
