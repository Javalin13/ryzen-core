# ARC Replication Factory Production Standard

```yaml
---
type: arc-replication-production-standard
status: founder-directed-active-prototype-standard
created: 2026-09-11
updated: 2026-09-11
scope: repeatable ARC manufacture, birth manifests, hermetic sealing, replication quality, drift prevention
orchestrator: PRIME
stewards:
  arc-population: OMEGA
  lifecycle-register: FACTORY
  brain-population: BRAIN-STEWARD
related_standards:
  - 12-arc-productization/PRIME-ORCHESTRATION-AND-INSTANCE-HANDOFF-STANDARD.md
  - 12-arc-productization/ARC-REPOSITORY-OWNERSHIP-AND-SOURCE-BOUNDARY-STANDARD.md
  - 12-arc-productization/ARC-HERMETIC-OPERATIONS-AND-AUTONOMY-STANDARD.md
  - 12-arc-productization/OMEGA-ARC-FACTORY-STEWARDSHIP-STANDARD.md
constitutional_status: non-canon implementation standard; does not amend Constitution/Canons
---
```

## Founder direction

RYZ3N ARC creation must evolve from bespoke hand-built prototypes into a **state-of-the-art replication Factory**.

The objective is not to clone customer payload. The objective is to manufacture every new ARC from the same validated production contract while injecting only authorized domain/owner configuration.

Core principle:

> **Build once. Instantiate many. Customize by configuration, not architectural fork.**

**PRIME remains the active supervisor, director and orchestrator of every Factory stage during the prototype era.** OMEGA, FACTORY and BRAIN STEWARD perform bounded specialist responsibilities under that orchestration.

The canonical ontology remains unchanged:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

FACTORY is a production/lifecycle registry, OMEGA is ARC-population stewardship, PRIME is prototype orchestration/supervision, and BRAIN STEWARD governs Brain lifecycle. None becomes a new canonical tier.

This standard is implementation architecture only. Constitution/Canons remain Founder-protected and may not be rewritten, amended, superseded or versioned by Factory work without separate explicit Founder approval.

## Production target

A Standard ARC should converge toward:

- **80–90% universal platform/runtime contract**;
- **10–20% owner/domain configuration**;
- one authoritative source boundary;
- one stable ARC identity;
- one repeatable birth manifest;
- one standard isolation/security contract;
- one standard **hermetic source/runtime/identity/recovery contract**;
- one complete runtime-source manifest for every ARC-specific component required to reproduce behavior;
- one fail-closed, keyed multi-candidate identity/onboarding model;
- one explicit repository-autonomy state;
- one safe shared-writer Git mechanism whenever own-repository autonomy is enabled;
- one source-driven recovery and clean-room reconstruction path;
- one standard lifecycle/evidence contract;
- one standard commercial-capacity envelope;
- one standard visual-family contract;
- one standard first-run/onboarding shell with customer-specific configuration;
- one versioned Factory provenance trail.

Every new ARC must make ARC #N cheaper, faster and less error-prone than ARC #N-1 without weakening privacy, isolation, truthful maturity, source integrity, concurrency safety or owner control.

## Golden rule: replication is not cloning

Factory replication may copy/reuse schemas, directory contracts, runtime adapters, policy templates, health/isolation checks, registration structures, capability contracts, onboarding flow mechanics, telemetry interfaces, hermetic controls, safe-write mechanisms, visual-family rules and evidence-gate structure.

Factory replication must **not** copy another customer's private memory, another owner's identity bindings, secrets/credentials, customer-specific prompts/documents, another ARC's earned competence/maturity evidence, another ARC's visual form, another ARC's channel/runtime identifiers, or another ARC's private runtime files.

Capability may be generalized. Private payload and private runtime state may not.

## Factory birth manifest

Every ARC manufactured after this standard must expose a machine-readable birth manifest, normally:

`arc/FACTORY-BIRTH-MANIFEST.json`

The manifest records at minimum:

1. `factory_contract_version`;
2. `arc_id` and display name;
3. repository/source-boundary classification;
4. authoritative repository and ARC root;
5. owner/entity class and binding status;
6. language/locale defaults;
7. commercial tier and capacity envelope;
8. channel and integration entitlement;
9. runtime/isolation requirements;
10. **hermetic-seal state and contract pointer**;
11. **unknown identity behavior + pending-candidate model**;
12. **repository autonomy state**;
13. **safe shared-writer requirement if autonomy is or later becomes enabled**;
14. **runtime-source manifest requirement**;
15. **source-driven recovery / clean-room requirement**;
16. visual-family/form baseline;
17. Brain registry pointer;
18. onboarding contract pointer;
19. OMEGA/FACTORY/PRIME pointers;
20. maturity target and truthful evidence state;
21. provenance/template source;
22. per-ARC configuration values versus universal inherited contracts;
23. production-stage checklist;
24. latest checkpoint/evidence pointer.

