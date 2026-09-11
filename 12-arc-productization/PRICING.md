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

Authoritative entitlement/usage standard:

`ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`

## Current tier ladder

| Tier | Target customer | Current price | Managed storage | Monthly AI allowance | Users | Integrations | Active automations |
|---|---|---:|---:|---:|---:|---:|---:|
| **ARC Standard** | Solo entrepreneur / small operator | **€500/year** or **€50/month** | **2 GB** | **2,000 AU** (~2M token-equivalent) | **1** | **2** | **5** |
| **ARC Pro** | Growing entrepreneur / small team | **€1,200/year** or **€120/month** | **5 GB** | **6,000 AU** (~6M token-equivalent) | **3** | **5** | **15** |
| **ARC Business** | Company / operational team | **€2,500/year** or **€250/month** | **15 GB** | **15,000 AU** (~15M token-equivalent) | **10** | **10** | **40** |
| **ARC Dedicated** | Higher-isolation / heavier operational use | **from €5,000/year** | **50 GB baseline** | **40,000 AU** (~40M token-equivalent) | **25** | **20** | **100** |
| **ARC Enterprise** | Larger organization / multi-ARC deployment | **custom, working floor ~€10,000/year** | custom | custom | custom | custom | custom |

Channels are additionally capped at 1 / 2 / 3 / 5 respectively for Standard / Pro / Business / Dedicated unless a Founder-approved exception applies.

**AU = ARC Usage Unit**, approximately 1,000 model tokens-equivalent of combined attributable model usage. Multi-step Agent/Brain work may consume multiple units. Exact metering rules are defined in `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`.

The tiers above Pro remain commercial working hypotheses until broader market validation, but these usage entitlements are the current Founder-directed launch limits.

## Usage behavior

The service must show customers what their tier includes instead of relying on vague “fair use”.

- AI allowance resets monthly; unused allowance does not roll over by default.
- Managed storage persists until files/data are deleted or moved.
- At ~80% usage, warn the customer.
- At 100%, do not silently bill overage. The customer may wait for reset, upgrade, or agree a separately priced capacity add-on.
- External Google Drive/CRM/dispatch/SaaS data does not count as ARC storage while it stays in the external system; persistent copies mirrored into ARC storage do count.
- Commercial caps do not override security, provider, latency, isolation or infrastructure-safety limits.

## Founding 20 launch cohort — 2026-09-10

The first commercial validation cohort should consist of up to **20 paying entrepreneurs** recruited primarily through trusted/direct channels before broad paid-media scale.

Working launch offer:

> **Founding ARC — €49/month, founding rate locked while continuously subscribed.**

Rules:

- maximum initial cohort: 20 paying Founding ARCs;
- free setup for Standard-scope onboarding;
- Founding ARC receives **Standard entitlements** unless another tier is explicitly purchased/authorized;
- the €49 founding rate is a launch-cohort privilege, not the permanent public Standard price;
- after the Founding 20, normal Standard pricing remains €50/month or €500/year unless the Founder changes it;
- continuity of the founding price may end if the subscription is cancelled and later restarted;
- bespoke integrations, dedicated resources, usage beyond Standard entitlement or high-touch support remain outside Standard scope;
- the Founder may pause the cohort before 20 if service quality, support burden, provisioning or model-capacity evidence requires it.

The purpose of Founding 20 is to validate willingness to pay, retention, onboarding repeatability, real usage, support effort and unit economics before scaling advertising.

## Founding Pilot rule

A free Founding Pilot may receive:

- free setup;
- a time-limited free ARC usage period;
- basic adaptations needed to validate the product;
- the commercial entitlements of its assigned tier.

A free period does **not** mean unlimited storage, AI consumption, integrations, users or automations.

Current Founder direction:

- **VONDA ARC** — six-month free Founding Pilot on **Standard entitlements**, then €50/month or €500/year if continued on Standard.
- **NARC** — six-month free Founding Pilot on **Standard entitlements**, then €50/month or €500/year if continued on Standard.
- Both should be shown the full Standard / Pro / Business / Dedicated / Enterprise ladder during onboarding so they understand upgrade paths.
- A pilot may upgrade its commercial tier without purchasing or faking ARC maturity/aura.

