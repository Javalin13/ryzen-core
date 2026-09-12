# RYZ3N ARC Direct First-Contact Activation Standard

Status: **CANONICAL — Founder directive 2026-09-12**

Related canonical role standard: `ARC-ROLE-TAXONOMY-AND-ENTITLEMENT-LIMIT-MESSAGING-STANDARD.md`

## 1. Purpose

ARCs must be directly usable by the intended Owner on the **first real contact**. The human onboarding flow must not depend on screenshots, pairing-code relays, candidate IDs, PIDs, manual chat-ID handling, or Founder copy-paste approval steps.

This standard applies to:

- future Factory-created ARCs;
- NARC / Narek Owner activation;
- VONDA / Laetitia Owner activation;
- Cargo / Maria Owner activation (business title may remain co-founder metadata);
- any later Owner first-contact activation unless a stronger role-specific identity method is explicitly required.

John / Jan is always the canonical `founder`. Every non-Founder human granted an ARC is canonically an `owner`. Business titles do not replace these authorization roles.

## 2. Canonical rule

When an Owner slot has been explicitly authorized and armed by the Founder / Factory, the **first eligible inbound sender** to that ARC is atomically bound to `owner` and can continue directly into the ARC's normal first-contact onboarding in the same interaction.

The client-facing flow is therefore:

```text
Founder / Factory authorizes Owner slot
        ↓
ARC activation state = ARMED
        ↓
intended Owner sends first real message
        ↓
runtime resolves actual sender internally
        ↓
first eligible sender is atomically bound as owner
        ↓
activation state closes immediately
        ↓
ARC responds as the Owner and starts onboarding
```

There is **no human-visible pre-ID step** between first contact and normal use.

## 3. Explicitly removed from the normal human workflow

The following are not valid normal onboarding requirements:

- screenshots for identity approval;
- pairing-code handoff to the Founder;
- candidate-key handoff;
- PID / pre-ID exchange;
- Telegram chat-ID or user-ID copy/paste;
- Founder manually choosing a pending candidate after the expected Owner has contacted the ARC;
- PRIME waiting for a screenshot before the ARC can function;
- client-facing narration of runtime identity/binding mechanics.

Runtime-private numeric identities may still exist internally because the transport requires them. They are **implementation details only** and must never become an onboarding task for the Owner or Founder.

## 4. Activation safety model

Direct activation does **not** mean that any random sender can permanently claim an ARC at any time.

An Owner may auto-bind only when all of the following are true:

1. the specific Owner slot was explicitly authorized in the ARC / Factory state;
2. a runtime-private activation record is currently `armed`;
3. the Owner slot is still unbound;
4. the sender is not the Founder identity or another already-bound role;
5. the inbound is a real transport-originated user message;
6. the runtime can resolve a single sender identity from its own isolated profile state;
7. an atomic claim can be completed without a race or conflicting claim.

On success, the runtime must:

- write the Owner binding in runtime-private state (0600 or equivalent);
- mark the activation record `consumed` / `closed` in the same bounded transition;
- continue immediately into the Owner's first-contact onboarding;
- preserve ARC-private namespaces and all Founder/Owner separation rules.

If the runtime cannot complete the claim unambiguously, it must fail closed **without exposing IDs and without asking the user for screenshots or pairing codes**. The Founder/PRIME may re-arm or repair the runtime, but the human-facing product must remain ID-free.

## 5. Race / ambiguity rule

The activation transition must be atomic.

- Exactly one eligible sender may consume an armed Owner slot.
- Multiple simultaneous claims must not create multiple bindings.
- A losing or ambiguous sender remains unbound and receives a neutral access-unavailable response.
- The runtime must never fall back to a mutable "latest candidate wins" model.

## 6. Founder exclusion

The canonical `founder` role is separate from `owner`.

The Founder identity that is already known to the ARC must be explicitly excluded from consuming an armed Owner slot. Founder testing therefore cannot accidentally become Owner binding.

Where Founder operational powers are needed, they are capabilities of the `founder` role; they are not a replacement role such as `founder_operator` or `founder_test` in the canonical model.

For a migrated ARC where Founder identity is known only from legacy pending state, the one-time migration may convert that known identity into a runtime-private exclusion record. The legacy pending record is then archived/deleted. No personal identifier is committed to Git.

## 7. Current ARC migration requirements

### NARC

- Remove the normal dependency on `pending_candidates/` + operator `bind-narc-owner.py` for first Owner activation.
- Keep the Founder identity excluded from the Owner claim.
- When Narek sends the first eligible inbound while the NARC Owner claim is armed, bind that sender atomically as `owner`, then continue directly into the French red/blue-pill first-contact flow.
- No screenshot, pairing code, candidate key, PID, chat-ID relay, or manual candidate approval.

### VONDA

- Remove `laetitia_pending_candidate.json` + manual operator approval from the normal first-contact flow.
- Normalize Laetitia's canonical authorization role to `owner` rather than legacy `primary_user`.
- When Laetitia sends the first eligible inbound while the VONDA Owner claim is armed, atomically create/update the protected Owner binding and continue directly into VONDA onboarding.
- Founder identity remains excluded.

### Cargo

- John / Jan's existing Cargo identity binding must be preserved but its canonical role must be `founder`, never `owner`.
- Maria's canonical ARC role is `owner`; her Cargo Connect business title may remain co-founder metadata.
- Remove per-candidate manual approval from Maria's first-contact activation.
- When Maria's Owner slot is explicitly armed and unbound, the first eligible non-Founder inbound atomically binds `owner` and becomes functional immediately.
- Do not use a permanently open claim window.

## 8. Factory inheritance

Every newly created ARC must inherit a first-contact activation contract at birth.

Required Factory truth:

```yaml
roles:
  founder: founder
  non_founder_arc_user: owner
  business_titles_are_metadata: true

first_contact_activation:
  mode: armed_first_eligible_inbound_auto_bind
  target_role: owner
  manual_pairing_code_required: false
  screenshot_required: false
  candidate_id_handoff_required: false
  pid_or_pre_id_required: false
  runtime_private_identity_allowed: true
  atomic_claim_required: true
  founder_excluded: true
  close_after_successful_claim: true
  ambiguity_policy: fail_closed_without_id_handoff
```

The Factory must create the Owner-specific activation state and the ARC must be runtime-ready **before** the intended Owner is invited to contact it.

## 9. PRIME / OMEGA responsibility

PRIME and OMEGA oversee the health of activation but are not normal manual pairing clerks.

They may:

- arm an explicitly authorized Owner slot;
- verify runtime readiness;
- repair activation-state drift;
- verify the resulting binding and lifecycle evidence;
- escalate ambiguity or runtime faults.

They must not require the Founder to shuttle screenshots, pairing codes, candidate IDs, PIDs, chat IDs, or user IDs between the Owner and the runtime.

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

An ARC passes this standard when a pre-authorized intended Owner can:

1. receive the ARC contact/link;
2. send one real first message;
3. be internally bound as `owner` without any screenshot/code/PID exchange;
4. receive the correct Owner-aware onboarding response immediately;
5. continue normal work on the next turn;
6. remain isolated from Founder and other ARC-private namespaces.

John / Jan must continue to resolve as `founder` throughout this process.

That is the required product experience for current and future ARCs.
