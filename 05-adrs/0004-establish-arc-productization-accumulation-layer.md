# 0004 — Establish ARC Productization Accumulation Layer

```yaml
---
id: 0004
title: Establish ARC Productization Accumulation Layer
status: accepted
date: 2026-09-03
decision_date: 2026-09-03
decision_author: jan-blommaert (founder)
co_author: luxcalibur
supersedes: none
superseded_by: none
related_adrs: 0001, 0002, 0003
related_docs:
  - 12-arc-productization/README.md
  - 12-arc-productization/PRICING.md
  - 12-arc-productization/COST-CAPACITY-MODEL.md
  - 12-arc-productization/PROVISIONING-BACKLOG.md
  - 12-arc-productization/founding-pilots/VONKA.md
classification: approved-architecture for accumulation structure; strategic-vision/research for pricing and capacity hypotheses
amendable: true-additively
---
```

## Status

**Accepted.** Founder directly instructed on 2026-09-03 to inspect the existing Ryzen repository and structure the new ARC pricing, cost, capacity, pilot and provisioning information into the correct repository locations.

## Context

`ryzen-core` was originally established as a continuity and accumulation foundation, with Fleet ARC discoveries as the first active accumulation stream. Since then, the Founder has proven a much more operational PRIME architecture on VPS/Telegram and has begun using that pattern as the basis for an external ARC prototype.

The first external Founding Pilot, VONKA, creates a new class of validated accumulation that is not purely Fleet dispatch intelligence and does not belong inside `11-fleet-arc-intake/`: commercial packaging, recurring pricing, cost allocation, capacity assumptions, provisioning repeatability, pilot boundaries and customer-support economics.

These facts should accumulate without falsely declaring the Ryzen runtime implemented.

## Decision

Create `12-arc-productization/` as an additive top-level accumulation layer for ARC commercial/product-operating knowledge.

The folder will hold:

- commercial pricing and tier hypotheses;
- known shared infrastructure costs and direct-vs-overhead accounting logic;
- capacity assumptions that require measurement;
- provisioning/scaling backlog;
- Founding Pilot records and learnings;
- future productization lessons that do not belong in Fleet-specific intake.

This decision does **not** authorize building the deferred Ryzen runtime or a full ARC Factory. Productization documentation and pilot learning may proceed; runtime implementation remains separately governed.

## Current Founder-directed commercial baseline

- ARC Standard floor: **€500/year**.
- ARC Standard monthly: **€50/month**.
- Higher tiers remain working commercial hypotheses until validated.
- Founding pilots may receive time-limited free usage.
- VONKA: first 6 months free, then €500/year or €50/month if continued; basic website offered free with indicative value €250; personal onboarding €100; FR↔NL interpretation attendance €100 per requested appointment.

## Consequences

### Positive

- ARC economics and product-learning now have a canonical home.
- Fleet-specific intake remains clean and domain-focused.
- The repository can accumulate commercial proof without pretending the runtime exists.
- Standardization needs become explicit before customer count grows.
- Pricing is separated from unproven infrastructure assumptions.

### Negative

- Adds another top-level folder to a structure whose historical numbering is already additive/inconsistent.
- Creates a new information stream that must be kept disciplined to avoid premature product expansion.
- Commercial hypotheses may change quickly as pilots generate evidence.

### Neutral

- Historical folders and ADRs remain untouched.
- `ryzen-continuity` remains the canonical continuity/doctrine sibling.
- FleetConnect remains an important operational source of validated ARC intelligence, but not the only future ARC productization source.

## Doctrine Compliance

### Founder Reality Check Protocol

| Dimension | Score | Justification |
|---|---|---|
| Revenue potential | High | Creates a durable model for recurring ARC monetization |
| Execution cost | Low | Documentation/accumulation only |
| Time cost | Low | Small structured repo addition |
| Complexity cost | Low-Medium | Adds one top-level accumulation domain |
| Opportunity cost | Low | Supports a real external pilot without authorizing runtime expansion |
| Strategic alignment | High | Directly supports ARC productization from proven PRIME patterns |
| Current priority alignment | Medium-High | Enables external pilot while preserving FleetConnect/runtime boundaries |

**Overall: ACCEPT.**

### Interpretation Protocol

| Item | Tier | Justification |
|---|---|---|
| New folder structure | approved-architecture | Founder explicitly authorized the structure addition |
| €500/year Standard floor | strategic/commercial decision | Founder-directed current price floor |
| €50/month Standard | strategic/commercial decision | Founder-directed current monthly alternative |
| Higher-tier prices | research-and-exploration | Working hypotheses, not market validated |
| 10 ARCs per 4GB VPS | research-and-exploration | Planning assumption requiring measurement |
| VONKA pilot | active commercial experiment | Proposal sent; client feedback pending |
| Ryzen runtime | NOT IMPLEMENTED | Unchanged |

### Founder Capability Model risks

| Risk | Mitigation |
|---|---|
| Opportunity overload | Productization stays in documentation/pilot-learning mode |
| Scope expansion | No full ARC Factory or runtime implementation authorized |
| Context switching | ARC product knowledge gets one canonical folder |
| Premature ecosystem expansion | Pilot-driven evidence before automation scale |
| Over-architecture | Provisioning backlog explicitly says automate repeated/safety-critical patterns only |
| Commercial delay | Pricing and conversion path are documented now |
| Insufficient focus | Standard tier and VONKA pilot are narrow first proof points |

## Cross-References

- `12-arc-productization/README.md`
- `12-arc-productization/PRICING.md`
- `12-arc-productization/COST-CAPACITY-MODEL.md`
- `12-arc-productization/PROVISIONING-BACKLOG.md`
- `12-arc-productization/founding-pilots/VONKA.md`
- `11-fleet-arc-intake/`
- `Javalin13/ryzen-continuity`
