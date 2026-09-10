# ARC A→Z Alignment Map — 2026-09-10

```yaml
---
type: cross-repo-alignment-map
status: founder-directed-current-reference
created: 2026-09-10
classification: current-reality + approved-architecture + commercial-operating-model
scope: RYZ3N Core + PRIME stewardship + VONDA reference ARC + ARC commercialization
amendable: true-additively
runtime_implementation_authorized: bounded-current-mission-only
---
```

## 1. Purpose

This is the current A→Z reading map for ARC work. It prevents historical migration notes, prototype implementation details, commercial experiments and canonical RYZ3N doctrine from being mistaken for one another.

The system must be read in this order:

1. **Founder authority and canonical RYZ3N doctrine** define what the ecosystem is.
2. **Current-reality overlays** define what is actually proven now.
3. **ARC productization standards** define the reusable product/runtime contracts.
4. **VONDA** supplies reference-ARC implementation evidence and the frozen Golden ARC Blueprint.
5. **PRIME** operates/stewards the current prototype and reports evidence; it does not become the canonical parent of ARCs.
6. **Commercialization doctrine** defines how the product is sold, measured and scaled without changing maturity, privacy or architecture rules.

Historical files remain evidence of prior state. They do not override a later Founder-directed current standard merely because they still exist in Git history.

---

## 2. Canonical hierarchy — invariant

```text
Creator
  ↓
RYZ3N
  ↓
ARCs
  ↓
Brains
  ↓
Agents
  ↓
Execution
```

Current project spelling is **RYZ3N**. Legacy canon may use `Ryzen`; this is a naming evolution, not an architectural change.

PRIME is not inserted into this canonical hierarchy.

Current prototype/steward view may be expressed operationally as:

```text
Founder / Owner
  ↓ intent and authority
PRIME steward / current prototype operator
  ↓
ARC runtime instance
  ↓
Domain / Project → Intent → Activity → Brain → Agents / Tools → Execution
  ↑ evidence / continuation
```

That is an implementation/steward view only.

---

## 3. Authority and decision boundaries

### Founder

The Founder owns final product direction, pricing, commercial promises, strategic priorities, maturity doctrine, risk acceptance and major launch decisions.

### RYZ3N

RYZ3N is the canonical ecosystem and future native layer for ARC registry, provisioning, governance, orchestration, verification, observability, continuity and cross-ARC convergence.

### PRIME

PRIME is the current high-agency execution/operator/steward layer. PRIME may implement approved patterns, provision bounded ARC instances, monitor runtime/capacity, verify evidence and surface risk. PRIME may not silently redefine RYZ3N, pricing, privacy, maturity or Founder strategy.

### Luxcalibur

Lux is the independent second-line strategy/architecture/product reviewer and bridge counterpart. Lux cross-checks evidence, benchmarks the market, converts Founder decisions into durable doctrine/directives and detects drift. Lux is not a canonical hierarchy tier and is not a customer ARC.

### Customer ARC

Each ARC serves its Owner inside explicit permissions. It owns its isolated identity/state boundary and must never expose another ARC's private payload.

---

## 4. Reference implementation status

**VONDA ARC is ARC #1 and the reference/tutorial proving node.**

As of 2026-09-10, the following are evidence-backed:

- isolated VONDA Hermes runtime/profile and gateway pattern;
- fail-closed unknown-user / pending-candidate approval pattern;
- Founder/test-user isolation from the future primary user;
- task persistence and bounded operational tools;
- onboarding state-machine implementation and V1 release preparation;
- ARC↔PRIME steward/event patterns;
- privacy-safe per-ARC model-capacity telemetry;
- real live model request/latency/token observations;
- separation of simulated and real telemetry evidence;
- model-capacity pool attribution;
- frozen reusable `arc/GOLDEN-ARC-BLUEPRINT.md` in `Javalin13/VONDA-Corporation`.

`VONDA_CAPACITY_TELEMETRY = GREEN` is closed. Do not reopen it without regression evidence.

