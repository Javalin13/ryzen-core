# RYZ3N Runtime Portability & Adapter Contract

Date: 2026-09-17
Status: Founder-directed architecture / continuity contract
Master: M3/16 — Cargo ARC GREEN
Current line: E1.24 — Cognitive Connection / request-pressure control

## Purpose

This document exists so RYZ3N never has to be rebuilt from scratch when either the underlying language model or the agent/runtime framework changes.

Canonical rule:

> RYZ3N owns identity, cognition policy, Owner sovereignty, Brains, tool policy, verification, continuity and evidence. Models and agent runtimes are replaceable substrates.

Current implementation uses Hermes, but Hermes is not RYZ3N. Laguna/Qwen/other models are not PRIME. PRIME and every ARC must survive substrate replacement.

## Canonical separation

```text
OWNER / HUMAN SOVEREIGNTY
        ↓
RYZ3N CANON + IDENTITY + GOVERNANCE
        ↓
OWNER IDENTITY / INTENT CONTEXT
        ↓
RYZ3N COGNITIVE CONNECTION LAYER
intent → R0/R1/R2/R3/R4 → tool policy → stop/verify/output
        ↓
BRAIN / CAPABILITY COMPOSITION
        ↓
RUNTIME ADAPTER CONTRACT
        ↓
Hermes today | future agent runtime | direct API runtime | other substrate
        ↓
MODEL ADAPTER CONTRACT
        ↓
Laguna | Qwen | Super | Ultra | Omni | future models
        ↓
TOOLS / PROVIDERS / INFRASTRUCTURE
```

## What MUST remain RYZ3N-owned

These concerns may never be made dependent on one specific agent framework or model:

- Owner sovereignty and authority boundaries;
- identity and continuity;
- ARC aura/form/maturity rules;
- Canon inheritance;
- Owner Intent interpretation and supersession;
- R0–R4 reasoning-budget policy;
- direct-vs-agentic classification;
- tool/no-tool discipline;
- public/private/action-state separation;
- bounded recursion and stopping rules;
- verification and intent-fidelity checks;
- Brain selection/composition;
- capability routing policy;
- privacy and cross-Owner isolation;
- transfer/reset behavior;
- observability/evidence schema;
- Reliable Excellence acceptance gates.

## Runtime adapter contract

A supported agent/runtime substrate must expose or be wrapped to expose equivalents for:

1. authenticated ingress / session identity;
2. pre-model turn classification;
3. request-local model payload mutation;
4. request-local tool-set control;
5. pre-tool authorization/blocking;
6. tool execution result observation;
7. public-output transformation/gating;
8. bounded continuation/stop behavior;
9. provider/model fallback signaling;
10. telemetry for model, latency, tokens, tools, retries and errors;
11. session continuity without leaking private payloads;
12. reversible installation/removal boundary.

The adapter MAY implement these via hooks, middleware, callbacks, interceptors, an orchestration API, or a thin compatibility layer. RYZ3N must consume the contract, not the framework-specific mechanism.

## Model adapter contract

A model is eligible when RYZ3N can describe at least:

- model/provider identity;
- modalities;
- context limits;
- tool/function-call support;
- structured-output support;
- reasoning characteristics;
- latency profile;
- cost/capacity constraints;
- provider cache behavior when available;
- observed reliability by R0–R4 lane;
- fallback eligibility and restrictions.

A model switch should normally require:

```text
capability profile
→ adapter/config
→ R0–R4 acceptance suite
→ telemetry comparison
→ rollback point
→ promotion decision
```

It must NOT require rewriting Owner sovereignty, Brain architecture, ARC identity, or business logic.

## Hermes-specific mapping — current evidence

Current Hermes seams discovered and used/assessed during E1.23/E1.24:

