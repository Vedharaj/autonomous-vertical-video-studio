# Google Flow Video Prompting Guide

> Sanitized prompt engineering standards for generating 720p 9:16 vertical video takes (`Omni 1.1 Flash`) with Dual-Anchor conditioning.

---

## Dual-Anchor Conditioning Setup

In the Google Flow prompt bar, always condition generation with **two chips**:
1. Registered character asset chip: `@Veera`, `@Chintu`, `@Pandi`, `@Kavya`, or `@BossMani`.
2. Shot reference image chip: `epXX_shotYY_ref.png`.

---

## Prompt Sanitization Rule

> [!CAUTION]
> **NEVER paste dialogue lines or spoken text into Google Flow video prompts.**
> Video diffusion models attempt to synthesize speech when words or quotes are in the prompt, producing garbled English commentary or mumbling voices that destroy multilingual dubbing.

**Instead, describe physical cues, expressions, and comedy reactions only.**

---

## Standard Flow Prompt Template

```text
@Character epXX_shotYY_ref.png
[CAMERA MOVEMENT]: (e.g. Static tripod camera / Slow cinematic push-in / Handheld subtle drift).
[ACTION BEAT]: [Describe precise physical motions, gestures, steps].
[FACIAL EXPRESSION & COMEDIC REACTION]: [Describe eye blinks, mouth drop, brow furrow, smiling].
[LIGHTING & ENVIRONMENT CONTINUITY]: Warm dusty South Indian village cricket ground, midday sun, gentle breeze rustling coconut palms.
```

---

## Battle-Tested Examples

### Example 1: Crease Tapping & Nervous Breathing (Ep 4 Shot 1)
```text
@Chintu ep04_shot01_ref.png
Static medium shot of chibi boy batsman Chintu standing at the batting crease. He nervously shifts his weight from foot to foot, repeatedly tapping the bottom of his heavy wooden cricket bat on the dusty pitch. His wide round eyes blink rapidly as he gulps nervously and looks ahead towards the bowler. Dusty cricket pitch, coconut trees in background swaying gently in breeze.
```

### Example 2: Blind Swing & Lucky Bat Connection (Ep 4 Shot 3)
```text
@Chintu ep04_shot03_ref.png
Fast dynamic front-facing shot of chibi batsman Chintu tightly shutting his eyes in fear while swinging his heavy wooden bat with all his strength in a clumsy wide horizontal arc. The red cricket ball strikes the sweet spot of the bat with high velocity and launches upward out of frame. Chintu wobbles off-balance from the follow-through, bat drooping in hands.
```

### Example 3: Pandi Referee Arm Hoist (Ep 4 Shot 6)
```text
@Pandi @Chintu ep04_shot06_ref.png
Comedic medium shot of Pandi in referee white shirt and dark sunglasses excitedly running over to Chintu. Pandi grabs Chintu's right arm and hoists it high into the air like a victorious boxing champion. Pandi is grinning broadly and shouting congratulations, while Chintu stands wide-eyed, blinking in utter confusion holding his cricket bat. Dusty village ground background, wooden stumps behind them.
```
