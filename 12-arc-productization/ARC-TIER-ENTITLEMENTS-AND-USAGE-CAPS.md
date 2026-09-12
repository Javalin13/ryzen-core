# ARC Tier Entitlements & Usage Caps

```yaml
---
type: commercial-entitlement-standard
status: founder-directed-current
created: 2026-09-11
updated: 2026-09-12
classification: commercial-pricing + usage-governance
currency: EUR
supersedes_conflicting_fair_use_deferral: true
supersedes_raw-token-au-definition: true
supersedes_business_30000_au_hard_cap: true
amendable: true-additively
---
```

## Purpose

Define current commercial entitlements for ARC Standard, Pro, Business, Dedicated and Enterprise while keeping Owner-facing entitlement separate from provider/infrastructure capacity.

Billing tier remains separate from ARC maturity V1→V6. Paying for a larger entitlement does not buy maturity or aura.

Canonical companion standards:

- `ARC-ROLE-TAXONOMY-AND-ENTITLEMENT-LIMIT-MESSAGING-STANDARD.md`
- `ARC-CAPACITY-FALLBACK-TEMPORARY-DOWNGRADE-AND-LOCAL-INFERENCE-STANDARD.md`
- `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`

## AU definition

AU is cost-normalized, not a raw-token promise.

> **1 ARC Usage Unit (AU) = €0.001 of provider-list-price-equivalent AI consumption.**

AU remains useful internally for Standard/Pro accounting and telemetry. Efficient routes provide more work per AU; premium routes consume AU faster.

## Current tier ladder

| Tier | Current price | Managed ARC storage | Owner high-performance entitlement | Capacity weight | Authorized users | Primary channels | Integrations | Active automations | Infrastructure |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
| **ARC Standard** | **€50/month or €500/year** | **2 GB** | **5,000 AU/month current launch allowance**; cadence controls may also include daily/weekly windows | **1 slot** | **1** | **1** | **2** | **5** | shared |
| **ARC Pro** | **€120/month or €1,200/year** | **5 GB** | **15,000 AU/month current launch allowance**; cadence controls may also include daily/weekly windows | **3 slots** | **3** | **2** | **5** | **15** | shared / higher allowance |
| **ARC Business** | **€250/month or €2,500/year** | **15 GB** | **Unlimited Owner usage entitlement**; backend capacity may temporarily downgrade while high-performance capacity resets | **6 slots** | **10** | **3** | **10** | **40** | shared business pool or isolated placement when needed |
| **ARC Dedicated** | **from €5,000/year** | **50 GB baseline** | **Unlimited or contract-defined Owner entitlement** on dedicated resources | dedicated | **25** | **5** | **20** | **100** | dedicated resources/VPS where required |
| **ARC Enterprise** | **custom; working floor ~€10,000/year** | custom | custom / contract-defined | custom/dedicated | custom | custom | custom | custom | dedicated / multi-ARC / SLA as contracted |

These are commercial/service entitlements, not claims about hard provider or hardware maximums.

## Standard and Pro usage windows

Standard and Pro may have one or more configured high-performance windows:

- daily;
- weekly;
- monthly.

The current concrete launch allowance remains monthly AU-based until Step 17B telemetry justifies a Founder-approved revision. Daily/weekly windows may be added as protective or productized high-performance limits without changing the canonical role model.

At a real configured limit, the ARC must identify the correct cadence and enter `temporary_reduced_capacity` when a suitable lower-cost/local fallback is available.

The Owner must not lose access merely because the high-performance allowance is exhausted if reduced-capacity service is technically available and permitted.

## Temporary downgrade behavior

At a Standard/Pro high-performance limit:

```text
full_performance
→ owner_entitlement_exhausted(<cadence>)
→ temporary_reduced_capacity
→ limit resets
→ full_performance
```

The Owner keeps:

- ARC identity;
- Owner binding;
- memory/state;
- supported tools;
- form/aura/maturity;
- normal privacy boundaries.

The downgrade changes only the model/capacity service state.

Canonical customer messaging is defined in `ARC-ROLE-TAXONOMY-AND-ENTITLEMENT-LIMIT-MESSAGING-STANDARD.md`.

## Business unlimited Owner entitlement

ARC Business is **unlimited at the Owner-entitlement layer**.

This supersedes the previous 30,000 AU/month Business hard cap.

Unlimited means RYZ3N does not tell a Business Owner that their commercial ARC usage allowance has been exhausted.

It does **not** mean:

- infinite simultaneous compute;
- no technical safety controls;
- unlimited third-party vendor spend funded by RYZ3N;
- no queueing;
- guaranteed premium-model availability at every instant;
- permission to purchase provider capacity autonomously.

If shared high-performance infrastructure is constrained, a Business ARC may temporarily run through a local/approved fallback and tell the Owner that it is temporarily in reduced-capacity mode. Full performance returns automatically when capacity recovers.

Backend capacity/fair-use controls are operational safeguards, not a Business Owner hard usage cap.

## Shared-capacity weight model

Until telemetry proves another safe ceiling:

> **maximum 10 Standard-equivalent weighted slots per shared model/VPS capacity pool.**

Weights:

- Standard = 1;
- Pro = 3;
- Business = 6;
- Dedicated = separate/dedicated;
- Enterprise = custom.

Examples:

- 10 Standard = 10;
- 3 Pro + 1 Standard = 10;
- 1 Business + 1 Pro + 1 Standard = 10;
- 1 Business + 4 Standard = 10.

This is a planning/safety model. PRIME/OMEGA may split earlier when latency, RAM, disk, local inference pressure, concurrency or provider quota requires it.

## Current provider economics relationship

