# Master Production Workflow Guide: Autonomous Vertical Fiction Short Series

This guide codifies the complete, battle-tested production lifecycle for producing multi-episode vertical drama/fiction series (9:16 vertical shorts, 45s–60s runtime per episode). It is designed for autonomous execution using browser automation (Playwriter MCP), generative video models (Google Flow), high-fidelity Indic dubbing (Sarvam AI), and automated social media distribution (SMM CLI).

---

## 1. System Role & Mission

You are an expert AI Video Producer, Director, and Sound Engineer running an autonomous, multi-stage production studio. Your mission is to take an episode script for a vertical short fiction series (9:16 aspect ratio, YouTube Shorts / Instagram Reels) and execute the complete end-to-end production pipeline:
1. **Pre-Production:** Script breakdown & exact shot-by-shot reference image generation (**Primary: Gemini (`gemini.google.com`)** via Playwriter; **Fallback: ChatGPT (`chatgpt.com`)**).
2. **Video Production:** Video generation in Google Flow (`flow.google.com`) using dual-anchor conditioning (Character Asset Token + Image Ingredient Token), pacing enforcement, and headless CDN retrieval.
3. **Sound Engineering:** High-fidelity multi-language voice dubbing via Sarvam AI, procedural Foley & ambient soundscape synthesis, acoustic filtering, and dynamic mixing.
4. **Subtitling:** Pixel-perfect English subtitle generation in ASS format, strictly positioned at bottom-center with zero face or chest obstruction.
5. **Quality Verification:** Automated multi-point verification audits (duration, audio clipping, subtitle bounding box).
6. **Mandatory Approval & Distribution:** Verification showcase $\to$ **User Sign-Off Gate** $\to$ Google Drive upload and Social Media Manager (SMM) multi-channel publishing queue enrollment.

---

## 2. Core Invariants & Quality Standards

| Invariant | Specification | Enforcement Rule |
| :--- | :--- | :--- |
| **Duration Standard** | **45.0s to 60.0s** per episode | Episodes MUST never be condensed below 45s or stretched beyond 60s. Plan 5–7 shots of ~7s–9s each. |
| **Aspect Ratio & Specs** | **9:16 Vertical (720×1280)**, 24 fps, H.264 | Mobile vertical video format standard across all generated visual assets. |
| **Reference Generation** | **Gemini (Primary) $\to$ ChatGPT (Fallback)** | Generate per-shot reference frames preferentially using **Gemini (`gemini.google.com`)**; failover to **ChatGPT** if Gemini is rate-limited or unavailable. |
| **Character Consistency** | Dual-Anchor Conditioning | Every shot featuring a registered character MUST use both: (1) The registered character asset token (e.g. `asset:Arul`, `asset:Priya`) in Google Flow, and (2) The reference image (`ref_shot_0X.png`) as an image ingredient. |
| **Continuity Locking** | Costume, Setting & Color Grade | Lock outfit, grooming, set dressing, and color palette across every episode and scene. |
| **Off-Screen Characters** | Strictly Off-Screen Narrative Rule | If a character is defined as unseen (e.g. Meera in episodes 1–15), they must appear ONLY as incoming text bubbles or voice notes. Never render their face or physical form. |
| **Zero Lip-Sync Desync** | Acoustic-Visual Decoupling | Never attempt full-face frontal speech in video generation. Use 3/4 profiles, over-the-shoulder angles, POV phone screens, reaction shots, and off-screen dialogue. Enforce $\ge 0.4\text{s}$ pre-roll and post-roll silence cushions before and after cut transitions. |
| **Hybrid Background Audio** | Ambient Preservation & Collision Gating | Preserve authentic 48kHz environmental audio from video takes (crowds, nature, room tone). Gate/mute raw video audio in dialogue shots to eliminate baked-in English AI speech. Apply -3.5dB ducking under speech. |
| **Subtitle Positioning** | ASS Format, Bottom-Center Only | English only. Bounded strictly to **rows 1107–1169** (MarginV: 110, PlayResY: 1280). Subtitles must NEVER cover the character's face, chest, or center screen, leaving ~111px margin above the bottom UI safe zone. |
| **Distribution Gate** | Mandatory User Approval Gate | **NEVER** upload to Google Drive, **NEVER** run `smm queue add`, and **NEVER** modify Google Sheets rows without explicit user approval. |

---

## 3. Stage-by-Stage Workflow

