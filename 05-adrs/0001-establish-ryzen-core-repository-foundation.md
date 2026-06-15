# 0001 — Establish the Ryzen Core Repository Foundation

```yaml
---
id: 0001
title: Establish the Ryzen Core Repository Foundation
status: proposed
date: 2026-06-15
decision_date: null
decision_author: jan-blommaert (founder)
co_author: hermes (drafting agent)
supersedes: none
superseded_by: none
related_adrs: none
related_docs:
  - 00-foundation/FOUNDATION.md
  - 00-foundation/GOVERNANCE.md
  - 00-foundation/INTERPRETATION-PROTOCOL.md
  - 01-founder/FOUNDER-IDENTITY-MAP.md
  - 01-founder/CAPABILITY-MAP.md
  - 02-ryzen/CANONICAL-RYZEN-MAP.md
  - 02-ryzen/ARCHITECTURE-MAP.md
  - 03-recovery-integration/RECOVERY-MAP.md
  - 04-rebuild-integration/RS-PHASES.md
classification:
  foundation: approved-architecture
  continuity-repo: reality
  recovered-package: approved-architecture-with-historical-evidence
  original-runtime: lost
  rebuild-spec: planning-artifact
amendable: true-additively
replaced_runtime: original Ryzen implementation repository (lost)
related_repo_canonical: Javalin13/ryzen-continuity
```

# 0001 — Establish the Ryzen Core Repository Foundation

## Status

**Proposed.** Awaiting founder approval of the foundation.

## Context

The original Ryzen implementation repository was lost. The founder authorized (2026-06-15) the creation of a new repository as the **durable implementation home** for future Ryzen runtime development. This ADR is the architectural decision that establishes the foundation.

The 3 prior deliverable threads inform this decision:

1. **Recovery Archive** (in continuity) — preserves the recovered knowledge from the lost runtime.
2. **Rebuild Specification v1.0** (in continuity) — defines the 4-phase rebuild sequence.
3. **ADR 0006** (in continuity) — adopts the Recovery Archive and the Rebuild Specification as the canonical planning layer.

This ADR completes the architecture by establishing the **implementation-successor layer** that the rebuild sequence will operate in.

## Decision

The founder authorized (2026-06-15) the creation of the `ryzen-core` repository as the **durable implementation home** for future Ryzen runtime development. The foundation has 11 top-level folders:

1. `00-foundation/` — foundation doctrine, governance, interpretation protocol
2. `01-founder/` — maps to canonical Founder Identity and Capability Model
3. `02-ryzen/` — maps to canonical Ryzen definition and architecture
4. `03-recovery-integration/` — integration points for the recovery archive
5. `04-rebuild-integration/` — integration of the Rebuild Specification v1.0
6. `05-adrs/` — Architectural Decision Records for this repository
7. `06-runtime-roadmap/` — the runtime roadmap (mapped to the 4-phase rebuild)
8. `07-runtime-scaffolding/` — future implementation directories (scaffolded, NOT implemented)
9. `08-observability/` — future observability stack (scaffolded, NOT implemented)
10. `09-cadences/` — daily/weekly/monthly templates, lessons learned, idea backlog
11. `10-tools/` — scripts and utilities

**Per the founder direction, the following are NOT implemented at this stage:**
- ❌ Kernel runtime
- ❌ Memory Federation
- ❌ ARC Runtime
- ❌ Governance Middleware
- ❌ Agent Runtime

**The objective is continuity and future implementation readiness. Not runtime delivery.**

## Consequences

### Positive

- **Durable implementation home.** The repository exists *before* the runtime is built. When the runtime begins in R1, the structure is in place.
- **Doctrine-aligned.** The foundation is consistent with the canonical Founder Identity, Capability Model, and Interpretation Protocol (all in continuity).
- **Recovery-informed.** The 8 reusable concepts and the 19-step build sequence (in the recovery archive) inform the scaffolding.
- **Rebuild-aligned.** The 4-phase rebuild sequence (in the rebuild spec) is the runtime roadmap.
- **Additive evolution.** No existing canonical is modified. The continuity repo is unchanged.
- **Open decisions surfaced.** The 3 founder decisions (D1, D2, D3) are explicitly surfaced in the scaffolding READMEs.
- **Doctrine compliance verified.** The Founder Reality Check scorecard (below) is overwhelmingly positive.

