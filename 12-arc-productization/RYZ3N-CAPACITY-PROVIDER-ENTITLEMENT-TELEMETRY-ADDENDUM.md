# RYZ3N Capacity Dashboard — Provider Entitlement & Exhaustion Telemetry Addendum

**Status:** Founder-authorized operational addendum  
**Date:** 2026-09-12  
**Parent standard:** `RYZ3N-CAPACITY-TELEMETRY-AND-COST-DASHBOARD-STANDARD.md`

## Purpose

Provider HTTP 429 responses are not all the same. RYZ3N must distinguish concurrency saturation, transient provider rate limiting, legacy subscription session/weekly limits, included-credit exhaustion, purchased-credit exhaustion, and other entitlement failures. Treating all 429s as generic congestion produces incorrect routing and capacity decisions.

## Required provider-pool entitlement metadata

For every shared capacity pool, record the best current truth available:

```text
provider
capacity_pool_id                 # non-secret logical identifier
plan_tier                        # e.g. free/pro/max/team/enterprise/unknown
pricing_regime                   # legacy_session_window | token_credit | metered | unknown
monthly_fixed_cost
currency
included_usage_value             # money/credits/tokens/time if exposed
included_usage_unit
included_usage_used
included_usage_remaining
purchased_credit_balance
billing_period_start
billing_period_reset_at
session_window_limit             # if legacy/provider exposes it
session_window_used
session_window_remaining
weekly_limit                     # if legacy/provider exposes it
weekly_used
weekly_remaining
concurrency_limit
active_concurrency
queue_depth
provider_reported_entitlement_state
last_entitlement_refresh_at
source_of_truth                   # provider_api | provider_ui | founder_config | estimated
```

Unknown values remain `unknown`; never fabricate them.

## Required 429/error classification

A model invocation failure should classify provider errors into at least:

```text
concurrency_limit
queue_full
transient_rate_limit
legacy_session_usage_limit
legacy_weekly_usage_limit
included_usage_exhausted
purchased_credits_exhausted
billing_entitlement_failure
model_unavailable
provider_outage
unknown_429
```

Store the provider's machine-readable error class/code where available, but never secrets or raw customer content.

## Routing behavior

Capacity routing must react to the classified reason rather than the HTTP status alone.

- `concurrency_limit` / `queue_full`: queue, shed lower-priority background work, or use an already-authorized fallback.
- `transient_rate_limit`: bounded retry/backoff, then eligible fallback.
- `legacy_session_usage_limit` / `legacy_weekly_usage_limit`: do not retry-storm. Mark the pool unavailable until the known/estimated reset and use an eligible fallback.
- `included_usage_exhausted`: do not autonomously buy credits. Use already-authorized remaining balance/fallback if policy allows; otherwise escalate Founder.
- `purchased_credits_exhausted` / `billing_entitlement_failure`: fail closed for that paid route and escalate Founder; no autonomous billing changes.
- `unknown_429`: bounded diagnostic check, no repeated blind retries.

## Founder dashboard additions

The capacity dashboard must visibly show, per provider pool:

- pricing regime (legacy-window vs token-credit/metered);
- plan/tier;
- current entitlement state;
- next known reset time/date;
- session/weekly headroom when applicable;
- monthly included-credit headroom when applicable;
- purchased-credit balance when applicable;
- concurrency headroom;
- which ARCs were blocked by entitlement vs congestion;
- exact count of 429s by classified reason;
- forecast of when current capacity will become insufficient;
- the least-cost Founder-authorized scaling option, clearly marked as a recommendation only.

## Current Ollama lesson — 2026-09-12

During the ARC-primary transition master run, Cargo ARC received an Ollama Cloud HTTP 429 whose provider text reported a **session usage limit / billing-or-credit entitlement exhaustion** while the gateway and Telegram transport remained healthy. This proves the dashboard must distinguish account entitlement exhaustion from network/provider congestion.

Current operational rule remains:

```text
AUTONOMOUS_CREDIT_PURCHASE = NO
AUTONOMOUS_TOP_UP = NO
AUTONOMOUS_PLAN_CHANGE = NO
FOUNDER_EXPLICIT_BILLING_AUTHORITY_ONLY = YES
```

The dashboard may recommend a plan/pricing-regime change after current provider truth is checked, but PRIME/OMEGA/ARCs must never perform that billing change autonomously.

## Factory inheritance

Every future ARC telemetry emitter must include enough metadata for the central capacity service to attribute entitlement/rate-limit failures to the ARC and shared capacity pool without storing raw prompts, responses, personal identifiers, API keys, or Owner-private state.
