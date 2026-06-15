# Ryzen Core — Interpretation Protocol (Foundation Layer)

```yaml
---
type: governance
section: foundation-interpretation-protocol
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
canonical_interpretation_protocol_ref: Javalin13/ryzen-continuity/blob/main/00-governance/INTERPRETATION-PROTOCOL.md
amendable: true-additively
```

## Purpose

This document is the **foundation interpretation protocol** for the `ryzen-core` repository. It is **not** the canonical interpretation protocol. The canonical lives in `Javalin13/ryzen-continuity/blob/main/00-governance/INTERPRETATION-PROTOCOL.md` (v1.0 as of 2026-06-15). When this document disagrees with the canonical, the canonical wins.

This document captures the *foundation-specific* application of the canonical protocol — how the 5-tier reality hierarchy, the 3 operational rules, the anti-hallucination rule, and the runtime index apply to *this* repository.

## The 3 Operational Rules (re-stated from the canonical)

The canonical Interpretation Protocol codifies 3 operational rules. They apply to this foundation in full:

### Rule IP-1 — Reality > Doctrine

**Operational meaning for this foundation:** The repository's own operation (governance, cadence, ADR system, naming, tagging, commit doctrine, scaffolding placeholders) is the only tier at "Reality." The recovered package is "Approved Architecture with historical implementation evidence." The original runtime is "Lost." The rebuild specification is "Planning Artifacts." The continuity repository is "Reality" (as the canonical doctrine layer).

### Rule IP-2 — Implementation > Aspiration

**Operational meaning for this foundation:** This foundation contains *no runtime code*. The runtime is *planned* (R1–R4) and *scaffolded* (empty directories with explicit "NOT IMPLEMENTED" placeholders). The foundation is *implementation-ready*, not *implementation-complete*. **The doctrine must not claim the foundation is more than it is.**

### Rule IP-3 — Evidence > Theory

**Operational meaning for this foundation:** Every claim in this foundation must be anchored to a file. Claims about "what the runtime will do" must reference the rebuild spec, the recovery archive, or the continuity doctrine. Claims about "what this repository is" must reference this file (or `README.md`, `FOUNDATION.md`, `GOVERNANCE.md`).

## The 5-Tier Document Classification (re-stated from the canonical)

The canonical Interpretation Protocol codifies a 5-tier document classification:

| # | Tier | Definition | This foundation's classification |
|---|---|---|---|
| 1 | **Reality** | The repository's own operation | This repository's own operation (governance, cadence, ADR system, naming, tagging, commit doctrine) |
| 2 | **Active Execution** | A canonical feature is currently being built | (Will become active in R1 of the rebuild) |
| 3 | **Approved Architecture** | The design is approved by the founder; the build is planned but not started | The 11-folder structure, the scaffolding placeholders, the recovery maps, the rebuild integration |
| 4 | **Strategic Vision** | Long-term direction in the canonical doctrine | The R4 multi-ARC plan, the civilization-scale framework (in continuity) |
| 5 | **Research & Exploration** | Investigated but not yet approved; not in the canonical | The 3 open founder decisions (D1, D2, D3) |

## The Anti-Hallucination Rule

Every claim in every file in this repository MUST be locatable in the 5-state anti-hallucination space:

1. **Implemented** — the runtime is built and operational.
2. **Planned** — the runtime is on the roadmap (R1–R4) but not yet started.
3. **Designed** — the runtime is designed (in the rebuild spec, the recovery archive) but not yet on the roadmap.
4. **Envisioned** — the runtime is conceptualized (in the continuity doctrine) but not yet designed.
5. **Researched** — the runtime is investigated but not yet conceptualized.

**The Anti-Hallucination Rule for this foundation:**

- ❌ **DO NOT** claim the runtime is "implemented" anywhere in this foundation. It is not.
- ✅ **DO** claim the runtime is "planned" (R1–R4 in the rebuild spec) and "designed" (in the recovery archive) and "scaffolded" (in `07-runtime-scaffolding/`).
- ❌ **DO NOT** claim the 3 open founder decisions are "decided." They are open.
- ✅ **DO** claim the 3 open founder decisions are "documented as open" (in `00-foundation/FOUNDATION.md` and the recovery archive's `OPEN-DECISIONS.md`).

## The Runtime Index

The canonical interpretation protocol requires a **runtime index** that classifies every document in the repository against the 5 tiers. This foundation's runtime index is at `00-foundation/CLASSIFICATION-INDEX.md` and is updated additively as files are added.

The runtime index is the **operational evidence** that the protocol is in force. Without it, the protocol is a sticker on a file.

## The 5 Foundation Lifecycle States (re-stated from the foundation doctrine)

The foundation doctrine's 5 lifecycle states (Reality / Active Execution / Approved Architecture / Strategic Vision / Research & Exploration) are the *application* of the 5-tier classification to *this* foundation. They are listed in `00-foundation/GOVERNANCE.md` §"The 5 Foundation Lifecycle States".

## How to Use This Protocol

When authoring a new file in this foundation:

1. **Classify the file** against the 5 tiers. Add the classification to the YAML front-matter (`classification:` field).
2. **Locate every claim** in the 5-state anti-hallucination space (implemented / planned / designed / envisioned / researched).
3. **Reference the canonical** for any claim that crosses repositories (e.g., "per the canonical Founder Identity Profile v1.0").
4. **Add the file to the runtime index** (`00-foundation/CLASSIFICATION-INDEX.md`) with its tier and the "why this tier" justification.
5. **Update the canonical interpretation index** (`Javalin13/ryzen-continuity/blob/main/00-governance/CLASSIFICATION-INDEX.md`) to reference the new file. This is the cross-repository index that proves both repositories are in sync.

## What This Protocol Does NOT Do

This protocol does **not**:

- ❌ Promote any claim from "Approved Architecture" to "Active Execution" without an explicit founder decision and an ADR in the continuity repo.
- ❌ Demote any claim from "Active Execution" to "Approved Architecture" without an explicit founder decision and an ADR.
- ❌ Re-classify the recovery archive (it is what it is: "Approved Architecture with historical implementation evidence").
- ❌ Re-classify the original runtime (it is what it is: "Lost").
- ❌ Add new tiers to the 5-tier hierarchy without an ADR in the continuity repo.

The protocol is **observational**, not **promotional**. It classifies; it does not promote.

## Cross-References

- `00-foundation/FOUNDATION.md` — the foundation doctrine
- `00-foundation/GOVERNANCE.md` — the foundation governance rules
- `00-foundation/CLASSIFICATION-INDEX.md` — the runtime index (will be created when files are added)
- Canonical interpretation protocol: `Javalin13/ryzen-continuity/blob/main/00-governance/INTERPRETATION-PROTOCOL.md`
- Canonical runtime index: `Javalin13/ryzen-continuity/blob/main/00-governance/CLASSIFICATION-INDEX.md`