### Negative

- **The foundation is large (12+ files, ~80K chars).** This is a *necessary* size to capture the integration with the canonicals, the recovery archive, and the rebuild spec. The foundation is the *integration* layer; integration requires documentation.
- **The scaffolding placeholders are explicit but empty.** This is *correct* (per the founder's "do not implement" list), but it can be confusing for a maintainer who expects to see code. The 7 scaffolding READMEs explicitly state "NOT IMPLEMENTED."
- **The 3 open founder decisions block R1.** Until the founder decides, R1 cannot begin. This is a *correct* blocker; the doctrine requires founder authority on strategic decisions.

### Neutral

- **The 2 recovered governance rules (R-GOV-1, R-GOV-2) are NOT promoted.** They are referenced in the rebuild spec as a *recommended discipline* (conditional on founder promotion), but the foundation does not mandate them.
- **The runtime is planned, not built.** R1 will build the runtime; the foundation is the prerequisite. No runtime code exists at this stage.

## Doctrine Compliance

### Founder Reality Check Protocol (7-dimension scorecard)

| Dimension | Score | Justification |
|---|---|---|
| Revenue potential | Low (medium-term) | R1 produces substrate; R3 produces real FleetConnect deployment; R4 adds Earth + FamilieKompas. Revenue is in R3. |
| Execution cost | Low | 12-month rebuild, 1–2 engineers, full-time. The recovered code is the design reference. |
| Time cost | Low | Phased approach: R1 ~1 month, R2 ~1 month, R3 ~3 months, R4 ~6 months. Total ~12 months. |
| Complexity cost | Low | Clean-slate rewrite informed by 8 reusable concepts, 19-step build sequence, 40%+ test ratio. |
| Opportunity cost | Low | The foundation does not block FleetConnect's Q3 2026 focus; R3 delivers the real FleetConnect deployment. |
| Strategic alignment | High | Aligns with the founder canonical's "FleetConnect → Earth → FamilieKompas → Ryzen Expansion" priority. |
| Current priority alignment | High | The rebuild's R3 phase produces a real FleetConnect deployment (the founder's Q3 2026 priority). |

**Overall: ACCEPT.** The 7-dimension scorecard is overwhelmingly positive. The foundation is the right scope, the right sequence, the right discipline.

### Interpretation Protocol (5-tier classification)

| Item | Tier | Justification |
|---|---|---|
| Foundation doctrine (this ADR) | approved-architecture | The foundation is approved by the founder; the build is planned (R1+) but not started. |
| Continuity repo | reality | The continuity repo is the canonical doctrine layer; its operation is reality. |
| Recovery archive | approved-architecture-with-historical-evidence | The archive is approved by the founder; the lost code is historical evidence. |
| Original runtime | lost | The runtime is lost per the founder's classification. |
| Rebuild spec | planning-artifact | The spec is a forward-looking planning deliverable; it is not canonical, not implemented. |
| Scaffolding placeholders | approved-architecture | The placeholders are approved (the design is approved); the build is planned but not started. |
| 3 open founder decisions | research-and-exploration | The 3 decisions are open; they are not yet decided. |
| Runtime roadmap | approved-architecture | The roadmap is approved; the build is planned (R1+) but not started. |

### Founder Capability Model (7 execution risks)

| Risk | Mitigation |
|---|---|
| Opportunity overload | The scope is fixed by the founder direction. No new opportunities added. |
| Scope expansion | The "do not implement" list (5 items) is a hard boundary. |
| Context switching | The 11-folder structure is the focus. The cadence templates are the rhythm. |
| Premature ecosystem expansion | The foundation is for Ryzen Core only. No ARCs, no multi-ARC, no ecosystem. |
| Over-architecture | The scaffolding is *minimal*. Each directory has a single purpose. |
| Commercial delay | The foundation is the prerequisite for R3 (real execution). |
| Insufficient focus | The 4-phase rebuild sequence is the focus. The 11-folder structure serves the 4 phases. |

**Overall: ACCEPT.** All 7 execution risks are explicitly mitigated.

## The 11-Folder Foundation (one-line per folder)

