# 0002 — Clarify the Ryzen Core Foundation's Strategic Posture (Deferred; Accumulation-First)

```yaml
---
id: 0002
title: Clarify the Ryzen Core Foundation's Strategic Posture (Deferred; Accumulation-First)
status: accepted
date: 2026-06-15
decision_date: 2026-06-15
decision_author: jan-blommaert (founder)
co_author: hermes (drafting agent)
supersedes: none
superseded_by: none
related_adrs: 0001
related_docs:
  - 11-fleet-arc-intake/README.md
  - 00-foundation/FOUNDATION.md
  - 06-runtime-roadmap/ROADMAP.md
  - README.md
classification:
  foundation: approved-architecture
  intake-folder: research-and-exploration (active as accumulation layer)
  ryzen-runtime: deferred (not approved for immediate implementation)
  fleetconnect: reality (primary execution priority)
amendable: true-additively
replaced_runtime: original Ryzen implementation repository (lost)
related_repo_canonical: Javalin13/ryzen-continuity
related_arc: FleetConnect (primary execution priority #1)
```

# 0002 — Clarify the Ryzen Core Foundation's Strategic Posture

## Status

**Accepted.** Founder-authorized via direct clarification on 2026-06-15.

## Context

On 2026-06-15, the founder authorized the creation of the Ryzen Core Repository Foundation as the **durable implementation home** for future Ryzen runtime development (ADR 0001). The founder has now provided an additional clarification of the foundation's *strategic posture*.

The clarification refines the rationale. The original framing was "implementation successor to the lost runtime." The refined framing is:

> A Ryzen Core Foundation Repository is authorized.
> This authorization is not based on immediate Ryzen runtime implementation.
> This authorization exists for **continuity, accumulation, and future implementation readiness**.

The founder then named the **operational risk** that motivates the foundation:

> FleetConnect remains the primary execution priority. However, FleetConnect is also the first operational ARC domain. As FleetConnect evolves, valuable ARC intelligence will continue to emerge, including: dispatch intelligence, capacity intelligence, demand intelligence, pricing intelligence, supply intelligence, operational governance patterns, memory requirements, verification requirements, runtime requirements, ARC coordination requirements.
>
> Without a Ryzen implementation repository, these discoveries risk becoming fragmented across FleetConnect repositories, documents, conversations, and future AI sessions.

And the **objective**:

> The objective is not to build Ryzen today. The objective is to ensure that every future Fleet ARC discovery has a canonical location where it can accumulate and compound.
>
> The repository should therefore be designed as: A continuity and implementation foundation. Not as an active runtime development project.
>
> FleetConnect remains execution priority #1.
>
> Ryzen Core acts as the long-term accumulation layer that receives validated intelligence from Fleet ARC and future ARC domains.

This ADR adopts the refined framing as the **strategic posture of the foundation**, replacing (in posture, not in artifacts) the previous "implementation successor" framing with the more accurate "accumulation-first" framing.

## Decision

The founder clarified the foundation's posture with 3 specific changes:

### Decision D-2.1 — The Foundation's Active Purpose is Accumulation, Not Implementation

The foundation's *active* purpose is to **accumulate validated Fleet ARC discoveries** in a canonical location. The foundation's *latent* purpose (the implementation successor role) is preserved but is **deferred**.

The runtime is *not* built today. The runtime is *not* built in the next 12 months. The runtime is *not* the foundation's deliverable for 2026 or 2027. The runtime is the *future*; the accumulation is the *present*.

**Operational consequence:** The 10 scaffolding placeholders in `07-runtime-scaffolding/` and the 1 placeholder in `08-observability/` remain `status: NOT-IMPLEMENTED`. The 3 open founder decisions (D1, D2, D3) remain open. R1 is *not* imminent.

### Decision D-2.2 — A New Folder `11-fleet-arc-intake/` is Created

The foundation gains a new **12th top-level folder** (`11-fleet-arc-intake/`) that is the **canonical intake point** for validated Fleet ARC discoveries. This folder is *active* (it accepts new intake files) but *not implemented as a runtime component* (it is a documentation accumulation layer).

