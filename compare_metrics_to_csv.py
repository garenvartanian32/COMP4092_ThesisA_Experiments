# #!/usr/bin/env python3
# import csv
# import sys
# from pathlib import Path

# # Radon
# from radon.complexity import cc_visit
# from radon.metrics import h_visit, mi_visit
# from radon.raw import analyze as radon_analyze

# # Lizard
# import lizard


# def safe_avg(values):
#     return sum(values) / len(values) if values else 0.0


# def analyse_file(file_path: Path) -> dict:
#     code = file_path.read_text(encoding="utf-8", errors="ignore")

#     # -------------------------
#     # Radon metrics
#     # -------------------------
#     raw = radon_analyze(code)
#     cc_blocks = cc_visit(code)
#     hal = h_visit(code)
#     mi_score = mi_visit(code, multi=True)

#     radon_cc_values = [block.complexity for block in cc_blocks]

#     # -------------------------
#     # Lizard metrics
#     # -------------------------
#     liz = lizard.analyze_file(str(file_path))
#     lizard_cc_values = [func.cyclomatic_complexity for func in liz.function_list]

#     return {
#         # -------------------------
#         # File info
#         # -------------------------
#         "file": file_path.name,
#         "folder": file_path.parent.name,
#         "label": "AI" if "ai" in file_path.name.lower() else "Human",

#         # -------------------------
#         # Radon (core metrics)
#         # -------------------------
#         "mi": round(mi_score, 2),

#         "cc_avg": round(safe_avg(radon_cc_values), 2),
#         "cc_max": max(radon_cc_values) if radon_cc_values else 0,

#         "halstead_volume": round(hal.total.volume, 2),
#         "halstead_difficulty": round(hal.total.difficulty, 2),
#         "halstead_effort": round(hal.total.effort, 2),

#         "loc": raw.loc,
#         "sloc": raw.sloc,
#         "lloc": raw.lloc,

#         # -------------------------
#         # Lizard (summary)
#         # -------------------------
#         "lz_nloc": liz.nloc,
#         "lz_cc_avg": round(safe_avg(lizard_cc_values), 2),
#         "lz_cc_max": max(lizard_cc_values) if lizard_cc_values else 0,
#         "lz_functions": len(liz.function_list),
#     }


# def find_python_files(root: Path):
#     return sorted(p for p in root.rglob("*.py") if p.is_file())


# def main():
#     if len(sys.argv) != 3:
#         print("Usage: python compare_metrics_to_csv.py <input_folder> <output_csv>")
#         sys.exit(1)

#     input_path = Path(sys.argv[1])
#     output_csv = Path(sys.argv[2])

#     if not input_path.exists():
#         print(f"Error: path does not exist: {input_path}")
#         sys.exit(1)

#     # Allow both file or folder input
#     if input_path.is_file():
#         py_files = [input_path]
#     else:
#         py_files = find_python_files(input_path)

#     if not py_files:
#         print("No Python files found.")
#         sys.exit(0)

#     rows = []
#     for file_path in py_files:
#         try:
#             row = analyse_file(file_path)
#             rows.append(row)
#             print(f"Processed: {file_path}")
#         except Exception as e:
#             print(f"Skipped {file_path}: {e}")

#     if not rows:
#         print("No files were successfully analysed.")
#         sys.exit(1)

#     fieldnames = list(rows[0].keys())

#     with output_csv.open("w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(rows)

#     print(f"\nDone. Wrote {len(rows)} rows to {output_csv}")


# if __name__ == "__main__":
#     main()

#!/usr/bin/env python3
import csv
import sys
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Radon only
from radon.complexity import cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze as radon_analyse


def safe_avg(values):
    return sum(values) / len(values) if values else 0.0


def file_hash(file_path: Path) -> str:
    """
    Creates a short hash for the file.
    Useful for checking whether the same file was analysed more than once.
    """
    content = file_path.read_bytes()
    return hashlib.sha256(content).hexdigest()[:12]


