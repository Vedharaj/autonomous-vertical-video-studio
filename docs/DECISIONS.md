# Architecture Decision Records (ADRs)

> Record of key architectural decisions, rationale, trade-offs, and invariants adopted across the vertical short-form production platform.

---

## ADR 1: Project-Local vs Global Customization Architecture

### Context
Customization skills (`google-flow-production`, `sarvam-indic-dubbing`, `short-form-series-production`) were initially placed in `~/.gemini/antigravity-cli/skills/`. This caused project-specific constraints, character names, and paths to leak into unrelated workspaces on the developer's machine and prevented version-controlling project workflows with the series code.

### Decision
Migrate to **Project-Local Customizations** by default:
- All project rules reside in `AGENTS.md` and `GEMINI.md` at the project root.
- All project skills reside in `<project>/.agents/skills/`.
- Global locations (`~/.gemini/...`) are reserved strictly for machine-wide, project-agnostic utilities (e.g. Playwriter browser daemon, system disk triage).

### Consequences
* **Positive:** Complete workspace self-containment. Each project can evolve its rules and skills independently without breaking other series. Cloned projects work out-of-the-box.
* **Negative:** Requires creating `.agents/` in each series workspace, which is solved by providing an automated bootstrap initialization template.

---

## ADR 2: Dual-Anchor Conditioning for Video Generative Stability

### Context
Generative video diffusion models (Omni 1.1 Flash) suffer from character likeness drift across shots when prompted purely from text. Prompts describing "Chintu with short hair" generate different faces, proportions, and outfits across shots.

### Decision
Enforce **Dual-Anchor Conditioning** in Google Flow:
1. Attach registered character asset chips (`@Veera`, `@Chintu`, etc.) trained/referenced on 360° turnaround profile images.
2. Attach a standalone 9:16 vertical reference image (`epXX_shotYY_ref.png`) pre-generated in Gemini Vision with a strict single-perspective prompt.

### Consequences
* **Positive:** Preserves consistent chibi 1:2 head-to-body proportions, costumes, props (Veera's bent bat, Kavya's score notebook), and environmental lighting across all shots.
* **Negative:** Requires an extra pre-production reference generation stage in Gemini Vision before rendering video in Flow.

---

## ADR 3: Acoustic-Visual Decoupling & Speech Collision Gating

### Context
Generative video models struggle to produce synchronized lip-sync for fast, nuanced Indic dialogue (Tamil and Hindi). Additionally, raw video takes synthesized by Omni 1.1 Flash often contain AI-hallucinated English audio and background mumbles that clash with dubbed dialogue.

### Decision
Adopt a **Hybrid Audio Architecture**:
1. **Speech Collision Gating:** Completely purge and mute raw video take audio in any shot where character dialogue plays.
2. **Acoustic Decoupling:** Frame long emotional dialogue off-screen, over-the-shoulder, or during reaction cutaways. Keep direct front-facing dialogue to ultra-short reactive utterances ($\le 2.0\text{s}$).
3. **Procedural SciPy Foley:** Synthesize high-impact bat cracks, ball whistles, and steps programmatically at 48kHz, ducking background beds by -3.5dB to -4dB under character speech.

### Consequences
* **Positive:** Zero lip-sync desync, zero dual-voice collision, broadcast-quality clear speech in Tamil and Hindi.
* **Negative:** Dubbing script must accurately calculate time windows and ducking envelopes.

---

## ADR 4: Bottom-Center English ASS Subtitle Standard

### Context
Short-form vertical video (9:16) has restricted visual real estate. Subtitles placed in the center or top obstruct character faces and comedy reactions. Subtitles placed too low are obscured by platform UI elements (YouTube Shorts description, sound button, progress bar).

### Decision
Standardize on bottom-center English ASS subtitles:
- Canvas: `PlayResX: 720`, `PlayResY: 1280`
- Style: `Fontname: Arial`, `Fontsize: 34`, `Bold: 1`, `Alignment: 2` (Bottom-Center), `MarginV: 110`
- Safe Zone: Mathematically bounded strictly between vertical rows 1107 and 1169 (~111px above bottom edge).

### Consequences
* **Positive:** Uniform readability across devices without covering character faces, chests, or mobile platform UI buttons.
* **Negative:** Requires strict margin calculations and automated bounding box verification.

---

## ADR 5: Mandatory Human Approval Gate Prior to Cloud Upload

### Context
Autonomous agents can rapidly generate, mux, and upload videos. However, generative AI video occasionally produces subtle visual glitches, inappropriate audio pacing, or imperfect subtitle alignments that automated tests cannot detect.

### Decision
Establish a **Mandatory Human Approval Gate**:
- The agent compiles master videos, generates verification keyframe stills for every shot, performs STT checks, and presents the results to the user.
- The agent strictly halts execution and waits for explicit user confirmation before uploading to Google Drive or modifying Google Sheets / SMM queues.

### Consequences
* **Positive:** Zero risk of publishing flawed or unverified content to public channels.
* **Negative:** Requires an interactive human turn before distribution.

---

## ADR 6: Sequential Publishing Order Invariant in Google Sheets / SMM Queue

### Context
In automated YouTube publishing, a cron job reads Google Sheets queue rows from top to bottom. If Episode 4 is enrolled before Episode 3, Episode 4 publishes first, destroying serial storytelling continuity.

### Decision
Enforce the **Sequential Publishing Order Invariant**:
- Before enrolling Episode $N$, the agent or script must inspect all active queue rows.
- The agent verifies that every preceding episode ($1 \dots N-1$) is present with status `COMPLETE` or `READY`.
- If a predecessor is missing, it must be enrolled first in strict numerical sequence.

### Consequences
* **Positive:** Guarantees 100% chronological continuity on YouTube channels.
* **Negative:** Requires an additional queue check step prior to row insertion.
