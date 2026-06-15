# 11 — Fleet ARC Intake (the Accumulation Layer)

```yaml
---
type: intake-folder
section: fleet-arc-intake
status: foundation-only
created: 2026-06-15
classification: research-and-exploration
related_founder_direction: 2026-06-15 (clarification: accumulation, not implementation)
amendable: true-additively
related_repo: Javalin13/ryzen-continuity
related_arc: FleetConnect (Javalin13/fleetconnect or local equivalent)
---

## Purpose

This folder (`11-fleet-arc-intake/`) is the **canonical intake point** for validated Fleet ARC discoveries. It is the *accumulation layer* that receives validated intelligence from FleetConnect (the first operational ARC domain) and from future ARCs as they emerge.

Per the founder's clarification 2026-06-15:

> Without a Ryzen implementation repository, these discoveries risk becoming fragmented across FleetConnect repositories, documents, conversations, and future AI sessions.
> The Ryzen Core Foundation Repository provides a durable implementation home for: Fleet ARC evolution, Recovered implementation knowledge, Runtime design decisions, Governance evolution, Future ARC development.
> The objective is not to build Ryzen today. The objective is to ensure that every future Fleet ARC discovery has a canonical location where it can accumulate and compound.
> The repository should therefore be designed as: A continuity and implementation foundation. Not as an active runtime development project.

This folder is the *operational form* of that objective.

## The 10 Intake Types (from the founder direction)

Per the founder's clarification 2026-06-15, the Fleet ARC will produce discoveries in 10 categories. Each category has a dedicated subdirectory:

| # | Subdirectory | What it receives |
|---|---|---|
| 1 | `01-dispatch-intelligence/` | Patterns, decisions, and learnings about *dispatching* (driver assignment, route optimization, timeline coordination) |
| 2 | `02-capacity-intelligence/` | Patterns, decisions, and learnings about *capacity* (driver availability, vehicle availability, supply matching) |
| 3 | `03-demand-intelligence/` | Patterns, decisions, and learnings about *demand* (booking patterns, customer behavior, seasonality) |
| 4 | `04-pricing-intelligence/` | Patterns, decisions, and learnings about *pricing* (rate cards, surge pricing, dynamic adjustments) |
| 5 | `05-supply-intelligence/` | Patterns, decisions, and learnings about *supply* (driver onboarding, vehicle procurement, supply expansion) |
| 6 | `06-operational-governance-patterns/` | Governance rules, validation gates, audit trails, escalation patterns that emerge from operational reality |
| 7 | `07-memory-requirements/` | Memory patterns: what needs to be remembered, for how long, at what layer (operational/strategic/creator/governance) |
| 8 | `08-verification-requirements/` | Verification patterns: what needs to be verified, how, with what level of recursion |
| 9 | `09-runtime-requirements/` | Runtime requirements: what the runtime must do to support FleetConnect's business |
| 10 | `10-arc-coordination-requirements/` | ARC coordination patterns: how Fleet ARC will interact with future ARCs (Earth, FamilieKompas) |

## The Intake Discipline

A discovery is *intake-worthy* if and only if it satisfies all 4 criteria:

1. **Validated.** The discovery has been observed in real FleetConnect operations (or in a FleetConnect simulation that the founder has accepted as evidence).
2. **Reusable.** The discovery is expected to recur or to inform future ARC design.
3. **Documented.** The discovery is captured in a structured format (the intake template, see below).
4. **Founder-accepted.** The founder (or a designated delegate) has accepted the discovery as a candidate for accumulation.

A discovery that does *not* satisfy all 4 criteria is **not** intake-worthy. It belongs in the FleetConnect repo, in conversation logs, in chat history — but not in this folder.

## The Intake Template (per discovery)

Every intake file in this folder follows the template at `09-cadences/fleet-arc-intake/TEMPLATE.md`. The template captures:

- **Discovery title** (one-line summary)
- **Date observed** (when the discovery was first made)
- **Source** (which FleetConnect repo, document, conversation, or AI session)
- **Validation evidence** (the data, observation, or simulation that supports the discovery)
- **Reusability argument** (why this discovery is expected to recur or to inform future ARC design)
- **Founder acceptance** (the founder's name + date + decision: accept / defer / decline)
- **Tier classification** (per the Interpretation Protocol: implemented / planned / designed / envisioned / researched)
- **Cross-references** (to the recovery archive, the rebuild spec, the runtime roadmap, etc.)
- **Status** (raw / validated / accepted / deprecated)

## The 5-State Lifecycle of an Intake

Every intake passes through 5 explicit lifecycle states:

1. **Raw** — the discovery is captured but not yet validated.
2. **Validated** — the discovery is supported by evidence; the founder has not yet accepted it.
3. **Accepted** — the founder has accepted the discovery for accumulation. The discovery is now durable.
4. **Promoted** — the accepted discovery has been promoted to a *design* (in the rebuild spec) or to a *runtime requirement* (in the runtime roadmap) or to a *governance rule* (in the foundation governance).
5. **Deprecated** — the accepted discovery is no longer valid (e.g., FleetConnect changed, the operational reality evolved, a better discovery superseded it). Deprecated intakes are *preserved* (additive only) but not removed.

A discovery that is **Raw** is not a foundation asset. A discovery that is **Validated** is a candidate. A discovery that is **Accepted** is a foundation asset. A discovery that is **Promoted** has crossed into the rebuild spec, the runtime roadmap, or the foundation governance. A discovery that is **Deprecated** is preserved for continuity but is no longer authoritative.

## What This Folder is NOT

This folder is **NOT**:

- ❌ A code repository. No runtime code is committed here. The folder holds *intake notes*, *validated discoveries*, and *accumulated intelligence* — not code.
- ❌ An active runtime development project. The runtime is deferred; this folder's purpose is accumulation, not implementation.
- ❌ A replacement for FleetConnect's own repositories. The FleetConnect repo is the operational home; this folder is the *accumulation home* for discoveries that emerge from FleetConnect but belong in the Ryzen continuity layer.
- ❌ A replacement for the recovery archive (in `ryzen-continuity/04-recovery-archive/`). The recovery archive is the *historical* home for the lost original runtime's recovered knowledge. This folder is the *forward-looking* home for *new* discoveries from FleetConnect and future ARCs.

## What This Folder IS

This folder **IS**:

- ✅ The **canonical intake point** for validated Fleet ARC discoveries.
- ✅ The **accumulation layer** that receives validated intelligence from FleetConnect and future ARCs.
- ✅ The **durable home** where discoveries compound over time without becoming fragmented.
- ✅ The **bridge** between FleetConnect's operational reality and the Ryzen continuity doctrine (in `ryzen-continuity/`).
- ✅ The **seedbed** for future runtime requirements, future governance evolution, and future ARC design.

## The Doctrine of Accumulation

The founder's clarification establishes a **doctrine of accumulation**:

> "The objective is to ensure that every future Fleet ARC discovery has a canonical location where it can accumulate and compound."

The doctrine has 4 rules:

1. **One canonical location per discovery type.** The 10 subdirectories are the canonical locations for the 10 intake types. No duplication, no fragmentation.
2. **One intake template per discovery.** Every intake follows the template. The template is the *contract* between the FleetConnect repo (the source) and this folder (the accumulation).
3. **Founder acceptance is required.** A discovery is not a foundation asset until the founder accepts it. Raw and validated discoveries are *candidates*; accepted discoveries are *assets*.
4. **Additive only.** Intakes are never deleted, never overwritten. Deprecated intakes are preserved for continuity.

## Cross-References

- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md` (will be created in this turn)
- Per-intake-type READMEs: `11-fleet-arc-intake/0X-*/README.md` (one per intake type)
- Intake log (index of accepted intakes): `11-fleet-arc-intake/INDEX.md` (will be created in this turn)
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Strategic posture clarification: ADR `0002-clarify-strategic-posture-deferred-accumulation-first.md`
- Continuity repo: `Javalin13/ryzen-continuity` (the canonical doctrine layer)
- FleetConnect canonical: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
