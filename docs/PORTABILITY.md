# Portability & Migration Guide

> Runbook for moving the *Match Fixers* workflow to a new series, a new machine, or a fresh cloud environment without hardcoded path breakage or global pollution.

---

## 1. Portability Principles

1. **Relative Paths by Default:** Scripts must calculate their root directory relative to `__file__` (e.g. `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`) rather than hardcoding `/media/vedha/E2/...`.
2. **Environment Variable Decoupling:** All secrets (`SARVAM_API_KEY`), cloud IDs (`GOOGLE_DRIVE_FOLDER_ID`), and network ports (`CHROME_REMOTE_DEBUG_PORT`) must be loaded from `os.environ` with documented fallback defaults.
3. **Self-Contained Discovery:** Keep all project instructions, rules, and skills inside the project repository under `.agents/` and `AGENTS.md`. A newly cloned repository will be recognized by AGI CLI immediately upon `cd <project>`.

---

## 2. Decoupled Path & Secret Architecture

Before portability refactoring:
```python
# ANTI-PATTERN: Hardcoded absolute paths and leaked secrets
SARVAM_API_KEY = "sk_sample_secret_key_here"
sys.path.insert(0, '/media/vedha/E2/code/youtube-automation-apps-script')
folder_id = '1IxzXjqaFbCx6Audvw1pSmILrGzN8aqVp'
```

After portability refactoring:
```python
# PORTABLE PATTERN: Environment-driven with relative resolution
SARVAM_API_KEY = os.environ.get("SARVAM_API_KEY")
if not SARVAM_API_KEY:
    raise ValueError("Missing SARVAM_API_KEY. Set it in config/.env")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVE_FOLDER_ID = os.environ.get("GOOGLE_DRIVE_FOLDER_ID", "1IxzXjqaFbCx6Audvw1pSmILrGzN8aqVp")
```

---

## 3. Migration Checklist to a New Machine

| Step | Action | Command / Verification |
| :--- | :--- | :--- |
| **1. Clone Repo** | Clone or copy the series directory to the new machine | `git clone <repo_url> /path/to/series` |
| **2. Install Toolchain** | Install FFmpeg (with `libass`), Python 3.10+, Node 18+, Chrome | See [docs/SETUP.md](SETUP.md) |
| **3. Virtualenv** | Create virtual environment and install Python packages | `python3 -m venv .venv && pip install -r requirements.txt` |
| **4. Config & Keys** | Copy and populate `config/.env` | `cp config/.env.example config/.env` |
| **5. Browser CDP** | Start Chrome with remote debugging on port 9333 | `bash scripts/core/flow_service.sh start` |
| **6. Verify Setup** | Execute automated system and environment validation test | `python3 tests/test_environment.py` |
| **7. Verify Subtitle Bounds** | Run ASS subtitle bounds audit on sample file | `python3 tests/test_subtitle_bounds.py` |

---

## 4. Migration Checklist to a New Series Project

To spin up a new series (e.g. *Series B*) using this workflow:
1. Copy the project template from `templates/video-series-template/` or run the bootstrap script:
   ```bash
   bash templates/bootstrap_new_series.sh --name "my-new-series" --target "/path/to/my-new-series"
   ```
2. Populate the narrative package in `my-new-series/series_package.md` and detailed screenplays in `my-new-series/episodes_detailed.md`.
3. Add character turnaround reference sheets to `my-new-series/assets/references/`.
4. Register characters in Google Flow under the new project ID.
5. Update `config/.env` with the new project settings.
6. The CLI will automatically load `.agents/` inside the new directory with 0 global configuration changes.