The **full** `VONDA_REFERENCE_ARC_COMPLETE` gate remains dependent on external reality: Laetitia's real first contact, operator-approved binding, onboarding, a real operational work cycle, later persistence/Brain reuse, a material steward event and a first real primary-user consumption baseline.

Do not manufacture replacement test gates while waiting for this real-user evidence.

---

## 5. Golden ARC Blueprint role

The Golden ARC Blueprint is the current reusable engineering contract for future ARC replication.

It captures patterns, not customer payload.

Every inheriting ARC must receive its own:

- `arc_id`;
- identity and owner/user binding;
- isolated profile/runtime/gateway;
- memory/tasks/Brain state boundary;
- secrets and permissions;
- channel routing;
- health/recovery/checkpoint state;
- ARC↔PRIME steward/event interface while PRIME remains operator;
- model-capacity-pool assignment;
- privacy-safe consumption telemetry;
- maturity/evidence state;
- form/aura/transfer-reset lifecycle state.

VONDA private memory, Laetitia private payload, credentials and VONDA-confidential corporate content must never become template material.

The blueprint is not proof that bulk provisioning is already automated or that ARC #2+ has been operationally replicated. Those remain later evidence gates.

---

## 6. Product identity

Customer-facing ARC positioning is:

> **ARC — Your AI operating partner. It grows with you.**

A useful campaign shorthand is:

> **Your first AI employee. You talk. Your ARC works.**

Do not lead with Hermes, Ollama, VPSs, Telegram setup or API-key management. Those are implementation details.

The commercial product is the managed whole: isolated owner-specific runtime, continuity, authorized memory, useful execution, progressive Brains/capabilities, infrastructure stewardship, predictable billing, privacy boundaries and verified maturity.

Do not claim ARC is the only AI assistant or only managed Hermes offer. The differentiation is the integrated ARC product system and its lifecycle/governance model.

---

## 7. Initial customer and launch sequence

Initial ideal customer:

> **Solo entrepreneur / starting entrepreneur / very small business owner who values AI but does not want to become an AI infrastructure engineer.**

Current launch sequence:

```text
VONDA reference proof
  ↓
Founding 20 paid validation cohort
  ↓
repeatable onboarding + unit economics + retained usage
  ↓
permissioned proof / testimonials / use cases
  ↓
organic demonstrations
  ↓
small paid acquisition experiments
  ↓
scale only when retention, support, capacity and economics prove it
```

Do not use broad ad spend to compensate for an unproven onboarding or retention loop.

---

## 8. Pricing — current commercial truth

### Founding 20

**€49/month**, founding rate locked while continuously subscribed, subject to Standard scope/fair-use boundaries.

This is a paid validation cohort, not the permanent Standard list price and not a mass-market unlimited plan.

### Standard

**€50/month or €500/year.**

### Higher working tiers

Current working hypotheses remain:

- Pro: €120/month or €1,200/year;
- Business: €250/month or €2,500/year;
- Dedicated: from €5,000/year;
- Enterprise: custom, current working floor around €10,000/year.

Higher tiers remain market hypotheses until validated.

Any older €550/year or €600/year Standard figure is superseded by the current Founder-directed `€500/year or €50/month` pricing standard.

VONDA's exceptional founding-pilot terms are reference-pilot terms and do not automatically apply to Founding 20 customers.

---

## 9. Billing tier ≠ maturity tier

Never conflate what a customer pays with what an ARC has actually earned.

**Billing tier** controls commercial scope, support, integrations, capacity and infrastructure.

**Maturity tier** represents verified capability/evidence:

```text
V1 Foundation        → Blue
V2 Operations        → Cyan / Electric Blue
V3 Specialist        → Violet / Amethyst
V4 Golden ARC        → Gold
V5 Platinum Presence → Platinum
V6 Sovereign         → Sovereign / Prismatic
```

A customer cannot simply purchase a false Gold/Platinum aura. A higher commercial tier may fund capabilities that make maturity easier to achieve, but the maturity gate remains evidence-based.

---

