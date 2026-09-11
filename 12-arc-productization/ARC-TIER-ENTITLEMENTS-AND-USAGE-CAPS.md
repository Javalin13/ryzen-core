# ARC Tier Entitlements & Usage Caps

```yaml
---
type: commercial-entitlement-standard
status: founder-directed-current
created: 2026-09-11
updated: 2026-09-11
classification: commercial-pricing + usage-governance
currency: EUR
supersedes_conflicting_fair_use_deferral: true
supersedes_raw-token-au-definition: true
amendable: true-additively
---
```

## Purpose

Define explicit commercial usage/entitlement limits for ARC Standard, Pro, Business, Dedicated and Enterprise so customers can understand what each package includes and PRIME/OMEGA can meter capacity consistently without exposing RYZ3N to uncontrolled provider cost.

Billing tier remains separate from ARC maturity V1→V6. Paying for a larger entitlement does not buy maturity or aura.

## Important correction — AU is cost-normalized, not raw-token based

The earlier v1.0 draft defined AU as approximately 1,000 model tokens. That is superseded.

Different cloud models have radically different per-token prices. A fixed-token allowance would either be unnecessarily restrictive on efficient models or financially unsafe on premium models.

Current internal normalization:

> **1 ARC Usage Unit (AU) = €0.001 of provider-list-price-equivalent AI consumption.**

AU therefore meters **normalized AI cost/capacity**, not a guaranteed raw token count.

The customer experiences a monthly AI allowance. The internal meter converts actual provider usage into AU according to the model/provider's current metered cost. A premium model consumes AU faster; an efficient model delivers materially more tokens/work for the same AU budget.

## Commercial entitlement matrix — corrected launch model

| Commercial tier | Current price | Managed ARC storage | Monthly AI allowance | Normalized AI value | Capacity weight | Authorized users | Primary channels | External integrations | Active automations | Infrastructure |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **ARC Standard** | **€50/month or €500/year** | **2 GB** | **5,000 AU/month** | **€5** | **1 slot** | **1** | **1** | **2** | **5** | shared |
| **ARC Pro** | **€120/month or €1,200/year** | **5 GB** | **15,000 AU/month** | **€15** | **3 slots** | **3** | **2** | **5** | **15** | shared / higher allowance |
| **ARC Business** | **€250/month or €2,500/year** | **15 GB** | **30,000 AU/month** | **€30** | **6 slots** | **10** | **3** | **10** | **40** | shared business pool or isolated placement when needed |
| **ARC Dedicated** | **from €5,000/year** | **50 GB included baseline** | **100,000 AU/month** | **€100 baseline** | **dedicated** | **25** | **5** | **20** | **100** | dedicated resources/VPS where required |
| **ARC Enterprise** | **custom; working floor ~€10,000/year** | **custom** | **custom** | **custom** | **custom/dedicated** | **custom** | **custom** | **custom** | **custom** | dedicated / multi-ARC / SLA as contracted |

These are launch entitlements, not claims about hard technical maximums of Hermes, Ollama, VPS infrastructure or model providers.

## Why the AU levels are higher than the first draft

Current Ollama public pricing checked on 2026-09-11 shows large model-price variation. Examples include inexpensive models below $1 per million tokens for many input/output patterns and premium models with substantially higher output pricing.

Therefore a Standard €5 normalized AI envelope can represent many millions of tokens on efficient models but far fewer on a premium model. This is intentional: **the package promises useful AI capacity, not an economically unsafe fixed quantity of premium-model tokens.**

The ARC/RYZ3N runtime may route ordinary work to a cost-efficient model when quality remains adequate and reserve premium models for tasks where the additional capability is justified.

## Shared-capacity weight model

The current Founder safety doctrine remains a maximum of **10 Standard-equivalent capacity slots per shared model/VPS pool until telemetry proves another safe ceiling**.

Commercial weights:

- Standard = **1 slot**;
- Pro = **3 slots**;
- Business = **6 slots**;
- Dedicated = separate/dedicated placement by default;
- Enterprise = custom.

Illustrative valid 10-slot mixes:

- 10 Standard = 10 slots;
- 3 Pro + 1 Standard = 10 slots;
- 1 Business + 1 Pro + 1 Standard = 10 slots;
- 1 Business + 4 Standard = 10 slots.

