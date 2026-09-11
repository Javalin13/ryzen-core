# ARC Factory Founder Trigger & Repository Provisioning

Status: Founder-directed target contract  
Created: 2026-09-11  
Updated: 2026-09-11 — PRIME orchestration + hermetic birth contract integrated  
Constitutional status: non-canon implementation standard; protected Constitution/Canons unchanged

## Founder experience

The intended mature Founder workflow is deliberately minimal:

> **Founder tells PRIME to create an ARC.**

The request may originate from the Founder's normal PRIME control surface, including Telegram once the control channel is live and authorized. The Founder should not normally need to open GitHub, create folders, copy templates, register OMEGA, edit FACTORY, wire PRIME supervision, design pending-candidate storage, create recovery scripts, or manually bolt on a hermetic runtime boundary.

Those are Factory responsibilities orchestrated by PRIME.

## Orchestration invariant

**PRIME remains the active supervisor, director and orchestrator of the entire production cycle.**

OMEGA, FACTORY, BRAIN STEWARD, repository provisioning infrastructure and the ARC itself perform specialized bounded work under PRIME's orchestrated control loop. PRIME does not merely hand the request away and step out of the process.

Governing responsibility standards:

- `12-arc-productization/PRIME-ORCHESTRATION-AND-INSTANCE-HANDOFF-STANDARD.md`
- `12-arc-productization/ARC-REPLICATION-FACTORY-PRODUCTION-STANDARD.md`
- `12-arc-productization/ARC-HERMETIC-OPERATIONS-AND-AUTONOMY-STANDARD.md`

## Canonical control flow

`Founder intent → PRIME opens production cycle → PRIME directs OMEGA classification/reservation → PRIME confirms FACTORY genesis → PRIME directs repository provisioning → PRIME directs ARC package + hermetic contract manufacture → PRIME requests OMEGA registration validation → PRIME confirms FACTORY activation/pre-runtime state → PRIME supervision mirror → PRIME coordinates isolated runtime/channel/capacity + source/recovery controls → PRIME coordinates exact-candidate Owner binding → ARC real use → PRIME gathers evidence → truthful lifecycle/hermetic/maturity state`

This is operational infrastructure around the canonical ontology:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

OMEGA and FACTORY do not become a new canonical tier. There is no separate Horizon layer.

## PRIME responsibilities

PRIME is the Founder-facing intake, supervisor and orchestrator during the prototype era. PRIME must:

- accept explicit Founder creation instruction;
- open and track the production cycle;
- normalize requested ARC display name, intended owner/domain, product/customer class and requested commercial tier;
- direct OMEGA to perform ARC identity/source-boundary stewardship;
- ensure FACTORY genesis/lifecycle records are created and updated through the correct stewardship path;
- direct repository creation/designation through approved infrastructure;
- direct Factory package manufacture from the versioned production contract;
- initialize/inherit the ARC hermetic-seal contract at birth;
- coordinate runtime, channel, capacity, isolation, complete runtime-source closure and recovery work;
- ensure keyed multi-candidate fail-closed onboarding before public channel exposure;
- ensure client-facing users interact with the ARC while PRIME stays backend infrastructure;
- declare repository autonomy disabled by default unless explicitly granted;
- if autonomy is granted, install/verify safe shared-writer concurrency before production use;
- involve BRAIN STEWARD only for Brain-level lifecycle/coherence responsibilities;
- block stage progression when any required gate fails;
- surface production status, blockers and completion back to Founder;
- obtain explicit Founder clarification only where intent is genuinely ambiguous or materially consequential;
- never invent customer/domain ownership or silently select paid external services.

PRIME orchestrates; it does not become the detailed source home of the ARC.

## OMEGA pre-repository responsibilities under PRIME

OMEGA begins work **before the repository exists**, when directed by PRIME. It must:

- reserve/check a unique `arc_id`;
- detect naming/identity collisions;
- classify the source boundary;
- determine whether the ARC belongs inside an existing RYZ3N product/domain repository or requires a dedicated customer/standalone repository;
- reject a second active source of truth;
- derive the required repository name/path under the applicable naming policy;
- prepare a privacy-safe creation specification for PRIME/FACTORY;
- initialize expected hermetic state as `inherited_pre_runtime` for a new ARC;
- record all unresolved assumptions explicitly rather than promoting them to facts;
- return classification/result/blockers to PRIME.

OMEGA does not independently orchestrate the full creation cycle.

## FACTORY genesis record

FACTORY must support a pre-repository genesis state. The ARC receives a lifecycle record before the source repository is created.

Minimum genesis fields:

- reserved `arc_id`;
- requested display name;
- Founder authorization timestamp/pointer;
- repository class;
- intended repository owner/account;
- intended repository name/path;
- privacy/visibility requirement;
- owner/entity class;
- requested commercial tier;
- primary language if known;
- production state;
- OMEGA steward status;
- initial hermetic state (`inherited_pre_runtime` for normal new birth);
- autonomy default (`not_granted` unless explicitly authorized);
- unresolved facts;
- source repository status (`pending`, `created`, `designated`, or `failed`).

FACTORY records; it does not orchestrate or reason. The genesis record is not activation and carries no maturity/aura.

## Repository provisioning contract

For a new customer/standalone ARC, the Factory target is that PRIME directs a narrowly scoped GitHub App/service capability to create the repository automatically.

Default requirements:

