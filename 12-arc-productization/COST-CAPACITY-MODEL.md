# ARC Cost & Capacity Model

```yaml
---
type: cost-capacity-model
status: working-model
created: 2026-09-03
updated: 2026-09-11
classification: reality + research-and-exploration
amendable: true-additively
---
```

## Purpose

Model ARC economics and service capacity using current known infrastructure, current public AI-provider pricing and conservative operational guardrails without confusing shared platform cost with per-customer cost.

Authoritative related standards:

- `PRICING.md`
- `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`
- `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`

## Known current shared infrastructure costs

Founder-reported recurring stack:

| Cost item | Current amount / known state | Treatment for ARC economics |
|---|---:|---|
| Hosting account | **~€25/month** | Shared business/platform overhead unless a client requires dedicated hosting/domain services |
| ChatGPT Plus | **~€25/month** | Founder productivity/tooling overhead; do not automatically treat as ARC runtime COGS |
| Ollama account | Founder previously reported **~€25/month**; public new Pro plan is now **$20/month** | Actual connected account may be legacy; verify before plan migration. Allocate shared model capacity, not full account cost to every ARC |
| VPS | **~€6/month** | Shared runtime infrastructure; allocation depends on weighted ARC density and real resource usage |

Do not add the full shared stack to each ARC. Maintain incremental and fully loaded contribution separately.

## Current VPS baseline

Known PRIME VPS baseline:

- approximately **2 vCPU**;
- approximately **4 GB RAM**;
- approximately **40 GB storage**;
- approximately **€6/month**.

Heavy model inference is primarily external/cloud, so the VPS is expected to carry orchestration, gateways, workspace/runtime state, logs and light services rather than frontier-model inference.

The VPS is therefore currently cheap relative to commercial subscription revenue, but RAM/disk/concurrency/isolation still impose service-quality limits.

## Current Ollama public pricing snapshot — 2026-09-11

Public new-plan pricing checked on 2026-09-11:

- **Pro — $20/month**, **$60 monthly usage credits**, **3 concurrent requests**;
- **Max — $100/month**, **$300 monthly usage credits**, **10 concurrent requests**;
- **Team — $500/month**, **$1,000 monthly shared usage credits**.

At the USD→EUR rate used on 2026-09-11:

- $20 ≈ **€17.24**;
- $60 ≈ **€51.72**.

Model prices vary materially by model and by input/cached-input/output token type. For that reason, customer entitlements must not be expressed as one fixed raw-token quantity across all models.

Existing Founder Ollama billing may be on legacy pricing. **Do not change the actual subscription solely because this public plan exists without first checking the connected account and migration implications.**

## Corrected AU economics

Current internal normalization:

> **1 AU = €0.001 of provider-list-price-equivalent AI consumption.**

Launch AI envelopes:

| Tier | AU/month | Normalized provider usage value | Shared capacity weight |
|---|---:|---:|---:|
| Standard | **5,000** | **€5** | **1 slot** |
| Pro | **15,000** | **€15** | **3 slots** |
| Business | **30,000** | **€30** | **6 slots** |
| Dedicated | **100,000 baseline** | **€100 baseline** | dedicated |
| Enterprise | custom | custom | custom |

This meter is cost-normalized. Efficient models can deliver much more raw token volume than premium models within the same commercial envelope.

## Why 10 Standard slots aligns with current Pro economics

Founder safety doctrine already used **10 Standard ARCs per model-capacity pool** as the initial ceiling.

The corrected economics now give that ceiling a commercial basis:

`10 Standard × €5 normalized AI allowance = €50 monthly normalized provider usage`

Current public Ollama Pro includes approximately €51.72 worth of monthly usage credits at the exchange rate used for this assessment.

Therefore one current Pro pool can theoretically cover the normalized usage envelopes of up to 10 Standard slots **on usage-credit value**, while the $20/€17.24 subscription buys access/concurrency and the included credit pool.

This does **not** prove that 10 ARCs are operationally safe. Pro currently exposes only 3 concurrent requests, so concurrency/latency may force an earlier split even when usage-credit value remains available.

## Shared weighted-slot model

Until production evidence supports a different ceiling:

> **maximum 10 Standard-equivalent weighted slots per shared model/VPS pool.**

Weights:

- Standard = 1;
- Pro = 3;
- Business = 6;
- Dedicated = separate/dedicated;
- Enterprise = custom.

Illustrative 10-slot mixes:

- 10 Standard;
- 3 Pro + 1 Standard;
- 1 Business + 1 Pro + 1 Standard;
- 1 Business + 4 Standard.

This same weight is a planning shorthand for model usage and shared runtime footprint; telemetry always overrides the shorthand.

## VPS cost allocation illustrations

At €6/month for a 10-slot shared VPS:

- one Standard slot at full 10-slot occupancy ≈ **€0.60/month raw VPS allocation**;
- one Pro at 3 slots ≈ **€1.80/month raw VPS allocation**;
- one Business at 6 slots ≈ **€3.60/month raw VPS allocation**.

These figures are raw infrastructure allocation only. They exclude backups, support, monitoring, storage expansion, payment fees, AI subscription allocation and incidents.

### Storage pressure

A 40 GB VPS cannot safely promise that every logical customer storage quota will be physically filled on the same machine simultaneously.

Current logical managed-storage entitlements:

- Standard 2 GB;
- Pro 5 GB;
- Business 15 GB;
- Dedicated 50 GB baseline on appropriate dedicated/expanded storage;
- Enterprise custom.

PRIME must preserve OS/log/checkpoint/recovery headroom and move/expand storage or runtime before local disk pressure becomes unsafe.

A useful initial operational trigger is to review/move capacity before sustained disk use exceeds approximately **70%** of the shared VPS, subject to real filesystem/log requirements.

