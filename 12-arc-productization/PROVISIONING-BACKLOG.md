# ARC Provisioning & Scaling Backlog

```yaml
---
type: productization-backlog
status: active
created: 2026-09-03
classification: planned-design-candidates
runtime_implementation_authorized: false
amendable: true-additively
---
```

## Objective

Reduce ARC onboarding from a bespoke technical project to a repeatable provisioning flow while ensuring every prototype produces structured learning for the final ARC UX/system.

Target end-state for Standard:

> New customer → choose tier → create isolated ARC identity/config → Telegram connection → workspace/memory → secrets/permissions → health test → live → capture real usage experience → feed validated patterns into the final ARC UX/system.

## Productization target

- Standard ARC: ~80–90% identical platform, ~10–20% customer configuration.
- Target mature Standard setup time: **1–2 founder/operator hours maximum**, excluding unusual migrations or custom integrations.
- Ongoing Standard support should be bounded and predictable.
- Each prototype must produce an auditable learning trail, not only a technical deployment.

## Provisioning backlog

### P0 — Pilot safety before scale

- [ ] Prove a second PRIME-derived ARC can coexist on the same VPS without cross-talk.
- [ ] Unique Telegram bot token and allowed-user scope per ARC.
- [ ] Unique ARC identity/persona/config.
- [ ] Separate workspace/memory boundaries.
- [ ] Separate secrets/env boundaries.
- [ ] Explicit tenant/user permissions.
- [ ] Restart/recovery behavior per ARC.
- [ ] Health check per ARC.
- [ ] Logs identify ARC/tenant without exposing secrets.
- [ ] Resource measurement: idle RAM, peak RAM, CPU, storage/log growth.
- [ ] Record every meaningful onboarding friction, reliability issue, confusion, support intervention and successful usage pattern in `prototype-experience/EXPERIENCE-BACKLOG.md`.

### P1 — Repeatable template

- [ ] Canonical ARC template derived from proven PRIME patterns, not raw copy-paste drift.
- [ ] Config schema: `arc_id`, owner, tier, language, channels, workspace, permissions, model route, support policy.
- [ ] Standard directory naming and service naming.
- [ ] Idempotent install/provision command.
- [ ] Idempotent update/upgrade mechanism.
- [ ] Rollback mechanism.
- [ ] Version marker/checkpoint per deployed ARC.
- [ ] Standard onboarding-question set derived from recurring prototype experience.
- [ ] Standard first-run UX derived from observed pilot friction, not assumed user behavior.

### P2 — Commercial controls

- [ ] Pilot start/end date field.
- [ ] Tier and billing-cycle field.
- [ ] Fair-use / usage counters.
- [ ] Dedicated-resource flag.
- [ ] Support entitlement.
- [ ] Feature entitlement per tier.
- [ ] Upgrade/downgrade path.
- [ ] Offboarding/data-export/deletion process.
- [ ] Track which requests are Standard product needs versus higher-tier/custom needs.

### P3 — Operations at 5–10 ARCs

- [ ] Per-ARC health overview.
- [ ] Resource usage dashboard.
- [ ] Central error surfacing without merging customer data.
- [ ] Backup policy.
- [ ] Update rollout order/canary path.
- [ ] Incident isolation.
- [ ] Usage/cost attribution.
- [ ] Support-time tracking.
- [ ] Cross-pilot experience review: identify recurring UX/system patterns across ARCs.
- [ ] Trace promoted UX requirements back to `EXP-*` evidence records.

### P4 — Dedicated / Business / Enterprise

- [ ] Dedicated VPS template.
- [ ] Stronger tenant isolation controls.
- [ ] Multiple authorized users/team permissions.
- [ ] External integrations governance.
- [ ] SLA/monitoring levels.
- [ ] Business continuity/recovery requirements.
- [ ] Audit/event history.
- [ ] Determine which prototype requests justify tier-specific UX rather than global complexity.

### P5 — Final ARC UX/system synthesis gate

Before the final ARC UX/system is frozen:

- [ ] Review the full prototype experience backlog.
- [ ] Group duplicate/recurrent friction patterns without deleting source history.
- [ ] Preserve successful interaction patterns that users naturally adopt.
- [ ] Convert validated patterns into explicit UX/system requirements and acceptance criteria.
- [ ] Map support-heavy manual actions to automation/simplification candidates.
- [ ] Confirm privacy, trust, memory, notification and recovery expectations from real users.
- [ ] Separate universal ARC UX from tier-specific/custom behavior.
- [ ] Document deliberately rejected requests and why.
- [ ] Identify remaining unvalidated assumptions.
- [ ] Re-test the final candidate UX with later pilots before declaring it stable.

## What NOT to automate prematurely

Do not build a full ARC Factory before the first pilots prove the repeatable requirements. The first external pilots are meant to reveal the minimum stable provisioning contract and the real user experience contract.

Automate only patterns that have repeated or are clearly safety-critical.

## Success metric

ARC #10 should require materially less Founder attention than ARC #1, while preserving isolation, reliability and user value.

The final ARC UX/system should be explainable from accumulated prototype evidence rather than being a design created in isolation from real users.
