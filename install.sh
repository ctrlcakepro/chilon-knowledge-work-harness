#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR=""
SKIP_AUTOMATIONS=0

print_step() {
  printf '[harness-installer] %s\n' "$1"
}

usage() {
  cat <<'EOF'
Usage:
  ./install.sh [--target /path/to/project] [--skip-automations]

Options:
  --target <dir>       Target project directory to install Chilon into.
  --skip-automations  Do not install Codex automation TOML files.
  -h, --help          Show this help message.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --target" >&2
        exit 1
      fi
      TARGET_DIR="$2"
      shift 2
      ;;
    --skip-automations)
      SKIP_AUTOMATIONS=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -z "$TARGET_DIR" ]]; then
  read -r -p "Enter the absolute path of the target project directory: " TARGET_DIR
fi

if [[ -z "$TARGET_DIR" ]]; then
  echo "No target directory provided. Installation cancelled." >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
RESOLVED_TARGET="$(cd "$TARGET_DIR" && pwd)"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP_ROOT="$RESOLVED_TARGET/.harness-install-backup/$TIMESTAMP"
mkdir -p "$BACKUP_ROOT"

copy_with_backup() {
  local source_path="$1"
  local destination_path="$2"
  local backup_root="$3"

  if [[ -e "$destination_path" ]]; then
    local backup_path="$backup_root/$(basename "$destination_path")"
    print_step "Backup existing item: $destination_path -> $backup_path"
    cp -R "$destination_path" "$backup_path"
    rm -rf "$destination_path"
  fi

  print_step "Install item: $destination_path"
  cp -R "$source_path" "$destination_path"
}

items_to_install=(
  "AGENTS.md"
  "PROJECT-WORKFLOW.md"
  ".project-memory"
  "harness-regression"
  "tools"
)

print_step "Install target: $RESOLVED_TARGET"
print_step "Backup root: $BACKUP_ROOT"

for item in "${items_to_install[@]}"; do
  source_path="$SCRIPT_DIR/$item"
  if [[ ! -e "$source_path" ]]; then
    echo "Package is missing required item: $item" >&2
    exit 1
  fi
  destination_path="$RESOLVED_TARGET/$item"
  copy_with_backup "$source_path" "$destination_path" "$BACKUP_ROOT"
done

if [[ "$SKIP_AUTOMATIONS" -eq 0 ]]; then
  automation_source="$SCRIPT_DIR/automations"
  if [[ -d "$automation_source" ]]; then
    codex_automation_root="$HOME/.codex/automations"
    mkdir -p "$codex_automation_root"

    install_automation() {
      local source_file="$1"
      local target_folder_name="$2"
      local target_folder="$codex_automation_root/$target_folder_name"
      local target_file="$target_folder/automation.toml"

      if [[ ! -f "$source_file" ]]; then
        return 0
      fi

      mkdir -p "$target_folder"
      if [[ -f "$target_file" ]]; then
        local automation_backup_root="$BACKUP_ROOT/automations/$target_folder_name"
        mkdir -p "$automation_backup_root"
        cp "$target_file" "$automation_backup_root/automation.toml"
      fi

      print_step "Install automation config: $target_file"
      cp "$source_file" "$target_file"
    }

    install_automation "$automation_source/weekly-harness-maintenance.toml" "weekly-harness-maintenance"
    install_automation "$automation_source/monthly-harness-deep-audit.toml" "monthly-harness-deep-audit"
  fi
fi

print_step "Installation complete."
print_step "If this is a Git project, review the diff before committing."
