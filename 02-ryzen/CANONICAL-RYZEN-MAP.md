# Canonical Ryzen Map (this repository → canonical)

```yaml
---
type: ryzen-integration
section: canonical-ryzen-map
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
canonical_ref: Javalin13/ryzen-continuity/blob/main/02-ryzen/RYZEN-CANONICAL.md
amendable: true-additively
```

## Purpose

This document is a **map** from this repository (`ryzen-core`) to the canonical Ryzen definition in the `ryzen-continuity` repository. It captures *which canonical Ryzen facts* are relevant to this implementation-successor repository, and *how* this repository honors them.

**The Ryzen Canonical v1.0 is the source of truth.** This map is a *navigation aid*. When this map disagrees with the canonical, the canonical wins.

## The Ryzen Identity (relevant facts)

The canonical Ryzen Canonical v1.0 codifies the Ryzen identity as:

> "Ryzen is a recursively governed, continuity-driven, executive cognitive infrastructure system capable of generating and governing ARCs. The objective is not theoretical intelligence. The objective is: sustained coherent operational continuity."

The 5 key facts from the canonical that this repository must honor:

### Fact R-1 — Ryzen is a *System*, Not a *Model*

Ryzen is not a language model. Ryzen is not a chatbot. Ryzen is a **system** — a runtime that generates and governs ARCs (Autonomous Relational Constructs).

**How this repository honors R-1:** The 11-folder structure is the *system*. The runtime will live in `07-runtime-scaffolding/`. The system is the *whole* repository, not a single file or directory.

### Fact R-2 — Ryzen is Recursively Governed

Every action in Ryzen passes through governance validation. The recursion is *bounded* (5 levels deep in the recovered code; R2 will add the Action Authorization Matrix and the Risk Classification).

**How this repository honors R-2:** The 10 foundation governance rules in `00-foundation/GOVERNANCE.md` are the governance substrate. The R2 phase of the rebuild will add the Action Authorization Matrix and the Risk Classification as *new* governance rules.

### Fact R-3 — Ryzen is Continuity-Driven

Ryzen's primary value is *continuity* — the preservation of operational coherence across time, across sessions, across ARCs, across evolution. The 4-layer Memory Model (operational / strategic / creator / governance) is the continuity substrate.

**How this repository honors R-3:** The recovery archive integration (`03-recovery-integration/`) is the continuity substrate *for the implementation successor*. The integration with the continuity repo (canonical doctrine) is the continuity substrate *for the doctrine*. The runtime roadmap (`06-runtime-roadmap/`) is the continuity substrate *for the operational evolution*.

### Fact R-4 — Ryzen Generates and Governs ARCs

ARCs (Autonomous Relational Constructs) are the operational units of Ryzen. The first-generation ARCs are **FleetConnect, Earth, and FamilieKompas**. The ARC Factory generates ARCs from a topology; the ARC governance substrate ensures ARCs operate within the doctrine.

**How this repository honors R-4:** `07-runtime-scaffolding/apps/arc-factory/` is the future home of the ARC Factory. `07-runtime-scaffolding/apps/fleet-arc/` is the future home of the first ARC. R4 of the rebuild will add `apps/earth-arc/` and `apps/familiekompas-arc/`.

### Fact R-5 — Ryzen's Objective is Sustained Coherent Operational Continuity

Not theoretical intelligence. Not AGI. Not consciousness. *Operational continuity* — the system that does the work, preserves the work, and improves the work over time.

**How this repository honors R-5:** The 4-phase rebuild sequence (R1 → R2 → R3 → R4) is the operational continuity roadmap. Each phase produces a *durable asset* that compounds. The foundation is stage 0 of the operational continuity chain.

## The Ecosystem Hierarchy

The canonical Ryzen Canonical v1.0 codifies the ecosystem hierarchy:

```
Creator (founder)
   ↓
Ryzen (the system)
   ↓
ARCs (operational units: FleetConnect, Earth, FamilieKompas)
   ↓
Brains (cognitive units within ARCs)
   ↓
Agents (execution units within Brains)
```

**How this repository honors the hierarchy:**
- This repository is **Ryzen** (the system), not an ARC, not a Brain, not an Agent.
- The runtime in `07-runtime-scaffolding/` will *generate* ARCs via the ARC Factory.
- The ARCs themselves are not in this repository. They are in their own repositories (per the doctrine's "ARCs may never create new ARCs" rule applied to projects).

## The 3 Ryzen Roles (from the canonical)

The canonical codifies 3 unrealized Ryzen roles. Per the Interpretation Protocol, they are classified as **Strategic Vision** (not implemented, not approved, not active execution):

1. **Persistent operational agent** — the runtime that operates 24/7 across the founder's workflows.
2. **Autonomous synthesis engine** — the runtime that produces *new* ARCs, *new* Brains, *new* governance rules.
3. **Continuity preservation engine** — the runtime that preserves the founder's identity, capability, and operational state across decades.

**How this repository honors the 3 roles:** The 11-folder structure is the foundation for all 3. The R1–R4 rebuild sequence is the path to all 3. The 3 roles are *not* implemented in this foundation; they are the *strategic vision* that this foundation serves.

## The Relationship to the Recovery Archive

The recovery archive (in `ryzen-continuity/04-recovery-archive/`) preserves the lost original runtime's recovered knowledge. This repository is the *implementation successor* to that lost runtime.

**How this repository honors the relationship:** The 8 reusable concepts (C1–C8) in the recovery archive are mapped to the scaffolding directories in `07-runtime-scaffolding/`. The 19-step build sequence in the recovery archive informs the runtime roadmap. The 7 lessons in the recovery archive inform the foundation governance.

## The Relationship to the Rebuild Specification

The Rebuild Specification v1.0 (in `ryzen-continuity/RYZEN-REBUILD-SPECIFICATION-v1.0.md`) defines the 4-phase rebuild sequence. This repository is the *implementation home* for the rebuild.

**How this repository honors the relationship:** The 4 phases (R1 → R2 → R3 → R4) are mapped to the runtime roadmap (`06-runtime-roadmap/`) and to the scaffolding (`07-runtime-scaffolding/`). Each phase is a *commitment*: when R1 begins, the substrate in `07-runtime-scaffolding/` is built per the rebuild spec.

## What This Map Does NOT Do

This map does **not**:

- ❌ Duplicate the canonical Ryzen Canonical. The canonical is in continuity.
- ❌ Add new Ryzen identities or ecosystem hierarchies that are not in the canonical.
- ❌ Promote the 3 unrealized Ryzen roles from "Strategic Vision" to "Active Execution" without an explicit founder decision and an ADR in continuity.
- ❌ Re-classify the recovery archive, the rebuild spec, or the original runtime.

The map is **observational**, not **additive**. It maps; it does not extend.

## Cross-References

- `02-ryzen/ARCHITECTURE-MAP.md` — the sibling map to the canonical architecture
- `03-recovery-integration/RECOVERY-MAP.md` — the map to the recovery archive
- `04-rebuild-integration/RS-PHASES.md` — the map to the rebuild spec
- `06-runtime-roadmap/ROADMAP.md` — the runtime roadmap (this repo)
- Canonical Ryzen Canonical: `Javalin13/ryzen-continuity/blob/main/02-ryzen/RYZEN-CANONICAL.md`
