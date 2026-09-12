# ARC Tier Entitlements & Resource Governance

```yaml
---
type: commercial-entitlement-standard
status: founder-directed-current
created: 2026-09-11
updated: 2026-09-12
classification: commercial-pricing + resource-governance
currency: EUR
supersedes_owner_ai_usage_caps: true
supersedes_owner_ai_limit_messages: true
local_first_arc_inference: true
amendable: true-additively
---
```

> **Legacy filename retained for reference stability. Current policy no longer uses Owner-facing AI usage caps for Standard/Pro/Business ARCs.**

## Purpose

Define current commercial entitlements for ARC Standard, Pro, Business, Dedicated and Enterprise while separating customer value from internal model/provider metering.

Billing tier remains separate from ARC maturity V1→V6. Paying for a larger entitlement does not buy maturity or aura.

Canonical companion standards:

- `ARC-ROLE-TAXONOMY-AND-ENTITLEMENT-LIMIT-MESSAGING-STANDARD.md`
- `ARC-CAPACITY-FALLBACK-TEMPORARY-DOWNGRADE-AND-LOCAL-INFERENCE-STANDARD.md`
- `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`

## 1. Current inference principle

- PRIME alone uses Ollama Cloud MiniMax M3 as its normal primary cloud route.
- Owner-facing ARCs use the verified shared local model as their normal primary route.
- ARCs may use Founder-authorized verified-free external fallbacks if the local route is unavailable.
- ARC Owners are not shown daily/weekly/monthly AI usage caps or reset messages.
- Internal calls/tokens/cost-equivalent telemetry remains available for economics and capacity planning.

## 2. AU becomes internal telemetry only

AU may remain as an internal normalization tool for historical comparison and cost-equivalent telemetry:

> **1 AU = €0.001 of provider-list-price-equivalent AI consumption.**

AU is **not** currently an Owner-facing entitlement, billing meter, hard-stop, or reset counter for local-first ARCs.

Do not show AU balances or AI-consumption reset windows to Owners unless a future explicit Founder decision reintroduces them.

## 3. Current tier ladder

Prices remain the current working launch prices pending Step 17B telemetry refinement.

| Tier | Current price | Managed ARC storage | AI service | Capacity weight | Authorized users | Primary channels | Integrations | Active automations | Infrastructure |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
| **ARC Standard** | **€50/month or €500/year** | **2 GB** | shared local inference included; no Owner-facing AI usage cap | **1 slot** | **1** | **1** | **2** | **5** | shared local |
| **ARC Pro** | **€120/month or €1,200/year** | **5 GB** | shared local inference included; no Owner-facing AI usage cap | **3 slots** | **3** | **2** | **5** | **15** | shared local / higher service allocation to be telemetry-calibrated |
| **ARC Business** | **€250/month or €2,500/year** | **15 GB** | shared local inference included; no Owner-facing AI usage cap | **6 slots** | **10** | **3** | **10** | **40** | shared business pool or isolated placement when needed |
| **ARC Dedicated** | **from €5,000/year** | **50 GB baseline** | dedicated/contract-defined inference | dedicated | **25** | **5** | **20** | **100** | dedicated resources/VPS where required |
| **ARC Enterprise** | **custom; working floor ~€10,000/year** | custom | custom / contract-defined | custom/dedicated | custom | custom | custom | custom | dedicated / multi-ARC / SLA as contracted |

These are commercial/service entitlements, not claims of infinite simultaneous compute.

## 4. What tiers can differentiate on

Without using Owner-facing model-call quotas, Standard / Pro / Business may differentiate through:

- managed storage;
- authorized users;
- channels;
- integrations;
- automations;
- support/service level;
- queue/concurrency priority;
- advanced features/capabilities;
- shared vs isolated placement;
- dedicated compute where contracted;
- future SLA/availability guarantees.

Exact queue/concurrency/service-priority differences must be based on real telemetry before being promised publicly.

## 5. No AI usage-limit warnings

For local-first Owner ARCs:

- no 80% AI-usage warning;
- no 100% AI hard-stop message;
- no daily/weekly/monthly AI reset message;
- no provider-credit or provider-session message;
- no AI-usage upsell triggered by model consumption.

If shared local capacity is busy, queue safely where possible.

If all authorized inference routes are unavailable, show only a sanitized temporary service-unavailable message.

This does not remove security, abuse, safety, or infrastructure-protection controls.

## 6. Shared-capacity weight model

Until telemetry proves another safe ceiling:

> **maximum 10 Standard-equivalent weighted slots per shared local inference/VPS capacity pool.**

Weights remain planning values:

- Standard = 1;
- Pro = 3;
- Business = 6;
- Dedicated = separate/dedicated;
- Enterprise = custom.

The weights are not Owner AI quotas. They help PRIME/OMEGA decide when to split, isolate or expand infrastructure.

Split earlier when actual latency, RAM, disk, queue depth, concurrency or local-model pressure requires it.

