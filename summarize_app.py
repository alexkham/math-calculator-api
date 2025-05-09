import os

BASE_DIR = "."
OUTPUT_FILE = "app_summary.py"

EXCLUDE_DIRS = {"__pycache__", ".git", "venv", ".venv", "env", "math-api-venv"}

structure = {}
content = {}

def should_exclude(path):
    parts = set(path.split(os.sep))
    return not parts.isdisjoint(EXCLUDE_DIRS)

for root, _, files in os.walk(BASE_DIR):
    if should_exclude(root):
        continue
    for file in files:
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, BASE_DIR)

        if should_exclude(rel_path):
            continue

        structure[rel_path] = ""
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                code = f.read().strip()
                snippet = code if len(code) <= 1000 else code[:1000] + "\n# ...truncated..."
                content[rel_path] = snippet
        except Exception as e:
            content[rel_path] = f"# Could not read file: {e}"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("structure = {\n")
    for path in structure:
        f.write(f'    "{path}": "",\n')
    f.write("}\n\n")

    f.write("content = {\n")
    for path in content:
        snippet = content[path].replace('"""', '\\"\\"\\"')
        f.write(f'    "{path}": """{snippet}""",\n')
    f.write("}\n")

print(f"✅ Summary written to {OUTPUT_FILE}")
