# ARC Factory Readiness Audit — 2026-09-11

Status: current-reality audit after NARC F0–F3 registration
Scope: RYZ3N Core, PRIME, OMEGA, FACTORY, BRAIN STEWARD, NARC, Factory replication path

## Executive verdict

The **architecture, authority split, source-boundary model and NARC registration state are aligned**.

The Factory is **not yet fully state-of-the-art operational automation**. It now has the correct production contract, machine-readable creation/birth schemas, reusable source template, PRIME orchestration/handoff rules and an executable source-package invariant validator. The remaining critical gaps are privileged infrastructure/runtime automation and live evidence.

Therefore the truthful state is:

`Factory contract = strong / aligned`
`Factory source replication layer = v1 established`
`Factory privileged automation = incomplete`
`NARC = registered_pre_runtime (F0–F3 complete; F4–F6 pending)`

## Board-wide authority alignment

| Surface | Required role | Audit state | Result |
|---|---|---|---|
| RYZ3N | canonical platform identity / reusable architecture | canonical hierarchy preserved | GREEN |
| PRIME | supervisor, director, orchestrator | explicit full-cycle orchestration standard exists | GREEN |
| OMEGA | ARC-population/source/lifecycle steward under PRIME | registry and boundary explicit | GREEN |
| FACTORY | durable lifecycle/provenance register under PRIME | non-reasoning/non-orchestrating role explicit | GREEN |
| BRAIN STEWARD | Brain lifecycle/interconnect steward under PRIME | bounded and idle when no real Brain exists | GREEN |
| ARC instance | own bounded domain source/execution | NARC authoritative source isolated in own repo | GREEN |

No extra canonical tier has been introduced.

## Factory production layers

### Layer A — Founder intent / machine intake

- Founder-to-PRIME creation model: defined
- machine-readable creation request schema: defined
- explicit side-effect authorization fields: defined
- Telegram as control surface, not authority: defined

State: **GREEN at contract level / not yet live-trigger automated**.

### Layer B — source classification and repository

- source-boundary classes: defined
- one-authoritative-source rule: defined
- collision/dual-source rejection: defined
- repository creation belongs inside Factory cycle: defined
- automatic private repository creation: **not yet implemented in current runtime/tooling**

State: **YELLOW**.

### Layer C — deterministic source manufacture

- Factory birth manifest schema: defined
- reusable neutral Factory source template: defined
- minimum generated file tree: defined
- no customer-payload inheritance rule: defined
- invariant validator: implemented as zero-dependency Node script
- fully idempotent renderer/generator command: not yet implemented

State: **YELLOW/GREEN boundary**.

### Layer D — stewardship registration

- OMEGA registry: operational
- FACTORY lifecycle register: operational
- PRIME supervision mirror: operational
- handoff ledger rule: operational
- NARC registered pre-runtime: verified

State: **GREEN**.

### Layer E — runtime provisioning

Required mature Factory capability:

- create isolated runtime/service/profile;
- allocate state/log/secrets boundaries;
- assign model-capacity pool;
- configure health/restart/recovery;
- run isolation smoke tests;
- configure primary channel;
- fail closed for unknown/unbound identities;
- produce deployment checkpoint.

For NARC these are not yet done.

State: **RED for NARC F4 / target architecture defined**.

### Layer F — owner binding / onboarding

- explicit Narek Owner binding: pending
- primary channel: pending
- French-first first-contact contract: ready
- red/blue-pill one-time configuration: ready
- unverified domain remains blocked: correct

State: **RED/PENDING for F5**.

### Layer G — evidence / maturity

- maturity gate doctrine: aligned
- no inherited Cargo/VONDA maturity: correct
- no aura claimed: correct
- real NARC useful-work evidence: none yet
- runtime isolation/recovery evidence: none yet

State: **RED/PENDING for F6**, which is correct at this point.

## NARC truth audit

NARC currently satisfies:

