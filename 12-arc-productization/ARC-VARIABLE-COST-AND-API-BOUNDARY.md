# ARC Variable-Cost & API Boundary

```yaml
---
type: commercial-cost-governance-standard
status: founder-directed-current
created: 2026-09-11
classification: commercial-governance + cost-control + integrations
currency: EUR
amendable: true-additively
---
```

## Purpose

Prevent an ARC owner, employee, customer, automation, Brain, Agent or preferred platform connection from creating uncontrolled third-party or model-provider costs for RYZ3N.

The number of integrations included in a commercial tier describes how many systems may be configured. It does **not** mean that RYZ3N accepts unlimited third-party subscriptions, API calls, message fees, map/search fees, storage fees, payment fees or other variable vendor charges.

## Non-negotiable rule

> **No customer-controlled action may create uncapped variable spend for RYZ3N by default.**

Every cost-bearing provider path must use one of these models:

1. **customer-owned billing** — preferred for paid third-party SaaS/API services;
2. **RYZ3N-included bounded allowance** — only where an explicit written allowance/budget exists;
3. **pre-approved add-on** — customer agrees price/cap before activation;
4. **blocked/no-cost mode** — connector may remain connected but cost-bearing calls stop when the approved budget is exhausted.

No silent pay-as-you-go pass-through and no silent RYZ3N-funded overage.

## Integration entitlement is not vendor-fee entitlement

Examples:

- Google Drive connection may count as one integration, but any paid Google Workspace/provider plan remains the customer's responsibility unless explicitly included.
- WhatsApp/SMS/telephony connection may count as one integration, but message/number/telephony charges require customer-owned billing or an explicit capped allowance.
- Maps/geocoding/search/data APIs may count as one integration, but paid requests are not unlimited merely because the connector is included.
- CRM/accounting/dispatch APIs may count as one integration, but vendor subscriptions, premium API access and transaction fees remain outside the ARC subscription unless explicitly included.
- Payment processing fees are never absorbed merely because an ARC can interact with a payment platform.

## Default billing ownership

For third-party services that can generate usage-based cost, preferred architecture is:

`customer chooses service → customer owns/authorizes vendor account and billing → ARC receives scoped credentials/connector access → ARC uses service within customer-approved permissions`

RYZ3N should not become the default financial guarantor for a customer's optional provider choices.

Where customer-owned billing is impossible or commercially undesirable, the Founder must approve a bounded RYZ3N-funded allowance before the cost-bearing connector is enabled.

## AI/model-provider boundary

AI/model usage is the exception that is deliberately bundled into ARC commercial tiers through **ARC Usage Units (AU)**.

AU is a cost-normalized capacity meter rather than a raw-token promise because model prices differ substantially.

Current internal normalization:

> **1 AU = €0.001 of provider-list-price-equivalent AI consumption.**

Current launch AI envelopes:

- Standard: **5,000 AU/month = €5 normalized AI allowance**;
- Pro: **15,000 AU/month = €15 normalized AI allowance**;
- Business: **30,000 AU/month = €30 normalized AI allowance**;
- Dedicated: **100,000 AU/month = €100 normalized AI allowance baseline**;
- Enterprise: custom.

The customer may receive many more raw tokens on efficient models than on premium models. Premium-model use therefore consumes AU faster rather than creating open-ended extra cost.

RYZ3N may route tasks to an appropriate lower-cost model where quality remains sufficient.

## Ollama/cloud-spend controls

Where Ollama Cloud is used:

- included subscription credits are treated as the first capacity pool;
- automatic customer-caused paid overage/top-up must be disabled or otherwise hard-capped where the provider permits;
- when the pooled allowance nears exhaustion, PRIME/OMEGA should warn, optimize, route, defer non-critical work, allocate another approved pool or require a commercial capacity decision;
- an ARC may never autonomously purchase additional provider credits;
- customers may not select premium models in a way that bypasses their AU allowance;
- model selection is a capability/quality choice inside the commercial allowance, not an unlimited cost entitlement.

Current public Ollama pricing checked 2026-09-11: Pro is $20/month with $60 monthly usage credits and 3 concurrent requests; Max is $100/month with $300 monthly usage credits and 10 concurrent requests. Provider pricing may change and must be re-checked before relying on it for future economics.

## Third-party API call guardrail

By default, **variable third-party API spend included in Standard/Pro/Business is €0 unless the commercial agreement explicitly lists an included vendor-cost allowance.**

This does not mean integrations are unusable. Free-tier/free-call APIs may operate normally, and customer-funded APIs may operate within the customer's own provider account.

If RYZ3N chooses to include a paid external API allowance for a customer, the agreement/config must record:

- provider/service;
- monthly euro ceiling;
- call/message/transaction ceiling where useful;
- warning threshold;
- hard-stop behavior;
- whether unused allowance rolls over (default: no);
- whether customer-owned billing takes over above the cap.

