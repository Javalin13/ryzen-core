# RYZ3N NVIDIA NIM / NEMOTRON ROUTING STANDARD

**Status:** FOUNDER APPROVED — AUTHORITATIVE MODEL ARCHITECTURE  
**Date:** 2026-09-13  
**Scope:** PRIME, Cargo, NARC, VONDA, OMEGA/Factory inheritance, future ARCs

This file is the single canonical model-routing standard. It supersedes older MiniMax-primary, ARC-local-primary, Kimi/DeepSeek normal-fallback, and Ultra→Qwen-only wording where those conflict.

## Canonical model stack

The RYZ3N stack is capability-aware, not a blind linear fallback chain.

```text
CORE BRAIN / NORMAL TEXT + TOOL WORK
NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  -> frontier reasoning, planning, coding, long-context analysis, tool use

SAME-PROVIDER TEXT FALLBACK
NVIDIA NIM / nvidia/nemotron-3-super-120b-a12b
  -> use when Ultra has a model-specific availability/compatibility problem

MULTIMODAL PERCEPTION SPECIALIST
NVIDIA NIM / nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
  -> image, video, audio/speech, OCR, GUI/document perception
  -> structured perception then handed to Ultra for reasoning/action/conversation

PROVIDER-INDEPENDENT EMERGENCY CONTINUITY
local Ollama / qwen3:0.6b
  -> only when NVIDIA is unavailable/unauthorized/rate-limited/network-failed or all eligible NVIDIA routes fail
  -> restricted emergency mode, not a full substitute brain
```

## Capability routing

### Normal text / planning / coding / tools / orchestration

1. Ultra primary.
2. If Ultra alone is unavailable or model-specific failure occurs, try Super.
3. If NVIDIA as a provider/account/network is unavailable or shared rate budget is exhausted, skip other NVIDIA retries and enter local Qwen restricted emergency continuity.
4. If no safe route remains, fail closed with sanitized user/Owner messaging.

### Image / video / audio / OCR / GUI / document perception

1. Route the media/perception step to Nano Omni.
2. Convert the result into a structured internal perception artifact.
3. Route that artifact to Ultra for reasoning, planning, tool use and final response.
4. Ultra remains the conversational brain; Nano Omni is a specialist, not the default chat brain.
5. Nano Omni's current direct language support limitation must not dictate Owner-facing language. The ARC may use Omni for perception and Ultra for multilingual response/synthesis.
6. If Omni is unavailable and the requested modality cannot be safely processed, fail/degrade gracefully rather than pretending the local text-only emergency model understood the media.

### Why Super is not the provider-outage fallback

Ultra, Super and Nano Omni share NVIDIA NIM/account capacity. Super protects against an Ultra-specific issue, not an NVIDIA-wide outage, credential failure, shared throttle or network failure. Local Qwen is the independent emergency route.

## Active topology for PRIME and all ARCs

PRIME, Cargo, NARC, VONDA and every future Factory-born ARC inherit the same model architecture:

```text
brain_primary:      nvidia/nemotron-3-ultra-550b-a55b
brain_fallback:     nvidia/nemotron-3-super-120b-a12b
multimodal_engine:  nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
emergency_fallback: local-ollama/qwen3:0.6b
```

Individual ARCs may have domain-specific tools, Brains, prompts and workflows, but they do not drift to a different normal model stack without explicit Founder-approved exception.

Kimi, DeepSeek and Ollama Cloud MiniMax are not active normal routes under this decision.

## NVIDIA endpoint and credential

NVIDIA NIM base URL:

`https://integrate.api.nvidia.com/v1`

Use `NVIDIA_API_KEY` from protected server secret/environment storage. Never print, log, commit, bridge-write or Owner-expose the credential.

The working Founder-created NVIDIA credential was manually proven against Ultra with an authenticated HTTP 200 response before PRIME cutover.

## Shared NVIDIA capacity

Current Founder dashboard evidence: **up to 40 requests/minute** for the NVIDIA account.

Treat this as one shared portfolio budget across PRIME + all ARCs + all NVIDIA models, not 40 RPM per model or per ARC.

Normal scheduling target: about **35 RPM** for headroom.

Required control plane:

