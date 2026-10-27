# Match Fixers — Autonomous Studio Project Instructions

> Primary project instructions and discovery file loaded automatically by Antigravity CLI when operating within `match_fixer/`.

---

## 1. Architectural Mandates: The 10 Commandments of Portability

To prevent global drift, configuration leakage, and project cross-contamination, all agents operating in this workspace **MUST** follow these 10 architecture rules without exception:

1. **Inspect before creating:** Check existing files, agent discovery rules, skill locations, and configuration before implementing anything.
2. **Local by default:** New project-specific agents, skills, prompts, and configurations must be created inside the project repository.
3. **Global only by exception:** Use global resources only when they are intentionally shared or technically required (e.g. system diagnostics, Playwriter browser daemon).
4. **No silent migration:** Record every proposed move, replacement, or dependency change before applying it.
5. **No destructive cleanup:** Never delete existing resources until the replacement has been tested and verified.
6. **No invented APIs:** Verify AGI CLI commands, supported configuration keys, and discovery mechanisms against the installed version and available documentation.
7. **Reproducible setup:** Another machine should be able to reconstruct the workflow using documented steps and authorized credentials.
8. **Dependency transparency:** Document every unavoidable external or global dependency in `docs/AGENT_INVENTORY.md`.
9. **Test before declaring success:** Run appropriate checks (`tests/test_environment.py`, `tests/test_subtitle_bounds.py`, `tests/test_audio_alignment.py`) before declaring any task complete.
10. **Update documentation:** Any change to agents, skills, commands, or architecture must include corresponding documentation updates in `docs/`.

---

## 2. Pre-Implementation Checklist

Before starting any production task (e.g. generating a new episode, modifying dubbing scripts, or touching queue configurations), execute this checklist:

- [ ] **Check Workspace Roots:** Am I working in `/media/vedha/E2/freelance/yt-series/match_fixer`?
- [ ] **Verify Discovery Rules:** Are my target skills located in `.agents/skills/`?
- [ ] **Single-Perspective Guard:** Does the Gemini reference prompt include mandatory negative constraints (`"Single unified composition, absolutely NO split screen..."`)?
- [ ] **Verified Take Gate:** Will the video download verify the take title in the Flow UI header before saving the file?
- [ ] **Universal Dialogue Coverage:** Does every scene with character action, comedy, or celebrations have dialogue in Tamil & Hindi?
- [ ] **ASS Subtitle Bounds:** Are English subtitles strictly configured with `Alignment: 2`, `MarginV: 110`, bounded between vertical rows 1107 and 1169?
- [ ] **Sequential Publishing Check:** Are all predecessor episodes ($1 \dots N-1$) present in the SMM queue before scheduling Episode $N$?
- [ ] **Human Approval Gate:** Will the pipeline halt and present keyframe stills and audio checks for human sign-off before cloud upload?

---

## 3. Specialized Agent Roles

This workspace is divided into four specialist agent roles defined in `agents/`:

| Agent File | Role | Primary Responsibility |
| :--- | :--- | :--- |
| [`agents/workflow-orchestrator.md`](agents/workflow-orchestrator.md) | Production Showrunner | Coordinates Stages 0–8, tracks continuity, enforces approval gates |
| [`agents/visual-director.md`](agents/visual-director.md) | Visual Director | Authors single-perspective Gemini prompts, conditions Dual-Anchor Flow takes |
| [`agents/audio-engineer.md`](agents/audio-engineer.md) | Audio Engineer | Synthesizes Sarvam Indic dubs, generates SciPy Foley, gates speech collision |
| [`agents/qa-publisher.md`](agents/qa-publisher.md) | QA & Distribution Officer | Audits runtime & ASS bounds, verifies STT, manages sequential SMM queue |

---

## 4. Key References & Documentation

* **Workflow Specification:** [`docs/WORKFLOW.md`](docs/WORKFLOW.md)
* **Agent Architecture:** [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
* **Component Inventory:** [`docs/AGENT_INVENTORY.md`](docs/AGENT_INVENTORY.md)
* **Setup & Environment:** [`docs/SETUP.md`](docs/SETUP.md)
* **Troubleshooting Bible:** [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)
* **Portability Guide:** [`docs/PORTABILITY.md`](docs/PORTABILITY.md)
* **Architecture Decisions:** [`docs/DECISIONS.md`](docs/DECISIONS.md)
* **Production Rules Bible:** [`GEMINI.md`](GEMINI.md)
