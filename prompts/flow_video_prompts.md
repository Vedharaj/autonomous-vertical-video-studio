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

## 3. Cinematic Video Generation Master Scene Prompt Standard

Every shot prompt in Google Flow MUST strictly follow this exact 10-section template:

```text
# CINEMATIC VIDEO GENERATION — MASTER SCENE PROMPT

## 1. REFERENCE ASSETS
- Character reference: @CharacterName
- Location reference: @LocationName
- Prop reference: @PropName
- Previous shot / start frame: [Attach the final frame of the previous clip when needed]

Use the attached references as the visual authority for identity, appearance, environment and object design. Do not reinterpret or redesign them.

## 2. CHARACTER IDENTITY LOCK
The main character is [CHARACTER NAME], a [AGE]-year-old [GENDER] with [FACE SHAPE], [SKIN TONE], [EYE SHAPE AND COLOR], [NOSE], [HAIR STYLE], [FACIAL HAIR], [HEIGHT AND BUILD], and [DISTINCTIVE FEATURES].

Clothing: [EXACT GARMENT, COLOR, FABRIC, FIT, SHOES AND ACCESSORIES].

Preserve the same facial identity, age, hairstyle, skin tone, body proportions, clothing and accessories as the character reference. Maintain natural anatomy and realistic facial expressions.

## 3. LOCATION AND ENVIRONMENT LOCK
The scene takes place in [EXACT LOCATION]. Preserve the reference's architecture, room dimensions, wall colors, floor material, doors, windows, furniture, background objects and spatial arrangement.

Important landmarks:
- [LANDMARK 1 AND POSITION]
- [LANDMARK 2 AND POSITION]
- [LANDMARK 3 AND POSITION]

Do not add, remove, relocate or redesign established objects unless explicitly required by the action.

## 4. CONTINUITY STATE
Story timeline: [DAY / NIGHT / EXACT STORY TIME].
Weather: [WEATHER].
Lighting condition: [LIGHTING].
Character position at the start: [POSITION AND ORIENTATION].
Previous action: [WHAT HAPPENED IN THE PREVIOUS SHOT].
Current emotional state: [EMOTION].
Props currently held or placed: [OBJECT AND EXACT POSITION].

Begin from this established state. Preserve all details that are not explicitly changed by the new action.

## 5. BLOCKING AND ACTION
At the beginning, [CHARACTER] stands/sits at [EXACT POSITION], facing [DIRECTION].

Action sequence:
1. Start with [INITIAL POSE].
2. The character [PRIMARY ACTION].
3. During the action, [SUBTLE BODY MOVEMENT AND FACIAL EXPRESSION].
4. Finish with [FINAL POSE AND GAZE DIRECTION].

Use believable timing, natural body mechanics and continuous motion. Keep the action physically possible. Do not introduce unrelated actions.

## 6. CAMERA AND COMPOSITION
Shot size: [WIDE / MEDIUM / CLOSE-UP / EXTREME CLOSE-UP].
Camera angle: [EYE LEVEL / LOW / HIGH / OVER-THE-SHOULDER].
Camera position: [EXACT RELATION TO CHARACTER AND LOCATION].
Lens aesthetic: [NATURAL CINEMATIC PERSPECTIVE / SHALLOW DEPTH OF FIELD].
Camera movement: [STATIC / SLOW DOLLY / TRACKING / PAN / TILT].
Composition: [SUBJECT POSITION, HEADROOM, FOREGROUND AND BACKGROUND].
Focus: [PRIMARY SUBJECT OR OBJECT].

Use one coherent camera setup. Avoid unintended cuts, sudden zooms, camera teleportation or changing screen direction.

## 7. LIGHTING AND VISUAL STYLE
Lighting: [KEY LIGHT DIRECTION, FILL LIGHT, PRACTICAL LIGHT SOURCES].
Color palette: [FIXED COLORS].
Contrast: [SOFT / MODERATE / HIGH].
Visual style: [PHOTOREALISTIC CINEMA / ANIMATION STYLE: Stylized 3D / Ghibli-inspired].
Texture: [SKIN, FABRIC, WOOD, METAL AND ENVIRONMENTAL DETAIL].
Atmosphere: [MOOD AND AMBIENCE].

Maintain the established visual style and color grading. Keep lighting consistent with the location, time and previous shot.

## 8. AUDIO AND DIALOGUE
Ambient sound: [ROOM TONE, WIND, RAIN, TRAFFIC OR OTHER SOUNDS].
Character voice: [VOICE DESCRIPTION OR ATTACHED VOICE REFERENCE].
Dialogue: "[EXACT SPOKEN LINE]".
Delivery: [PACE, EMOTION, VOLUME AND PAUSES].
Other sounds: [FOOTSTEPS, OBJECT MOVEMENT OR SILENCE].

Only the specified character speaks. Keep dialogue and sound effects appropriate to the action. If there is no dialogue, specify no spoken dialogue.

## 9. FINAL FRAME AND CONTINUITY HANDOFF
The clip ends with [EXACT FINAL POSE, CAMERA FRAMING AND OBJECT STATE].

The final frame must be usable as the starting reference for the next shot. Preserve the character's identity, clothing, location layout, prop positions, lighting direction and screen direction.

## 10. QUALITY CONTROL
No identity drift, face morphing, wardrobe changes, duplicated characters, extra limbs, floating objects, unexplained prop changes, inconsistent architecture, flickering lighting, unnatural motion or unintended scene transitions.

Generate one continuous, visually coherent shot that follows the supplied references and the action specified above.
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