- `pre_gateway_dispatch` — generic ingress/control seam;
- `pre_llm_call` — ephemeral user-context injection, not request mutation;
- `pre_tool_call` — execution gate;
- `transform_llm_output` — public-output control;
- `llm_request` middleware — intended request-local provider-payload rewrite seam;
- `pre_api_request` — observer/telemetry seam after request middleware;
- `build_api_kwargs(..., tools_for_api=...)` — request-local tool-list support in Hermes core;
- Telegram adapter is transport only and must not own RYZ3N semantics.

These names are Hermes implementation details. Future runtimes only need equivalent semantics.

## Current Cognitive Connection implementation trail

### v0.1.0
- structural plugin installed;
- R0 exact-response path proven;
- no `/think` leakage on exact test;
- basic live integration proven.

### v0.2.0
- R1 explicit no-tool lane;
- no-tool execution block;
- bounded-output/repetition collapse;
- fixed severe single-call Laguna restatement loop observed in T3.

### v0.3.0
- added request-local `llm_request` middleware intended to strip tool schemas for R0/R1 without mutating `agent.tools`;
- Doctor validates plugin import/registration surface;
- live provider telemetry has NOT yet proven request mutation;
- current E1.24 work is determining why middleware is absent from the effective live request.

## Evidence preservation standard

For every future model or runtime change, preserve:

- exact version/commit/config used;
- reason for change;
- old and new architecture mapping;
- files/functions/seams touched;
- tests run and exact acceptance criteria;
- failures and rejected hypotheses;
- latency/token/tool/retry evidence;
- rollback boundary;
- what is substrate-specific vs canonical RYZ3N logic;
- final GREEN/AMBER/RED status;
- unresolved debt explicitly listed.

Do not compress away failed experiments if they teach a portability constraint. Avoid raw secret/private payload retention.

## Migration procedure — future agent runtime

When Hermes is replaced or supplemented:

1. freeze the current RYZ3N acceptance matrix;
2. inventory the new runtime against the Runtime Adapter Contract;
3. build the smallest adapter rather than porting all Hermes-specific code;
4. map R0/R1 first, then R2 tool execution, then R3/R4 bounded recursion;
5. replay canonical acceptance tests;
6. compare observability and capacity behavior;
7. prove Owner/ARC continuity;
8. run parallel/shadow where possible;
9. promote only after Reliable Excellence evidence;
10. keep rollback to prior runtime until durable receipt.

## Migration procedure — future model

For a new model:

1. add capability profile;
2. bind through existing model adapter/router;
3. run R0 exact, R1 no-tool, R2 bounded-tool, R3 deep and R4 research tests as applicable;
4. measure latency, input/output tokens, retries, cache and tool behavior;
5. verify no public/private reasoning leakage;
6. confirm fallback/circuit policy;
7. promote by capability lane, not by brand.

## Anti-rebuild invariant

No future substrate migration is allowed to begin with “rebuild PRIME/ARC from scratch” unless explicit evidence proves the canonical state is unusable.

Migration order is:

```text
preserve Canon + identity + continuity
→ preserve Cognitive Connection contracts
→ adapt substrate
→ replay acceptance evidence
→ promote
```

## Current unresolved runtime-specific items

- Hermes `llm_request` middleware is supported by source contract but v0.3 live telemetry did not show mutation (`middleware_trace_count=0` and unchanged request fingerprint/size).
- Standalone synthetic probe at 2026-09-17 ~16:29 CEST reported `has_llm_request_middleware=False`, `changed=False`, `trace_count=0`, with `tools` and `tool_choice` still present. This proves that synthetic process did not expose the expected middleware registration; it does not by itself prove the live gateway uses the same plugin-discovery state.
- Laguna primary capacity remains unstable with provider-side ResourceExhausted events.
- Fallback UX leakage remains known but lower priority than cognition/capacity correctness.

## Founder continuity requirement

The quality of documentation is itself part of Reliable Excellence. Architecture, runtime mappings, failed hypotheses, evidence and migration boundaries must be good enough that a future engineer/agent can resume from the current state without rediscovering days of work.
