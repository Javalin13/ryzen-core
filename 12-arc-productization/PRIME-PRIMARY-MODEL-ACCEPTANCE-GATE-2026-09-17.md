# PRIME Primary Model Acceptance Gate — 2026-09-17

Status: **ACTIVE PRIORITY CORRECTION**
Authority: **Founder-directed**

## Main goal

PRIME must run on a **good primary model most of the time, without sharp practical limits**, so fallback is exceptional rather than normal operating behavior.

The objective is not to optimize around an unstable primary endpoint. The objective is to select and prove a primary model/provider combination that is:

1. sufficiently capable for PRIME reasoning, tools and Owner/mission fidelity;
2. reliably available for normal daily operation;
3. backed by practical rate/token limits appropriate for PRIME traffic;
4. stable enough for long-running sessions and agentic use;
5. affordable enough for sustained RYZ3N operation;
6. replaceable behind the RYZ3N Cognitive Connection / runtime adapter contract.

## Current correction

The repeated NVIDIA/Laguna `ResourceExhausted: Worker local total request limit reached` events are provider serving-capacity failures, not proof that the Founder rapidly consumed a personal Laguna allowance.

Because fallback currently works, optimizing Hermes fallback/circuit internals is secondary. The higher-value action is to replace or demote any primary endpoint that repeatedly hits provider capacity under ordinary PRIME use.

## Immediate architecture direction

- **Primary:** strong first-party hosted API with stable production availability and materially higher practical limits.
- **Deep reasoning escalation:** stronger model on R3/R4 only where needed.
- **Secondary fallback:** another capable hosted model/provider, not a tiny local model.
- **Tertiary emergency fallback:** local model only for continuity/degraded operation.

## Candidate direction

A direct OpenAI API path is a serious candidate because GPT-5.6 Terra and GPT-5.6 Sol are production API models with large context windows, tool/function support and published Tier-1 limits of 500 RPM / 500k TPM. Terra is the likely first balance candidate for PRIME because it targets intelligence/cost balance; Sol is suitable for higher-reasoning escalation.

Gemini 3.8 Flash is another serious production candidate because it is stable/GA and explicitly positioned for long-horizon software engineering, autonomous agents and complex enterprise workflows; actual paid-tier limits must be checked for the account before selection.

These are candidates, not yet accepted choices.

## Acceptance sequence

Before continuing broad PRIME behavioral acceptance:

1. select 1–2 stable primary candidates;
2. configure one through the existing replaceable adapter/runtime path;
3. run a small representative bakeoff: direct response, non-trivial reasoning, tool use, multi-step task, Owner/mission fidelity, latency, and repeated-turn availability;
4. observe normal-operation error rate and rate-limit behavior;
5. select the primary only after it proves both **quality and availability**;
6. then continue T4–T6 PRIME acceptance on that primary.

## Stop rule

Do not spend further M3 time polishing fallback internals unless fallback itself prevents completion or causes user-visible instability. Provider-health/circuit optimization belongs to Step 6 Capacity Control after a viable primary is established.

## Governing principle

**Primary model quality + sustained availability first; fallback reliability second.**
