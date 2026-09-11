# ARC Tier Entitlements & Usage Caps

```yaml
---
type: commercial-entitlement-standard
status: founder-directed-current
created: 2026-09-11
classification: commercial-pricing + usage-governance
currency: EUR
supersedes_conflicting_fair_use_deferral: true
amendable: true-additively
---
```

## Purpose

Define the first explicit commercial usage/entitlement limits for ARC Standard, Pro, Business, Dedicated and Enterprise so customers can understand what each package includes and PRIME/OMEGA can meter capacity consistently.

This standard supersedes earlier language that postponed all numerical fair-use limits until after Founding-20 telemetry. Telemetry still matters and may justify later revisions, but the Founder has now directed that launch packages receive concrete initial limits.

Billing tier remains separate from ARC maturity V1→V6. Paying for a larger entitlement does not buy maturity or aura.

## Commercial entitlement matrix — v1.0

| Commercial tier | Current price | Managed ARC storage | Monthly AI allowance | Authorized users | Primary channels | External integrations | Active automations | Infrastructure |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **ARC Standard** | **€50/month or €500/year** | **2 GB** | **2,000 ARC Usage Units / month** (~2M model-token-equivalent) | **1** | **1** | **2** | **5** | shared |
| **ARC Pro** | **€120/month or €1,200/year** | **5 GB** | **6,000 ARC Usage Units / month** (~6M token-equivalent) | **3** | **2** | **5** | **15** | shared / higher allowance |
| **ARC Business** | **€250/month or €2,500/year** | **15 GB** | **15,000 ARC Usage Units / month** (~15M token-equivalent) | **10** | **3** | **10** | **40** | shared business pool or isolated placement when needed |
| **ARC Dedicated** | **from €5,000/year** | **50 GB included baseline** | **40,000 ARC Usage Units / month** (~40M token-equivalent) | **25** | **5** | **20** | **100** | dedicated resources/VPS where required |
| **ARC Enterprise** | **custom; working floor ~€10,000/year** | **custom** | **custom** | **custom** | **custom** | **custom** | **custom** | dedicated / multi-ARC / SLA as contracted |

These are launch entitlements, not claims about hard technical maximums of Hermes, Ollama, VPS infrastructure or model providers.

## ARC Usage Unit definition

One **ARC Usage Unit (AU)** equals approximately **1,000 model tokens-equivalent** of combined model consumption attributable to that ARC, including where measurable:

- owner/user requests;
- ARC responses;
- Brain/Agent model calls;
- background reasoning or automation model calls;
- retries caused by that ARC;
- model-backed website/workflow execution.

Where a provider does not expose token accounting directly, PRIME/RYZ3N may use the closest provider usage-equivalent measurement while preserving the same commercial allowance intent.

The token-equivalent figure is a capacity/accounting unit, not a guarantee that every user message consumes exactly one unit. A simple request may consume less; a multi-step agentic task may consume several units.

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

System security logs, platform telemetry and provider-side backups are managed separately and are not customer-visible storage unless an exceptional workload creates disproportionate retention cost.

## Monthly reset and warnings

AI allowance resets monthly on the billing/entitlement cycle and does not roll over by default.

Storage is persistent and does not reset monthly.

Usage behavior:

- at approximately **80%** of monthly AI allowance, the ARC/RYZ3N service should warn the Owner/customer and surface current consumption;
- at **100%**, RYZ3N does **not** silently charge overage;
- the customer may wait for the monthly reset, upgrade tier, or agree a separately priced capacity add-on;
- safety/security-critical system functions may continue even when customer discretionary AI allowance is exhausted;
- RYZ3N may temporarily restrict abusive, runaway or technically unsafe workloads independent of the commercial cap.

No surprise pass-through provider invoice is allowed.

## Integration definition

An integration is one independently configured external system/service connection that requires ARC credentials, API access, webhook linkage or durable connector configuration.

Examples include Google Drive, Calendar, a CRM, dispatch platform, accounting system or bespoke API.

Multiple workflows inside the same configured integration do not automatically count as separate integrations unless they require materially separate credentials/environments/contracts.

## Automation definition

An active automation is a persistent recurring, triggered or condition-based workflow configured to run without the Owner manually initiating each execution.

Examples include:

- scheduled reports;
- document reminders;
- insurance-expiry checks;
- recurring follow-ups;
- file-processing triggers;
- business monitoring tasks.

One-off tasks do not count as active automations merely because an Agent executes multiple internal steps.

## Channel definition

A primary channel is a persistent customer-facing or owner-facing interface bound to the ARC, for example Telegram, web chat, WhatsApp, email gateway or a later native ARC interface.

Multiple authorized users inside one channel do not create additional channels, but user-count entitlement still applies.

## Founding Pilot entitlement rule

Free Founding Pilot status does **not** mean unlimited use.

Unless the Founder explicitly grants a different entitlement:

- **VONDA ARC** receives **ARC Standard entitlements** during its six-month free Founding Pilot;
- **NARC** receives **ARC Standard entitlements** during its six-month free Founding Pilot;
- both may be shown the complete Standard / Pro / Business / Dedicated / Enterprise ladder from onboarding onward;
- either pilot may voluntarily upgrade commercial entitlement before or after the free pilot without affecting evidence-derived V1→V6 maturity rules;
- after the pilot, continuation at €50/month or €500/year preserves Standard entitlement unless another tier is selected.

## KMS7 Founding Business exception

If Adnan accepts and the Founder authorizes KMS7 ARC creation, KMS7 receives a customer-specific **Founding Business** commercial exception:

- price: **€170/month**;
- entitlement level: **ARC Business**;
- included known scope: Telegram ARC/system, agreed Google Drive/document workflows, driver expense handling, vehicle/insurance tracking, business/marketing assistance, agreed multiple workflows and the currently discussed dispatch-system relationship/integration scope;
- Business entitlement limits: **15 GB managed ARC storage, 15,000 AU/month, up to 10 users, 3 channels, 10 integrations and 40 active automations**;
- normal future ARC Business price remains **€250/month or €2,500/year**;
- the discounted KMS7 price must not become the default Business tariff;
- materially new scope outside the agreed known Business implementation may still require a later change order, higher tier or dedicated resources.

Founder working direct-operational-cost ceiling for KMS7 remains **≤€50/month**, to be verified from real telemetry rather than assumed as proven economics.

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
- monthly AI allowance included and used;
- authorized users;
- channels;
- integrations;
- active automations;
- upgrade options;
- next reset date;
- warning when nearing limits.

## Review rule

These v1.0 limits are concrete commercial launch limits, but not immutable forever.

Review using real VONDA, NARC, KMS7 and Founding-20 telemetry. A future Founder-approved revision may raise, lower or restructure allowances if production evidence shows that margin, usability or infrastructure safety requires it.

Existing accepted customer-specific exceptions must be handled according to their agreement rather than silently changed retroactively.

## Founder shorthand

> **Pilot does not mean unlimited. Standard, Pro and Business must visibly mean something. GB, AI allowance, users, integrations and automations are part of the product. VONDA and NARC start on Standard limits; KMS7 gets Business limits at its €170 Founding Business exception; future Business customers pay €250.**
