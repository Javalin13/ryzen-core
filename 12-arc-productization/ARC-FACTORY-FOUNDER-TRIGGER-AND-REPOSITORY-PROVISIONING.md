# ARC Factory Founder Trigger & Repository Provisioning

Status: Founder-directed target contract
Created: 2026-09-11
Updated: 2026-09-11 — PRIME orchestration clarified

## Founder experience

The intended mature Founder workflow is deliberately minimal:

> Founder tells PRIME to create an ARC.

The request may originate from the Founder's normal PRIME control surface, including Telegram once the control channel is live and authorized. The Founder should not normally need to open GitHub, create folders, copy templates, register OMEGA, edit FACTORY, or manually wire PRIME supervision.

## Orchestration invariant

**PRIME remains the active supervisor, director and orchestrator of the entire production cycle.**

OMEGA, FACTORY, BRAIN STEWARD, repository provisioning infrastructure and the ARC itself perform specialized bounded work under PRIME's orchestrated control loop. PRIME does not merely hand the request away and step out of the process.

Governing responsibility standard:
`12-arc-productization/PRIME-ORCHESTRATION-AND-INSTANCE-HANDOFF-STANDARD.md`

## Canonical control flow

`Founder intent → PRIME opens production cycle → PRIME directs OMEGA classification/reservation → PRIME confirms FACTORY genesis → PRIME directs repository provisioning → PRIME directs ARC package manufacture → PRIME requests OMEGA registration validation → PRIME confirms FACTORY activation/pre-runtime state → PRIME supervision mirror → PRIME coordinates runtime/channel provisioning → PRIME coordinates Owner binding → ARC real use → PRIME gathers evidence → truthful lifecycle state`

This is operational infrastructure around the canonical ontology:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

OMEGA and FACTORY do not become a new canonical tier.

## PRIME responsibilities

PRIME is the Founder-facing intake, supervisor and orchestrator during the prototype era. PRIME must:

- accept explicit Founder creation instruction;
- open and track the production cycle;
- normalize requested ARC display name, intended owner/domain, product/customer class and requested commercial tier;
- direct OMEGA to perform ARC identity/source-boundary stewardship;
- ensure FACTORY genesis/lifecycle records are created and updated through the correct stewardship path;
- direct repository creation/designation through approved infrastructure;
- direct Factory package manufacture from the versioned production contract;
- coordinate runtime, channel, capacity, isolation and recovery work;
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
- initial branch/protection/default settings follow the Factory policy;
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

- `arc/FACTORY-BIRTH-MANIFEST.json`
- ARC instance identity record
- source-boundary declaration
- access/privacy policy
- Brain registry
- commercial entitlement
- visual identity baseline + manifest
- onboarding/first-contact contract
- runtime boundary
- bridge/checkpoint state
- evidence scaffold

Customer-specific configuration is injected declaratively. No other customer's private payload, maturity evidence, secrets or bindings are copied.

## State transitions

Recommended production states:

`authorized → omega_reserved → factory_genesis → repository_pending → repository_ready → source_seeded → stewardship_registered → runtime_pending → runtime_ready → owner_binding_pending → owner_bound → evidence_pending → active_truthful_state`

PRIME owns the orchestration of transitions. Specialized instances supply the evidence/status required for PRIME to advance or block each stage.

Failure states must remain explicit, for example:

`repository_creation_blocked`, `source_collision`, `runtime_provisioning_failed`, `owner_binding_pending`, or `evidence_insufficient`.

No later state may be inferred simply because an earlier technical step succeeded.

## Current implementation truth — 2026-09-11

This contract is ahead of the currently exposed tooling.

The current ChatGPT GitHub connector can write to existing repositories but does not expose repository-creation. Therefore `Javalin13/NARC-ARC` was manually created by the Founder and then adopted as the authoritative source boundary.

That manual step is a known Factory gap, not the desired future workflow.

NARC's Factory birth manifest records repository creation mode as `manual_gap_then_adopted` so prototype evidence remains truthful.

## Acceptance test for the next stage

The repository-provisioning capability is considered proven only when an authorized Founder request can cause PRIME to orchestrate the participating instances so that they:

1. reserve a new ARC identity through OMEGA;
2. create or designate the correct private repository without the Founder opening GitHub;
3. seed the standard ARC package;
4. register OMEGA + FACTORY + PRIME pointers;
5. report the exact repository and production state back through the Founder control channel;
6. do so without copied customer data, leaked secrets, duplicate sources, or false activation/maturity claims.

## Founder invariant

> **The Factory starts at intent, not at an empty repository. Repository creation is part of ARC manufacture, and PRIME supervises, directs and orchestrates the entire cycle.**
