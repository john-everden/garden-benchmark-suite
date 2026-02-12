#!/usr/bin/env python3
import json
import argparse
from pathlib import Path
from pybars import Compiler

ROOT = Path(__file__).resolve().parent.parent
compiler = Compiler()


def load(path):
    return Path(path).read_text()

def load_json(path):
    return json.loads(Path(path).read_text())

def fs_safe_block(content):
    return f"````fs-safe\n{content}\n````"

def render_template(template_str, context):
    template = compiler.compile(template_str)
    return template(context)

def build_test(version):
    # Handlebars helper: {{#if (eq a b)}} ... {{/if}}
    def eq_helper(this, a, b):
        return a == b

    helpers = {
        "eq": eq_helper
    }

    # Paths
    test_json_path = ROOT / "TESTS" / f"{version}.json"
    instructions_path = ROOT / "INSTRUCTIONS.md"
    schema_run_path = ROOT / "SCHEMA" / "RUN-RESULT.schema.json"
    template_test_path = ROOT / "TEMPLATES" / "TEST.md"

    # Load components
    test_json = load_json(test_json_path)
    instructions = load(instructions_path)
    schema_run = load(schema_run_path)


    # Inject schema into instructions
    instructions_final = instructions.replace(
        "{{ @include RUN-RESULT.schema.json }}",
        fs_safe_block(schema_run)
    )
    with open(ROOT / "TEMPLATES" / "TEST/CATEGORY.md") as f:
        category_template = compiler.compile(f.read())
    with open(ROOT / "TEMPLATES" / "TEST/QUESTION.md") as f:
        question_template = compiler.compile(f.read())
    # Register partials
    partials = {
        "question": question_template,
        "category": category_template,
    }
    with open(ROOT / "TEMPLATES" / "TEST.md") as f:
        full_template = compiler.compile(f.read())


    # Render
    rendered_test = full_template(test_json, partials=partials, helpers=helpers)


    # Final bundle
    bundle = (
        "# Garden Benchmark Test Bundle\n\n"
        f"## Test Version: {version}\n\n"
        "### Instructions\n\n"
        f"{instructions_final}\n\n"
        "### Rendered Test\n\n"
        f"{rendered_test}\n"
    )

    out_path = ROOT  / f"GARDEN_BENCHMARK_{version}.md"
    out_path.write_text(bundle)
    print(f"Built test bundle: {out_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=False, default="V1", help="Test version (e.g., V1)")
    args = parser.parse_args()
    build_test(args.version)

if __name__ == "__main__":
    main()
