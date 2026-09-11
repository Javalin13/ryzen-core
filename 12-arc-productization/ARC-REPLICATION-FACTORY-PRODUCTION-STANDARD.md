# ARC Replication Factory Production Standard

```yaml
---
type: arc-replication-production-standard
status: founder-directed-active-prototype-standard
created: 2026-09-11
scope: repeatable ARC manufacture, birth manifests, replication quality, drift prevention
stewards:
  runtime-supervisor: PRIME
  arc-population: OMEGA
  lifecycle-register: FACTORY
  brain-population: BRAIN-STEWARD
---
```

## Founder direction

RYZ3N ARC creation must evolve from bespoke hand-built prototypes into a **state-of-the-art replication Factory**.

The objective is not to clone customer payload. The objective is to manufacture every new ARC from the same validated production contract while injecting only authorized domain/owner configuration.

Core principle:

> **Build once. Instantiate many. Customize by configuration, not architectural fork.**

The canonical ontology remains unchanged:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

FACTORY is a production/lifecycle registry, OMEGA is ARC-population stewardship, PRIME is current prototype supervision, and BRAIN STEWARD governs Brain lifecycle. None becomes a new canonical tier.

## Production target

A Standard ARC should converge toward:

- **80–90% universal platform/runtime contract**;
- **10–20% owner/domain configuration**;
- one authoritative source boundary;
- one stable ARC identity;
- one repeatable birth manifest;
- one standard isolation/security contract;
- one standard lifecycle/evidence contract;
- one standard commercial-capacity envelope;
- one standard visual-family contract;
- one standard first-run/onboarding shell with customer-specific configuration;
- one versioned Factory provenance trail.

Every new ARC must make ARC #N cheaper, faster and less error-prone than ARC #N-1 without weakening privacy, isolation, truthful maturity or owner control.

## Golden rule: replication is not cloning

Factory replication may copy/reuse:

- schemas;
- directory contracts;
- runtime adapters;
- policy templates;
- health/isolation checks;
- registration structures;
- capability contracts;
- onboarding flow mechanics;
- telemetry interfaces;
- visual-family rules;
- evidence-gate structure.

Factory replication must **not** copy:

- another customer's private memory;
- another owner's identity bindings;
- secrets or credentials;
- customer-specific prompts/documents;
- another ARC's domain competence as if already earned;
- another ARC's maturity evidence;
- another ARC's visual form as the new ARC's identity;
- another ARC's channel identifiers or runtime secrets.

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
10. visual-family/form baseline;
11. Brain registry pointer;
12. onboarding contract pointer;
13. OMEGA/FACTORY/PRIME pointers;
14. maturity target and truthful evidence state;
15. provenance/template source;
16. per-ARC configuration values versus universal inherited contracts;
17. production-stage checklist;
18. latest checkpoint/evidence pointer.

Schema:
`12-arc-productization/ARC-FACTORY-BIRTH-MANIFEST-SCHEMA.json`

## Production stages

Factory production is a staged pipeline, not one giant script:

### F0 — Authorization

- Founder/authorized creation intent exists.
- `arc_id` reserved.
- intended owner/domain class recorded.

### F1 — Source boundary

- repository class chosen;
- one authoritative repository designated;
- bounded `arc/` source initialized;
- dual-active source rejected.

### F2 — Instance package

- ARC instance record;
- Factory birth manifest;
- access/privacy policy;
- Brain registry;
- commercial entitlement;
- visual identity record + machine manifest;
- onboarding/first-contact contract;
- runtime boundary;
- bridge/evidence scaffolding.

### F3 — Stewardship registration

- OMEGA active registration;
- FACTORY active-instance entry;
- PRIME supervision mirror;
- Factory provenance/version recorded.

Registration does **not** mean runtime activation.

### F4 — Runtime provisioning

- isolated runtime/service identity;
- secrets outside Git;
- capacity pool assignment;
- primary channel binding;
- health/restart/recovery controls;
- tenant namespace isolation;
- unknown identity fail-closed;
- privacy-safe telemetry.

### F5 — Owner binding and first-run

- explicit owner identity binding;
- owner-facing first-run experience;
- ARC identity/no-PRIME-leak verification;
- commercial entitlement visible/true;
- real useful work cycle.

