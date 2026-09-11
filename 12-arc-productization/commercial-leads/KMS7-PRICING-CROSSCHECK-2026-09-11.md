# KMS7 Cars — ARC Pricing Cross-Check

```yaml
---
type: commercial-pricing-crosscheck
status: founder-superseded-assessment
created: 2026-09-11
updated: 2026-09-11
classification: commercial-validation + pricing-alignment
prospect: KMS7 Cars
contact: Adnan
accepted_price: false
arc_creation_authorized: false
founder_exception_price: 170-eur-month
entitlement_if_accepted: arc-business
---
```

## Current conclusion

KMS7 is Business-class in scope. If Adnan accepts, the Founder-authorized exception is **€170/month**, while normal future Business remains **€250/month / €2,500/year**.

The €170 exception does not create a new public tier.

## Corrected Business entitlement

KMS7 receives, if accepted and authorized:

- **15 GB managed ARC storage**;
- **30,000 AU/month**;
- current AU normalization: **1 AU = €0.001 provider-list-price-equivalent AI consumption**;
- therefore Business AI envelope = **€30 normalized AI capacity/month**;
- up to **10 users**;
- up to **3 channels**;
- up to **10 integrations**;
- up to **40 active automations**;
- **6 weighted shared-capacity slots**.

AU is not a fixed token count. Efficient models can provide substantially more raw tokens; premium models consume AU faster.

## Why this is economically coherent

Current public Ollama new-plan pricing checked 2026-09-11 shows Pro at $20/month with $60 monthly usage credits and 3 concurrent requests. The shared-pool model assigns 10 Standard-equivalent slots per pool. KMS7 Business consumes 6 of those slots.

The Founder direct-operational-cost target remains **≤€50/month**. Current VPS/model-subscription allocation can fit below that target if concurrency and third-party variable spend remain controlled, but this must be verified from real telemetry.

## API / platform-cost boundary

KMS7's 10 integration slots do **not** include unlimited third-party vendor spend.

Default rule:

- paid provider subscriptions/API/message/transaction costs are customer-funded;
- RYZ3N-funded variable third-party spend is **€0 by default** unless a specific capped allowance is explicitly agreed;
- free-tier/free-call integrations may operate normally;
- no Agent/Brain/ARC can autonomously buy credits, seats, phone numbers, message packs, storage or provider capacity;
- any RYZ3N-funded provider allowance warns at 80% and hard-stops at 100%;
- recurring automations must have retry/concurrency/runaway-spend controls.

A customer preference for a more expensive platform does not automatically transfer its cost to RYZ3N.

## Known KMS7 scope

Subject to final acceptance/freeze:

- car dealer + taxi-company operational support;
- Telegram assistant/robot interface;
- Google Drive/document linkage;
- driver document and expense handling;
- vehicle/insurance tracking;
- marketing/business assistance;
- multiple workflows;
- discussed integration relationship with the existing dispatch application.

“Full scope” does not mean unlimited future feature requests, unlimited support, unlimited AI consumption, unlimited third-party API spend or automatic Dedicated infrastructure.

## Unit economics

Founder working target:

- revenue: **€170/month**;
- direct operational cost ceiling: **≤€50/month**;
- direct contribution if ceiling holds: **≥€120/month** before Founder support time, shared overhead, tax/admin.

## Guardrails

- Business public price remains €250/month.
- KMS7 exception is customer-specific.
- If Adnan never accepts, there is no contract or revenue.
- If he accepts, freeze included scope and integration billing ownership before ARC creation.
- Measure AU, pool allocation, VPS, any RYZ3N-funded vendor spend, support and incidents from activation.

## Related sources

- `KMS7-CARS-ARC-PROPOSAL-2026-09-11.md`
- `../ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`
- `../ARC-VARIABLE-COST-AND-API-BOUNDARY.md`
- `../COST-CAPACITY-MODEL.md`
- `../PRICING.md`
- `Javalin13/prime-vps-migration/ARCS/FOUNDER-DIRECTIVE-2026-09-11-NARC-AND-KMS7-COMMERCIAL-QUEUE.md`
