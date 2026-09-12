# RYZ3N Client Capacity, Support & Infrastructure Scaling Ladder

**Status:** Founder-authorized scaling framework  
**Date:** 2026-09-12  
**Scope:** PRIME, OMEGA, Factory, current ARCs and future ARC population growth

## 1. Founder scaling concern

The current infrastructure/model decision cannot be evaluated only for today's 3 Owner ARCs. The capacity model must explicitly forecast the path from the current pilot population toward **10, 20, 40, 50 and 100 ARCs**.

A critical real-world signal already exists:

> Founder reported that the current legacy Ollama Pro weekly allowance was exhausted by the Founder alone within only a few hours of intensive RYZ3N/ARC work.

Exact elapsed productive hours, tokens and provider-side units are not yet measured, so no false precision may be invented. The operational evidence is still decisive: **one heavy RYZ3N operator can exhaust the current legacy weekly Ollama allowance in one intensive work session/day.**

If 3 additional ARC Owners behaved similarly, a simple stress model implies roughly four heavy-user-equivalents competing for the same cloud pool. This does not mean wall-clock exhaustion is exactly 4x faster; caching, task mix, concurrency and prompt lengths differ. It does mean the current legacy cloud allowance is not a viable normal inference pool for PRIME plus a growing ARC population.

This is a primary reason for the current architecture:

```text
PRIME
  primary  = Ollama Cloud / minimax-m3:cloud
  fallback = local Ollama / qwen3:0.6b

Cargo / NARC / VONDA
  primary  = local Ollama / qwen3:0.6b
  fallback = NONE
```

## 2. What must be measured per Owner and ARC

For scaling decisions, telemetry must track non-content operational data for each ARC/Owner cohort:

- human turns;
- model calls per human turn;
- input/cached/output tokens where exposed;
- peak concurrent requests;
- p50/p95 latency;
- queue wait and rejected/failed requests;
- local CPU/RAM/swap pressure;
- tool/function-call success rate;
- local-model quality escalations;
- cloud fallback events for PRIME;
- support minutes/incidents per Owner;
- Founder/operator interventions;
- allocated infrastructure cost;
- equivalent cloud-model cost;
- ARC revenue and contribution margin where commercial.

Private prompts, responses, memories and transport IDs remain excluded.

## 3. Heavy-owner equivalence model

The Founder workload becomes an empirical **heavy-owner reference cohort** until enough real Owner telemetry exists.

For planning only, define:

- `1.00 FHE` = one Founder-heavy-equivalent workload;
- light Owner = illustrative `0.15 FHE`;
- ordinary active Owner = illustrative `0.35 FHE`;
- heavy Owner = illustrative `1.00 FHE`.

These coefficients are planning assumptions, not measured facts, and must be replaced by real cohort data as Narek, Laetitia, Maria and future Owners generate evidence.

Illustrative ARC-owner demand, excluding PRIME/Founder load:

| ARC Owners | Light cohort 0.15x | Ordinary cohort 0.35x | Heavy cohort 1.00x |
| ---: | ---: | ---: | ---: |
| 3 | 0.45 FHE | 1.05 FHE | 3 FHE |
| 10 | 1.5 FHE | 3.5 FHE | 10 FHE |
| 20 | 3 FHE | 7 FHE | 20 FHE |
| 40 | 6 FHE | 14 FHE | 40 FHE |
| 50 | 7.5 FHE | 17.5 FHE | 50 FHE |
| 100 | 15 FHE | 35 FHE | 100 FHE |

The Founder/PRIME workload is additional. At today's 3 Owner ARCs, a worst-case Founder + 3 heavy Owners is approximately **4 FHE**.

## 4. Scale gates: 3 -> 10 -> 20 -> 40 -> 50 -> 100 ARCs

### Current: 3 Owner ARCs

Goal: prove the architecture and collect real cohort telemetry.

Current lowest-cost posture:

- Hetzner CX23 application/inference host;
- qwen3:0.6b shared local ARC primary;
- PRIME alone on Ollama Cloud M3 primary;
- no normal cloud fallback for ARCs.

Upgrade earlier than the next population milestone if Owner latency, swap pressure, failures, quality, support burden or concurrency are already unacceptable.

### Around 10 ARCs

Do not automatically buy capacity at ARC #10. Evaluate:

- how many of the 10 are actually active weekly;
- peak simultaneous Owners;
- qwen3:0.6b task success;
- CPU/RAM/swap headroom;
- support burden;
- cost per active Owner.

Likely paths if pressure is material:

