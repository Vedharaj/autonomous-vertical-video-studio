---
name: short-form-series-production
description: Master lifecycle guide for developing, scripting, directing, producing, dubbing, and distributing vertical serial comedy-drama short-form series (9:16 vertical shorts, 45–60s per episode, 20-episode seasons). Use when starting, planning, or executing any multi-episode YouTube Shorts or Reel series.
---

# Short-Form Series Master Production Lifecycle

## Overview
This skill governs the complete 9-phase pipeline for creating high-retention, serialized vertical fiction (comedy, drama, thriller, romance) optimized for YouTube Shorts and Instagram Reels (45–60s / episode), from intake to channel queueing.

---

## The 9 Production Phases

### Phase 1: Intake & High Concept
* Define core dramatic question / moral premise (e.g. *"Wrong number connects two strangers during pivotal life moments"*).
* Target format: 9:16 vertical, 45–60 seconds / episode, 20-episode arc.
* Primary audience & tone (e.g. soap-opera warm orange and dusk indigo palette, intimate, curious).

### Phase 2: Character Bible & Asset Design
* Main Protagonists (max 3–5 recurring characters):
  * Name, age, appearance, costume signature, emotional wound, secret.
* Generate and lock master reference images (front portrait, neutral lighting, consistent costume).
* Register character assets in Google Flow (`asset:<Name>`).

### Phase 3: Season Arc & Continuity Ledger
* 4-Act Structural Breakdown for 20 Episodes:
  * **Act 1: The Mistake (Episodes 1–3)** — Premise introduced, identity confusion, initial connection.
  * **Act 2: The Parallel Lives (Episodes 4–9)** — Deepening bond, dual struggles, cross-cutting emotional resonance.
  * **Act 3: The Threat of Exposure (Episodes 10–15)** — Stakes rise, near-misses, guilt of deception.
  * **Act 4: The Truth & Climax (Episodes 16–20)** — Revelation, confrontation, resolution.
* Maintain a strict Continuity Invariants Ledger (e.g. *"Character A remains voice-only until Episode 16 reveal"*).

### Phase 4: Standalone Episode Screenplays & Lip-Sync Framing Architecture
* **Duration & Word Count Standard:** Every episode MUST run between 45 and 60 seconds (100–140 spoken words).
* **Exact Script Shot Breakdown Invariant:** Always strictly adhere to the exact number of shots, scene environments, and timestamped dialogue beats specified in `episodes/script-for-each-episodes.md`. Do not condense or drop beats.
* **Lip-Sync Framing Architecture (Zero Desync Rules):**
  * **Rule A (Off-Screen Dialogue / Voice Notes):** Long emotional dialogue is delivered via voice notes, phone calls, or off-camera while the on-screen character listens. (Lip-sync failure risk: ZERO).
  * **Rule B (Cutaways & Non-Face Angles):** Frame talking characters over-the-shoulder, from 3/4 profile, or cut to B-roll (hands typing, steering wheel, walking feet). (Lip-sync failure risk: ZERO).
  * **Rule C (Short Utterances for Direct Face Shots):** Direct front-facing talking shots are restricted to ultra-short 1–3 word reactions (e.g. *"What?"*, *"Wrong number-a?"*), lasting $< 2.0\text{s}$.
* **5–8 Shot Structure for 45–60s Episodes:**
  * Shot 1 (0–6s): Hook / environmental establishment / incoming trigger (e.g. phone vibration).
  * Shot 2 (6–16s): Core emotional dialogue / voice note playback while character listens.
  * Shot 3 (16–26s): Internal reaction / re-listening / perplexed confrontation.
  * Shot 4 (26–36s): Active response / investigate / typing / dialogue exchange.
  * Shot 5 (36–48s): Critical choice point / hesitation / new incoming complication.
  * Shot 6 (48–55s+): Final resolution beat / suspended choice / fade to black.

### Phase 5: Master Reference Image & Video Prompts
* Write deterministic camera and lighting prompts for each shot.
* **Reference Generation Priority:** Always generate 9:16 vertical shot reference images preferentially in **Gemini (`gemini.google.com`)** via Playwriter. Failover to **ChatGPT** only if Gemini is rate-limited or unavailable.
* **Single-Perspective Composition Guard:** Every reference image prompt must mandate a single unified camera angle. Explicitly include negative constraints to prevent AI hallucinated multi-panels: *"Single unified composition, absolutely NO split screen, NO multi-panel collage, NO duplicated characters, NO motion trail lines, NO text."*
* Standard preset: Omni 1.1 Flash 720p 9:16 vertical, referencing registered character assets (`asset:<Name>`) and the per-shot reference image chips.
* **Prompt Sanitization:** DO NOT include spoken dialogue in visual prompts (describe behavioral cues and expressions only to prevent AI hallucinated speech).
* Verify composition with 0-credit stills before video rendering.

