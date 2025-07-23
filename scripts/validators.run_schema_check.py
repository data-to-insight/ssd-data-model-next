# Will validate all schema/*.yml files using Pydantic

# PYTHONPATH=. python scripts/validators.run_schema_check.py

from pathlib import Path
import yaml
from schema_model import NodeFile, RelationshipFile
from pydantic import ValidationError

def validate_all_yml(path: Path):
    yml_files = list(path.glob("*.yml"))
    errors = []

    for yml_file in yml_files:
        try:
            with open(yml_file, "r", encoding="utf-8") as f:
                raw = yaml.safe_load(f)

            if yml_file.name == "relationships.yml":
                RelationshipFile.model_validate(raw)
            else:
                NodeFile.model_validate(raw)

            print(f"✅ Valid: {yml_file.name}")
        except ValidationError as ve:
            print(f"❌ Validation error in {yml_file.name}")
            errors.append((yml_file.name, ve))
        except Exception as e:
            print(f"General error in {yml_file.name}: {e}")
            errors.append((yml_file.name, e))

    if errors:
        print("\nSummary of validation issues:")
        for fname, err in errors:
            print(f"\n{fname}:\n{err}")
    else:
        print("\nAll files passed validation.")

if __name__ == "__main__":
    validate_all_yml(Path("ssd-reference/objects"))