The folder has 10 subdirectories, one per intake type (per the founder's clarification):

| # | Subdirectory | What it receives |
|---|---|---|
| 1 | `01-dispatch-intelligence/` | Patterns, decisions, and learnings about dispatching |
| 2 | `02-capacity-intelligence/` | Patterns, decisions, and learnings about capacity |
| 3 | `03-demand-intelligence/` | Patterns, decisions, and learnings about demand |
| 4 | `04-pricing-intelligence/` | Patterns, decisions, and learnings about pricing |
| 5 | `05-supply-intelligence/` | Patterns, decisions, and learnings about supply |
| 6 | `06-operational-governance-patterns/` | Governance rules, validation gates, audit trails |
| 7 | `07-memory-requirements/` | Memory patterns, layer requirements, retention |
| 8 | `08-verification-requirements/` | Verification patterns, recursion levels, failure modes |
| 9 | `09-runtime-requirements/` | Performance, integration, concurrency, state, recovery |
| 10 | `10-arc-coordination-requirements/` | Cross-ARC intelligence, memory, governance, workflows |

Each subdirectory has a `README.md` that:
- Names what belongs in the directory
- Names what does NOT belong (code, duplicates, FleetConnect's operational home)
- Specifies the intake discipline (template, 5-state lifecycle, doctrine of accumulation)
- Specifies the file naming convention
- Cross-references the parent folder, the intake template, the intake log, the foundation doctrine, and the relevant canonical

### Decision D-2.3 — A New Cadence `fleet-arc-intake` is Added

The foundation gains a new **6th cadence** (`09-cadences/fleet-arc-intake/`) that holds the **intake template** (`TEMPLATE.md`). The intake template is the *contract* between the FleetConnect repo (the source) and this foundation (the accumulation).

The 6 cadences are now:
1. `09-cadences/daily-snapshots/` — daily cadence (unchanged)
2. `09-cadences/weekly-reviews/` — weekly cadence (unchanged)
3. `09-cadences/monthly-reviews/` — monthly cadence (unchanged)
4. `09-cadences/lessons-learned/` — lessons INDEX (unchanged)
5. `09-cadences/idea-backlog/` — idea backlog (unchanged)
6. **[ADDITIVE — 2026-06-15]** `09-cadences/fleet-arc-intake/` — Fleet ARC intake template (new)

The 6th cadence is **event-driven**, not time-driven. An intake is created when a Fleet ARC discovery is validated and founder-accepted, not on a daily/weekly/monthly schedule.

## Consequences

### Positive

- **Strategic posture clarified.** The foundation's active purpose is *accumulation*, not *implementation*. The Founder Reality Check Protocol's 7-dim scorecard for any *new* idea must include "is this a Fleet ARC discovery, or a runtime build?" — and if the latter, the idea is **deferred** until the founder explicitly authorizes the runtime phase.
- **Fragmentation risk mitigated.** Per the founder's clarification: "Without a Ryzen implementation repository, these discoveries risk becoming fragmented across FleetConnect repositories, documents, conversations, and future AI sessions." The new `11-fleet-arc-intake/` folder is the *single canonical location* for validated Fleet ARC discoveries. No fragmentation.
- **Doctrine-of-accumulation codified.** The 5-state lifecycle (Raw → Validated → Accepted → Promoted → Deprecated) + the founder-acceptance requirement + the additive-only discipline + the promotion rules (governance patterns to canonical governance, runtime requirements to rebuild spec) make the accumulation *governed*, not chaotic.
- **Cross-ARC future-proofing.** The 10th intake type (`10-arc-coordination-requirements/`) captures Fleet ARC's intelligence about how it will interact with future ARCs (Earth, FamilieKompas). When Earth ARC and FamilieKompas ARC are eventually built, the cross-ARC convergence protocol is *informed* by Fleet ARC's accumulated coordination intelligence.
- **Reuse of existing intake patterns.** The 4 criteria (Validated, Reusable, Documented, Founder-accepted) and the 5-state lifecycle are *consistent* with the continuity doctrine's Founder Reality Check Protocol and the Interpretation Protocol's 5-tier classification. No new doctrine is invented; existing patterns are applied.

### Negative

- **The foundation is now 12 folders, not 11.** The numbering convention (`00-foundation/` through `10-tools/`) is now broken: `11-fleet-arc-intake/` exists as the 12th folder. The numbering is *historical* (the first 11 folders were created in ADR 0001); the 12th is added *additively*. A future maintainer may find the inconsistency confusing.
  - **Mitigation:** The README documents the 12-folder structure; the 12th folder is the operational accumulation layer. The numbering inconsistency is *honest* (it reflects the additive evolution).
- **The intake discipline adds overhead.** Every Fleet ARC discovery must be *captured* (raw), *validated* (evidence), *founder-accepted* (decision), and *promoted* or *deprecated* (status). The discipline is *not* free; it costs time. But the alternative (fragmentation, lost discoveries, repeated conversations) is more expensive.
- **The 3 open founder decisions (D1, D2, D3) remain open.** They are not promoted, not demoted, not resolved. The accumulation-first posture does *not* require them; they remain open until the runtime phase begins (which is deferred per Decision D-2.1).

### Neutral

- **The 10 scaffolding placeholders in `07-runtime-scaffolding/` remain `NOT-IMPLEMENTED`.** The clarification does not change the runtime's "do not implement" boundary; it reinforces it.
- **The runtime roadmap in `06-runtime-roadmap/ROADMAP.md` is updated** to reflect the deferred posture. R1, R2, R3, R4 are *not* imminent. The roadmap is *latent* (it exists for future reference) but not *active* (no commitment to start R1 in any specific timeframe).
- **The continuity repo is unchanged.** The clarification is a *ryzen-core* posture; it does not modify the continuity doctrine.

## Doctrine Compliance

### Founder Reality Check Protocol (7-dimension scorecard)

| Dimension | Score | Justification |
|---|---|---|
| Revenue potential | Low (medium-term) | The accumulation is *foundational*; the revenue is in FleetConnect (which is the primary execution priority). The accumulation *enables* future revenue when the runtime is built. |
| Execution cost | Low | The intake folder is 10 READMEs + 1 parent README + 1 INDEX + 1 template = 13 new files. No code. No infrastructure. |
| Time cost | Low | No daily/weekly/monthly commitment; intake is event-driven. |
| Complexity cost | Low | The 5-state lifecycle is consistent with the existing doctrine. The 4-criteria intake discipline is consistent with the Founder Reality Check. No new patterns. |
| Opportunity cost | Low | Does not block FleetConnect's Q3 2026 focus; in fact, the intake folder *supports* FleetConnect by capturing its discoveries. |
| Strategic alignment | High | Aligns exactly with the founder's clarification: "The objective is to ensure that every future Fleet ARC discovery has a canonical location where it can accumulate and compound." |
| Current priority alignment | High | FleetConnect is the primary execution priority #1. The intake folder is the *companion* to FleetConnect, not a replacement. |

**Overall: ACCEPT.** The 7-dimension scorecard is overwhelmingly positive. The intake folder is the right scope, the right sequence, the right discipline.

### Interpretation Protocol (5-tier classification)

| Item | Tier | Justification |
|---|---|---|
| Foundation (ADR 0001) | approved-architecture | The foundation is approved; the design is in place. |
| Intake folder (`11-fleet-arc-intake/`) | research-and-exploration (active as accumulation layer) | The folder is *active* for accumulation; the discoveries are research-and-exploration. They become promoted assets only when the founder accepts them. |
| Intake subdirectories (10) | research-and-exploration (active as accumulation subdirs) | Same as above; each is a sub-classification for the 10 intake types. |
| 10 scaffolding placeholders in `07-runtime-scaffolding/` | approved-architecture (deferred) | The placeholders are approved; the runtime is deferred. |
| 3 open founder decisions (D1, D2, D3) | research-and-exploration (open) | Unchanged. |
| Runtime roadmap (R1–R4) | approved-architecture (deferred) | The roadmap is approved as a *future* path; not active. |
| Continuity repo | reality | Unchanged. |
| Recovery archive | approved-architecture-with-historical-evidence | Unchanged. |
| Rebuild spec | planning-artifact | Unchanged. |
| Original runtime | lost | Unchanged. |

### Founder Capability Model (7 execution risks)

| Risk | Mitigation |
|---|---|
| Opportunity overload | The scope is fixed by the founder direction. The intake folder is *bounded* (10 subdirectories). No new opportunities added. |
| Scope expansion | The "do not implement" list (5 items) is unchanged. The intake folder is a *documentation* layer, not a *code* layer. |
| Context switching | The 6 cadences are the focus: daily, weekly, monthly, lessons, idea-backlog, fleet-arc-intake. The intake cadence is event-driven, not time-driven; it does not compete with the other 5. |
| Premature ecosystem expansion | The foundation is for Ryzen Core + Fleet ARC intake only. No Earth ARC, no FamilieKompas ARC, no multi-ARC, no ecosystem. |
| Over-architecture | The 10 intake subdirectories are *minimal*. Each has a single purpose. Each README is concise. |
| Commercial delay | The foundation does not delay FleetConnect; the intake folder *supports* FleetConnect. |
| Insufficient focus | The 10 intake types are the focus. The doctrine of accumulation is the discipline. |

**Overall: ACCEPT.** All 7 execution risks are explicitly mitigated.

## The Founder Direction (verbatim, 2026-06-15)

> A Ryzen Core Foundation Repository is authorized.
> This authorization is not based on immediate Ryzen runtime implementation.
> This authorization exists for continuity, accumulation, and future implementation readiness.
>
> Additional rationale:
> FleetConnect remains the primary execution priority.
> However, FleetConnect is also the first operational ARC domain.
> As FleetConnect evolves, valuable ARC intelligence will continue to emerge, including: dispatch intelligence, capacity intelligence, demand intelligence, pricing intelligence, supply intelligence, operational governance patterns, memory requirements, verification requirements, runtime requirements, ARC coordination requirements.
>
> Without a Ryzen implementation repository, these discoveries risk becoming fragmented across FleetConnect repositories, documents, conversations, and future AI sessions.
>
> The Ryzen Core Foundation Repository provides a durable implementation home for: Fleet ARC evolution, Recovered implementation knowledge, Runtime design decisions, Governance evolution, Future ARC development.
>
> Repository creation is authorized.
> Runtime implementation remains deferred.
>
> The objective is not to build Ryzen today.
> The objective is to ensure that every future Fleet ARC discovery has a canonical location where it can accumulate and compound.
>
> The repository should therefore be designed as: A continuity and implementation foundation. Not as an active runtime development project.
>
> FleetConnect remains execution priority #1.
> Ryzen Core acts as the long-term accumulation layer that receives validated intelligence from Fleet ARC and future ARC domains.

## What Changes in the Foundation (per this ADR)

| File | Change |
|---|---|
| `README.md` | Re-framed: "Ryzen Continuity & Accumulation Foundation" + Fleet ARC accumulation as the active purpose |
| `00-foundation/FOUNDATION.md` | Added: *Strategic Posture* section (deferred, accumulation-first) |
| `06-runtime-roadmap/ROADMAP.md` | Updated: Phase 0 in progress; R1+ deferred; intake-first path |
| `05-adrs/INDEX.md` | Updated: ADR 0002 added (this ADR) |
| `05-adrs/0002-clarify-...md` | NEW: this ADR |
| `11-fleet-arc-intake/` | NEW: 12th top-level folder (parent README + 10 subdirectories + INDEX) |
| `11-fleet-arc-intake/INDEX.md` | NEW: intake log (additive, empty for now) |
| `11-fleet-arc-intake/01-dispatch-intelligence/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/02-capacity-intelligence/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/03-demand-intelligence/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/04-pricing-intelligence/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/05-supply-intelligence/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/06-operational-governance-patterns/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/07-memory-requirements/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/08-verification-requirements/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/09-runtime-requirements/README.md` | NEW: per-intake-type README |
| `11-fleet-arc-intake/10-arc-coordination-requirements/README.md` | NEW: per-intake-type README |
| `09-cadences/fleet-arc-intake/TEMPLATE.md` | NEW: 6th cadence (event-driven, not time-driven) |

## What Does NOT Change

- The 10 scaffolding placeholders in `07-runtime-scaffolding/` — still `NOT-IMPLEMENTED`
- The 1 placeholder in `08-observability/` — still `NOT-IMPLEMENTED`
- The 3 open founder decisions (D1, D2, D3) — still open
- The 0X–10X folder numbering — preserved (the 12th folder is a *historical anomaly*, not a re-numbering)
- The continuity repo (Javalin13/ryzen-continuity) — unchanged
- The recovery archive — unchanged
- The rebuild spec — unchanged

## Cross-References

- ADR 0001: `05-adrs/0001-establish-ryzen-core-repository-foundation.md` (the original foundation establishment)
- Intake folder: `11-fleet-arc-intake/`
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Runtime roadmap: `06-runtime-roadmap/ROADMAP.md`
- Canonical FleetConnect: `Javalin13/ryzen-continuity/blob/main/04-fleetconnect/FLEETCONNECT-CANONICAL.md`
- Canonical recovery archive: `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/`
- Canonical rebuild spec: `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md`

## Next Steps After This ADR

1. **Founder action:** Create the GitHub remote (e.g., `https://github.com/Javalin13/ryzen-core`) and provision a credential.
2. **Founder action:** Push the local repository to the remote.
3. **Founder action:** Begin accumulating validated Fleet ARC discoveries in `11-fleet-arc-intake/0X-<intake-type>/`.
4. **Founder action:** When the runtime phase begins (separately authorized via a new ADR), promote the accumulated discoveries to the rebuild spec, the runtime roadmap, or the foundation governance.

**Until those steps are taken, the foundation is the *accumulation layer*, not the *implementation project*.**
