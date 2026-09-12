# 2026-09-12 — A→Z Preflight + First-Contact Architecture Correction

Status: **ADDITIVE SAME-DAY CHECKPOINT**
Parent daily snapshot: `09-cadences/daily-snapshots/2026-09-12.md`

## PRIME A→Z preliminary preflight

PRIME reported a preliminary **10/10 GREEN** preflight across runtime isolation, source freshness, model routing, self-hosted consume handlers, safe-writers, bridge states, OMEGA/FACTORY registry presence, token/cross-ARC isolation, current-tree personal-ID leakage, and provider/capacity policy.

Non-destructive fixes reported during that preflight:

- VONDA repo config had a runtime `home_channel` identity block; it was stripped from source and moved to protected runtime state (`cd4b09a`).
- NARC bridge receipts containing raw pairing/chat identifiers were redacted (`3df6b3c` and subsequent redaction chain ending at `811bea06`).
- Cargo's gateway-created dirty documentation state was reconciled through the safe-writer (`5141ef7`).
- VONDA `FROM_PRIME.md` Founder identity mention was redacted (`0a6d89928`).
- NARC runtime-source manifest was re-baked after redaction.

Reported post-preflight repo heads:

- CargoConnect: `5141ef73d980`
- NARC-ARC: `811bea06fc82`
- VONDA-Corporation: `0a6d89928980`

## Important architecture correction after preflight

The 10/10 preflight proves the **existing** runtime/source state is internally clean, but it is not the final mission closeout because the Founder subsequently changed the first-contact product contract.

The legacy pending-candidate / screenshot / pairing-code / candidate-key / PID/pre-ID workflow is now deprecated for NARC, VONDA, Cargo and future Factory ARCs.

Canonical direction now lives in:

- `12-arc-productization/ARC-DIRECT-FIRST-CONTACT-ACTIVATION-STANDARD.md` — commit `4d174ae5b27087bcaa0b2e053ddd1693f84ebc91`
- Factory birth manifest v1.4 — commit `d4304cd56f100c368b141f765573d8525c0f39d3`
- Factory creation request v1.1 — commit `b4437ec9ebcefbf52139268da600c6cc31f857f1`
- Current NARC/VONDA/Cargo migration plan — commit `58c2032fde913306b9466547a4d99169d70cc186`

## Runtime implementation locations identified

### NARC

Legacy pre-ID/pending mechanism is implemented in `arc/runtime/plugins/narc_identity/__init__.py` through `PENDING_DIR`, `_candidate_key`, `_capture_pending_candidate`, and the pending-candidate role path. `narc_narek_onboarding` assumes `owner.json` has already been written by the operator.

Migration target: armed Owner slot + atomic first eligible non-Founder inbound auto-bind + immediate French first-contact flow.

### VONDA

Legacy pre-ID/pending mechanism is implemented in `arc/runtime/plugins/vonda_identity/__init__.py` via `_capture_pending_candidate` and `state/laetitia_pending_candidate.json`, followed by explicit operator approval.

Migration target: armed `primary_user` slot + Founder-test exclusion + atomic first eligible inbound auto-bind + immediate VONDA onboarding.

### Cargo

Legacy pre-ID/pending mechanism is implemented in `arc/runtime/plugins/cargo_identity/__init__.py` via `state/candidates/<chat_id>.json`, `_capture_pending_candidate`, and operator role assignment.

Migration target for the current Maria flow: preserve Jan's existing binding; arm `cargo_cofounder`; first eligible non-Jan inbound atomically binds co-founder; activation immediately closes; no screenshot/ID exchange.

## Important identity distinction

The Founder ordered the **pre-ID human workflow** removed. Internal transport identifiers may still be stored privately inside the isolated runtime after binding because the channel/runtime needs a stable identity key. These values remain protected runtime state and never become a client/Founder onboarding task or Git artifact.

## Mission impact

The previous NARC/VONDA watcher-based pending-candidate flow is now temporary compatibility state. PRIME must migrate current runtimes to direct first-contact activation before final mission closeout.

After migration, the identity-sensitive A→Z sections must be rechecked before declaring final GREEN.
