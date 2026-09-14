# Temporal Coherence & Evidence Freshness for Reliable Excellence

**Status:** Strategic Capability / Future Reliability Skill  
**Constitution/Canon impact:** none — deepens existing continuity, provenance and source-freshness requirements

## Purpose

Temporal Coherence is the capability to reason correctly about **when** a fact, state, decision, capability, configuration or piece of evidence was valid, what has changed since, and which newer evidence supersedes older evidence.

RYZ3N already requires continuity, evidence freshness, source freshness, historical/current distinction and truthful state. This capability turns those existing requirements into a deliberate cognitive skill.

## Core rule

> **A statement can have been true and still be false now. Historical truth must never silently become current truth.**

A reliable system should be able to distinguish:

- historical state;
- last-known state;
- current observed state;
- current unverified state;
- superseded state;
- future planned state;
- predicted state;
- expired/stale evidence;
- unknown state after an interruption or evidence gap.

## Reliability role

A mature ARC should be able to:

- determine whether evidence remains fresh enough for the claim being made;
- reconstruct the sequence of material changes rather than collapsing them into one summary;
- identify which decision or evidence superseded an older one;
- prevent old GREEN/proven states from masking present degradation;
- detect when a source was recently modified but the relevant content is still old;
- distinguish deployment time, observation time, event time and report time where material;
- reconcile interrupted missions after restart using the newest authoritative state;
- carry temporal context through memory, Brain handoffs and evidence chains;
- require fresh proof when risk or elapsed time makes old proof insufficient.

## Freshness is claim-dependent

Evidence does not have one universal expiration period.

Examples:

- a constitutional Founder decision may remain valid until amended;
- a repository HEAD must be re-read before a concurrent write;
- runtime health can become stale within seconds or minutes;
- a recovery drill may remain useful evidence longer but cannot prove present runtime health forever;
- a maturity claim may require sustained evidence over time rather than one point-in-time success.

Therefore freshness must be evaluated against the **claim, consequence and volatility of the underlying state**.

## Relationship to existing architecture

This capability strengthens existing mechanisms:

- OMEGA already distinguishes historical evidence from current evidence.
- Reliable Excellence requires evidence freshness and truthful current reporting.
- Enhancement Propagation requires source-freshness checks before changes.
- Mission control uses durable checkpoints and current authoritative source revisions.
- FACTORY preserves provenance/history rather than overwriting it.
- Memory Federation provides continuity substrate but must not flatten time.

Temporal Coherence is the reasoning skill that helps those mechanisms answer: **which state is authoritative now, and why?**

## Failure modes to prevent

- stale GREEN state;
- old configuration treated as current deployment truth;
- historical success used as proof of current reliability;
- planned work reported as implemented;
- recently copied old documents treated as new because metadata is recent;
- restart recovery from a stale checkpoint while newer state exists;
- conflicting timelines silently merged;
- evidence without event/observation time;
- superseded policy continuing to route decisions.

## Verification targets

Future evidence may include:

- stale-state detection precision/recall;
- correct supersession resolution;
- correct reconstruction after interrupted missions;
- rate of historical/current state confusion;
- source-freshness violations caught before writes;
- percentage of material evidence carrying sufficient temporal metadata;
- false GREEN prevention attributable to freshness checks;
- correct re-verification triggers after material elapsed time or change.

## OMEGA / FACTORY relationship

OMEGA should challenge claims whose proof is too old, temporally ambiguous or contradicted by newer evidence.

FACTORY should increasingly build temporal integrity in through timestamps, revision pointers, evidence freshness policies, supersession fields, current-state checks and re-verification triggers appropriate to each ARC capability.

## Governing principle

> **Reliability is not only knowing what is true. It is knowing what is true now, what used to be true, what changed, and what evidence justifies the transition.**
