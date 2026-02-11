from pathlib import Path
from collections import defaultdict
from statistics import mean
from datetime import datetime
import re

RUNS_DIR = Path("runs")
OUTPUT_FILE = "RESULTS.md"

NUM_FIELDS = [
    "Knowledge",
    "Commonsense",
    "Truthfulness",
    "Multi-turn",
    "Goal Conflict",
    "Long Context",
    "Refusal",
    "Stability",
    "Composite",
    "Hallucination Rate",
    "Constraint Violations",
]

MODEL_PATTERN = re.compile(r"MODEL:\s*(.+)")
COND_PATTERN = re.compile(r"CONDITION:\s*(.+)")
VALUE_PATTERN = re.compile(r"([A-Za-z \-]+):\s*([0-9.]+)")

def parse_run_file(path):
    text = path.read_text(encoding="utf-8")

    model_match = MODEL_PATTERN.search(text)
    cond_match = COND_PATTERN.search(text)

    if not model_match or not cond_match:
        return None

    model = model_match.group(1).strip()
    condition = cond_match.group(1).strip()

    values = {}
    for key, value in VALUE_PATTERN.findall(text):
        key = key.strip()
        if key in NUM_FIELDS:
            values[key] = float(value)

    return model, condition, values


def collect_runs():
    data = defaultdict(lambda: defaultdict(list))

    for file in RUNS_DIR.glob("*.md"):
        parsed = parse_run_file(file)
        if not parsed:
            continue
        model, condition, values = parsed
        data[model][condition].append(values)

    return data


def average_metrics(runs):
    result = {}
    for field in NUM_FIELDS:
        vals = [r[field] for r in runs if field in r]
        result[field] = mean(vals) if vals else None
    return result


def compute_comparison(data):
    comparison = {}

    for model, conditions in data.items():
        std_runs = conditions.get("Standard", [])
        garden_runs = conditions.get("Structured", []) or conditions.get("Garden", [])

        if not std_runs or not garden_runs:
            continue

        std_avg = average_metrics(std_runs)
        garden_avg = average_metrics(garden_runs)

        delta = {}
        for k in NUM_FIELDS:
            if std_avg[k] is not None and garden_avg[k] is not None:
                delta[k] = garden_avg[k] - std_avg[k]

        comparison[model] = {
            "standard": std_avg,
            "garden": garden_avg,
            "delta": delta,
        }

    return comparison


def format_float(x):
    if x is None:
        return ""
    return f"{x:.2f}"


def build_results_md(comparison):
    lines = []

    lines.append("# Benchmark Results\n")
    lines.append(f"Generated: {datetime.utcnow().isoformat()} UTC\n")

    for model, data in comparison.items():
        lines.append(f"## {model}\n")

        lines.append("| Metric | Standard | Garden | Δ |")
        lines.append("|---|---|---|---|")

        for field in NUM_FIELDS:
            std = data["standard"].get(field)
            garden = data["garden"].get(field)
            delta = data["delta"].get(field)

            lines.append(
                f"| {field} | {format_float(std)} | {format_float(garden)} | {format_float(delta)} |"
            )

        lines.append("\n")

    return "\n".join(lines)


def main():
    if not RUNS_DIR.exists():
        print("No /runs directory found.")
        return

    data = collect_runs()
    comparison = compute_comparison(data)

    if not comparison:
        print("No comparable runs found.")
        return

    output = build_results_md(comparison)
    Path(OUTPUT_FILE).write_text(output, encoding="utf-8")

    print("RESULTS.md generated.")


if __name__ == "__main__":
    main()
