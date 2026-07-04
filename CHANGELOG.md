# Changelog

## v0.1.3 - 2026-07-04

### Overview

v0.1.3 focuses on making Chilon easier to install and safer to distribute as a real open-source package. This release completes the P0 portability cleanup, adds macOS installation support, and makes the public package structurally complete enough for new users to clone, install, and run the basic health check.

### Added

- Added `install.sh` for macOS and Unix-like environments.
- Added macOS installation instructions to `README.md`.
- Added support for `./install.sh --target /path/to/project`.
- Added support for `./install.sh --skip-automations`.
- Added a minimal public `.project-memory/` template layer.
- Added missing regression cases under `harness-regression/cases/`.
- Added drill indexes under `harness-regression/drills/`.

### Changed

- Replaced author-local absolute paths with portable relative paths in public-facing harness files.
- Removed hard-coded personal `cwds` paths from automation TOML files.
- Updated `tools/check_harness.py` to better match the public package structure.
- Included `install.sh` in package completeness and portability checks.
- Updated README package structure to include both Windows and macOS installers.

### Fixed

- Fixed the issue where installation could fail because `.project-memory/` was missing from the public repository.
- Fixed the open-source portability problem caused by Windows-specific personal paths.
- Fixed README / repository mismatch around regression cases and drills.

### Notes

Some `.project-memory/` files are intentionally minimal public templates. They are designed to be customized after installation rather than publishing private workspace state.

---

## v0.1.2 and earlier

Earlier versions were internal or early public snapshots before the P0 portability cleanup.
