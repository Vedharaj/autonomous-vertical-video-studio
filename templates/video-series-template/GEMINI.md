# Production Consistency & Operational Invariants

## Core Production Rules
1. **Character Consistency Locks:**
   - Reference registered character asset chips (`asset:<Character>`) and 360° turnaround reference sheets.
   - Preserve costume, props, and facial characteristics across all shots.
   - Never re-prompt character faces purely from text.

2. **Duration Strict Standard (45s–60s):**
   - Every episode MUST run between 45.0s and 60.0s in total master runtime.

3. **Dual-Anchor Conditioning in Flow:**
   - Always condition video generation in Google Flow using both:
     1. The registered character asset chip
     2. The specific shot reference image chip (`epXX_shotYY_ref.png`)

4. **Single-Perspective Reference Invariant:**
   - Every Gemini reference prompt must enforce a single unified camera perspective.
   - Mandatory negative constraints:
     `"Single unified composition, absolutely NO split screen, NO multi-panel collage, NO duplicated characters, NO motion trail lines, NO text."`

5. **Verified Take Retrieval Gate:**
   - Verify take title in Flow UI header before downloading to prevent wrong-video corruption.

6. **Hybrid Audio Architecture & Speech Collision Gating:**
   - Purge/mute raw video take audio during all dialogue shots.
   - Preserve authentic environmental ambiance from speech-free takes.
   - Apply smooth -3.5dB to -4dB dynamic ducking under character speech.

7. **Universal Dialogue Coverage Invariant:**
   - Every visual shot with interacting characters, comedy beats, celebrations, or reactions must include voiced dialogue in all target languages. Never leave character action beats silent.

8. **Bottom-Center English Subtitle Standard (ASS Format):**
   - Subtitles burned onto vertical video masters MUST be in English.
   - ASS parameters: `PlayResX: 720`, `PlayResY: 1280`, `Fontsize: 34`, `Alignment: 2` (Bottom-Center), `MarginV: 110`.
   - Strictly bounded between vertical rows 1107 and 1169 (~111px above bottom edge).

9. **Sequential Publishing Order Invariant:**
   - Episodes MUST be enrolled in Google Sheets / SMM queue in strict numerical sequence (Ep. 1 -> Ep. 2 -> Ep. 3 -> ...).
   - Preceding episodes ($1 \dots N-1$) must be verified present in the queue before adding Episode $N$.

10. **Mandatory Human Approval Gate:**
    - Never upload completed episode videos to Google Drive or modify Google Sheets / SMM queues without explicit user approval.
