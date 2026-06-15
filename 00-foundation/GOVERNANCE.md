# Ryzen Core — Governance

```yaml
---
type: governance
section: foundation-governance
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
canonical_governance_ref: Javalin13/ryzen-continuity/blob/main/00-governance/GOVERNANCE.md
amendable: true-additively
```

## Purpose

This document establishes the **foundation governance rules** for the `ryzen-core` repository. It is **not** the canonical governance. The canonical governance lives in `Javalin13/ryzen-continuity/blob/main/00-governance/GOVERNANCE.md` (v1.0 as of 2026-06-15). When this document disagrees with the canonical, the canonical wins.

This document captures the *foundation-specific* rules — the rules that apply to this repository as an *implementation successor* to the lost original runtime, *not* as a doctrine layer.

## The 10 Foundation Governance Rules

### Rule F-GOV-1 — Doctrine-Continuity Alignment

The `ryzen-continuity` repository is the canonical doctrine layer. This repository (`ryzen-core`) is the implementation successor layer. The two are not the same.

- The Founder Identity Profile, the Founder Capability Model, the Interpretation Protocol, the Recovery Archive, and the Rebuild Specification **live in continuity**, not here.
- This repository may *reference* canonicals but may not *duplicate* them.
- When the two repositories disagree, **continuity wins**. No exceptions.
- If a change to continuity is needed, propose it via an ADR in **continuity**, not here.

**Mapped to continuity rule:** `Rule 1: Additive-only evolution`.

### Rule F-GOV-2 — Recovery-Informed Scaffolding

Every empty directory in `07-runtime-scaffolding/` and `08-observability/` MUST have a `README.md` that:

1. Names the recovered concept(s) the directory will eventually implement.
2. Names the rebuild phase(s) in which the directory will be built.
3. States "NOT IMPLEMENTED" explicitly.
4. References the canonical source of the design.

A directory that is empty *and silent* is a doctrinal violation. A directory that is empty *and explicit* is doctrinally compliant.

**Mapped to continuity rule:** `Rule 1: Additive-only evolution`.

### Rule F-GOV-3 — No Implementation at This Stage

Per the founder's direction 2026-06-15, the following are **NOT implemented** at this stage:

- ❌ Kernel runtime
- ❌ Memory Federation
- ❌ ARC Runtime
- ❌ Governance Middleware
- ❌ Agent Runtime

The runtime is *not* built in this foundation. The runtime is *planned* in `06-runtime-roadmap/` and *scaffolded* in `07-runtime-scaffolding/`. **No exceptions.**

**Mapped to continuity rule:** `Rule 2: Continuity before scaling`.

### Rule F-GOV-4 — Additive Evolution

Every change to this repository MUST be additive. No change may delete, modify, or rewrite existing content. The continuity doctrine's "Additive-only evolution" rule applies here in full.

**Mapped to continuity rule:** `Rule 1: Additive-only evolution`.

### Rule F-GOV-5 — Founder Authority Preserved

Every change to this repository requires founder direction. The 7 execution risks from the Founder Capability Model apply in full. The Founder Reality Check Protocol's 7-dimension scorecard MUST be executed before any new idea is pursued.

**Mapped to continuity rule:** `Rule 4: Founder authority`.

### Rule F-GOV-6 — Interpretation Protocol in Force

Every claim in this repository MUST be classified against the 5-tier reality hierarchy (Reality / Active Execution / Approved Architecture / Strategic Vision / Research & Exploration). The runtime index lives at `00-foundation/CLASSIFICATION-INDEX.md` and is updated additively.

**Mapped to continuity rule:** `Rule 6: Interpretation Protocol`.

### Rule F-GOV-7 — Token Hygiene

No credentials, tokens, secrets, API keys, or sensitive data are committed to this repository. All credentials are stored in the OS credential store and used transiently. The token literal never appears in:

- Chat output
- Any file under the working tree
- Any commit
- Any tag annotation
- `.git/config`
- Any skill reference

The only acceptable storage is process-local variable (wiped at end) or OS credential store (encrypted at rest, revocable).

**Mapped to continuity rule:** `Rule 5: Operational realism`.

### Rule F-GOV-8 — Naming Discipline

- Files use **kebab-case** (e.g., `ryzen-rebuild-specification-v1.0.md`).
- Folders use **`NN-purpose`** with a zero-padded two-digit prefix (e.g., `00-foundation`, `07-runtime-scaffolding`).
- Top-level folders are numbered 00–10 (11 folders total).
- Sub-folders within `07-runtime-scaffolding/` use the recovered structure: `apps/`, `packages/`, `infrastructure/`, `docs/`.

