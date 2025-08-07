from pathlib import Path
import yaml
from collections import defaultdict

SCHEMA_DIR = Path("schema")
DOMAIN_MAP = {
    # 
    "cla": ["looked_after", "care_plan", "placement", "substance_misuse", "visits", "reviews", "episodes"],
    "cin": ["child_in_need", "assessment", "plan", "referral", "visit", "factors", "need", "contact"],
    "cp": ["child_protection", "conference", "cp_plan", "review", "visit", "pre_proceedings", "s47_enquiry", "initial_cp_conference"],
    "identity": ["identity", "address", "linked_identifiers", "immigration", "mother", "convictions", "sdq", "voice_of_child", "health", "immunisations"],
    "health": ["disability"],
    "ehcp": ["ehcp", "ehcp_request", "ehcp_assessment"],
    "send": ["send"],
    "early_help": ["early_help", "family"],
    "care_leavers": ["care_leavers", "adoption", "permanence"],
    "finance": ["finance"],
    "workforce": ["workforce"],
    "ssd_admin": ["admin"]
}

def normalise(tags):
    return [t.lower().replace("-", "_") for t in tags]

def infer_domain_from_field_tags(field_tags):
    domain_counts = defaultdict(int)
    for tag in field_tags:
        for domain, valid_tags in DOMAIN_MAP.items():
            if tag in valid_tags:
                domain_counts[domain] += 1
    if len(domain_counts) == 1:
        return next(iter(domain_counts))
    return None

def audit_and_enrich_node_categories():
    updated = 0
    for file in SCHEMA_DIR.glob("*.yml"):
        with open(file, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)

        changed = False
        malformed_indices = []

        for node in content.get("nodes", []):
            # Clean malformed field entries
            valid_fields = []
            for i, field in enumerate(node.get("fields", [])):
                if isinstance(field, dict) and "name" in field:
                    valid_fields.append(field)
                else:
                    malformed_indices.append((file.name, node.get("name", "?"), i))
            node["fields"] = valid_fields

            # Enrich node-level categories if missing or empty
            if "categories" in node and node["categories"]:
                continue

            all_field_tags = []
            for field in node.get("fields", []):
                all_field_tags.extend(normalise(field.get("categories", [])))

            if not all_field_tags:
                continue

            inferred = infer_domain_from_field_tags(all_field_tags)
            if inferred:
                node["categories"] = DOMAIN_MAP[inferred]
                node["_inferred"] = True
                changed = True

        if changed:
            with open(file, "w", encoding="utf-8") as f:
                yaml.dump(content, f, sort_keys=False)
            print(f"Updated categories in: {file.name}")
            updated += 1

        for fname, nname, idx in malformed_indices:
            print(f"Malformed field entry removed in {fname} (node: {nname}, index: {idx})")

    print(f"\nAudit & enrichment complete. {updated} files updated.")

if __name__ == "__main__":
    audit_and_enrich_node_categories()