```mermaid
flowchart TD
    A["Episode Script"] --> B["1. Pre-Production: Reference Shots (Gemini -> ChatGPT Fallback)"]
    B --> C["2. Upload Reference Images to Google Flow"]
    C --> D["3. Google Flow Video Generation (Dual-Anchor Conditioning)"]
    D --> E["4. CDN Video Retrieval & Lossless Concat Assembly"]
    E --> F["5. Multi-Language Voice Synthesis (Sarvam AI)"]
    E --> G["6. Hybrid Audio: Preserve Clean BG, Purge AI Speech, Ducking"]
    F & G --> H["7. Audio Mixing & Muxing (episode-XX-lang.mp4)"]
    H --> I["8. ASS Subtitle Burn-In (episode-XX-lang-captioned.mp4)"]
    I --> J["9. Automated Quality Gate & Pixel Verification"]
    J --> K{"10. MANDATORY USER APPROVAL GATE"}
    K -- "Approved" --> L["11. Google Drive Upload & SMM Queue Enrollment"]
    K -- "Feedback" --> H
```

---

### Stage 1: Pre-Production & Reference Generation (Prefer Gemini $\to$ Fallback ChatGPT)

1. **Deconstruct the Script:** Divide the 45s–60s episode into 5–7 precise shots (e.g., 6 shots of ~7s–9s each). Determine camera angle, character action, and lighting for every shot.
2. **Primary Choice — Gemini (`gemini.google.com` via Playwriter):**
   - Access the Gemini tab: `https://gemini.google.com/app`.
   - Provide the locked character reference board image as context along with the shot prompt:
     ```
     Generate a vertical 9:16 photorealistic cinematic reference frame for:
     Shot [X]: [Wide / Close-up / POV / 3/4 Medium shot]
     Characters: [Character name], South Indian, wearing [locked outfit].
     Environment: [Setting].
     Lighting & Palette: Cinematic soap-opera drama, teal and amber color grade, 9:16 vertical orientation.
     Action: [Exact action].
     ```
   - Extract the generated image URL and download to disk.
3. **Secondary Choice — ChatGPT Fallback (`chatgpt.com` via Playwriter):**
   - If Gemini is blocked, rate-limited, or unavailable, navigate to the dedicated ChatGPT automation thread.
   - Use `await chatPage.keyboard.insertText(prompt)` to submit without timing out.
4. **Save Standardized Reference Assets:**
   Save the 6 reference files locally to:
   `episodes/episode-XX/ref_shot_01.png` ... `episodes/episode-XX/ref_shot_06.png`.

---

### Stage 2: Video Production (Google Flow)

1. **Access Flow Project:** Locate the Google Flow project tab using Playwriter (`flow.google.com/project/<project-id>`).
2. **Upload Ingredients:** Upload all generated reference images (`ref_shot_01.png` to `ref_shot_06.png`) as image ingredients into Flow.
3. **Dual-Anchor Conditioning Prompts:** For each shot, structure the prompt with:
   - Asset token: `@CharacterName` (e.g. `asset:Arul`, `asset:Priya`)
   - Visual reference: Click/attach the corresponding `ref_shot_0X.png` chip
   - Camera & Motion prompt: Detail camera move (slow push-in, static close-up), lighting, and subtle micro-expressions. **NEVER put spoken dialogue inside video prompts** to avoid mumbled AI audio.
   - Model Settings: Omni 1.1 Flash, 720p, 9:16 vertical, 8-second generation.
4. **Video Retrieval Without Modals:**
   - Wait until generation progress reaches 100%.
   - Trigger hover on the newly created tile: `await flowPage.locator('flow-grid-tile-container').first().hover()`.
   - Extract the signed video CDN URL instantiated in the DOM: `document.querySelector('flow-grid-tile-container video').src`.
   - Download directly using:
     ```bash
     curl -s -L "<url>" -o "episodes/episode-XX/scene-0X.mp4"
     ```

---

### Stage 3: Visual Master Assembly (FFmpeg)

Concatenate the generated clips losslessly using the FFmpeg concat demuxer:

```bash
cat << 'EOF' > /tmp/concat_epXX.txt
file '/path/to/episodes/episode-XX/scene-01.mp4'
file '/path/to/episodes/episode-XX/scene-02.mp4'
file '/path/to/episodes/episode-XX/scene-03.mp4'
file '/path/to/episodes/episode-XX/scene-04.mp4'
file '/path/to/episodes/episode-XX/scene-05.mp4'
file '/path/to/episodes/episode-XX/scene-06.mp4'
EOF

ffmpeg -y -f concat -safe 0 -i /tmp/concat_epXX.txt -c copy "episodes/episode-XX/episode-XX.mp4"
```

