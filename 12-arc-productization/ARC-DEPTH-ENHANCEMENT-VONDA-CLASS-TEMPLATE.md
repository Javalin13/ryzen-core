# ARC Depth Enhancement — VONDA-Class Production Template

Status: Founder-directed reusable production-line template  
Effective: 2026-09-11  
Scope: Standard ARC runtime depth, client-facing identity quality, onboarding, capacity telemetry, clean-room verification  
Constitution/Canon impact: none

## Purpose

A Factory-born ARC must not stop at "gateway is running" or "identity plugin exists". The production line must manufacture enough runtime depth that the ARC presents as itself, keeps operator/platform machinery behind the curtain, onboards the exact Owner safely, measures capacity without leaking private payload, and can be reconstructed from authoritative source.

This template generalizes the depth pattern proven through VONDA and the NARC client-facing repair/hardening work.

> **Future ARCs inherit the depth contract by default; customer/domain payload remains instance-specific.**

## Default four-boundary runtime stack

A Standard ARC should ship with four explicit runtime responsibilities. Implementations may be separate plugins/modules, but the boundaries must remain independently testable.

1. **`<arc>_identity`**
   - resolves the actual current sender from the ARC's own isolated runtime state;
   - unknown users fail closed;
   - keyed pending candidates remain separate;
   - exact Owner/role binding is operator/Founder approved;
   - no cross-ARC private identity inference;
   - user-facing prompt blocks never expose candidate keys, numeric identifiers, namespaces, runtime paths, PRIME/OMEGA/FACTORY/Hermes machinery.

2. **`<arc>_task_store`**
   - keeps bounded durable work/memory/task state inside the ARC's own namespace;
   - no cross-owner or cross-ARC namespace reads/writes;
   - client-safe abstractions rather than raw implementation labels.

3. **`<arc>_owner_onboarding`**
   - owns the first-run state machine after exact Owner binding;
   - reads binding state but never self-binds;
   - keeps a durable progression such as `pre_binding → first_contact_pending → choice/step_recorded → complete`;
   - instance-specific easter eggs/copy stay configuration, not architecture;
   - never exposes backend transition/state machinery to the Owner.

4. **`<arc>_capacity_telemetry`**
   - records privacy-safe consumption/health signals without message content or identity payload;
   - raw events and protected rollups remain ARC-local;
   - only safe aggregate stewardship data may cross into portfolio oversight;
   - explicit unavailable markers are preferable to fabricated metrics;
   - rate-limit/headroom and disproportionate-consumption warnings are evidence signals, not automatic commercial/maturity decisions.

Any deviation from the four-boundary baseline must be explicit, evidence-backed and recorded in the ARC birth/runtime manifest. It must not occur merely because an earlier prototype happened to use fewer modules.

## VONDA-class system-prompt depth

The runtime configuration must contain an ARC-specific system prompt. An empty/default platform prompt is not acceptable on a public ARC channel.

At minimum it must define:

- ARC identity and domain mission;
- primary/secondary language and natural register;
- tone/voice and formatting quality rules;
- verified-Owner versus pending/unknown behavior;
- client-safe labels/abstractions;
- side-effect discipline (`read ≠ write`, proposal ≠ execution);
- domain-grounding and hypothesis labeling rules;
- local-time rendering rule where relevant;
- bounded tool/capability description;
- first-contact/onboarding behavior;
- explicit cross-ARC/source-boundary restrictions;
- a strong implementation-abstraction rule.

### Minimum never-expose categories

The client-facing prompt must prevent narration of at least these implementation classes when they are not intentionally part of the product surface:

1. Hermes/platform identity or pairing machinery;
2. PRIME internals;
3. RYZ3N operator scaffolding;
4. OMEGA internals;
5. FACTORY internals;
6. BRAIN STEWARD/internal Brain governance;
7. ARC runtime/profile paths;
8. numeric sender/session/platform IDs;
9. candidate keys/binding files/namespaces;
10. secret/token/provider credential handling;
11. raw telemetry/storage implementation;
12. repository/operator-only mechanics not needed by the customer.

The exact names can differ by runtime, but the abstraction boundary is mandatory.

## Client-facing release gate

A public channel is not GREEN merely because transport is connected.

Before release or re-entry after drift, a clean unbound sender must prove:

