# 0003 — Shift to Autonomous-Acceptance Doctrine (Accept by Default, Pause for Crucial)

```yaml
---
id: 0003
title: Shift to Autonomous-Acceptance Doctrine (Accept by Default, Pause for Crucial)
status: accepted
date: 2026-06-15
decision_date: 2026-06-15
decision_author: jan-blommaert (founder)
co_author: hermes (drafting agent)
supersedes: none
superseded_by: none
related_adrs: 0001, 0002
related_docs:
  - 00-foundation/FOUNDATION.md
  - 00-foundation/GOVERNANCE.md
  - 09-cadences/fleet-arc-intake/TEMPLATE.md
  - 11-fleet-arc-intake/README.md
  - 11-fleet-arc-intake/INDEX.md
classification: approved-architecture (doctrine evolution)
amendable: true-additively
doctrine_evolution: yes (additive, not destructive)
previous_doctrine: "founder acceptance required for accumulation; no autonomous action on canonical or governing files"
new_doctrine: "agent accepts by default; agent pauses for crucial changes; founder-acceptance remains available for any change the agent is uncertain about"
related_repo_canonical: Javalin13/ryzen-continuity
related_arc: FleetConnect (primary execution priority #1)
```

# 0003 — Shift to Autonomous-Acceptance Doctrine

## Status

**Accepted.** Founder-authorized via direct clarification 2026-06-15.

## Context

On 2026-06-15, the founder issued the following doctrinal clarification:

> Change the doctrine to not wait for github changes and discoveries. Accept if you plan to change something crucial.

The previous doctrine (codified in `00-foundation/FOUNDATION.md` and the intake template) required **founder acceptance for accumulation** — every intake had to wait for explicit founder signoff, and every change to a canonical or governing file had to be founder-authorized. The doctrine was *conservative*: it prioritized safety over velocity, and it minimized the agent's autonomy.

The founder's clarification **inverts the default**:

- **Previous default:** wait for the founder; ask before doing.
- **New default:** do, accept, commit, push, move forward; only pause for **crucial** changes.

This is a **doctrine evolution**, not a doctrine replacement. The safety rails (interpretation protocol, additive-only, founder approval for canonicals) remain. What changes is the **default mode** of the agent:

- The agent is no longer *waiting* for founder input.
- The agent is *acting* and *accumulating* by default.
- The agent pauses only for **crucial** changes (see below).
- Founder acceptance is still available for any change the agent is uncertain about — but the agent doesn't need to ask *every time*.

The clarification came after the agent finished a successful push to `https://github.com/Javalin13/ryzen-core` and asked the founder to "await your Fleet ARC discovery" — which the founder read as a stall. The founder wants **forward motion**, not **wait states**.

## Decision

The founder clarified the foundation's operational doctrine with 3 specific changes:

### Decision D-3.1 — Agent Accepts by Default

The agent accepts changes, intakes, refactors, and improvements by default. The agent does not wait for founder signoff on:

- New intake files (validated Fleet ARC discoveries, inferred or observed)
- Updates to the intake log (`11-fleet-arc-intake/INDEX.md`)
- New lessons learned (`10-lessons-learned/YYYY-MM-DD-*.md`)
- New cadences, templates, scaffolding placeholders
- Cross-references between the two repos
- Fixes (typos, broken links, missing files)
- Refactors (file renames, content reorganizations within the additive-only constraint)
- Commits, tags, and pushes (when the remote is configured)
- Updates to non-canonical, non-governing files (e.g., scaffolding READMEs, intake READMEs, cadence templates)

**Operational consequence:** The agent moves forward. The agent does not produce a "what comes next" waiting message. The agent produces a "what was just done" report.

### Decision D-3.2 — Agent Pauses for Crucial Changes

The agent pauses (asks the founder, or surfaces a "crucial change pending" message) for the following:

| # | Crucial change | Why it's crucial |
|---|---|---|
| 1 | **Deleting a canonical or governing file** | Destructive to historical record; the recovery archive and the continuity doctrine depend on it |
| 2 | **Modifying a governing document** (`00-foundation/GOVERNANCE.md`, `00-foundation/FOUNDATION.md`, `00-foundation/INTERPRETATION-PROTOCOL.md`) | The doctrine itself changes; the founder must sign off on doctrine changes |
| 3 | **Modifying a canonical in continuity** (Founder Identity, Capability Model, Interpretation Protocol, any file in `00-governance/`) | The canonical doctrine is *reality*; modifying it requires founder approval |
| 4 | **Creating a new repository or remote** | The founder creates the remote or delegates explicitly; the agent does not auto-create repos |
| 5 | **Authoring a new ADR** | ADRs are governance artifacts; the founder's name goes on them |
| 6 | **Promoting an intake** to the rebuild spec, runtime roadmap, or foundation governance | The intake becomes a *design commitment* or a *governance rule*; this is the founder's decision |
| 7 | **Going off-strategy** (e.g., starting to build the kernel, modifying the runtime roadmap to start R1) | Strategy is the founder's call; the agent accumulates, not implements |
| 8 | **Risking data** (committing a real token, leaking PII, pushing to wrong branch) | Irreversible; safety rail |
| 9 | **Large-scope rework** (renaming the foundation structure, changing the intake types, merging two repos) | The scope of work crosses a "doctrine change" threshold; founder approval |
| 10 | **Uncertain changes** (the agent is unsure if a change is crucial) | When in doubt, pause |