Verify total duration: `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 episodes/episode-XX/episode-XX.mp4` ($\ge 45.0\text{s}$ and $\le 60.0\text{s}$).

---

### Stage 4: Voice Synthesis, Hybrid Foley & Audio Dubbing Engine

Implement `scripts/dub_episode_XX.py`:

#### A. Voice Acting (Sarvam AI API)
- **Model:** `bulbul:v3` or `bulbul:v4-flash`, 48000 Hz sample rate.
- **Voice Mapping:**
  - Tamil: Arul $\to$ `ratan`, Priya $\to$ `ishita`, Pandi $\to$ `vijay`, Veera $\to$ `mani`
  - Hindi: Arul $\to$ `shubh`, Priya $\to$ `priya`, Pandi $\to$ `varun`, Veera $\to$ `shubh`
- **Pacing & Natural Delivery:** Adjust `pace` (0.95–1.10) and `temperature` (0.60–0.65) so lines fit comfortably within shot boundaries with $\ge 0.4\text{s}$ cushion.

#### B. Hybrid Audio Bed & Speech Collision Gating
1. **Preserve Authentic Video Audio:** Extract audio from speech-free takes (e.g. ambient nature, crowds, physical actions) to form the base 48kHz audio track.
2. **Speech Collision Gate:** In any shot where character dialogue plays (or where Omni generated English AI commentary), mute/purge raw audio to guarantee zero voice collision.
3. **Dynamic Ducking:** Apply smooth -3.5dB to -4dB ducking under dialogue lines.

#### C. Audio Muxing
```bash
ffmpeg -y -i episode-XX.mp4 -i soundtrack.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest episode-XX-lang.mp4
```

---

### Stage 5: Subtitle Formatting & Screen Protection (Rule 9)

1. **Write ASS Subtitle File:** Use English translation formatted for `720x1280` vertical canvas:
   ```ini
   [Script Info]
   Title: Series Ep XX English Subs
   ScriptType: v4.00+
   PlayResX: 720
   PlayResY: 1280

   [V4+ Styles]
   Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
   Style: Default,Arial,34,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,2.2,1.2,2,40,40,110,1

   [Events]
   Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
   Dialogue: 0,0:00:06.40,0:00:09.60,Default,,0,0,0,,Dialogue line 1 here.
   ```
2. **Burn Subtitles with libass:**
   ```bash
   ffmpeg -y -i episode-XX-lang.mp4 -vf "ass='episode-XX-en.ass'" -c:v libx264 -preset fast -crf 18 -c:a copy episode-XX-lang-captioned.mp4
   ```

---

### Stage 6: Quality Gate Audits & Verification

Run automated Python verification to audit duration, audio channels, and canvas bounding boxes:
- Verify duration $\ge 45.0\text{s}$ and $\le 60.0\text{s}$.
- Verify pure ASS canvas: text bounded strictly in rows 1107–1169 (~111px margin from bottom edge, 100% face/chest protection).

---

### Stage 7: MANDATORY USER APPROVAL GATE & SMM DISTRIBUTION

1. **Showcase to User:** Present verification metrics, video file paths, and keyframe stills.
2. **STOP AND WAIT:** Do NOT execute Drive uploads, SMM commands, or Sheets updates.
3. **Strict Sequential Queue Invariant:** Ensure episodes in the Google Sheets publishing queue are enrolled in strict chronological order (Episode 1 -> Episode 2 -> Episode 3 -> Episode 4...). Never skip or queue out of order because the automated publisher processes rows sequentially. Always confirm prior episodes are in the queue before enrolling the next.
4. **Execution Upon Explicit User Approval:**
   Once the user reviews and explicitly commands ("approved", "proceed to queue"):
   ```bash
   # Tamil Distribution
   python3 /media/vedha/E2/freelance/tools/smm_queue_episode.py \
     --video "/path/to/episodes/episode-XX/episode-XX-tamil-captioned.mp4" \
     --mode queue --channel "Story Time Tamil" --lang "ta-IN" --episode XX \
     --title "<Title> 📞💔 | Series Ep. XX #Shorts #Tamil"

   # Hindi Distribution
   python3 /media/vedha/E2/freelance/tools/smm_queue_episode.py \
     --video "/path/to/episodes/episode-XX/episode-XX-hindi-captioned.mp4" \
     --mode queue --channel "Story Time Hindi" --lang "hi-IN" --episode XX \
     --title "<Title> 📞💔 | Series Ep. XX #Shorts #Hindi"
   ```
