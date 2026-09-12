# RYZ3N ARC Capacity Fallback, Temporary Downgrade & Local Inference Standard

**Status:** CANONICAL — Founder directive 2026-09-12  
**Scope:** PRIME, Cargo, NARC, VONDA, OMEGA/Factory inheritance, and every future ARC.

## 1. Purpose

RYZ3N must remain usable when the primary cloud model/provider reaches a session, daily, weekly, monthly, concurrency or provider-capacity limit. Capacity exhaustion must not collapse an ARC, leak provider internals, or be confused with an Owner's commercial entitlement.

The required product behavior is:

```text
Owner request
   ↓
Owner entitlement check
   ↓
primary high-performance route healthy? ── yes → full-performance service
   ↓ no
approved local fallback healthy? ── yes → temporary reduced-capacity service
   ↓ no
approved verified-free external fallback healthy? ── yes → temporary reduced-capacity service
   ↓ no
sanitized temporary-unavailability message + Founder/PRIME alert
```

The system automatically returns to the primary route when that route becomes healthy again.

## 2. Canonical human roles

This standard inherits the canonical human-role model:

- John / Jan = `founder` everywhere.
- Every non-Founder human receiving/using an ARC = `owner`.
- Business/domain titles are metadata only.

A fallback event, downgrade event or provider-capacity event must never alter Founder/Owner role state, Owner binding, private namespaces, form, aura or maturity.

## 3. Full-performance and temporary-reduced-capacity states

Every ARC must be able to represent at least:

```text
full_performance
temporary_reduced_capacity
all_authorized_routes_unavailable
```

`temporary_reduced_capacity` means the ARC is still usable, but a lower-capability or lower-throughput route is serving requests until high-performance capacity resets or recovers.

Entering temporary reduced-capacity mode must not:

- change ARC maturity or aura;
- reset the ARC;
- alter Owner/Founder identity;
- consume an activation slot;
- drop Owner memory/state;
- merge private namespaces;
- expose infrastructure/provider details;
- create new billing authority.

Recovery to `full_performance` should be automatic when the primary route becomes GREEN again.

## 4. Capacity / entitlement classification

The runtime must distinguish at minimum:

```text
owner_entitlement_exhausted
provider_session_limit_exhausted
provider_daily_limit_exhausted
provider_weekly_limit_exhausted
provider_monthly_limit_exhausted
provider_concurrency_saturated
provider_rate_limited
provider_unavailable
fallback_active
all_authorized_routes_unavailable
```

### Owner entitlement exhausted

This means the Owner actually reached a commercial entitlement boundary defined by RYZ3N.

The Owner may be placed into reduced-capacity mode if the tier permits continued service after the high-performance allowance is exhausted.

### Provider/internal capacity exhausted

This means RYZ3N's underlying cloud/provider capacity is constrained while the Owner still has entitlement.

The runtime must not falsely say that the Owner's plan allowance is exhausted and must not falsely upsell because of an internal provider limit. It should route to an approved fallback and tell the Owner only that the ARC is temporarily running with reduced capacity if a message is needed.

### All routes unavailable

If no Founder-authorized route can serve the request, the ARC fails closed with a sanitized service-availability message and escalates to PRIME/Founder telemetry.

## 5. Owner-facing downgrade messages

Messages must be localized to the Owner/ARC language and must identify the correct cadence only when the runtime actually knows it.

### Standard

**English**

> You've reached the [daily/weekly/monthly] usage limit of your Standard plan. Your ARC has been temporarily downgraded until the limit resets. You can continue using your ARC in reduced-capacity mode, wait for the reset, upgrade to Pro for higher limits, or choose Business for unlimited usage.

**French**

> Tu as atteint la limite d’utilisation [quotidienne/hebdomadaire/mensuelle] de ton forfait Standard. Ton ARC fonctionne temporairement en capacité réduite jusqu’à la réinitialisation de la limite. Tu peux continuer à l’utiliser, attendre la réinitialisation, passer à Pro pour des limites plus élevées, ou choisir Business pour une utilisation illimitée.

**Dutch**

