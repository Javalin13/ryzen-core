# PRIME Master Bridge + Free Router Directive — 2026-09-13

Status: **ACTIVE / CONSUME VIA RYZ3N CORE PRIME BRIDGE**

## Canonical bridge location correction

Founder correction: the canonical Lux <-> PRIME master engineering bridge is in `Javalin13/ryzen-core`, using the established TO-PRIME and FROM-PRIME markdown bridge files in that repository.

VONDA bridge material is ARC-specific. It is not the master PRIME bridge and must not be used as the authority for global PRIME/RYZ3N handoffs.

Canonical hierarchy:

```text
Javalin13/ryzen-core + its TO/FROM PRIME markdowns
  = global Lux <-> PRIME engineering bridge / RYZ3N source truth

ARC repository bridges (Cargo / NARC / VONDA / future ARCs)
  = ARC-local handoff, evidence, Owner/ARC/runtime-specific state

runtime transport directories on VPS
  = live transport/state only, never a substitute for the canonical repository bridge
```

## Current mission

MASTER: M3/16 — Cargo ARC GREEN
Current substep: implement the Founder-approved free capability router after a read-only integration inspection.

Proven runtime evidence on 2026-09-13:

- Cargo request processing began around 13:41:34, so Telegram was not the multi-minute latency source.
- Ultra returned `Service temporarily overloaded` and Hermes retried the same Ultra route.
- final Cargo reply was around 13:44:14.
- separate background work also hit Ultra overload.
- direct same-runtime benchmark: Ultra -> HTTP 503 in ~56.96 s; Super -> HTTP 200 in ~0.68 s.

Approved capability lanes:

```text
FAST_INTERACTIVE  -> NVIDIA Nemotron Super
DEEP_REASONING    -> NVIDIA Nemotron Ultra when warranted and healthy
MULTIMODAL        -> NVIDIA Nemotron Omni perception -> Super/Ultra synthesis
BACKGROUND_LIGHT  -> local Qwen 0.6B when safe
BACKGROUND_NORMAL -> Super
EMERGENCY_LOCAL   -> local Qwen restricted continuity
```

Required overload behavior:

- no repeated same-Ultra interactive retry storm on 503/overload/excessive latency;
- shared Ultra cooldown/circuit roughly 60–120 seconds;
- while open, ordinary interactive work goes directly to Super;
- one half-open Ultra health probe after cooldown before restoring deep-lane eligibility;
- background/self-improvement work does not use Ultra by default;
- remain compatible with the shared NVIDIA capacity policy around the observed ~40 RPM account limit and ~35 RPM operating target.

## Phase A — inspect first

PRIME is authorized to inspect the live Hermes/runtime and report the cleanest integration point for:

1. per-turn / per-capability model selection;
2. retry/fallback classification before repeated Ultra retries;
3. shared Ultra circuit state usable by PRIME and ARC profiles without sharing Owner-private content;
4. background route selection;
5. compatibility with the existing Omni media path;
6. sanitized Owner-facing fallback/error behavior.

Preference order:

1. native Hermes model/config override;
2. plugin/hook/extension point;
3. thin versioned RYZ3N routing layer around Hermes;
4. Hermes-core mutation only if no safe boundary exists.

**Do not mutate Hermes core during Phase A.**
**Do not restart PRIME/Cargo/NARC/VONDA merely for this inspection.**
Do not touch Owner bindings, memory, identities, forms, aura, maturity, business logic, secrets or ARC sovereignty.

## Reporting contract

Use the existing canonical `ryzen-core` FROM-PRIME markdown bridge for the detailed report, not VONDA.

Detailed report must include:

- current ryzen-core HEAD / consumed directive;
- exact files/classes/functions/hooks inspected;
- whether native per-turn model selection exists;
- whether retry policy is configurable without Hermes-core mutation;
- proposed implementation boundary;
- proposed shared circuit state location/lifecycle;
- expected changed paths;
- rollback plan;
- privacy/isolation impact;
- risks/blockers;
- elapsed inspection time;
- implementation ETA;
- `LUX: SYNC NEEDED` or `LUX: NO SYNC NEEDED`.

Founder receives only the normal timed MINI REPORT:

```text
STATUS: <GREEN/AMBER/RED + one line>
CHANGED: inspection only; no runtime mutation
NEXT: <next bounded action>
TIME: <elapsed> | ETA: <estimate>
LUX: SYNC NEEDED | NO SYNC NEEDED
BRIDGE: <ryzen-core pushed short SHA>
```

If work exceeds ~5 minutes, provide a 3–5 minute progress checkpoint rather than going silent.

## Additional roadmap item already approved

ARC Media / Video Engine remains a RYZ3N-wide future capability: free/open/self-hosted-first media generation pipeline, clean exports without forced third-party branding where licensing permits, proper social-platform compatibility and no deliberate moderation/provenance/detection bypass.

## Permanent rule

> Master PRIME coordination lives in RYZ3N Core. ARC bridges remain ARC-specific.

Founder is Founder, never Owner. PRIME remains supervisory. Direct Owner -> ARC interaction remains intact.