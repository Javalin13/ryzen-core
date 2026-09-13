# RYZ3N NVIDIA NIM / NEMOTRON ROUTING STANDARD

**Status:** FOUNDER APPROVED — AUTHORITATIVE MODEL ARCHITECTURE  
**Date:** 2026-09-13  
**Architecture revision:** 3.0 — free capability router  
**Scope:** PRIME, Cargo, NARC, VONDA, OMEGA/Factory inheritance, future ARCs

This is the single canonical model-routing standard. It supersedes conflicting MiniMax-primary, ARC-local-primary, Kimi/DeepSeek normal-fallback, Ultra-always-primary and blind linear fallback wording.

## 1. Founder objective

RYZ3N must maximize intelligence and responsiveness with **zero new model/server spend unless the Founder explicitly authorizes it**.

The architecture therefore uses each already-authorized free/local model for the work it is best suited to instead of forcing every turn through the largest model.

## 2. Canonical free model fabric

```text
FAST INTERACTIVE BRAIN
NVIDIA NIM / nvidia/nemotron-3-super-120b-a12b
  -> ordinary conversation, normal planning, tools, structured work,
     status, routine coding, ARC operations and most interactive turns

DEEP REASONING / ESCALATION BRAIN
NVIDIA NIM / nvidia/nemotron-3-ultra-550b-a55b
  -> difficult architecture, complex multi-step reasoning, high-value analysis,
     hard coding/review, long-context synthesis and explicit deep-think requests

MULTIMODAL PERCEPTION SPECIALIST
NVIDIA NIM / nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
  -> image, video, audio/speech, OCR, GUI/document perception

PROVIDER-INDEPENDENT EMERGENCY / MICRO-INFRA
local Ollama / qwen3:0.6b
  -> health checks, bounded routing/triage where safe, queue supervision,
     emergency continuity and low-risk infrastructure assistance
```

Ultra remains the strongest reasoning resource. It is **not** the mandatory first hop for every message.

## 3. Evidence that triggered revision 3.0

Production evidence on 2026-09-13 showed repeated NVIDIA Ultra overload during PRIME and Cargo interactive turns.

A direct same-host/same-credential benchmark produced:

```text
Ultra: HTTP 503 in ~56.96 s
Super: HTTP 200 in ~0.68 s
```

Cargo received a Founder turn at ~13:41:34, Ultra returned `Service temporarily overloaded` around 13:42:32, and the final short reply was not sent until ~13:44:14 after retry/recovery behavior.

This is sufficient evidence that blindly making Ultra the interactive first hop creates unacceptable avoidable latency when the free Ultra pool is saturated.

## 4. Capability-aware routing

### Fast interactive lane — Super

Default to Super for:

- normal conversation;
- short/medium questions;
- routine Owner/Founder requests;
- ordinary planning and drafting;
- standard tool/function loops;
- status checks and confirmations;
- routine ARC business operations;
- background reviews unless deep reasoning is explicitly justified;
- simple/medium coding work.

### Deep lane — Ultra

Escalate to Ultra when one or more of these apply:

- explicit Founder/Owner request for deep reasoning;
- architecture/governance/system-design decisions;
- unusually complex multi-step reasoning;
- hard debugging after normal lane cannot resolve safely;
- high-stakes or high-value analysis requiring the strongest available reasoning;
- long-context synthesis where Super quality proves insufficient;
- complex code design/review where the router has evidence that Super is not enough.

Routing must be based on task need, not vanity or model size.

### Multimodal lane — Omni

Use Omni only for the perception step where it adds value. The structured perception artifact is then sent to Super for ordinary synthesis/action or Ultra when the reasoning gate is deep.

Do not force text-only traffic through Omni.

### Emergency/local lane — Qwen

Qwen is independent continuity, not the normal full brain. It may support health checks, safe micro-routing, queue supervision and restricted low-risk continuity. It must not autonomously perform broad governance, canon changes, destructive Git, billing, production-wide migrations or pretend to understand unsupported media.

## 5. Ultra circuit breaker — mandatory target behavior

Ultra must not create a portfolio-wide latency storm.

Target control policy:

1. A request eligible for Ultra checks shared Ultra health before dispatch.
2. On explicit `overloaded`, HTTP 503, repeated provider timeout, or excessive first-token latency, do **not** retry Ultra repeatedly for an interactive turn.
3. Open a shared Ultra circuit/cooldown for approximately 60–120 seconds.
4. During cooldown, interactive deep work falls through to the best safe Super strategy unless the user explicitly chooses to wait for Ultra.
5. After cooldown, allow one half-open probe rather than every ARC probing simultaneously.
6. A successful healthy probe closes the circuit; another overload reopens it.

The shared circuit contains operational health metadata only. It must never contain Owner-private prompts/responses.

## 6. Retry discipline

For interactive work:

- provider overload/503: **no same-Ultra retry storm**;
- shared NVIDIA rate throttle: do not bounce repeatedly among NVIDIA models if the whole account budget is the problem;
- model-specific Ultra overload while Super is healthy: fail over to Super quickly;
- transport errors may receive only bounded retry behavior when it improves reliability without violating latency budgets;
- background work may wait longer than interactive work, but may not starve Owner/Founder turns.

