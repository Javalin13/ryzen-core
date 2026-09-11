# ARC Pricing Model

```yaml
---
type: commercial-model
status: founder-directed-current-working-model
created: 2026-09-03
updated: 2026-09-11
classification: strategic-vision + launch-pricing
currency: EUR
amendable: true-additively
---
```

## Pricing principle

**€500/year is the current minimum commercial floor for a Standard ARC, not the ceiling for the product family.**

Monthly billing is deliberately priced above annual billing to reward commitment and compensate for churn/flexibility.

The customer buys a managed ARC service, not raw model tokens or a Hermes installation.

Authoritative commercial usage/cost sources:

- `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`
- `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`

## Current tier ladder

| Tier | Target customer | Current price | Managed storage | Monthly AI allowance | Capacity weight | Users | Integrations | Active automations |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **ARC Standard** | Solo entrepreneur / small operator | **€500/year** or **€50/month** | **2 GB** | **5,000 AU** | **1 slot** | **1** | **2** | **5** |
| **ARC Pro** | Growing entrepreneur / small team | **€1,200/year** or **€120/month** | **5 GB** | **15,000 AU** | **3 slots** | **3** | **5** | **15** |
| **ARC Business** | Company / operational team | **€2,500/year** or **€250/month** | **15 GB** | **30,000 AU** | **6 slots** | **10** | **10** | **40** |
| **ARC Dedicated** | Higher-isolation / heavier operational use | **from €5,000/year** | **50 GB baseline** | **100,000 AU baseline** | dedicated | **25** | **20** | **100** |
| **ARC Enterprise** | Larger organization / multi-ARC deployment | **custom, working floor ~€10,000/year** | custom | custom | custom | custom | custom | custom |

Channels are additionally capped at 1 / 2 / 3 / 5 respectively for Standard / Pro / Business / Dedicated unless a Founder-approved exception applies.

## AU definition — corrected 2026-09-11

AU is **not a fixed token quantity**.

Current internal normalization:

> **1 AU = €0.001 of provider-list-price-equivalent AI consumption.**

Therefore:

- Standard 5,000 AU = **€5 normalized AI capacity**;
- Pro 15,000 AU = **€15 normalized AI capacity**;
- Business 30,000 AU = **€30 normalized AI capacity**;
- Dedicated 100,000 AU = **€100 normalized AI capacity baseline**.

This protects both sides. Efficient models can deliver many more tokens/tasks inside the same allowance, while expensive premium-model use consumes the allowance faster rather than creating uncontrolled RYZ3N cost.

Do not market a guaranteed fixed raw-token quantity across all models.

## Shared capacity weights

Until production evidence proves another safe ceiling:

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

Split earlier when actual concurrency, RAM, disk, provider quota or latency requires it.

## Current AI-provider economics snapshot — 2026-09-11

Current public Ollama new-plan pricing checked on 2026-09-11:

- Pro: $20/month with $60 monthly usage credits and 3 concurrent requests;
- Max: $100/month with $300 monthly usage credits and 10 concurrent requests;
- Team: $500/month with $1,000 monthly shared usage credits.

At the exchange rate used for the 2026-09-11 assessment, $60 was approximately €51.72.

The corrected Standard allowance therefore has a deliberate economic relationship to the current Pro pool:

`10 Standard × €5 normalized AI capacity = €50`

which fits just under the current Pro plan's approximately €51.72 included usage-credit value.

Provider prices and the Founder's actual account/legacy plan may differ. Re-check before changing the real account subscription.

## Usage behavior

- AI allowance resets monthly; unused allowance does not roll over by default.
- Managed storage persists until files/data are deleted or moved.
- At ~80% usage, warn the customer.
- At 100%, do not silently bill AI overage. The customer may wait for reset, upgrade, or agree a separately priced capacity add-on.
- RYZ3N may route an ordinary task to a lower-cost model when quality remains sufficient.
- External Google Drive/CRM/dispatch/SaaS data does not count as ARC storage while it stays in the external system; persistent copies mirrored into ARC storage do count.
- Commercial caps do not override security, provider, latency, isolation or infrastructure-safety limits.

## Integration/API cost boundary

**Integration count and third-party vendor spend are separate.**

A plan may include 2, 5 or 10 configured integrations without RYZ3N accepting unlimited external API/message/subscription charges.

Default rule for Standard / Pro / Business:

- third-party paid API/subscription/message/transaction cost is **customer-funded by default**;
- RYZ3N-funded variable third-party spend is **€0 by default unless the agreement explicitly includes a capped vendor allowance**;
- free-tier/free-call integrations can operate normally;
- customer-owned billing is preferred for cost-bearing optional platforms;
- no ARC/Brain/Agent may purchase provider credits, seats, numbers, message packs, storage or other paid capacity autonomously;
- if RYZ3N funds a specific external provider allowance, warn at 80% and hard-stop at 100% unless a higher approved cap already exists;
- there are no surprise pass-through provider bills.

See `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`.

## Founding 20 launch cohort

Working launch offer:

> **Founding ARC — €49/month, founding rate locked while continuously subscribed.**

Founding ARC receives **Standard entitlements** unless another tier is explicitly purchased/authorized.

## Founding Pilot rule

A free Founding Pilot is assigned a real commercial entitlement. Free does not mean unlimited.

Current Founder direction:

- **VONDA ARC** — six-month free Founding Pilot on **Standard**: 2 GB, 5,000 AU, 1 user, 1 channel, 2 integrations, 5 automations.
- **NARC** — six-month free Founding Pilot on **Standard** with the same entitlement.
- Both should be shown the full Standard / Pro / Business / Dedicated / Enterprise ladder during onboarding.
- Commercial upgrade does not purchase or fake ARC maturity/aura.

## KMS7 Founding Business exception

If Adnan accepts and KMS7 ARC creation is authorized:

- customer-specific price: **€170/month**;
- entitlement: **ARC Business**;
- included: **15 GB managed storage, 30,000 AU/month, up to 10 users, 3 channels, 10 integrations and 40 active automations**;
- capacity weight: **6 shared slots**;
- normal future Business remains **€250/month or €2,500/year**;
- materially new future scope may still require a change order, Dedicated resources or another explicit arrangement.

Founder direct-operational-cost ceiling target for KMS7 remains **≤€50/month**.

KMS7's 10 integration slots do **not** mean RYZ3N pays unlimited vendor/API costs. Paid third-party platform usage remains customer-funded by default unless the accepted KMS7 agreement explicitly grants a capped included vendor allowance.

## Customer-facing usage promise

Preferred external promise:

> **One predictable subscription with a clear included AI allowance and clear integration limits. Third-party services may have their own provider fees. No surprise pass-through bill and no open-ended provider spending.**

## Billing tier ≠ maturity/aura tier

Commercial billing tier and ARC maturity are separate concepts.

- Billing tier defines commercial scope, support, storage/usage allowance, integrations and infrastructure.
- V1→V6 defines verified ARC capability maturity.

A customer cannot purchase a false Gold/Platinum/Sovereign aura merely by paying a higher subscription.

## Margin discipline

Revenue should be evaluated against:

- attributable model/provider cost;
- model-capacity pool subscription/allocation;
- VPS/platform allocation;
- third-party integration spend actually funded by RYZ3N;
- support time;
- founder implementation/configuration time;
- incidents/retries/failure burden;
- payment/admin overhead;
- monitoring/backups/security.

The hidden cost to protect against remains human time and uncapped third-party variable spend.

See `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`, `ARC-VARIABLE-COST-AND-API-BOUNDARY.md`, `ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md` and `COST-CAPACITY-MODEL.md`.