## Model-capacity pool economics

Using the current public Pro plan only as a planning reference:

- pool subscription ≈ €17.24/month;
- included usage-credit value ≈ €51.72/month;
- 10 Standard envelopes total €50 normalized AI usage;
- full 10-slot raw VPS cost ≈ €6/month.

At full 10-Standard occupancy, rough base subscription allocation would be approximately:

- AI subscription: **~€1.72 per Standard/month**;
- VPS: **~€0.60 per Standard/month**;
- combined raw AI-subscription + VPS allocation: **~€2.32 per Standard/month**, before other direct/shared costs.

This is an illustration, not a guaranteed production margin. Usage may not distribute evenly; concurrency may require more pools; legacy account pricing may differ; and support/human time can dominate economics.

## Business/KMS7 illustration

KMS7, if accepted, is Business entitlement with 6 weighted slots at €170/month.

On a fully utilized 10-slot shared pool, rough raw allocations are:

- 6/10 of a €17.24 AI subscription ≈ **€10.34/month**;
- 6/10 of a €6 VPS ≈ **€3.60/month**;
- combined raw AI-subscription + VPS allocation ≈ **€13.94/month**.

KMS7's Business AU envelope is €30 normalized provider-list-price-equivalent AI usage. If the pool's included credits cover that usage, the incremental invoice may remain inside the pool subscription. If KMS7 usage/concurrency forces a separate pool, cost rises and must be measured.

Founder target remains:

> **KMS7 total direct operational cost ≤ €50/month.**

That leaves headroom for bounded integration/vendor costs, backups/monitoring and operational variance—but only if third-party variable spend is controlled.

## Direct COGS vs shared overhead

### Direct / incremental ARC costs

Track where measurable:

- model/provider usage attributable to the ARC;
- allocated/new model-capacity pool subscriptions triggered by that ARC;
- dedicated VPS/resources if required;
- RYZ3N-funded third-party API/vendor usage explicitly included;
- customer-specific domain/storage/external services;
- payment processing;
- extraordinary support/implementation labor.

### Shared overhead

Examples:

- Founder's ChatGPT Plus subscription;
- shared hosting already required for the business;
- shared base VPS until additional capacity is required;
- general R&D;
- common monitoring/tooling.

Maintain both:

1. **incremental technical contribution**; and
2. **fully loaded contribution** including support/admin/shared-platform allocation.

## Third-party API/vendor cost boundary

Integration count is not permission to generate unlimited external spend.

Default rule:

- customer-funded billing for paid third-party providers;
- RYZ3N-funded variable third-party spend = **€0 by default** unless explicitly capped in the commercial agreement;
- any included RYZ3N-funded vendor allowance must warn at 80% and hard-stop at 100%;
- no Agent/Brain/ARC may buy credits, seats, phone numbers, message packs, storage or other provider capacity autonomously;
- retries/loops/concurrency on paid providers must be bounded.

See `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`.

## Provider overage protection

Where the provider supports it:

- disable automatic usage top-up / unlimited pay-as-you-go exposure on shared customer pools;
- prefer a finite purchased balance or provider-side budget cap;
- warn before included pool credits are exhausted;
- route suitable work to more efficient models;
- split/provision another approved pool only through operational/commercial decision;
- never let customer model choice bypass AU metering.

## Required per-ARC telemetry

Track privacy-safe operational signals where available:

- AU consumed and percentage of monthly entitlement;
- provider-list-price-equivalent usage cost;
- request count;
- model mix;
- successful/failed calls;
- throttling/rate-limit events;
- retry bursts;
- latency;
- concurrency;
- model/provider incidents;
- storage usage;
- active automation count;
- paid third-party calls and spend where RYZ3N-funded;
- support/intervention minutes.

Do not place private customer conversation payload into steward/business telemetry.

## Capacity expansion triggers

Split/add capacity before recurring user degradation when any becomes structurally true:

- weighted 10-slot ceiling reached;
- concurrency queue/rejection pressure;
- recurring throttling/rate limits;
- latency degrades during overlapping use;
- provider-credit headroom becomes too small;
- one ARC consumes disproportionate AU/capacity;
- RAM/storage headroom becomes unsafe;
- isolation requirements exceed shared-host capability;
- customer requires dedicated availability/resources.

## Commercial heavy-usage treatment

When an ARC becomes structurally heavy:

1. determine whether inefficient implementation is wasting capacity;
2. optimize/reroute where reasonable;
3. reassign/split pool capacity if needed;
4. upgrade the commercial tier or sell an explicit capacity add-on where usage exceeds the purchased entitlement;
5. use Dedicated when isolation/resources/availability justify it.

Never silently pass unexpected provider overage to the customer.

## Current unknowns to measure

1. Actual AU distribution across real Standard/Pro/Business users.
2. Real model mix and cost per useful task.
3. Whether current Founder Ollama account is legacy or new pricing and its practical API/concurrency behavior.
4. RAM footprint per live ARC at idle and under load.
5. Telegram/gateway concurrency and process footprint.
6. Storage/log growth over 30/90/365 days.
7. Support minutes per customer/month.
8. Provisioning time per ARC.
9. Failure/intervention burden.
10. Whether 10 weighted slots preserves acceptable p95 latency.
11. Whether Business users need Max/dedicated pools sooner than usage-credit math suggests.
12. Real third-party provider costs by integration category.

## Business objective

The economic design target is:

> **recurring revenue grows faster than model capacity + runtime + external-provider spend + support obligations.**

Cheap VPS capacity helps, but uncontrolled AI/API/provider usage can destroy that advantage. Cost-normalized AU, weighted pools and third-party hard boundaries are therefore mandatory parts of ARC productization.