### F6 — Evidence closeout

- isolation/privacy evidence;
- persistence/recovery evidence;
- useful work evidence;
- maturity gate evaluation;
- truthful lifecycle status.

Only evidence can promote maturity/aura.

## Replication quality gates

A Factory-produced ARC is not production-quality unless it passes all relevant gates:

- **Identity gate:** no identity collision or inherited customer identifiers.
- **Source gate:** exactly one authoritative source boundary.
- **Privacy gate:** no copied private payload or secrets.
- **Isolation gate:** independent state, secrets, logs and restart boundary.
- **Capacity gate:** entitlement/pool assignment explicit and enforceable.
- **Channel gate:** unique approved binding, unknown users fail closed.
- **Recovery gate:** known-good source/checkpoint and restart path.
- **Drift gate:** generated package conforms to Factory manifest/schema.
- **Visual gate:** same RYZ3N family, unique ARC form, no maturity-by-artwork.
- **Maturity gate:** no inherited evidence or aura.
- **Stewardship gate:** OMEGA + FACTORY + PRIME pointers agree.

Any contradiction blocks activation and is escalated to OMEGA/PRIME.

## Configuration versus architecture

Per-ARC configuration may include:

- owner/customer identity;
- business/domain context;
- primary/secondary language;
- chosen channel;
- approved integrations;
- commercial tier;
- onboarding copy/easter eggs;
- visual-form candidate metadata;
- domain-specific competence and workflows;
- verified website/domain pointers.

It must not require forking the universal ARC architecture unless a validated product requirement proves a reusable contract change is necessary.

When a new ARC reveals a generally useful improvement, promote that improvement back into the Factory standard/template rather than leaving a one-off patch.

## Factory provenance

Every ARC must declare which Factory contract/template version produced its birth package.

A later Factory upgrade does not silently rewrite all existing ARCs. Upgrades use explicit versioned migrations with:

- source version;
- destination version;
- affected contracts;
- compatibility decision;
- rollback/checkpoint;
- evidence that owner data/permissions were preserved.

## State-of-the-art target capabilities

The Factory roadmap should converge toward:

- schema-validated ARC manifests;
- idempotent birth/provision commands;
- deterministic directory/package generation;
- policy-as-code validation;
- source-boundary collision detection;
- secret scanning and zero-secret templates;
- automated namespace uniqueness checks;
- runtime health/restart tests;
- isolation smoke tests;
- entitlement/capacity policy validation;
- generated OMEGA/FACTORY/PRIME registration patches;
- versioned template migrations;
- canary rollout/rollback;
- privacy-safe fleet telemetry;
- Factory quality report per ARC;
- human approval gates where Founder/Owner intent is inherently required.

Automation must remain bounded: no script may infer owner consent, fabricate domain ownership, buy provider capacity, claim maturity, or bypass explicit identity binding.

## NARC production role

NARC (`Javalin13/NARC-ARC`) is the first ARC deliberately manufactured as a **Factory replication candidate** under this standard.

NARC must therefore:

- use the Factory birth manifest;
- preserve its own customer/domain source boundary;
- use French-first owner configuration;
- keep unverified domain data explicitly unverified;
- keep its one-time red/blue-pill onboarding joke as configuration, not architecture;
- generate reusable production lessons without leaking Narek-specific payload into the universal template.

Cargo and VONDA remain valuable engineering references. NARC is the transition point from reference-copying toward versioned Factory manufacture.

## Relationship to the existing provisioning backlog

This standard does not authorize reckless one-click deployment before safety evidence exists. It authorizes building the **replication contract now** and automating proven or safety-critical parts incrementally.

The correct sequence is:

`standardize → validate → replicate → measure → automate → continuously harden`

—not:

`copy → mutate → hope`.

## Success criteria

Factory quality is improving when:

- creation time falls ARC by ARC;
- customer-specific code decreases;
- isolation defects do not increase;
- new ARC birth artifacts are complete by construction;
- OMEGA/FACTORY/PRIME never disagree on ARC identity/source state;
- reusable fixes are promoted upstream;
- owner/domain customization stays declarative;
- maturity remains evidence-derived;
- ARC #10 is materially easier and safer to create than ARC #3.