## 10. Form / aura / transfer lifecycle

Core invariant:

> **Form is Owner-resettable. Aura is maturity-derived.**

A cosmetic factory reset of the ARC's look/form does not alter maturity, competence, evidence or aura.

Example:

`V4 + factory-form reset → V4 + Gold aura`

Sale/transfer alone does not automatically force V1.

If ownership transfer includes a genuine reset/removal of the owner-specific state, competence and evidence that supported prior maturity, leaving the ARC effectively empty for the new Owner:

`transferred + genuinely emptied ARC → V1 Foundation → Blue aura`

Private previous-Owner identity, memory, secrets, permissions and payload do not pass to the new Owner by default.

---

## 11. Privacy and capability federation

Network value comes from reusable generalized capability, not private-memory sharing.

> **Share capability, not private payload. Reuse intelligence patterns, not another Owner's memory.**

Reusable module/Brain/Agent/workflow contracts may be promoted after evidence review. Client-private payload remains in the owning ARC boundary unless explicitly authorized under a valid data-sharing purpose.

---

## 12. Usage promise and fair use

Standard customer promise:

> **One predictable subscription with standard AI usage included. No API keys to manage and no surprise pass-through model bill.**

Do not sell `unlimited AI`.

Standard excludes structurally heavy or bespoke workloads such as continuous bulk generation, high-frequency autonomous jobs, unlimited custom integrations, dedicated model capacity, unlimited human support or business-critical 24/7 SLA.

When an ARC becomes materially heavy:

1. optimize the workflow;
2. reassign/split model capacity where appropriate;
3. move it to Pro/Dedicated where justified;
4. or agree a clearly priced capacity/usage arrangement before billing changes.

Never silently pass an unexpected provider overage to a Standard customer.

---

## 13. Capacity doctrine

Founder safety ceiling:

> **Maximum 10 Standard ARCs per Ollama/Hermes model-capacity pool until production telemetry proves another ceiling preserves service quality.**

This is an operating safety/commercial ceiling, not a technical claim that the provider can only run 10 ARCs.

Split earlier when real telemetry shows recurring throttling, rate limits, retries, latency degradation, concurrency pressure, provider quota/headroom risk, incidents or disproportionate use from one ARC.

Each ARC needs per-ARC attribution and a migration/reassignment path that does not change ARC identity/memory contracts.

The ceiling may be lowered immediately for reliability. It may only be raised from real evidence.

---

## 14. Evidence still required before scale

The current architecture is promising but these scale claims are **not yet proven**:

- bulk automated provisioning for ARC #2+;
- safe real multi-ARC VPS process density at meaningful concurrency;
- real-world capacity behavior with 5–10 simultaneously active Standard ARCs;
- 30/60/90-day retention for paid external entrepreneurs;
- support minutes/intervention burden at cohort scale;
- actual CAC and payback from paid acquisition;
- reliable fully loaded contribution margin;
- mature customer-success/support operations;
- production legal/privacy/compliance package for broad public scale.

Do not market these as solved merely because the blueprint exists.

---

## 15. Scale gates

Broad paid acquisition should wait until the product machine is credible. Before materially scaling ads, require approximately:

- 10+ genuinely paying non-Founder users, preferably approaching Founding 20;
- repeatable provisioning/onboarding;
- fast time-to-first-value;
- credible early retention;
- healthy privacy/isolation evidence;
- healthy model-capacity telemetry;
- manageable support burden;
- at least 3 strong repeatable entrepreneur use cases;
- permissioned proof/testimonials;
- measured unit economics good enough to set a rational CAC ceiling.

Clicks are not success. Retained paying customers are success.

---

## 16. Team operating model

### 0–20 paid ARCs

Founder leads early sales, customer discovery, commercial decisions and enough onboarding to directly learn the product. PRIME handles approved technical provisioning, runtime, isolation, telemetry and recovery. Lux performs independent product/architecture/market review and bridge cross-checking.

### ~20–50 paid ARCs

