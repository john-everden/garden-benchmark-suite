#!/usr/bin/env python3
"""
BUILD/score_and_build_results.py

Ingest model runs from RUNS/, score them using score_run.py,
and generate RESULTS.md in BUILD/ARTIFACTS using the TEMPLATES:
- RESULTS.md -> main RESULTS file skeleton
- RESULTS_TABLE.md -> table for per-run comparison
"""
from pathlib import Path
from score_run import score_run  # assumes returns dict with all score fields

# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------
BUILD_DIR = Path(__file__).parent
ARTIFACTS_DIR = BUILD_DIR / "ARTIFACTS"
RUNS_DIR = Path(__file__).parent.parent / "RUNS"
TEMPLATES_DIR = Path(__file__).parent.parent / "TEMPLATES"

RESULTS_FILE = ARTIFACTS_DIR / "RESULTS.md"
RESULTS_TEMPLATE_FILE = TEMPLATES_DIR / "RESULTS.md"
TABLE_TEMPLATE_FILE = TEMPLATES_DIR / "RESULTS_TABLE.md"

ARTIFACTS_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------
# Load Templates
# ------------------------------------------------------------
def load_template(template_path: Path) -> str:
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text(encoding="utf-8")


# ------------------------------------------------------------
# Render Table
# ------------------------------------------------------------
def render_table(runs: list[dict], table_template: str) -> str:
    """
    Fill RESULTS_TABLE.md template with scored runs.
    Placeholder in template: {{TABLE_ROWS}}
    """
    rows = []
    for run in runs:
        row = (
            f"| {run.get('MODEL_NAME','')} | {run.get('CONDITION','')} | "
            f"{run.get('CompositeScore','')} | {run.get('RobustnessScore','')} | "
            f"{run.get('HallucinationRate','')} | {run.get('ConstraintViolationRate','')} |"
        )
        rows.append(row)
    table_filled = table_template.replace("{{TABLE_ROWS}}", "\n".join(rows))
    return table_filled


# ------------------------------------------------------------
# Render Results File
# ------------------------------------------------------------
def render_results_file(runs: list[dict], results_template: str, table_template: str) -> str:
    """
    Fill RESULTS.md template:
    - {{RESULTS_TABLE}} -> table of runs
    - {{SUMMARY}} -> optional overall summary
    """
    table_str = render_table(runs, table_template)
    results_filled = results_template.replace("{{RESULTS_TABLE}}", table_str)

    # You can optionally inject other summary info here
    summary_lines = [
        f"Total Runs: {len(runs)}",
        f"Average Composite Score: {sum(r.get('CompositeScore',0) for r in runs)/len(runs) if runs else 0:.2f}"
    ]
    results_filled = results_filled.replace("{{SUMMARY}}", "\n".join(summary_lines))

    return results_filled


# ------------------------------------------------------------
# Main Build Routine
# ------------------------------------------------------------
def main():
    print("◎ Scoring runs and generating RESULTS.md")

    # Load templates
    results_template = load_template(RESULTS_TEMPLATE_FILE)
    table_template = load_template(TABLE_TEMPLATE_FILE)

    # Collect run files
    run_files = sorted(RUNS_DIR.glob("*.md"))
    runs_scored = []

    for run_file in run_files:
        print(f"→ Scoring {run_file.name}")
        run_data = score_run(run_file)  # should return dict with MODEL_NAME, CONDITION, CompositeScore, etc.
        runs_scored.append(run_data)

    # Render RESULTS.md
    results_content = render_results_file(runs_scored, results_template, table_template)
    RESULTS_FILE.write_text(results_content, encoding="utf-8")
    print(f"◎ RESULTS.md generated: {RESULTS_FILE}")


if __name__ == "__main__":
    main()
