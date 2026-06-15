# Founder Capability Map (this repository → canonical)

```yaml
---
type: founder-integration
section: founder-capability-map
version: 1.0
status: foundation-only
created: 2026-06-15
classification: approved-architecture
canonical_ref: Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-CAPABILITY-MODEL.md
amendable: true-additively
```

## Purpose

This document is a **map** from this repository (`ryzen-core`) to the canonical Founder Capability Model v1.0 in the `ryzen-continuity` repository. It captures *which canonical capability facts* are relevant to this implementation-successor repository, and *how* this repository operationalizes them.

**The Founder Capability Model v1.0 is the source of truth.** This map is a *navigation aid*. When this map disagrees with the canonical, the canonical wins.

## The 22 Capability Domains (relevant subset)

The canonical Founder Capability Model v1.0 codifies 22 high-value capability domains. The following domains are *directly relevant* to the implementation of the Ryzen Core runtime:

| # | Domain | Relevance to this repository |
|---|---|---|
| 1 | **AI Augmentation** | The runtime itself is the AI augmentation substrate. `07-runtime-scaffolding/` is the future home. |
| 2 | **Automation** | The cadence templates (`09-cadences/`) and tools (`10-tools/`) are the automation substrate. |
| 3 | **Knowledge Management** | The recovery archive integration (`03-recovery-integration/`) and the rebuild spec integration (`04-rebuild-integration/`) are the knowledge management substrate. |
| 4 | **Systems Architecture** | The 11-folder structure is the system architecture. The 4-phase rebuild sequence is the architectural roadmap. |
| 5 | **Executive Function** | The 7 execution risks (in `00-foundation/FOUNDATION.md`) and the Founder Reality Check Protocol (applied via ADRs) are the executive function substrate. |
| 6 | **Operations** | The cadence templates and the runtime roadmap are the operations substrate. |
| 7 | **Continuity** | The Recovery Archive integration and the rebuild spec integration are the continuity substrate. |
| 8 | **Decision-Making** | The ADR system (`05-adrs/`) is the decision-making substrate. |
| 9 | **Risk Management** | The 7 execution risks and the Founder Reality Check Protocol are the risk management substrate. |
| 10 | **Strategic Planning** | The 4-phase rebuild sequence and the runtime roadmap are the strategic planning substrate. |
| 11 | **Capability Design** | The 11-folder structure and the scaffolding placeholders are the capability design substrate. |
| 12 | **Process Design** | The cadence templates (daily/weekly/monthly) are the process design substrate. |
| 13 | **Tool Mastery** | The 10-tools folder and the integration with the continuity repo are the tool mastery substrate. |
| 14 | **Pattern Recognition** | The 8 reusable concepts (in the recovery archive) and their mapping to the scaffolding are the pattern recognition substrate. |
| 15 | **Architectural Thinking** | The 4-phase rebuild sequence and the 11-folder structure are the architectural thinking substrate. |
| 16 | **Substrate Design** | `07-runtime-scaffolding/` (the runtime substrate) and `08-observability/` (the observability substrate) are the substrate design homes. |
| 17 | **Governance Design** | `00-foundation/GOVERNANCE.md` (the 10 foundation governance rules) is the governance design. |
| 18 | **Memory Architecture** | The recovery archive (in continuity) and the integration map (`03-recovery-integration/`) are the memory architecture substrate. |
| 19 | **Cognition Engineering** | The recovery archive's "CognitionLoop" reference and the rebuild spec's "C1 — The 5-stage Cognition Loop pattern" are the cognition engineering references. |
| 20 | **Execution Discipline** | The 11-folder structure (one folder = one purpose) and the commit doctrine (one artifact class per commit) are the execution discipline substrate. |
| 21 | **Asset Compounding** | The 4-phase rebuild sequence (R1 → R2 → R3 → R4) compounds the runtime asset over time. Each phase is a *durable asset*. |
| 22 | **Leverage Engineering** | The 4-phase rebuild sequence and the integration with the continuity repo are the leverage engineering substrate. The runtime is *leverage* — it amplifies the founder's capacity, not replaces it. |

