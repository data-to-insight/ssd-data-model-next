from pathlib import Path
import yaml

SCHEMA_DIR = Path("schema")
all_categories = set()

for file in SCHEMA_DIR.glob("*.yml"):
    with open(file, "r", encoding="utf-8") as f:
        try:
            content = yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading {file.name}: {e}")
            continue

    for node in content.get("nodes", []):
        for cat in node.get("categories", []):
            all_categories.add(cat.lower().replace("-", "_"))

        for field in node.get("fields", []):
            for cat in field.get("categories", []):
                all_categories.add(cat.lower().replace("-", "_"))

print("✅ Unique category values found:\n")
for cat in sorted(all_categories):
    print(f"- {cat}")