- no platform pairing/operator command is exposed;
- no generic platform persona replaces the ARC persona;
- the sender reaches the ARC's own keyed pending-candidate flow;
- the response is in the intended ARC language/tone;
- the response is brief, natural and fail-closed;
- the sender remains unbound;
- no PRIME/OMEGA/FACTORY/Hermes/runtime/profile/binding/candidate machinery leaks;
- no private Owner/domain namespace becomes available before exact binding.

This is a separate gate from Telegram/transport health.

## Capacity telemetry doctrine

Capacity telemetry uses three planes:

`raw ARC-local events → ARC-local protected rollups → privacy-safe steward aggregate`

Rules:

- raw events: mode/protection appropriate to ARC private runtime;
- rollups: private ARC summary suitable for local enforcement;
- steward aggregate: only minimum non-private capacity/health facts needed for PRIME/OMEGA oversight;
- never record message content, private business content, personal platform IDs, display names, secrets or Owner memory in telemetry;
- every signal can be `available`, `unavailable`, or `degraded`; never fabricate values;
- recommended baseline signals include request counts, success/error counts, rate-limit events, latency, token/AU proxy where available, capacity headroom, retry pressure, tool failure rate, queue/concurrency pressure and disproportionate-consumption indication;
- a practical disproportionate-consumption heuristic may flag a current window above `3×` the median of a recent comparable window set, but this remains a warning signal, not an entitlement rewrite;
- a default rate-limit/headroom warning floor of `20%` may be used where provider data is available;
- entitlement hard stops and silent-overage rules remain governed by the ARC commercial/capacity contract.

## Authoritative runtime-source manifest

The manifest must include every ARC-specific runtime component required to reproduce behavior, including:

- deep runtime config/system prompt;
- identity module + metadata;
- task-store module + metadata;
- onboarding module + metadata;
- capacity-telemetry module + metadata;
- launch/recovery scripts;
- binding/first-contact scripts;
- audits/verifiers required for reconstruction.

Each versioned component should carry cryptographic source identity and, where live-deployed, deployed-content verification.

A working VPS file that is not versioned/manifsted is not authoritative production truth.

## Clean-room reconstruction gate

Before GREEN closure after a material runtime-depth change:

1. start from a fresh clone/export of authoritative source;
2. verify manifest/hash coherence;
3. import/load all required runtime modules without relying on accidental VPS residue;
4. confirm configuration is present and syntactically valid;
5. run hermetic/source audits;
6. do not start an unsafe duplicate public poller during the drill;
7. prove the runtime can be rebuilt from source plus intentional protected secrets/state only.

## Live deployment gate

After source passes clean-room checks:

1. deploy only from authoritative ARC source;
2. controlled ARC-only restart;
3. prove all expected modules/plugins are loaded;
4. prove channel health;
5. run clean unbound client-facing test;
6. verify exact candidate remains unbound;
7. rerun source/deploy integrity;
8. prove controlled restart/recovery;
9. prove other ARCs/PRIME-default were untouched.

Only then may a prior client-facing RED/DRIFT return GREEN.

## Factory inheritance

Every future ARC Factory package should inherit pointers/checks for:

- four-boundary runtime baseline;
- deep ARC-specific system prompt;
- never-expose implementation-abstraction rules;
- client-facing release test;
- privacy-safe capacity telemetry;
- complete runtime-source manifest;
- clean-room reconstruction;
- live loaded-module proof;
- post-change recovery/integrity/isolation proof.

Factory automation may render names/configuration from `arc_id`, domain, language and entitlement. It must not copy another customer's private payload, bindings, memory, secrets, earned maturity or visual form.

## NARC reference

NARC revealed why this depth contract belongs upstream:

- a technically healthy gateway still fell back to a generic platform persona when its ARC system prompt was effectively empty;
- client-facing leakage correctly reopened the hermetic/onboarding gate without erasing already-proven transport/isolation facts;
- the repair expanded NARC from a minimal two-module runtime toward the four-boundary VONDA-class depth pattern;
- clean-room and live unbound re-verification became part of the acceptance gate rather than optional QA.

Detailed customer/runtime evidence remains in `Javalin13/NARC-ARC`; this reusable document contains only the production lesson.

## Founder invariant

> **An ARC is production-deep only when it behaves as itself at the client boundary, reconstructs from authoritative source, keeps private machinery private, onboards exact identities safely and reports capacity without leaking customer payload.**
