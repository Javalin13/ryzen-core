# ARC Pricing Model

```yaml
---
type: commercial-model
status: founder-directed-current-working-model
created: 2026-09-03
updated: 2026-09-10
classification: strategic-vision + launch-pricing
currency: EUR
amendable: true-additively
---
```

## Pricing principle

**€500/year is the current minimum commercial floor for a Standard ARC, not the ceiling for the product family.**

Monthly billing is deliberately priced above annual billing to reward commitment and compensate for churn/flexibility.

The customer buys a managed ARC service, not raw model tokens or a Hermes installation.

## Current tier ladder

| Tier | Target customer | Current price direction | Scope principle |
|---|---|---:|---|
| **ARC Standard** | Solo entrepreneur / small operator | **€500/year** or **€50/month** | Telegram ARC, base identity/context, tasks/reminders, light business assistance, normal shared infrastructure, fair-use support/AI usage |
| **ARC Pro** | Growing entrepreneur / small team | **€1,200/year** or **€120/month** | Standard + deeper memory/workflows, calendar/CRM-light, more automation and support |
| **ARC Business** | Company / operational team | **€2,500/year** or **€250/month** | Multiple workflows, business/team context, deeper integrations, reporting, higher usage and governance |
| **ARC Dedicated** | Higher-isolation / heavier operational use | **from €5,000/year** | Dedicated resources/VPS where required, custom integrations, stronger isolation, monitoring and business-critical automation |
| **ARC Enterprise** | Larger organization / multi-ARC deployment | **custom, working floor ~€10,000/year** | Multiple ARCs, API/integrations, governance, dedicated infrastructure, SLA/support and bespoke implementation |

The tiers above Pro are **commercial working hypotheses**, not yet market-validated price points. Standard's €500/year floor and €50/month option are current Founder decisions.

## Founding 20 launch cohort — 2026-09-10

The first commercial validation cohort should consist of up to **20 paying entrepreneurs** recruited primarily through trusted/direct channels before broad paid-media scale.

Working launch offer:

> **Founding ARC — €49/month, founding rate locked while continuously subscribed.**

Rules:

- maximum initial cohort: 20 paying Founding ARCs;
- free setup for Standard-scope onboarding;
- the €49 founding rate is a launch-cohort privilege, not the permanent public Standard price;
- after the Founding 20, normal Standard pricing remains €50/month or €500/year unless the Founder changes it;
- continuity of the founding price may end if the subscription is cancelled and later restarted;
- bespoke integrations, dedicated resources, unusually heavy usage or high-touch support remain outside Standard scope;
- the Founder may pause the cohort before 20 if service quality, support burden, provisioning or model-capacity evidence requires it.

The purpose of Founding 20 is to validate willingness to pay, retention, onboarding repeatability, real usage, support effort and unit economics before scaling advertising.

## Standard customer-facing usage promise

The preferred external promise is:

> **One predictable subscription with standard AI usage included. No API keys to manage and no surprise pass-through model bill.**

Do **not** advertise Standard as unlimited AI/model consumption.

Standard should include normal entrepreneur/personal-business usage on monitored shared infrastructure under fair use.

If a customer's usage structurally exceeds Standard economics or creates service-quality risk, do not silently forward an unexpected provider bill. Instead:

1. optimize the workflow where possible;
2. move/reassign model capacity if appropriate;
3. offer ARC Pro or Dedicated where the workload requires it;
4. agree a clearly priced capacity/usage arrangement before additional billing applies.

Exact public numerical fair-use thresholds should be set only after enough VONDA + Founding-20 production telemetry exists to support them honestly.

## Standard guardrails

ARC Standard must not silently become a bespoke IT project. Standard should exclude or cap:

- unlimited custom integrations;
- dedicated VPS/model capacity by default;
- unlimited AI/model consumption;
- unlimited personal support;
- 24/7 SLA;
- large multi-user permission models;
- custom business-critical workflow engineering;
- continuous bulk-generation or high-frequency autonomous processing.

When those needs appear, move the customer to a higher tier or quote an implementation/capacity fee.

## Billing tier ≠ maturity/aura tier

Commercial billing tier and ARC maturity are separate concepts.

- Billing tier defines commercial scope, support, resource allowance, integrations and infrastructure.
- V1→V6 defines verified ARC capability maturity.

A customer cannot purchase a false Gold/Platinum/Sovereign aura merely by paying a higher subscription. Higher plans may provide resources that enable additional capabilities, but maturity must remain evidence-derived.

## Founding Pilot rule

A Founding Pilot may receive:

- free setup;
- a time-limited free ARC usage period;
- basic adaptations needed to validate the product.

The free period must have an explicit end date/duration. At the end, the customer either:

1. converts to a paid tier;
2. stops using the ARC; or
3. receives a Founder-approved exceptional arrangement.

A free Founding Pilot is distinct from the **paid Founding 20 commercial cohort**.

## Current Founding Pilot example — VONDA

- ARC setup: free.
- ARC usage: first **6 months free**.
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

See `ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md` and `COST-CAPACITY-MODEL.md` for the launch gates, usage policy and operating metrics.