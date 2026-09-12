# RYZ3N NVIDIA NIM NEMOTRON PRIMARY STANDARD — 2026-09-12

**Status:** FOUNDER SUPERSESSION — AUTHORITATIVE
**Scope:** PRIME, Cargo ARC, NARC, VONDA, OMEGA / ARC Factory inheritance, future ARCs

## Founder decision

The prior routing posture that used Ollama Cloud MiniMax M3 for PRIME and local Qwen as ARC primary is superseded by this standard after successful migration acceptance.

Target routing for the entire RYZ3N ARC ecosystem:

```text
PRIME
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b
  additional normal fallbacks = NONE

Cargo ARC
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b
  additional normal fallbacks = NONE

NARC
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b
  additional normal fallbacks = NONE

VONDA
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b
  additional normal fallbacks = NONE

Future ARCs
  default primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  default fallback = local Ollama / qwen3:0.6b
  additional normal fallbacks = NONE unless Founder explicitly supersedes this policy
```

## Why this model

At the time of this Founder decision, NVIDIA Build exposes `nvidia/nemotron-3-ultra-550b-a55b` as a hosted Free Endpoint for prototyping/development with an OpenAI-compatible API, 1M context, and explicit agentic reasoning / planning / coding / tool-calling positioning.

This makes it the preferred hosted intelligence layer for RYZ3N while local Qwen remains the self-hosted continuity fallback.

## Ollama Cloud retirement target

After the NVIDIA NIM route is verified GREEN in live RYZ3N/Hermes operation:

- Ollama Cloud MiniMax M3 is removed from PRIME active routing;
- Ollama Cloud is removed from normal ARC routing;
- no Ollama Cloud fallback remains anywhere;
- Founder may cancel the Ollama Cloud subscription manually;
- PRIME/OMEGA/ARCs must not autonomously purchase, renew, top up, upgrade or re-enable Ollama Cloud.

Do not cancel or disable the currently working Ollama Cloud route before the NVIDIA NIM cutover has passed acceptance and rollback-safe migration checks.

## NVIDIA NIM secret handling

- NVIDIA API key is a server secret only.
- Never commit the key to Git.
- Never print it in Telegram, logs, bridge files, reports or Owner-facing errors.
- Load it from protected runtime environment / secret storage.
- Founder/PRIME telemetry may record provider status and non-secret usage metadata only.

## Migration acceptance gates

Do not call the NVIDIA cutover GREEN until all are proven:

1. PRIME can call Nemotron successfully through the configured NVIDIA NIM endpoint.
2. Cargo, NARC and VONDA can call Nemotron successfully.
3. Hermes tool/function calling works on all four runtimes.
4. EN / FR / NL normal interaction works.
5. Owner-facing conversations do not expose provider/model names, endpoint URLs, rate-limit internals, credentials or raw errors.
6. One poller per gateway remains true.
7. Telegram connectivity remains GREEN.
8. Founder/Owner role separation and activation state are preserved.
9. Direct Owner interaction remains functional.
10. Fallback to local `qwen3:0.6b` is tested from each runtime without cross-ARC interference.
11. Local Qwen fallback must fail closed with sanitized Owner messaging if Hermes requirements cannot be satisfied safely.
12. No third normal provider route remains configured.
13. Final A→Z runtime/source parity passes after cutover.

## Fallback contract

The only normal fallback is local Ollama `qwen3:0.6b`.

If NVIDIA NIM is unavailable:

- attempt local Qwen;
- do not silently route to Ollama Cloud, Kimi, DeepSeek or another paid/free hosted provider;
- if local Qwen cannot safely service the request, fail closed with a sanitized temporary-unavailable Owner message;
- report the condition to PRIME/Founder telemetry.

## Free-endpoint caveat

The Founder decision intentionally uses NVIDIA's currently available hosted Free Endpoint. Free/prototype endpoint availability, rate limits and commercial terms can change. Runtime telemetry must therefore track availability, latency, throttling and fallback frequency. A future commercial/production licensing decision is separate from this routing decision and must be explicitly approved by Founder.

## Factory inheritance

OMEGA / ARC Factory must treat this as the current default model-routing birth policy for new ARCs until Founder supersedes it.

No newly created ARC should inherit Ollama Cloud MiniMax, Kimi, DeepSeek or another normal fallback by default.
