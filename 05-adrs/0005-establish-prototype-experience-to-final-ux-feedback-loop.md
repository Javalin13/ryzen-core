# 0005 — Establish Prototype Experience → Final ARC UX/System Feedback Loop

```yaml
---
id: 0005
title: Establish Prototype Experience → Final ARC UX/System Feedback Loop
status: accepted
date: 2026-09-03
decision_date: 2026-09-03
decision_author: jan-blommaert (founder)
co_author: luxcalibur
supersedes: none
superseded_by: none
related_adrs: 0003, 0004
related_docs:
  - CURRENT-REALITY-2026-09.md
  - REPOSITORY-MAP.md
  - 12-arc-productization/prototype-experience/README.md
  - 12-arc-productization/prototype-experience/EXPERIENCE-BACKLOG.md
  - 12-arc-productization/prototype-experience/UX-FEED-CONTRACT.md
  - 12-arc-productization/PROVISIONING-BACKLOG.md
classification: approved-product-process + active-accumulation
amendable: true-additively
---
```

## Status

**Accepted.** Founder explicitly directed on 2026-09-03 that experience accumulated by ARC prototypes must be kept in a backlog and later directly feed the final ARC UX/system, and authorized applying the broader repo improvements identified in the prior review.

## Context

The Ryzen Core foundation historically accumulated architecture and Fleet ARC intelligence, while the September 2026 productization layer added pricing, costs, provisioning and the VONKA Founding Pilot.

A missing link remained: real prototype experience could otherwise disappear into conversations, support interventions or individual memory. That would create a final ARC UX designed from theory despite having access to real user evidence.

At the same time, June 2026 documents describe an earlier state in which runtime work was deferred and the repository had fewer top-level accumulation domains. PRIME and the external ARC pilot direction create a newer operational reality that should overlay—not erase—the historical record.

## Decision

1. Establish `12-arc-productization/prototype-experience/` as the canonical cross-pilot experience accumulation layer.
2. Maintain a structured `EXPERIENCE-BACKLOG.md` using `EXP-*` records.
3. Require reusable pilot experience to follow the lifecycle:
   `usage → capture → classify → generalize → validate → design-candidate → implement → re-test`.
4. Require final ARC UX/system design to trace major requirements back to prototype evidence or an explicit Founder decision.
5. Preserve customer confidentiality by promoting generalized patterns, not private customer content.
6. Add `CURRENT-REALITY-2026-09.md` and `REPOSITORY-MAP.md` so future agents interpret historical roadmap/folder-count statements through the current operational state.
7. Do not build a full ARC Factory merely because the feedback system exists; product/runtime implementation still follows evidence and Founder authorization.

## Consequences

### Positive

- Prototype experience becomes a durable product asset.
- The final ARC UX/system can be evidence-led rather than assumption-led.
- Support burden, onboarding friction and user trust issues become measurable design inputs.
- Successful behaviors are preserved instead of focusing only on failures.
- Historical doctrine remains intact while current reality becomes easy to navigate.

### Negative

- Pilots create documentation discipline in addition to technical work.
- The backlog can become noisy if every preference is promoted without validation.
- Experience records require confidentiality discipline.

### Neutral

- A repeated request is not automatically a feature.
- Higher-tier/custom needs may remain outside Standard even when users request them.
- The final UX remains future work; this ADR governs how evidence will feed it.

## Doctrine Compliance

### Founder Reality Check Protocol

| Dimension | Score | Justification |
|---|---|---|
| Revenue potential | High | Better UX, lower support burden and clearer tier boundaries improve scalable recurring revenue |
| Execution cost | Low | Primarily documentation/process now |
| Time cost | Low-Medium | Requires ongoing pilot capture discipline |
| Complexity cost | Low | One canonical backlog and feed contract prevents scattered learning |
| Opportunity cost | Low | Uses learning from work already being done |
| Strategic alignment | High | Converts ARC prototypes into compounding Ryzen knowledge |
| Current priority alignment | High | Directly supports VONKA and future ARC pilots |

**Overall: ACCEPT.**

### Interpretation Protocol

| Item | Tier | Justification |
|---|---|---|
| Experience capture process | approved-product-process | Founder explicitly authorized |
| Individual raw experience | research-and-exploration | Observation until validated |
| Recurring validated pattern | product-design-candidate | Evidence supports broader consideration |
| Final ARC UX/system | strategic vision / future implementation | Not yet frozen or implemented |
| PRIME operational evidence | reality/active execution | Current working source of reusable patterns |
| VONKA experience | active commercial experiment | External pilot evidence when usage begins |

### Founder Capability Model risks

| Risk | Mitigation |
|---|---|
| Opportunity overload | Backlog captures ideas without requiring immediate implementation |
| Scope expansion | Promotion threshold separates preference from product requirement |
| Context switching | One canonical cross-pilot experience layer |
| Premature ecosystem expansion | Evidence first; factory/runtime not auto-authorized |
| Over-architecture | Only repeated/critical patterns are promoted |
| Commercial delay | UX/support learning occurs during real pilots, not before them |
| Insufficient focus | Priority order starts with safety, reliability and core-task blockers |

## Cross-References

- `CURRENT-REALITY-2026-09.md`
- `REPOSITORY-MAP.md`
- `12-arc-productization/README.md`
- `12-arc-productization/PROVISIONING-BACKLOG.md`
- `12-arc-productization/prototype-experience/`
- `12-arc-productization/founding-pilots/VONKA.md`
