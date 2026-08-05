#!/bin/bash
# chmod +x scripts/lite-update-legacy-ssd.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
TARGET_DIR="$REPO_ROOT/ssd-legacy-clone"

mkdir -p "$TARGET_DIR"

TMP_DIR=$(mktemp -d)

git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/data-to-insight/ssd-data-model.git \
  "$TMP_DIR"

(
  cd "$TMP_DIR"
  git sparse-checkout set deployment_extracts
)

rsync -av --delete \
  "$TMP_DIR/deployment_extracts/" \
  "$TARGET_DIR/"

rm -rf "$TMP_DIR"

echo "legacy SSD deployment_extracts updated in $TARGET_DIR"