def infer_label(file_path: Path) -> str:
    """
    Tries to label files as AI or Human based on folder/file names.
    """
    parts = [part.lower() for part in file_path.parts]
    stem = file_path.stem.lower()

    ai_terms = {"ai", "generated", "chatgpt", "copilot", "llm"}
    human_terms = {"human", "manual", "student", "real"}

    if any(part in ai_terms for part in parts) or stem.startswith("ai_"):
        return "AI"

    if any(part in human_terms for part in parts) or stem.startswith("human_"):
        return "Human"

    return "Unknown"


def analyse_file(file_path: Path, root: Path, dataset_name: str, run_id: str, analysed_at: str) -> dict:
    code = file_path.read_text(encoding="utf-8", errors="ignore")

    # -------------------------
    # Radon metrics
    # -------------------------
    raw = radon_analyse(code)
    cc_blocks = cc_visit(code)
    hal = h_visit(code)
    mi_score = mi_visit(code, multi=True)

    cc_values = [block.complexity for block in cc_blocks]

    return {
        # -------------------------
        # Run/filter info
        # -------------------------
        "run_id": run_id,
        "analysed_at": analysed_at,
        "dataset": dataset_name,
        "source_root": str(root),

        # -------------------------
        # File info
        # -------------------------
        "relative_path": str(file_path.relative_to(root)),
        "file": file_path.name,
        "folder": file_path.parent.name,
        "label": infer_label(file_path),
        "file_hash": file_hash(file_path),

        # -------------------------
        # Maintainability Index
        # -------------------------
        "mi": round(mi_score, 2),

        # -------------------------
        # Cyclomatic Complexity
        # -------------------------
        "cc_avg": round(safe_avg(cc_values), 2),
        "cc_max": max(cc_values) if cc_values else 0,
        "functions": len(cc_blocks),

        # -------------------------
        # Halstead metrics
        # -------------------------
        "halstead_volume": round(hal.total.volume, 2),
        "halstead_difficulty": round(hal.total.difficulty, 2),
        "halstead_effort": round(hal.total.effort, 2),

        # -------------------------
        # Line metrics
        # -------------------------
        "loc": raw.loc,
        "sloc": raw.sloc,
        "lloc": raw.lloc,
        "comments": raw.comments,
        "blank": raw.blank,
    }


def find_python_files(root: Path):
    return sorted(
        p for p in root.rglob("*.py")
        if p.is_file() and "__pycache__" not in p.parts
    )


def shorten(text, width):
    text = str(text)
    if len(text) <= width:
        return text
    return "..." + text[-(width - 3):]


def print_results_table(rows, limit=50):
    print("\n" + "=" * 115)
    print("PER-FILE RESULTS FOR THIS RUN")
    print("=" * 115)

    header = (
        f"{'Dataset':<18} "
        f"{'Label':<10} "
        f"{'File':<40} "
        f"{'MI':>7} "
        f"{'CC Avg':>8} "
        f"{'CC Max':>8} "
        f"{'LOC':>7} "
        f"{'Hal Vol':>10}"
    )

    print(header)
    print("-" * len(header))

    for row in rows[:limit]:
        print(
            f"{shorten(row['dataset'], 18):<18} "
            f"{row['label']:<10} "
            f"{shorten(row['relative_path'], 40):<40} "
            f"{row['mi']:>7.2f} "
            f"{row['cc_avg']:>8.2f} "
            f"{row['cc_max']:>8} "
            f"{row['loc']:>7} "
            f"{row['halstead_volume']:>10.2f}"
        )

    if len(rows) > limit:
        print(f"\nShowing first {limit} files only. Full results are saved in the CSV.")


def print_summary(rows):
    grouped = defaultdict(list)

    for row in rows:
        key = (row["dataset"], row["label"])
        grouped[key].append(row)

    print("\n" + "=" * 115)
    print("SUMMARY FOR THIS RUN")
    print("=" * 115)

    header = (
        f"{'Dataset':<22} "
        f"{'Label':<10} "
        f"{'Files':>7} "
        f"{'Avg MI':>10} "
        f"{'Avg CC':>10} "
        f"{'Max CC':>10} "
        f"{'Avg LOC':>10} "
        f"{'Total LOC':>10}"
    )

    print(header)
    print("-" * len(header))

    for (dataset, label), group in grouped.items():
        avg_mi = safe_avg([row["mi"] for row in group])
        avg_cc = safe_avg([row["cc_avg"] for row in group])
        max_cc = max(row["cc_max"] for row in group)
        avg_loc = safe_avg([row["loc"] for row in group])
        total_loc = sum(row["loc"] for row in group)

        print(
            f"{shorten(dataset, 22):<22} "
            f"{label:<10} "
            f"{len(group):>7} "
            f"{avg_mi:>10.2f} "
            f"{avg_cc:>10.2f} "
            f"{max_cc:>10} "
            f"{avg_loc:>10.2f} "
            f"{total_loc:>10}"
        )


