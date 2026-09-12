---
id: 2026-09-12-narc-pairing-runtime-drift
date: 2026-09-12
status: active-blocker
classification: runtime-drift + owner-first-contact + product-acceptance
projects_touched: [ryzen-core, NARC-ARC, VONDA-Corporation, prime-vps-migration]
---

# 2026-09-12 — NARC owner-facing pairing runtime drift

## Founder evidence

Founder provided a Telegram screenshot showing NARC still emitted the default Hermes unknown-user pairing UX on a real inbound at approximately 17:49, with the same legacy behavior also visible earlier in the day.

No pairing code is recorded here. Pairing material is ephemeral/sensitive and is not part of the canonical Owner onboarding flow.

## Interpretation

This is a hard runtime/product drift signal, not merely a documentation issue.

Canonical RYZ3N source already requires:

- John / Jan = `founder`;
- intended non-Founder ARC holder = `owner`;
- explicitly armed Owner slot;
- first eligible real inbound atomically binds Owner;
- no screenshot, pairing code, candidate key, PID/pre-ID, chat-ID or manual operator ritual;
- same-turn Owner onboarding;
- fail-closed ambiguity without leaking IDs.

Therefore prior NARC source/unit-test GREEN does **not** prove the live Owner-facing path GREEN while generic Hermes pairing still intercepts the message.

Exact root cause remains to be diagnosed from runtime evidence. Possibilities include stale/wrong deployed process/profile, ingress ordering, middleware precedence, incomplete reload/restart, or another live-source parity fault. Do not assume one without evidence.

## Canonical correction

`ARC-DIRECT-FIRST-CONTACT-ACTIVATION-STANDARD.md` now includes an explicit transport-pairing precedence rule:

- armed ARC Owner atomic claim must be evaluated before human-visible generic pairing UX;
- generic pairing must not pre-empt the armed intended-Owner activation path;
- unauthorized/unarmed/ambiguous users still fail closed;
- any human-visible Hermes/default pairing prompt/code on an armed intended-Owner path is a hard RED release failure.

## Bridge correction

The active Founder/Lux→PRIME bridge now contains:

`arc/bridge/CONSUME-ADDENDUM-2026-09-12-NARC-HERMES-PAIRING-RUNTIME-DRIFT.md`

`SYNC_PROTOCOL.md` was updated so Founder command `consume` means PRIME reads `TO_PRIME.md` plus all active `CONSUME-ADDENDUM-*.md` files. Founder remains outside the technical copy/paste loop.

## Current acceptance requirement

Before Narek first-contact proof can be accepted:

1. live NARC Telegram ingress ordering is inspected;
2. armed Owner claim path no longer emits pairing UX;
3. Founder exclusion remains effective;
4. unauthorized/unarmed paths remain fail-closed;
5. atomic one-winner semantics remain intact;
6. scratch tests do not consume real activation state;
7. actual serving process/profile is proven current after controlled NARC-only restart/reload;
8. Narek slot remains armed+unbound until his real message.

## Mission impact

NARC direct-first-contact is now classified:

`SOURCE/UNIT CONTRACT = GREEN`

`LIVE OWNER-FACING FIRST-CONTACT = RED / BLOCKED ON PAIRING-MIDDLEWARE DRIFT`

This does not invalidate the overall direct-first-contact architecture. It proves that live ingress parity must be an explicit release gate for every ARC and Factory-born instance.
