# PYTHONPATH=. python scripts/docs.generate_domain_erds.py
from pathlib import Path
from collections import defaultdict
import yaml
import subprocess

# Output format: "svg" or "png"
OUTPUT_FORMAT = "svg"
CATEGORY_SCOPE = "field"  # Options: "node", "field", or "both"

SCHEMA_PATH = Path("schema")
IMAGE_DIR = Path("docs/assets/images")
DOT_DIR = Path("docs/dot")
DOT_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# Expanded domain mapping
DOMAIN_MAP = {
    "cla": ["looked_after", "care_plan", "placement", "substance_misuse", "visits", "reviews", "episodes"],
    "cin": ["child_in_need", "assessment", "plan", "referral", "visit", "factors", "need", "contact"],
    "cp": ["child_protection", "conference", "cp_plan", "review", "visit", "pre_proceedings","s47_enquiry", "initial_cp_conference"],
    "identity": ["identity", "address", "linked_identifiers",  "immigration", "mother", "convictions", "sdq", "voice_of_child"],
    "health": ["health", "disability", "immunisations"],
    "ehcp": ["ehcp", "ehcp_request", "ehcp_assessment"],
    "send": ["send"],
    "early_help": ["early_help", "family"],
    "care_leavers": ["care_leavers", "adoption", "permanence"],
    "finance": ["finance"],
    "workforce": ["workforce"],
    "ssd_admin": ["admin"]
}
def normalise_tags(raw_tags):
    return [t.strip().lower().replace("-", "_") for t in raw_tags]

def collect_entities_by_domain():
    grouped = defaultdict(list)
    seen = set()  # Track (domain, table_name) to prevent duplication

    for yml_file in SCHEMA_PATH.glob("*.yml"):
        with open(yml_file, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)

        for node in content.get("nodes", []):
            table_name = node["name"]
            node_tags = normalise_tags(node.get("categories", []))

            if CATEGORY_SCOPE in ("node", "both"):
                for domain, valid_tags in DOMAIN_MAP.items():
                    if any(tag in valid_tags for tag in node_tags):
                        key = (domain, table_name)
                        if key not in seen:
                            grouped[domain].append((table_name, node))
                            seen.add(key)

            if CATEGORY_SCOPE in ("field", "both"):
                for field in node.get("fields", []):
                    field_tags = normalise_tags(field.get("categories", []))
                    for domain, valid_tags in DOMAIN_MAP.items():
                        key = (domain, table_name)
                        if key not in seen and any(tag in valid_tags for tag in field_tags):
                            grouped[domain].append((table_name, node))
                            seen.add(key)

    return grouped



def generate_dot_for_domain(domain, entities):
    nodes = {}
    edges = []

    for table_name, node in entities:
        if table_name not in nodes:
            nodes[table_name] = []

        for field in node.get("fields", []):
            label = field["name"]
            if field.get("primary_key"):
                label += " PK"
            elif field.get("foreign_key"):
                label += f" → {field['foreign_key']}"
                try:
                    ref_table, ref_field = field["foreign_key"].split(".")
                    edges.append((table_name, ref_table, field["name"]))
                except ValueError:
                    print(f"Malformed foreign_key: {field['foreign_key']} in {table_name}.{field['name']}")
            nodes[table_name].append(label)

    lines = [
        'digraph G {',
        '  node [shape=record];'
    ]

    for table_name, fields in nodes.items():
        joined = "\\l".join(fields) + "\\l"
        lines.append(f'  {table_name} [label="{{{table_name}|{joined}}}"];')

    for from_table, to_table, label in edges:
        lines.append(f'  {from_table} -> {to_table} [label="{label}"];')

    lines.append("}")

    dot_path = DOT_DIR / f"erd_{domain}.dot"
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"DOT written: {dot_path}")

    # Generate SVG or PNG
    image_path = IMAGE_DIR / f"erd_{domain}.{OUTPUT_FORMAT}"
    try:
        subprocess.run(["dot", f"-T{OUTPUT_FORMAT}", str(dot_path), "-o", str(image_path)], check=True)
        print(f"Image generated: {image_path}")
    except FileNotFoundError:
        print("'dot' command not found. Please install Graphviz.")

def generate_all_domain_diagrams():
    grouped_entities = collect_entities_by_domain()
    for domain in DOMAIN_MAP:
        entities = grouped_entities.get(domain, [])
        if entities:
            generate_dot_for_domain(domain, entities)
        else:
            print(f"No entities found for domain: {domain}")

generate_all_domain_diagrams()
