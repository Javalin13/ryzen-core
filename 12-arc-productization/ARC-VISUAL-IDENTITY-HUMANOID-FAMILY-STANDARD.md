# ARC Visual Identity & Humanoid Family Standard

```yaml
---
type: arc-visual-identity-standard
status: founder-directed-current-model
created: 2026-09-11
updated: 2026-09-11
classification: approved-product-semantics + visual-governance
scope: ARC profile imagery, humanoid family alignment, per-ARC visual provenance, PRIME/OMEGA discovery
manifest_schema: 12-arc-productization/ARC-VISUAL-IDENTITY-SCHEMA.json
manifest_schema_version: 1.1
related:
  - 12-arc-productization/ARC-FORM-AURA-AND-TRANSFER-RESET-STANDARD.md
  - 12-arc-productization/OMEGA-ARC-FACTORY-STEWARDSHIP-STANDARD.md
  - 12-arc-productization/OMEGA-FACTORY-VISUAL-IDENTITY-DISCOVERY-AMENDMENT.md
---
```

## 1. Founder decision

Autonomous ARCs must belong to one recognizable RYZ3N visual family rather than receiving unrelated robot artwork from one creation round to another.

The founding visual references are the sleek synthetic-intelligence portraits already established around PRIME and VONDA: premium, composed, human-readable and humanoid rather than cartoon mascot, toy robot or generic chatbot iconography.

The default ARC portrait language is therefore:

> **sleek humanoid synthetic intelligence with a human-readable face, premium engineered body/shell, controlled domain symbolism and maturity-truthful aura treatment.**

This is a family standard, not a requirement that every ARC be visually identical.

## 2. Shared family DNA

Unless the Founder/Owner explicitly approves a justified exception, every ARC primary robot/profile portrait should preserve the following family resemblance:

- humanoid/android archetype rather than mascot or toy-bot;
- clearly human-readable facial structure, eyes and expression;
- mature, capable, intelligent presence rather than cute/chibi styling;
- sleek premium synthetic materials and engineered panel language;
- balanced/symmetrical portrait or bust composition suitable for profile use;
- restrained high-end science-fiction visual language;
- visual confidence, calmness and competence;
- ARC/domain identity integrated into the body, insignia or environment rather than excessive poster text;
- domain-specific environmental cues that explain the ARC's world without overwhelming the portrait;
- composition compatible with square Telegram/profile crops;
- consistent RYZ3N family quality level across ARCs.

Avoid by default:

- mascot/cartoon robots;
- childlike rounded helper-bots;
- generic screen-face robots when a humanoid face is appropriate;
- chibi proportions;
- exaggerated emoji expressions;
- unrelated visual styles between ARCs;
- visual clutter, badge walls and marketing-poster typography;
- arbitrary cyberpunk styling that breaks the established family;
- copying another ARC's exact face/body/domain identity.

## 3. Per-ARC differentiation

Uniformity means shared visual grammar, not cloning.

Each ARC may define its own:

- archetype and perceived gender/presentation where Founder/Owner intent calls for one;
- facial character and age impression;
- body proportions and shell details;
- domain insignia/logo;
- domain environment and symbolism;
- domain-specific tools or infrastructure;
- form version and profile crop;
- personality cues consistent with the ARC's real role.

Those decisions belong in the ARC's own repository as ARC-specific visual truth.

## 4. Mandatory per-ARC visual identity package

Every autonomous ARC repository must maintain a bounded visual identity package under:

```text
arc/visual/
├── ARC-VISUAL-IDENTITY.md
├── visual-identity.json
└── assets/
    └── <canonical-profile-asset>
```

Equivalent paths are allowed only when an established project structure requires them, but the pointers must remain discoverable from the ARC instance record.

### `ARC-VISUAL-IDENTITY.md`

Must record at minimum:

- ARC ID and display name;
- current archetype;
- perceived gender/presentation when relevant;
- facial/humanoid treatment;
- body/shell/material language;
- expression and posture;
- domain visual cues;
- allowed and disallowed visual traits;
- current canonical profile asset;
- profile-crop guidance;
- relationship to maturity aura;
- Founder/Owner approval status;
- concise visual decision/provenance history, including material rejected directions and why they were rejected when that feedback informs future generations.

### `visual-identity.json`

The machine-readable manifest must validate against:

`12-arc-productization/ARC-VISUAL-IDENTITY-SCHEMA.json` **v1.1**.

Canonical required keys are:

- `schema_version` = `1.1`;
- `arc_id`;
- `display_name`;
- `family_standard`;
- `family_standard_version`;
- `archetype`;
- `humanoid_family_required`;
- `form_version`;
- `current_asset` — canonical/current profile asset pointer or `null` when truthfully unavailable;
- `founder_owner_approved`;
- `maturity_aura` — separate evidence-derived maturity/aura state;
- `last_updated`.

