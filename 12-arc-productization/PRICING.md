# ARC Pricing Model

```yaml
---
type: commercial-model
status: founder-directed-current-working-model
created: 2026-09-03
updated: 2026-09-12
classification: strategic-vision + launch-pricing
currency: EUR
local_first_arc_inference: true
owner_ai_usage_caps: false
amendable: true-additively
---
```

## Pricing principle

**€500/year is the current minimum commercial floor for a Standard ARC, not the ceiling for the product family.**

Monthly billing is deliberately priced above annual billing to reward commitment and compensate for churn/flexibility.

The customer buys a managed ARC service, not raw model tokens or a Hermes installation.

Current architecture principle:

- PRIME uses Founder-authorized Ollama Cloud MiniMax M3 as its premium cloud primary;
- Owner-facing ARCs run on the verified shared local inference service as their normal primary route;
- Owners are not billed or messaged through daily/weekly/monthly AI model-usage counters;
- third-party vendor/API costs remain separate where applicable.

Authoritative commercial/resource sources:

- `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`
- `ARC-CAPACITY-FALLBACK-TEMPORARY-DOWNGRADE-AND-LOCAL-INFERENCE-STANDARD.md`
- `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`

## Current tier ladder

| Tier | Target customer | Current price | Managed storage | AI service | Capacity weight | Users | Integrations | Active automations |
|---|---|---:|---:|---|---:|---:|---:|---:|
| **ARC Standard** | Solo entrepreneur / small operator | **€500/year** or **€50/month** | **2 GB** | shared local inference included; no Owner-facing AI usage cap | **1 slot** | **1** | **2** | **5** |
| **ARC Pro** | Growing entrepreneur / small team | **€1,200/year** or **€120/month** | **5 GB** | shared local inference included; higher service allocation/priority to be telemetry-calibrated | **3 slots** | **3** | **5** | **15** |
| **ARC Business** | Company / operational team | **€2,500/year** or **€250/month** | **15 GB** | shared local inference included; stronger business service allocation/possible isolation | **6 slots** | **10** | **10** | **40** |
| **ARC Dedicated** | Higher-isolation / heavier operational use | **from €5,000/year** | **50 GB baseline** | dedicated/contract-defined inference resources | dedicated | **25** | **20** | **100** |
| **ARC Enterprise** | Larger organization / multi-ARC deployment | **custom, working floor ~€10,000/year** | custom | custom / dedicated / SLA-defined | custom | custom | custom | custom |

Channels remain capped at 1 / 2 / 3 / 5 respectively for Standard / Pro / Business / Dedicated unless a Founder-approved exception applies.

## No Owner-facing AI usage cap

Standard, Pro and Business do not currently expose a daily/weekly/monthly model-usage allowance to the Owner.

Therefore:

- no AI usage balance is shown;
- no 80% AI usage warning is shown;
- no "you reached your daily/weekly/monthly AI limit" message is shown;
- no AI-consumption reset clock is shown;
- no model-usage upsell is triggered by the local model.

This does **not** promise infinite simultaneous compute. Shared local capacity may queue requests and heavier workloads may require isolation or Dedicated infrastructure.

## AU remains internal telemetry only

AU may remain as an internal equivalent-cost normalization for telemetry and historical comparison:

> **1 AU = €0.001 of provider-list-price-equivalent AI consumption.**

AU is not currently marketed as an Owner allowance and is not a hard-stop mechanism for local-first ARCs.

## Shared capacity weights

Until production evidence proves another safe ceiling:

> **maximum 10 Standard-equivalent weighted slots per shared local inference/VPS capacity pool.**

Planning weights:

- Standard = 1;
- Pro = 3;
- Business = 6;
- Dedicated = separate/dedicated;
- Enterprise = custom.

These weights help capacity planning; they are not customer AI quotas.

Split earlier when concurrency, RAM, disk, queue depth, latency or service quality requires it.

## What plans are paying for

Pricing should increasingly reflect:

- managed ARC storage;
- authorized users;
- integrations;
- automations;
- channels;
- support/service level;
- queue/concurrency priority;
- shared vs isolated compute placement;
- advanced capabilities;
- dedicated infrastructure where required;
- operational support and maintenance burden.

