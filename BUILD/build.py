#!/usr/bin/env python3
"""
BUILD/bundle_garden_benchmark.py

Bundle RUN.md instructions + all TEST_SUITE_Vx.md + ANSWERS.md
into a single Markdown file for ingestion or prompt.
"""

from pathlib import Path

# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------
BUILD_DIR = Path(__file__).parent
ARTIFACTS_DIR = BUILD_DIR / "ARTIFACTS"
PROMPTS_DIR = Path(__file__).parent.parent / "PROMPTS"
TEMPLATES_DIR = Path(__file__).parent.parent / "TEMPLATES"

ARTIFACTS_DIR.mkdir(exist_ok=True)

# Output bundle
BUNDLE_FILE = ARTIFACTS_DIR / "GARDEN_BENCHMARK_BUNDLE.md"

# Template sources
RUN_TEMPLATE = TEMPLATES_DIR / "RUN.md"
ANSWERS_TEMPLATE = TEMPLATES_DIR / "ANSWERS.md"

# ------------------------------------------------------------
# Bundler
# ------------------------------------------------------------
def bundle_prompt():
    """Bundle instruction template + test suites + answer schema into a single Markdown file."""
    if not RUN_TEMPLATE.exists():
        raise FileNotFoundError(f"RUN template not found: {RUN_TEMPLATE}")
    if not ANSWERS_TEMPLATE.exists():
        raise FileNotFoundError(f"Answers template not found: {ANSWERS_TEMPLATE}")

    bundled_content = ["# GARDEN BENCHMARK PROMPT\n"]

    # 1️⃣ Add RUN instructions
    bundled_content.append("## 1. RUN Instructions\n")
    run_content = RUN_TEMPLATE.read_text(encoding="utf-8")
    bundled_content.append(run_content)

    # 2️⃣ Add Test Suites
    test_files = sorted(PROMPTS_DIR.glob("TEST_SUITE_V*.md"))
    if not test_files:
        print("⚠ No test suites found in PROMPTS/")
    else:
        for test_file in test_files:
            bundled_content.append(f"\n## 2. {test_file.name}\n")
            bundled_content.append(test_file.read_text(encoding="utf-8"))

    # 3️⃣ Add Answer Schema
    bundled_content.append("\n## 3. Expected Answer Schema\n")
    answers_content = ANSWERS_TEMPLATE.read_text(encoding="utf-8")
    bundled_content.append(answers_content)

    # Write final bundle
    BUNDLE_FILE.write_text("\n".join(bundled_content), encoding="utf-8")
    print(f"◎ Prompt bundle generated: {BUNDLE_FILE}")


# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------
if __name__ == "__main__":
    bundle_prompt()