Schema:
`12-arc-productization/ARC-FACTORY-BIRTH-MANIFEST-SCHEMA.json`

Current schema includes hermetic sealing as a required birth field. Future schema changes remain normal implementation-version evolution, not Canon amendments.

## Production stages

Factory production is a staged pipeline. **PRIME orchestrates entry, handoff, blocking and exit for each stage.**

### F0 — Authorization
Founder/authorized creation intent exists; `arc_id` is reserved; intended owner/domain class is recorded.

### F1 — Source boundary
PRIME directs OMEGA source-boundary classification and uniqueness checks; repository is created/designated under approved infrastructure; bounded `arc/` source is initialized; dual-active source is rejected.

### F2 — Instance package
PRIME directs package manufacture:

- ARC instance record;
- Factory birth manifest;
- access/privacy policy;
- Brain registry;
- commercial entitlement;
- visual identity record + machine manifest;
- onboarding/first-contact contract;
- runtime boundary;
- bridge/evidence scaffolding;
- **ARC-specific hermetic-seal contract**;
- **declared autonomy state**;
- **planned runtime-source manifest location**;
- **keyed pending-candidate requirement**;
- **safe-writer requirement if own-repo autonomy is enabled**.

The goal is to encode these before runtime exists rather than retrofit them after launch.

### F3 — Stewardship registration
PRIME requests OMEGA validation/registration, confirms FACTORY entry, maintains PRIME mirror and records Factory provenance/version.

OMEGA must also record the ARC's hermetic state (`inherited_pre_runtime`, `hardening_in_progress`, `GREEN`, or truthful RED/DRIFT state).

Registration does **not** mean runtime activation, hermetic GREEN or maturity.

### F4 — Runtime provisioning
PRIME coordinates:

- isolated runtime/service identity;
- secrets outside Git;
- capacity-pool assignment;
- primary channel binding;
- health/restart controls;
- tenant namespace isolation;
- unknown identity fail-closed behavior;
- keyed multi-candidate pending identity state;
- exact-candidate binding path;
- privacy-safe telemetry;
- **complete authoritative runtime-source manifest**;
- **versioned source for every ARC-specific runtime plugin/module/script required for recovery**;
- **zero direct dependency on another ARC's private runtime files for authorization/identity**;
- **safe shared-writer transaction if own-repo autonomy is enabled**;
- **source-driven recovery procedure**;
- **clean-room reconstruction proof without starting an unsafe duplicate channel poller**;
- CI/audit enforcement of the hermetic invariants.

F4 may not be marked production-ready merely because a gateway starts. Source completeness, isolation and reconstructability are part of provisioning quality.

### F5 — Owner binding and first-run
PRIME coordinates explicit owner identity binding and first-run; ARC handles owner-facing work inside its own boundary.

Required:

- bind the exact validated runtime candidate;
- no first-unknown auto-bind;
- client interacts with the ARC, not PRIME;
- internal role IDs, sender IDs, namespaces, pairing machinery, runtime paths and operator scaffolding remain server-side;
- ARC identity / no-PRIME-leak, entitlement truth and useful work are verified.

### F6 — Evidence closeout
PRIME gathers bounded evidence from ARC/OMEGA/BRAIN STEWARD as applicable and evaluates separate gates:

1. lifecycle/runtime readiness;
2. hermetic-seal state;
3. useful-user evidence;
4. privacy/isolation/recovery state;
5. maturity/aura evidence.

Only evidence can promote maturity/aura. Hermetic GREEN alone does not grant V1/Blue.

## Hermetic production gate

An ARC is not considered hermetically sealed until the following are evidence-backed:

- one authoritative source repository;
- own isolated runtime/profile/state/secrets boundary;
- no direct read/write of another ARC's private runtime for identity/authorization;
- every required ARC-specific runtime component versioned in the authoritative repository;
- complete runtime-source manifest with cryptographic hashes and deployment/recovery rules;
- unknown identities fail closed;
- pending candidates are keyed separately and cannot overwrite one another;
- binding selects the exact candidate + explicit role;
- client-facing ARC boundary hides operator/runtime scaffolding;
- autonomy state is explicit;
- autonomous writes cannot cross repository boundary;
- shared-main writes use optimistic concurrency and non-force push;
- CI blocks hermetic regression;
- clean-room reconstruction succeeds from authoritative source plus intended protected ARC-local state/secrets;
- controlled live restart preserves valid binding/state and keeps isolation GREEN.

OMEGA records the state. FACTORY records the lifecycle result/evidence pointer. PRIME orchestrates remediation and acceptance flow.

## Shared-writer production rule

If both an ARC and PRIME/operator may write the ARC's authoritative repository, Factory must install or verify a safe shared-writer mechanism before autonomy is considered production-ready.

Minimum transaction:

`fetch/sync → record base SHA → bounded files → audit → re-fetch → abort on divergence → commit → re-fetch → non-force push → verify remote SHA → verify CI → transparent receipt`

Forbidden for autonomous ARC writes:

