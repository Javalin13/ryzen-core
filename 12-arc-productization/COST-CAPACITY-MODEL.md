# ARC Cost & Capacity Model

```yaml
---
type: cost-capacity-model
status: working-model
created: 2026-09-03
classification: reality + research-and-exploration
amendable: true-additively
---
```

## Known current shared infrastructure costs

Founder-reported current recurring stack:

| Cost item | Current amount | Treatment for ARC economics |
|---|---:|---|
| Hosting account | **~€25/month** | Shared business/platform overhead unless a client needs dedicated hosting/domain services |
| ChatGPT Plus | **~€25/month** | Founder productivity/tooling overhead; **do not automatically treat as ARC runtime COGS** |
| Ollama Cloud | **~€25/month** | Shared AI/model capacity; allocation per ARC must be measured from real usage |
| VPS | **~€6/month** | Shared runtime infrastructure; allocation depends on safe ARC density and actual resource usage |
| **Current shared monthly stack** | **~€81/month** | Not equivalent to €81/month per ARC |
| **Current shared annual stack** | **~€972/year** | Shared across Founder/product activity; allocation must avoid double-counting overhead |

## Current VPS baseline

Known PRIME VPS baseline from the existing infrastructure work:

- approximately **2 vCPU**;
- approximately **4 GB RAM**;
- approximately **40 GB storage**;
- VPS price around **€6/month**.

The architecture thesis is that ARC nodes remain relatively light on the VPS when heavy model inference is delegated to cloud/model services.

## Important distinction: direct COGS vs shared overhead

### Direct / incremental ARC costs

Costs that should eventually be attributable to a specific ARC where measurable:

- model/API usage caused by that ARC;
- dedicated VPS/resources if required;
- paid third-party integrations;
- domain or external service purchased specifically for that customer;
- backups/storage beyond shared baseline;
- payment processing;
- extraordinary support/implementation labor.

### Shared overhead

Costs that exist even without a specific new ARC:

- Founder's ChatGPT Plus subscription;
- shared hosting account already in use;
- shared base VPS until new capacity is required;
- general development and R&D;
- common monitoring/tooling.

Do not charge the full shared stack to every ARC in margin calculations. Instead, maintain both:

1. **incremental gross margin** — price minus customer-specific costs; and
2. **fully loaded contribution** — price minus a fair share of common infrastructure + support/admin/R&D.

## VPS density assumption

A prior planning assumption used **~10 light ARCs per 4 GB VPS** as a rough economic model.

This is **not a proven capacity limit**.

It must be validated with live measurements of:

- idle RAM per ARC process;
- peak RAM under active use;
- CPU under simultaneous requests;
- disk/log growth;
- Telegram/webhook process footprint;
- retry/background-task behavior;
- model request concurrency;
- failure isolation;
- latency at 1 / 5 / 10+ active ARCs.

At 10 ARCs per €6/month VPS, the raw VPS allocation would be approximately **€7.20 per ARC/year**. That number is useful only as an infrastructure illustration; it excludes AI usage, labor, third-party services, support, tax, admin and risk.

## Standard ARC margin guardrail

Current Standard annual revenue floor: **€500/year**.

A useful working guardrail is to keep technical/direct annual COGS well below the selling price and prevent support time from destroying contribution margin.

Illustrative scenario only:

- Revenue: €500/year.
- If direct + allocated technical cost eventually measures at €100/year, technical contribution before labor/overhead would be €400/year.
- This is **not yet a measured production margin** and must not be presented externally as a proven margin.

## Capacity trigger

Provision another VPS or move heavy customers to Dedicated when one or more thresholds become structurally unsafe:

- memory headroom becomes too small;
- simultaneous usage materially degrades response time;
- customer isolation requirements exceed shared-host capability;
- a single customer creates disproportionate compute/log/storage load;
- operational risk means one failure could impact too many ARC tenants.

The trigger should become metric-based before commercial scale.

## Current unknowns that must be measured

1. Actual Ollama Cloud usage/cost profile per light, medium and heavy ARC.
2. Whether current Ollama plan has practical request/token/concurrency limits relevant to multi-ARC scale.
3. RAM footprint of a duplicated PRIME-derived ARC at idle and under load.
4. Safe number of gateway/Telegram bot processes on the current VPS.
5. Storage/log growth over 30/90/365 days.
6. Support minutes per Standard customer per month.
7. Provisioning time per ARC.
8. Failure rate and intervention burden.
9. Whether additional database/vector/memory infrastructure becomes necessary.
10. Backup/recovery and privacy costs at paid-customer scale.

## Business objective

The economic design target is not merely cheap hosting. It is:

> **recurring revenue grows faster than infrastructure + support + founder-time obligations.**

That requires measurement, automation, tenant isolation and disciplined tier boundaries.
