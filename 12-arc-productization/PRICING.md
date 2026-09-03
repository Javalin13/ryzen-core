# ARC Pricing Model

```yaml
---
type: commercial-model
status: founder-directed-current-working-model
created: 2026-09-03
classification: strategic-vision
currency: EUR
amendable: true-additively
---
```

## Pricing principle

**€500/year is the current minimum commercial floor for a Standard ARC, not the ceiling for the product family.**

Monthly billing is deliberately priced above annual billing to reward commitment and compensate for churn/flexibility.

## Current tier ladder

| Tier | Target customer | Current price direction | Scope principle |
|---|---|---:|---|
| **ARC Standard** | Solo entrepreneur / small operator | **€500/year** or **€50/month** | Telegram ARC, base identity/context, tasks/reminders, light business assistance, normal shared infrastructure, fair-use support/AI usage |
| **ARC Pro** | Growing entrepreneur / small team | **€1,200/year** or **€120/month** | Standard + deeper memory/workflows, calendar/CRM-light, more automation and support |
| **ARC Business** | Company / operational team | **€2,500/year** or **€250/month** | Multiple workflows, business/team context, deeper integrations, reporting, higher usage and governance |
| **ARC Dedicated** | Higher-isolation / heavier operational use | **from €5,000/year** | Dedicated resources/VPS where required, custom integrations, stronger isolation, monitoring and business-critical automation |
| **ARC Enterprise** | Larger organization / multi-ARC deployment | **custom, working floor ~€10,000/year** | Multiple ARCs, API/integrations, governance, dedicated infrastructure, SLA/support and bespoke implementation |

The tiers above Pro are **commercial working hypotheses**, not yet market-validated price points. Standard's €500/year floor and €50/month option are current Founder decisions.

## Standard guardrails

ARC Standard must not silently become a bespoke IT project. Standard should exclude or cap:

- unlimited custom integrations;
- dedicated VPS by default;
- unlimited AI/model consumption;
- unlimited personal support;
- 24/7 SLA;
- large multi-user permission models;
- custom business-critical workflow engineering.

When those needs appear, move the customer to a higher tier or quote an implementation fee.

## Founding Pilot rule

A Founding Pilot may receive:

- free setup;
- a time-limited free ARC usage period;
- basic adaptations needed to validate the product.

The free period must have an explicit end date/duration. At the end, the customer either:

1. converts to a paid tier;
2. stops using the ARC; or
3. receives a Founder-approved exceptional arrangement.

## Current Founding Pilot example — VONKA

- ARC setup: free.
- ARC usage: first **6 months free**.
- After pilot: **€500/year** or **€50/month** for Standard if continued.
- Basic website: free, indicative standalone value **€250**.
- Personal onboarding session: **€100**.
- FR ↔ NL interpretation attendance: **€100 all-in per requested appointment**.

See `founding-pilots/VONKA.md` for the pilot boundary and learning goals.

## Margin discipline

Revenue should be evaluated against:

- direct ARC compute/model usage;
- shared VPS/platform allocation;
- third-party integrations;
- support time;
- founder implementation/configuration time;
- failure/debug burden;
- payment/admin overhead;
- future monitoring/backups/security.

The hidden cost to protect against is **human time**. A €500/year Standard ARC that consumes tens of hours of bespoke support is commercially broken even if server costs are low.
