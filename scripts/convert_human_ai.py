import csv
from pathlib import Path

dataset_dir = Path("datasets/human_vs_ai")
csv_files = list(dataset_dir.rglob("*.csv"))

input_file = csv_files[0]
print(f"Using file: {input_file}")

human_dir = dataset_dir / "human"
ai_dir = dataset_dir / "ai"

human_dir.mkdir(exist_ok=True)
ai_dir.mkdir(exist_ok=True)

with open(input_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for i, row in enumerate(reader):
        language = row.get("language", "")

        # only keep Python
        if "python" not in language.lower():
            continue

        ai_code = row.get("ai_generated_code")
        human_code = row.get("human_generated_code")

        if ai_code:
            with open(ai_dir / f"ai_{i}.py", "w", encoding="utf-8") as f:
                f.write(ai_code)

        if human_code:
            with open(human_dir / f"human_{i}.py", "w", encoding="utf-8") as f:
                f.write(human_code)

print("Done. Files created.")