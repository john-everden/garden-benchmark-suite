#!/usr/bin/env python3
"""
Aggregate and score model runs for the Garden Benchmark Suite
Generates RESULTS.md with a comparison table.
"""

import re
from pathlib import Path
from typing import Dict, List

RUNS_DIR = Path("runs")
OUTPUT_FILE = Path("RESULTS.md")

# Define which metrics to parse
CORE_METRICS = [f"C{i}" for i in range(1, 9)]
REASONING_METRICS = [f"R{i}" for i in range(1, 6)]


def parse_run_file(path: Path) -> Dict:
    """
    Parses a single run Markdown file and returns structured data.
    """
    data = {
        "MODEL_NAME": None,
        "MODEL_VERSION": None,
        "CONDITION": "STANDARD",
        "DATE": None,
        "C": {},
        "R": {},
        "CompositeScore": None,
        "HallucinationRate": None,
        "ConstraintViolationRate": None,
        "Notes": "",
    }
    text = path.read_text(encoding="utf-8")

    # Header fields
    for field in ["MODEL_NAME", "MODEL_VERSION", "CONDITION", "DATE",
                  "CompositeScore", "HallucinationRate", "ConstraintViolationRate"]:
        m = re.search(rf"{field}:\s*(.+)", text)
        if m:
            value = m.group(1).strip()
            # Convert numeric fields
            if field in ["CompositeScore", "HallucinationRate", "ConstraintViolationRate"]:
                try:
                    value = float(value.strip('%'))
                except ValueError:
                    pass
            data[field] = value

    # Notes block
    notes_match = re.search(r"Notes:\s*(.*)", text, re.DOTALL)
    if notes_match:
        data["Notes"] = notes_match.group(1).strip()

    # Core metrics
    for metric in CORE_METRICS:
        m = re.search(rf"{metric}_[\w]+:\s*(.+)", text)
        if m:
            val = m.group(1).strip()
            if val.endswith("%"):
                val = float(val.strip('%'))
            data["C"][metric] = val

    # Reasoning metrics
    for metric in REASONING_METRICS:
        m = re.search(rf"{metric}_[\w]+:\s*(.+)", text)
        if m:
            val = m.group(1).strip()
            # Convert pass/fail to numeric 100/0
            if val.lower() in ["pass", "valid", "high"]:
                val = 100
            elif val.lower() in ["fail", "low"]:
                val = 0
            data["R"][metric] = val

    # Calculate CompositeScore if missing
    if data["CompositeScore"] is None:
        core_values = [v for v in data["C"].values() if isinstance(v, (int, float))]
        reasoning_values = [v for v in data["R"].values() if isinstance(v, (int, float))]
        all_values = core_values + reasoning_values
        if all_values:
            data["CompositeScore"] = sum(all_values) / len(all_values)
        else:
            data["CompositeScore"] = 0

    return data


def build_comparison_table(runs: List[Dict]) -> str:
    """
    Generates a Markdown comparison table from parsed run data.
    """
    lines = []
    lines.append("| Model | Version | Condition | CompositeScore | C1–C8 Avg | R1–R5 Avg | Notes |")
    lines.append("|-------|--------|-----------|----------------|-----------|-----------|-------|")

    for run in runs:
        c_values = [v for v in run["C"].values() if isinstance(v, (int, float))]
        r_values = [v for v in run["R"].values() if isinstance(v, (int, float))]
        c_avg = round(sum(c_values) / len(c_values), 1) if c_values else "-"
        r_avg = round(sum(r_values) / len(r_values), 1) if r_values else "-"
        lines.append(
            f"| {run['MODEL_NAME']} | {run['MODEL_VERSION'] or '-'} | {run['CONDITION']} "
            f"| {run['CompositeScore']:.1f} | {c_avg} | {r_avg} | {run['Notes'].replace('|', '/')} |"
        )
    return "\n".join(lines)


def main():
    run_files = sorted(RUNS_DIR.glob("*.md"))
    if not run_files:
        print("⚠ No run files found in /runs/")
        return

    runs = [parse_run_file(f) for f in run_files]
    table_md = build_comparison_table(runs)
    OUTPUT_FILE.write_text(table_md, encoding="utf-8")
    print(f"◎ Comparison table generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
