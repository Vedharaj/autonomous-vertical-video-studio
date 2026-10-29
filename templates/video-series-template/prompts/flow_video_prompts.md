# Google Flow Video Prompting Guide — Continuity-Locked Production Standard

> Production-grade prompt engineering standards for generating vertical video takes (`Omni 1.1 Flash`, 720p, 9:16) with multi-anchor conditioning, chronological action sequencing, strict spatial blocking, and final-frame continuity handoffs.

---

## 1. Multi-Anchor Visual Conditioning

> [!IMPORTANT]
> **Actual Image Ingredients vs. Text Identifiers:** Writing a filename like `ep04_shot01_ref.png` in text does NOT feed the image to the video model. You MUST attach the actual uploaded/registered image ingredient via the Flow interface or API.

- **Identity Anchor:** Attach the approved, registered character reference(s):
  - **Web UI (Playwriter / Chrome):** `@CharacterName` chip (`@Veera`, `@Chintu`, `@Pandi`, `@Kavya`, `@Boss Mani`).
  - **Flow MCP API (`flow_generate`):** `asset:<CharacterName>` in `reference_images` array and prompt prefix.
  - **Multi-Character Shots:** Attach chips for *both* characters (e.g. `@Pandi` + `@Chintu` or `asset:Pandi` + `asset:Chintu`).
- **Composition & Pose Anchor:** Attach the specific shot reference image ingredient (`epXX_shotYY_ref.png`) to lock framing, starting pose, and spatial layout.
- **Technical Parameter Enforcement:** Never rely on prompt text to enforce resolution or ratio. Always set `resolution: "720p"`, `aspect_ratio: "9:16"`, `duration: 8` (or 6), and `model: "Omni 1.1 Flash"` directly via Flow UI drawer controls or Flow MCP call parameters.

---

## 2. Tested Workflow Invariants

1. **Prompt Sanitization (Dubbing-First Pipeline):** Omit spoken dialogue lines, quoted text, subtitles, or instructions to speak. Diffusion models synthesize garbled English commentary or erratic mouth movements when dialogue is present, creating dual-voice collision with Indic dubbing.
2. **One Principal Action Beat:** Keep each 6s–8s clip focused on one continuous, physically plausible action with a defined beginning, progression, and ending.
3. **Strict Spatial Blocking & Prop Tracking:** Explicitly define left/right screen positions, which hand holds each prop, and exact points of contact when characters interact.
4. **Final-Frame Handoff:** Describe the exact finishing pose, prop state, and character positions so the next shot's reference image matches the cut boundary seamlessly.
5. **Shot-Specific Failure Prevention:** Avoid generic boilerplates; target only the high-risk failure points for that specific action (e.g. hand swapping, sliding feet, phantom bat duplication).

---

## 3. Continuity-Locked Shot Prompt Template

```text
# GOOGLE FLOW — CONTINUITY-LOCKED SHOT PROMPT

## REFERENCE CONDITIONING
Ingredients attached: [Character asset(s)] + [Shot reference image]
Identity: @CharacterName1 [@CharacterName2]
Composition: epXX_shotYY_ref.png

## CAMERA
[Shot size: e.g. Static medium shot / Dynamic medium-wide / Slow cinematic push-in], [Camera angle: e.g. Eye-level / Low-angle / Over-the-shoulder], [Subject framing]. Smooth physical motion, preserving established screen direction and spatial relationships.

## ACTION SEQUENCE
Beginning: [Exact initial pose, screen position, and balance].
Action 1: [First physical movement, leading limb/prop].
Action 2: [Second movement, physical contact or follow-through].
Reaction: [Visible physical or facial response from interacting character, if present].
Ending: [Exact final pose, gaze direction, hand position, and prop state].

## FACIAL EXPRESSION AND BODY LANGUAGE
[Visible details: eye direction, blinking, eyebrow movement, mouth shape, head tilt, posture, balance, and timing]. Communicate emotion purely through physical performance. No spoken dialogue or instructions to speak.

## CHARACTER AND PROP CONTINUITY
Preserve approved chibi designs (1:2 head-to-body ratio), clothing, and props.
- Character positions: [Left / Right / Foreground / Background].
- Hand assignment: [Left hand / Right hand holding or touching specific prop].
- Prop state: [Starting position -> trajectory -> ending position].
- Interaction: [Who touches whom, which hand/arm is involved, direction of movement].

## ENVIRONMENT AND LIGHTING
Location: [Established location: e.g. Rustic South Indian village cricket ground / Tea stall].
Background landmarks: [Fixed background objects, stumps, banyan tree, scoreboard].
Lighting: [Direction, intensity, warm golden morning/midday sun, shadow consistency].
Atmosphere: [Subtle dust haze, gentle breeze rustling coconut palms].

## FINAL-FRAME HANDOFF
Finish with [specific final composition and pose]. Preserves resulting character positions and object states for the subsequent shot's continuity reference.

## SHOT-SPECIFIC FAILURE PREVENTION
Avoid: [Targeted failure points: e.g. hand swapping, floating feet, duplicated bat, morphing sunglasses, inconsistent ball trajectory]. Single coherent take without cuts or vocal synthesis.
```