- repository is **private** unless Founder explicitly authorizes otherwise;
- repository is created under the approved RYZ3N/GitHub account or organization;
- name is deterministic from the approved Factory specification;
- no secrets are committed;
- default branch settings follow Factory policy;
- where supported, branch protection/rules prohibit force push/deletion and require appropriate CI;
- where private-repository protection features are unavailable, Factory records compensating controls such as safe-writer + CI + OMEGA drift detection;
- repository description is generated from non-sensitive ARC identity metadata;
- creation result is returned to PRIME and written into FACTORY/OMEGA state;
- creation failure halts downstream production and reports the exact blocker to PRIME.

For a RYZ3N-owned product/domain ARC, PRIME should normally direct designation of the existing product repository and creation of the bounded `arc/` package instead of creating a new repository.

## Repository-creation authority

Repository creation is a privileged side effect and must use least privilege.

The infrastructure must not depend on a broad personal access token when a narrower GitHub App/service identity can provide the required repository administration scope. Repository creation credentials remain outside Git and outside ARC customer memory.

The repository creator is infrastructure. It does not become the ARC Owner.

## Telegram / control-channel trigger

Telegram is a **control surface**, not the authority or orchestrator itself.

A future approved PRIME Telegram control path may accept requests such as:

`Create ARC: NARC; customer/standalone; Owner: Narek; language: French; tier: Standard.`

Before any privileged creation action, PRIME must verify that the message originates from an authorized Founder/operator identity and preserve an audit pointer to the accepted intent.

Customer-facing ARC bots/channels must never be allowed to create arbitrary new ARC repositories merely because they can send messages to PRIME.

## Automatic package manufacture

After repository creation/designation, PRIME directs Factory manufacture from the versioned production contract:

- `arc/FACTORY-BIRTH-MANIFEST.json`;
- ARC instance identity record;
- source-boundary declaration;
- access/privacy policy;
- Brain registry;
- commercial entitlement;
- visual identity baseline + manifest;
- onboarding/first-contact contract;
- **ARC-specific `arc/HERMETIC-SEAL.md` or equivalent**;
- runtime boundary;
- **planned `arc/runtime/runtime-source-manifest.json` location/contract**;
- **keyed multi-candidate onboarding requirement**;
- **repository autonomy state**;
- **safe-writer requirement when autonomy is enabled**;
- **source-driven recovery / clean-room reconstruction requirement**;
- bridge/checkpoint state;
- evidence scaffold.

Customer-specific configuration is injected declaratively. No other customer's private payload, maturity evidence, secrets, bindings or private runtime configuration are copied.

## Runtime provisioning gate

Repository/package manufacture alone may not advance directly to customer activation.

Before `runtime_ready`, PRIME must prove or truthfully mark pending:

- isolated ARC runtime/profile;
- ARC-only state/secrets/binding boundary;
- no direct dependency on another ARC's private runtime files;
- complete authoritative source for every ARC-specific runtime component;
- runtime-source manifest with hashes/recovery rules;
- unknown identity fail-closed;
- keyed pending-candidate model;
- exact-candidate binding path;
- client-facing ARC-only experience;
- model/capacity assignment;
- health/telemetry controls;
- source-driven recovery;
- clean-room source reconstruction;
- safe shared-writer if repository autonomy has been granted;
- CI/audit enforcement.

A gateway PID alone is not `runtime_ready`.

## State transitions

Recommended production states:

`authorized → omega_reserved → factory_genesis → repository_pending → repository_ready → source_seeded → stewardship_registered → runtime_pending → hermetic_runtime_hardening → runtime_ready → owner_binding_pending → owner_bound → evidence_pending → active_truthful_state`

PRIME owns the orchestration of transitions. Specialized instances supply the evidence/status required for PRIME to advance or block each stage.

Hermetic state is tracked separately in parallel:

`inherited_pre_runtime → hardening_in_progress → GREEN`

or a truthful `DRIFT/RED` if an invariant regresses.

Failure states remain explicit, for example:

`repository_creation_blocked`, `source_collision`, `runtime_source_incomplete`, `cross_arc_runtime_dependency`, `candidate_binding_ambiguous`, `unsafe_writer`, `runtime_provisioning_failed`, `owner_binding_pending`, or `evidence_insufficient`.

No later state may be inferred simply because an earlier technical step succeeded.

## Current implementation truth — 2026-09-11

This contract remains ahead of some exposed infrastructure capabilities.

The current ChatGPT GitHub connector can write to existing repositories but does not expose repository creation. Therefore `Javalin13/NARC-ARC` was manually created by the Founder and then adopted as the authoritative source boundary.

That manual step is a known Factory gap, not the desired future workflow.

NARC's Factory birth manifest records repository creation mode as `manual_gap_then_adopted`. NARC now also inherits the hermetic contract before F4 runtime provisioning, preventing Cargo's post-launch hardening gaps from being copied forward.

Current private-repository ruleset enforcement may also depend on account/plan capability. Where unavailable, Factory must compensate with repository-local safe-writer, CI and steward drift detection rather than weakening write safety.

## Acceptance test for the next stage

The repository-provisioning + birth capability is considered proven only when an authorized Founder request can cause PRIME to orchestrate the participating instances so that they:

1. reserve a new ARC identity through OMEGA;
2. create or designate the correct private repository without the Founder opening GitHub;
3. seed the standard ARC package including hermetic contract;
4. register OMEGA + FACTORY + PRIME pointers;
5. declare autonomy state and install safe writer if required;
6. prepare complete runtime-source/recovery/onboarding contracts before production runtime;
7. report the exact repository and production state back through the Founder control channel;
8. do so without copied customer data, leaked secrets, duplicate sources, ambiguous auto-binding, cross-ARC runtime dependency or false activation/maturity claims.

## Founder invariant

> **The Factory starts at intent, not at an empty repository. Repository creation, hermetic sealing, recovery design and write safety are part of ARC manufacture, and PRIME supervises, directs and orchestrates the entire cycle.**
