---
name: google-flow-production
description: Production guide and runbook for automating Google Flow (flow.google.com) via flow-mcp, Playwright CDP, and local FFmpeg. Covers project navigation, character asset locking, credit-safe staging, Agent mode toggles, queue pacing, video assembly, voice overlap prevention, and lip-sync safety.
---

# Google Flow Production & Consistency Guide

## Purpose & Scope
This skill guides the end-to-end production of vertical short-form serial episodes (9:16 aspect ratio, ~20–30s) using Google Flow (`flow.google.com`) through the local `flow-mcp` service on port 8787 and Chrome DevTools Protocol (CDP) on port 9333.

---

## 1. Prerequisites & Service Setup
* **Chrome CDP:** Must run with user profile `/home/vedha/.flow-mcp/chrome-profile` on port `9333`.
* **flow-mcp Daemon:** Runs on port `8787` (`node /media/vedha/E2/mcp/flow-mcp/dist/index.js`).
* **Service Management:** Use `/media/vedha/E2/freelance/tools/flow_service.sh {start|status|stop}`.

---

## 2. Critical UI & Selector Invariants (Flow Angular App)

### Project Navigation
* Flow's Angular SPA can lose project state if opened only to `/`.
* Always navigate directly to the project URL: `https://flow.google.com/project/<project-id>`.

### Agent Mode Toggle vs. Standard Composer
* Flow defaults to **Agent Mode** on startup (`button.agent-mode-chip[aria-pressed="true"]`).
* When Agent Mode is active, the standard generation options (`.settings-trigger-button`, model picker, aspect ratio, duration) are hidden (`display: none`).
* **Rule:** Before configuring settings or generating shots, check `button.agent-mode-chip`. If `aria-pressed="true"`, click it to toggle off Agent Mode. This surfaces the standard composer and settings drawer.

### Collection Creation & Asset Population Invariant
* **Non-Empty Collection Rule:** Whenever a collection is created in Google Flow (e.g. `Environments`, `Props`, `Costumes`), immediately move or upload all corresponding media/image assets into it. Never leave a created collection empty.
* **Standard Workflow:**
  1. Create and name the collection via the Library drawer or Add media menu (`role=button[name="Create collection"i]`).
  2. Populate the collection immediately with its designated images or video references (via direct upload inside the collection or moving existing assets).
  3. Confirm that the collection tile displays thumbnail previews and item count ($N \ge 1$) before proceeding to shot generation.

---

## 3. Character Consistency Locking
1. **Asset Registration:**
   * Register key characters in Flow using `flow_character`:
     `flow_character({ name: "Arul", prompt: "...", image: "/path/to/reference.png" })`
   * Confirm registration with `flow_characters()`. Registered assets are bound as `asset:<Name>` (e.g. `asset:Arul`, `asset:Meera`).
2. **Shot Prompting Invariant:**
   * Always reference `asset:<Name>` in the `reference_images` parameter or text prompt.
   * Never describe faces purely in natural language without linking the registered asset token.
   * Lock costume, hair, and lighting palette across all shots within an episode.

---

## 4. Google Flow Credit Safety & Presets
* **Pre-flight Stills (0 Credits):** Before generating video takes, generate a single still frame (`type: "image"`, model: Nano Banana 2, 0 credits) to verify composition, framing, and character likeness.
* **Credit Calculation & Quote:**
  * Video generation preset: `Omni 1.1 Flash`, `720p`, `9:16` vertical.
  * 4s shot = ~7 credits
  * 6s shot = ~10 credits
  * 8s shot = ~12 credits
  * Calculate and report exact credit totals before executing generation.
* **Queue Pacing:** Wait for each shot take to finish (`flow_wait({ take: take_id })`) before submitting the subsequent scene take.

---

## 5. Preventing Voice Overlap, Missing Audio & Speech Collision

### A. Speech Collision Prevention & Hybrid Audio Protocol
* **The Problem:** When Omni 1.1 Flash generates a video from prompts containing action cues or implied commentary (e.g. sports scenes, crowd dialogue), it synthesizes internal AI English speech. Blindly merging original audio causes dual-voice collision with Sarvam AI dubbed dialogue. Blindly stripping all audio removes valuable realistic Foley and atmosphere.
* **Rule 1 (Prompt Sanitization):** NEVER include spoken dialogue in visual prompts. Instead, describe visual behavior only:
  * ❌ *Bad:* *"Arul muttering 'who is this... wrong number?'"*
  * ✅ *Good:* *"Close-up on Arul's face, furrowed brow, lips slightly parted in bewilderment, looking down at glowing phone screen."*
