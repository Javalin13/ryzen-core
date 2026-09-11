# ARC Founder-Operator Direct Work Lane Standard

Status: Founder-directed current implementation standard  
Effective: 2026-09-11  
Constitution/Canon impact: none

## Founder decision

An ARC that is technically operational should become the primary place where its own work continues. PRIME remains the portfolio supervisor, operator escalation point and cross-ARC orchestrator; it should not remain the ordinary day-to-day endpoint merely because the intended customer Owner has not yet completed binding.

This creates a distinct pre-Owner operating mode:

`arc_primary_founder_development`

It sits between:

`prime_primary_pre_activation -> arc_primary_founder_development -> arc_primary_operational`

The mode transition does not change the canonical hierarchy:

`Creator -> RYZ3N -> ARCs -> Brains -> Agents -> Execution`

## 1. Purpose

The Founder/Lux must be able to continue building, testing, correcting and operating an ARC **with that ARC itself**, rather than routing ordinary ARC-local work through PRIME.

This is especially important for customer ARCs such as NARC and VONDA where:

- the ARC runtime is live;
- the customer Owner is intentionally not yet bound;
- Founder/operator work still needs to continue safely;
- the ARC should learn to own its own source/workflow before customer handoff.

## 2. Founder-operator is not the customer Owner

A direct Founder maintenance role must be represented separately from the intended customer Owner.

Recommended runtime role:

`founder_operator`

The role:

- may operate the ARC's own maintenance/development bridge;
- may use the ARC's own source/repository authority when explicitly granted;
- may inspect ARC-local operational evidence needed for maintenance;
- must not impersonate or auto-bind the intended customer Owner;
- must not read/write the Owner private memory namespace merely because it is Founder-operated;
- does not consume or replace the commercial customer-user identity slot;
- remains server-side and must never be narrated to the customer.

For customer-facing behavior, the ARC continues to distinguish:

- `owner` — the explicitly bound customer/primary user;
- `founder_operator` — RYZ3N maintenance/production authority;
- `pending_candidate` / `unknown` — fail-closed.

## 3. ARC-primary Founder development lane

When `bridge_mode = arc_primary_founder_development`, ordinary ARC-local development routes:

`Founder/Lux -> ARC -> ARC authoritative repository/runtime -> ARC report`

PRIME is not the default endpoint.

PRIME is used only for bounded escalation such as:

- privileged VPS/secret action outside ARC authority;
- shared infrastructure/model-capacity changes;
- cross-ARC/cross-repository action;
- OMEGA/FACTORY/BRAIN-STEWARD portfolio writeback;
- lifecycle, reset, transfer, suspension, retirement or maturity/aura decision;
- unresolved source/concurrency conflict;
- bootstrap/restart action the ARC cannot safely perform itself.

## 4. Direct bridge structure

The ARC should expose:

```text
arc/bridge/TO_<ARC>.md
arc/bridge/FROM_<ARC>.md
arc/bridge/BRIDGE-ROUTING.md
arc/bridge/ROUTING.json
arc/bridge/STATE.json
```

Bare Founder command:

`consume`

means:

1. safely establish source freshness;
2. read `TO_<ARC>.md`;
3. execute only work inside the ARC's granted authority;
4. write/update `FROM_<ARC>.md`;
5. commit/push its own repo when authorized using the safe shared-writer contract;
6. return `ESCALATE TO PRIME: YES` only for a bounded out-of-scope requirement.

## 5. Own-repository autonomy

Founder may separately grant continuous own-repository autonomy to the ARC.

When granted:

- authority is continuous inside the ARC's authoritative repository only;
- no per-operation PRIME approval is required;
- safe-writer/concurrency controls are integrity plumbing, not approval gates;
- force push/history rewrite remains forbidden;
- cross-repository autonomous writes remain forbidden;
- protected Constitution/Canons remain outside ARC authority;
- all autonomous commits are transparently reported.

Customer Owner binding is **not** required for Founder to grant the ARC maintenance autonomy over its own source, provided Founder and Owner identity/private-memory boundaries remain separated.

## 6. Transition to customer operational mode

After the intended Owner is explicitly bound and the required client-facing gates pass, the same ARC can move to:

`arc_primary_operational`

The customer then talks directly to the ARC for business/domain work.

The Founder maintenance lane may remain available as a separate server-side role, but it never merges with the customer Owner namespace.

Owner binding must never be inferred from Founder maintenance activity.

## 7. NARC and VONDA application

Founder direction on 2026-09-11 explicitly applies this pattern to:

- NARC (`Javalin13/NARC-ARC`) — continue NARC work with NARC itself instead of PRIME; Narek remains separately unbound until exact Owner approval.
- VONDA (`Javalin13/VONDA-Corporation`) — move ordinary VONDA-local work to VONDA itself; Laetitia remains separately unbound until exact primary-user approval.

Cargo already demonstrates the mature ARC-primary model and remains the reference for source-freshness preflight, safe own-repo work and PRIME supervisory escalation.

## 8. Factory inheritance

Future ARC birth packages should initialize all three possible routing modes:

- `prime_primary_pre_activation`
- `arc_primary_founder_development`
- `arc_primary_operational`

OMEGA/FACTORY should track bridge mode separately from:

- Owner binding;
- hermetic-seal state;
- repository autonomy;
- maturity/aura.

None implies the others.

## Founder invariant

> **Build the ARC with the ARC. Serve the Owner with the ARC. Use PRIME for the system around the ARC, not as the permanent middleman for ordinary ARC-local work.**