This slot system is a planning/safety model, not a claim that all workload combinations have identical CPU/RAM/concurrency characteristics. PRIME/OMEGA may split earlier when telemetry shows pressure.

## Current Ollama economics alignment — 2026-09-11

Current public Ollama pricing at the time of this correction:

- Pro: **$20/month**, including **$60/month usage credits**, **3 concurrent requests**;
- Max: **$100/month**, including **$300/month usage credits**, **10 concurrent requests**;
- Team: **$500/month**, including **$1,000/month shared usage credits**.

At the 2026-09-11 USD→EUR rate used for this assessment, $60 is approximately €51.72.

That makes the current Standard-weight design economically coherent as a launch model:

`10 Standard × €5 normalized AI allowance = €50 normalized monthly model usage`

which fits just below one current Ollama Pro plan's approximately €51.72 included usage-credit value.

The subscription fee itself is still a platform cost and concurrency may require earlier pool splitting. Do not assume unused provider credits can always be perfectly allocated, and do not assume Ollama pricing will remain unchanged.

Existing/legacy Ollama account pricing may differ from the current public new-plan pricing. Actual account billing must be checked before migration or plan changes.

## Managed ARC storage definition

Managed ARC storage is the customer-specific persistent storage controlled by the ARC/RYZ3N service for items such as:

- retained uploads;
- ARC workspace files;
- generated documents/assets intentionally retained;
- customer-specific structured memory/state where stored as files/data;
- cached working data retained beyond a transient execution window.

The following do **not** automatically count against managed ARC storage when they remain in their original external system:

- Google Drive files;
- OneDrive/Dropbox files;
- CRM records;
- dispatch-system records;
- customer website-hosting assets held outside the ARC workspace;
- other connected SaaS data.

If external data is copied, mirrored or persistently cached into the ARC workspace, the copied ARC-side amount counts toward the storage allowance.

The current shared VPS baseline is approximately 40 GB storage. Customer storage entitlements are logical service limits, not a promise that every customer's maximum quota can reside simultaneously on one 40 GB VPS. PRIME must preserve OS/log/recovery headroom and split/move storage or runtime before disk pressure becomes unsafe.

## Monthly reset and warnings

AI allowance resets monthly on the billing/entitlement cycle and does not roll over by default.

Storage is persistent and does not reset monthly.

Usage behavior:

- at approximately **80%** of monthly AU allowance, the ARC/RYZ3N service should warn the Owner/customer and surface current consumption;
- at **100%**, RYZ3N does **not** silently charge AI overage;
- the customer may wait for the monthly reset, upgrade tier, or agree a separately priced capacity add-on;
- safety/security-critical system functions may continue even when customer discretionary AI allowance is exhausted;
- RYZ3N may route to a lower-cost suitable model before exhaustion;
- RYZ3N may temporarily restrict abusive, runaway or technically unsafe workloads independent of the commercial cap.

No surprise pass-through provider invoice is allowed.

## Integration entitlement vs third-party cost

The number of integrations included in a tier means the ARC may configure that many external-system connections. It does **not** mean unlimited vendor/API spend is included.

Authoritative variable-cost rule:

`ARC-VARIABLE-COST-AND-API-BOUNDARY.md`

Default rule for Standard/Pro/Business:

- paid third-party subscriptions/API/message/transaction usage is **customer-funded by default**;
- RYZ3N-funded variable third-party spend is **€0 by default unless an explicit capped allowance is written into the commercial agreement**;
- free-tier/free-call integrations may operate normally;
- no Agent/Brain/ARC may autonomously purchase credits, seats, message packs, storage or provider capacity;
- any RYZ3N-funded external allowance must warn at 80% and hard-stop at 100% unless a higher Founder-approved cap already exists.

## Integration definition

An integration is one independently configured external system/service connection that requires ARC credentials, API access, webhook linkage or durable connector configuration.

Examples include Google Drive, Calendar, a CRM, dispatch platform, accounting system or bespoke API.

Multiple workflows inside the same configured integration do not automatically count as separate integrations unless they require materially separate credentials/environments/contracts.

## Automation definition

