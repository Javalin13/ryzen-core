# ARC Productization — Commercial & Operational Accumulation

```yaml
---
type: arc-productization-index
status: active-accumulation
created: 2026-09-03
classification: strategic-vision + research-and-exploration
founder_direction: structure ARC pricing, costs, pilots, provisioning, capacity assumptions and prototype experience in Ryzen Core
runtime_implementation_authorized: false
amendable: true-additively
---
```

## Purpose

This folder is the canonical accumulation point in `ryzen-core` for the **productization of ARC nodes**: commercial packaging, pricing, cost model, pilot structure, provisioning requirements, capacity assumptions, prototype experience and lessons needed before ARC becomes a repeatable product.

It does **not** declare the Ryzen runtime implemented. It documents the business/product layer learned from the PRIME architecture and external ARC pilots.

## Current product thesis

- PRIME remains the Founder's execution/operator node and is not itself the commercial ARC product.
- ARC nodes are intended to become personal/business operator nodes derived from repeatable infrastructure patterns proven through PRIME.
- Telegram is the initial interface for pilots; the own-platform/final UX layer remains future work.
- The commercial floor for a Standard ARC is currently **€500/year**.
- Monthly Standard is **€50/month** (€600/year), intentionally more expensive than annual billing.
- Founding pilots may receive a limited free period in exchange for real-world validation and feedback; free access must be time-bounded unless the Founder explicitly decides otherwise.
- Heavy customization, dedicated infrastructure, higher usage and business-critical integrations must move to higher tiers or separate implementation fees.
- **Every meaningful prototype experience must be captured and made available to the final ARC UX/system design.**

## Folder map

- `PRICING.md` — current ARC tier model and pricing principles.
- `COST-CAPACITY-MODEL.md` — known shared infrastructure costs, direct-vs-overhead distinction, capacity assumptions and margin guardrails.
- `PROVISIONING-BACKLOG.md` — what must be standardized/automated so ARC #10 costs much less Founder time than ARC #1.
- `founding-pilots/VONKA.md` — first external Founding Pilot commercial structure and learning goals.
- `prototype-experience/README.md` — doctrine for accumulating lived ARC prototype experience.
- `prototype-experience/EXPERIENCE-BACKLOG.md` — canonical cross-pilot experience backlog.
- `prototype-experience/TEMPLATE.md` — standard experience record.
- `prototype-experience/UX-FEED-CONTRACT.md` — rules for converting validated pilot experience into final ARC UX/system requirements.

## Classification discipline

The files in this folder separate:

1. **Known current facts** — e.g. prices the Founder currently pays and commercial terms explicitly chosen.
2. **Working assumptions** — e.g. how many light ARCs may fit on one VPS; these require measurement.
3. **Commercial decisions** — current offer/pricing direction, amendable by Founder.
4. **Future design** — provisioning automation, tier isolation and dedicated infrastructure patterns not yet production-proven.
5. **Prototype evidence** — real user/operator experience that may become a reusable product requirement after validation.

## Prototype learning doctrine

The prototype phase is not only for proving that an ARC runs. It must reveal how people actually experience it.

The feedback loop is:

`ARC prototype → lived experience → backlog → recurring/reusable pattern → UX/system design candidate → later implementation → re-validation`.

A useful experience must not disappear into chat history or anecdotal memory. Customer-specific confidential data stays private; only the generalized reusable lesson is promoted.

## Current strategic goal

Turn the PRIME-derived architecture into a repeatable ARC product without allowing support or customization effort to scale linearly with customer count, while ensuring the eventual final ARC UX/system is built from real prototype evidence.

The core productization rule is:

> **Standard ARC should become ~80–90% repeatable platform and ~10–20% customer configuration.**

Higher tiers may intentionally include more custom work because they carry higher commercial value.
