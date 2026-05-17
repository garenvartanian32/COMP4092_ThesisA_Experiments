#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

# Radon
from radon.complexity import cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze as radon_analyze

# Lizard
import lizard


def safe_avg(values):
    return sum(values) / len(values) if values else 0.0


def analyse_file(file_path: Path) -> dict:
    code = file_path.read_text(encoding="utf-8", errors="ignore")

    # -------------------------
    # Radon metrics
    # -------------------------
    raw = radon_analyze(code)
    cc_blocks = cc_visit(code)
    hal = h_visit(code)
    mi_score = mi_visit(code, multi=True)

    radon_cc_values = [block.complexity for block in cc_blocks]

    # -------------------------
    # Lizard metrics
    # -------------------------
    liz = lizard.analyze_file(str(file_path))
    lizard_cc_values = [func.cyclomatic_complexity for func in liz.function_list]

    return {
        # -------------------------
        # File info
        # -------------------------
        "file": file_path.name,
        "folder": file_path.parent.name,
        "label": "AI" if "ai" in file_path.name.lower() else "Human",

        # -------------------------
        # Radon (core metrics)
        # -------------------------
        "mi": round(mi_score, 2),

        "cc_avg": round(safe_avg(radon_cc_values), 2),
        "cc_max": max(radon_cc_values) if radon_cc_values else 0,

        "halstead_volume": round(hal.total.volume, 2),
        "halstead_difficulty": round(hal.total.difficulty, 2),
        "halstead_effort": round(hal.total.effort, 2),

        "loc": raw.loc,
        "sloc": raw.sloc,
        "lloc": raw.lloc,

        # -------------------------
        # Lizard (summary)
        # -------------------------
        "lz_nloc": liz.nloc,
        "lz_cc_avg": round(safe_avg(lizard_cc_values), 2),
        "lz_cc_max": max(lizard_cc_values) if lizard_cc_values else 0,
        "lz_functions": len(liz.function_list),
    }


def find_python_files(root: Path):
    return sorted(p for p in root.rglob("*.py") if p.is_file())


def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_metrics_to_csv.py <input_folder> <output_csv>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_csv = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: path does not exist: {input_path}")
        sys.exit(1)

    # Allow both file or folder input
    if input_path.is_file():
        py_files = [input_path]
    else:
        py_files = find_python_files(input_path)

    if not py_files:
        print("No Python files found.")
        sys.exit(0)

    rows = []
    for file_path in py_files:
        try:
            row = analyse_file(file_path)
            rows.append(row)
            print(f"Processed: {file_path}")
        except Exception as e:
            print(f"Skipped {file_path}: {e}")

    if not rows:
        print("No files were successfully analysed.")
        sys.exit(1)

    fieldnames = list(rows[0].keys())

    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nDone. Wrote {len(rows)} rows to {output_csv}")


if __name__ == "__main__":
    main()