# ADR TEMPLATE — Ryzen Core

```yaml
---
id: NNNN
title: <one-line title>
status: proposed | accepted | superseded-by-NNNN | deprecated
date: YYYY-MM-DD
decision_date: YYYY-MM-DD (when status moves to accepted)
decision_author: jan-blommaert (founder)
co_author: <hermes | other agent>
supersedes: <NNNN | none>
superseded_by: <NNNN | none>
related_adrs: <NNNN ... | none>
related_docs:
  - <path/to/relevant/doc>
  - ...
classification:
  <artifact>: <tier>
amendable: true-additively
---

# NNNN — <one-line title>

## Status

**Proposed** (or **Accepted** if founder has approved).

## Context

<What is the issue we're seeing that motivates this decision?>

<Reference the canonical doctrine, the recovery archive, the rebuild spec, or the runtime roadmap as appropriate.>

<The context should answer: "What forces are at play? What constraints exist? What is the situation?">

## Decision

<What is the change we're proposing or have agreed to implement?>

<The decision should be unambiguous and complete. A future reader should be able to read the decision and understand exactly what will be done.>

## Consequences

### Positive

<What becomes easier because of this decision?>

### Negative

<What becomes harder because of this decision?>

### Neutral

<What changes but is neither better nor worse?>

## Doctrine Compliance

### Founder Reality Check Protocol (7-dimension scorecard)

| Dimension | Score | Justification |
|---|---|---|
| Revenue potential | <Low/Medium/High> | <why> |
| Execution cost | <Low/Medium/High> | <why> |
| Time cost | <Low/Medium/High> | <why> |
| Complexity cost | <Low/Medium/High> | <why> |
| Opportunity cost | <Low/Medium/High> | <why> |
| Strategic alignment | <Low/Medium/High> | <why> |
| Current priority alignment | <Low/Medium/High> | <why> |

**Overall: <ACCEPT / DEFER / DECLINE>** (per the founder canonical).

### Interpretation Protocol (5-tier classification)

| Item | Tier | Justification |
|---|---|---|
| <item 1> | <tier> | <why> |

### Founder Capability Model (7 execution risks)

| Risk | Mitigation |
|---|---|
| <risk 1> | <mitigation> |

## Cross-References

- <path/to/relevant/doc>
- ...

---

## ADR Format Notes

- The **Status** field uses a fixed enum: `proposed | accepted | superseded-by-NNNN | deprecated`. (Per the continuity repo's lesson `2026-06-15-adr-status-enum`.)
- The **Context** section captures the *why* of the decision; the *what* is in the **Decision** section; the *so what* is in the **Consequences** section.
- The **Doctrine Compliance** section is *required* for every ADR. A Founder Reality Check scorecard is *required* for every ADR. (Per the continuity repo's lesson `2026-06-15-founder-reality-check-as-executable-guardrail`.)
- ADRs are **additive**: a new ADR never deletes or modifies an old ADR. Superseded ADRs are marked `superseded-by-NNNN`, not deleted.
- ADRs are **sequentially numbered**: 0001, 0002, 0003, ... (4-digit zero-padded). The sequence is **per-repository**: this is ADR 0001 of `ryzen-core`, not ADR 0007 of the ecosystem.
- ADR tags follow the pattern `decision-<NNNN>-<status>` (e.g., `decision-0001-accepted`).
