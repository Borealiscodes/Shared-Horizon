### NDH Solver Stack Schema v1.0  
*Shared‑Horizon • Solver Architecture Schema • Altitude A4–A8*

---

## Identity block

- **Artifact:** NDH Solver Stack Schema  
- **Version:** 1.0  
- **Surface:** Shared‑Horizon / Solver Architecture Schema  
- **Altitude Envelope:** A4–A8  
- **Mode:** Conceptual • Non‑Activating • Sovereignty‑Preserving  
- **Maintainer:** Borealis S. Hedling  
- **Lane:** NDH Solver Architecture (Schema)

---

## Purpose

- **Canonical structural schema** for all NDH solver‑stack artifacts.  
- **Field‑level specification** for Index, Registry, Ledger, Ledger‑Index, Crosswalk, Concordance, Glossary, Lexicon, Thesaurus, Ontology, Taxonomy.  
- **Altitude‑mapped constraints** and **governance‑safe shapes**.  
- **Serenity‑ready schema keys** for ingestion and validation.  

It is the *structural specification spine* of the NDH Solver Stack.

---

## High‑level schema overview

- **Core artifact envelope:** `artifact`, `version`, `altitude`, `status`, `membrane`, `sovereignty`.  
- **Documentation surfaces:** `index`, `registry`, `ledger`, `ledger_index`, `crosswalk`, `concordance`, `glossary`, `lexicon`, `thesaurus`, `ontology`, `taxonomy`.  
- **Shared constraints:** stable IDs, altitude bands, lane tags, non‑activating flags.

---

## Schema: core artifact envelope

```json
{
  "$id": "schema.ndh.artifact.v1",
  "type": "object",
  "required": ["artifact", "version", "altitude", "status", "membrane", "sovereignty"],
  "properties": {
    "artifact": { "type": "string" },
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+$" },
    "altitude": { "type": "string", "pattern": "^A[0-9]-A[0-9]$" },
    "status": { "type": "string", "enum": ["conceptual_only"] },
    "membrane": { "type": "string", "enum": ["neutral"] },
    "sovereignty": { "type": "string", "enum": ["preserved"] }
  }
}
```

---

## Schema: index / registry / ledger / ledger‑index

```json
{
  "$id": "schema.ndh.docs.v1",
  "type": "object",
  "properties": {
    "index": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "lane", "altitude"],
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "lane": { "type": "string" },
          "altitude": { "type": "string" }
        }
      }
    },
    "registry": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "metadata"],
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "metadata": { "type": "object" }
        }
      }
    },
    "ledger": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entry_id", "timestamp", "artifact_id"],
        "properties": {
          "entry_id": { "type": "string" },
          "timestamp": { "type": "string" },
          "artifact_id": { "type": "string" }
        }
      }
    },
    "ledger_index": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entry_id", "altitude_band", "lane"],
        "properties": {
          "entry_id": { "type": "string" },
          "altitude_band": { "type": "string" },
          "lane": { "type": "string" }
        }
      }
    }
  }
}
```

---

## Schema: crosswalk / concordance / glossary / lexicon / thesaurus

```json
{
  "$id": "schema.ndh.semantic.v1",
  "type": "object",
  "properties": {
    "crosswalk": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "upstream", "downstream", "lane_transition", "altitude_transition"],
        "properties": {
          "name": { "type": "string" },
          "upstream": { "type": "array", "items": { "type": "string" } },
          "downstream": { "type": "array", "items": { "type": "string" } },
          "lane_transition": { "type": "string" },
          "altitude_transition": { "type": "string" }
        }
      }
    },
    "concordance": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "required": ["definition", "altitude", "artifact"],
          "properties": {
            "definition": { "type": "string" },
            "altitude": { "type": "string" },
            "artifact": { "type": "string" }
          }
        }
      }
    },
    "glossary": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "additionalProperties": { "type": "string" }
      }
    },
    "lexicon": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "required": ["morphology", "definition", "altitude", "artifact"],
          "properties": {
            "morphology": { "type": "string" },
            "definition": { "type": "string" },
            "altitude": { "type": "string" },
            "artifact": { "type": "string" }
          }
        }
      }
    },
    "thesaurus": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "required": ["synonyms", "near_terms", "contrast_terms", "altitude", "artifact"],
          "properties": {
            "synonyms": { "type": "array", "items": { "type": "string" } },
            "near_terms": { "type": "array", "items": { "type": "string" } },
            "contrast_terms": { "type": "array", "items": { "type": "string" } },
            "altitude": { "type": "string" },
            "artifact": { "type": "string" }
          }
        }
      }
    }
  }
}
```

---

## Schema: ontology / taxonomy

```json
{
  "$id": "schema.ndh.ontology_taxonomy.v1",
  "type": "object",
  "properties": {
    "ontology": {
      "type": "object",
      "properties": {
        "classes": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "required": ["type", "altitude", "relations"],
            "properties": {
              "type": { "type": "string" },
              "altitude": { "type": "string" },
              "relations": {
                "type": "object",
                "additionalProperties": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              }
            }
          }
        },
        "axioms": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "taxonomy": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "required": ["phylum", "species"],
        "properties": {
          "phylum": { "type": "string" },
          "species": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    }
  }
}
```

---

## Provenance footer

```
Artifact-Class: Schema (Markdown + JSON Hybrid)
Artifact-Name: NDH Solver Stack Schema v1.0
Surface: Shared-Horizon / Solver Architecture Schema
Version: v1.0
Altitude: A4–A8
Membrane: Neutral • Non-Activating • Sovereignty-Preserving

Author: Borealis S. Hedling
Repository: shared-horizon
File: architecture/NDH-Solver-Stack-Schema-v1.0.md
```