**Mapped to continuity rule:** `Rule 7: Naming & structure`.

### Rule F-GOV-9 — Tagging Discipline

- Canonical tags follow the pattern `canonical-<name>-v<major>.<minor>` (e.g., `canonical-recovery-archive-v1.0`).
- Decision tags follow the pattern `decision-<NNNN>-<status>` (e.g., `decision-0001-accepted`).
- All tags are **annotated** with `-a`, with a multi-line message describing what the tag points to.
- Tags are pushed to the remote with `--follow-tags` (or equivalent).

**Mapped to continuity rule:** `Rule 8: Tagging`.

### Rule F-GOV-10 — Commit Discipline

- One **artifact class** per commit. A single commit should change a single coherent unit of work.
- Commit messages follow the pattern `<type>(<scope>): <description>` (Conventional Commits), where type is one of: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `archive`, `decision`, `lesson`, `snapshot`, `spec`, `foundation`, `integration`, `scaffolding`.
- Commit messages include a multi-line body explaining *what* and *why* (not *how*).
- Commit messages reference the ADR(s) that authorize the change (when applicable).
- Every commit MUST be atomic: the working tree MUST be in a coherent state after the commit.

**Mapped to continuity rule:** `Rule 3: Commit doctrine`.

## The 5 Foundation Lifecycle States

The continuity repo's Interpretation Protocol uses a 5-state anti-hallucination space (implemented / planned / designed / envisioned / researched). This foundation re-states the lifecycle as 5 foundation lifecycle states:

| # | State | Definition | Foundation usage |
|---|---|---|---|
| 1 | **Reality** | The repository's own operation (governance, cadence, ADR system, naming, tagging, commit doctrine) | This repository's own foundation doctrine |
| 2 | **Active Execution** | A canonical feature is currently being built (e.g., R1 of the rebuild) | (Will become active in R1) |
| 3 | **Approved Architecture** | The design is approved by the founder; the build is planned but not started | The 11-folder structure, the scaffolding placeholders, the recovery maps |
| 4 | **Strategic Vision** | Long-term direction in the canonical doctrine (e.g., multi-ARC ecosystem, civilization-scale framework) | The R4 multi-ARC plan |
| 5 | **Research & Exploration** | Investigated but not yet approved; not in the canonical | The 3 open founder decisions (D1, D2, D3) |

Every claim in every file in this repository MUST be locatable in this 5-state space.

## The Access Matrix (per the 7 Continuity Access Roles)

The continuity repo's `00-governance/GOVERNANCE.md` codifies 7 access roles. This foundation applies them:

| Role | Authority in this repository |
|---|---|
| Founder (Jan Blommaert) | Full read/write/push. Sole authority on all decisions. |
| Hermes (agent) | Read/write local; push requires founder approval. |
| ARC implementation agents | Read; write to feature branches only; no push to main. |
| External collaborators | Read-only (when remote is configured). |
| Public | Read-only (when remote is configured as public). |
| Auditors | Read-only. |
| Founders' designated delegates | Per founder authorization. |

## The 7 Execution Risks (from the Founder Capability Model)

The 7 execution risks are *re-stated* in `00-foundation/FOUNDATION.md` §"The 7 Execution Risks". This document is consistent with that section.

## The 3 Open Founder Decisions (blocking R1)

The 3 open founder decisions are *re-stated* in `00-foundation/FOUNDATION.md` §"The 3 Founder Decisions". This document is consistent with that section.

## What Comes Next

Per the founder's direction, this is **foundation only**. The runtime is not built. The next deliverables (after founder authorization) will be:

1. **Phase R1** — stand up the substrate in `07-runtime-scaffolding/` per the rebuild spec.
2. **Phase R2** — production governance hardening per the rebuild spec.
3. **Phase R3** — real execution & adaptive cognition per the rebuild spec.
4. **Phase R4** — multi-ARC foundations per the rebuild spec.

## Cross-References

- `00-foundation/FOUNDATION.md` — the foundation doctrine
- `00-foundation/INTERPRETATION-PROTOCOL.md` — the foundation interpretation protocol
- Canonical governance: `Javalin13/ryzen-continuity/blob/main/00-governance/GOVERNANCE.md`
- Founder Identity: `Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-IDENTITY.md`
- Founder Capability Model: `Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-CAPABILITY-MODEL.md`
- Interpretation Protocol (canonical): `Javalin13/ryzen-continuity/blob/main/00-governance/INTERPRETATION-PROTOCOL.md`
