# PRIME Free-Hosted Primary Model — Macro Analysis Lock — 2026-09-17

Status: **ACTIVE EXECUTION LOCK**
Authority: Founder correction + current provider documentation

## Actual objective

PRIME must have a **strong hosted primary model that works for normal daily use without a metered pay-per-token / pay-per-call dependency**.

The objective is not merely "fallback works." The model fabric must make strong cognition available most of the time.

## Hard constraints

1. Normal PRIME cognition uses a hosted capable model.
2. Primary path is free for normal use; no metered paid API becomes the dependency.
3. Reasoning/coding/tool/agent quality must be strong enough for PRIME and ARC work.
4. Practical daily token/request headroom must fit PRIME's real payload, not a synthetic tiny prompt.
5. No single free provider is assumed to provide production-SLA availability.
6. RYZ3N must remain model/provider/runtime portable.
7. Local small Qwen remains emergency continuity, not the normal brain.

## Correct diagnosis of the observed Laguna failure

Observed live error:

`ResourceExhausted: Worker local total request limit reached (.../32)`

For this event, the evidence points to **provider-side worker/request-capacity saturation**. It is not evidence of:

- PRIME exhausting its context window;
- a daily token allowance being consumed;
- an account-level token quota being depleted.

Those other failure classes remain possible independently and must be measured separately.

## NVIDIA NIM macro implication

NVIDIA documents free hosted NIM endpoints through its Developer Program for prototyping, research, development and testing. NVIDIA explicitly distinguishes that from production service, which requires NVIDIA AI Enterprise licensing.

Therefore NVIDIA/Laguna can remain a useful free development route and specialist/provider in the fabric, but it is **not accepted as the sole long-term dependable free production backbone** merely because the model itself is capable.

Reference:
- https://docs.api.nvidia.com/nim/docs/product
- https://docs.api.nvidia.com/nim/docs/run-anywhere

## Candidate 1 — Cerebras GPT-OSS-120B

Current official public-model metadata reports:

- model: `gpt-oss-120b`;
- max context: **131,072 tokens**;
- reasoning support;
- function/tool calling;
- structured outputs;
- streaming.

Cerebras' published general Free-tier table currently lists for `gpt-oss-120b`:

- **64K TPM**;
- **1M TPH**;
- **1M TPD**;
- **30 RPM**;
- **900 RPH**;
- **14.4K RPD**.

However, Cerebras also currently warns that high demand has caused **temporarily reduced free-tier limits** for `gpt-oss-120b`. Therefore the documentation table is not sufficient acceptance evidence; PRIME must read/test the account's actual current limits.

References:
- https://inference-docs.cerebras.ai/api-reference/models/public-models
- https://inference-docs.cerebras.ai/support/rate-limits
- https://inference-docs.cerebras.ai/models/overview

### Headroom implication

Daily headroom must be judged from real PRIME token use:

`practical turns/day ≈ effective free TPD ÷ average total tokens per PRIME turn`

Example only: a 20K-token heavy turn against a 1M TPD ceiling is roughly 50 turns before output/retry overhead. This is why actual payload measurement and Cognitive Connection reductions are part of model selection, not separate optimization trivia.

## Candidate 2 — Gemini free tier

Google currently provides a Gemini API Free tier with free input/output tokens for eligible models and makes the Free tier available in many regions including the EEA.

`gemini-3.8-flash` is currently listed with free input/output on the Free tier and is positioned for agentic/long-horizon workloads.

Important constraints:

- rate limits are model/project/tier-specific and must be checked in the actual project/AI Studio limits view;
- preview/experimental models can be more restricted;
- Free-tier content may be used to improve Google products.

References:
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/rate-limits
- https://ai.google.dev/gemini-api/docs/billing

Gemini is therefore an independent-provider candidate, not an assumed winner.

## Groq position

Groq remains useful as an independent route, but its published `openai/gpt-oss-120b` limits include materially tighter token headroom than Cerebras' general free table (for example 8K TPM / 200K TPD on the published rate-limit page). With PRIME's current heavy context, this is unlikely to be a first-choice primary unless real workload measurements show otherwise.

Reference:
- https://console.groq.com/docs/rate-limits

## Execution decision

Do **not** switch PRIME blindly.

Phase 1 bakeoff:

1. preserve current Laguna route;
2. add/test Cerebras `gpt-oss-120b` separately;
3. run the same representative PRIME workload against both;
4. capture actual input/output token use, latency, reasoning/tool fidelity, failure rate and account headers/limits;
5. project sustainable workday capacity from measured tokens/turn;
6. only if neither provides sufficient dependable headroom, test Gemini as the next independent free provider;
7. choose primary/secondary roles from evidence.

## Acceptance test for a PRIME primary

A candidate is not accepted because it has a good benchmark score. It must prove:

**quality × availability × free practical headroom × context fit × tool fidelity × provider independence × terms suitability.**

## Stop rule

No more fallback-cosmetic or low-level circuit work unless the primary-model bakeoff shows it materially blocks this objective.

## Macro engineering order

`Founder requirement → hard economic constraint → real workload → provider capacity/headroom → model quality → routing/fallback → adapter details`

Do not reverse this order.
