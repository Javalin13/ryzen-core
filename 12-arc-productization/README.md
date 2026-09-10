# ARC Productization — Commercial & Operational Accumulation

```yaml
---
type: arc-productization-index
status: active-accumulation
created: 2026-09-03
updated: 2026-09-10
classification: strategic-vision + research-and-exploration
founder_direction: structure ARC pricing, costs, pilots, provisioning, capacity assumptions, commercialization and prototype experience in RYZ3N Core
runtime_implementation_authorized: false
amendable: true-additively
---
```

## Purpose

This folder is the canonical accumulation point in `ryzen-core` for the **productization of ARC nodes**: commercial packaging, pricing, cost model, pilot structure, provisioning requirements, capacity assumptions, go-to-market, operating responsibilities, prototype experience and lessons needed before ARC becomes a repeatable product.

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
- The current first paid validation strategy is **Founding 20**: up to 20 paying entrepreneurs recruited primarily through trusted/direct channels, with a working €49/month founding rate locked while continuously subscribed.
- The Founding-20 price is a launch-cohort offer; it does not replace the normal Standard €50/month or €500/year pricing.
- Standard should promise predictable included normal usage under fair use, **not unlimited AI** and not silent pass-through API/model bills.
- Broad paid advertising should be scaled only after early customers prove repeatable onboarding, usage, retention, support burden and unit economics.
- Founding pilots may receive a limited free period in exchange for real-world validation and feedback; free access must be time-bounded unless the Founder explicitly decides otherwise.
- Heavy customization, dedicated infrastructure, higher usage and business-critical integrations must move to higher tiers or separate implementation fees.
- ARC commercialization now uses a Founder-directed **V1→V6 maturity journey**: Foundation → Operations → Specialist → Golden Recursive ARC → Platinum/JARVIS Presence → Sovereign Gamified Ecosystem.
- Billing tier and maturity tier are distinct: paying more may unlock resources/scope, but it may never buy a false maturity aura.
- Every ARC may reuse validated capability modules, Brain contracts, Agent patterns and generalized lessons from the wider ARC network without inheriting another owner's private memory/data/secrets.
- ARC **form/look** is owner-selectable and factory-resettable, but the **aura/shine is maturity-derived and cannot be manually changed by a cosmetic reset**.
- If a sale/transfer includes a real capacity/competence/owner-state reset that leaves the ARC effectively empty, the ARC returns to **V1 Foundation with the V1 Blue aura**.
- **Every meaningful prototype experience must be captured and made available to the final ARC UX/system design.**
- **No critical reusable operating knowledge should remain only in PRIME runtime memory; reusable patterns must become structured RYZ3N-readable knowledge.**

## Folder map

- `ARC-A2Z-ALIGNMENT-MAP-2026-09-10.md` — current cross-repo authority map aligning RYZ3N canon, PRIME stewardship, VONDA/Golden Blueprint, commercialization, pricing, usage, maturity, capacity, team roles, communication and scale gates.
- `ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md` — canonical actionable go-to-market: positioning, benchmark snapshot, Founding 20, usage/fair-use policy, capacity/commercial triggers, team responsibilities, KPIs, paid-ad scale gates and immediate execution sequence.
- `PRICING.md` — current ARC tier model, Founding-20 launch price, usage promise and pricing principles.
- `COST-CAPACITY-MODEL.md` — known shared infrastructure costs, direct-vs-overhead distinction, capacity assumptions, telemetry requirements and margin guardrails.
- `PROVISIONING-BACKLOG.md` — what must be standardized/automated so ARC #10 costs much less Founder time than ARC #1.
- `ARC-V1-V6-COMMERCIAL-MATURITY-TUTORIAL.md` — customer/commercial maturity journey, visual shine progression, V4 recursive-cognition threshold, V5 JARVIS-style presence, V6 gamified ecosystem, and privacy-safe reuse of validated modules/Brains across the ARC legion.
- `ARC-FORM-AURA-AND-TRANSFER-RESET-STANDARD.md` — Founder-directed separation of ARC form/look from maturity aura, factory-form reset invariance, transfer-reset semantics, and the rule that an emptied transferred ARC returns to V1/Blue.
- `ARC-BRAIN-INTERCONNECT-AND-PRIME-STEWARDSHIP.md` — bounded Brain interconnect and stewarded cross-ARC convergence rules.
- `ARC-BRAIN-SPECIALIZATION-REGISTRY.md` — evidence-driven Brain specialization and reusable Brain contract rules.
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
3. **Commercial decisions** — current offer/pricing direction and maturity packaging, amendable by Founder.
4. **Future design** — provisioning automation, tier isolation and dedicated infrastructure patterns not yet production-proven.
5. **Prototype evidence** — real user/operator experience that may become a reusable product requirement after validation.
6. **Launch experiments** — commercial hypotheses such as Founding-20 acquisition, which must be judged by conversion, retention, support burden and unit economics rather than enthusiasm alone.

