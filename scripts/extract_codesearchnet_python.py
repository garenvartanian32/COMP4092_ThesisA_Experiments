from pathlib import Path
from datasets import load_dataset

LIMIT = 500  # change to 1000 if you want

out_dir = Path("datasets/codesearchnet_python/files")
out_dir.mkdir(parents=True, exist_ok=True)

print("Loading dataset...")
ds = load_dataset("Nan-Do/code-search-net-python", split="train")

print(f"Loaded {len(ds)} rows")
count = 0

for i, row in enumerate(ds):
    if count >= LIMIT:
        break

    # try likely code fields
    code = (
        row.get("code")
        or row.get("func_code_string")
        or row.get("function")
    )

    if not isinstance(code, str) or not code.strip():
        continue

    (out_dir / f"{count}.py").write_text(code, encoding="utf-8")
    count += 1

print(f"Created {count} Python files.")