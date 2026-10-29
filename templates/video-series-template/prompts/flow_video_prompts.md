# Google Flow Video Prompting Guide

> Sanitized prompt engineering standards for generating 720p 9:16 vertical video takes (`Omni 1.1 Flash`) with Dual-Anchor conditioning.

---

## 1. Dual-Anchor Conditioning Setup

In the Google Flow prompt bar, always condition generation with registered character tokens AND the shot reference image chip:

- **Web UI (Playwriter / Chrome):**
  - Character chips: `@Veera`, `@Chintu`, `@Pandi`, `@Kavya`, `@Boss Mani`.
  - Shot reference image chip: `epXX_shotYY_ref.png`.
- **Flow MCP API (`flow_generate`):**
  - Character token: `asset:<Character>` (e.g. `asset:Boss Mani`, `asset:Veera`).
  - Reference still token: `asset:<Project>-<Scene>` (e.g. `asset:MatchFixers_Ep06_Shot01_Ref-scene-01`).
  - Add all tokens to `reference_images: ["asset:Boss Mani", "asset:Veera", "asset:..."]`.

---

## 2. Zero-Dialogue Prompt Sanitization Guard

> [!CAUTION]
> **NEVER paste dialogue lines or spoken quotes into Google Flow video prompts.**
> Video diffusion models attempt to synthesize speech when words or quotes are in the prompt, producing garbled English commentary or mumbling voices that cause severe speech collision with multilingual dubbing.

**Always describe physical cues, expressions, and comedy reactions only.**

---

## 3. The 6-Slot Master Prompt Architecture

Every video generation prompt in Flow must follow this standardized 6-slot structure:

```text
[SLOT 1: DUAL/MULTI-ANCHOR TOKENS]
asset:<Character1> [asset:<Character2>] asset:<ShotReferenceStill>

[SLOT 2: CAMERA MOVEMENT & FRAMING]
[e.g. Eye-level medium wide shot / Static tripod camera / Handheld slow cinematic push-in].

[SLOT 3: CHARACTER VISUAL LOCKS & COSTUMES]
[Character 1 name] with oversized round head and stubby chibi proportions (1:2 head-to-body ratio) in [exact costume, signature props]; [Character 2 name] in [exact costume].

[SLOT 4: SANITIZED PHYSICAL ACTION BEAT]
[Describe concrete physical movement, gestures, steps — ZERO dialogue quotes].

[SLOT 5: FACIAL EXPRESSION & COMEDY REACTION]
[Micro-expressions: eyebrow twitch, wide comedic eye blink, nervous gulp, forced wide smile].

[SLOT 6: ENVIRONMENT & LIGHTING CONTINUITY]
[Rustic location details, sunlight direction, soft breeze, environmental palette].
```

---

## 4. Battle-Tested Examples

### Example 1: Multi-Character Interaction (Ep 6 Shot 1)
```text
asset:Boss Mani asset:Veera asset:MatchFixers_Ep06_Shot01_Ref-scene-01 Eye-level medium wide shot at rustic South Indian village tea stall under a sprawling banyan tree. Boss Mani with oversized round head and stubby chibi proportions in colorful floral Hawaiian shirt, gold neck chain, and thick curled mustache pulls young chibi boy batsman Veera in blue cricket jersey aside by his shoulder near the wooden tea stall bench while cricket team celebrates in background. Soft warm morning village daylight.
```

### Example 2: Crease Tapping & Nervous Breathing (Ep 4 Shot 1)
```text
asset:Chintu asset:ep04_shot01_ref.png Static medium shot of chibi boy batsman Chintu standing at the batting crease. Chintu with oversized round head, messy black hair, and stubby chibi body in yellow T-shirt shifts his weight from foot to foot, repeatedly tapping the bottom of his heavy wooden cricket bat on the dusty pitch. His wide round eyes blink rapidly as he gulps nervously and looks ahead towards the bowler. Dusty cricket pitch, coconut trees in background swaying gently in breeze.
```

### Example 3: Blind Swing & Lucky Bat Connection (Ep 4 Shot 3)
```text
asset:Chintu asset:ep04_shot03_ref.png Fast dynamic front-facing shot of chibi batsman Chintu in yellow T-shirt tightly shutting his eyes in fear while swinging his heavy wooden bat with all his strength in a clumsy wide horizontal arc. The red cricket ball strikes the sweet spot of the bat with high velocity and launches upward out of frame. Chintu wobbles off-balance from the follow-through, bat drooping in hands.
```

### Example 4: Pandi Referee Arm Hoist (Ep 4 Shot 6)
```text
asset:Pandi asset:Chintu asset:ep04_shot06_ref.png Comedic medium shot of Pandi in referee white shirt and dark sunglasses excitedly running over to Chintu. Pandi grabs Chintu's right arm and hoists it high into the air like a victorious boxing champion. Pandi is grinning broadly and laughing excitedly, while Chintu stands wide-eyed, blinking in utter confusion holding his cricket bat. Dusty village ground background, wooden stumps behind them.
```

### Example 5: Solo Reaction Beat (Ep 6 Shot 5)
```text
asset:Veera asset:MatchFixers_Ep06_Refs-scene-02 Medium eye-level close-up of chibi batsman boy Veera in blue cricket jersey standing under the banyan tree shade. He sighs reluctantly, looking down at the ground with furrowed brows, slowly nodding his head in uncomfortable agreement. Wooden bat resting loosely against his leg. Warm morning daylight filtering through banyan leaves.
```

### Example 6: Two-Plane Dynamic Framing (Ep 6 Shot 6)
```text
asset:Boss Mani asset:Veera asset:MatchFixers_Ep06_Refs-scene-03 Wide shot under sprawling banyan tree. In the foreground, Boss Mani with round belly, floral shirt, and big mustache wipes sweat from his forehead with a handkerchief while holding his glowing mobile phone, smiling with sneaky relief. In the midground, chibi boy batsman Veera in blue cricket jersey walks away towards the distant sunny cricket ground, glancing back once over his shoulder. Soft dusty golden sunlight.
```
