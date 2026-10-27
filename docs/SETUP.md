# Zero-to-One Setup & Environment Configuration

> Step-by-step setup guide for replicating the *Match Fixers* autonomous video generation studio on any Linux, macOS, or Windows WSL2 machine.

---

## 1. System Packages & Prerequisites

### Linux (Ubuntu / Debian)
```bash
sudo apt update && sudo apt install -y \
  ffmpeg \
  libass-dev \
  python3 \
  python3-pip \
  python3-venv \
  nodejs \
  npm \
  curl \
  jq \
  google-chrome-stable
```

### macOS (Homebrew)
```bash
brew install ffmpeg libass python@3.11 node curl jq
# Install Google Chrome from https://www.google.com/chrome/
```

Verify FFmpeg was compiled with `libass` and `libx264`:
```bash
ffmpeg -version | grep -E "enable-libass|enable-libx264"
```

---

## 2. Python Environment Setup

Create a dedicated virtual environment inside or alongside the project:
```bash
cd /media/vedha/E2/freelance/yt-series/match_fixer
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install requests numpy scipy pyyaml
```

---

## 3. Environment Variables & API Credentials

1. Copy the environment template:
   ```bash
   cp config/.env.example config/.env
   ```

2. Open `config/.env` and supply your credentials:
   ```bash
   # Sarvam AI API Key (from https://dashboard.sarvam.ai)
   export SARVAM_API_KEY="your_sarvam_api_key_here"

   # Google Drive Publishing Staging Folder ID
   export GOOGLE_DRIVE_FOLDER_ID="1IxzXjqaFbCx6Audvw1pSmILrGzN8aqVp"

   # SMM Channel Names
   export SMM_TAMIL_CHANNEL="Story Time Tamil"
   export SMM_HINDI_CHANNEL="Story Time Hindi"

   # Browser Automation Ports
   export CHROME_REMOTE_DEBUG_PORT="9333"
   export FLOW_MCP_PORT="8787"
   ```

3. Export the variables in your active shell or load them into your profile:
   ```bash
   source config/.env
   ```

---

## 4. Google Flow Automation Setup

Google Flow runs in Chrome and can be automated via Chrome DevTools Protocol (CDP) or the Playwriter MCP extension:

1. Launch Chrome with remote debugging on port 9333:
   ```bash
   bash scripts/core/flow_service.sh start
   ```

2. In the opened Chrome browser window, sign in to your Google Account and navigate to:
   `https://flow.google.com`

3. Confirm the service status:
   ```bash
   bash scripts/core/flow_service.sh status
   ```

---

## 5. Antigravity CLI Customization Registration

Antigravity CLI discovers project-local customizations automatically from the `.agents/` folder at the repository root:
* Rules: `AGENTS.md` and `GEMINI.md` are loaded automatically from the project root.
* Skills: `.agents/skills/` contains the localized production skills:
  * `.agents/skills/google-flow-production/`
  * `.agents/skills/sarvam-indic-dubbing/`
  * `.agents/skills/short-form-series-production/`

To verify that the CLI recognizes the local skills:
```bash
python3 tests/test_environment.py
```

---

## 6. SMM Social Media Automation Engine

The Social Media Manager (`smm`) CLI connects YouTube brand channels with the Google Sheets scheduling queue:
1. Verify SMM CLI installation:
   ```bash
   smm --version
   ```
2. Verify connected channels:
   ```bash
   smm channels list
   ```
   Expected output:
   * `Story Time Tamil`
   * `Story Time Hindi`
3. Inspect current queue state:
   ```bash
   smm queue list "Story Time Tamil"
   smm queue list "Story Time Hindi"
   ```

---

## 7. Automated Environment Verification

Run the project verification script to ensure all dependencies, API keys, audio libraries, and paths are valid before commencing production:
```bash
python3 tests/test_environment.py
```
Expected output:
`[ALL CHECKS PASSED] System is ready for video generation and dubbing.`
