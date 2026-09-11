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

## Original pricing question

Does the approximately **€150–€170/month** figure communicated to Adnan match the canonical ARC tier ladder?

## Canonical tier answer

No. The canonical ladder remains:

- **ARC Standard** — €50/month or €500/year.
- **ARC Pro** — €120/month or €1,200/year.
- **ARC Business** — €250/month or €2,500/year.
- **ARC Dedicated** — from €5,000/year.
- **ARC Enterprise** — custom, working floor approximately €10,000/year.

KMS7's known business requirements map most naturally to **ARC Business**.

## Founder superseding commercial decision — 2026-09-11

The Founder clarified that the earlier communicated price was intentionally meant to cover the **complete currently known KMS7 scope**, not only a reduced introductory Phase 1.

Founder decision:

- final intended recurring price for KMS7 if Adnan accepts: **€170/month**;
- KMS7 is treated as the **first Business-class client / Founding Business exception**;
- KMS7 receives **ARC Business entitlements** at that exception price;
- the full currently known KMS7 Business scope is included at that price;
- future comparable Business clients remain at canonical **€250/month / €2,500/year** unless another explicit exception is approved;
- this exception does **not** create a €170 tier and does **not** change `PRICING.md`.

## Business entitlement attached to the KMS7 exception

If accepted and authorized, KMS7 receives:

- **15 GB managed ARC storage**;
- **15,000 ARC Usage Units (AU) / month** (~15M model-token-equivalent);
- up to **10 authorized users**;
- up to **3 primary channels**;
- up to **10 external integrations**;
- up to **40 active automations**;
- Business-class shared infrastructure/capacity placement, with dedicated/isolation treatment only when technically required or separately agreed.

AI allowance resets monthly. Storage persists. Warn around 80%. At 100%, do not silently bill overage; use reset, agreed capacity add-on or a later tier/infrastructure decision.

External Google Drive/dispatch/SaaS data does not count against the 15 GB while it stays external. Persistent ARC-side copies/mirrors do count.

The authoritative entitlement standard is:

`../ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`

## Known KMS7 scope

The known KMS7 scope includes, subject to final acceptance/freeze:

- car dealer + taxi-company operational support;
- Telegram assistant/robot interface;
- Google Drive/document linkage;
- driver document and expense handling;
- vehicle/insurance tracking;
- marketing/business assistance;
- multiple business workflows;
- the previously discussed integration relationship with the existing dispatch application.

“Full scope” means the currently discussed/agreed KMS7 requirement set. It does not mean unlimited future feature requests, unlimited support, unlimited usage, dedicated infrastructure by default or materially new work added after agreement.

## Unit economics

Founder working assumption:

- recurring revenue: **€170/month**;
- direct operational cost ceiling target: **≤ €50/month**;
- direct contribution if that ceiling holds: **≥ €120/month** before Founder support time, shared overhead, tax and administrative cost.

A conservative internal planning figure of approximately €100/month contribution can be used if an additional ~€20/month buffer is reserved, but the direct arithmetic at €170 revenue and €50 direct cost is €120.

The €50 cost ceiling must be verified from real KMS7 usage. It is not yet evidence.

## Commercial rationale

The exception is commercially coherent as a first Business validation case if it produces real evidence on:

- business-class ARC provisioning;
- integration/support burden;
- actual per-client model/infrastructure cost;
- real consumption against the 15,000 AU / 15 GB Business envelope;
- customer retention and willingness to pay;
- scope discipline;
- whether future Business pricing at €250/month has healthy contribution.

The learning value and early reference-client value are part of why the Founder may intentionally price KMS7 below the standard Business rate.

## Guardrails

- Do not change ARC Business from €250/month globally.
- Do not represent €170 as ARC Pro, Business public pricing, Dedicated or a new formal tier.
- Record it as a **Founder-authorized Founding Business exception with Business entitlements**.
- If Adnan never accepts, there is no contract or revenue.
- If he accepts, freeze the included known scope before ARC creation.
- Business entitlement still has numeric usage limits; “full scope” does not mean unlimited consumption.
- Materially new post-agreement scope remains separately reviewable.
- Measure actual cost/support burden from activation onward.

## Related sources

- `KMS7-CARS-ARC-PROPOSAL-2026-09-11.md`
- `../ARC-TIER-ENTITLEMENTS-AND-USAGE-CAPS.md`
- `../PRICING.md`
- `../ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md`
- `../ARC-COMMERCIAL-PIPELINE-2026-09-11.md`
- `Javalin13/prime-vps-migration/ARCS/FOUNDER-DIRECTIVE-2026-09-11-NARC-AND-KMS7-COMMERCIAL-QUEUE.md`

## Current conclusion

> **KMS7 = Business-class scope + Business entitlement at a one-off founding price of €170/month if accepted. Future comparable Business clients = €250/month. The exception validates the Business model; it does not redefine it.**
