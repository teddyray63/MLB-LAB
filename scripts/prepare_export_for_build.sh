#!/usr/bin/env sh
set -eu

usage() {
  cat <<'EOF'
Usage: scripts/prepare_export_for_build.sh EXPECTED_SHA256 SOURCE_PATH

Verify SOURCE_PATH matches EXPECTED_SHA256, then install it at data/daily_export.json
for web-dashboard build (prebuild sync-data / Vite closeBundle).

Example:
  scripts/prepare_export_for_build.sh \\
    d73cd29001c2e8e26c3bbfc43186f979c1d8afefb8138c2107d4b13d6328d509 \\
    data/candidates/daily_export.2026-08-14.real.json
EOF
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 0
fi

if [ "$#" -ne 2 ]; then
  usage >&2
  exit 1
fi

EXPECTED_SHA="$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')"
SOURCE="$2"

validate_sha256() {
  _sha=$1
  if [ "${#_sha}" -ne 64 ]; then
    return 1
  fi
  case "$_sha" in
    *[!0123456789abcdef]*) return 1 ;;
  esac
  return 0
}

if ! validate_sha256 "$EXPECTED_SHA"; then
  echo "prepare_export_for_build: invalid SHA256: $1" >&2
  exit 1
fi

if [ ! -f "$SOURCE" ]; then
  echo "prepare_export_for_build: source not found: $SOURCE" >&2
  exit 1
fi

ROOT="$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/data/daily_export.json"

abs_path() {
  _target=$1
  _dir=$(dirname "$_target")
  _base=$(basename "$_target")
  _dir=$(CDPATH= cd -- "$_dir" && pwd)
  printf '%s/%s' "$_dir" "$_base"
}

SOURCE_ABS="$(abs_path "$SOURCE")"
DEST_ABS="$(abs_path "$DEST")"

sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  else
    shasum -a 256 "$1" | awk '{print $1}'
  fi
}

SOURCE_SHA="$(sha256_file "$SOURCE_ABS" | tr '[:upper:]' '[:lower:]')"

if [ "$SOURCE_SHA" != "$EXPECTED_SHA" ]; then
  echo "prepare_export_for_build: SHA256 mismatch" >&2
  echo "  expected: $EXPECTED_SHA" >&2
  echo "  actual:   $SOURCE_SHA" >&2
  echo "  source:   $SOURCE_ABS" >&2
  exit 1
fi

if [ "$SOURCE_ABS" = "$DEST_ABS" ]; then
  echo "prepare_export_for_build: source is already data/daily_export.json (SHA verified)"
  echo "  sha256: $EXPECTED_SHA"
  echo "  path:   $DEST_ABS"
  exit 0
fi

mkdir -p "$(dirname "$DEST_ABS")"
cp -f "$SOURCE_ABS" "$DEST_ABS"

DEST_SHA="$(sha256_file "$DEST_ABS" | tr '[:upper:]' '[:lower:]')"
if [ "$DEST_SHA" != "$EXPECTED_SHA" ]; then
  echo "prepare_export_for_build: destination SHA256 mismatch after copy" >&2
  echo "  expected: $EXPECTED_SHA" >&2
  echo "  actual:   $DEST_SHA" >&2
  echo "  dest:     $DEST_ABS" >&2
  exit 1
fi

echo "prepare_export_for_build: OK"
echo "  sha256: $EXPECTED_SHA"
echo "  from:   $SOURCE_ABS"
echo "  to:     $DEST_ABS"
