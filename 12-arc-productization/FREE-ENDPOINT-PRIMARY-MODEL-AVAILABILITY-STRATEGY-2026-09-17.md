# Free-Endpoint Primary Model Availability Strategy — 2026-09-17

Status: ACTIVE PRIORITY CORRECTION
Authority: Founder-directed constraint clarification

## Non-negotiable constraints

PRIME's main operating model path must prioritize:

1. no variable pay-per-call / per-token API billing for the normal primary path;
2. strong enough reasoning, coding, tool use and agentic behavior for PRIME;
3. usable most of the day under normal Founder workload;
4. no tiny daily request cap that makes ordinary operation impractical;
5. provider/runtime portability under the RYZ3N Cognitive Connection architecture;
6. independent fallback providers so one provider's capacity event does not disable the whole stack.

Paid first-party API recommendations do not satisfy the current Founder constraint and must not be presented as the default solution.

## Laguna/NVIDIA evidence correction

The observed live error was:

`ResourceExhausted: Worker local total request limit reached (259/32)`

This is not evidence of PRIME rapidly consuming its context/token budget or account token allowance. The error names a worker-local request ceiling and matches current reports on NVIDIA-hosted free endpoints where upstream serving capacity is exhausted.

NVIDIA's own Developer Program documentation describes the hosted NIM API Catalog as free for prototyping/development but explicitly notes that rate/latency can vary with concurrent users and that the no-cost catalog may experience extended waits under high load.

Therefore:

- Laguna's model capability is not disproven;
- the current NVIDIA-hosted free serving path is not sufficiently dependable by itself to be PRIME's only primary availability dependency;
- context/token pressure remains a separate engineering concern and should be measured separately from provider worker saturation.

## Macro engineering conclusion

There is no assumption that one free hosted endpoint will provide frontier-quality intelligence, unlimited throughput and production-grade availability simultaneously.

The correct architecture is a **free multi-provider model fabric**:

`RYZ3N cognition policy -> strongest healthy free primary -> independent free secondary -> NVIDIA free specialist/secondary -> local emergency continuity`

Provider diversity is a first-class availability primitive, not merely a fallback afterthought.

## Current candidate direction

### Cerebras Inference — GPT-OSS-120B

Strong candidate for primary bakeoff because current Cerebras documentation exposes a free tier and lists GPT-OSS-120B as a production model with reasoning, tools/function calling and structured outputs. Published free-tier limits are approximately 30 RPM, 64K TPM, 1M TPD and 14.4K RPD, subject to account-specific/current adjustments. Cerebras also notes temporary free-tier reductions under high demand, so this must be measured in PRIME rather than assumed GREEN.

### NVIDIA NIM free endpoints

Keep as a major free provider because Laguna XS 2.1 and other agentic/coding models are explicitly available as Free Endpoints. However, NVIDIA-hosted free endpoints share a capacity-risk domain demonstrated by repeated worker-pool exhaustion reports, so multiple NVIDIA models do not equal independent provider redundancy.

### Gemini API Free Tier

Potential independent provider. Current Google documentation confirms a Free usage tier and free-of-charge access for some models, including Gemini 3.8 Flash pricing entries, but active per-project rate limits vary and are not guaranteed. Exact account limits must be checked before treating Gemini as a dependable primary.

### Groq Free Tier

Useful independent fallback candidate, but published free-tier limits for large models such as GPT-OSS-120B are materially tighter than Cerebras (for example 1K RPD / 200K TPD / 8K TPM in current docs), so it is less suitable as PRIME's sole primary under large-context operation.

## Capacity must be evaluated against PRIME's real payload

A provider's headline RPD is insufficient. PRIME's effective operating capacity depends on:

- input tokens per ordinary turn;
- tool schema payload after Cognitive Connection reduction;
- system/Canon context size;
- output/reasoning tokens;
- TPM/TPD, not only RPM/RPD;
- shared-worker saturation and provider availability.

Example: a nominal 1M-token daily free allowance supports only ~50 turns/day if an ordinary PRIME request consumes ~20K input tokens. Therefore context reduction and provider selection are coupled at the macro level even though provider worker saturation and token limits are distinct failure classes.

## Acceptance gate for PRIME primary model

Do not call a model/provider PRIMARY GREEN until it proves, under PRIME's real payload:

- reasoning/tool quality acceptable;
- no paid metered billing in the intended normal path;
- sustained ordinary conversation without frequent provider-capacity failure;
- enough token/request headroom for a normal active workday;
- acceptable latency;
- clean R0/R1/R2 behavior through the RYZ3N Cognitive Connection layer;
- independent fallback continuity when the provider is unavailable.

## Immediate direction

Stop optimizing cosmetic fallback behavior before primary availability is solved. The next model work should be a bounded free-endpoint bakeoff, beginning with an independent provider rather than another model on the same NVIDIA serving domain. Cerebras GPT-OSS-120B is the current first candidate to test against Laguna using PRIME's real payload and acceptance suite.
