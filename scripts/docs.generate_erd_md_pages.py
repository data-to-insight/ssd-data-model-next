# PYTHONPATH=. python scripts/docs.generate_erd_pages.py

from pathlib import Path
import os

# --- CONFIG---
IMAGE_SUBFOLDER = "assets/images"
DOT_SUBFOLDER = "dot"
MARKDOWN_SUBFOLDER = "schema"
IMAGE_EXT = os.getenv("ERD_IMAGE_TYPE", "svg")  # "svg" or "png"
DOCS_DIR = Path("docs")
DOMAINS = ["cla", "cin", "cp"]

# Ensure folders exist
(DOCS_DIR / IMAGE_SUBFOLDER).mkdir(parents=True, exist_ok=True)
(DOCS_DIR / DOT_SUBFOLDER).mkdir(parents=True, exist_ok=True)
(DOCS_DIR / MARKDOWN_SUBFOLDER).mkdir(parents=True, exist_ok=True)

# --- MARKDOWN WRITER ---
for domain in DOMAINS:
    image_filename = f"erd_{domain}.{IMAGE_EXT}"
    image_path = DOCS_DIR / IMAGE_SUBFOLDER / image_filename
    dot_path = DOCS_DIR / DOT_SUBFOLDER / f"erd_{domain}.dot"
    md_path = DOCS_DIR / MARKDOWN_SUBFOLDER / f"erd_{domain}.md"

    if not image_path.exists():
        print(f"Missing: {image_path} — skipping.")
        continue

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {domain.upper()} ERD\n\n")
        f.write(f"![{domain.upper()} ERD](../{IMAGE_SUBFOLDER}/{image_filename})\n\n")
        f.write(f"[🔍 View full image](../{IMAGE_SUBFOLDER}/{image_filename}) &nbsp;|&nbsp; ")
        f.write(f"[⬇️ Download {IMAGE_EXT.upper()}](../{IMAGE_SUBFOLDER}/{image_filename})\n\n")
        f.write(f"[⬇️ Download DOT file](../{DOT_SUBFOLDER}/erd_{domain}.dot)\n")


    print(f"Created Markdown page: {md_path}")