At 80% of any RYZ3N-funded variable-cost allowance, warn. At 100%, stop cost-bearing calls unless a Founder-approved higher cap already exists.

## User-selected platform rule

A customer may prefer a platform that is more expensive than the default supported option. That preference does not automatically change ARC economics.

Before enabling a cost-bearing preferred platform:

1. identify vendor subscription and variable usage fees;
2. choose customer-owned billing or a priced RYZ3N allowance;
3. define API/call/message limits;
4. define credentials and data boundaries;
5. record the commercial treatment;
6. only then enable the connection.

If a cheaper supported platform can satisfy the same outcome, RYZ3N may recommend it, but the customer may still choose the more expensive option if they accept its cost treatment.

## Automation / runaway-spend protection

Every recurring or autonomous workflow that can call a paid provider must have:

- per-run call ceiling where technically possible;
- monthly cost/usage ceiling;
- retry ceiling;
- loop/runaway detection;
- concurrency limit;
- fail-closed behavior when budget is exhausted;
- audit/telemetry sufficient to attribute spend to the ARC.

Retries caused by ARC logic count against the relevant allowance. Engineering defects causing pathological retries must be corrected and should not be treated as a reason to surprise-bill the customer.

## KMS7 specific boundary

If KMS7 activates at the €170/month Founding Business exception:

- Business AI allowance applies: **30,000 AU/month = €30 normalized provider-list-price-equivalent AI allowance**;
- third-party variable API/vendor spend is **not unlimited** and is customer-funded by default unless the accepted KMS7 scope explicitly states that a specific vendor allowance is included;
- Founder target remains **≤€50/month total direct operational cost**;
- therefore any RYZ3N-funded third-party allowance must fit inside the remaining direct-cost headroom after model and infrastructure allocation;
- no ARC/Agent may autonomously buy credits, paid seats, phone numbers, message packs, storage or other vendor capacity.

## Customer-facing wording

Preferred plain-language explanation:

> **Your ARC subscription includes a defined AI allowance and a defined number of integrations. Third-party services you connect may have their own subscription or usage fees. We never let your ARC create surprise third-party charges for RYZ3N or silently pass them to you: paid connections use your provider account or a clearly agreed capped allowance.**

## Founder shorthand

> **Integrations are included; somebody else's API bill is not automatically included. AI is bundled through AU. Every other variable-cost provider is customer-funded or hard-capped before the ARC can spend. No agent gets an open wallet.**

## Founder free-model runtime invariant — 2026-09-12

This section is a binding Founder clarification of the AI/model-provider boundary for **PRIME, Hermes, OMEGA-supervised ARC runtimes, every current ARC, every Brain/Agent that can select a model, and every future ARC produced by the ARC Factory**.

Runtime model selection is **free-only unless the Founder explicitly authorizes a paid route**. "Prefer free" is not sufficient.

Machine-readable operating invariants:

```text
FREE_ENDPOINT_REQUIRED = true
PAID_MODEL_FALLBACK_ALLOWED = false
AUTONOMOUS_BILLING_CHANGES_ALLOWED = false
AUTONOMOUS_CREDIT_PURCHASE_ALLOWED = false
PAID_OVERRIDE_AUTHORITY = founder_explicit_only
```

Required behavior:

- a model/provider route must be verified as a free endpoint/model route at selection time before it is eligible for autonomous use;
- no ARC, Brain, Agent, PRIME, Hermes or OMEGA process may autonomously enable billing, pay-as-you-go, a paid tier, subscription upgrade, top-up, credit purchase or paid-only endpoint;
- no automatic fallback chain may cross from a free route into a paid route;
- a provider's retirement, EOL, HTTP 404/410, loss of free status, quota change or capability loss must trigger selection of another **verified free** route, not paid escalation;
- deterministic model-retirement/EOL errors should not be repeatedly retried as if transient; move to the next eligible free route or fail closed;
- if no verified free route can satisfy the required capability, the ARC/runtime must enter a truthful blocked/degraded state and escalate to the Founder; it must **never create cost by itself**;
- among eligible free routes, selection should maximize the capabilities actually required by the task and then maximize useful context window, reasoning/tool quality and reliability;
- capability routing is allowed and encouraged: an ARC may use one free model as its primary long-context brain and another free model for a specialist modality such as video, provided both remain inside the same free-only boundary;
- image/video/multimodal requirements must not be solved by silently purchasing a paid model;
- model names are replaceable runtime choices, not permanent canon: if a stronger suitable free route appears, it may replace the current free route under normal verification/change control without weakening this financial invariant.

Existing AU, capacity-pool and paid-provider economics in this document remain useful for commercial planning and for any **Founder-explicitly-approved** paid capacity. They do **not** grant autonomous authority to move a runtime onto paid inference. A commercial allowance is not itself permission for an ARC to spend it without an approved provider route.

> **Hard rule: free model routes only by default; maximize capability inside the free boundary; if free cannot do the job, stop and ask the Founder rather than spend.**
