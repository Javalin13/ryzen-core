# apps/memory-federation/ — NOT IMPLEMENTED

```yaml
---
type: scaffolding
status: NOT-IMPLEMENTED
created: 2026-06-15
implements_concept: C2 (4-layer Memory Model)
rebuild_phase: R1 (basic) + R3 (semantic search)
blocked_by: D2 (semantic memory implementation strategy)
classification: approved-architecture
amendable: true-additively
```

## Status: NOT IMPLEMENTED

This directory is **scaffolded, not implemented**. Per the founder's direction 2026-06-15, no runtime code is written at this stage. The C2 Memory Federation will be added in **R1** (basic 4-layer implementation) and extended in **R3** (semantic search).

## What will go here (in R1 and R3)

This directory will contain the **Memory Federation Layer** — the continuity substrate.

### R1 (Concept C2 — The 4-layer Memory Model)

In R1, this directory will contain:

- `federation.py` — the `MemoryFederationLayer` class
- `layers.py` — the 4 layer definitions: `operational`, `strategic`, `creator`, `governance`
- `storage.py` — the storage backend (PostgreSQL + pgvector, per the recovered evidence)
- `retrieval.py` — the retrieval methods: `store_memory`, `retrieve_by_layer`, `retrieve_recent`, `get_continuity_context`
- `__init__.py` — the package init
- `tests/test_federation.py` — the test suite

The C2 Memory Federation is the *continuity substrate* — it is the system that preserves the founder's operational context, the strategic state, the creator identity, and the governance audit trail across time.

### R3 (Semantic Memory — D2 decision)

In R3, this directory will *extend* with:

- `semantic_search.py` — the real semantic retrieval (replacing the placeholder in R1's `federation.py`)
- `vector_store.py` — the vector store abstraction (pgvector / dedicated vector DB / external service, **depending on D2**)
- `embeddings.py` — the embedding generation
- `tests/test_semantic.py` — the semantic test suite

The R3 extensions are *blocked* by the **D2 founder decision** (semantic memory implementation strategy). Until the founder decides, R1's `federation.py` will have a *placeholder* for `search_semantic`, exactly as the recovered code did.

## The 4-Layer Memory Model (C2)

The C2 concept is a 4-layer memory model:

1. **Operational** — ephemeral, short-term, task-specific memory
2. **Strategic** — durable, long-term, decision-and-pattern memory
3. **Creator** — founder identity, capability, doctrine (immutable)
4. **Governance** — audit trail, immutable, cryptographically signed

The 4 layers are *doctrine*. Any future build *must* support them. The implementation can be different (pgvector, dedicated vector DB, in-memory), but the *abstraction* is preserved.

## The D2 Open Decision

The recovery archive's `OPEN-DECISIONS.md` codifies the **D2 — Semantic Memory Implementation** decision. The 5 options:

| Option | Description | Pros | Cons |
|---|---|---|---|
| **pgvector** (in PostgreSQL) | Use the pgvector extension (already in the dependencies) | Single database, no extra infrastructure, no extra cost | Limited to PostgreSQL, less feature-rich |
| **Dedicated vector database** (Qdrant, Weaviate) | Stand up a separate vector database service | Best-in-class vector search, scalable, filterable | Extra infrastructure, extra cost |
| **External service** (Pinecone, OpenAI Embeddings) | Use a managed vector service | Zero ops, best-in-class features | Vendor lock-in, ongoing cost |
| **In-memory** (FAISS, Annoy) | Use a local vector index in memory | Fast, no extra infrastructure | Doesn't persist, doesn't scale |
| **Pluggable** (provider-agnostic) | A `VectorStore` contract with multiple implementations | Most substrate-adaptive | Most architecture; risk of over-engineering |

**Hermes's recommendation:** Start with pgvector (already in the dependencies, already in the docker-compose). Migrate to a dedicated vector database in R3+ if the data scale or query patterns demand it.

**Decision required from founder:** Which implementation? Or: which *trade-offs* are acceptable?

## The "DO NOT IMPLEMENT" Reminder

Per the founder's direction 2026-06-15:

> Do not implement: Kernel runtime, **Memory Federation**, ARC Runtime, Governance Middleware, Agent Runtime at this stage.

The Memory Federation is on the "do not implement" list. This scaffolding README is the *placeholder*, not the implementation.

## Cross-References

- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-CODE-INVENTORY.md` — the recovered code inventory (apps/memory/federation.py, 76 LOC, 41 LOC tests)
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/RECOVERED-REUSABLE-CONCEPTS.md` §"C2" — the 4-layer Memory Model concept
- `Javalin13/ryzen-continuity/blob/main/04-recovery-archive/OPEN-DECISIONS.md` — the 3 open decisions (D1, D2, D3)
- `Javalin13/ryzen-continuity/blob/main/RYZEN-REBUILD-SPECIFICATION-v1.0.md` §"R1" and §"R3" — the rebuild spec
- `04-rebuild-integration/RS-PHASES.md` — the rebuild spec integration map