- move from CX23 toward a 16-32 GB cost-optimized node when available;
- use a stronger local model if quality, not concurrency, is the limiting factor;
- separate background work from interactive work;
- preserve PRIME cloud independence.

### Around 20 ARCs

Expect shared-local inference to require intentional queue/concurrency management even if not all Owners are active at once.

Consider separating application/control workloads from inference if:

- local generations materially delay gateways/services;
- swap becomes routine rather than emergency-only;
- support incidents arise from resource contention;
- one-node failure affects too much of the customer population.

A dedicated inference node becomes a serious option here even if total raw RAM could still fit on one larger VPS.

### Around 40 ARCs

At this population, capacity planning should be cohort-based rather than server-size-based.

Required questions:

- active Owners/day and peak concurrent Owners;
- inference seconds per human turn;
- model mix and context size;
- average/95th percentile queue depth;
- cost per successful work cycle;
- incident/support load per 100 Owner sessions.

Likely architecture: separate production/control node plus one or more dedicated inference workers. CPU-only versus GPU must be decided from measured cost per completed Owner task.

### Around 50 ARCs

Treat inference as a pooled service rather than a feature of one VPS.

Requirements should include:

- worker health and draining;
- bounded scheduling/queueing;
- per-ARC attribution;
- no cross-ARC memory/state leakage;
- capacity reservation for interactive work;
- background-work throttling;
- failure-domain isolation;
- Founder/OMEGA capacity forecasts.

The next purchase should be justified by forecasted demand and margin, not by round-number client count.

### Around 100 ARCs

One shared small CPU model process is no longer an adequate architecture even if average traffic appears low.

Plan for an **inference fabric**:

```text
PRIME / OMEGA capacity steward
        |
        +-- production/control services
        |
        +-- inference worker pool
        |     +-- worker A
        |     +-- worker B
        |     +-- worker C / GPU pool as justified
        |
        +-- bounded queue / scheduler
        +-- telemetry + cost attribution
        +-- health / fail-closed controls
```

100 ARCs does not imply 100 model copies. Shared inference remains the goal, with isolation at ARC identity/memory/runtime boundaries and pooled compute measured centrally.

## 5. Hetzner pathways currently under consideration

Provider pricing/availability must be refreshed before any purchase. Founder approval is mandatory.

### CX23 — current

- 2 vCPU;
- 4 GB RAM;
- 40 GB disk;
- observed Founder-console price: EUR 6.64/month in Belgian VAT display context.

Use as long as qwen3:0.6b + live runtimes remain safe and Owner service remains acceptable.

### CX43 — intermediate cost-optimized path

Current Germany/Finland public reference after June 2026 adjustment:

- EUR 15.99/month ex VAT;
- Founder console showed EUR 19.35/month incl. 21% VAT;
- 8 vCPU / 16 GB RAM class from Founder console.

Useful intermediate capacity, but 16 GB should not be assumed safe for a full production stack plus gpt-oss:20b without measured proof.

### CX53 — preferred 32 GB cost-optimized step when available

Current Germany/Finland public reference:

- EUR 29.49/month ex VAT;
- Founder console showed EUR 35.68/month incl. 21% VAT;
- 16 vCPU / 32 GB RAM class from Founder console.

This was unavailable in the Founder-visible pool on 2026-09-12. Availability is therefore a real constraint.

### CAX41 — ARM alternative

Current Germany/Finland public reference:

- EUR 40.99/month ex VAT;
- 16 ARM vCPU / 32 GB class.

Only consider after validating Ollama, Hermes and chosen-model compatibility/performance on ARM.

### CPX52 — regular-performance premium path

Correct product name is **CPX52**, not CX52.

Current Germany/Finland public reference:

- EUR 100.49/month ex VAT;
- Founder console showed EUR 121.59/month incl. 21% VAT;
- 12 AMD vCPU / 24 GB RAM class from Founder console.

This is not the default next step because the monthly price is high relative to cost-optimized RAM capacity. Consider only when CPU consistency/latency is measured to justify the premium or cost-optimized capacity remains unavailable.

### Dedicated / Server Auction

Observed examples on 2026-09-12, not purchased:

- Xeon E5-1650v3 / 64 GB / 2x480 GB Datacenter SSD — EUR 58.70/month ex VAT;
- Ryzen 5 3600 / 64 GB / 2x2 TB Enterprise HDD — EUR 62.70/month ex VAT.

Dedicated inference becomes attractive when isolation, 64 GB+ RAM, predictable CPU, or multiple concurrent Owners are worth more than keeping everything on one shared VPS.

