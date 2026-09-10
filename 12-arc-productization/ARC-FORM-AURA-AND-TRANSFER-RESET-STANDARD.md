# ARC Form, Aura & Transfer Reset Standard

```yaml
---
type: arc-form-aura-transfer-reset-standard
status: founder-directed-current-model
created: 2026-09-10
classification: approved-product-semantics + lifecycle-governance
scope: ARC visual form, maturity aura, factory-form reset, ownership transfer, empty-ARC reset
amendable: true-additively
runtime_implementation_authorized: false
related:
  - ARC-V1-V6-COMMERCIAL-MATURITY-TUTORIAL.md
  - PRIME-RYZ3N-ARC-PROTOTYPE-DOCTRINE.md
---
```

## 1. Founder decision

The ARC has two separate user-visible concepts that must never be conflated:

1. **Form / look** — the ARC's chosen visual body, shell, skin, layout or presentation state.
2. **Aura** — the ARC's visible maturity signature, corresponding to its verified ARC maturity/version state.

The Owner may reset the ARC's **form/look** to its factory presentation.

The Owner may **not manually reset, select, recolor or falsify the aura** merely by changing or factory-resetting the ARC's form.

Core rule:

> **Form is owner-resettable. Aura is maturity-derived.**

---

## 2. Factory form reset

A normal factory-form reset is a presentation reset only.

It may restore the ARC's visual body/shell/layout to the default factory appearance for the product, but it must preserve the ARC's actual verified maturity state.

Therefore:

- a V4 Golden ARC whose Owner resets its form to factory appearance remains a **V4 ARC**;
- its maturity aura remains **Gold**;
- its verified Brains, capabilities, competence, evidence and lifecycle state are not downgraded merely because the visual shell was reset;
- the reset may not be used to impersonate V1 or another maturity tier;
- the reset may not grant a higher aura or maturity tier either.

A factory-form reset is therefore **not** a competence reset, memory reset, ownership reset or maturity reset unless a separate lifecycle operation explicitly performs those actions.

---

## 3. Aura invariance rule

The ARC aura is system-derived from the ARC's current verified maturity state.

Current progression remains:

`V1 Blue → V2 Cyan/Electric Blue → V3 Violet/Amethyst → V4 Gold → V5 Platinum → V6 Sovereign/Prismatic`

The aura may change only when the underlying verified maturity state changes through an authorized lifecycle transition.

The Owner may choose the ARC's form, but the Owner may not directly choose the aura independently of maturity.

This protects the meaning of progression: aura communicates what the ARC has actually become, not what skin the Owner selected.

---

## 4. Transfer / sale reset

Sale or transfer to another Owner introduces a different lifecycle case.

A transfer does **not automatically** mean that the ARC must lose all maturity. The transfer operation must explicitly define what is being retained, exported, deleted or reset according to privacy, ownership, commercial and technical rules.

However, when the transfer includes a **capacity / competence / owner-state reset** that makes the ARC effectively empty, the ARC must return to the Foundation state.

An **empty ARC** means the previous Owner's private identity/context, permissions, secrets, private memory and owner-specific operational competence/evidence have been removed or are no longer valid for the new Owner, such that the ARC can no longer truthfully claim the previous maturity state for that Owner.

In that case:

`Transferred + emptied/reset ARC → V1 Foundation ARC → V1 Blue aura`

The new Owner then grows that ARC again from V1 according to the normal evidence-based maturity path.

---

## 5. Transfer principle

A transfer must separate four things explicitly:

- **shared ARC platform/runtime** — reusable system foundation that remains part of the product;
- **ARC form/look** — owner-selectable presentation state that may be factory-reset;
- **private Owner state** — identity, memory, secrets, permissions, documents and private context subject to transfer/deletion rules;
- **verified maturity/competence state** — evidence-backed capability state that determines the aura.

The new Owner may not inherit the previous Owner's private payload by default.

Transferable generalized modules, platform capabilities and reusable Brain templates may still exist in the RYZ3N ecosystem, but they do not by themselves prove that the newly emptied ARC instance has already earned a higher maturity tier.

---

## 6. Maturity downgrade rule

Aura downgrade must follow a real lifecycle downgrade, never a cosmetic action alone.

Examples:

- **Reset visual form only** → maturity unchanged → aura unchanged.
- **Change skin/body/layout only** → maturity unchanged → aura unchanged.
- **Owner transfer with retained, valid and revalidated capability state** → maturity determined by the accepted transfer/revalidation result.
- **Owner transfer with empty/capacity/competence reset** → V1 Foundation → Blue aura.
- **Full ARC lifecycle wipe to empty ARC** → V1 Foundation → Blue aura.

No operation may leave an empty ARC displaying a higher aura for competence it no longer possesses.

---

## 7. Runtime implementation contract

When reset controls are eventually implemented, the runtime must represent form and aura as separate state domains.

Conceptually:

```text
form_state       = owner-selectable / factory-resettable presentation
maturity_state   = evidence-derived ARC version
maturity_aura    = deterministic projection of maturity_state
owner_state      = private identity/context/permissions/memory boundary
transfer_state   = explicit retain/export/delete/reset decision set
```

A form reset must not write to `maturity_state` or `maturity_aura`.

A full transfer/empty reset may write to maturity only after the system has invalidated or removed the competence/evidence required to claim the prior tier.

The aura is never an arbitrary color picker.

---

## 8. PRIME / steward obligation

PRIME and future native RYZ3N stewardship must verify that:

- cosmetic form resets do not silently alter maturity;
- aura remains coupled to verified maturity;
- transfers do not leak prior Owner private state;
- transfer/reset operations declare which capability/evidence is retained or invalidated;
- an empty ARC is recorded as V1 and rendered with the V1 aura;
- no ARC visually claims a maturity tier that its post-transfer evidence no longer supports.

This is a lifecycle and truthfulness invariant, not merely a design preference.

---

## 9. Founder shorthand

> **You can reset how your ARC looks. You cannot reset or pick its aura. The aura shows what the ARC truly is.**

> **If the ARC is transferred and genuinely emptied of the competence/state that made it mature, it becomes V1 again — with the V1 Blue aura.**