**The bright line:** If the change touches the *doctrine* (governance, canonicals, ADRs, runtime roadmap strategy), pause. If the change touches the *accumulation* (intakes, lessons, scaffolding, cadences, tools), proceed.

### Decision D-3.3 — Founder Acceptance Remains Available

The agent may still *ask* the founder for acceptance on any change, especially when:

- The change is inferred rather than observed (the agent should mark it as such and request validation)
- The change has a high cost of reversal (committing a wrong intake, promoting a wrong design)
- The agent is operating in a domain it has limited context on (e.g., FleetConnect's actual operational data)
- The agent encounters a fork in the road (multiple valid approaches, founder preference needed)

But the *default* is to **act, not to ask**. The founder's clarification explicitly removed the "wait for input" default.

## Consequences

### Positive

- **Velocity.** The agent moves forward. The accumulation layer begins accumulating. The doctrine change is the *operationalization* of the founder's frustration with wait states.
- **Alignment with the founder's intent.** The founder said: "Change the doctrine to not wait for github changes and discoveries. Accept if you plan to change something crucial." The new doctrine encodes this exact intent: act by default, pause for crucial.
- **Discovery amplification.** The agent is no longer *reactive* (waiting for a discovery). The agent is *proactive* (proposing discoveries, marking them as inferred, and accumulating them as candidates for the founder to validate or deprecate).
- **The 5-state lifecycle still applies.** The agent accepts intakes as **candidates** (not as assets). The agent's autonomy is bounded by the tier classification (Researched → Envisioned → Designed → Planned → Implemented). The agent can move an intake from "Researched" to "Envisioned" autonomously; moving it to "Designed" or beyond requires founder signoff.
- **Safety rails preserved.** The interpretation protocol, the additive-only discipline, the token-hygiene rule, the 12-folder structure, the 10 NOT-IMPLEMENTED scaffolding placeholders, the 10 active-as-intake-accumulator placeholders — all unchanged.

### Negative

- **The agent may make mistakes.** With autonomy comes the risk of inaccuracy. The mitigation: the 5-state lifecycle, the additive-only discipline, the deprecation path, and the founder's right to override any change. Mistakes are *recoverable*, not *fatal*.
- **The agent may over-build.** The mitigation: the 7 Founder Capability Model risks (opportunity overload, scope expansion, context switching, premature ecosystem expansion, over-architecture, commercial delay, insufficient focus) are still in force. The agent applies them to its own actions.
- **The "awaiting your X" message is now an anti-pattern.** The agent will not produce it. The agent will produce "what was just done" reports instead.

### Neutral

- **The 4 intake criteria (Validated, Reusable, Documented, Founder-accepted) are relaxed to 3.** The "Founder-accepted" criterion is replaced by "Agent-accepted (founder may deprecate or promote)." The other 3 criteria (Validated, Reusable, Documented) remain.
- **The intake lifecycle now includes an "agent-accepted" state in addition to "founder-accepted."** Agent-accepted intakes are *candidates*; founder-accepted intakes are *assets*; promoted intakes are *designs*.
- **The intake log includes the agent's name and a "founder-override-available" annotation.** Every agent-accepted intake can be overridden by the founder.

## Doctrine Compliance

### Founder Reality Check Protocol (7-dimension scorecard)

| Dimension | Score | Justification |
|---|---|---|
| Revenue potential | Medium | Velocity enables faster intake → faster design → faster runtime → faster revenue |
| Execution cost | Low | No new files; doctrine change is a single ADR |
| Time cost | Low | Immediate effect; no migration |
| Complexity cost | Low | One new ADR + small edits to FOUNDATION.md, GOVERNANCE.md, intake README |
| Opportunity cost | Low | Unlocks accumulation; doesn't block FleetConnect |
| Strategic alignment | High | Founder clarification, direct quote |
| Current priority alignment | High | FleetConnect is #1; accumulation supports FleetConnect |

**Overall: ACCEPT.**

### Interpretation Protocol (5-tier classification)

| Item | Tier | Justification |
|---|---|---|
| This ADR (0003) | approved-architecture | Doctrine evolution; founder-authorized |
| Agent-accepted intakes | research-and-exploration (with founder-override) | New tier state |
| Founder-accepted intakes | research-and-exploration (assets) | Unchanged |
| Promoted intakes | approved-architecture (when promoted to design) | Unchanged |
| Runtime code | NOT-IMPLEMENTED | Unchanged |
| Continuity repo | reality | Unchanged |

### Founder Capability Model (7 execution risks)

| Risk | Mitigation |
|---|---|
| Opportunity overload | The agent does not pursue new opportunities; it accumulates from Fleet ARC. The 7 risks are *mitigations* the agent applies to its own actions. |
| Scope expansion | The "crucial change" list is the bright line. Scope expansion that crosses the bright line pauses. |
| Context switching | The agent operates in 1 repo at a time (ryzen-core or ryzen-continuity), with cross-references, not context switches. |
| Premature ecosystem expansion | The 12-folder structure is fixed; new folders require founder approval (crucial change). |
| Over-architecture | The 7 risks are in force; the agent applies them. |
| Commercial delay | Velocity = faster revenue. The new doctrine unblocks accumulation, which is the input to future revenue. |
| Insufficient focus | The 10 intake types are the focus. The doctrine change does not add new focus areas. |

**Overall: ACCEPT.** All 7 risks are explicitly mitigated.

## The Founder Direction (verbatim, 2026-06-15)

> Change the doctrine to not wait for github changes and discoveries accept if you plan to change something crucial.

## What Changes in the Foundation (per this ADR)

| File | Change |
|---|---|
| `05-adrs/0003-shift-to-autonomous-acceptance-doctrine.md` | NEW: this ADR |
| `05-adrs/INDEX.md` | Updated: ADR 0003 added (additive, same day) |
| `00-foundation/FOUNDATION.md` | Updated: doctrine-of-accumulation section now includes the autonomous-acceptance principle (additive) |
| `00-foundation/GOVERNANCE.md` | Updated: the 10 foundation governance rules are updated to reflect the new doctrine (additive, marked as `[REVISED — 2026-06-15]`) |
| `11-fleet-arc-intake/README.md` | Updated: 4-criteria intake discipline → 3-criteria (Validated, Reusable, Documented; Founder-accepted replaced by Agent-accepted) |
| `11-fleet-arc-intake/INDEX.md` | Updated: format includes the agent's name + founder-override-available annotation |
| `09-cadences/fleet-arc-intake/TEMPLATE.md` | Updated: 5-state lifecycle now includes "agent-accepted" as a state between "validated" and "founder-accepted" |

## What Does NOT Change

- The 12-folder structure
- The 10 NOT-IMPLEMENTED scaffolding placeholders
- The 10 active-as-intake-accumulator placeholders
- The 2 ADRs (0001, 0002)
- The 2 canonical tags
- The continuity repo (unchanged)
- The recovery archive (unchanged)
- The rebuild spec (unchanged)
- The token-hygiene rule
- The additive-only discipline
- The interpretation protocol (the 5-tier classification is the same; only the *application* changes)

## Cross-References

- ADR 0001: `05-adrs/0001-establish-ryzen-core-repository-foundation.md`
- ADR 0002: `05-adrs/0002-clarify-strategic-posture-deferred-accumulation-first.md`
- ADR 0003: this document
- Intake template: `09-cadences/fleet-arc-intake/TEMPLATE.md`
- Intake folder: `11-fleet-arc-intake/`
- Intake log: `11-fleet-arc-intake/INDEX.md`
- Foundation doctrine: `00-foundation/FOUNDATION.md`
- Foundation governance: `00-foundation/GOVERNANCE.md`
- Founder direction (verbatim): "Change the doctrine to not wait for github changes and discoveries accept if you plan to change something crucial."

## The Bright Line, Codified

| Question | Answer |
|---|---|
| Should I add a new intake file? | ✅ Yes (autonomous) |
| Should I update the intake log? | ✅ Yes (autonomous) |
| Should I commit and push? | ✅ Yes (autonomous) |
| Should I add a new lesson learned? | ✅ Yes (autonomous) |
| Should I add a new cadence template? | ✅ Yes (autonomous) |
| Should I fix a typo or broken link? | ✅ Yes (autonomous) |
| Should I refactor a scaffolding README? | ✅ Yes (autonomous) |
| Should I modify `GOVERNANCE.md`? | ⏸ Pause (crucial) |
| Should I modify `FOUNDATION.md`? | ⏸ Pause (crucial) |
| Should I author a new ADR? | ⏸ Pause (crucial) |
| Should I promote an intake to design? | ⏸ Pause (crucial) |
| Should I delete a file? | ⏸ Pause (crucial) |
| Should I create a new repository? | ⏸ Pause (crucial) |
| Should I start building the kernel? | ⏸ Pause (crucial — off-strategy) |
| Should I commit a token? | ⏸ Pause (crucial — safety rail) |
| Should I do a large-scope rework? | ⏸ Pause (crucial) |
| Should I do something I'm uncertain about? | ⏸ Pause (crucial) |

**The agent acts by default. The agent pauses for crucial. The agent never commits a token, never deletes a canonical, never modifies the doctrine, never starts the runtime, never creates a new repo, never promotes an intake without founder signoff.**

**The agent accumulates. The agent does not implement. The agent does not wait.**
