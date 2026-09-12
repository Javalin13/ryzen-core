# Current ARC First-Contact Activation Migration — 2026-09-12

Status: **Founder-authorized / implementation required now**
Canonical standards:
- `ARC-DIRECT-FIRST-CONTACT-ACTIVATION-STANDARD.md`
- `ARC-ROLE-TAXONOMY-AND-ENTITLEMENT-LIMIT-MESSAGING-STANDARD.md`

## Founder decision

The legacy human workflow based on screenshots, pairing IDs/codes, candidate IDs, PIDs/pre-IDs, or manual pending-candidate approval is removed for **NARC, VONDA, Cargo and future ARCs**.

Canonical human roles are also normalized:
- John / Jan = `founder` everywhere;
- every intended non-Founder ARC human = `owner`;
- domain/business titles are metadata, not authorization roles.

The intended Owner must become functional on the first real inbound once the Owner slot has been explicitly armed.

## NARC migration

Required behavior:
- preserve Founder exclusion in runtime-private state;
- create a runtime-private armed Owner activation record;
- while armed and Owner unbound, first eligible non-Founder inbound atomically writes the NARC Owner binding;
- immediately close/consume activation;
- same turn proceeds to NARC's French first-contact/red-blue-pill onboarding;
- normal human workflow uses no pending candidate, screenshot, pairing code, PID, candidate key or chat-ID handoff.

Canonical roles:
- John / Jan = `founder`
- Narek = `owner`

## VONDA migration

Required behavior:
- retire legacy `primary_user` as the canonical authorization role;
- preserve Founder identity as `founder` and exclude it from Owner claim;
- create runtime-private armed `owner` activation state;
- first eligible non-Founder inbound while armed atomically binds Laetitia as `owner`;
- immediately close/consume activation;
- same turn enters VONDA first-contact onboarding;
- delete/archive the legacy pending-candidate state after migration;
- no screenshot/pairing/PID/manual-candidate handling.

Canonical roles:
- John / Jan = `founder`
- Laetitia = `owner`

## Cargo migration

Required behavior:
- preserve John / Jan's existing Cargo identity binding, but normalize the canonical authorization role from legacy `owner` to `founder`;
- preserve all Founder capabilities required for Cargo administration/operation;
- Maria's canonical authorization role is `owner`; her Cargo Connect business title may remain co-founder metadata;
- create runtime-private armed activation for target role `owner`;
- first eligible non-Founder inbound while that Owner slot is armed and unbound atomically creates Maria's Owner binding;
- close/consume the activation immediately;
- same turn becomes normal Cargo Owner experience with co-founder business context where relevant;
- do not leave a permanently open auto-claim window;
- legacy per-candidate records are not part of normal human onboarding and should be archived/removed when no longer needed for migration evidence.

Canonical roles:
- John / Jan = `founder`
- Maria = `owner` (business title: co-founder)

## Entitlement-limit correction

Owner-facing usage-limit messaging must follow `ARC-ROLE-TAXONOMY-AND-ENTITLEMENT-LIMIT-MESSAGING-STANDARD.md`.

If the Owner's own plan allowance is exhausted, the ARC must say that the Owner reached the current plan limit and present valid commercial choices, e.g. Standard -> wait, Pro for higher limits, Business for unlimited usage.

Shared provider/account exhaustion must not be misrepresented as an Owner plan-limit event. Provider/model/billing internals stay Founder/PRIME-only.

## Atomicity and race safety

Each ARC implementation must use an atomic claim transition. At minimum:
- lock or exclusive-create around the Owner-binding transition;
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
2. normalize human role vocabulary to `founder` / `owner`;
3. replace legacy manual first-contact binding path with armed direct Owner auto-bind;
4. preserve Founder exclusion and existing valid identity bindings;
5. safe-writer commit/push;
6. re-bake runtime manifest if tracked source changed;
7. run ARC-specific audits;
8. controlled ARC-only restart;
9. verify Telegram connected and primary/fallback model routing according to Founder policy;
10. verify no duplicate poller and no cross-ARC disturbance;
11. arm current intended Owner activation;
12. verify first eligible real inbound becomes functional without screenshot/code/PID/candidate handoff;
13. verify Owner entitlement-limit messages do not expose provider internals;
14. record non-identifying closeout receipt.

## Current mission impact

NARC, VONDA and Cargo first-contact proof are not considered complete merely because an activation slot exists. They close only after the direct first-contact path binds the intended real person as `owner` and completes the first-contact flow.

John / Jan must remain `founder` in all three ARCs throughout migration.

Future Factory-created ARCs must be born with this role model and first-contact behavior rather than retrofitted later.
