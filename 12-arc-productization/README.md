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

It does **not** declare the RYZ3N runtime implemented. It documents the business/product layer learned from the PRIME architecture and external ARC pilots.

## Current product thesis

- PRIME remains the Founder's execution/operator node and is not itself the commercial ARC product.
- ARC nodes are intended to become personal/business operator nodes derived from repeatable infrastructure patterns proven through PRIME.
- A client ARC is an **autonomous runtime node under PRIME supervision**, not merely another chat/session inside PRIME's own client runtime.
- For early pilots, PRIME and client ARC nodes may share one physical VPS host, but each ARC should have its **own Hermes runtime/service identity, gateway lifecycle, channel adapter, workspace, memory, secrets, logs, checkpoints and restart boundary**.
- The current PRIME + autonomous ARC runtime model is a **bounded prototype of the future RYZ3N ↔ ARC operating model**, not a competing ecosystem hierarchy.
- PRIME currently bootstraps/supervises the runtime patterns; mature RYZ3N is intended to inherit native orchestration, governance, provisioning, continuity and cross-ARC coordination while PRIME becomes supervisor/mentor/execution steward.
- Telegram is the initial interface for pilots; the own-platform/final UX layer remains future work. ARC identity and state must remain channel-independent.
- ARC runtime contracts should become replicable: shared template + isolated client configuration/state, not bespoke architectural forks.
- Same VPS is allowed for proven early isolation; **same runtime identity is not**.
- ARC nodes should be portable later to dedicated VPS infrastructure without conceptual redesign.
- The commercial floor for a Standard ARC is currently **€500/year**.
- Monthly Standard is **€50/month** (€600/year), intentionally more expensive than annual billing.
- Founding pilots may receive a limited free period in exchange for real-world validation and feedback; free access must be time-bounded unless the Founder explicitly decides otherwise.
- Heavy customization, dedicated infrastructure, higher usage and business-critical integrations must move to higher tiers or separate implementation fees.
- **Every meaningful prototype experience must be captured and made available to the final ARC UX/system design.**
- **No critical reusable operating knowledge should remain only in PRIME runtime memory; reusable patterns must become structured RYZ3N-readable knowledge.**

## Folder map

- `PRICING.md` — current ARC tier model and pricing principles.
- `COST-CAPACITY-MODEL.md` — known shared infrastructure costs, direct-vs-overhead distinction, capacity assumptions and margin guardrails.
- `PROVISIONING-BACKLOG.md` — what must be standardized/automated so ARC #10 costs much less Founder time than ARC #1.
- `PRIME-RYZ3N-ARC-PROTOTYPE-DOCTRINE.md` — additive doctrine aligning today's PRIME-mediated ARC prototypes with the canonical RYZ3N hierarchy, convergence model, future native orchestration, replication contracts, operational logs/checkpoints and PRIME knowledge-transfer role.
- `AUTONOMOUS-ARC-NODE-RUNTIME.md` — Founder runtime standard: each client ARC is an autonomous Hermes-based child runtime under PRIME supervision, with independent gateway/service, channel adapter, state, secrets, logs, checkpoints and future dedicated-VPS portability.
- `founding-pilots/` — external Founding Pilot commercial structure and learning goals; VONDA is the current first external proving node.
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

The prototype phase is not only for proving that an ARC runs. It must reveal how people actually experience it and which runtime contracts are genuinely reusable.

The feedback loop is:

`ARC prototype → lived experience + operational evidence → backlog → recurring/reusable pattern → RYZ3N-readable standard candidate → UX/system design candidate → later implementation → re-validation`.

A useful experience must not disappear into chat history or anecdotal memory. Customer-specific confidential data stays private; only the generalized reusable lesson is promoted.

The current runtime prototype must also preserve the canonical convergence discipline through local mission state, checkpoints, decisions, lessons, drift evidence, verification and continuation state so that future RYZ3N ingestion/migration does not require architectural reinvention.

## Current strategic goal

Turn the PRIME-derived architecture into a repeatable ARC product and a transferable prototype of the future RYZ3N ↔ ARC operating model, without allowing support or customization effort to scale linearly with customer count.

The core productization rule is:

> **Standard ARC should become ~80–90% repeatable platform and ~10–20% customer configuration.**

The core architecture rules are:

> **Build once, instantiate many. Customize by configuration, not by architectural fork.**

> **An ARC is an autonomous runtime node under supervision, not a chat branch pretending to be autonomous.**

Higher tiers may intentionally include more custom work because they carry higher commercial value.
