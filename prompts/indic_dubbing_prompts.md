# Sarvam AI Indic Dubbing & Subtitling Guide

> Character voice archetypes, colloquial translation formulas, and Universal Dialogue Coverage rules for Tamil (`ta-IN`) and Hindi (`hi-IN`).

---

## Universal Dialogue Coverage Rule

> [!IMPORTANT]
> **Every visual shot featuring character interaction, comedy, or celebrations must include voiced dialogue in both target languages.**
> Even when script outlines list physical action only (e.g. umpire signals, referee arm hoist, crowd reaction), author punchy character dialogue. Never leave character action beats silent.

---

## Character Voice Archetypes (Sarvam `bulbul:v3`)

| Character | Personality / Archetype | Tamil Voice (`ta-IN`) | Hindi Voice (`hi-IN`) | Pace | Temp |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Veera** | Grounded team captain, earnest, stressed | `ratan` | `shubh` | `1.05` | `0.65` |
| **Chintu** | Clueless kid, nervous, wide-eyed | `rohan` | `ashutosh` | `1.15` | `0.70` |
| **Pandi** | Flamboyant commentator & referee, boastful | `vijay` | `varun` | `1.10` | `0.65` |
| **Kavya** | Sharp scorer, quiet investigator, suspicious | `ishita` | `priya` | `1.05` | `0.65` |
| **Boss Mani** | Smug local sponsor, secret match-fixer | `ratan` (low pitch) | `shubh` (commanding) | `1.00` | `0.60` |

---

## Dialogue Timings & Synchronized English ASS Subtitles

### Shot 2: Non-Striker Advice (8.0s shot, dialogue 8.5s–12.0s)
* **Tamil (`ta-IN`, Veera):**
  `"கண்ணை மூடி சுத்தாதே சின்டு! பந்தை மட்டும் பாரு!"`
* **Hindi (`hi-IN`, Veera):**
  `"आँखें बंद करके मत घुमा चिंटू! बस गेंद पर नज़र रख!"`
* **English ASS Subtitle (00:00:08.50 -> 00:00:12.00):**
  `"Don't swing blindly, Chintu! Just keep your eyes on the ball!"`

### Shot 5: Post-Hit Confusion (8.0s shot, dialogue 32.5s–36.0s)
* **Tamil (`ta-IN`, Chintu):**
  `"அய்யோ... பந்து எங்க போச்சு? நான் அவுட்டா?"`
* **Hindi (`hi-IN`, Chintu):**
  `"अरे... बॉल कहाँ गई? क्या मैं आउट हो गया?"`
* **English ASS Subtitle (00:00:32.50 -> 00:00:36.00):**
  `"Oh no... where did the ball go? Am I out?"`

### Shot 6: Pandi Arm Hoist Punchline (8.0s shot, dialogue 40.5s–44.8s)
* **Tamil (`ta-IN`, Pandi):**
  `"இதோ நம்ம புதிய சாம்பியன் சின்டு! சிக்ஸர் கிங் டா நீ!"`
* **Hindi (`hi-IN`, Pandi):**
  `"और ये रहे हमारे नए चैंपियन चिंटू! सिक्सर किंग है तू भाई!"`
* **English ASS Subtitle (00:00:40.50 -> 00:00:44.80):**
  `"Here is our new champion Chintu! You are the Sixer King!"`

---

## Subtitle Styling Specification (ASS Format)

```ini
[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,34,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,3.0,0,2,40,40,110,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:08.50,0:00:12.00,Default,,0,0,0,,Don't swing blindly, Chintu! Just keep your eyes on the ball!
Dialogue: 0,0:00:32.50,0:00:36.00,Default,,0,0,0,,Oh no... where did the ball go? Am I out?
Dialogue: 0,0:00:40.50,0:00:44.80,Default,,0,0,0,,Here is our new champion Chintu! You are the Sixer King!
```
