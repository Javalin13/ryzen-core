# KMS7 Cars — ARC Pricing Cross-Check

```yaml
---
type: commercial-pricing-crosscheck
status: current-assessment
created: 2026-09-11
classification: commercial-validation + pricing-alignment
prospect: KMS7 Cars
contact: Adnan
accepted_price: false
arc_creation_authorized: false
---
```

## Question

Does the approximately **€150–€170/month** figure communicated to Adnan on 2026-09-11 match the current canonical ARC pricing ladder?

## Canonical answer

No. It does not correspond to an existing canonical tier.

Current working tier ladder in `../PRICING.md`:

- **ARC Standard** — €50/month or €500/year.
- **ARC Pro** — €120/month or €1,200/year.
- **ARC Business** — €250/month or €2,500/year.
- **ARC Dedicated** — from €5,000/year.
- **ARC Enterprise** — custom, working floor approximately €10,000/year.

Therefore **€150–€170/month is an in-between Founder-communicated figure**, above Pro and below Business. It must not become a new tier by accident.

## KMS7 scope mapping

Previously discussed KMS7 needs include, subject to reconfirmation with Adnan:

- car dealer + taxi-company operational support;
- Telegram assistant/robot interface;
- Google Drive/document linkage;
- driver document and expense handling;
- vehicle/insurance tracking;
- marketing/business assistance;
- possible integration with the existing dispatch application;
- multiple business workflows rather than only personal assistance.

That overall shape fits **ARC Business** more closely than ARC Pro because Business is the canonical tier for company/team context, multiple workflows, deeper integrations, reporting, higher usage and stronger governance.

If the dispatch integration becomes custom, technically burdensome, business-critical or requires stronger isolation/dedicated resources, **ARC Dedicated and/or a separate implementation fee** should be considered.

## Commercial treatment of the price already communicated

Do not retract or rewrite the historical voice-message figure. The truthful commercial state is:

- Founder communicated approximately €150–€170/month;
- Adnan has not accepted it yet;
- no final scope exists yet;
- therefore no final tier/contract price exists yet.

If Adnan responds positively, use one of these paths:

### Path A — bounded introductory Phase 1

Keep the approximately €150–€170/month figure as a **Founder-authorized introductory/pilot exception** only if Phase 1 is deliberately bounded, for example Telegram-first assistance plus selected light workflows/Drive support without committing to the entire original bespoke integration burden.

### Path B — full known business scope

If KMS7 wants the broader known scope — multiple operational workflows, deeper Drive/data processes, vehicle/insurance/expense automation, team/business context and meaningful system integration — use **ARC Business €250/month** as the canonical commercial reference.

### Path C — heavy/custom integration

If KMS7 requires deep integration with the existing dispatch system, dedicated infrastructure, stronger service availability or substantial implementation work, move toward **ARC Dedicated / separate implementation pricing** rather than absorbing the work into a discounted monthly plan.

## Guardrail

The Founder quote is sales history, not pricing canon.

> **Communicated price ≠ canonical tier. Final price follows confirmed scope.**

Do not alter `PRICING.md` merely to make the KMS7 quote fit.

## Related sources

- `KMS7-CARS-ARC-PROPOSAL-2026-09-11.md`
- `../PRICING.md`
- `../ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md`
- `../ARC-COMMERCIAL-PIPELINE-2026-09-11.md`
- `Javalin13/prime-vps-migration/ARCS/FOUNDER-DIRECTIVE-2026-09-11-NARC-AND-KMS7-COMMERCIAL-QUEUE.md`
