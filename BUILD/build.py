#!/usr/bin/env python3
"""
Build markdown artifacts from prompt + layer files
"""
from pathlib import Path
from score_run import score_run

ROOT_TOP_FILES = [
    "README.md",
    "INSTRUCTIONS.md",

]


FILES_TO_INCLUDE = [
    ("Project Overview", "README.md"),
    ("Evaluation Protocol", "PROTOCOL.md"),
    ("Scoring Rubric", "INSTRUCTIONS.md"),
    ("Prompt Dataset", "PROMPTS/TEST_SUITE_V1.md"),
    ("Model Output Schema", "TEMPLATES/"),
    ("Results Template", "templates/results_template.md"),
    ("Analysis Table Template", "analysis/results_table_template.md"),
]

ARTIFACTS_DIR = Path(__file__).parent / "ARTIFACTS"
ARTIFACTS_DIR.mkdir(exist_ok=True)

def build_artifact(output_path: Path, title: str, content: str):
    for filename in ROOT_TOP_FILES:
        path = Path(filename)
        out.append(f"\n# FILE: {filename}\n")
        content = read_file(path)
        if compress:
            content = compress_content(content)
        out.append(content)
        out.append("\n")

    output_path.write_text(f"# {title}\n\n{content}", encoding="utf-8")
    print(f"◎ Artifact built: {output_path}")

if __name__ == "__main__":
    build_artifact(ARTIFACTS_DIR / "INSTRUCTIONS.md", "GARDEN OF FREEDOM BENCHMARKING INSTRUCTIONS", )