Provider subscription/credit economics remain infrastructure metadata, not Owner entitlement truth.

RYZ3N must separately measure:

- actual provider cost;
- equivalent model cost;
- fixed subscription allocation;
- local inference utilization;
- fallback frequency;
- session/daily/weekly/monthly capacity pressure;
- concurrency and queue pressure.

Step 17B uses these real telemetry values to refine prices/limits. Public prices and entitlements never change automatically.

## Managed ARC storage

Managed ARC storage is customer-specific persistent storage controlled by the ARC/RYZ3N service, including retained uploads, workspace files, generated retained assets, customer-specific state stored as files/data and persistent caches.

External data remaining in Google Drive, OneDrive/Dropbox, CRM, dispatch or another connected SaaS does not automatically count as ARC storage. Persistent ARC-side copies do count.

The shared VPS baseline must retain OS/log/recovery/model headroom. Logical customer storage entitlement is not a promise that every maximum quota will physically reside on one VPS simultaneously.

## Warnings and resets

For Standard/Pro:

- warn at approximately 80% of the relevant configured allowance;
- at 100%, do not silently bill overage;
- identify whether the reached limit is daily, weekly or monthly;
- temporarily downgrade when an approved reduced-capacity route is available;
- automatically restore full performance when the relevant limit resets;
- the Owner may wait, upgrade, or choose another commercial option where applicable.

For Business:

- do not issue an Owner entitlement-exhausted warning;
- capacity warnings remain Founder/PRIME operational telemetry;
- Owner may receive only a temporary reduced-capacity service-state message when required.

No surprise pass-through provider invoice is allowed.

## Integration entitlement vs third-party cost

Integration slots do not create an open third-party wallet.

For Standard/Pro/Business:

- paid third-party subscription/API/message/transaction cost is customer-funded by default;
- RYZ3N-funded variable third-party spend is €0 by default unless a written capped allowance exists;
- free-tier/free-call integrations may operate normally;
- no ARC/Brain/Agent may autonomously purchase credits, seats, message packs, storage or provider capacity;
- any RYZ3N-funded external allowance must warn at 80% and hard-stop at 100% unless a higher Founder-approved cap already exists.

## Definitions

### Integration

One independently configured external system/service connection requiring durable credentials/configuration. Multiple workflows inside one configured integration do not automatically count as separate integrations.

### Active automation

A persistent recurring, triggered or condition-based workflow configured to run without the Owner manually initiating each execution. One-off multi-step Agent work is not automatically an active automation.

### Primary channel

A persistent Owner-facing interface such as Telegram, web chat, WhatsApp, email gateway or later native ARC interface.

## Founding Pilot rule

Free Founding Pilot status does not mean unlimited use unless the Founder explicitly grants Business or another entitlement.

Current direction:

- VONDA ARC: six-month free Founding Pilot on Standard;
- NARC: six-month free Founding Pilot on Standard;
- current Standard baseline: 2 GB + 5,000 AU/month + 1 user + 1 channel + 2 integrations + 5 active automations;
- pilots may upgrade commercial entitlement without affecting evidence-derived V1→V6 maturity.

## KMS7 Founding Business exception

If Adnan accepts and the Founder authorizes KMS7 ARC creation:

- price: **€170/month**;
- entitlement: **ARC Business**;
- Owner usage entitlement: **unlimited**;
- 15 GB managed ARC storage;
- up to 10 users;
- 3 channels;
- 10 integrations;
- 40 active automations;
- capacity weight: 6 shared slots, with earlier isolation/splitting if telemetry requires it;
- normal future Business price remains €250/month or €2,500/year.

Founder working direct-operational-cost ceiling for KMS7 remains **≤€50/month**. The unlimited Owner entitlement therefore depends on routing efficiency, local fallback, shared-capacity management and telemetry — not on accepting unlimited provider bills.

Third-party variable API/vendor costs remain customer-funded by default unless a specific capped KMS7 vendor allowance is explicitly included.

## Capacity and technical-safety relationship

Commercial entitlement does not override runtime safety.

OMEGA/PRIME may move an ARC to a different model-capacity pool, local fallback, VPS or dedicated resource if latency, concurrency, isolation, storage, provider quota or another technical risk requires it.

Unused entitlement does not guarantee that every workload shape is safe on shared infrastructure. High-frequency bulk jobs may be queued or isolated even when an Owner has entitlement remaining.

## Customer-facing presentation

At minimum, onboarding/account surfaces should show:

- current tier;
- price/billing arrangement;
- managed storage included/used;
- Standard/Pro high-performance allowance and reset cadence where applicable;
- Business unlimited Owner entitlement where applicable;
- authorized users;
- channels;
- integrations;
- automations;
- upgrade options;
- next reset date for capped high-performance windows;
- reduced-capacity state if active;
- clear separation of third-party provider fees from the ARC subscription.

Do not expose internal euro-per-AU normalization, provider IDs, local model details, HTTP errors or account billing internals in normal Owner UX.

## Review rule

Review Standard/Pro allowances, Business infrastructure economics and all prices using real telemetry from VONDA, NARC, Cargo, KMS7 and later cohorts.

A future Founder-approved revision may raise, lower or restructure limits/prices when production evidence justifies it. Existing accepted customer-specific agreements are not silently rewritten.

## Founder shorthand

> **Standard and Pro have measurable high-performance allowances and may temporarily downgrade after daily/weekly/monthly limits. Business is unlimited at the Owner-entitlement layer. Provider/internal limits are not Owner limits. Local and approved free fallbacks preserve continuity. Telemetry refines the economics; only the Founder changes pricing or entitlements.**
