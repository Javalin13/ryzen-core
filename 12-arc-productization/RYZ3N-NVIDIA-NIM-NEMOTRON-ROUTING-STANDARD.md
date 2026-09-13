# RYZ3N NVIDIA NIM / NEMOTRON ROUTING STANDARD

**Status:** FOUNDER APPROVED — AUTHORITATIVE ROUTING + RECOVERY STANDARD  
**Date:** 2026-09-13  
**Scope:** PRIME, Cargo, NARC, VONDA, OMEGA/Factory inheritance, future ARCs

## Final Founder-approved topology

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

This supersedes MiniMax-primary and ARC-local-primary routing.

## Mandatory recovery gate — NVIDIA FIRST

When PRIME is operating only on the weak local emergency model, it is not trusted for broad architecture/governance work.

Before PRIME handles any other master-mission work, the NVIDIA NIM route must be installed/configured, authenticated, tested and made PRIME's live primary.

The recovery gate is:

1. load the existing protected NVIDIA NIM API key from server secret/environment storage;
2. test `https://integrate.api.nvidia.com/v1` with `nvidia/nemotron-3-ultra-550b-a55b`;
3. require HTTP 200 + valid model response;
4. prove normal response, structured output, Hermes tool/function calling, EN/FR/NL and sanitized errors;
5. switch PRIME to Nemotron primary;
6. restart/verify PRIME with exactly one poller, Telegram connected and Nemotron actually serving PRIME.

Until this gate is GREEN, local `qwen3:0.6b` is restricted to bounded recovery/health actions only. It must not autonomously rewrite canon, make architecture/governance decisions, perform broad refactors, migrate all ARCs, execute destructive Git operations, or make financial/billing changes.

## NVIDIA credential rule

Reuse the existing protected NVIDIA NIM key first. Never print, echo, log, commit, bridge-write or Owner-expose the credential.

Only if the existing key is actually rejected, revoked, expired or unauthorized may PRIME report `NEW NVIDIA KEY REQUIRED`.

## Master model build-up sequence

Once PRIME is GREEN on Nemotron, PRIME owns the remaining work in order:

1. preserve source freshness, Founder/Owner bindings, pairing/access and activation state;
2. migrate Cargo to Nemotron primary + local Qwen fallback and verify;
3. migrate NARC likewise and verify;
4. migrate VONDA likewise and verify;
5. persist authoritative configs/manifests through each ARC's safe process;
6. prove local Qwen fallback for PRIME and all three ARCs, including live Hermes context/runtime requirements and no reasoning leakage;
7. implement shared NVIDIA rate limiting/queueing;
8. update OMEGA/Factory so all future ARCs inherit the same stack;
9. verify direct Owner interaction and Owner privacy;
10. run final post-cutover A→Z + source/runtime parity;
11. update bridge/state/routing truth and push final commits;
12. report `OLLAMA CLOUD SAFE TO CANCEL` only when objectively true;
13. keep the master mission OPEN until required real Owner proofs are valid.

## Shared NVIDIA capacity

Founder operating evidence: hosted Nemotron free endpoint capacity is approximately **40 requests/minute**.

Treat this as one shared portfolio budget across PRIME + all ARCs. Target normal scheduling around **35 RPM** for headroom.

Required control plane:

- central shared rate limiter/scheduler;
- fair ARC queueing;
- bounded queue;
- PRIME priority for critical orchestration without permanent Owner starvation;
- anti-429 stampede protection;
- telemetry for throttle events, queue latency, fallback frequency and concurrency;
- no Owner-facing provider/rate-limit details.

Re-measure if NVIDIA changes endpoint/account behavior.

## Compute placement

Normal inference runs on NVIDIA-hosted infrastructure. The Hetzner CX23 is not the normal LLM compute plane.

Local CPU/RAM/swap inference is fallback-only. Local congestion is a fallback-capacity risk, not the steady-state design.

## Local fallback

```text
provider = local Ollama
model    = qwen3:0.6b
endpoint = localhost/private only
```

No Kimi, DeepSeek, Ollama Cloud or other provider is a normal fallback.

Fallback must be validated against the live Hermes runtime, not merely config text. Required context/runtime overrides must be persisted in authoritative source/config. Thinking/reasoning traces must never leak to Owners.

For PRIME specifically, local Qwen is emergency continuity, not a trusted full-intelligence replacement for Nemotron.

## Direct Owner interaction

PRIME remains supervisory and is not a conversational relay.

- Narek ↔ NARC directly
- Maria ↔ Cargo directly
- Laetitia ↔ VONDA directly

Founder never consumes an Owner slot. Owner namespaces remain isolated.

## Owner UX

Owners must not see provider/model names, API/rate-limit figures, raw 429/5xx errors, context-window values, localhost endpoints, Hermes/runtime internals, configuration instructions, billing/credit messages, credentials or fallback diagnostics.

Use sanitized temporary-unavailable messaging only.

## OMEGA / Factory inheritance

OMEGA/Factory must bake into every new ARC by default:

- Nemotron primary;
- local Qwen fallback;
- no additional normal fallback;
- central NVIDIA capacity scheduler;
- protected credential use;
- sanitized Owner UX;
- local fallback safety controls;
- direct Owner-to-ARC interaction.

No ARC may drift independently without explicit Founder-approved exception.

## Ollama Cloud retirement

Ollama Cloud MiniMax is not part of the target active topology.

Do not tell Founder to cancel until all of the following are GREEN:

1. PRIME Nemotron primary;
2. Cargo/NARC/VONDA Nemotron primary;
3. chat + Hermes tools + EN/FR/NL;
4. local Qwen fallback;
5. all four gateways healthy, exactly one poller each;
6. direct Owner interaction intact;
7. active Ollama Cloud routing removed;
8. final A→Z GREEN.

Only then report `OLLAMA CLOUD SAFE TO CANCEL`.

## Spend boundary

No autonomous purchase, top-up, subscription change, paid endpoint activation or server purchase.

## Completion boundary

No master-mission completion until the routing cutover, fallback proof, direct Owner path and required real Owner proofs are all valid.