## 6. Ollama Cloud pathways

Current public pricing verified 2026-09-12. The Founder account is believed to remain on **legacy Pro** while it auto-renews, so actual account rules override new-plan references until changed.

### Legacy Pro — current Founder evidence

- historical session/weekly limits apply;
- Founder alone reported reaching the weekly allowance within a few hours of intensive work;
- therefore unsuitable as the shared normal ARC pool at scale.

Do not infer exact token value from the legacy weekly limit unless Ollama exposes it.

### New Pro

- USD 20/month or USD 200/year;
- USD 60 monthly usage credits;
- 3 concurrent requests;
- no old 5-hour/weekly usage limits;
- usage beyond included credits can continue at published per-token pricing using additional credits;
- switching from a legacy plan resets usage and moves the account to the new pricing model.

Potential role: PRIME-only cloud route if the economics remain favorable.

### Max

- USD 100/month;
- USD 300 monthly usage credits;
- 10 concurrent requests;
- early access to newer models.

Evaluate Max when PRIME concurrency/usage actually approaches Pro constraints and when `Max fixed cost + included usage` beats `Pro + incremental credits` or materially improves service quality.

### Team — the official team/business-scale Ollama path

Ollama's current official plan name is **Team**, not Business:

- USD 500/month introductory price;
- USD 1,000 shared monthly usage credits;
- unlimited users;
- 10 concurrent requests;
- centralized billing/administration;
- priority support.

Potential future role: RYZ3N organization-wide cloud capacity only if real Owner/agent demand and support requirements justify it. Under the current local-first ARC architecture it is not needed merely because ARCs exist.

### Enterprise

- custom pricing;
- Team features plus model access controls, per-user/API-key budgets, dedicated support channel and custom security work.

Consider only when RYZ3N reaches genuine organization/enterprise-scale cloud requirements or contractual support/security needs.

## 7. Cloud versus local decision formula

At each scale checkpoint compare:

```text
LOCAL MONTHLY COST
= application/control infrastructure
+ inference infrastructure
+ storage/network attributable cost
+ operational/support burden

CLOUD MONTHLY COST
= fixed Ollama plan
+ incremental usage credits/overage
+ other provider usage
+ cloud-related support burden
```

Also compare service value:

- model quality;
- latency;
- peak concurrency;
- availability;
- privacy;
- failure domains;
- operational complexity.

Do not choose local merely because marginal API cost is zero. Do not choose cloud merely because initial infrastructure is easy.

## 8. Capacity triggers

PRIME/OMEGA should surface a Founder decision when one or more persist:

- p95 local queue/latency breaches the service target;
- swap is routinely used for active model working memory;
- CPU saturation causes ARC/gateway contention;
- model quality creates repeated human rework/support;
- temporary-unavailable rate grows;
- cloud pool reaches 70/85/95% of known included capacity;
- PRIME fallback frequency becomes material;
- support minutes per active Owner increase materially;
- forecast next-cohort demand exceeds safe headroom;
- infrastructure cost per active Owner or contribution margin crosses Founder-set thresholds.

No threshold purchases capacity autonomously. It creates a Founder recommendation with evidence and alternatives.

## 9. Required Founder dashboard cohort views

The dashboard must support scenario views for at least:

- current 3 Owner ARCs;
- 10 ARCs;
- 20 ARCs;
- 40 ARCs;
- 50 ARCs;
- 100 ARCs.

For each scenario show:

- projected active Owners;
- projected FHE demand range;
- estimated concurrency;
- estimated CPU/RAM/inference-worker requirement;
- projected Ollama equivalent usage/cost;
- projected Hetzner/local infrastructure cost;
- expected support burden;
- recommended architecture stage;
- confidence level and assumptions.

As real cohort data arrives, projections must automatically replace illustrative FHE assumptions with measured distributions.

## 10. Commercial rule

Standard / Pro / Business remain RYZ3N commercial product tiers where defined, but infrastructure scaling is a backend service-allocation decision. A customer tier must not silently weaken privacy, identity isolation or governance.

Higher-value service tiers may justify:

- higher queue priority;
- stronger model allocation where available;
- greater concurrency reservation;
- faster support response;
- more automation/integrations;

only when those differences are explicitly part of the commercial product and remain within canonical ARC boundaries.

---

**Founder decision:** design for 100 ARCs now at the telemetry/economics layer, but buy capacity only when measured usage, service quality, support burden and unit economics justify the next infrastructure stage.