**The other 10 capability domains** (from the canonical's 22) are not directly relevant to the runtime foundation. They may be relevant to other repos in the ecosystem (e.g., Earth, FamilieKompas) but not to `ryzen-core`.

## The 9 Cognitive Advantages (relevant subset)

The canonical Founder Capability Model v1.0 codifies 9 cognitive advantages. The following advantages are *directly leveraged* by this repository:

| # | Advantage | How this repository leverages it |
|---|---|---|
| 1 | **Cross-domain synthesis** | The 11-folder structure is the cross-domain synthesis — foundation + founder + ryzen + recovery + rebuild + ADRs + roadmap + scaffolding + observability + cadences + tools. |
| 2 | **First-principles decomposition** | The 4-phase rebuild sequence decomposes the runtime into substrate → governance → execution → multi-ARC. |
| 3 | **Systems-level thinking** | The 11-folder structure is the system. The 4-phase rebuild sequence is the system evolution. The cadence is the system rhythm. |
| 4 | **Architectural intuition** | The 11-folder structure is the architectural intuition. The kebab-case + zero-padded prefix pattern is the architectural intuition. |
| 5 | **Pattern recognition** | The 8 reusable concepts (in the recovery archive) are the patterns this repository recognizes. The 19-step build sequence is the pattern. The 4-phase rebuild sequence is the pattern. |
| 6 | **Strategic patience** | The foundation exists *before* the runtime. The runtime is *not* built at the foundation stage. This is strategic patience. |
| 7 | **Compounding leverage** | The 4-phase rebuild sequence compounds the runtime asset over time. The cadence compounds the operational learning over time. |
| 8 | **Founder-Architect stance** | The repository is designed for the founder, not for general users. The 11-folder structure is the founder's workspace, not a public product. |
| 9 | **Identity + Capability = Sibling canonicals** | The founder's own doctrine (Identity + Capability as siblings) is mirrored in this folder (`01-founder/FOUNDER-IDENTITY-MAP.md` + `01-founder/CAPABILITY-MAP.md`). |

## The Learning Model (Learn → Connect → Integrate → Operationalize → Scale)

The canonical Founder Capability Model codifies the founder's learning model:

1. **Learn** — acquire new information (the recovery archive, the rebuild spec, the founder's canonicals).
2. **Connect** — link the new information to existing knowledge (the 8 reusable concepts ↔ the 11-folder structure).
3. **Integrate** — make the connections part of the operating system (the integration maps in `01-founder/`, `02-ryzen/`, `03-recovery-integration/`, `04-rebuild-integration/`).
4. **Operationalize** — turn the integrated knowledge into a runnable system (R1 of the rebuild).
5. **Scale** — extend the system to new domains (R4 multi-ARC foundations, then beyond).

**How this repository honors the learning model:** The foundation is **stages 1–3** of the model. Stages 4 and 5 happen in R1+ of the rebuild. **The foundation is the integration stage; the runtime is the operationalization stage.**

## The 7 Execution Risks (operationalized as foundation guards)

The 7 execution risks from the canonical Founder Capability Model v1.0 are *re-stated* in `00-foundation/FOUNDATION.md` §"The 7 Execution Risks" and *operationalized* as 7 foundation guards. This document is consistent with that section.

## The Founder Reality Check Protocol (operationalized via ADRs)

The canonical Founder Capability Model v1.0 codifies the **Founder Reality Check Protocol** as a 7-dimension scorecard that must be **executed** (not just cited) before any new idea is pursued.

**How this repository operationalizes the Reality Check Protocol:** Every architectural decision in this repository is captured as an **ADR** in `05-adrs/`. Each ADR includes the 7-dimension scorecard as a check before the ADR is accepted. The first ADR (`0001-foundation-establishment.md`) demonstrates this pattern.

## The Executive Amplification Directive (operationalized as the 11-folder chain)

The canonical Founder Capability Model v1.0 codifies the Executive Amplification Directive: **Ideas → Plans → Systems → Operations → Revenue → Durable Assets**.

**How this repository operationalizes the Executive Amplification Directive:** The 11-folder structure is the chain:
- `02-ryzen/` = the System (the design)
- `04-rebuild-integration/` = the Plan (the rebuild spec integration)
- `06-runtime-roadmap/` = the Operations (the 4-phase rebuild sequence)
- `07-runtime-scaffolding/` = the future Revenue (R1–R4 will produce the revenue-producing runtime)
- `00-foundation/` + `09-cadences/` + `10-tools/` = the Durable Assets

The chain is *complete*: every folder serves one or more stages of the chain. No folder is a "loose end."

## What This Map Does NOT Do

This map does **not**:

- ❌ Duplicate the canonical Founder Capability Model. The canonical is in continuity.
- ❌ Add new capability domains that are not in the canonical.
- ❌ Add new cognitive advantages that are not in the canonical.
- ❌ Re-classify the canonical as "draft" or "superseded."

The map is **observational**, not **additive**. It maps; it does not extend.

## Cross-References

- `01-founder/FOUNDER-IDENTITY-MAP.md` — the sibling map to the canonical Identity
- `00-foundation/FOUNDATION.md` — the foundation doctrine (which references the founder's execution risks)
- `05-adrs/` — Architectural Decision Records (this repo)
- Canonical Founder Capability Model: `Javalin13/ryzen-continuity/blob/main/01-founder/CANONICAL-FOUNDER-CAPABILITY-MODEL.md`
