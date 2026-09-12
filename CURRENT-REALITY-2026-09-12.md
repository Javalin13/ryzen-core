# RYZ3N Core — Current Reality Overlay (2026-09-12)

```yaml
---
type: current-reality-overlay
status: active-reference
created: 2026-09-12
supersedes_for_current-reading: CURRENT-REALITY-2026-09.md
classification: reality + active-execution + architecture-convergence
historical_docs_preserved: true
---
```

## Purpose

This overlay records the current cross-repository state after the 2026-09-11 ARC build cycle and the 2026-09-12 free-only model/runtime repair work. It does not delete the 2026-09 monthly overlay; it supersedes that file only where later verified facts differ.

Canonical ecosystem remains:

```text
Creator → RYZ3N → ARCs → Brains → Agents → Execution
```

Current prototype control plane remains:

```text
Founder / Owner
  ↓
PRIME — supervisor / director / orchestrator
  ├── OMEGA — ARC population/lifecycle steward
  ├── BRAIN STEWARD — Brain lifecycle/interconnection steward
  └── FACTORY — durable ARC creation/lifecycle provenance register
        ↓
ARC runtime instance
```

OMEGA is not an ARC. FACTORY is not a Brain. PRIME is not inserted into the canonical ontology.

## 2026-09-12 convergence decisions

### ARC Factory contract

Factory schema/template have converged on **v1.3**.

Birth packages now require, from source creation rather than later retrofit:

- hermetic seal contract;
- Founder-operator role separated from customer Owner/private namespace;
- no Founder-operator access to Owner-private or cross-ARC private state;
- bounded safe-writer requirement when own-repository autonomy is granted;
- Founder-authorized free-only model/provider boundary;
- deterministic model EOL/404/410 failover without retry storms;
- capability routing only inside eligible free routes unless Founder explicitly authorizes paid capacity.

`node scripts/validate-arc-factory-contract.mjs` is the canonical schema/template drift gate. Generated packages remain validated by `scripts/validate-arc-factory-package.mjs`.

## PRIME / Hermes current model boundary

The previous MiniMax M3 route reached provider EOL on 2026-09-09 and must not be treated as an active recovery target.

Current approved free-only runtime direction:

```text
primary:  NVIDIA free endpoint → moonshotai/kimi-k3
fallback: NVIDIA free endpoint → deepseek-ai/deepseek-v4-pro-0813
```

Binding rule is capability/cost based rather than model-ID based:

```text
FREE_ENDPOINT_REQUIRED = true
PAID_MODEL_FALLBACK_ALLOWED = false
AUTONOMOUS_BILLING_CHANGES_ALLOWED = false
AUTONOMOUS_CREDIT_PURCHASE_ALLOWED = false
PAID_OVERRIDE_AUTHORITY = founder_explicit_only
```

If either named model loses free eligibility, capability or availability, Hermes/ARC routing must select another verified-free route or fail closed and escalate to the Founder.

The live PRIME VPS configuration has been moved toward this route. The durable PRIME repository must keep recovery truth synchronized with the proven runtime and must never restore the retired MiniMax route as an active default.

## Cargo ARC

Cargo remains the strongest current post-VONDA implementation reference for:

- dedicated source boundary in `Javalin13/CargoConnect/arc/`;
- isolated runtime/profile/state/secrets;
- own-repository autonomy with bounded safe writer;
- CI-backed coherence/hermetic audits;
- durable runtime source manifest and recovery rules;
- keyed candidate/onboarding isolation;
- OMEGA + FACTORY + PRIME supervision registration.

The historical MiniMax pool assignment is no longer a valid future recovery target after provider EOL. Cargo must be reassigned only to a verified-free route and runtime evidence must distinguish desired assignment from observed live assignment.

Cargo maturity remains evidence-derived; architecture/runtime readiness does not by itself manufacture an earned aura.

## NARC

NARC is no longer a pre-creation reservation.

Current verified repository reality:

- dedicated authoritative repository: `Javalin13/NARC-ARC`;
- OMEGA/FACTORY/PRIME registration exists;
- isolated NARC runtime source package exists;
- four-plugin depth-enhancement package exists;
- NARC client-facing leak incident was repaired and clean re-verification evidence exists;
- Owner binding to Narek remains a separate F5 event and must not be simulated;
- Founder direct-work lane exists as an operator role separate from Narek's Owner/private namespace;
- maturity remains unearned until evidence gates close.

The retired MiniMax assignment must not be considered an active recovery target. NARC inherits the same free-only model/provider boundary as PRIME and other ARCs.

## VONDA ARC

VONDA remains ARC #1 / tutorial and Golden Blueprint reference. Its bridge/direct-Founder-development doctrine is active source truth. VONDA must retain:

- separate Owner/customer namespace from Founder-operator maintenance authority;
- hermetic private-state boundaries;
- OMEGA/FACTORY registration;
- evidence-derived maturity/aura;
- free-only model/provider routing unless Founder explicitly authorizes paid capacity.

VONDA remains a blueprint/reference source; private customer payload must never become Factory template data.

## Fleet / Earth / FamilieKompas

- Fleet ARC source boundary is reserved in `Javalin13/FleetConnect`, but Fleet ARC is not thereby instantiated.
- EarthEcom and FamilieKompas contain RYZ3N integration-hardening references but are not autonomous ARC instances merely because product repositories exist.
- Future instantiation must pass the same Factory v1.3 birth and evidence gates.

## Founder direct-work invariant

The Founder may work directly with an ARC in its bounded development/maintenance lane without becoming or impersonating the customer Owner.

```text
Founder session
→ founder_operator
→ ARC-local development/maintenance authority
→ bounded own-repository safe writer when granted
→ no Owner-private memory inheritance
→ no cross-ARC private-state access

Owner session
→ customer Owner
→ customer/business operating experience
→ Owner-private ARC namespace

Unknown/unbound
→ fail closed
```

PRIME supervises/escalates and coordinates lifecycle state; it does not need to remain the permanent conversational middleman for ordinary ARC-local work.

## Engineering quality target

A repository or ARC is not called state of the art because it contains many documents. The target remains:

- deterministic source manufacture;
- policy-as-code and CI enforcement;
- one authoritative source boundary per ARC;
- least-privilege privileged actions;
- safe retry/idempotency and reconciliation;
- isolation by construction;
- recovery/reconstruction proof;
- observability without private-payload leakage;
- evidence-derived lifecycle/maturity;
- free-only model routing unless Founder explicitly changes the financial boundary;
- progressively lower Founder effort per ARC without reducing auditability.

## Current priority

Do not redesign the hierarchy. Continue closing operational/source drift:

1. keep PRIME repository recovery truth synchronized with proven live runtime;
2. remove retired MiniMax from active desired-state assignments while retaining historical evidence where useful;
3. keep Cargo/NARC/VONDA source truth distinct from runtime observations;
4. run Factory v1.3 contract CI and ARC-local hermetic/coherence CI;
5. implement transactional/idempotent Factory provisioning and reconciliation rather than adding new architecture layers.

> **Architecture is stable. The work now is convergence, automation, evidence and drift prevention.**