def append_rows_to_csv(output_csv: Path, rows: list, fieldnames: list):
    """
    Appends results to the CSV instead of overwriting.

    If the CSV does not exist, it creates it and writes the header.
    If the CSV already exists, it appends new rows.
    """

    output_csv.parent.mkdir(parents=True, exist_ok=True)

    file_exists = output_csv.exists()
    file_has_content = file_exists and output_csv.stat().st_size > 0

    # New CSV file
    if not file_has_content:
        with output_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        return

    # Existing CSV file
    with output_csv.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        existing_fieldnames = reader.fieldnames or []

    if existing_fieldnames != fieldnames:
        print("\nWarning: existing CSV header is different from this script's header.")
        print("To avoid damaging your stored results, use a new CSV file or update the old CSV manually.")
        print(f"Existing columns: {existing_fieldnames}")
        print(f"New columns:      {fieldnames}")
        sys.exit(1)

    with output_csv.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(rows)


def main():
    if len(sys.argv) not in [3, 4]:
        print("Usage: python compare_metrics_to_csv.py <input_folder> <output_csv> [dataset_name]")
        print()
        print("Example:")
        print("python compare_metrics_to_csv.py datasets/human_vs_ai results/all_metrics.csv HumanVsAI")
        sys.exit(1)

    input_folder = Path(sys.argv[1])
    output_csv = Path(sys.argv[2])

    if len(sys.argv) == 4:
        dataset_name = sys.argv[3]
    else:
        dataset_name = input_folder.name

    if not input_folder.exists():
        print(f"Error: folder does not exist: {input_folder}")
        sys.exit(1)

    if not input_folder.is_dir():
        print(f"Error: input must be a folder: {input_folder}")
        sys.exit(1)

    py_files = find_python_files(input_folder)

    if not py_files:
        print("No Python files found in the folder.")
        sys.exit(0)

    analysed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    rows = []
    skipped = []

    print(f"Dataset: {dataset_name}")
    print(f"Run ID: {run_id}")
    print(f"Found {len(py_files)} Python files.\n")

    for file_path in py_files:
        try:
            row = analyse_file(
                file_path=file_path,
                root=input_folder,
                dataset_name=dataset_name,
                run_id=run_id,
                analysed_at=analysed_at,
            )
            rows.append(row)
            print(f"Analysed: {file_path}")
        except Exception as e:
            skipped.append((file_path, str(e)))
            print(f"Skipped: {file_path} | Reason: {e}")

    if not rows:
        print("\nNo files were successfully analysed.")
        sys.exit(1)

    fieldnames = [
        "run_id",
        "analysed_at",
        "dataset",
        "source_root",
        "relative_path",
        "file",
        "folder",
        "label",
        "file_hash",
        "mi",
        "cc_avg",
        "cc_max",
        "functions",
        "halstead_volume",
        "halstead_difficulty",
        "halstead_effort",
        "loc",
        "sloc",
        "lloc",
        "comments",
        "blank",
    ]

    append_rows_to_csv(output_csv, rows, fieldnames)

    print_results_table(rows)
    print_summary(rows)

    print("\n" + "=" * 115)
    print("DONE")
    print("=" * 115)
    print(f"Successfully analysed this run: {len(rows)} files")
    print(f"Skipped files this run: {len(skipped)}")
    print(f"Results appended to: {output_csv}")
    print()
    print("Useful CSV filters:")
    print("- dataset")
    print("- label")
    print("- run_id")
    print("- analysed_at")
    print("- source_root")
    print("- folder")
    print("- file_hash")

    if skipped:
        print("\nSkipped files:")
        for file_path, reason in skipped:
            print(f"- {file_path}: {reason}")


if __name__ == "__main__":
    main()