## 7. Internal economics relationship

RYZ3N must still measure the real economics of local-first service:

- local CPU/RAM/runtime consumption;
- VPS allocation;
- storage;
- queue/concurrency pressure;
- calls/tokens per Owner;
- free external fallback frequency;
- PRIME cloud cost separately from ARC local cost;
- support/incident burden;
- third-party integration spend actually funded by RYZ3N.

Step 17B uses this evidence to refine prices and service allocation. Public prices never change automatically.

## 8. Managed ARC storage

Managed ARC storage is customer-specific persistent storage controlled by the ARC/RYZ3N service, including retained uploads, workspace files, generated retained assets, customer-specific state stored as files/data and persistent caches.

External data remaining in Google Drive, OneDrive/Dropbox, CRM, dispatch or another connected SaaS does not automatically count as ARC storage. Persistent ARC-side copies do count.

Shared VPS capacity must preserve OS/log/recovery/model headroom. Logical customer storage entitlement is not a promise that every maximum quota will physically reside on one VPS simultaneously.

## 9. Integration entitlement vs third-party cost

Local inference does not create an open wallet for other vendors.

For Standard/Pro/Business:

- paid third-party subscription/API/message/transaction cost is customer-funded by default;
- RYZ3N-funded variable third-party spend is €0 by default unless a written capped allowance exists;
- free-tier/free-call integrations may operate normally;
- no ARC/Brain/Agent may autonomously purchase credits, seats, message packs, storage or provider capacity;
- any RYZ3N-funded external allowance must warn/hard-stop according to that specific external allowance, not according to ARC AI usage.

## 10. Definitions

### Integration

One independently configured external system/service connection requiring durable credentials/configuration. Multiple workflows inside one configured integration do not automatically count as separate integrations.

### Active automation

A persistent recurring, triggered or condition-based workflow configured to run without the Owner manually initiating each execution. One-off multi-step Agent work is not automatically an active automation.

### Primary channel

A persistent Owner-facing interface such as Telegram, web chat, WhatsApp, email gateway or later native ARC interface.

## 11. Founding Pilot rule

Current direction:

- VONDA ARC: six-month free Founding Pilot on Standard;
- NARC: six-month free Founding Pilot on Standard;
- Standard pilot includes 2 GB storage, 1 user, 1 channel, 2 integrations and 5 active automations;
- local AI interaction is included without an Owner-facing AI usage cap;
- pilots may upgrade commercial scope without affecting evidence-derived V1→V6 maturity.

A free pilot still does **not** imply unlimited third-party vendor spend, unlimited storage, unlimited users/integrations/automations or infinite simultaneous compute.

## 12. KMS7 Founding Business exception

If Adnan accepts and the Founder authorizes KMS7 ARC creation:

- price: **€170/month**;
- entitlement: **ARC Business**;
- 15 GB managed ARC storage;
- up to 10 users;
- 3 channels;
- 10 integrations;
- 40 active automations;
- local AI interaction included without an Owner-facing AI usage cap;
- capacity weight: 6 shared slots, with earlier isolation/splitting if telemetry requires it;
- normal future Business price remains €250/month or €2,500/year.

Founder working direct-operational-cost ceiling for KMS7 remains **≤€50/month**.

Third-party variable API/vendor costs remain customer-funded by default unless a specific capped KMS7 vendor allowance is explicitly included.

## 13. Capacity and technical-safety relationship

No Owner-facing AI cap does not mean infinite simultaneous compute.

OMEGA/PRIME may:

- queue workloads;
- prioritize interactive work over background work;
- isolate heavy workloads;
- move an ARC to a different local pool/VPS;
- require Dedicated infrastructure for structurally heavy workloads;
- apply security/abuse/safety protections.

These are infrastructure/service controls, not "you used too much AI" messages.

## 14. Customer-facing presentation

At minimum, onboarding/account surfaces should show:

- current tier;
- price/billing arrangement;
- managed storage included/used;
- authorized users;
- channels;
- integrations;
- automations;
- upgrade options;
- relevant service/support level;
- clear separation of third-party provider fees from the ARC subscription.

Do **not** show:

- AI token balances;
- AU balances;
- daily/weekly/monthly AI reset clocks;
- provider IDs;
- local model details;
- HTTP/provider errors;
- PRIME's Ollama subscription state.

## 15. Review rule

Review Standard/Pro/Business economics using real telemetry from VONDA, NARC, Cargo, KMS7 and later cohorts.

A future Founder-approved revision may change prices, service priority, resource allocation or tier structure when production evidence justifies it.

Any future reintroduction of Owner-facing AI quotas requires a new explicit Founder directive; telemetry alone cannot create them.

## Founder shorthand

> **PRIME pays for premium cloud intelligence; ARCs run local-first. Owners do not see AI usage-limit counters or reset messages. Standard/Pro/Business remain commercial tiers differentiated by service scope/resources, while telemetry measures the real economics behind the scenes.**