## Prototype learning doctrine

The prototype phase is not only for proving that an ARC runs. It must reveal how people actually experience it and which runtime contracts are genuinely reusable.

The feedback loop is:

`ARC prototype → lived experience + operational evidence → backlog → recurring/reusable pattern → RYZ3N-readable standard candidate → UX/system design candidate → later implementation → re-validation`.

A useful experience must not disappear into chat history or anecdotal memory. Customer-specific confidential data stays private; only the generalized reusable lesson is promoted.

The current runtime prototype must also preserve the canonical convergence discipline through local mission state, checkpoints, decisions, lessons, drift evidence, verification and continuation state so that future RYZ3N ingestion/migration does not require architectural reinvention.

## Commercial maturity doctrine

The ARC product should be understandable as an evolution path rather than a feature dump:

`V1 Blue/Foundation → V2 Cyan/Operations → V3 Violet/Specialist → V4 Gold/Recursive Cognition → V5 Platinum/JARVIS Presence → V6 Sovereign/Prismatic Gamified Ecosystem`.

The shine/aura is a visible maturity indicator and must follow verified capability, not marketing alone. The Owner may reset or change the ARC's visual form without changing that aura. Only a real lifecycle maturity change may alter the aura; an ARC that is transferred and genuinely emptied of the state/competence supporting its prior maturity returns to V1/Blue.

A new ARC is not built from zero. It receives the proven shared platform and can adopt reusable validated modules from the ARC network. Cross-ARC reuse is capability federation, not private-memory federation: **share capability, not private payload**.

## Commercialization doctrine

The current go-to-market rule is:

> **Do not sell the infrastructure. Sell the operating partner.**

The launch sequence is:

`VONDA real proof → Founding 20 direct/referral customers → measurable usage/retention/support/unit economics → proof assets + organic demos → small paid acquisition tests → scale only retained-customer acquisition`.

The first buyer is deliberately narrow: AI-aware solo entrepreneurs and very small business owners who value an AI operating partner but do not want to manage servers, Hermes installation, Telegram bot plumbing, API keys, model/provider accounts or technical failure modes themselves.

## Current operating roles

- **Founder** — final product/commercial authority, early sales/customer discovery, pricing exceptions, strategic approvals and scale decisions.
- **PRIME** — implementation/provisioning/runtime/capacity/isolation steward; no authority to invent prices or commercial promises.
- **Luxcalibur** — independent strategy/benchmarking/productization reviewer and Founder→GitHub doctrine bridge; not a canonical ARC parent or customer product.
- **Customer ARC** — isolated customer-facing runtime operating only inside its authorized scope.
- **Future human functions** — onboarding/customer success, support/ops, sales/growth, finance/admin, legal/privacy and infrastructure/security; no named assignment without explicit Founder confirmation.

## Current strategic goal

Turn the PRIME-derived architecture into a repeatable ARC product and a transferable prototype of the future RYZ3N ↔ ARC operating model, without allowing support or customization effort to scale linearly with customer count.

The core productization rule is:

> **Standard ARC should become ~80–90% repeatable platform and ~10–20% customer configuration.**

The core architecture and business rules are:

> **Build once, instantiate many. Customize by configuration, not by architectural fork.**

> **An ARC is an autonomous runtime node under supervision, not a chat branch pretending to be autonomous.**

> **Every ARC grows individually, while the legion learns collectively through reusable, privacy-safe modules and validated Brains.**

> **Predictable subscription for normal use; telemetry protects both customer experience and unit economics.**

Higher tiers may intentionally include more custom work because they carry higher commercial value.