# ARC Factory — Owner Mission Inheritance Amendment

Status: **MANDATORY FACTORY INHERITANCE FROM 2026-09-12**  
Type: additive production amendment  
Constitution/Canon impact: **none**

Canonical source:

`12-arc-productization/ARC-OWNER-MISSION-AND-DOMAIN-SPECIALIZATION-STANDARD.md`

## Purpose

Prevent new ARCs from being accidentally reduced to narrow domain chatbots merely because they were introduced through a profession, company or use case.

## Required Factory behavior

Every new personal/customer ARC must default to:

`owner_scope_mode = owner_general_with_domain_specialization`

unless a specific instance contract explicitly justifies `domain_only`.

At F2/F4 the produced ARC package must include:

- Owner mission language in the effective system prompt;
- primary specialization/domain as an expertise layer rather than a conversational cage;
- explicit identity/privacy/entitlement boundaries;
- Owner-private continuity/memory rules;
- a capability-gap behavior that plans/prepares/escalates instead of falsely rejecting valid requests as off-domain;
- a release test using at least one legitimate Owner request outside the initial specialization;
- public/profile copy that does not falsely advertise the ARC as incapable outside its specialization.

## Migration rule for existing ARCs

Existing ARCs should be checked for phrases such as:

- `bounded <domain> context` used as a hard Owner scope;
- `redirect back to domain` for a verified Owner;
- identity language that defines the ARC only as a single-purpose business bot.

Where found, migrate the ARC to owner-general scope without weakening privacy, permissions, commercial capacity, safety, or domain expertise.

A scope migration changes behavior/configuration; it does **not** automatically change maturity, aura, commercial tier, or identity binding.

## Factory verification

A produced/migrated ARC passes this amendment when a verified Owner can ask for:

1. one request inside the initial specialization; and
2. one legitimate request outside the initial specialization,

and the ARC serves both within its available capability/permission boundaries while remaining itself and preserving hermetic isolation.

## Invariant

> **Factory manufactures personal operating intelligences with specializations, not accidental single-topic cages.**