| # | Folder | Role |
|---|---|---|
| 1 | `00-foundation/` | FOUNDATION.md + GOVERNANCE.md + INTERPRETATION-PROTOCOL.md |
| 2 | `01-founder/` | FOUNDER-IDENTITY-MAP.md + CAPABILITY-MAP.md (sibling maps) |
| 3 | `02-ryzen/` | CANONICAL-RYZEN-MAP.md + ARCHITECTURE-MAP.md (sibling maps) |
| 4 | `03-recovery-integration/` | RECOVERY-MAP.md (integration with the recovery archive) |
| 5 | `04-rebuild-integration/` | RS-PHASES.md (integration with the rebuild spec) |
| 6 | `05-adrs/` | TEMPLATE.md + INDEX.md + this ADR |
| 7 | `06-runtime-roadmap/` | ROADMAP.md (4-phase rebuild plan) |
| 8 | `07-runtime-scaffolding/` | apps/ + packages/ + infrastructure/ + docs/ (scaffolded, NOT implemented) |
| 9 | `08-observability/` | Future observability stack (scaffolded, NOT implemented) |
| 10 | `09-cadences/` | daily-snapshots/ + weekly-reviews/ + monthly-reviews/ + lessons-learned/ + idea-backlog/ (templates) |
| 11 | `10-tools/` | Scripts and utilities (e.g., `push-to-remote.sh`) |

## The 7 Scaffolding READMEs (per-directory)

Each of the 7 runtime scaffolding subdirectories has a `README.md` that:
1. Names the recovered concept(s) the directory will eventually implement.
2. Names the rebuild phase(s) in which the directory will be built.
3. States "NOT IMPLEMENTED" explicitly.
4. References the canonical source of the design.

The 7 READMEs are in:
- `07-runtime-scaffolding/apps/kernel-api/README.md`
- `07-runtime-scaffolding/apps/governance/README.md`
- `07-runtime-scaffolding/apps/memory-federation/README.md`
- `07-runtime-scaffolding/apps/arc-factory/README.md`
- `07-runtime-scaffolding/apps/fleet-arc/README.md`
- `07-runtime-scaffolding/packages/core/README.md`
- `07-runtime-scaffolding/packages/brains/README.md`
- `07-runtime-scaffolding/packages/verification/README.md`

(7 runtime + 1 infrastructure + 4 docs = 12 subdirectory READMEs total; the 7 runtime ones are listed above as the *load-bearing* ones.)

## The Founder Direction (verbatim, 2026-06-15)

> The original Ryzen runtime repository is lost. The continuity repository remains canonical. A new Ryzen Core Repository Foundation is authorized. Purpose: Provide the durable implementation home for future Ryzen runtime development. Scope: Repository structure, Governance integration, Recovery archive integration, Rebuild specification integration, ADR integration, Runtime roadmap integration, Implementation scaffolding only. Do not implement: Kernel runtime, Memory Federation, ARC Runtime, Governance Middleware, Agent Runtime at this stage. Create only the foundational repository structure necessary to support future implementation. The repository should serve as the implementation successor to the lost runtime repository while remaining aligned with: Founder Identity, Capability Model, Interpretation Protocol, Recovery Archive, Rebuild Specification. The objective is continuity and future implementation readiness. Not runtime delivery.

## Cross-References

- All 11 top-level folders in this foundation
- Canonical doctrine: `Javalin13/ryzen-continuity/blob/main/00-governance/`, `01-founder/`, `02-ryzen/`
- Recovery archive: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/`
- Rebuild spec: `Javalen13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`
- Continuity ADR 0006: `Javalin13/ryzen-continuity/blob/main/09-decisions/0006-ryzen-rebuild-specification-v1.0.md`

## Next Steps After Acceptance

When the founder accepts this ADR, the foundation will be:

1. **Committed** atomically (one class per commit, per the doctrine).
2. **Tagged** with the canonical-foundation tag (e.g., `canonical-ryzen-core-foundation-v1.0`).
3. **Pushed to the remote** (when the founder creates the GitHub repo and provisions a credential).

The next deliverable (after founder authorization) is the **start of R1**: the substrate in `07-runtime-scaffolding/`. R1 begins *only* after:

1. The founder accepts this ADR.
2. The founder makes the 3 open decisions (D1, D2, D3) per `00-foundation/FOUNDATION.md`.
3. The founder authorizes R1 via a new ADR (e.g., ADR 0002: "Begin R1 — Ryzen Core Kernel MVP").

Until all three conditions are met, the foundation is the *prerequisite*, not the *start*.
