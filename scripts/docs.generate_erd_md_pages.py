# PYTHONPATH=. python scripts/docs.generate_erd_md_pages.py

from pathlib import Path
import os
import yaml

# --- CONFIG ---
IMAGE_SUBFOLDER = "assets/images"
DOT_SUBFOLDER = "dot"
MARKDOWN_SUBFOLDER = "schema"
SCHEMA_DIR = Path("schema")
IMAGE_EXT = os.getenv("ERD_IMAGE_TYPE", "svg")  # "svg" or "png"
DOCS_DIR = Path("docs")

# becomes the .md pages, needs to align with mkdocs.yml nav
DOMAINS = ["cla", "cin", "cp","identity", "health", "ehcp", "send","early_help", "care_leavers", "finance", "workforce", "ssd_admin"]

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


# Ensure output folders exist
(DOCS_DIR / IMAGE_SUBFOLDER).mkdir(parents=True, exist_ok=True)
(DOCS_DIR / DOT_SUBFOLDER).mkdir(parents=True, exist_ok=True)
(DOCS_DIR / MARKDOWN_SUBFOLDER).mkdir(parents=True, exist_ok=True)

# Load schema
def load_schema():
    tables = {}
    for file in SCHEMA_DIR.glob("*.yml"):
        with open(file, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
            for node in content.get("nodes", []):
                tables[node["name"]] = node
    return tables

schema = load_schema()

# --- DOMAIN PAGE WRITER ---
for domain in DOMAINS:
    image_filename = f"erd_{domain}.{IMAGE_EXT}"
    image_path = DOCS_DIR / IMAGE_SUBFOLDER / image_filename
    dot_path = DOCS_DIR / DOT_SUBFOLDER / f"erd_{domain}.dot"
    md_path = DOCS_DIR / MARKDOWN_SUBFOLDER / f"erd_{domain}.md"

    if not image_path.exists():
        print(f"Missing image: {image_path} — skipping.")
        continue

    domain_tables = []

    for table_name, table_def in sorted(schema.items()):
        raw_tags = table_def.get("categories") or []
        table_tags = [tag.lower().replace("-", "_") for tag in raw_tags]

        if not any(tag in DOMAIN_MAP[domain] for tag in table_tags):
            for field in table_def.get("fields", []):
                field_tags = field.get("categories") or []
                field_tags = [tag.lower().replace("-", "_") for tag in field_tags]
                if any(tag in DOMAIN_MAP[domain] for tag in field_tags):
                    domain_tables.append((table_name, table_def))
                    break
        else:
            domain_tables.append((table_name, table_def))

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {domain.upper()} ERD\n\n")
        f.write(f"![{domain.upper()} ERD](../{IMAGE_SUBFOLDER}/{image_filename})\n\n")
        f.write(f"[View full image](../{IMAGE_SUBFOLDER}/{image_filename})  |  ")
        f.write(f"[Download {IMAGE_EXT.upper()}](../{IMAGE_SUBFOLDER}/{image_filename})  |  ")
        f.write(f"[Download DOT file](../{DOT_SUBFOLDER}/erd_{domain}.dot)\n\n")

        f.write(f"## Table Field Previews\n\n")
        f.write(f"**Tables in domain:** {len(domain_tables)}\n\n")

        for table_name, table_def in sorted(domain_tables):
            f.write("<details>\n")
            f.write(f"<summary><strong>{table_name}</strong></summary>\n\n")

            f.write("<table>\n<thead>\n<tr><th>Field</th><th>Type</th><th>Notes</th></tr>\n</thead>\n<tbody>\n")
            for field in table_def.get("fields", []):
                name = field["name"]
                dtype = field.get("type", "")
                notes = []
                if field.get("primary_key"):
                    notes.append("PK")
                if field.get("foreign_key"):
                    fk = field["foreign_key"]
                    target_table = fk.split(".")[0]
                    if target_table in dict(domain_tables):
                        notes.append(f'FK → <a href="#{target_table.lower()}">{target_table}</a>')
                    else:
                        notes.append(f"FK → {target_table}")
                if field.get("enum"):
                    notes.append("enum")
                if field.get("nullable"):
                    notes.append("nullable")
                if field.get("optional"):
                    notes.append("optional")
                notes_str = "; ".join(notes)
                f.write(f"<tr><td>{name}</td><td>{dtype}</td><td>{notes_str}</td></tr>\n")
            f.write("</tbody>\n</table>\n\n")

            f.write("</details>\n\n")



    print(f"Created Markdown page: {md_path}")
