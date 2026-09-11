# RYZ3N ARC Factory Template v1

Status: reusable source template for ARC Factory manufacture
Orchestrator: PRIME
Stewardship: OMEGA + FACTORY + BRAIN STEWARD under PRIME

## Purpose

This directory defines the reusable, customer-neutral source template from which PRIME-orchestrated ARC production can manufacture a new ARC package.

It is not an ARC instance and contains no customer-private data, credentials, maturity evidence or live owner binding.

## Production rule

> Build once. Instantiate many. Customize by configuration, not architectural fork.

The Factory should render customer/domain values into these contracts from a validated `ARC-FACTORY-CREATION-REQUEST-SCHEMA.json` input and then validate the generated package against the canonical schemas/gates.

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
10. customer-specific facts marked unverified remain unverified.

## Versioning

Template version begins at `factory-template-v1.0`.

Every generated ARC records the template/Factory contract version in its birth manifest. Later template upgrades require explicit migration provenance; they do not silently rewrite existing ARCs.
