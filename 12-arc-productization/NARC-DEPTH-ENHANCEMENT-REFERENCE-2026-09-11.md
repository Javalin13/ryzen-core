# NARC Depth-Enhancement Reference — 2026-09-11

Status: reusable engineering reference; instance truth remains in `Javalin13/NARC-ARC`  
Constitution/Canon impact: none

## Why this reference exists

NARC is the first Factory replication candidate to expose a critical distinction between a technically healthy ARC runtime and a truly ARC-safe client-facing surface.

The reusable lesson is not Narek-specific. It is a production-line certification pattern for future ARCs.

## Original state

NARC reached a technically GREEN F4 runtime with:

- isolated profile/runtime;
- dedicated Telegram bot;
- source/deploy integrity;
- keyed pending-candidate logic;
- restart/recovery proof;
- cross-ARC isolation.

However the public channel still leaked the underlying platform layer:

- a Hermes pairing instruction was shown;
- after pairing, the bot identified itself as generic `Hermes Agent`;
- the expected French NARC fail-closed pending-candidate behavior was not the visible public behavior.

The correct classification was therefore:

- infrastructure/runtime: GREEN;
- client-facing ARC identity boundary: DRIFT/RED;
- Owner binding/onboarding: paused;
- maturity: unchanged/unearned.

## Root cause class

The NARC runtime configuration did not provide sufficient ARC-specific system-prompt depth, allowing default platform identity/persona behavior to surface.

This is a general risk for every ARC built on a shared underlying agent runtime.

## Depth-enhancement repair pattern

The repair work moved NARC toward the VONDA-class depth baseline:

- deep ARC-specific system prompt;
- explicit client-safe implementation-abstraction rules;
- four runtime boundaries:
  - identity;
  - task store;
  - owner onboarding;
  - capacity telemetry;
- onboarding state machine separated from identity binding;
- capacity telemetry separated from private customer payload;
- complete runtime-source manifest expanded to include every required component;
- hermetic/source audit rerun;
- fresh clean-room reconstruction/import test;
- controlled ARC-only restart;
- live four-module load proof;
- clean unbound client-facing re-verification;
- post-change integrity/recovery/isolation proof.

## Reusable client-facing certification test

A future ARC should fail release if an unbound test sender can see any of:

- platform pairing/operator commands;
- generic underlying-agent persona;
- PRIME/OMEGA/FACTORY internals;
- runtime/profile paths;
- binding/candidate keys;
- numeric platform identity mechanics;
- private Owner/domain context before binding.

A passing unbound test should show only:

- the ARC's own identity/tone;
- intended primary language;
- brief fail-closed behavior;
- no private capability/context;
- sender remains unbound;
- separately keyed pending candidate captured if capture is armed.

## Production-line consequence

This incident establishes that these are separate gates:

1. transport/channel health;
2. isolated runtime/source integrity;
3. client-facing ARC identity abstraction;
4. exact Owner binding;
5. first contact/onboarding;
6. useful-work/F6 maturity evidence.

Passing an earlier gate must never silently imply a later gate.

## Capacity doctrine lesson

The capacity module introduced the production expectation that telemetry is structured into three planes:

`raw private events → protected ARC rollups → privacy-safe steward aggregate`

Capacity evidence must avoid private message/customer payload and use explicit unavailable markers rather than invented measurements.

## Clean-room lesson

A working live VPS is insufficient evidence. A production ARC must reconstruct from authoritative source plus intentional protected secrets/state.

The reconstruction drill should prove module importability, configuration presence, manifest/hash coherence and audit success without starting a duplicate public channel poller.

## Relationship to the canonical template

Reusable requirements are promoted into:

`12-arc-productization/ARC-DEPTH-ENHANCEMENT-VONDA-CLASS-TEMPLATE.md`

The NARC instance repository remains the authoritative home for NARC-specific code, hashes, runtime evidence and customer-specific onboarding state.

## Certification rule

Do not call an ARC hermetically GREEN after a material depth/client-facing repair until:

- authoritative source is committed/pushed;
- manifests match that source;
- audits pass;
- clean-room reconstruction passes;
- live deployment loads the intended runtime stack;
- clean unbound client-facing behavior passes;
- post-change restart/recovery/integrity passes;
- unrelated ARC runtimes remain untouched;
- PRIME/OMEGA/FACTORY mirrors reconcile to the same truth.