- [x] Founder authorization
- [x] stable `arc_id = narc`
- [x] dedicated authoritative repository
- [x] repository class `customer_standalone_domain`
- [x] Factory manifest
- [x] instance record
- [x] source-boundary record
- [x] access/privacy policy
- [x] Brain registry initialized and empty
- [x] visual baseline/manifest
- [x] onboarding contract
- [x] commercial entitlement record
- [x] runtime boundary contract
- [x] bridge state
- [x] evidence register
- [x] OMEGA registration
- [x] FACTORY registration
- [x] PRIME mirror + orchestration ledger
- [x] French-first configuration
- [x] candidate domain kept explicitly unverified
- [x] maturity/aura kept unearned
- [ ] automatic repository creation provenance (manual gap recorded truthfully)
- [ ] isolated runtime
- [ ] model-capacity pool
- [ ] primary channel
- [ ] owner binding
- [ ] approved canonical visual asset
- [ ] verified production domain, only if needed
- [ ] live useful work cycle
- [ ] recovery/isolation evidence
- [ ] V1 evidence closeout

## Critical missing capabilities before calling Factory operationally state of the art

### P0 — privileged Factory automation

1. **PRIME-controlled repository creation service** using least-privilege GitHub App/service identity.
2. **Authorized Founder control-channel trigger**, including Telegram if selected, with audit proof and replay/idempotency protection.
3. **Idempotent ARC renderer/generator** from creation request → full source package.
4. **Transactional registration workflow** so OMEGA/FACTORY/PRIME/source either converge or fail with rollback/reconciliation state.
5. **Runtime provisioner** for isolated Hermes/service profile, state, secrets, logs and restart identity.
6. **Channel provision/binding workflow** with unknown-user fail-closed tests.
7. **Model-capacity allocator** with pool population/headroom rules and Standard entitlement telemetry.
8. **Recovery/rollback checkpoint automation** before and after material provisioning stages.

### P1 — production quality / scale

9. CI validation of Factory package invariants on every ARC source PR.
10. secret scanning and branch/ruleset policy for newly Factory-created repos.
11. deterministic Factory version + migration engine.
12. portfolio-level health/telemetry without merging client memory.
13. structured incident/reconciliation state if an inter-repo transaction partially fails.
14. signed/auditable production-event trail for privileged actions.
15. canary Factory template upgrades before fleet-wide migration.

## Transactional alignment requirement

A production cycle touches more than one source of operational truth. State-of-the-art handling must treat registration as a coordinated transaction, even if Git itself cannot provide a cross-repository atomic commit.

PRIME should therefore orchestrate a transaction ID across:

- Factory creation request;
- ARC source manifest;
- OMEGA registration;
- FACTORY lifecycle record;
- PRIME mirror;
- runtime provisioning checkpoint.

If one step fails, PRIME records `reconciliation_required` rather than silently leaving contradictory “complete” states.

This is a major requirement before large-scale ARC manufacture.

## Security / privacy requirements

Before automated Factory repo/runtime creation is enabled:

- repository creator uses least privilege;
- no customer secrets enter template or registry repos;
- customer repo is private by default;
- owner binding is explicit;
- control-channel commands are authenticated and replay-resistant;
- paid external side effects remain separately authorized;
- domain/DNS mutations remain blocked without explicit verified authority;
- cross-ARC private state stays forbidden;
- logs/telemetry remain privacy-safe.

## Definition of “state of the art” for this project

Do not use the phrase based on UI polish or quantity of automation. For RYZ3N ARC Factory, it means:

- one-command/one-intent Founder experience;
- PRIME-orchestrated delegated control;
- deterministic repeatable source manufacture;
- least-privilege privileged actions;
- policy-as-code and validation;
- idempotency and safe retry;
- transactional reconciliation across repositories/runtime;
- isolation by construction;
- evidence-derived lifecycle/maturity;
- observability, rollback and recovery;
- configuration-driven customization;
- no customer-data cloning;
- progressively lower Founder effort per ARC.

## Current conclusion

**Board alignment: GREEN.**

**NARC F0–F3: GREEN.**

**Factory source contract/template/validation: GREEN/YELLOW, v1 established but generator/CI not complete.**

**Factory privileged automation and NARC runtime F4–F6: NOT COMPLETE.**

This is the correct point to continue: do not redesign the hierarchy again; implement the missing privileged Factory/runtime automation against the now-stable contract and use NARC as the first replication-quality live proof.