### Phase 6: Video Generation & Stitching
* Generate scene takes sequentially using Google Flow (`flow_generate`, `flow_wait`).
* Download takes (`flow_download`) into `episodes/episode-NN/scene-NN.mp4`.
* Concatenate into raw visual master (`episode-NN.mp4`).

### Phase 7: Multilingual Dialogue & Sarvam AI Dubbing
* Script natural colloquial translations for target Indian languages (Tamil, Hindi, Telugu, etc.).
* **Universal Dialogue Coverage Invariant:** Every visual shot featuring interacting characters, comedy beats, celebrations, or reactions must have dubbed dialogue across all target languages. Never leave character action beats silent or relying on background music alone.
* Match character voice archetypes using Sarvam Bulbul voices.
* Tune pace (`1.10–1.20`) and expressiveness (`temperature: 0.65–0.70`).
* Apply telephone bandpass EQ for voice notes/calls; wide-range room EQ for live on-camera dialogue.
* Enforce automated timeline validation: pre-roll padding, cut-point containment, and overlap prevention.

### Phase 8: Hybrid Audio Design, Foley, Subtitling, and Lossless Muxing
* **Hybrid Environmental Bed:** Preserve authentic 48kHz ambient environment audio (crowds, field action, room tone) from AI video takes. Never replace with flat synthetic sine waves.
* **Speech Collision Gate:** In any shot where character dialogue plays (or where AI synthesized English voices), purge/mute raw video audio completely to eliminate dual-voice overlap.
* **Dynamic Ducking:** Apply smooth -3.5dB to -4dB ducking under character speech so dubbed dialogue is punchy, clear, and distinct.
* Synthesize Foley bed: haptic phone vibrations, touch clicks, WhatsApp chimes, bat strikes, tension swells.
* Normalize master soundtrack to -0.5dB peak.
* **Bottom-Center English Subtitle Standard:**
  * Subtitles burned onto vertical video masters MUST strictly be in **English**.
  * Use ASS format (`PlayResX: 720`, `PlayResY: 1280`, `Fontsize: 34`, `Alignment: 2` (Bottom-Center), `MarginV: 110`).
  * Text strictly contained in rows 1107–1169 (~111px margin above bottom edge), never obscuring faces or chest areas.
* Output named delivery masters: `episode-NN-tamil.mp4`, `episode-NN-hindi.mp4`, `episode-NN-tamil-captioned.mp4`, `episode-NN-hindi-captioned.mp4`.

### Phase 9: Quality Verification & Mandatory Human Approval Gate
* **STRICT INVARIANT (No Auto-Uploads):** NEVER upload completed episode videos to Google Drive, NEVER run `smm queue add`, and NEVER modify Google Sheets scheduling rows without explicit user approval.
* **Step 9A — Local Quality Verification:** Verify total runtime (45s–60s), audio channel count, absence of speech collision, and subtitle vertical bounding box audit locally.
* **Step 9B — Human Review & Approval:** Present keyframe verification stills and metrics to the user. Halt execution and wait for explicit confirmation (e.g., *"approved"*, *"proceed to queue"*).
* **Step 9C — Post-Approval Distribution via SMM:** ONLY after user sign-off, upload to Google Drive (`YouTube_Queue`, `1IxzXjqaFbCx6Audvw1pSmILrGzN8aqVp`) and enroll in `Story Time Tamil` and `Story Time Hindi` with status `READY`:
  * **Sequential Publishing Order Invariant:** Episodes MUST be enrolled in strict numerical sequence (Episode 1 -> Episode 2 -> Episode 3 -> Episode 4 -> ...). Never queue an episode out of sequence because YouTube publishing picks rows top-to-bottom. Always verify preceding episodes are enrolled in the queue before adding the next episode row.
  * **Automated Publishing Schedule:** Content is published at **11:00 IST** and **18:00 IST** via ecosystem cron triggers.
  * **Tamil Master:** Target channel `Story Time Tamil`
    ```bash
    python3 /media/vedha/E2/freelance/tools/smm_queue_episode.py \
      --video "episodes/episode-NN/episode-NN-tamil-captioned.mp4" \
      --mode queue \
      --channel "Story Time Tamil" \
      --lang "ta-IN" \
      --episode NN
    ```
  * **Hindi Master:** Target channel `Story Time Hindi`
    ```bash
    python3 /media/vedha/E2/freelance/tools/smm_queue_episode.py \
      --video "episodes/episode-NN/episode-NN-hindi-captioned.mp4" \
      --mode queue \
      --channel "Story Time Hindi" \
      --lang "hi-IN" \
      --episode NN
    ```
* Verify queue status:
  ```bash
  smm queue list "Story Time Tamil"
  smm queue list "Story Time Hindi"
  ```