---

## 4. Canonical Battle-Tested Examples

### Example 1 — Chintu Taps the Batting Crease (Ep 4 Shot 1)
* **Attached Ingredients:** `@Chintu` (Identity) + `ep04_shot01_ref.png` (Composition)
* **Flow MCP Call:** `reference_images: ["asset:Chintu", "asset:MatchFixers_Ep04_Refs-scene-01"]`

```text
Static medium shot of Chintu, the same chibi boy batsman from the character reference, standing at the batting crease. He shifts his weight nervously between his feet while tapping the bottom of the same wooden cricket bat against the dusty pitch three times. His eyes blink rapidly, his eyebrows lift slightly, and he swallows nervously while staring toward the unseen bowler. The bat remains in both hands throughout. Preserve his established clothing, proportions and facial design. Coconut palms sway gently in the background under consistent midday sunlight. End with the bat resting on the pitch and Chintu looking forward. Avoid: bat changing shape, sliding feet, or floating above ground.
```

### Example 2 — The Lucky Hit (Ep 4 Shot 3)
* **Attached Ingredients:** `@Chintu` (Identity) + `ep04_shot03_ref.png` (Composition)
* **Flow MCP Call:** `reference_images: ["asset:Chintu", "asset:MatchFixers_Ep04_Refs-scene-03"]`

```text
Dynamic medium-wide shot from the front of the same cricket crease. Chintu squeezes his eyes shut, grips the wooden bat with both hands and swings in one broad, clumsy horizontal arc. The red cricket ball approaches from the bowler's direction and visibly contacts the bat once. The ball launches upward and exits the top of the frame. Chintu's body rotates with the swing, his feet remain grounded until his weight shifts forward, and the bat follows through naturally. Preserve the bat's shape, the ball's red color and the established field layout. End with Chintu wobbling slightly but retaining his grip on the bat. Avoid: ball duplicating, bat vanishing on follow-through, or multiple bat swings.
```

### Example 3 — Pandi Hoists Chintu's Arm (Ep 4 Shot 6)
* **Attached Ingredients:** `@Pandi` + `@Chintu` (Identity) + `ep04_shot06_ref.png` (Composition)
* **Flow MCP Call:** `reference_images: ["asset:Pandi", "asset:Chintu", "asset:MatchFixers_Ep04_Refs-scene-06"]`

```text
Comedic medium shot on the same dusty village cricket ground. Pandi, wearing his established white referee shirt and dark sunglasses, approaches Chintu from the left side of the frame. Chintu stands on the right, holding his cricket bat in his left hand. Pandi reaches with his right hand, grasps Chintu's right wrist and raises Chintu's arm overhead in a single continuous motion, like a boxing champion announcing a winner. Pandi displays a broad, excited grin. Chintu's eyes widen, his eyebrows rise and his head tilts toward Pandi in bewilderment. Chintu keeps the bat in his left hand throughout. Both characters retain their established designs and clothing. Wooden stumps remain behind them. No spoken dialogue, mouth articulation intended as speech, subtitles or captions. End with Pandi holding Chintu's right arm aloft while Chintu looks confused. Avoid: bat switching to right hand, sunglasses disappearing from Pandi, or disconnected wrist grasp.
```

### Example 4 — Tea Stall Confrontation (Ep 6 Shot 1)
* **Attached Ingredients:** `@Boss Mani` + `@Veera` (Identity) + `ep06_shot01_ref.png` (Composition)
* **Flow MCP Call:** `reference_images: ["asset:Boss Mani", "asset:Veera", "asset:MatchFixers_Ep06_Shot01_Ref-scene-01"]`

```text
Eye-level medium-wide two-shot under the rustic village banyan tree. Boss Mani, on the left in his floral Hawaiian shirt, gold chain, and curled mustache, leans toward young chibi batsman Veera, standing on the right in blue cricket jersey. Boss Mani places his heavy right hand onto Veera's left shoulder, pulling him a half-step closer while glancing suspiciously left and right. Veera holds his curved wooden bat in his right hand, resting it against the ground, while looking up at Boss Mani with skeptical, narrowed eyes. In the distant background, village teammates celebrate near the wooden tea bench. Warm morning sunlight filters through banyan leaves. End with Boss Mani whispering close to Veera's ear and Veera frowning skeptically. Avoid: bat changing hands, floral shirt pattern morphing, or gold chain vanishing.
```

---

## 5. Episode Continuity Log Standard

For every episode, maintain an `assets/epXX/continuity_log.md` tracking physical elements across shot boundaries:

| Shot | Characters & Screen Positions | Props & Hand Assignment | Ending Pose & State | Handoff to Next Shot |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Mani (Left), Veera (Right) | Bat in Veera's right hand | Mani's hand on Veera's shoulder | Cut to medium close-up of Mani |
| **02** | Mani (Center-Left) | Phone in Mani's left pocket | Mani pointing right index finger | Match eye-line to Veera looking up |
| **...** | ... | ... | ... | ... |
