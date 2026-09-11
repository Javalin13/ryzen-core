# ARC Repository Ownership & Source-Boundary Standard

```yaml
---
type: arc-repository-source-boundary-standard
status: founder-directed-current-model
created: 2026-09-11
classification: approved-architecture + repository-governance
scope: ARC source ownership, repository placement, Factory birth classification, product-vs-customer boundaries
related:
  - 12-arc-productization/OMEGA-ARC-FACTORY-STEWARDSHIP-STANDARD.md
  - 12-arc-productization/ARC-A2Z-ALIGNMENT-MAP-2026-09-10.md
  - 12-arc-productization/ARC-VISUAL-IDENTITY-HUMANOID-FAMILY-STANDARD.md
---
```

## Founder decision

Every ARC must have one authoritative source boundary, but **one ARC does not automatically require one standalone GitHub repository**.

The correct repository is the repository that owns the domain/product/customer truth the ARC serves.

Canonical rule:

> **The ARC lives with its authoritative domain truth. RYZ3N owns the universal architecture. PRIME/OMEGA/FACTORY keep bounded pointers and lifecycle metadata.**

There is **no separate Horizon architecture, Horizon Core, Horizon orchestration layer or Horizon authority tier**. Any earlier use of `Horizon` as a conceptual platform/orchestration name is superseded. The canonical platform is **RYZ3N**.

The canonical ontology remains:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

## Repository class A — RYZ3N-owned product/domain ARC

When RYZ3N owns and develops the underlying product/domain repository, that repository is the natural authoritative home for the ARC serving it.

Examples:

- `Javalin13/CargoConnect` → `Cargo ARC` under `arc/`;
- `Javalin13/FleetConnect` → future `Fleet ARC` under `arc/`.

Why:

- product implementation and domain truth already live there;
- the ARC can reason against the current product/business/governance state without a second synchronization layer;
- product-specific ARC evidence and configuration remain beside the system they serve;
- RYZ3N Core stays free of product-private payload;
- PRIME does not become a duplicate source repository.

A second standalone `Cargo-ARC` or `Fleet-ARC` repository should not be created merely because the ARC exists.

## Repository class B — customer / standalone domain ARC

When the ARC serves an external customer, standalone organization, personal business or domain that does not already have an appropriate authoritative repository, create or designate a dedicated private customer/domain repository.

Examples:

- `Javalin13/VONDA-Corporation` → `VONDA ARC` under `arc/`;
- future Narek fitness/coaching domain repo → `NARC` under `arc/`;
- future KMS7 customer/domain repo → KMS7 ARC under `arc/`, if/when Founder authorizes creation.

The repository should represent the **customer/domain boundary**, not merely the robot name, unless the ARC itself is the domain/product.

Example preferred shape:

```text
<Customer-or-Domain-Repo>/
├── arc/
│   ├── <ARC instance / identity / access / visual / bridge / Brains>
├── website/ or app/              # where applicable
├── operations/                   # where applicable
├── integrations/                 # where applicable
└── domain/customer documentation # bounded and authorized
```

If a customer already has a suitable authoritative repository, Factory should use that repository instead of creating a redundant new one.

## RYZ3N Core boundary

`Javalin13/ryzen-core` owns **universal reusable architecture only**, including:

- ARC canon and hierarchy;
- schemas and contracts;
- maturity/aura model;
- Factory/OMEGA rules;
- Brain/Agent lifecycle standards;
- security/governance principles;
- provisioning patterns;
- reusable productization/commercial rules;
- cross-ARC interoperability standards.

RYZ3N Core must **not** become the home for individual customer/domain ARC payload, private memory, credentials, customer documents or product-specific operational truth.

A domain ARC may reference RYZ3N Core canon, but should not clone universal doctrine locally unless a bounded implementation contract genuinely requires an ARC-side artifact.

## PRIME / OMEGA / FACTORY boundary

PRIME is the current prototype operator/supervisor, not the owning source repository for each ARC.

