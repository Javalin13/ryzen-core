# RYZ3N Model & Agent Runtime Portability Contract

Date: **2026-09-17**  
Status: **Canonical engineering portability requirement**  
Master alignment: **M3/16 — Cargo ARC GREEN**

## Purpose

RYZ3N must never become architecturally dependent on one language model, one model provider, or one agent runtime.

Hermes is the current execution substrate. Laguna, local Qwen and other models are current intelligence substrates. None of them are the identity of PRIME, the identity of an ARC, or the owner of RYZ3N cognition.

The durable target is:

```text
Owner / Founder intent
→ RYZ3N sovereignty + identity + Canon
→ RYZ3N Cognitive Connection Layer
→ Brains / reasoning policy / tool policy / verification
→ capability request
→ model adapter and/or agent-runtime adapter
→ replaceable model / provider / agent runtime
→ tools / infrastructure / reality
```

## Core portability invariant

```text
PRIME ≠ Hermes
PRIME ≠ Laguna
PRIME ≠ NVIDIA
PRIME ≠ Qwen
PRIME ≠ Ollama

PRIME = RYZ3N identity + authority + memory/continuity + Canon + cognition architecture + replaceable execution substrates.
```

The same principle applies recursively to every ARC.

## What must remain RYZ3N-owned

The following must remain above and independent of the current agent/model substrate whenever technically possible:

- Owner identity, authority and sovereignty boundaries;
- current intent and intent supersession;
- ARC identity, aura/form/maturity and capability state;
- Canon and governance;
- Brain composition and specialization contracts;
- reasoning classes / reasoning budget policy;
- tool/no-tool policy;
- action/observation/verification loop semantics;
- stopping rules and bounded recursion;
- private/action/public state separation;
- public output discipline;
- capability and resource policy;
- evidence, receipts, continuity and migration state;
- acceptance tests and Reliable Excellence gates.

## What may be substrate-specific

Substrate-specific integration is allowed only at bounded adapters/seams:

### Model adapter

A model adapter may define:

- provider/model identifier;
- context-window and output limits;
- structured-tool-call support;
- reasoning/thinking controls where available;
- multimodal capabilities;
- latency/cost/capacity metadata;
- provider-specific request/response normalization;
- fallback compatibility;
- known degradation patterns.

### Agent-runtime adapter

An agent-runtime adapter may define:

- lifecycle hook mapping;
- middleware/request transformation mapping;
- tool registry mapping;
- session/turn identity mapping;
- runtime transport integration;
- system-prompt/context injection seams;
- tool execution interception;
- output transformation/public-delivery seams;
- telemetry and health signals;
- startup/discovery/reload behavior.

The adapter must not silently become the source of RYZ3N cognition or governance.

## Migration requirement

A future model or runtime switch must not require rebuilding PRIME/ARCs from scratch.

A compliant migration should be mostly:

```text
1. characterize new substrate capabilities
2. implement/adjust adapter
3. map existing RYZ3N contracts onto substrate seams
4. run canonical acceptance matrix
5. compare evidence against current baseline
6. cut over reversibly
7. preserve rollback and continuity
```

If migration requires rewriting Owner identity, Canon, Brain architecture, ARC business logic, or continuity payloads, portability has failed.

## Required migration artifact set

Every runtime/model integration must leave durable records sufficient for a future engineer or agent to reproduce or replace it without rediscovery from scratch:

- architecture decision and rationale;
- exact runtime/model/provider versions where material;
- adapter/seam map;
- source paths/functions touched;
- environment/runtime assumptions;
- deployment path and service boundary;
- configuration contract excluding secrets;
- plugin/hook/middleware registration contract;
- tool-routing contract;
- context/prompt contract;
- public-output contract;
- fallback/circuit behavior;
- telemetry/evidence paths;
- acceptance tests and expected results;
- known defects and non-goals;
- rollback/isolation boundaries;
- migration notes for a different model;
- migration notes for a different agent runtime.

## Anti-restart-from-zero rule

No future migration may begin by discarding the current knowledge base unless the existing records are proven unusable.

Before switching model or agent runtime, the operator must first read:

1. this portability contract;
2. the Cognitive Connection architecture direction;
3. the current master alignment;
4. the active runtime plugin source and manifest;
5. relevant evidence receipts;
6. the latest acceptance matrix / GREEN receipts;
7. known substrate-specific deviations.

The goal is **reuse of RYZ3N cognition contracts, not reinvention**.

## Current Hermes lesson

The present Hermes integration is intentionally being used to discover and formalize the correct seams:

- `pre_gateway_dispatch` for generic ingress/control observation;
- `pre_llm_call` for per-turn semantic context/policy injection;
- `pre_tool_call` for tool-execution control;
- `transform_llm_output` for public-output enforcement;
- `llm_request` middleware for request-local provider payload transformation;
- `pre_api_request` / post/error hooks for telemetry and evidence.

These are **Hermes mappings of RYZ3N contracts**, not the contracts themselves.

A future agent runtime may expose different names and APIs. The migration task is to map equivalent RYZ3N semantics onto the new runtime, not to redesign RYZ3N around that runtime.

## Model portability acceptance

A new model integration is not accepted until it proves, at minimum:

- R0 exact/direct behavior;
- R1 bounded no-tool behavior;
- representative reasoning quality;
- correct tool/no-tool judgment;
- bounded agentic execution where applicable;
- no private reasoning leakage;
- public-output discipline;
- acceptable latency/capacity behavior;
- fallback/degradation behavior;
- no loss of Owner/ARC identity or continuity.

## Agent-runtime portability acceptance

A new agent runtime is not accepted until it proves equivalent or better support for:

- authenticated ingress;
- session/turn continuity;
- RYZ3N reasoning-lane control;
- request-local model/tool payload control;
- bounded tool execution;
- observation/verification loops;
- public-output transformation;
- telemetry and health evidence;
- restart/recovery boundaries;
- PRIME/ARC identity preservation;
- reversible migration.

## Documentation quality requirement

Engineering records are part of the product architecture, not administrative afterthought.

For every material change:

```text
intent
→ reason for change
→ evidence before
→ exact seam/path/function
→ implementation
→ deployment proof
→ behavioral acceptance
→ measured effect
→ remaining defect/non-goal
→ rollback boundary
→ portability implication
```

This chain should be recoverable from Git history and evidence files without relying on Founder memory or chat reconstruction.

## Strategic objective

The long-term payoff of the current intensive Cognitive Connection work is to make RYZ3N progressively easier to connect to stronger future intelligence and execution substrates while preserving its identity, business logic, governance, memory and acceptance standards.

The architectural asset is therefore not Hermes or any individual model. It is the **portable RYZ3N cognition and control contract**.
