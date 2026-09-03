# ARC Productization — Commercial & Operational Accumulation

```yaml
---
type: arc-productization-index
status: active-accumulation
created: 2026-09-03
classification: strategic-vision + research-and-exploration
founder_direction: structure ARC pricing, costs, pilots, provisioning and capacity assumptions in Ryzen Core
runtime_implementation_authorized: false
amendable: true-additively
---
```

## Purpose

This folder is the canonical accumulation point in `ryzen-core` for the **productization of ARC nodes**: commercial packaging, pricing, cost model, pilot structure, provisioning requirements, capacity assumptions and lessons needed before ARC becomes a repeatable product.

It does **not** declare the Ryzen runtime implemented. It documents the business/product layer learned from the PRIME architecture and the first external ARC pilots.

## Current product thesis

- PRIME remains the founder's execution/operator node and is not itself the commercial ARC product.
- ARC nodes are intended to become personal/business operator nodes derived from repeatable infrastructure patterns proven through PRIME.
- Telegram is the initial interface for pilots; the own-platform layer remains future work.
- The commercial floor for a Standard ARC is currently **€500/year**.
- Monthly Standard is **€50/month** (€600/year), intentionally more expensive than annual billing.
- Founding pilots may receive a limited free period in exchange for real-world validation and feedback; free access must be time-bounded unless the Founder explicitly decides otherwise.
- Heavy customization, dedicated infrastructure, higher usage and business-critical integrations must move to higher tiers or separate implementation fees.

## Folder map

- `PRICING.md` — current ARC tier model and pricing principles.
- `COST-CAPACITY-MODEL.md` — known shared infrastructure costs, direct-vs-overhead distinction, capacity assumptions and margin guardrails.
- `PROVISIONING-BACKLOG.md` — what must be standardized/automated so ARC #10 costs much less founder time than ARC #1.
- `founding-pilots/VONKA.md` — first external Founding Pilot commercial structure and learning goals.

## Classification discipline

The files in this folder separate:

1. **Known current facts** — e.g. prices the Founder currently pays and commercial terms explicitly chosen.
2. **Working assumptions** — e.g. how many light ARCs may fit on one VPS; these require measurement.
3. **Commercial decisions** — current offer/pricing direction, amendable by Founder.
4. **Future design** — provisioning automation, tier isolation and dedicated infrastructure patterns not yet production-proven.

## Current strategic goal

Turn the PRIME-derived architecture into a repeatable ARC product without allowing support or customization effort to scale linearly with customer count.

The core productization rule is:

> **Standard ARC should become ~80–90% repeatable platform and ~10–20% customer configuration.**

Higher tiers may intentionally include more custom work because they carry higher commercial value.