An active automation is a persistent recurring, triggered or condition-based workflow configured to run without the Owner manually initiating each execution.

One-off tasks do not count as active automations merely because an Agent executes multiple internal steps.

Any automation that can trigger paid third-party calls must additionally inherit per-run/retry/monthly spend controls from `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`.

## Channel definition

A primary channel is a persistent customer-facing or owner-facing interface bound to the ARC, for example Telegram, web chat, WhatsApp, email gateway or a later native ARC interface.

Multiple authorized users inside one channel do not create additional channels, but user-count entitlement still applies.

Paid messaging/telephony/channel-provider fees are not automatically included merely because a channel slot exists.

## Founding Pilot entitlement rule

Free Founding Pilot status does **not** mean unlimited use.

Unless the Founder explicitly grants a different entitlement:

- **VONDA ARC** receives **ARC Standard entitlements** during its six-month free Founding Pilot;
- **NARC** receives **ARC Standard entitlements** during its six-month free Founding Pilot;
- both may be shown the complete Standard / Pro / Business / Dedicated / Enterprise ladder from onboarding onward;
- either pilot may voluntarily upgrade commercial entitlement before or after the free pilot without affecting evidence-derived V1→V6 maturity rules;
- after the pilot, continuation at €50/month or €500/year preserves Standard entitlement unless another tier is selected.

Standard pilot entitlement is therefore now **2 GB + 5,000 AU/month + 1 user + 1 channel + 2 integrations + 5 active automations**.

## KMS7 Founding Business exception

If Adnan accepts and the Founder authorizes KMS7 ARC creation, KMS7 receives a customer-specific **Founding Business** commercial exception:

- price: **€170/month**;
- entitlement level: **ARC Business**;
- Business AI allowance: **30,000 AU/month = €30 normalized provider-list-price-equivalent AI capacity**;
- **15 GB** managed ARC storage;
- up to **10 users**;
- **3 channels**;
- **10 integrations**;
- **40 active automations**;
- capacity weight: **6 shared slots**, with earlier isolation/splitting if concurrency or operational evidence requires it;
- normal future ARC Business price remains **€250/month or €2,500/year**.

Founder working direct-operational-cost ceiling for KMS7 remains **≤€50/month**.

Third-party variable API/vendor costs are **not unlimited inside the €170 price**. They are customer-funded by default unless a specific capped KMS7 vendor allowance is explicitly included in the accepted agreement.

## Capacity and technical-safety relationship

Commercial allowance does not override runtime safety.

OMEGA/PRIME may move an ARC to a different model-capacity pool, VPS or dedicated resource before the commercial allowance is exhausted if latency, concurrency, isolation, storage, provider quota or another technical risk requires it.

Conversely, unused commercial allowance does not guarantee that all workload shapes are safe on shared infrastructure; high-frequency bulk jobs can be structurally different from ordinary interactive use.

## Customer-facing presentation rule

Customers should be able to see the tier ladder and their current entitlement without needing to understand PRIME, OMEGA, FACTORY or provider internals.

At minimum, onboarding/account presentation should show:

- current tier;
- price/billing arrangement;
- managed storage included and used;
- monthly AU allowance included and used;
- authorized users;
- channels;
- integrations;
- active automations;
- upgrade options;
- next reset date;
- warning when nearing limits;
- clear note that third-party provider fees may require the customer's own account/billing or a separately agreed capped allowance.

Do not expose the internal euro-per-AU normalization in marketing unless commercially useful. Customer-facing language may simply call AU the ARC's monthly AI-capacity allowance.

## Review rule

These corrected launch limits are concrete commercial limits, but not immutable forever.

Review using real VONDA, NARC, KMS7 and Founding-20 telemetry. A future Founder-approved revision may raise, lower or restructure allowances if production evidence shows that margin, usability or infrastructure safety requires it.

Existing accepted customer-specific exceptions must be handled according to their agreement rather than silently changed retroactively.

## Founder shorthand

> **AU follows cost, not raw tokens. Efficient models give the customer more work; premium models burn allowance faster. Standard = €5 AI capacity, Pro = €15, Business = €30. Shared pools max at 10 weighted slots until telemetry proves otherwise. Integrations do not give Agents an open third-party wallet.**
