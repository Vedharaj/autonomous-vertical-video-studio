# Vertical Series Production Template

> A production-grade, self-contained template for creating new 9:16 vertical short fiction series (45.0s–60.0s per episode) with Google Flow, Gemini Vision, Sarvam AI Indic dubbing, procedural SciPy Foley, and sequential SMM queueing.

---

## Quick Start for New Series

### 1. Initialize Series from Template
Run the bootstrap script:
```bash
bash /media/vedha/E2/freelance/templates/bootstrap_new_series.sh \
  --name "my-series" \
  --target "/media/vedha/E2/freelance/yt-series/my-series"
```

### 2. Configure Environment
```bash
cd /media/vedha/E2/freelance/yt-series/my-series
cp config/.env.example config/.env
# Set SARVAM_API_KEY and other parameters in config/.env
```

### 3. Verify System Health
```bash
python3 tests/test_environment.py
```

---

## Directory Architecture

```text
<series-name>/
├── README.md                          # Series overview and instructions
├── AGENTS.md                          # Primary project instructions loaded by AGI CLI
├── GEMINI.md                          # Series consistency & continuity rules
├── docs/                              # Architecture, workflow, and troubleshooting
├── agents/                            # Specialized agent role definitions
├── .agents/                           # AGI CLI project-local discovery root
│   ├── rules/                         # Workspace rules
│   └── skills/                        # Project-local production skills
├── config/                            # Environment and settings templates
├── prompts/                           # Vision, video, and dubbing prompt bibles
├── scripts/core/                      # Reusable dubbing, publishing, and service tools
├── tests/                             # Validation test suite
└── assets/references/                 # Character turnarounds and background stills
```