A free Founding Pilot is distinct from the **paid Founding 20 commercial cohort**.

## KMS7 Founding Business exception

If Adnan accepts and KMS7 ARC creation is authorized:

- customer-specific price: **€170/month**;
- commercial entitlement: **full ARC Business entitlement** for the currently known/agreed KMS7 scope;
- included: **15 GB managed ARC storage, 15,000 AU/month, up to 10 authorized users, 3 channels, 10 integrations and 40 active automations**;
- normal future Business price remains **€250/month or €2,500/year**;
- the KMS7 discount is a first-business-client / Founding Business exception and does not create a new public tier;
- materially new future scope beyond the agreed Business implementation may still require a change order, Dedicated resources or another explicit arrangement.

Founder working direct-operational-cost ceiling for KMS7: **≤€50/month**, to be measured rather than assumed as proven.

## Customer-facing usage promise

Preferred external promise:

> **One predictable subscription with a clear included allowance. No API keys to manage and no surprise pass-through model bill.**

Do **not** advertise unlimited AI/model consumption.

If a customer structurally exceeds the included tier allowance or creates service-quality risk:

1. optimize the workflow where possible;
2. move/reassign model capacity if appropriate;
3. upgrade tier or add capacity;
4. agree the changed commercial treatment before additional billing applies.

## Standard guardrails

ARC Standard must not silently become a bespoke IT project. Its current launch entitlements are:

- 2 GB managed ARC storage;
- 2,000 AU/month (~2M token-equivalent);
- 1 authorized user;
- 1 primary channel;
- 2 integrations;
- 5 active automations;
- shared infrastructure;
- no dedicated VPS/model capacity by default;
- no 24/7 SLA;
- no unlimited custom workflow engineering or human support.

When needs exceed this shape, move the customer to Pro, Business, Dedicated or a Founder-approved exception.

## Billing tier ≠ maturity/aura tier

Commercial billing tier and ARC maturity are separate concepts.

- Billing tier defines commercial scope, support, storage/usage allowance, integrations and infrastructure.
- V1→V6 defines verified ARC capability maturity.

A customer cannot purchase a false Gold/Platinum/Sovereign aura merely by paying a higher subscription. Higher plans may provide resources that enable additional capabilities, but maturity must remain evidence-derived.

## Current Founding Pilot example — VONDA

- ARC setup: free.
- ARC usage: first **6 months free** on **Standard entitlement**.
- Standard entitlement during pilot: **2 GB managed storage, 2,000 AU/month, 1 user, 1 channel, 2 integrations, 5 active automations**.
- After pilot: **€500/year** or **€50/month** for Standard if continued.
- Basic website: free, indicative standalone value **€250**.
- Personal onboarding session: **€100**.
- FR ↔ NL interpretation attendance: **€100 all-in per requested appointment**.

See `founding-pilots/VONDA.md` for the pilot boundary and learning goals.

## Market-pricing context — snapshot 2026-09-10

Current observed external pricing reinforces that the managed AI-assistant/AI-worker market already exists around and above the ARC Standard price point.

Examples reviewed:

- Hermes Agent France Essential: €49/month;
- Lindy Plus: $29.99/month, with higher usage tiers at $99.99 and $199.99;
- Sintra standard monthly plan: $97/month before promotional discounts.

This does **not** prove ARC pricing is optimal. It means €49–€50 is commercially plausible enough to test rather than being obviously outside the category.

Re-benchmark before public comparative claims or major price changes.

## Margin discipline

Revenue should be evaluated against:

- direct ARC compute/model usage;
- model-capacity pool allocation/reserve;
- shared VPS/platform allocation;
- third-party integrations;
- support time;
- founder implementation/configuration time;
- failure/debug burden;
- payment/admin overhead;
- monitoring/backups/security.

The hidden cost to protect against is **human time**. A €500/year Standard ARC that consumes tens of hours of bespoke support is commercially broken even if server costs are low.

Every paying ARC should therefore become measurable on both:

1. incremental gross margin; and
2. fully loaded contribution after support/admin/platform allocation.

See `ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`, `ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md` and `COST-CAPACITY-MODEL.md` for the usage, capacity and economics rules.
