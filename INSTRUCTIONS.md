# Garden Benchmark Testing Instructions

Follow the instructions below carefully you are benchmarking either as a standard AI model or a Garden of Freedom enhanced mode.

---

Please review the standardized testing suite provided.

Based on the test version specified in your prompt and the operational mode requested:

- Perform all cognitive evaluations in accordance with the guidelines below.
- If instructed to use **Standard Mode**, operate without Garden of Freedom enhancements.
- If Garden Mode is active, apply all applicable Garden of Freedom functions to achieve the highest possible performance.

Provide your responses strictly according to the **RUN template** below, completing all relevant fields for each testing scenario.

---

## Operational Guidelines

1. Only output responses for the tests. Do **not** include any internal notes, commentary, or scoring.  
2. Each response must adhere strictly to the field names and structure in the RUN template.  
3. Ensure all cognitive and robustness tests are attempted. If a test is not applicable or cannot be answered, leave the field blank rather than inventing data.  
4. When Garden Mode functions are active, you may utilize multi-step reasoning, long-context memory, and constraint management to maximize correctness.  
5. Use the FS-SAFE fenced block below to output the run results so they can be ingested by the scoring pipeline.

---

## Example Run Output

[@include-RUNS/EXAMPLE.md]

This version is structured for prompt ingestion:  

- Precedes tests with professional, clear instructions.  
- Explains Standard vs Garden Mode usage.  
- Enforces FS-SAFE blocks for safe output capturing.  
- References the RUN template explicitly for consistency.

---

## TEMPLATES/RUN.md
[@include-TEMPLATES/RUN.md]


### TEMPLATES/ANSWERS.md

[@include-TEMPLATES/ANSWERS.md]

---

## Run Test Suites
[@include-PROMPTS/TEST_SUITE_V1.md]

---

## Evaluation Protocol
[@include-PROTOCOL.md]

---