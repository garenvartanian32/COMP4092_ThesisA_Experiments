from pathlib import Path
from datasets import load_dataset

LIMIT = 500

base_dir = Path("datasets/humanvsai")
human_dir = base_dir / "human"
chatgpt_dir = base_dir / "chatgpt"
dsc_dir = base_dir / "dsc"
qwen_dir = base_dir / "qwen"

for d in [human_dir, chatgpt_dir, dsc_dir, qwen_dir]:
    d.mkdir(parents=True, exist_ok=True)

def is_python(code: str) -> bool:
    if not isinstance(code, str) or not code.strip():
        return False
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False

loaded = load_dataset("OSS-forge/HumanVsAICode")
ds = loaded["train"]

count = 0

for i, row in enumerate(ds):
    if count >= LIMIT:
        break

    human_code = row.get("human_code")
    chatgpt_code = row.get("chatgpt_code")
    dsc_code = row.get("dsc_code") or row.get("deepseek_code")
    qwen_code = row.get("qwen_code")

    # only keep rows where the human version looks like valid Python
    if not is_python(human_code):
        continue

    if isinstance(human_code, str) and human_code.strip():
        (human_dir / f"human_{count}.py").write_text(human_code, encoding="utf-8")

    if isinstance(chatgpt_code, str) and chatgpt_code.strip():
        (chatgpt_dir / f"chatgpt_{count}.py").write_text(chatgpt_code, encoding="utf-8")

    if isinstance(dsc_code, str) and dsc_code.strip():
        (dsc_dir / f"dsc_{count}.py").write_text(dsc_code, encoding="utf-8")

    if isinstance(qwen_code, str) and qwen_code.strip():
        (qwen_dir / f"qwen_{count}.py").write_text(qwen_code, encoding="utf-8")

    count += 1

print(f"Done. Extracted {count} Python rows.")