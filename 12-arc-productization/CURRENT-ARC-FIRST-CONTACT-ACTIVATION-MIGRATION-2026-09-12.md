# Current ARC First-Contact Activation Migration — 2026-09-12

Status: **Founder-authorized / implementation required now**
Canonical standard: `ARC-DIRECT-FIRST-CONTACT-ACTIVATION-STANDARD.md`

## Founder decision

The legacy human workflow based on screenshots, pairing IDs/codes, candidate IDs, PIDs/pre-IDs, or manual pending-candidate approval is removed for **NARC, VONDA, Cargo and future ARCs**.

The intended role must become functional on the first real inbound once its role slot has been explicitly armed.

## NARC migration

Current legacy behavior:
- `narc_identity` captures unknown senders under `state/pending_candidates/`.
- operator-side binding is required before Narek can become `owner`.

Required behavior:
- preserve Founder/operator exclusion in runtime-private state;
- create a runtime-private armed Owner activation record;
- while armed and Owner unbound, first eligible non-Founder inbound atomically writes the NARC Owner binding;
- immediately close/consume activation;
- same turn proceeds to NARC's French first-contact/red-blue-pill onboarding;
- legacy Founder test candidate must never bind and should be archived/removed after its identity is migrated to the Founder-exclusion state;
- normal human workflow uses no pending candidate, screenshot, pairing code, PID, candidate key or chat-ID handoff.

## VONDA migration

Current legacy behavior:
- `vonda_identity` captures `laetitia_pending_candidate.json` and requires explicit operator approval/bind.

Required behavior:
- use existing Founder-test binding as an exclusion;
- create runtime-private armed `primary_user` activation state;
- first eligible non-Founder inbound while armed atomically binds `primary_user` to the resolved sender;
- immediately close/consume activation;
- same turn enters VONDA first-contact onboarding;
- delete/archive the legacy pending-candidate state after migration;
- no screenshot/pairing/PID/manual-candidate handling.

## Cargo migration

Current legacy behavior:
- unknown users are stored under `state/candidates/` and require operator role assignment.

Required behavior for the current Maria flow:
- Jan's existing Cargo binding remains unchanged;
- create runtime-private armed activation for target role `cargo_cofounder`;
- first eligible non-Jan inbound while that role is armed and unbound atomically creates Maria/co-founder binding;
- close/consume the activation immediately;
- same turn becomes normal `cargo_cofounder` experience;
- do not leave a permanently open auto-claim window;
- legacy per-candidate records are not part of normal human onboarding and should be archived/removed when no longer needed for migration evidence.

## Atomicity and race safety

Each ARC implementation must use an atomic claim transition. At minimum:
- lock or exclusive-create around the role-binding transition;
- re-read the binding after the claim;
- only one sender can win;
- activation closes on success;
- later unknown senders fail closed;
- ambiguity does not trigger ID handoff to the Founder.

## Runtime-private state only

The following remain outside Git:
- chat/user IDs;
- role bindings;
- activation claim identities;
- legacy candidate records;
- any transport secrets.

Git may contain only non-identifying state labels and implementation/policy code.

## PRIME migration acceptance gates

For each of NARC, VONDA and Cargo:
1. source-freshness preflight;
2. replace legacy manual first-contact binding path with armed direct auto-bind;
3. preserve Founder/operator exclusions and existing valid bindings;
4. safe-writer commit/push;
5. re-bake runtime manifest if tracked source changed;
6. run ARC-specific audits;
7. controlled ARC-only restart;
8. verify Telegram connected and primary model route GREEN;
9. verify no duplicate poller and no cross-ARC disturbance;
10. arm current intended role activation;
11. verify first eligible real inbound becomes functional without screenshot/code/PID/candidate handoff;
12. record non-identifying closeout receipt.

## Current mission impact

NARC M11/M12 and VONDA M14/final GREEN are not considered complete merely because a watcher exists. They close only after the new direct first-contact path binds the intended real person and completes the first-contact flow.

Cargo's Maria co-founder onboarding should also be moved to this direct first-contact model before asking Maria for any further screenshots or IDs.

Future Factory-created ARCs must be born with this behavior rather than retrofitted later.
