# ARC Prototype Experience → Final UX/System Feed Contract

```yaml
---
type: product-feedback-contract
status: active
created: 2026-09-03
classification: approved-product-process
---
```

## Principle

The final ARC UX/system must be informed by accumulated prototype evidence. Prototype feedback is not merely archived; validated reusable patterns become design inputs.

## Feed stages

1. **Capture** — record meaningful prototype experience.
2. **Classify** — category, impact, frequency, evidence quality, tier impact.
3. **Generalize** — remove customer-specific/confidential content and state the reusable pattern.
4. **Validate** — confirm through repetition, measurement, criticality or Founder promotion.
5. **Promote** — move to `design-candidate` when evidence justifies a product-wide change.
6. **Specify** — translate the candidate into a concrete UX/system requirement with acceptance criteria.
7. **Implement** — build only when authorized in the relevant runtime/product phase.
8. **Re-test** — validate the change in later pilots; do not assume implementation solved the original problem.
9. **Close/retain** — mark implemented/rejected/deferred while preserving historical evidence.

## Mandatory final-UX gate

Before the final ARC UX/system is frozen, the design review must explicitly answer:

- Which prototype experiences shaped this flow?
- Which recurring frictions were removed?
- Which successful patterns were preserved?
- Which support-heavy actions were automated or simplified?
- Which privacy/trust/reliability requirements came from real users?
- Which requests were intentionally excluded and why?
- Which tier boundaries are visible in UX/entitlements?
- Which assumptions remain unvalidated?

A final UX proposal without this evidence trace is incomplete.

## No popularity-only rule

Not every repeated request becomes a feature. Promotion also checks:

- strategic alignment;
- complexity and maintenance cost;
- effect on Standard repeatability;
- privacy/security;
- whether the need belongs in a higher tier;
- whether a simpler UX solution solves the underlying need.

## Design traceability

Every major final ARC UX/system requirement should eventually reference one or more `EXP-*` records or an explicit Founder decision. This creates traceability from lived experience to final product design.