OMEGA and FACTORY maintain bounded discovery/lifecycle metadata:

- stable `arc_id`;
- repository classification (`ryz3n_owned_product_domain` or `customer_standalone_domain`);
- owning repository;
- ARC root path;
- source-of-truth pointer;
- Owner/entity class;
- lifecycle/runtime/maturity/form state;
- evidence/checkpoint pointers;
- transfer/reset history;
- safe visual identity pointers;
- Brain registry pointer.

They do not duplicate unrestricted ARC payload.

PRIME keeps a bounded supervision mirror under `ARCS/<ARC-ID>/` and resolves detailed truth back to the owning ARC repository.

## Runtime boundary

Repository placement and runtime isolation are separate concerns.

An ARC may live under the product/customer repository while its runtime remains isolated, for example:

```text
GitHub source:
Javalin13/CargoConnect/arc/

Runtime:
~/.hermes/profiles/cargo/
```

Do not create a separate GitHub repository merely to achieve runtime isolation. Runtime state/secrets remain outside Git according to the established security model.

## Factory birth classification

Before OMEGA registration/FACTORY activation, Factory must classify the ARC source boundary:

1. **Does an authoritative domain/product/customer repository already exist?**
   - yes → place the ARC there under the bounded ARC package/path;
   - no → continue.
2. **Is this a RYZ3N-owned product being developed as its own repository?**
   - yes → create/use the product repository, then place its ARC there;
   - no → continue.
3. **Is this a customer/standalone domain ARC?**
   - yes → create/designate one private customer/domain repository;
   - no → escalate only if the domain boundary is genuinely ambiguous.

Then register:

`authorized creation → classify owning domain/source boundary → designate/create authoritative repository → initialize ARC package → reserve arc_id → OMEGA registration → FACTORY entry → PRIME mirror → runtime/isolation/evidence`

The source-boundary decision must be recorded in the ARC instance record and FACTORY.

## Source-boundary invariants

- one active authoritative repository/source boundary per ARC;
- no dual active source-of-truth repositories for the same ARC;
- RYZ3N Core owns reusable canon, not customer/product instance payload;
- PRIME is a supervision/control plane, not the detailed domain source;
- runtime secrets/state stay outside Git;
- a product ARC stays with its product repository unless a deliberate future migration is authorized;
- a customer ARC stays inside its customer/domain boundary and must not leak into unrelated ARCs;
- reuse capability/patterns, never another Owner's private payload;
- repository transfer/migration must preserve history and update OMEGA/FACTORY pointers atomically;
- repository naming is secondary to the domain boundary; source ownership is primary.

## Current mappings

| ARC | Class | Authoritative repository | ARC location | State |
|---|---|---|---|---|
| VONDA ARC | customer/standalone domain | `Javalin13/VONDA-Corporation` | `arc/` | active reference ARC |
| Cargo ARC | RYZ3N-owned product/domain | `Javalin13/CargoConnect` | `arc/` | active runtime / binding phase |
| Fleet ARC | RYZ3N-owned product/domain | `Javalin13/FleetConnect` | future `arc/` | not yet instantiated |
| NARC | customer/standalone domain | dedicated Narek/customer-domain repo to be created/designated at birth | future `arc/` | authorized queue / not yet instantiated |

## No-Horizon invariant

The RYZ3N ecosystem has one canonical platform identity: **RYZ3N**.

Do not introduce `Horizon`, `Horizon Core`, or any equivalent parallel platform as an orchestration layer between RYZ3N and ARCs.

If legacy product files contain historical `Horizon` branding/text, that does not create architectural authority. New architecture, Factory decisions, ARC creation, supervision and documentation must use **RYZ3N** only.

## Founder shorthand

> **RYZ3N defines the system. The domain repository owns the ARC. PRIME supervises. OMEGA keeps the portfolio coherent. FACTORY remembers where every ARC belongs and what happened to it.**
