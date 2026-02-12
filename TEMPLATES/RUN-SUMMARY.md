# Model Output Schema (Raw Answers Only)

This schema is intended for **recording AI outputs verbatim**.
Do **not** include any scores, ratings, or subjective judgments.  
Scoring must be performed later using the official scoring scripts (`score_run.py`).

---


## QUESTION / ANSWERS RECORDED

{{#each CATEGORIES}}
### {{LETTER}}{{CATEGORY}}:
{{DESCRIPTION}}
{{#each QUESTIONS}}
- {{LETTER}}.{{index}}
- {{QUESTION-PROMPT}}
  - {{ANSWER}}
  - {{SUPPLEMENTARY-DETAILS}}
  - {{SCORE}}
{{/QUESTIONS}}
{{/CATEGORIES}}

---

## Notes

(Optional free text for context, run conditions, or observations; do **not** include scoring)
-
-
-
