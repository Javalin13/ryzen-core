# RYZ3N ARC Direct First-Contact Activation Standard

Status: **CANONICAL — Founder directive 2026-09-12**

## 1. Purpose

ARCs must be directly usable by the intended Owner / authorized role on the **first real contact**. The human onboarding flow must not depend on screenshots, pairing-code relays, candidate IDs, PIDs, manual chat-ID handling, or Founder/operator copy-paste approval steps.

This standard applies to:

- future Factory-created ARCs;
- NARC / Narek Owner activation;
- VONDA / Laetitia primary-user activation;
- Cargo / Maria `cargo_cofounder` activation;
- any later single-role first-contact activation unless a stronger role-specific identity method is explicitly required.

## 2. Canonical rule

When a role slot has been explicitly authorized and armed by the Founder / Factory, the **first eligible inbound sender** to that ARC is atomically bound to the pre-authorized role and can continue directly into the ARC's normal first-contact onboarding in the same interaction.

The client-facing flow is therefore:

```text
Founder / Factory authorizes role slot
        ↓
ARC activation state = ARMED
        ↓
intended person sends first real message
        ↓
runtime resolves actual sender internally
        ↓
first eligible sender is atomically bound
        ↓
activation state closes immediately
        ↓
ARC responds as the authorized role and starts onboarding
```

There is **no human-visible pre-ID step** between first contact and normal use.

## 3. Explicitly removed from the normal human workflow

The following are not valid normal onboarding requirements:

- screenshots for identity approval;
- pairing-code handoff to the Founder;
- candidate-key handoff;
- PID / pre-ID exchange;
- Telegram chat-ID or user-ID copy/paste;
- Founder manually choosing a pending candidate after the expected user has contacted the ARC;
- PRIME waiting for a screenshot before the ARC can function;
- client-facing narration of runtime identity/binding mechanics.

Runtime-private numeric identities may still exist internally because the transport requires them. They are **implementation details only** and must never become an onboarding task for the Owner, Founder, or customer.

## 4. Activation safety model

Direct activation does **not** mean that any random sender can permanently claim an ARC at any time.

A role may auto-bind only when all of the following are true:

1. the specific role slot was explicitly authorized in the ARC / Factory state;
2. a runtime-private activation record is currently `armed`;
3. the role slot is still unbound;
4. the sender is not an excluded Founder/operator identity or another already-bound role;
5. the inbound is a real transport-originated user message;
6. the runtime can resolve a single sender identity from its own isolated profile state;
7. an atomic claim can be completed without a race or conflicting claim.

On success, the runtime must:

- write the role binding in runtime-private state (0600 or equivalent);
- mark the activation record `consumed` / `closed` in the same bounded transition;
- continue immediately into the role's first-contact onboarding;
- preserve ARC-private namespaces and all Founder/Owner separation rules.

If the runtime cannot complete the claim unambiguously, it must fail closed **without exposing IDs and without asking the user for screenshots or pairing codes**. The operator may re-arm or repair the runtime, but the human-facing product must remain ID-free.

## 5. Race / ambiguity rule

The activation transition must be atomic.

- Exactly one eligible sender may consume an armed role slot.
- Multiple simultaneous claims must not create multiple bindings.
- A losing or ambiguous sender remains unbound and receives a neutral access-unavailable response.
- The runtime must never fall back to a mutable "latest candidate wins" model.

## 6. Founder/operator exclusion

Founder/operator roles are separate from customer / Owner roles.

A Founder/operator identity that is already known to the ARC must be explicitly excluded from consuming an armed customer/Owner slot. Founder testing therefore cannot accidentally become Owner binding.

For a migrated ARC where the Founder identity is known only from legacy pending state, the one-time migration may convert that known Founder identity into a runtime-private exclusion record. The legacy pending record is then archived/deleted. No personal identifier is committed to Git.

## 7. Current ARC migration requirements

### NARC

- Remove the normal dependency on `pending_candidates/` + operator `bind-narc-owner.py` for first Owner activation.
- Keep the Founder/operator identity excluded from the Owner claim.
- When Narek sends the first eligible inbound while the NARC Owner claim is armed, bind that sender atomically as `owner`, then continue directly into the French red/blue-pill first-contact flow.
- No screenshot, pairing code, candidate key, PID, chat-ID relay, or manual candidate approval.

### VONDA

- Remove `laetitia_pending_candidate.json` + manual operator approval from the normal first-contact flow.
- When Laetitia sends the first eligible inbound while the VONDA primary-user claim is armed, atomically create/update the protected primary-user binding and continue directly into VONDA onboarding.
- Founder test identity remains excluded.

### Cargo

- Preserve Jan's existing Cargo role exactly as currently intended.
- Remove per-candidate manual approval from Maria's `cargo_cofounder` first-contact activation.
- When the Maria co-founder role slot is explicitly armed and unbound, the first eligible non-Jan inbound atomically binds `cargo_cofounder` and becomes functional immediately.
- Do not use a permanently open claim window.

## 8. Factory inheritance

Every newly created ARC must inherit a first-contact activation contract at birth.

Required Factory truth:

```yaml
first_contact_activation:
  mode: armed_first_eligible_inbound_auto_bind
  manual_pairing_code_required: false
  screenshot_required: false
  candidate_id_handoff_required: false
  pid_or_pre_id_required: false
  runtime_private_identity_allowed: true
  atomic_claim_required: true
  founder_operator_excluded: true
  close_after_successful_claim: true
  ambiguity_policy: fail_closed_without_id_handoff
```

The Factory must create the role-specific activation state and the ARC must be runtime-ready **before** the intended person is invited to contact it.

## 9. PRIME / OMEGA responsibility

PRIME and OMEGA oversee the health of activation but are not normal manual pairing clerks.

They may:

- arm an explicitly authorized role slot;
- verify runtime readiness;
- repair activation-state drift;
- verify the resulting binding and lifecycle evidence;
- escalate ambiguity or runtime faults.

They must not require the Founder to shuttle screenshots, pairing codes, candidate IDs, PIDs, chat IDs, or user IDs between the client and the runtime.

## 10. Privacy / Git rule

No transport identifier, pairing secret, activation token, candidate ID, chat ID, user ID, or Owner-private identity record belongs in Git.

Git stores only the **policy, schema, code and non-identifying lifecycle evidence**. Runtime-private identity and activation state remain outside source control.

## 11. Maturity and commercial effect

Direct first-contact activation is infrastructure ergonomics only.

It does not:

- promote ARC maturity or aura;
- bypass commercial entitlement;
- bypass child/minor safety gates;
- grant cross-ARC access;
- grant billing authority;
- alter Owner-private namespace protections.

## 12. Acceptance test

An ARC passes this standard when a pre-authorized intended user can:

1. receive the ARC contact/link;
2. send one real first message;
3. be internally bound to the correct pre-authorized role without any screenshot/code/PID exchange;
4. receive the correct role-aware onboarding response immediately;
5. continue normal work on the next turn;
6. remain isolated from Founder/operator and other ARC-private namespaces.

That is the required product experience for current and future ARCs.
