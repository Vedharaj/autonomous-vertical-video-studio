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

## 6. Google Flow Video Master Prompt Invariant (Cinematic Master Scene Prompt)
- **Character Tagging in Google Flow:** Always use `@character-name` (e.g. `@mani`, `@veera`, `@chintu`, `@pandi`, `@kavya`).
- **Mandatory Character Descriptors in Every Shot:**
  Every shot prompt MUST explicitly describe: complete outfit (garments, colors, fabrics, shoes, accessories), size, height, body proportions (e.g. chibi 1:2 head-to-body ratio, stubby limbs), and cartoon theme/aesthetic (stylized 3D animation / Ghibli-inspired aesthetic).
- **Exact 10-Section Prompt Structure:** Every video generation prompt in Google Flow (`Omni 1.1 Flash`) MUST strictly follow the exact 10-section formula:
  `# CINEMATIC VIDEO GENERATION — MASTER SCENE PROMPT`
  `## 1. REFERENCE ASSETS` (Character reference: @CharacterName, Location reference: @LocationName, Prop reference: @PropName, Previous shot / start frame)
  `## 2. CHARACTER IDENTITY LOCK` (Character name, age, gender, facial traits, height, build, complete outfit, accessories)
  `## 3. LOCATION AND ENVIRONMENT LOCK` (Exact location, architecture, dimensions, furniture, fixed landmarks)
  `## 4. CONTINUITY STATE` (Timeline, weather, lighting, starting position, previous action, emotional state, held props)
  `## 5. BLOCKING AND ACTION` (Exact starting pose, chronological action sequence 1-4, physically plausible motion)
  `## 6. CAMERA AND COMPOSITION` (Shot size, angle, position, lens aesthetic, movement, composition, focus)
  `## 7. LIGHTING AND VISUAL STYLE` (Key light, fill, practical lights, fixed color palette, contrast, visual style [stylized 3D / Ghibli], textures, atmosphere)
  `## 8. AUDIO AND DIALOGUE` (Ambient sound, character voice, dialogue; for dubbing-first clips specify: "No spoken dialogue" to prevent diffusion speech collision)
  `## 9. FINAL FRAME AND CONTINUITY HANDOFF` (Exact final pose, camera framing, object state for next cut)
  `## 10. QUALITY CONTROL` (Negative constraints: no identity drift, face morphing, wardrobe changes, duplicated characters, extra limbs, floating objects, flickering lighting)
- **Actual Ingredient Attachment:** Supply actual visual ingredients for identity (approved character assets) and composition (shot reference image). When multiple characters appear, attach chips for both. Never rely on text filenames alone.
- **Technical Control Enforcement:** Enforce `720p`, `9:16`, `duration`, and `Omni 1.1 Flash` via Flow UI/API controls, not prompt text.
- **Continuity Tracking:** Maintain an episode continuity log tracking left/right positions, hand assignments, and prop states across every shot cut.

## 12. Universal Dialogue Coverage Invariant (Zero Silent Shots)
- **No Silent Action Beats:** Never leave character action, comedy, or celebration beats silent. Even when script outlines list physical action only (e.g. referee arm hoist, crowd reaction), author punchy character dialogue in all target languages (Tamil & Hindi).
- **Shot 1 Dialogue Hook:** Establishing and opening shots MUST NEVER be silent visual filler. If characters interact, enter, or pull someone aside in Shot 1, vocal dialogue or voiceover narration must begin within the first 1.5 seconds to secure viewer retention.
- Synchronize matching bottom-center English ASS subtitles for every spoken line.

## 13. Atomic Prompt Injection Invariant (Zero Asset Search Collision)
- **Atomic Text Insertion Only:** When automating Google Flow video prompts, NEVER type prompts containing `@character-name` character-by-character using `keyboard.type()`.
- **Root Cause Prevention:** Character keystroke listeners in Google Flow's ProseMirror editor trigger the Asset Mention autocomplete modal on `@`, which hijacks keyboard focus into `<input class="search-input">`.
- **Enforcement:** Always use atomic text insertion (`keyboard.insertText()` or CDP `Input.insertText`) or clipboard paste (`ControlOrMeta+v`) preceded by an `Escape` keypress to clear active overlays.

## 14. Dramatic Action Guard for Prop-Equipped Characters
- **Sports Gear Diffusion Bias:** When characters possess iconic sports equipment in their asset reference (e.g., Veera's bent cricket bat), diffusion models (Omni 1.1 Flash) will default to athletic action (batting, swinging, running) even during tense dialogue or quiet comedy scenes.
- **Mandatory Negative Action Constraints:** In any shot requiring non-athletic drama, conversation, or comedic reactions, Section 5 (Blocking) and Section 10 (Quality Control) of the Master Scene Prompt MUST explicitly forbid unintended sports actions:
  `"ABSOLUTELY NO CRICKET BATTING, NO SWINGING BAT, NO BALL HITTING, NO PITCH ACTION. Physical action is strictly: [specific dramatic/dialogue action]."`

## 15. Solo Character Scene Guard (Zero Duplicate / Cloned Characters)
- **OTS Ban for Solo Scenes:** When generating single-character dialogue, calculation, or contemplation shots in Google Flow (Omni 1.1 Flash), NEVER specify "over-the-shoulder" (OTS) framing. OTS prompts cause diffusion models to create two instances of the character (one foreground back-view, one background front-view).
- **Approved Solo Framing:** Frame single-character shots strictly as 45° three-quarter medium shots, side profiles, or solo medium close-ups.
- **Mandatory Negative Duplication Constraints:** Section 5 (Blocking) and Section 10 (Quality Control) of the Master Scene Prompt MUST explicitly forbid duplicate characters:
  `"SOLO CHARACTER ONLY, EXACTLY ONE PERSON IN SCENE. ABSOLUTELY NO SECOND CHARACTER, NO TWIN, NO CLONE, NO OVER-THE-SHOULDER FOREGROUND PERSON, NO SILHOUETTES."`

## 16. Wardrobe & Hair Continuity Lock for Emotional Close-Ups
- **Diffusion Wardrobe Drift Bias:** In dramatic close-ups or emotional reaction shots where body visibility is reduced, diffusion models (Omni 1.1 Flash) frequently drift to generic everyday clothing (e.g., blue kurti, casual tunic, t-shirt) and default hairstyles (e.g., top buns).
- **Mandatory Negative Wardrobe Constraints:** Section 2 (Character Identity Lock) and Section 10 (Quality Control) MUST explicitly state negative wardrobe and hair exclusions:
  `"ABSOLUTELY NO BLUE KURTI, NO TUNIC, NO CASUAL SHIRT, NO DRESS, NO BUN HAIRSTYLE. Uniform is strictly: [canonical garments, colors, collar trim, footwear] and [canonical hair style/accessories]."`
- **Turnaround Reference Attachment for Re-Renders:** Whenever re-rendering a shot due to wardrobe or styling drift, always generate and attach a verified turnaround reference still (`clip-01.jpeg`) as a composition/character ingredient chip alongside the primary character token.

