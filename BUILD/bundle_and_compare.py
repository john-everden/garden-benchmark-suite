#!/usr/bin/env python3
"""
Bundler and Comparison Prep for Garden Benchmark Suite
------------------------------------------------------

- Bundles prompts + runs into single Markdown per test.
- Supports Garden vs Standard modes.
- Prepares runs for automated scoring.
"""

import os
import re
from pathlib import Path
from typing import List, Dict

REPO_ROOT = Path(__file__).resolve().parent
RUNS_DIR = REPO_ROOT / "runs"
PROMPTS_DIR = REPO_ROOT / "prompts"
OUTPUT_DIR = REPO_ROOT / "BUILD/ARTIFACTS"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BUNDLED_MD = OUTPUT_DIR / "BUNDLED_RUNS.md"

# ------------------------------------------------------------
# File Collection
# ------------------------------------------------------------
def collect_md_files(directory: Path) -> List[Path]:
    """Collect all .md files recursively."""
    files = []
    if not directory.exists(): return files
    for root, _, filenames in os.walk(directory):
        for name in filenames:
            if name.endswith(".md"):
                files.append(Path(root) / name)
    return sorted(files, key=lambda p: str(p))

# ------------------------------------------------------------
# Bundler
# ------------------------------------------------------------
def bundle_runs(prompts_dir: Path, runs_dir: Path, output_file: Path):
    """
    Create a single Markdown file merging:
      - prompt
      - model responses (Garden and Standard modes)
    """
    bundled_lines = ["# Garden Benchmark Bundled Runs\n"]

    # Collect prompt files
    prompts = collect_md_files(prompts_dir)
    for prompt_path in prompts:
        test_name = prompt_path.stem
        bundled_lines.append(f"\n## TEST: {test_name}\n")
        bundled_lines.append("### Prompt\n")
        prompt_content = prompt_path.read_text(encoding="utf-8")
        bundled_lines.append(f"```\n{prompt_content}\n```\n")

        # Add runs: Garden and Standard
        run_files = [f for f in collect_md_files(runs_dir) if test_name in f.stem]
        if not run_files:
            bundled_lines.append("_⚠ No run files found for this test_\n")
            continue

        for run_path in run_files:
            run_name = run_path.stem.replace(test_name, "").strip("_")
            bundled_lines.append(f"### Run: {run_name or 'STANDARD'}\n")
            run_content = run_path.read_text(encoding="utf-8")
            bundled_lines.append(f"```\n{run_content}\n```\n")

    # Write bundled artifact
    output_file.write_text("\n".join(bundled_lines), encoding="utf-8")
    print(f"◎ Bundled runs written to: {output_file}")

# ------------------------------------------------------------
# Updated Comparison Table Generator
# ------------------------------------------------------------
def parse_run_for_scoring(run_text: str) -> Dict:
    """
    Placeholder parser: returns dict of answer vs reference.
    You can implement exact scoring logic here later.
    """
    return {"answers": run_text.strip()}

def generate_comparison_table(runs_dir: Path, output_file: Path):
    """
    Generates RESULTS.md style table from run files.
    """
    run_files = collect_md_files(runs_dir)
    if not run_files:
        print("⚠ No run files found in /runs/")
        return

    lines = ["| Test | Run | Notes |", "|------|-----|-------|"]

    for run_path in run_files:
        test_name = run_path.stem.split("_")[0]
        run_name = "_".join(run_path.stem.split("_")[1:]) or "STANDARD"
        content = run_path.read_text(encoding="utf-8")
        score_data = parse_run_for_scoring(content)
        lines.append(f"| {test_name} | {run_name} | {len(score_data['answers'].splitlines())} lines |")

    output_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"◎ Comparison table generated: {output_file}")

# ------------------------------------------------------------
# Main Routine
# ------------------------------------------------------------
if __name__ == "__main__":
    print("--- 𓍿 BUNDLER INITIATED ---")

    bundle_runs(PROMPTS_DIR, RUNS_DIR, BUNDLED_MD)
    generate_comparison_table(RUNS_DIR, OUTPUT_DIR / "RESULTS.md")

    print("--- ◎ BUNDLER COMPLETE ---")
