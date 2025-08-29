# Scripts

Contains Python scripts used for admin and dev-data tasks across SSD data model or data refresh.

---

## Script Naming Convention

Scripts follow the naming pattern:


| Area         | Purpose                                      |
|--------------|----------------------------------------------|
| `schema`     | Anything related to schema modelling or structure |
| `docs`       | Documentation-related generation or updates  |
| `data`       | Data transformation, imports, or conversion  |
| `validators` | Schema or data validation tasks              |

| Action       | Purpose                                      |
|--------------|----------------------------------------------|
| `generate`   | Script generates files, graphs, or markdown  |
| `migrate`    | Script transforms or updates existing assets |
| `convert`    | Script converts from one format to another   |
| `run`        | Script executes a check or validation        |

---

## Examples

| Filename                             | Description                                        |
|-------------------------------------|----------------------------------------------------|
| `schema.generate_dot.py`            | Generates DOT graph files from YML object schema   |
| `schema.migrate_relationships.py`   | Migrate standalone `relationships.yml` into inline foreign_key refs |
| `docs.generate_index.py`            | Create markdown pages for ERD visualisation       |
| `data.convert_csv_to_yml.py`        | Convert legacy CSV metadata into YAML format      |
| `validators.run_schema_check.py`    | Validate YML objects against Pydantic models      |

---

## Notes

- All scripts assumed to run from repo root:

  ```bash
  PYTHONPATH=. python scripts/<script_name>.py


## Dev notes

Locate/search scripts by type:

 ```bash
ls scripts/schema.*
ls scripts/data.*

Adding a new .yml/SSD object

