# Production Invariants & Studio Safety Guardrails

> Hierarchical workspace rules loaded automatically by Antigravity CLI for all files in this project.

## 1. Local by Default Invariant
- All project-specific agents, skills, rules, prompts, and configurations MUST be created and maintained inside this project repository.
- Never write project-specific customizations to `~/.gemini/antigravity-cli/skills/` or other machine-global paths.

## 2. Multi-Anchor Conditioning & Continuity-Locked Prompt Invariant
- Standalone reference frames in Gemini Vision must use single unified camera perspective.
- Mandatory negative constraint in all image prompts: `"Single unified composition, absolutely NO split screen, NO multi-panel collage, NO duplicated characters, NO motion trail lines, NO text."`
- Video takes in Flow must be conditioned on actual visual ingredients: registered character asset(s) for identity + shot reference still for composition and pose. Attach chips for both characters in multi-character shots.
- **Continuity-Locked Prompt Standard:** Prompts must follow chronological sequencing (Beginning -> Action 1 -> Action 2 -> Reaction -> Ending), explicit spatial blocking (left/right positions, hand assignment for props), final-frame handoff, and shot-specific failure prevention.
- **Technical Control Enforcement:** Enforce `720p`, `9:16`, `duration`, and `Omni 1.1 Flash` via UI/API controls, never prompt text alone.
- **Zero-Dialogue Guard:** NEVER include spoken dialogue quotes in video prompts. Describe physical performance only to eliminate speech collision.
- **Episode Continuity Log:** Maintain an episode continuity log tracking left/right positions, hand assignments, and prop states across all shot cuts.

## 3. Verified Flow Take Retrieval Gate
- Inspect header (`h1` or `.header-title`) in the Flow editor before initiating download.
- Never download an unverified tile. Check file size (>1MB) and duration with `ffprobe`.

## 4. Universal Dialogue Coverage Invariant
- Every visual shot with interacting characters, comedy beats, celebrations, or reactions must have dubbed dialogue in all target languages (Tamil and Hindi). Never leave character action beats silent.

## 5. ASS Bottom-Center Subtitle Standard
- Subtitles burned onto vertical video masters MUST be in English.
- Use ASS format: `PlayResX: 720`, `PlayResY: 1280`, `Fontsize: 34`, `Alignment: 2` (Bottom-Center), `MarginV: 110`.
- Bounded strictly between vertical rows 1107 and 1169 (~111px above bottom edge).

## 6. Sequential Publishing Order Invariant
- Episodes must be enrolled in Google Sheets / SMM queue in strict numerical sequence ($1 \dots N$).
- Preceding episodes ($1 \dots N-1$) must be verified present in the queue with status `COMPLETE` or `READY` before adding Episode $N$.

## 7. Mandatory Human Approval Gate
- Never upload to Google Drive or modify Google Sheets / SMM queues without explicit user authorization.
