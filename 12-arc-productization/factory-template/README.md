# RYZ3N ARC Factory Template v1.3

Status: reusable source template for ARC Factory manufacture  
Orchestrator: PRIME  
Stewardship: OMEGA + FACTORY + BRAIN STEWARD under PRIME

## Purpose

This directory defines the reusable, customer-neutral source template from which PRIME-orchestrated ARC production can manufacture a new ARC package.

It is not an ARC instance and contains no customer-private data, credentials, maturity evidence or live owner binding.

## Production rule

> Build once. Instantiate many. Customize by configuration, not architectural fork.

The Factory should render customer/domain values into these contracts from a validated `ARC-FACTORY-CREATION-REQUEST-SCHEMA.json` input and then validate the generated package against the canonical schemas/gates.

Template v1.3 also makes three boundaries mandatory at birth instead of relying on later repair:

- hermetic isolation/autonomy contract;
- Founder-operator separation from the customer Owner/private namespace;
- Founder-authorized free-only model/provider cost boundary.

## Minimum generated package

```text
arc/
├── FACTORY-BIRTH-MANIFEST.json
├── <ARC>_INSTANCE.json
├── README.md
├── REPOSITORY-SOURCE-BOUNDARY.md
├── access-policy.json
├── BRAINS/
│   └── README.md
├── governance/
│   └── COMMERCIAL-ENTITLEMENT.md
├── visual/
│   ├── ARC-VISUAL-IDENTITY.md
│   └── visual-identity.json
├── onboarding/
│   └── FIRST-CONTACT.md
├── runtime/
│   └── README.md
├── bridge/
│   └── STATE.json
└── evidence/
    └── README.md
```

## Template values

The template must only accept values that originate from explicit Founder/authorized input, canonical tier rules, or verified infrastructure facts. Unverified values remain marked unverified.

Common placeholders:

- `{{arc_id}}`
- `{{display_name}}`
- `{{repository_class}}`
- `{{authoritative_repository}}`
- `{{owner_display_name}}`
- `{{owner_entity_class}}`
- `{{primary_language}}`
- `{{commercial_tier}}`
- `{{candidate_hostname}}`
- `{{candidate_hostname_verification}}`

## Forbidden inheritance

A generated ARC must never inherit from the previous ARC:

- owner identity bindings;
- private memory/content;
- secrets/credentials;
- customer documents;
- earned maturity/aura;
- channel identifiers/tokens;
- model-pool state unless explicitly assigned;
- visual asset as its canonical identity;
- customer-specific Brain payload.

Founder/operator maintenance authority must also never be implemented by impersonating the customer Owner or by inheriting the Owner-private namespace.

## Required validation

Before PRIME accepts F2 as complete:

1. creation request is schema-valid;
2. generated birth manifest is schema-valid;
3. required paths exist;
4. source boundary has exactly one authoritative repository;
5. no secret-bearing fields are present;
6. no unresolved template placeholders remain;
7. OMEGA registration pointers are valid or explicitly pending;
8. lifecycle state does not exceed evidence;
9. maturity/aura is unearned unless evidence says otherwise;
10. customer-specific facts marked unverified remain unverified;
11. hermetic seal contract is present and maturity-neutral;
12. Founder operator and Owner roles are separate and cross-private-state access is denied;
13. own-repository autonomous writes require bounded safe-writer integrity plumbing when granted;
14. model/provider routing is free-only unless the Founder explicitly authorizes a paid route;
15. deterministic model EOL/404/410 fails over to an eligible free route or fails closed rather than retry-storming.

Run the repository-level contract drift gate with:

```bash
node scripts/validate-arc-factory-contract.mjs
```

Generated ARC packages continue to use:

```bash
node scripts/validate-arc-factory-package.mjs <path-to-arc>
```

## Versioning

Current version: `factory-template-v1.3` / Factory contract `1.3`.

Every generated ARC records the template/Factory contract version in its birth manifest. Later template upgrades require explicit migration provenance; they do not silently rewrite existing ARCs.