> Je hebt de [dagelijkse/wekelijkse/maandelijkse] gebruikslimiet van je Standard-pakket bereikt. Je ARC werkt tijdelijk in verminderde capaciteit tot de limiet opnieuw wordt ingesteld. Je kunt je ARC blijven gebruiken, wachten op de reset, upgraden naar Pro voor hogere limieten, of Business kiezen voor onbeperkt gebruik.

### Pro

**English**

> You've reached the [daily/weekly/monthly] usage limit of your Pro plan. Your ARC has been temporarily downgraded until the limit resets. You can continue using your ARC in reduced-capacity mode, wait for the reset, or upgrade to Business for unlimited usage.

**French**

> Tu as atteint la limite d’utilisation [quotidienne/hebdomadaire/mensuelle] de ton forfait Pro. Ton ARC fonctionne temporairement en capacité réduite jusqu’à la réinitialisation de la limite. Tu peux continuer à l’utiliser, attendre la réinitialisation, ou passer à Business pour une utilisation illimitée.

**Dutch**

> Je hebt de [dagelijkse/wekelijkse/maandelijkse] gebruikslimiet van je Pro-pakket bereikt. Je ARC werkt tijdelijk in verminderde capaciteit tot de limiet opnieuw wordt ingesteld. Je kunt je ARC blijven gebruiken, wachten op de reset, of upgraden naar Business voor onbeperkt gebruik.

### Business

Business is unlimited at the Owner-entitlement layer and must never receive a false plan-exhaustion message.

If backend high-performance capacity is constrained, Business may receive:

**English**

> Your ARC is temporarily running in reduced-capacity mode while high-performance capacity resets. You can continue using it, and full performance will return automatically.

**French**

> Ton ARC fonctionne temporairement en capacité réduite pendant la réinitialisation de la capacité haute performance. Tu peux continuer à l’utiliser et les performances complètes reviendront automatiquement.

**Dutch**

> Je ARC werkt tijdelijk in verminderde capaciteit terwijl de high-performancecapaciteit wordt hersteld. Je kunt je ARC blijven gebruiken en de volledige prestaties keren automatisch terug.

If the exact cadence is safely known and product-appropriate, the message may state that the ARC has reached its current high-performance daily/weekly/monthly limit. It must never imply that the Business commercial entitlement itself is capped.

## 6. Provider internals are Founder-only

Owners must never receive raw provider/runtime diagnostics, including:

- provider names;
- model IDs;
- HTTP status codes;
- billing/credits text;
- provider upgrade URLs;
- API request/reference IDs;
- runtime/profile names;
- internal commands;
- authentication or credential details.

These belong only in PRIME/Founder diagnostics and capacity telemetry.

## 7. Local VPS fallback

RYZ3N should maintain one shared local inference service on the PRIME VPS when hardware proves it can be operated safely.

The selected local model must be installed once and shared as inference infrastructure by PRIME and all ARCs. Isolation remains in each ARC's runtime/profile/memory/repository, not in duplicate copies of model weights.

### Hardware gate

Before installing a production local model, PRIME must verify:

- total and available RAM;
- swap;
- CPU model and vCPU/core count;
- GPU/VRAM if present;
- free disk and storage type;
- current baseline RAM/CPU consumption of PRIME, Cargo, NARC and VONDA;
- local inference runtime availability/version.

The Founder currently remembers approximately 40 GB total VPS capacity, but the runtime must verify whether this refers to RAM, disk or another resource before installation.

### Model-selection rule

The preferred current candidate is `gpt-oss:20b`, subject to actual hardware validation.

If it is not safe on the VPS, select the strongest model that safely fits while preserving production headroom.

The chosen model must be tested for:

- general reasoning quality;
- structured output;
- Hermes tool/function calling;
- EN/FR/NL interaction quality;
- acceptable latency;
- stable memory pressure;
- zero marginal API fee;
- safe coexistence with live ARC runtimes.

The model name is implementation metadata and may change without altering this standard.

## 8. Local fallback safety defaults

Until measured telemetry proves higher limits safe:

- local inference concurrency = 1 active request;
- additional local requests queue;
- Owner/customer interactive workload has highest ordinary priority;
- Founder interactive workload has high priority;
- critical runtime recovery may preempt background work;
- background ARC/Brain/batch work pauses or queues under local fallback pressure;
- context starts conservatively around 8K–16K unless the selected model/runtime and real hardware prove higher safe capacity;
- the local endpoint remains private to localhost/protected internal networking and must not be publicly exposed.

