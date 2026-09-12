# RYZ3N NVIDIA NIM / NEMOTRON ROUTING STANDARD

**Status:** FOUNDER APPROVED — AUTHORITATIVE ROUTING SUPERSESSION  
**Date:** 2026-09-12  
**Scope:** PRIME, Cargo, NARC, VONDA, OMEGA/Factory inheritance, future ARCs

## Founder-approved target

The normal inference topology is now:

```text
PRIME
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b
  additional normal fallbacks = NONE

Cargo
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b

NARC
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b

VONDA
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b

Future ARCs
  primary  = NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  fallback = local Ollama / qwen3:0.6b
```

This supersedes previous active routing in which PRIME used Ollama Cloud MiniMax M3 and current ARCs used local Qwen as normal primary.

## NVIDIA credential rule

Use the existing protected NVIDIA NIM API key first. The key must remain in protected server environment/secret storage and must never be printed, committed, echoed into logs, or exposed to Owners.

If the existing NVIDIA NIM key returns a successful authenticated Nemotron request, reuse it. Only require Founder to generate a replacement NVIDIA key if the existing key is actually rejected, revoked, or expired.

## Shared NVIDIA capacity policy

Current Founder operating assumption/evidence: hosted Nemotron free endpoint permits approximately **40 requests per minute**.

PRIME must treat this as a shared portfolio capacity budget, not as 40 RPM per ARC.

Required control plane:

- central shared rate limiter/scheduler across PRIME + all ARCs;
- target normal operating ceiling around **35 RPM** to preserve headroom below the observed 40 RPM limit;
- fair queueing across ARCs;
- PRIME may receive priority for critical orchestration but must not permanently starve Owner ARCs;
- short bounded queue before fallback where safe;
- do not allow a burst of 429/throttle events to stampede all traffic onto the small VPS at once;
- record throttling, queue latency, fallback frequency, and active concurrency in Founder/PRIME telemetry;
- no Owner-facing provider/rate-limit details.

The 40 RPM figure is an operational planning value and must be re-measured if NVIDIA changes endpoint behavior or account policy.

## Compute placement

Under normal operation, Nemotron inference is hosted on NVIDIA infrastructure. The Hetzner VPS therefore should not carry the normal LLM inference CPU burden.

The local VPS becomes inference-active mainly during fallback events. CPU/RAM/swap congestion is therefore a **fallback-capacity risk**, not the intended steady-state architecture.

PRIME must monitor local fallback pressure and prevent cascading failure. Queue safely, preserve ARC isolation, and fail closed with a sanitized Owner message if both primary and fallback are unavailable/unsafe.

## Local fallback

Local fallback remains:

```text
provider = local Ollama
model    = qwen3:0.6b
endpoint = localhost/private only
```

No Kimi, DeepSeek, Ollama Cloud, or other provider is a normal fallback under this Founder decision.

The local fallback must be proven compatible with the active Hermes runtime. Any context-window/runtime settings required for Hermes must be persisted in authoritative ARC source/config and validated against the live loaded Ollama runtime rather than merely present as config text.

Reasoning/thinking traces must never leak to Owner-facing responses.

## Ollama Cloud retirement

Ollama Cloud MiniMax is no longer part of the target active routing topology.

Do not tell Founder to cancel the paid Ollama Cloud subscription until PRIME has objectively verified:

1. Nemotron primary works for PRIME;
2. Nemotron primary works for Cargo, NARC, and VONDA;
3. normal chat works;
4. Hermes tool/function calling works;
5. EN/FR/NL behavior is acceptable;
6. local Qwen fallback works;
7. all four gateways remain healthy with exactly one poller each;
8. no Owner identity/onboarding regression occurs;
9. old Ollama Cloud routing is removed from active configs;
10. final post-cutover A→Z is GREEN.

Only then report: `OLLAMA CLOUD SAFE TO CANCEL`.

## Owner UX

Owners must not see:

- provider/model names;
- API/rate-limit figures;
- raw 429/5xx errors;
- context-window values;
- localhost endpoints;
- Hermes/runtime internals;
- configuration instructions;
- billing/credit messages;
- fallback diagnostics.

Owner-facing route failures must be sanitized. Provider/runtime details remain Founder/PRIME telemetry only.

## OMEGA / Factory inheritance

OMEGA/Factory must bake this routing policy into new ARCs by default:

- Nemotron primary;
- local Qwen fallback;
- no additional normal fallback;
- shared central NVIDIA capacity scheduler;
- protected credential use;
- sanitized Owner UX;
- local fallback safety controls.

Future Founder supersessions may change the model/provider, but individual ARCs must not drift independently without an explicit approved exception.

## Migration ownership

PRIME owns execution of the cutover. Founder/Lux should not manually rewrite every ARC runtime.

PRIME must:

1. pull/consume latest canonical source and bridge directives;
2. test existing protected NVIDIA key against Nemotron;
3. validate Nemotron normal chat + tools + EN/FR/NL;
4. cut over PRIME first;
5. cut over Cargo/NARC/VONDA one at a time;
6. preserve direct Owner interaction and activation state;
7. verify exactly one Telegram poller per gateway;
8. implement shared rate limiting/queueing;
9. verify local Qwen fallback;
10. update OMEGA/Factory inheritance and all relevant source/config/bridge truth;
11. remove active Ollama Cloud routing only after Nemotron is GREEN;
12. run final A→Z;
13. report whether Ollama Cloud is safe to cancel.

## Non-negotiable invariants

- PRIME remains supervisory; it is not a required conversational relay between an Owner and their ARC.
- Founder never consumes an Owner slot.
- Owner private namespaces remain isolated.
- No credentials in Git, chat, bridge files, or Owner-visible output.
- No autonomous purchase, top-up, subscription change, or paid provider activation.
- No master-mission completion until real Owner interaction proofs remain valid after the routing cutover.