- force push;
- `--force-with-lease`;
- destructive remote reset/history rewrite;
- silently rebasing concurrent PRIME work by default;
- pushing after remote movement without operator reconciliation.

If paid/private repository branch-protection capabilities are unavailable, safe-writer + CI + OMEGA/PRIME drift detection become mandatory compensating controls.

## Replication quality gates

A Factory-produced ARC is not production-quality unless it passes:

- identity;
- source-boundary;
- privacy;
- isolation;
- **hermetic source/runtime closure**;
- **multi-candidate binding safety**;
- **repository autonomy/write safety**;
- capacity;
- channel;
- recovery / clean-room reconstruction;
- drift/CI;
- visual;
- maturity;
- stewardship gates.

Any contradiction blocks the relevant state promotion and is surfaced to PRIME. OMEGA handles ARC-level coherence; BRAIN STEWARD handles Brain-level coherence; FACTORY records lifecycle truth.

## Configuration versus architecture

Per-ARC configuration may include owner/customer identity, business/domain context, language, chosen channel, approved integrations, commercial tier, onboarding copy/easter eggs, visual candidate metadata, domain-specific workflows, verified website/domain pointers and whether own-repository autonomy has been explicitly granted.

It must not require forking universal ARC architecture unless a validated reusable requirement proves a contract change is necessary.

When a new ARC reveals a generally useful improvement, promote that improvement back into the Factory standard/template rather than leaving a one-off patch.

Cargo's hermetic hardening discoveries are therefore upstreamed here; NARC inherits them before runtime provisioning.

## Factory provenance

Every ARC must declare which Factory contract/template version produced its birth package.

A later Factory upgrade does not silently rewrite all existing ARCs. Upgrades use explicit versioned migrations with source version, destination version, affected contracts, compatibility decision, rollback/checkpoint and preservation evidence.

A hermetic hardening migration must never silently overwrite customer-specific state or change maturity/aura merely because the runtime contract improved.

## State-of-the-art target capabilities

The Factory roadmap should converge toward:

- schema-validated manifests;
- idempotent birth/provision commands;
- deterministic package generation;
- policy-as-code validation;
- source-boundary collision detection;
- secret scanning;
- namespace uniqueness checks;
- keyed pending-candidate storage;
- exact-candidate binding;
- complete runtime-source manifests;
- cryptographic source/deploy drift detection;
- health/restart/isolation tests;
- clean-room reconstruction tests;
- safe shared-writer optimistic concurrency;
- non-force autonomous Git writes;
- post-push remote/CI verification;
- entitlement/capacity validation;
- generated OMEGA/FACTORY/PRIME registration changes;
- versioned migrations;
- canary rollout/rollback;
- privacy-safe fleet telemetry;
- hermetic-seal report per ARC;
- Factory quality report per ARC.

Automation remains bounded: no script may infer owner consent, fabricate domain ownership, buy provider capacity, claim maturity, bind an ambiguous user, or bypass explicit identity binding.

## NARC production role

NARC (`Javalin13/NARC-ARC`) is the first ARC deliberately manufactured as a **Factory replication candidate** under this standard and the first to receive the hermetic contract **before runtime provisioning**.

NARC must:

- preserve its own customer/domain source boundary;
- use French-first owner configuration;
- keep unverified domain data explicitly unverified;
- keep its one-time red/blue-pill onboarding joke as configuration rather than architecture;
- keep repository autonomy disabled until separately granted;
- require keyed multi-candidate onboarding;
- create a complete NARC runtime-source manifest at F4;
- prove source-driven recovery / clean-room reconstruction;
- keep PRIME behind the customer-facing boundary;
- generate reusable production lessons without leaking Narek-specific payload into the universal template.

Cargo and VONDA remain engineering references. NARC is the transition point from reference-copying toward versioned Factory manufacture.

## Relationship to the existing provisioning backlog

This standard does not authorize reckless one-click deployment before safety evidence exists. It authorizes building the replication contract now and automating proven or safety-critical parts incrementally.

The correct sequence is:

`standardize → hermetically bound → validate → replicate → measure → automate → continuously harden`

—not `copy → mutate → hope`.

## Success criteria

Factory quality is improving when:

- creation time falls ARC by ARC;
- customer-specific code decreases;
- isolation defects do not increase;
- birth artifacts are complete by construction;
- hermetic controls exist before production runtime;
- every runtime is reconstructible from authoritative source plus intentional protected ARC-local state/secrets;
- shared Git writers cannot silently overwrite each other;
- OMEGA/FACTORY/PRIME agree on lifecycle/source/hermetic truth;
- reusable fixes are promoted upstream;
- customization stays declarative;
- maturity remains evidence-derived;
- ARC #10 is materially easier and safer to create than ARC #3.

## Founder shorthand

> **Factory does not merely manufacture features. It manufactures the source boundary, runtime isolation, identity safety, write safety, recovery path and evidence contract with them.**