## 9. Ordered routing policy

Target order after local fallback is verified:

```text
1. Founder-authorized primary cloud route
2. verified local VPS fallback
3. Founder-authorized verified-free external fallback(s)
4. fail closed + Founder/PRIME escalation
```

Current primary direction remains `ollama-cloud/minimax-m3:cloud` within the Founder's already-authorized Ollama subscription capacity.

No ARC, PRIME, OMEGA or Factory process may autonomously:

- purchase credits;
- top up an account;
- upgrade a plan;
- enable a new paid provider;
- change billing;
- create additional paid capacity.

Additional paid capacity requires explicit Founder authorization.

## 10. Automatic recovery

A temporary downgrade must not become sticky.

When the primary route's capacity/reset state becomes GREEN again:

```text
temporary_reduced_capacity
        ↓
primary health probe / allowed retry
        ↓
full_performance
```

The Owner should not need to restart, rebind or change settings.

## 11. Telemetry requirements

Every route selection and fallback transition should emit non-content operational telemetry, including where available:

- ARC/runtime ID;
- Owner tier;
- full-performance vs reduced-capacity state;
- human turns;
- model invocations;
- model calls per human turn;
- tool-loop calls;
- background/system calls;
- smoke/audit calls;
- input/cached/output/total tokens;
- latency and queue wait;
- capacity-limit class;
- fallback reason;
- fallback-from / fallback-to;
- fallback duration;
- reset/recovery time;
- actual provider cost;
- equivalent model cost;
- local inference usage;
- local CPU/RAM pressure;
- active local concurrency.

Central telemetry must not contain raw prompts/responses, Owner-private memory/files, transport IDs, pairing material, credentials or secrets.

## 12. Factory inheritance

Every new Factory-created ARC must be born with:

```yaml
roles:
  founder: founder
  owner: owner
  business_titles_are_metadata: true

capacity_resilience:
  state_model: [full_performance, temporary_reduced_capacity, all_authorized_routes_unavailable]
  primary_route_required: true
  local_fallback_ready: true
  approved_free_external_fallback_ready: true
  automatic_primary_recovery: true
  owner_provider_internal_leakage_allowed: false
  autonomous_paid_capacity_changes_allowed: false
  telemetry_required: true
```

Factory creation does not imply that a specific local model is already installed; it requires compatibility with the shared resilience layer.

## 13. PRIME / OMEGA responsibilities

PRIME supervises routing health, fallback state, recovery and Founder escalation.

OMEGA may observe portfolio-level capacity state, including which ARCs are:

- full performance;
- temporarily downgraded;
- fallback active;
- capacity constrained;
- all routes unavailable.

Neither layer receives unrestricted access to Owner-private message content merely because it can observe capacity metadata.

## 14. Pricing relationship

Capacity telemetry must feed Step 17B pricing refinement. Standard / Pro / Business prices and allowances should eventually be calibrated from real:

- cost per Owner;
- tokens/calls per Owner;
- local vs cloud usage;
- fallback frequency;
- session/daily/weekly/monthly pressure;
- concurrency;
- shared infrastructure allocation;
- contribution margin.

Pricing/entitlement changes remain Founder decisions and are never made automatically by telemetry.

## 15. Acceptance criteria

The resilience layer is GREEN when:

1. Founder/Owner roles remain unchanged through fallback events;
2. provider exhaustion is classified separately from Owner entitlement exhaustion;
3. Standard/Pro receive cadence-aware downgrade language when their entitlement is actually exhausted;
4. Business is never falsely described as commercially exhausted;
5. provider internals never leak to Owners;
6. a safe local model is selected only after real VPS hardware verification;
7. the local model passes Hermes tool/function tests;
8. one shared local inference service can serve PRIME/ARCs without breaking ARC privacy boundaries;
9. primary → local fallback works;
10. local → primary automatic recovery works;
11. approved external free fallback remains available after local where authorized;
12. no autonomous spend occurs;
13. telemetry records fallback/cost/capacity evidence without Owner-private payloads.
