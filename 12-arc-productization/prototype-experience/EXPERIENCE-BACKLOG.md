# ARC Prototype Experience Backlog

```yaml
---
type: ux-product-experience-backlog
status: active
created: 2026-09-03
classification: research-and-exploration -> product-design-candidates
source_scope: all ARC prototypes and founding pilots
---
```

## Objective

Convert lived ARC prototype experience into reusable product intelligence for the final ARC UX/system.

## Backlog fields

Each item should record:

| Field | Meaning |
|---|---|
| ID | `EXP-YYYYMMDD-NNN` |
| ARC / pilot | Source prototype, e.g. PRIME, VONKA |
| User type | Founder, solo entrepreneur, team member, etc. |
| Date | When experienced |
| Category | onboarding / interaction / memory / trust / notifications / workflow / language / reliability / support / pricing / other |
| Observation | What actually happened |
| User impact | low / medium / high / critical |
| Frequency | once / repeated / systemic |
| Evidence | observed / user-reported / measured / inferred |
| Workaround | What was done during prototype |
| Reusable lesson | Generalized lesson without customer-confidential data |
| Candidate change | UX/system/product change worth testing |
| Tier impact | Standard / Pro / Business / Dedicated / Enterprise / all |
| Status | raw / validated / recurring-pattern / design-candidate / implemented / rejected / deferred |
| Validation target | Which later ARC/pilot should test the improvement |

## Prioritization

Use this order:

1. safety/privacy/data isolation;
2. reliability/recovery;
3. blockers that prevent users completing core work;
4. repeated high-friction UX;
5. repeated high-value requests;
6. onboarding/support burden that prevents scale;
7. commercial/tier implications;
8. convenience/polish.

## Promotion threshold

An experience should feed the final ARC UX/system when one of these is true:

- it repeats across two or more users/prototypes;
- it is safety/privacy/reliability critical even once;
- it materially reduces onboarding/support time;
- it is a strong direct user need aligned with the ARC product thesis;
- it is measured to improve task completion, trust or retention;
- the Founder explicitly promotes it.

A single preference should normally stay a pilot-specific customization until evidence supports product-wide promotion.

## Current seed items

| ID | ARC / pilot | Category | Observation | Candidate change | Status |
|---|---|---|---|---|---|
| EXP-20260903-001 | PRIME | continuity | Durable repo/state reduced dependence on transient chat context | Make durable state/continuity a baseline ARC property | validated |
| EXP-20260903-002 | PRIME | interaction | Telegram works as a low-friction initial operating interface | Keep Telegram as pilot interface while final UX is learned | validated |
| EXP-20260903-003 | PRIME | operations | Manual/repetitive technical intervention must decrease as ARC count grows | Productize provisioning, health and recovery controls | design-candidate |
| EXP-20260903-004 | VONKA | onboarding | First external user will reveal what explanation/configuration is actually required | Track every onboarding question and convert recurring ones into guided setup | raw |
| EXP-20260903-005 | VONKA | UX | External non-technical use should drive final interaction design | Capture confusion, successful prompts, preferred flows and ignored features | raw |

## Review cadence

- During active pilot: capture meaningful events continuously.
- Weekly during early pilots: review new items and merge duplicates conceptually without deleting history.
- At each new ARC launch: review recurring patterns before provisioning.
- Before final ARC UX/system design: perform a full backlog synthesis and only then freeze core UX requirements.
