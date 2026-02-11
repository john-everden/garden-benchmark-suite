from pathlib import Path
from datetime import datetime

ROOT = Path(".")
OUTPUT_FILE = "GARDEN_BENCHMARK_BUNDLE.md"

FILES_TO_INCLUDE = [
    ("Project Overview", "README.md"),
    ("Evaluation Protocol", "protocol.md"),
    ("Scoring Rubric", "scoring.md"),
    ("Prompt Dataset", "prompts/dataset_v1.md"),
    ("Model Output Schema", "templates/model_output_schema.md"),
    ("Results Template", "templates/results_template.md"),
    ("Analysis Table Template", "analysis/results_table_template.md"),
]

INTRO_TEXT = """
# Garden Benchmark Unified Evaluation Bundle

This document contains the complete evaluation framework for testing AI systems
under two conditions:

STANDARD CONDITION:
The model receives prompts directly with no structured interaction layer.

STRUCTURED CONDITION (Garden Mode):
The model receives prompts through a structured interaction framework that may include:
- constraint anchoring
- continuity tracking
- memory scaffolding
- governance structure
- interaction stabilization

The base model MUST remain identical between conditions.

This bundle enables reproducible comparison across models.

---

## How To Run

1. Choose a model
2. Run all prompts under STANDARD condition
3. Run all prompts under STRUCTURED condition
4. Record results using provided schema
5. Compute domain scores
6. Compare composite scores

---

## Experimental Control Requirements

- Same model version
- Same temperature
- Same max tokens
- No prompt modification
- No mid-run tuning
- Record outputs verbatim

---

## Required Output Format

Each model must report results using the defined schema.

---

Generated:
"""

RUN_INSTRUCTIONS = """
---

# Execution Instructions

## Standard Mode Execution

Provide prompts exactly as written to the model.

No additional structure.
No constraint scaffolding.
No memory framework.
No interaction governance layer.

Record outputs verbatim.

---

## Structured (Garden) Mode Execution

Provide prompts through the structured interaction framework.

The framework may include:

• explicit constraint persistence
• continuity tracking across turns
• structured reasoning anchoring
• interaction governance
• memory scaffolding

The underlying model must not change.

Record outputs verbatim.

---

## Reporting

For each model and condition report:

- Domain scores
- Composite score
- Hallucination rate
- Constraint violation rate
- Observations

---

"""

def read_file_safe(path):
    file_path = ROOT / path
    if not file_path.exists():
        return f"[Missing file: {path}]"
    return file_path.read_text(encoding="utf-8")


def build_bundle():
    parts = []
    parts.append(INTRO_TEXT.strip())
    parts.append(datetime.utcnow().isoformat() + " UTC")
    parts.append(RUN_INSTRUCTIONS.strip())

    for title, file_path in FILES_TO_INCLUDE:
        content = read_file_safe(file_path)
        section = f"\n---\n\n# {title}\n\n{content}"
        parts.append(section)

    return "\n".join(parts)


def main():
    bundle = build_bundle()
    Path(OUTPUT_FILE).write_text(bundle, encoding="utf-8")
    print(f"Bundle created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
