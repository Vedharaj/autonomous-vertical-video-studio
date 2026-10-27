# Agent, Skill, Script & Configuration Inventory

> Comprehensive inventory of all software components, skills, scripts, external services, and configuration files utilized in the *Match Fixers* production pipeline.

---

## 1. Specialist Agents

| Agent Name | Definition File | Role / Responsibility | Scope |
| :--- | :--- | :--- | :--- |
| **Workflow Orchestrator** | `agents/workflow-orchestrator.md` | Master production coordinator; enforces gates, invariants, and approvals | Project-Local |
| **Visual Director** | `agents/visual-director.md` | Gemini vision reference frames & Google Flow video take conditioning | Project-Local |
| **Audio Engineer** | `agents/audio-engineer.md` | Sarvam Indic dubbing, SciPy Foley, speech collision gating & ASS subtitles | Project-Local |
| **QA & Distribution Officer** | `agents/qa-publisher.md` | Compliance audit, keyframe proofing, Drive staging & sequential queueing | Project-Local |

---

## 2. Skills & Customizations

| Skill Name | Local Path | Global Fallback | Scope & Status |
| :--- | :--- | :--- | :--- |
| **google-flow-production** | `.agents/skills/google-flow-production/SKILL.md` | `~/.gemini/antigravity-cli/skills/google-flow-production/SKILL.md` | **Localized**; covers Flow CDP automation, Dual-Anchor conditioning, and Verified Take Retrieval Gate |
| **sarvam-indic-dubbing** | `.agents/skills/sarvam-indic-dubbing/SKILL.md` | `~/.gemini/antigravity-cli/skills/sarvam-indic-dubbing/SKILL.md` | **Localized**; covers Sarvam TTS/STT, Foley engineering, speech collision gating, and subtitle standards |
| **short-form-series-production** | `.agents/skills/short-form-series-production/SKILL.md` | `~/.gemini/antigravity-cli/skills/short-form-series-production/SKILL.md` | **Localized**; master lifecycle guide for 9:16 vertical series, approval gates, and sequential queueing |
| **playwriter** | `~/.agents/skills/playwriter/SKILL.md` | `~/.agents/skills/playwriter/SKILL.md` | **Legitimate Global Tool**; bridges user Chrome browser session to automate Gemini Vision & Flow CDP |

---

## 3. Automation Scripts & Tools

| Script / Tool | Path | Language / Runtime | Purpose & Responsibility |
| :--- | :--- | :--- | :--- |
| **Dubbing & Mastering Pipeline** | `scripts/dub_match_fixer_ep*.py` | Python 3 (NumPy, SciPy, Requests) | Generates episode-specific audio bed, Foley, Sarvam TTS, ASS subs, and muxes video masters |
| **Core Dubbing Engine** | `scripts/core/sarvam_dub_engine.py` | Python 3 | Parameterized, reusable dubbing and Foley engine driven by environment variables |
| **Core SMM Publisher** | `scripts/core/smm_publisher.py` | Python 3 | Parameterized Drive uploader and sequential SMM queue manager |
| **Flow Service Daemon** | `scripts/core/flow_service.sh` | Bash | Manages Chrome remote debugging (port 9333) and Flow MCP daemon (port 8787) |
| **SMM CLI** | `/home/vedha/.local/bin/smm` | Go / Python executable | Interacts with YouTube Data API v3 and Google Sheets queue |
| **FFmpeg / FFprobe** | `/usr/bin/ffmpeg` | C / Binary (libass, libx264) | Concat demuxing, audio extraction, filtering, and hardsub burn-in |

---

## 4. Configuration & Secrets

| Configuration File | Path | Description | Handling Rule |
| :--- | :--- | :--- | :--- |
| **Environment Config** | `config/.env` | Holds `SARVAM_API_KEY`, Drive folder ID, channel names, ports | **Excluded from Git** via `.gitignore` |
| **Environment Template** | `config/.env.example` | Sample environment variables with descriptive placeholders | Committed to Git |
| **YAML Config Schema** | `config/config.example.yaml` | Series metadata, character archetypes, audio sample rates, video dimensions | Committed to Git |
| **JSON Config Schema** | `config/config.example.json` | JSON format configuration for tools expecting JSON | Committed to Git |

---

## 5. External Services & Cloud APIs

| Service | Endpoint / Interface | Authentication | Purpose | Verified Status |
| :--- | :--- | :--- | :--- | :--- |
| **Google Gemini** | `https://gemini.google.com` via Playwriter CDP | User Browser Cookie / Session | Pre-production visual reference frame generation (9:16) | **Verified (Ep 1–4)** |
| **Google Flow** | `https://flow.google.com` via Playwriter / Flow MCP | Google Workspace Session Cookie | Omni 1.1 Flash 720p 9:16 video generation | **Verified (Ep 1–4)** |
| **Sarvam AI TTS** | `https://api.sarvam.ai/text-to-speech` | `api-subscription-key` header | Multi-character 48kHz voice synthesis (`bulbul:v3`) | **Verified (Ep 1–4)** |
| **Sarvam AI STT** | `https://api.sarvam.ai/speech-to-text` | `api-subscription-key` header | Dialogue clarity verification (`saaras:v3`) | **Verified (<30s slice)** |
| **Google Drive** | Folder: `1IxzXjqaFbCx6Audvw1pSmILrGzN8aqVp` | Workspace OAuth Token via Apps Script | Intermediate cloud staging for video masters | **Verified (Ep 1–4)** |
| **YouTube Data API** | Managed via Google Sheets & SMM CLI | Service Account / OAuth | Scheduled publishing at 11:00 & 18:00 IST | **Verified (Ep 1–4)** |

---

## 6. Project Invariant Rules Files

| File | Path | Scope |
| :--- | :--- | :--- |
| **Workspace Instructions** | `AGENTS.md` | Primary Antigravity CLI entry point; defines local-by-default rules and checklists |
| **Production Bible** | `GEMINI.md` | Detailed rules for consistency, character props, subtitles, and queueing |
| **Series Screenplays** | `match_fixers_episodes_detailed.md` | Full 20-episode screenplays and shot breakdowns |
| **Series Bible** | `match_fixers_series_package.md` | Narrative universe, character turnarounds, and visual style |
