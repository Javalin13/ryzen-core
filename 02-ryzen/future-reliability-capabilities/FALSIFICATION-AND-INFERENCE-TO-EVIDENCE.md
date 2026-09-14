# Falsification & Inference-to-Evidence for Reliable Excellence

**Status:** Strategic Capability / Future Reliability Skill  
**Constitution/Canon impact:** none — complements existing Recursive Verification and adversarial validation

## Purpose

Falsification & Inference-to-Evidence is the capability to take a model-generated inference, heuristic hypothesis, diagnosis or architectural belief and determine **what evidence would most efficiently prove it wrong, prove it insufficient, or strengthen it enough for the relevant decision**.

The existing RYZ3N architecture already owns verification, critique, validation, adversarial failure simulation and evidence gates. This capability does not duplicate those mechanisms. It improves the cognitive step **between inference and verification**.

## Core rule

> **When intelligence proposes X, the next reliability question is not only “Why might X be right?” but “What observation would show X is wrong?”**

## Reliability role

A mature ARC should be able to:

- translate a plausible explanation into testable claims;
- identify the highest-information next test;
- search for disconfirming evidence rather than only supporting evidence;
- distinguish a test of the real hypothesis from a convenient proxy;
- choose independent evidence where correlated evidence could create false confidence;
- identify assumptions that must be tested separately;
- stop spending verification effort once evidence is sufficient for the consequence level;
- escalate when decisive evidence cannot be obtained safely;
- preserve failed hypotheses as useful reliability memory rather than hiding them.

## Reference loop

`observation → inference / hypothesis → predicted consequences → discriminating test → evidence → falsify / weaken / strengthen → Recursive Verification → bounded action → outcome verification`

This loop feeds the existing verification substrate. It is not a replacement for it.

## Minimum decisive evidence

Reliable verification should seek the **smallest evidence set that can materially discriminate between competing explanations**, while increasing the evidence burden for higher-consequence actions.

Examples:

- If a runtime appears healthy because a process exists, test functional behavior rather than collecting more process listings.
- If a deployment is claimed successful, verify the running version and intended external behavior rather than relying on upload success.
- If two models agree, ask whether they relied on the same source or assumption before treating that agreement as independent support.
- If an actuator command was issued, verify physical outcome rather than treating command acknowledgement as success.

## Evidence independence

Multiple pieces of evidence do not necessarily provide multiple independent reasons for belief.

A mature system should consider:

- shared source dependence;
- copied or derived evidence;
- common model/provider failure modes;
- common sensor failure modes;
- shared configuration or deployment assumptions;
- whether two tests actually exercise different failure paths.

This strengthens the existing **Redundancy Reasoning** capability without creating a separate evidence layer.

## Relationship to existing architecture

- Heuristic Reasoning generates provisional likely paths.
- Layer 19 adversarial validation searches failure paths and dangerous assumptions.
- Recursive Verification critiques and validates candidate outputs before execution.
- Constitution Compliance requires evidence before claims become reality.
- Mission control owns objective acceptance gates and completion truth.
- OMEGA evaluates whether evidence really supports lifecycle and reliability claims.
- FACTORY converts recurring falsified assumptions into reusable prevention controls.

## Failure modes to prevent

- confirmation-only testing;
- collecting many weak pieces of evidence instead of one decisive test;
- circular validation where output validates itself;
- correlated evidence mistaken for independent confirmation;
- proxy metrics treated as outcome proof;
- tests that cannot fail by design;
- moving acceptance criteria after a hypothesis fails;
- endless verification without consequence-sensitive stopping rules;
- discarding failed hypotheses and rediscovering them later.

## Verification targets

Future evidence may include:

- time-to-disconfirm incorrect hypotheses;
- information gained per diagnostic/test action;
- percentage of material hypotheses with explicit falsification criteria;
- confirmation-bias error rate;
- correlated-evidence failures detected;
- false-positive closure prevented by discriminating tests;
- verification cost versus defect-detection value;
- reduction in recurring wrong diagnoses after failed hypotheses are retained.

## OMEGA / FACTORY relationship

OMEGA should challenge evidence packages that are circular, correlated, proxy-only or incapable of disproving the claim.

FACTORY should encode recurring decisive tests, negative tests and falsification conditions into reusable production gates so future ARCs do not need to rediscover the same verification logic manually.

## Governing principle

> **Heuristics accelerate the search. Falsification protects the search from believing itself. Verification decides what the evidence justifies.**