* **Rule 2 (Speech Collision Gate & Mute):** In any shot where character dialogue plays (or where Omni generated unwanted English commentary), completely purge/mute the raw audio track for that shot segment. Never let raw AI speech play simultaneously with dubbed dialogue.
* **Rule 3 (Authentic Foley & Environmental Preservation):** For dialogue-free action or B-roll shots (e.g. cricket ball striking stumps, foot steps, ambient crowd roar, traffic), preserve the authentic 48kHz environmental audio from the video takes rather than substituting with synthetic sine waves.
* **Rule 4 (Dynamic Ducking):** Apply smooth -3.5dB to -4dB ducking under character speech so dubbed dialogue remains punchy, clear, and distinct while ambient environment sounds stay alive.

### B. Preventing Lip-Sync Desynchronization
AI video models cannot guarantee phoneme-accurate lip movements for full sentences. Use the **3 Director Framing Rules**:
1. **Rule A (Off-Screen / Diegetic Voice):**
   * Long dialogue (e.g. voice notes, phone calls, narration) must play while the character is listening, looking away, or off-camera. (Lip-sync failure risk: **ZERO**).
2. **Rule B (Cutaways & Non-Face Angles):**
   * Frame speakers over-the-shoulder, from 3/4 profile, or cut to B-roll (hands typing, steering wheel, walking feet, glowing screens). (Lip-sync failure risk: **ZERO**).
3. **Rule C (Ultra-Short On-Camera Utterances):**
   * When the camera directly captures a talking face, keep in-camera dialogue to ultra-short 1–3 word reactions (e.g. *"Yaaru da idhu?"*, *"What?"*, *"Wait"*). Limit visible mouth movement to $< 2.0\text{s}$.

### C. Preventing Missing Audio & Cutoff Lines
* **Pre-Roll & Post-Roll Cushion:** Spoken line duration must be $\le \text{Shot Duration} - 0.8\text{s}$. Leave $\ge 0.4\text{s}$ cushion at the start and end of every shot cut.
* **Tail Guard:** Ensure the last audio element ends at least $0.2\text{s}$ before total video duration to avoid container cutoff.

---

## 6. Dual-Anchor Conditioning & Signed CDN Video Extraction

### Dual-Anchor Conditioning Protocol
To maintain consistent likeness, costume, and color grading across shots:
1. **Gemini Per-Shot Reference Pre-Generation:**
   - For every shot cut in an episode, generate a dedicated 9:16 vertical reference image in **Gemini (`gemini.google.com`)** via Playwriter before generating the video take.
   - Condition Gemini on the locked character sheet/portrait and the environment sheet to maintain 100% aesthetic continuity.
   - Save the rendered frame locally as `ep<Episode>_shot<Shot>_ref.png`.
2. **Upload & Mention in Flow:**
   - Upload the generated shot reference image into Google Flow.
   - In Flow's prompt composer, attach/mention BOTH:
     - The registered character asset chips/tokens (`@Character`)
     - The specific shot reference image (`ep<Episode>_shot<Shot>_ref.png`)
3. **Native Keyboard Input:** Type prompt text into `.ProseMirror` using native keyboard events (`delay: 5`ms) and click `button[aria-label="Start generation"]`.

### Signed CDN Video Retrieval & Verified Take Download Gate
Once generation reaches 100%:
* **Direct Retrieval:** Google Flow renders a signed CDN URL: `https://flow-content.google/video/<id>?Expires=...&KeyName=...&Signature=...`.
* Extract matching URLs from `document.documentElement.innerHTML` using regex `/https:\/\/flow-content\.google\/video\/[^"'\s<>]+/g`.
* Download the clean MP4 directly using `curl -s -L "<url>" -o scene-NN.mp4`.
* **Take Verification Gate (UI Download):**
  - When opening a generated take in the Flow editor (`/edit/<id>`), ALWAYS verify that the take title displayed in the header (`h1` or `.header-title`) exactly matches the target shot before downloading.
  - Never blindly click the first tile or download menu item without cross-referencing the take name.
  - Cross-verify the downloaded file name and duration using `ffprobe` before moving to episode asset directories.

---

## 7. Bottom-Center English Subtitle Standard (ASS Format)
* **Language Standard:** Burn-in subtitles must strictly be in **English**.
* **Canvas Calibration:** Set `PlayResX: 720`, `PlayResY: 1280`.
* **Style:** `Fontname: Arial`, `Fontsize: 34`, `Bold: 1`, `Alignment: 2` (Bottom-Center), `MarginV: 110`.
* **Safe Zone:** Text is strictly contained in rows 1109–1162 (118px above the bottom margin), preventing any overlap with actors' faces, necks, or upper bodies.

