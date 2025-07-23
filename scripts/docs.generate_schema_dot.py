# PYTHONPATH=. python scripts/docs.generate_schema_dot.py

from pathlib import Path
import subprocess
import yaml

# --- CONFIGURATION ---
SCHEMA_PATH = Path("schema")
DOT_OUTPUT_DIR = Path("docs/dot")
IMAGE_OUTPUT_DIR = Path("docs/assets/images")
DOT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_dot_from_yml():
    dot_lines = [
        'digraph G {',
        '  node [shape=record];'
    ]

    nodes = {}
    edges = []

    for yml_file in SCHEMA_PATH.glob("*.yml"):
        with open(yml_file, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)

        for node in content.get("nodes", []):
            table_name = node["name"]
            field_lines = []

            for field in node.get("fields", []):
                field_label = field["name"]
                if field.get("primary_key"):
                    field_label += " PK"
                elif field.get("foreign_key"):
                    field_label += f" → {field['foreign_key']}"
                field_lines.append(field_label)

                if "foreign_key" in field:
                    try:
                        ref_table, _ = field["foreign_key"].split(".")
                        edges.append((table_name, ref_table, field["name"]))
                    except ValueError:
                        print(f"Malformed foreign_key: {field['foreign_key']} in {table_name}.{field['name']}")

            joined_fields = "\\l".join(field_lines) + "\\l"
            label = f'{{{table_name}|{joined_fields}}}'
            nodes[table_name] = f'  {table_name} [label="{label}"];'

    dot_lines.extend(nodes.values())
    for from_table, to_table, label in edges:
        dot_lines.append(f'  {from_table} -> {to_table} [label="{label}"];')
    dot_lines.append("}")

    dot_path = DOT_OUTPUT_DIR / "schema_diagram.dot"
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write("\n".join(dot_lines))
    print(f"DOT file written: {dot_path}")

    for fmt in ["svg", "png"]:
        output_path = IMAGE_OUTPUT_DIR / f"schema_diagram.{fmt}"
        try:
            subprocess.run(
                ["dot", f"-T{fmt}", str(dot_path), "-o", str(output_path)],
                check=True
            )
            print(f"{fmt.upper()} generated at: {output_path}")
        except FileNotFoundError:
            print("Graphviz 'dot' not found. Please install it to generate diagrams.")
        except subprocess.CalledProcessError as e:
            print(f"Error generating {fmt.upper()}: {e}")

generate_dot_from_yml()