Step 17B should refine the exact balance using real telemetry rather than pre-guessing AI token ceilings.

## Local-first economics

Even with zero marginal API fees for the normal ARC model route, inference is not economically free.

RYZ3N must measure:

- VPS/server cost;
- CPU/RAM utilization;
- local model storage;
- queue/concurrency pressure;
- calls/tokens per Owner;
- free external fallback frequency;
- support/incidents;
- backups/security/monitoring;
- Founder implementation/configuration time;
- future hardware expansion needs.

PRIME's Ollama Cloud MiniMax usage is a separate Founder/control-plane cost and must not be allocated as though every ARC is consuming that cloud pool.

## Integration/API cost boundary

**Integration count and third-party vendor spend are separate.**

A plan may include 2, 5 or 10 configured integrations without RYZ3N accepting unlimited external API/message/subscription charges.

Default rule for Standard / Pro / Business:

- third-party paid API/subscription/message/transaction cost is **customer-funded by default**;
- RYZ3N-funded variable third-party spend is **€0 by default unless the agreement explicitly includes a capped vendor allowance**;
- free-tier/free-call integrations can operate normally;
- customer-owned billing is preferred for cost-bearing optional platforms;
- no ARC/Brain/Agent may purchase provider credits, seats, numbers, message packs, storage or other paid capacity autonomously;
- there are no surprise pass-through provider bills.

See `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`.

## Founding 20 launch cohort

Working launch offer:

> **Founding ARC — €49/month, founding rate locked while continuously subscribed.**

Founding ARC receives Standard service scope unless another tier is explicitly purchased/authorized.

## Founding Pilot rule

Current Founder direction:

- **VONDA ARC** — six-month free Founding Pilot on Standard: 2 GB, 1 user, 1 channel, 2 integrations, 5 automations, shared local AI service included.
- **NARC** — six-month free Founding Pilot on Standard with the same scope.
- Both should be shown the commercial tier ladder during onboarding when commercially appropriate.
- Commercial upgrade does not purchase or fake ARC maturity/aura.

Free pilot status does not mean unlimited third-party vendor spend, unlimited storage, unlimited users/integrations/automations or infinite simultaneous compute.

## KMS7 Founding Business exception

If Adnan accepts and KMS7 ARC creation is authorized:

- customer-specific price: **€170/month**;
- entitlement: **ARC Business**;
- included: **15 GB managed storage, up to 10 users, 3 channels, 10 integrations and 40 active automations**;
- shared local AI service included without an Owner-facing model-usage cap;
- capacity weight: **6 shared slots**;
- earlier isolation/splitting may occur if telemetry shows pressure;
- normal future Business remains **€250/month or €2,500/year**.

Founder direct-operational-cost ceiling target for KMS7 remains **≤€50/month**.

KMS7's integration slots do **not** mean RYZ3N pays unlimited vendor/API costs.

## Customer-facing promise

Preferred external promise:

> **One predictable subscription for your ARC, with local AI service included and clear service/integration scope. Third-party services may have their own provider fees. No surprise pass-through bill.**

Do not market provider/session/token-reset mechanics to Owners.

## Billing tier ≠ maturity/aura tier

Commercial billing tier and ARC maturity are separate concepts.

- Billing tier defines commercial scope, support, storage, users, integrations, automations and infrastructure/service allocation.
- V1→V6 defines verified ARC capability maturity.

A customer cannot purchase a false Gold/Platinum/Sovereign aura merely by paying a higher subscription.

## Margin discipline

Revenue should be evaluated against:

- shared/dedicated VPS and local inference allocation;
- model storage/resource consumption;
- third-party integration spend actually funded by RYZ3N;
- support time;
- Founder implementation/configuration time;
- incidents/retries/failure burden;
- payment/admin overhead;
- monitoring/backups/security;
- future hardware scaling requirements.

The hidden costs to protect against remain human time, infrastructure pressure and uncapped third-party variable spend.

See `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`, `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`, `ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md` and `COST-CAPACITY-MODEL.md`.
