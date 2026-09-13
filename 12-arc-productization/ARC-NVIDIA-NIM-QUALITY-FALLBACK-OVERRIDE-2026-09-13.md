# ARC NVIDIA NIM Quality Fallback Override — 2026-09-13

**Status:** FOUNDER-DIRECTED ADDITIVE OVERRIDE  
**Scope:** PRIME, current ARCs, OMEGA/Factory inheritance, future ARC legion

## Why this override exists

A very small local fallback model was observed producing low-trust, context-drifting output during an Ollama Cloud weekly-capacity event. That behavior is unacceptable for Founder-facing strategy, architecture, web research, repository decisions, steward actions, or Owner-facing operational work.

The Founder therefore requires a quality-preserving hosted fallback to be established before normal autonomous work resumes when the primary Ollama route is exhausted.

## Canonical routing priority for high-trust work

Until superseded by later Founder evidence:

```text
PRIME high-trust route
1. Ollama Cloud / MiniMax M3 when healthy and within capacity
2. verified NVIDIA NIM hosted Nemotron route
3. verified stronger local model, only after hardware + Hermes tool/function gates are GREEN
4. tiny/emergency local model = restricted degraded mode only
5. no trustworthy route = fail closed / queue high-trust work
```

Owner-facing ARCs may use a separately approved route policy, but they inherit the same **quality floor**: a weak emergency model must never silently perform high-trust work merely because it is available.

## NVIDIA NIM integration target

Hosted endpoint class:

`https://integrate.api.nvidia.com/v1`

The API credential is runtime-private. It must never be committed to GitHub, pasted into bridge reports, Telegram, logs, screenshots, or shared ARC memory.

Preferred first benchmark candidates:

1. `nvidia/nemotron-3.5-lightning-30b-a3b`
   - preferred first candidate for long-running autonomous-agent / agentic workflow performance;
   - benchmark for Hermes tool/function calling, structured output, coding, reasoning, EN/FR/NL practical quality, latency and stability.

2. `nvidia/nemotron-3-super-120b-a12b`
   - quality-oriented alternate benchmark for harder reasoning / planning / tool use;
   - use if it materially outperforms the first candidate at acceptable latency/reliability.

Do not select by model size or marketing label alone. The production route must be chosen by controlled real Hermes evidence.

## Required NIM acceptance test before resuming high-trust autonomous work

A candidate is GREEN only after all applicable checks pass:

- authenticated hosted NIM request succeeds through the intended PRIME/Hermes path;
- coherent Founder-context response without cross-project drift;
- one deterministic structured-output task;
- one safe Hermes tool/function call with correct arguments;
- one canon-grounded repository/read task without invented repository facts;
- one coding/technical reasoning task;
- EN and FR quality acceptable; NL must be practically tested even where not an officially advertised language;
- no raw provider/model/API details exposed to Owners;
- latency acceptable for fallback service;
- failure is classified cleanly and does not trigger random web research or unrelated recovered content.

## Weak local model restriction

Any tiny local model such as `qwen3:0.6b` is **not a trusted substitute** for PRIME-level cognition.

While such a model is the only route available, it may be used only for bounded low-risk continuity such as:

- health/status acknowledgement;
- sanitized temporary-unavailability messaging;
- queueing / deferring work;
- deterministic local checks that do not require reasoning;
- simple read-only status summaries from already-verified structured data.

It must not autonomously:

- perform architecture or strategy decisions;
- browse the web to establish project truth;
- modify GitHub or production state;
- change ARC/Owner identity, permissions, memory or maturity;
- create or rewrite canonical doctrine;
- infer commercial/legal/security decisions;
- claim a task is GREEN based on its own unverified reasoning.

If no trusted cloud/NIM/verified-local route is available, high-trust work is queued or failed closed rather than degraded into unreliable autonomous execution.

## Service-quality rule

Fallback exists to preserve **trustworthy service**, not merely to keep a process answering.

A response from an incapable model is worse than a transparent temporary pause for high-trust work.

## Factory / Golden ARC inheritance

OMEGA, the Golden ARC Blueprint, and every future ARC provisioning contract must record:

- route quality class;
- minimum capability gate for each action class;
- trusted vs emergency-degraded model classification;
- no silent promotion of an emergency model to high-trust execution;
- provider capacity telemetry and automatic route recovery;
- runtime-private credential handling;
- ability to substitute another verified route without changing ARC identity, memory, form, aura or maturity.

## Founder rule

> **When the premium route is exhausted, preserve intelligence quality before preserving uninterrupted autonomy. A weak model may keep the lights on; it may not take the wheel.**
