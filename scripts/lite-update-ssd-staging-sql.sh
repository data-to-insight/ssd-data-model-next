#!/bin/bash
# chmod +x scripts/lite-update-ssd-staging-sql.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
TARGET_DIR="$REPO_ROOT/ssd-data-staging-clone"

mkdir -p "$TARGET_DIR"

TMP_DIR=$(mktemp -d)

git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/data-to-insight/dfe-csc-api-data-flows.git \
  "$TMP_DIR"

(
  cd "$TMP_DIR"
  git sparse-checkout set build_dfe_payload_staging
)

cp -f \
  "$TMP_DIR/build_dfe_payload_staging/populate_ssd_api_data_staging_2016.sql" \
  "$TARGET_DIR/"

rm -rf "$TMP_DIR"

echo "populate_ssd_api_data_staging_2016.sql updated"