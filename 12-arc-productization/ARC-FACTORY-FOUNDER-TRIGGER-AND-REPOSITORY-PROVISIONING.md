# ARC Factory Founder Trigger & Repository Provisioning

Status: Founder-directed target contract
Created: 2026-09-11

## Founder experience

The intended mature Founder workflow is deliberately minimal:

> Founder tells PRIME to create an ARC.

The request may originate from the Founder's normal PRIME control surface, including Telegram once the control channel is live and authorized. The Founder should not normally need to open GitHub, create folders, copy templates, register OMEGA, edit FACTORY, or manually wire PRIME supervision.

## Canonical control flow

`Founder intent → PRIME intake → OMEGA classification/reservation → FACTORY genesis record → repository provisioning → ARC package manufacture → OMEGA active registration → FACTORY activation → PRIME supervision mirror → runtime/channel provisioning → Owner binding → evidence gate`

This is operational infrastructure around the canonical ontology:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

OMEGA and FACTORY do not become a new canonical tier.

## PRIME responsibilities

PRIME is the Founder-facing intake and orchestration surface during the prototype era. PRIME must:

- accept an explicit Founder creation instruction;
- normalize the requested ARC display name, intended owner/domain, product/customer class and requested commercial tier;
- forward the request into OMEGA/FACTORY production rather than manually constructing the ARC itself;
- obtain explicit Founder clarification only where intent is genuinely ambiguous or materially consequential;
- surface production status, blockers and completion back to the Founder;
- never invent customer/domain ownership or silently select paid external services.

## OMEGA pre-repository responsibilities

OMEGA begins work **before the repository exists**. It must:

- reserve a unique `arc_id`;
- detect naming/identity collisions;
- classify the source boundary;
- determine whether the ARC belongs inside an existing RYZ3N product/domain repository or requires a dedicated customer/standalone repository;
- reject a second active source of truth;
- derive the required repository name/path under the applicable naming policy;
- prepare a privacy-safe creation specification for FACTORY/PRIME;
- record all unresolved assumptions explicitly rather than promoting them to facts.

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

The genesis record is not activation and carries no maturity/aura.

## Repository provisioning contract

For a new customer/standalone ARC, the Factory target is that PRIME uses a narrowly scoped GitHub App/service credential to create the repository automatically.

Default requirements:

- repository is **private** unless Founder explicitly authorizes otherwise;
- repository is created under the approved RYZ3N/GitHub account or organization;
- name is deterministic from the approved Factory specification;
- no secrets are committed;
- initial branch/protection/default settings follow the Factory policy;
- repository description is generated from non-sensitive ARC identity metadata;
- creation result is written back to FACTORY and OMEGA;
- creation failure halts downstream production and reports the exact blocker to PRIME.

For a RYZ3N-owned product/domain ARC, the Factory must usually designate the existing product repository and create the bounded `arc/` package instead of creating a new repository.

## Repository-creation authority

Repository creation is a privileged side effect and must use least privilege.

The Factory must not depend on a broad personal access token when a narrower GitHub App/service identity can provide the required repository administration scope. Repository creation credentials remain outside Git and outside ARC customer memory.

The repository creator is infrastructure. It does not become the ARC Owner.

## Telegram / control-channel trigger

Telegram is a **control surface**, not the authority itself.

A future approved PRIME Telegram control path may accept requests such as:

`Create ARC: NARC; customer/standalone; Owner: Narek; language: French; tier: Standard.`

Before any privileged creation action, PRIME must verify that the message originates from an authorized Founder/operator identity and preserve an audit pointer to the accepted intent.

Customer-facing ARC bots/channels must never be allowed to create arbitrary new ARC repositories merely because they can send messages to PRIME.

## Automatic package manufacture

After repository creation/designation, Factory manufacture should instantiate the standard source package from the versioned Factory contract:

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

Failure states must remain explicit, for example:

`repository_creation_blocked`, `source_collision`, `runtime_provisioning_failed`, `owner_binding_pending`, or `evidence_insufficient`.

No later state may be inferred simply because an earlier technical step succeeded.

## Current implementation truth — 2026-09-11

This contract is ahead of the currently exposed tooling.

The current ChatGPT GitHub connector can write to existing repositories but does not expose repository-creation. Therefore `Javalin13/NARC-ARC` was manually created by the Founder and then adopted as the authoritative source boundary.

That manual step is a known Factory gap, not the desired future workflow.

NARC's Factory birth manifest must record repository creation mode as `manual_gap_then_adopted` so the prototype evidence remains truthful.

## Acceptance test for the next stage

The repository-provisioning capability is considered proven only when an authorized Founder request can cause PRIME/OMEGA/FACTORY to:

1. reserve a new ARC identity;
2. create or designate the correct private repository without the Founder opening GitHub;
3. seed the standard ARC package;
4. register OMEGA + FACTORY + PRIME pointers;
5. report the exact repository and production state back through the Founder control channel;
6. do so without copied customer data, leaked secrets, duplicate sources, or false activation/maturity claims.

## Founder invariant

> **The Factory starts at intent, not at an empty repository. Repository creation is part of ARC manufacture.**