Add/assign customer-success/onboarding capacity when recurring support begins stealing Founder time from sales/product direction. Automate repeated provisioning before hiring people to perform avoidable manual steps.

### ~50–100 paid ARCs

Separate support/operations from Founder sales/product work. Formalize billing, incident handling, onboarding, service boundaries and capacity planning.

### 100+ paid ARCs

Operate as a subscription platform with explicit operational ownership, stronger security/compliance, segment/pool capacity planning, structured growth experimentation and SLAs where sold.

Evidence of workload overrides vanity headcount targets.

---

## 17. Founder ↔ PRIME ↔ Lux communication

Founder is not a human clipboard.

For VONDA/current ARC bridge rounds:

```text
PRIME executes
  ↓
PRIME writes detailed evidence to FROM_PRIME.md and pushes
  ↓
PRIME sends Founder only a mini report
  ↓
Founder tells Lux: "sync"
  ↓
Lux independently reads/cross-checks current bridge + repo evidence
  ↓
Lux writes/pushes TO_PRIME.md
  ↓
Founder tells PRIME: "consume"
  ↓
PRIME consumes and executes
```

Detailed engineering exchange belongs on the bridge. Founder receives the command view.

---

## 18. Current priority order

1. Preserve VONDA reference ARC in ready state and wait for the real primary-user cycle; do not manufacture new VONDA gates.
2. Prepare commercial launch assets and a repeatable provisioning/onboarding checklist from the Golden ARC Blueprint.
3. When Founder recruits a Founding customer, instantiate deliberately from the blueprint and record real provisioning/support/capacity evidence.
4. Use early paying customers to validate repeatability, retention, economics and support burden.
5. Automate what repeats.
6. Scale distribution only after evidence.
7. Continue feeding reusable proof back into RYZ3N Core so eventual native RYZ3N orchestration inherits proven reality rather than speculative complexity.

Do **not** spawn 20 ARCs just because the cohort is called Founding 20. Provision only real authorized customers.

---

## 19. Anti-drift / supersession rules

Current files supersede older conflicting operational statements as follows:

| Topic | Current authority | Older conflicting wording treatment |
|---|---|---|
| Canonical hierarchy | RYZ3N canon + `PRIME-RYZ3N-ARC-PROTOTYPE-DOCTRINE.md` | PRIME prototype diagrams do not redefine canon |
| September reality | `CURRENT-REALITY-2026-09.md` + this map | June “no implementation today” text is historical context |
| Standard pricing | `PRICING.md` | €550/€600 old figures superseded |
| Founding 20 | `ARC-COMMERCIALIZATION-LAUNCH-AND-OPERATING-PLAN.md` | VONDA exceptional free pilot is not cohort default |
| Usage/capacity | `COST-CAPACITY-MODEL.md` + Golden Blueprint | no unlimited-usage assumption |
| Maturity/aura | `ARC-V1-V6-COMMERCIAL-MATURITY-TUTORIAL.md` | billing level does not create aura |
| Form/transfer reset | `ARC-FORM-AURA-AND-TRANSFER-RESET-STANDARD.md` | cosmetic reset cannot reset/recolor aura |
| PRIME↔Lux bridge | active VONDA `arc/bridge/SYNC_PROTOCOL.md` + current PRIME comms | old “deferred/post-cutover” bridge text is superseded |

---

## 20. Definition of aligned

The ecosystem is A→Z aligned when the same proposition remains true from strategy through runtime through sales:

> **RYZ3N is the canonical ecosystem. PRIME currently proves and stewards reusable ARC operations. Each ARC is isolated and Owner-specific. The Golden Blueprint captures reusable engineering without customer payload. ARC is sold as a managed AI operating partner with predictable included Standard usage. Maturity is earned, aura reflects maturity, form is independently resettable, capacity is measured before scale, and commercial growth follows evidence rather than hype.**

Any implementation, sales claim, pricing exception, new Brain, new ARC, marketing experiment or infrastructure change that contradicts that proposition must be surfaced as drift and corrected or explicitly re-authorized by the Founder.