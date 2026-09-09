# ARC Brain Specialization Registry — Runtime/Productization Standard

Date: 2026-09-09
Status: Founder-directed additive architecture
Classification: approved-architecture + evidence-driven runtime guidance

## Purpose

Operationalize the canonical `ARC → Brains → Agents → Execution` structure without inventing Brains before reality justifies them.

A client ARC may develop specialist reasoning domains over time. When a specialization becomes real and useful enough to preserve, the ARC records it as a dedicated Brain under its own GitHub `BRAINS/` tree.

Example shape:

```text
ARC/
└── BRAINS/
    ├── README.md
    ├── COACHING/
    │   ├── README.md
    │   ├── SCOPE.md
    │   ├── MEMORY-CONTRACT.md
    │   ├── AGENTS.md
    │   ├── DECISIONS.md
    │   └── EVIDENCE.md
    └── <future-specialization>/
```

The folder name represents a **reasoning specialization**, not a marketing label and not merely a tool category.

## Canonical rule

The canonical hierarchy remains:

`Creator → RYZ3N → ARCs → Brains → Agents → Execution`

A Brain:
- reasons within the ARC's approved domain framing;
- does not redefine the ARC;
- does not invent Founder strategy;
- does not execute external actions directly when an Agent boundary is required;
- may own specialized memory, policies, decision patterns and Agent contracts.

## Evidence gate for creating a Brain

Do not create a Brain merely because a concept sounds useful.

A Brain folder should be created when at least one of these is true:

1. recurring real use shows a stable reasoning specialization;
2. a distinct body of domain knowledge/memory is accumulating;
3. a distinct decision pattern repeatedly appears;
4. specialized Agents/tools need a clear reasoning owner;
5. Founder explicitly approves a specialization as an architectural unit.

Every new Brain must declare its current reality tier:
- `candidate`
- `prepared`
- `active`
- `validated`
- `deprecated`

## Minimum Brain contract

Each Brain folder should eventually define:

- `README.md` — purpose, status, owner ARC, current evidence;
- `SCOPE.md` — what it reasons about and what it may not decide;
- `MEMORY-CONTRACT.md` — what knowledge/memory it may read/write;
- `AGENTS.md` — execution entities it may delegate to;
- `DECISIONS.md` — local decision trail / supersession;
- `EVIDENCE.md` — real observations/tests showing the Brain is warranted.

For early pilots, only `README.md` is required. Add more files when reality demands them.

## VONDA application

VONDA ARC should maintain:

`VONDA-Corporation/arc/BRAINS/`

Any specialization developed through real use belongs there.

Example:

`arc/BRAINS/COACHING/`

if VONDA develops a stable coaching reasoning specialization through actual client use and/or explicit Founder approval.

The Brain folder is the durable GitHub representation of the specialization. Runtime prompts/config/memory may implement that specialization inside VONDA's autonomous Hermes node, but the GitHub Brain contract is the portable architectural source of truth.

## PRIME role

PRIME may:
- detect recurring specialization patterns;
- propose/create a Brain folder after evidence or Founder approval;
- verify that runtime behavior matches the Brain contract;
- surface drift;
- promote generalized lessons to RYZ3N productization.

PRIME may not silently create an architectural Brain from one-off behavior.

## Replication rule

A validated Brain should be reusable as a template pattern without copying client-private payloads.

Promote:
- reasoning contract;
- workflow pattern;
- agent contract;
- memory schema;
- verification criteria.

Do not promote:
- private conversations;
- personal client data;
- secrets;
- confidential payloads.

## Constitutional check

After a Brain is added or materially changed, run the RYZ3N constitutional three-pass check:

1. Reality — does this specialization actually exist in use/runtime?
2. Implementation — does the implementation match the Brain contract and ARC framing?
3. Evidence — can the claim be proven?

If any pass fails, the Brain must not be reported as validated.
