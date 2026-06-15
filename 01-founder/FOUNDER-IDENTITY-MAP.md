# Founder Identity Map (this repository → canonical)

```yaml
---
type: founder-integration
section: founder-identity-map
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
canonical_ref: Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-IDENTITY.md
amendable: true-additively
```

## Purpose

This document is a **map** from this repository (`ryzen-core`) to the canonical Founder Identity Profile v1.0 in the `ryzen-continuity` repository. It captures *which canonical founder facts* are relevant to this implementation-successor repository, and *how* this repository honors them.

**The Founder Identity Profile v1.0 is the source of truth.** This map is a *navigation aid* for future maintainers and agents. When this map disagrees with the canonical, the canonical wins.

## The Founder Identity Facts Relevant to This Repository

The canonical Founder Identity Profile v1.0 codifies a specific set of facts about Jan Blommaert (John Dough / King John Dough), the founder. The following facts are *directly relevant* to the implementation of the Ryzen Core runtime:

### Fact F-1 — Founder Identity

The founder is **Jan Blommaert**, Belgian, multilingual. He is the **Founder-Architect** — a person who designs systems, architectures, and leverage, not tools. His work is organized around 22 high-value capability domains and 9 cognitive advantages. His learning model is **Learn → Connect → Integrate → Operationalize → Scale**.

**How this repository honors F-1:** The 11-folder structure is *systems-oriented*, not *tool-oriented*. The folders organize around capabilities (foundation, founder, ryzen, recovery, rebuild, ADRs, roadmap, scaffolding, observability, cadences, tools) — the *capability stack* — not around tools (Python, FastAPI, PostgreSQL). The 7 doctrine rules (in `00-foundation/GOVERNANCE.md`) are *systems* (governance, recovery, ADR, naming, tagging, commit, interpretation), not *tool features*.

### Fact F-2 — Executive Operating Profile

The founder operates as **Strategic Advisor, Executive Architect, Systems Designer, Business Analyst, Operations Partner, Automation Coordinator, Continuity Guardian**. The Executive Amplification Directive is: **Ideas → Plans → Systems → Operations → Revenue → Durable Assets**.

**How this repository honors F-2:** The 11-folder structure mirrors the Executive Amplification chain:
- `02-ryzen/` = the System (the design)
- `04-rebuild-integration/` = the Plan (the rebuild spec integration)
- `06-runtime-roadmap/` = the Operations (the 4-phase rebuild sequence)
- `07-runtime-scaffolding/` = the future Revenue (R1–R4 will produce the revenue-producing runtime)
- `00-foundation/` + `09-cadences/` + `10-tools/` = the Durable Assets (the foundation, the cadences, the tools that outlast any specific runtime version)

The Continuity Guardian role is honored by the **Recovery Archive integration** (`03-recovery-integration/`) — the durable home for the lost runtime's recovered knowledge.

### Fact F-3 — 7 Execution Risks (the real risks)

The 7 execution risks are **opportunity overload, scope expansion, context switching, premature ecosystem expansion, over-architecture, commercial delay, insufficient focus**. These are the *real* risks, not intelligence/creativity/architecture/vision.

**How this repository honors F-3:** The 7 risks are *operationalized* as 7 foundation guards in `00-foundation/FOUNDATION.md` §"The 7 Execution Risks". Each guard has a specific mitigation in this repository's design. The "do not implement" list (Kernel runtime, Memory Federation, ARC Runtime, Governance Middleware, Agent Runtime) is a *hard scope expansion guard*. The 11-folder structure is a *context switching guard*. The 4-phase rebuild sequence is a *premature ecosystem expansion guard*.

### Fact F-4 — Interpretation Protocol

The founder's interpretation protocol is: **reality > doctrine, implementation > aspiration, evidence > theory**. The anti-hallucination rule is the 5-state space: **implemented / planned / designed / envisioned / researched**.

**How this repository honors F-4:** The foundation interpretation protocol (`00-foundation/INTERPRETATION-PROTOCOL.md`) re-states the 3 operational rules and the 5-tier classification, and applies them to *this* repository. The 5-state anti-hallucination space is operationalized in the protocol's "How to Use This Protocol" section.

### Fact F-5 — Priority Hierarchy

The founder's priority hierarchy is: **FleetConnect (top) → Earth → FamilieKompas → Ryzen Expansion**. FleetConnect is the primary operational priority.

**How this repository honors F-5:** The `06-runtime-roadmap/` explicitly maps the R1 → R2 → R3 → R4 phases to FleetConnect operational outcomes. R1 produces the substrate; R2 produces the production governance; R3 produces the real FleetConnect deployment. FleetConnect is *the* commercial vehicle that the runtime serves.

### Fact F-6 — The Identity + Capability Model Are Siblings

The canonical doctrine establishes: **Identity + Capability Model are SIBLING canonicals**. The Identity answers "who is the founder?" The Capability Model answers "how does the founder operate?" The two are not parent and child.

**How this repository honors F-6:** This folder (`01-founder/`) has two files:
- `FOUNDER-IDENTITY-MAP.md` (this file) — the map to the canonical Identity
- `CAPABILITY-MAP.md` (next file) — the map to the canonical Capability Model

The two are siblings, not parent and child. The repository honors the founder's own structure.

## What This Map Does NOT Do

This map does **not**:

- ❌ Duplicate the canonical Founder Identity Profile. The canonical is in continuity.
- ❌ Add new founder facts that are not in the canonical.
- ❌ Re-classify the canonical as "draft" or "superseded."
- ❌ Add new execution risks that are not in the canonical Capability Model.

The map is **observational**, not **additive**. It maps; it does not extend.

## When to Update This Map

This map should be updated when:

1. The canonical Founder Identity Profile is updated (new version, new amendment, new fact).
2. The Founder Capability Model is updated (new version, new amendment, new fact).
3. The 22 capability domains, the 9 cognitive advantages, or the 7 execution risks change.
4. The Executive Amplification Directive changes.
5. The Founder Reality Check Protocol changes.

In all cases, the update is **additive**: add a new section documenting the change, never delete the old section.

## Cross-References

- `01-founder/CAPABILITY-MAP.md` — the sibling map to the canonical Capability Model
- `00-foundation/FOUNDATION.md` — the foundation doctrine (which references the founder's execution risks)
- Canonical Founder Identity Profile: `Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-IDENTITY.md`
- Canonical Founder Capability Model: `Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-CAPABILITY-MODEL.md`
