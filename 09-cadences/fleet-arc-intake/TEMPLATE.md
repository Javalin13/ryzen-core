# Fleet ARC Intake — Template

```yaml
---
id: YYYY-MM-DD-NN-<short-slug>
date_observed: YYYY-MM-DD
date_intake_created: YYYY-MM-DD
intake_type: <one of the 10 intake types — see below>
title: <one-line title>
status: raw | validated | accepted | promoted | deprecated
classification: research-and-exploration
amendable: true-additively
related_fleetconnect_evidence: <path, document, conversation, or AI session>
related_arc: FleetConnect
founder_acceptance:
  founder: jan-blommaert
  date: YYYY-MM-DD | null
  decision: accept | defer | decline | pending
  notes: <founder's notes, when applicable>
---

# YYYY-MM-DD-NN — <Title>

## 1. Discovery

<One-paragraph description of the discovery. What was observed? Where? When? Under what conditions?>

## 2. Source (FleetConnect Evidence)

<Where did this discovery come from? Which FleetConnect repo, document, conversation, or AI session produced the observation?>

<If the discovery is from a simulation, name the simulation, the parameters, and the founder's acceptance of the simulation as evidence.>

## 3. Validation Evidence

<What evidence supports the discovery? Data points, observations, simulations, comparisons?>

<If the discovery is *inferred* rather than *observed*, mark it explicitly. Inferred discoveries are valid intake candidates but are flagged.>

## 4. Reusability Argument

<Why is this discovery expected to recur? Why does it inform future ARC design? What is the *load-bearing* insight that makes it durable?>

<If the reusability argument is weak, the discovery is not intake-worthy. Mark as `decline` and document the reason.>

## 5. Tier Classification (per the Interpretation Protocol)

<Every claim in the intake must be locatable in the 5-state anti-hallucination space:>

- **Implemented** — already a real part of FleetConnect's operation. *(rare for new discoveries)*
- **Planned** — on FleetConnect's roadmap, but not yet built.
- **Designed** — designed (in FleetConnect's architecture docs or in this intake), but not yet planned.
- **Envisioned** — conceptualized (in the canonical doctrine or in conversation), but not yet designed.
- **Researched** — investigated, but not yet conceptualized.

<Mark which state(s) the discovery is in. Most new discoveries start at "Researched" or "Envisioned" and move up as they mature.>

## 6. Cross-References

- **Recovery archive:** <relevant recovered concept or design decision>
- **Rebuild spec:** <relevant R1–R4 section, when applicable>
- **Runtime roadmap:** <relevant phase, when applicable>
- **Foundation governance:** <relevant rule, when applicable>
- **Continuity canonical:** <relevant canonical, when applicable>
- **Other intakes:** <related intakes, when applicable>

## 7. Promotion Path (when status moves to "promoted")

<If the founder accepts the discovery for promotion, document the promotion path. The discovery may be promoted to:>

- The **rebuild spec** (e.g., as a new R1 deliverable, an amendment to C1–C8, or a new design decision)
- The **runtime roadmap** (e.g., as a new runtime requirement for R1–R4)
- The **foundation governance** (e.g., as a new governance rule, via a new ADR)
- The **canonical doctrine** (e.g., as an amendment to the Founder Identity, the Capability Model, or the Interpretation Protocol)
- A **new intake** (e.g., a related but distinct discovery that deserves its own intake)

<Promotion requires a new ADR. The promotion ADR must reference this intake.>

## 8. Deprecation Path (when status moves to "deprecated")

<If the discovery is deprecated, document:>

- Why the discovery is no longer valid.
- What superseded it (a new intake, a canonical change, an operational reality shift).
- Whether the discovery's insights are preserved in a *new* intake (continuity) or simply abandoned (rare; usually a new intake supersedes).

<Deprecated intakes are *preserved* (additive only); they are never deleted.>

## 9. Notes

<Free-form notes. Open questions. Related conversations. Anything that doesn't fit the structured sections.>

---

## Template Notes

- **Filename convention:** `YYYY-MM-DD-NN-<short-slug>.md`
  - `YYYY-MM-DD` — date the intake was added.
  - `NN` — sequence number (01, 02, ...) for intakes added on the same day.
  - `<short-slug>` — kebab-case slug describing the discovery.
  - Example: `2026-07-15-01-driver-assignment-by-proximity.md`

- **Intake type (one of 10):**
  1. `01-dispatch-intelligence` — patterns, decisions, and learnings about dispatching
  2. `02-capacity-intelligence` — patterns, decisions, and learnings about capacity
  3. `03-demand-intelligence` — patterns, decisions, and learnings about demand
  4. `04-pricing-intelligence` — patterns, decisions, and learnings about pricing
  5. `05-supply-intelligence` — patterns, decisions, and learnings about supply
  6. `06-operational-governance-patterns` — governance rules, validation gates, audit trails
  7. `07-memory-requirements` — memory patterns, layer requirements, retention
  8. `08-verification-requirements` — verification patterns, recursion levels, failure modes
  9. `09-runtime-requirements` — performance, integration, concurrency, state, recovery
  10. `10-arc-coordination-requirements` — cross-ARC intelligence, memory, governance, workflows

- **Status lifecycle:** `raw → validated → accepted → promoted | deprecated`
  - `raw` — captured but not yet validated.
  - `validated` — supported by evidence; founder not yet accepted.
  - `accepted` — founder has accepted the discovery for accumulation. The discovery is now a foundation asset.
  - `promoted` — the accepted discovery has been promoted to a design, a runtime requirement, or a governance rule.
  - `deprecated` — the accepted discovery is no longer valid; preserved but not authoritative.

- **Founder acceptance is required for accumulation.** Raw and validated intakes are *candidates*; accepted intakes are *assets*. Promoted intakes have crossed into the rebuild spec, the runtime roadmap, or the foundation governance. Deprecated intakes are preserved for continuity.

- **Additive only.** Intakes are never deleted, never overwritten. Deprecated intakes are preserved (with the deprecation reason documented in section 8).
