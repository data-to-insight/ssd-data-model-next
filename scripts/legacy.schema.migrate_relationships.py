# PYTHONPATH=. python scripts/schema.migrate_relationships.py
#  Script to migrate relationships.yml into foreign_key fields

import yaml
from pathlib import Path

SCHEMA_PATH = Path("schema")
RELATIONSHIPS_FILE = SCHEMA_PATH / "relationships.yml"

def migrate_relationships_to_foreign_keys():
    # Load relationships.yml
    with open(RELATIONSHIPS_FILE, "r", encoding="utf-8") as f:
        relationships_data = yaml.safe_load(f)

    relationships = relationships_data.get("relationships", [])
    updated_files = []

    for relation in relationships:
        child_object = relation["child_object"]
        child_key = relation["child_key"]
        parent_object = relation["parent_object"]
        parent_key = relation["parent_key"]
        fk_value = f"{parent_object}.{parent_key}"

        child_file_path = SCHEMA_PATH / f"{child_object}.yml"
        if not child_file_path.exists():
            print(f"Missing file for child object: {child_object}")
            continue

        with open(child_file_path, "r", encoding="utf-8") as f:
            node_data = yaml.safe_load(f)

        modified = False
        for node in node_data.get("nodes", []):
            for field in node.get("fields", []):
                if field.get("name") == child_key:
                    current_fk = field.get("foreign_key")
                    print(f"{child_object}.{child_key} → expected foreign_key: {fk_value}")
                    print(f"   current: {current_fk if current_fk else 'None'}")
                    if current_fk != fk_value:
                        field["foreign_key"] = fk_value
                        modified = True
                        print(f"Updated foreign_key in {child_object}.yml for field {child_key} → {fk_value}")

        if modified:
            with open(child_file_path, "w", encoding="utf-8") as f:
                yaml.dump(node_data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
            updated_files.append(child_file_path.name)

    print("\nMigration complete.")
    if updated_files:
        print("Files updated:")
        for fname in updated_files:
            print(f" - {fname}")
    else:
        print("No changes needed — all foreign keys already present or matched expected values.")

if __name__ == "__main__":
    migrate_relationships_to_foreign_keys()