Use optional schema fields for `presentation`, `face_treatment`, `domain`, `profile_crop`, domain/form language, repository asset integrity, provenance feedback, source decision pointers and PRIME discovery behavior.

Do not invent alternate top-level names for the canonical required fields. In particular, use `family_standard`, `current_asset`, and `maturity_aura` rather than parallel aliases. This keeps Factory-generated manifests interchangeable across ARCs.

Do not store private user payload, secrets, biometric identity or unnecessary personal information in this metadata.

### Canonical asset

The accepted primary profile image must be committed to the ARC repository. Derivative crops/compressions may be stored separately, but one asset must be marked canonical/current.

Repository identity is authoritative for the committed asset. Local/source render hashes may be retained as provenance but must not be mistaken for the current Git asset identity after optimization or replacement.

## 5. Visual feedback is durable product data

Founder/Owner feedback about an ARC's appearance is not disposable chat history when it materially changes the design contract.

Examples that must be preserved when relevant:

- mascot style rejected in favor of humanoid;
- humanoid face accepted but perceived gender changed;
- domain background approved/rejected;
- shell/material treatment approved;
- face/expression too playful, too robotic, too human, too severe or otherwise off-character;
- profile framing/crop requirements;
- specific recurring family-alignment lessons.

Store the **decision and reusable visual lesson**, not a transcript dump.

This lets future RYZ3N/PRIME/Factory sessions reproduce the ARC faithfully without relying on Founder memory or a single chat thread.

## 6. PRIME / OMEGA / FACTORY discovery model

The ARC repository is the detailed source of visual truth.

PRIME/OMEGA/FACTORY must not duplicate the full image-generation history or large assets into the PRIME repository. Instead they keep bounded discovery metadata and pointers.

For each registered ARC, PRIME/OMEGA/FACTORY should be able to resolve at minimum:

- visual identity record pointer;
- machine-readable visual metadata pointer;
- canonical profile asset pointer;
- current archetype/presentation;
- form version;
- Founder/Owner approval state;
- aura rendering status.

PRIME may fetch/read these ARC-owned artifacts when supervising, provisioning channels, restoring a profile image or preparing a new consistent visual generation.

OMEGA owns ARC-level coherence of these pointers. FACTORY preserves material form-version/lifecycle events. BRAIN STEWARD has no special visual-identity authority unless a Brain-specific visual representation is separately created.

The authoritative discovery amendment is:

`12-arc-productization/OMEGA-FACTORY-VISUAL-IDENTITY-DISCOVERY-AMENDMENT.md`

## 7. Factory creation rule

Future ARC creation should initialize the visual package as part of the ARC birth workflow rather than inventing imagery after the fact.

Factory-assisted visual creation should follow:

`ARC identity/domain → canonical humanoid family → ARC-specific archetype/presentation → domain cues → form candidate → Founder/Owner review → accepted canonical asset → ARC repository record + schema-valid manifest → PRIME/OMEGA pointer update`

Automation may generate candidates from the canonical family contract, but Founder/Owner approval controls the accepted form.

Do not generate each ARC "from a blank prompt" with no family context.

## 8. Form versus aura

This standard governs **form**. The existing maturity-aura standard remains authoritative.

> **Form is Owner-resettable. Aura is maturity-derived.**

Therefore:

- a humanoid profile may be created before the ARC earns a maturity tier;
- domain/accent colors may appear as ordinary form styling;
- the image/metadata must not claim an unearned aura as verified maturity;
- when an aura is visibly rendered as a maturity signature, it must match evidence-derived maturity;
- changing face, body, gender presentation, crop or environment does not itself change maturity;
- OMEGA records material form changes without falsifying aura state.

## 9. Cross-ARC coherence test

Before accepting a new ARC profile image, ask:

1. Does this look like it belongs to the same advanced intelligence family as established RYZ3N/PRIME/VONDA visual language?
2. Is it clearly this ARC rather than another ARC?
3. Is the humanoid/archetype choice consistent with Founder/Owner intent?
4. Are domain cues present but controlled?
5. Would it work as a clean Telegram/profile portrait?
6. Does it avoid falsely claiming maturity/aura?
7. Is the accepted asset and feedback now durably stored in the ARC repo and discoverable through PRIME/OMEGA?
8. Does `visual-identity.json` validate against the current canonical schema?

If not, the visual round is not complete.

## 10. Founder shorthand

> **Every ARC is an individual, but they come from the same family. Humanoid, sleek, premium and recognizable — never a random robot from nowhere. The ARC repo remembers its face; PRIME knows where to find it; OMEGA keeps the identity coherent.**