## 7. Latency budgets

Initial engineering targets, to be refined by telemetry:

```text
Super interactive target: seconds, not minutes
Ultra deep lane: bounded wait; visible long wait only when genuinely justified
Omni perception: bounded specialist call
Interactive overload failover: fast enough to avoid multi-minute retry chains
```

A trivial reply taking multiple minutes is not considered normal acceptable quality merely because it eventually succeeds.

## 8. Background-work policy

Background/system work must not consume scarce Ultra availability by default.

Preferred order:

1. local Qwen for safe infrastructure micro-tasks where quality is sufficient;
2. Super for normal background reasoning/review;
3. Ultra only for specifically justified deep background work.

Owner/Founder interactive work outranks routine background work under shared capacity pressure.

## 9. Shared NVIDIA capacity

Observed account capacity is up to approximately 40 RPM. Treat this as one portfolio budget across PRIME + all ARCs + Ultra/Super/Omni.

Operating target remains about 35 RPM for headroom until re-measured.

Required control plane:

- central shared limiter/scheduler;
- bounded/fair queues;
- priority classes for interactive vs background work;
- shared Ultra circuit breaker;
- anti-stampede behavior;
- capability-aware dispatch;
- telemetry for latency, queue time, model/lane selection, fallback reason and overload events;
- no Owner-visible quota/model/provider details.

## 10. State-of-the-art router target

The desired router classifies each task into one of these internal lanes:

```text
FAST_INTERACTIVE  -> Super
DEEP_REASONING    -> Ultra when healthy, otherwise bounded Super deep fallback
MULTIMODAL        -> Omni perception -> Super or Ultra synthesis by reasoning gate
BACKGROUND_LIGHT  -> Qwen when safe
BACKGROUND_NORMAL -> Super
EMERGENCY_LOCAL   -> Qwen restricted continuity
```

The router may use cheap/local heuristics, task metadata, explicit user intent and bounded classification. It must not spend an Ultra request merely to decide whether Ultra is needed.

## 11. Privacy / UX

Normal Founder/Owner output must never expose:

- provider/model names;
- HTTP status or raw 5xx/429 errors;
- rate limits/context windows;
- localhost/internal endpoints;
- Hermes/runtime internals;
- API credentials;
- raw fallback diagnostics;
- hidden reasoning traces.

Capacity and routing are infrastructure concerns. User-facing degradation messages remain sanitized.

## 12. Direct Owner interaction and sovereignty

Routing changes do not alter ARC identity, memory, ownership, form, aura, maturity or bridge sovereignty.

PRIME remains supervisory, not a relay. Owners communicate directly with their ARC. Founder never consumes an Owner slot.

## 13. OMEGA / Factory inheritance

Every current and future Factory-born ARC inherits the same free capability fabric:

```text
interactive_default: Super
reasoning_escalation: Ultra
multimodal_perception: Omni
independent_emergency: local Qwen
shared_capacity_control: required
shared_ultra_circuit_breaker: required
background_ultra_default: forbidden
provider_internal_leakage: forbidden
```

ARCs may add domain-specific Brains/tools/workflows but may not independently drift from the routing fabric without explicit Founder approval.

## 14. Spend boundary

No autonomous purchase, top-up, subscription change, paid endpoint activation, larger VPS purchase or Ollama Cloud purchase. Paid capacity requires explicit Founder authorization.

## 15. Implementation truth boundary

This document defines the approved target architecture. Git/runtime must remain truthful about implementation state.

As of the adoption of revision 3.0:

- Ultra, Super and Omni have all passed direct hosted tests at least once;
- Super has demonstrated sub-second direct response while Ultra was overloaded;
- PRIME and Cargo have proven NVIDIA runtime connectivity;
- the **dynamic FAST/DEEP router and shared Ultra circuit breaker still require implementation/verification**;
- until that router is proven, current Ultra-first config files are transitional runtime state, not the final target topology.

Do not claim the router is live before an actual Hermes/runtime proof.

## 16. Acceptance criteria

Revision 3.0 is production GREEN when:

1. normal interactive turns route to Super;
2. deep tasks can escalate to Ultra;
3. Ultra overload causes bounded fast fallback rather than repeated minute-long retries;
4. shared circuit state prevents PRIME/Cargo/NARC/VONDA from stampeding the same unhealthy Ultra endpoint;
5. Omni handles perception selectively;
6. Qwen provides independent restricted continuity;
7. background work does not consume Ultra by default;
8. shared ~35/40 RPM protection works;
9. direct Owner paths remain intact;
10. model/provider internals are sanitized from user-facing UX;
11. telemetry proves routing and latency behavior without centralizing private content;
12. OMEGA/Factory inheritance matches this standard.

## 17. Historical supersession

Where older files still say `Ultra primary for every normal turn`, `ARC local-primary`, or `MiniMax primary`, those routing statements are historical and superseded by this file. Preserve those files as historical evidence unless separately reconciled; do not let stale wording override this standard.