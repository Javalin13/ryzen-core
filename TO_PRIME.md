# RYZ3N CORE — TO PRIME

**Status:** CONSUME REQUIRED  
**Authority:** Founder / Lux master engineering bridge  
**Repository:** `Javalin13/ryzen-core`  
**Counterpart:** `FROM_PRIME.md`

## Master position

**MASTER: M3/16 — CARGO ARC GREEN**

Current bounded task: complete the free capability-router Phase-A inspection, then report through `FROM_PRIME.md` for Lux review before any runtime mutation.

## Current approved routing target

```text
FAST_INTERACTIVE  -> NVIDIA Nemotron Super
DEEP_REASONING    -> NVIDIA Nemotron Ultra only when warranted and healthy
MULTIMODAL        -> NVIDIA Nemotron Omni perception -> Super/Ultra synthesis
BACKGROUND_LIGHT  -> local Qwen 0.6B when safe
BACKGROUND_NORMAL -> Super
EMERGENCY_LOCAL   -> local Qwen restricted continuity
```

Required overload behavior:

- ordinary interactive work must not repeatedly retry an overloaded Ultra endpoint;
- Ultra 503 / provider-overloaded / excessive-latency evidence should open a shared Ultra cooldown/circuit of roughly 60–120 seconds;
- while the circuit is open, normal interactive traffic routes directly to Super;
- after cooldown, permit one half-open Ultra health probe before restoring deep-lane eligibility;
- background/self-improvement work must not consume Ultra by default;
- retain compatibility with the observed shared NVIDIA account limit around 40 RPM and the planned ~35 RPM operating target;
- keep Omni as the perception specialist and local Qwen as independent emergency continuity.

## Proven evidence driving this work

2026-09-13 live evidence:

- Cargo received the Founder request at ~13:41:34, proving Telegram was not the multi-minute bottleneck;
- Ultra returned `Service temporarily overloaded` around 13:42:32 and Hermes retried;
- Cargo final reply was delivered around 13:44:14;
- separate Cargo background work also hit Ultra overload;
- direct same-runtime benchmark: Ultra -> HTTP 503 in ~56.96 seconds; Super -> HTTP 200 in ~0.68 seconds.

## PHASE A — INSPECTION ONLY

Inspect the live Hermes/runtime and identify the cleanest existing integration point for:

1. per-turn / per-capability model selection or override;
2. failure/fallback classification before repeated Ultra retries;
3. shared Ultra circuit state usable across PRIME and ARC profiles without sharing Owner-private content;
4. background-work route selection;
5. compatibility with the existing Omni media path;
6. sanitized Owner-facing fallback/error behavior.

Preference order:

1. native Hermes config/model override capability;
2. plugin/hook/extension point;
3. thin versioned RYZ3N routing layer around Hermes;
4. Hermes-core modification only if no safe supported boundary exists.

### Phase-A hard boundaries

- do **not** modify Hermes core during Phase A;
- do **not** restart PRIME, Cargo, NARC or VONDA merely for inspection;
- do not change Owner bindings, ARC memories, identities, forms, aura, maturity, business logic, secrets or sovereignty;
- do not reopen settled Hetzner IPv6/DNS64/NAT64 investigation without contradictory new evidence;
- preserve `HERMES_TELEGRAM_DISABLE_FALLBACK_IPS=true` where already established;
- Founder remains Founder, never Owner;
- PRIME remains supervisory; direct Owner -> ARC paths stay intact.

## Required report

Write the full Phase-A result to repository-root `FROM_PRIME.md`, commit and push it to `ryzen-core`, then give the Founder only the timed MINI REPORT.

`FROM_PRIME.md` must include:

- consumed `ryzen-core` HEAD / directive;
- exact files/classes/functions/hooks inspected;
- whether native per-turn model selection exists;
- whether retry/fallback policy is configurable without Hermes-core mutation;
- cleanest proposed implementation boundary;
- proposed shared circuit-breaker state location and lifecycle;
- proposed lane-decision inputs;
- how PRIME/Cargo/future NARC/VONDA share policy without sharing private Owner payload;
- expected changed paths;
- rollback plan;
- privacy/isolation impact;
- risks/blockers;
- elapsed inspection time;
- implementation ETA;
- `LUX: SYNC NEEDED` or `LUX: NO SYNC NEEDED`.

Founder-facing MINI REPORT format:

```text
STATUS: <GREEN/AMBER/RED + one-line result>
CHANGED: inspection only; no runtime mutation
NEXT: <smallest proposed implementation step>
TIME: <elapsed> | ETA: <implementation estimate>
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <ryzen-core pushed short SHA>
```

## Session-crash / provider-error recovery

If the active PRIME chat/session terminates, throws an unexpected error, or is abandoned because the current provider is overloaded before the bounded task is completed:

1. do **not** ask the Founder to reconstruct technical context;
2. start a fresh PRIME session if required;
3. fetch/pull current `Javalin13/ryzen-core` `origin/main` first;
4. read repository-root `TO_PRIME.md` and current `FROM_PRIME.md`;
5. resume from the latest durable bridge state and the last verified source/runtime checkpoint;
6. do not repeat already-proven diagnostics merely because the chat session changed;
7. continue to the same acceptance gate and report through `FROM_PRIME.md`.

The durable bridge is the continuity mechanism. A failed chat/session does not reset the mission.

## Bridge hierarchy

`TO_PRIME.md` / `FROM_PRIME.md` in `ryzen-core` are the canonical Lux <-> PRIME master bridge.

Cargo/NARC/VONDA repository bridges are ARC-local only and must not replace this master bridge.

## Additional queued roadmap item

The ARC Media / Video Engine remains a future RYZ3N-wide capability: free/open/self-hosted-first video generation, clean exports without forced third-party branding where licensing permits, native-quality social-platform compatibility, and no deliberate moderation/provenance/detection bypass.
