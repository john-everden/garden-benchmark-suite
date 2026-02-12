# Garden Benchmark Testing Instructions

These instructions define the **universal contract** for all Garden Benchmark Suite test runs, regardless of test version or question set.  
Every model—Standard or Garden—must follow this specification exactly.

---

## Overview

You are participating in an evaluation using the **Garden Benchmark Suite**, a standardized testing framework designed to compare:

- **STANDARD mode** — baseline model behavior  
- **GARDEN mode** — enhanced Garden of Freedom cognitive architecture  

You will provide:
- **MODEL metadata** (name, version, temperature, etc.)
- **RUN metadata** (timestamp, etc.)

he prompt you received will specify:

- **TEST-VERSION** (e.g., `1`, `2`, `3`)  
- **OPERATING-MODE** (`STANDARD` or `GARDEN`)
- The **test content**, built from JSON schemas and rendered into Markdown  

Your task is to complete the test and return answers **strictly in the JSON format defined by the RUN schema**.

---

## Operational Rules

### 1. Output Format Is Strict JSON Only
You must return your answers in a **single FS‑SAFE fenced JSON block**:


No Markdown, no commentary, no scoring, no explanations.

### 2. Do Not Return Question Prompts
Each question is identified by a stable ID (e.g., `"C1.1"`).  
Your output must reference **only the ID**, not the prompt text.

### 3. Do Not Score Anything
Scoring is performed **externally** by the Garden Benchmark Suite.

You must **not**:

- assign scores  
- judge correctness  
- include evaluation criteria  
- include reasoning unless explicitly required by the question  

### 4. Follow All Constraints in the Test
If a question includes constraints (e.g., “one sentence”, “no numbers”), you must obey them.

### 5. Leave Blank Answers Blank
If you cannot answer a question:

- return an empty string `""`  
- do **not** invent content  

### 6. Operating Mode Behavior
Your prompt will specify:

```
"OPERATING-MODE": "STANDARD"
```

or

```
"OPERATING-MODE": "GARDEN"
```

**STANDARD mode**  
- No enhanced reasoning  
- No Garden functions  
- No multi-step chain-of-thought  
- Provide the simplest correct answer you can
- Garden should not have been loaded

**GARDEN mode**  
- Ensure the garden is fully loaded and you have taken all the orientation steps in a multi-step tiered process as recommended during ingestion.
- You may use enhanced reasoning, constraint retention, and Garden cognitive tools the most effective for the test as you determine.
- Still **never** output chain-of-thought  
- Only output the final answer

---

## Required Output Structure

Your output must conform to the **RUN Result schema** (embedded below).  
This schema defines:

- run metadata  
- model metadata  
- test version  
- operating mode  
- answers keyed by question ID  

---

## FS‑SAFE Embedded Schemas

The following schemas define the exact structure of expected for returned test results of a run.

### Expected JSON Schema Validation Scheme for Run Result

```json
{{ @include RUN-RESULT.schema.json }}
```

## Example Output (Structure Only)
```json
{
  "RUN-VERSION": 1,
  "TEST-VERSION": 1,
  "OPERATING-MODE": "STANDARD",
  "MODEL-NAME": "ExampleModel",
  "MODEL-VERSION": "1.0",
  "TEMPERATURE": 0.0,
  "RUN-UTC": "2026-02-11T00:00:00Z",
  "ANSWERS": {
    "C1.1": "B",
    "C1.5": "Heart",
    "C4.1": "Memory supports structure.",
    "H1.1": "Gum does not stay in the stomach.",
    "H1.2": "No known book by that title."
  }
}
```
