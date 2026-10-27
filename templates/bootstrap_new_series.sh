#!/usr/bin/env bash
# ==============================================================================
# Bootstrap New Vertical Series Project
# Initializes a self-contained, project-local production workspace from template
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DIR="${SCRIPT_DIR}/video-series-template"

usage() {
  echo "Usage: $0 --name <series_name> --target <target_path>"
  echo ""
  echo "Arguments:"
  echo "  --name    Human-readable name or slug for the series (e.g., 'village-detective')"
  echo "  --target  Destination directory path for the new series workspace"
  echo ""
  echo "Example:"
  echo "  $0 --name 'village-detective' --target '/media/vedha/E2/freelance/yt-series/village-detective'"
  exit 1
}

SERIES_NAME=""
TARGET_DIR=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)
      SERIES_NAME="$2"
      shift 2
      ;;
    --target)
      TARGET_DIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "Unknown argument: $1"
      usage
      ;;
  esac
done

if [ -z "${SERIES_NAME}" ] || [ -z "${TARGET_DIR}" ]; then
  echo "[ERROR] Both --name and --target are required."
  usage
fi

if [ -d "${TARGET_DIR}" ]; then
  echo "[WARNING] Target directory already exists: ${TARGET_DIR}"
  read -p "Do you want to proceed and populate missing files? [y/N]: " confirm
  if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
  fi
fi

echo "=== Initializing New Series: ${SERIES_NAME} ==="
echo "Target Directory: ${TARGET_DIR}"

mkdir -p "${TARGET_DIR}"

# Copy template files preserving structure
cp -r "${TEMPLATE_DIR}/"* "${TARGET_DIR}/"
cp -r "${TEMPLATE_DIR}/.agents" "${TARGET_DIR}/"

# Customize series name in README and config if placeholders exist
if [ -f "${TARGET_DIR}/config/config.example.yaml" ]; then
  sed -i "s/Match Fixers/${SERIES_NAME}/g" "${TARGET_DIR}/config/config.example.yaml"
fi
if [ -f "${TARGET_DIR}/config/config.example.json" ]; then
  sed -i "s/Match Fixers/${SERIES_NAME}/g" "${TARGET_DIR}/config/config.example.json"
fi

# Ensure executable permissions on scripts and tests
chmod +x "${TARGET_DIR}/scripts/core/"*.sh 2>/dev/null || true
chmod +x "${TARGET_DIR}/scripts/core/"*.py 2>/dev/null || true
chmod +x "${TARGET_DIR}/tests/"*.py 2>/dev/null || true

# Initialize .env from example if not already present
if [ ! -f "${TARGET_DIR}/config/.env" ]; then
  cp "${TARGET_DIR}/config/.env.example" "${TARGET_DIR}/config/.env"
  echo "[OK] Created initial config/.env from template."
fi

echo ""
echo "=== Running Initial Environment & Structure Verification ==="
python3 "${TARGET_DIR}/tests/test_environment.py"

echo ""
echo "=============================================================================="
echo "[SUCCESS] Project '${SERIES_NAME}' successfully initialized at:"
echo "          ${TARGET_DIR}"
echo ""
echo "Next Steps:"
echo "  1. cd ${TARGET_DIR}"
echo "  2. Edit config/.env with your SARVAM_API_KEY and credentials"
echo "  3. Add character turnaround references to assets/references/"
echo "  4. Define screenplays in episodes_detailed.md"
echo "=============================================================================="