- central shared limiter/scheduler;
- fair ARC queueing;
- bounded queue;
- priority for critical PRIME orchestration without permanent Owner starvation;
- capability-aware dispatch so media calls go to Omni only when needed;
- avoid retry storms between Ultra/Super/Omni;
- provider-wide throttle detection must jump to local emergency policy instead of consuming the same NVIDIA limit repeatedly;
- telemetry for queue latency, throttle events, route/model selection, fallback frequency and concurrency;
- no provider/rate-limit internals exposed to Owners.

Re-measure if NVIDIA changes endpoint/account behavior.

## Reasoning / privacy policy

Internal reasoning traces must never be surfaced to Founder/Owner/customer conversational output.

Where supported, disable exposed reasoning content for ordinary user-facing turns. Tool calls and structured internal artifacts may use hidden reasoning internally, but final output must contain only intended answer/tool results.

Owners must never see:

- provider/model names;
- API/rate-limit figures;
- raw 429/5xx/provider errors;
- context-window values;
- localhost/internal endpoints;
- Hermes/runtime internals;
- configuration instructions;
- billing/credit messages;
- credentials;
- fallback diagnostics.

## Local Qwen restricted emergency mode

Local route:

```text
provider = local Ollama
model    = qwen3:0.6b
endpoint = localhost/private only
```

For PRIME, Qwen may perform health checks, bounded recovery, queue supervision and safe status reporting. It must not autonomously perform broad architecture/governance decisions, canon rewrites, broad refactors, destructive Git operations, financial/billing actions or production-wide migrations.

For ARCs, Qwen may provide reduced-capacity continuity only where the task is safe for the small model. Media understanding must not be fabricated.

## Direct Owner interaction

PRIME remains supervisory and is not a conversational relay.

- Narek ↔ NARC directly
- Maria ↔ Cargo directly
- Laetitia ↔ VONDA directly

Founder never consumes an Owner slot. Owner namespaces remain isolated.

## OMEGA / Factory inheritance

OMEGA/Factory must bake into every new ARC:

- Ultra as core brain primary;
- Super as same-provider text fallback;
- Nano Omni as multimodal perception specialist;
- local Qwen as provider-independent restricted emergency fallback;
- central shared NVIDIA capacity scheduler;
- capability-aware dispatch;
- protected credential use;
- sanitized Owner UX;
- no reasoning leakage;
- direct Owner-to-ARC interaction;
- no independent model drift without Founder-approved exception.

## Migration / master execution order

1. PRIME NVIDIA key + Ultra raw API proof.
2. PRIME source/config points to Ultra primary and local Qwen emergency fallback.
3. Validate Super and Nano Omni with the same protected NVIDIA account before activating them in routing.
4. Install capability-aware routing in PRIME: Ultra brain, Super text fallback, Omni specialist, Qwen independent emergency.
5. Restart/verify PRIME once with exactly one poller, Telegram connected, normal chat and Hermes tool/function tests GREEN.
6. Only after PRIME is GREEN, migrate Cargo one ARC at a time to the same stack and verify.
7. Migrate NARC and verify.
8. Migrate VONDA and verify.
9. Persist authoritative ARC source/config/manifests through each ARC safe process.
10. Implement/verify shared ~35/40-RPM scheduling and anti-stampede behavior.
11. Update OMEGA/Factory inheritance.
12. Verify direct Owner path + privacy + multimodal dispatch + fallback behavior.
13. Run final post-cutover A→Z and source/runtime parity.
14. Remove active Ollama Cloud routing.
15. Report `OLLAMA CLOUD SAFE TO CANCEL` only when objectively true.
16. Keep the master mission OPEN until required real Owner proofs are valid.

## Ollama Cloud retirement

Ollama Cloud MiniMax is not part of the target active topology.

Do not tell Founder to cancel until PRIME/Cargo/NARC/VONDA are GREEN on the new stack, local emergency fallback is proven, gateways/pollers are healthy, Owner paths are intact, active Ollama Cloud routing is removed, and final A→Z is GREEN.

## Spend boundary

No autonomous purchase, top-up, subscription change, paid endpoint activation or server purchase.

## Completion boundary

No master-mission completion until model routing, capability routing, fallback proof, direct Owner path and required real Owner proofs are all valid.