# Vertical Short Fiction Series — Universal Production Rules

## 1. Mandatory Distribution Approval Gate (No Auto-Uploads)
- **Local Completion Only:** Assemble, dub, Foley-mix, and burn subtitles strictly in the local episode workspace.
- **Verification Showcase:** Present verification metrics (duration, audio channels, pure ASS canvas bounding box audit) and keyframe stills to the user.
- **STRICT INVARIANT:** NEVER upload to Google Drive, NEVER run `smm queue add`, and NEVER modify Google Sheets scheduling rows without explicit user approval.
- **Wait for Sign-Off:** Wait for explicit user confirmation (e.g. "approved", "proceed to queue") before executing any Drive or SMM distribution commands.

## 2. Reference Generation Priority (Gemini First)
- **Primary Engine:** Always generate 9:16 vertical shot reference images in Gemini (`gemini.google.com`) via Playwriter.
- **Fallback Engine:** Failover to ChatGPT (`chatgpt.com`) only if Gemini encounters rate limits or safety filter blocks.

## 3. Hybrid Audio Preservation & Speech Collision Gating
- **Background Preservation:** Preserve authentic 48kHz environmental audio (crowd murmur, sports action, nature, room tone) from AI video takes. Never replace with flat synthetic sine waves.
- **Speech Collision Gate:** In any shot featuring character dialogue (e.g. Pandi commentary), mute/purge raw video audio to eliminate baked-in English AI speech. Never let raw AI speech play concurrently with dubbed dialogue.
- **Dynamic Ducking:** Apply smooth -3.5dB to -4dB ducking under character speech so dialogue is punchy and diction is crystal clear, while ambient environment sounds remain audible.

## 4. Subtitle Standard (Bottom-Center English ASS Format)
- Subtitles must be in English ASS format (`PlayResX: 720`, `PlayResY: 1280`, `Fontsize: 34`, `Bold: 1`, `Alignment: 2` (Bottom-Center), `MarginV: 110`).
- Bounded strictly between vertical rows 1107 and 1169 (~111px margin from bottom edge, 100% face/chest protection).

## 5. Runtime Invariant (45s–60s)
- All episodes must adhere strictly to 45.0s–60.0s total runtime.

## 6. Google Flow Video Master Prompt Invariant
- Video generation prompts in Google Flow (`Omni 1.1 Flash`) must follow the Continuity-Locked Shot Prompt formula:
  `[Multi-Anchor Tokens] + [Camera Motion/Framing] + [Chronological Action Sequence: Beginning -> Action 1 -> Action 2 -> Reaction -> Ending] + [Physical/Facial Performance (Zero Dialogue)] + [Screen Positions & Prop Hand Assignment] + [Environment & Lighting] + [Final-Frame Handoff] + [Shot-Specific Failure Prevention]`
- **Actual Ingredient Attachment:** Supply actual visual ingredients for identity (approved character assets) and composition (shot reference image). When multiple characters appear, attach chips for both. Never rely on text filenames alone.
- **Technical Control Enforcement:** Enforce `720p`, `9:16`, `duration`, and `Omni 1.1 Flash` via Flow UI/API controls, not prompt text.
- **Zero-Dialogue Guard:** NEVER include spoken dialogue quotes in video prompts. Describe visual behavior and physical comedy only.
- **Continuity Tracking:** Maintain an episode continuity log tracking left/right positions, hand assignments, and prop states across every shot cut.
