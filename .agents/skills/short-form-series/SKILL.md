---
name: short-form-series-developer
description: Develops an original 20-episode fictional series of roughly 30-second short-form videos, using supplied YouTube Shorts transcripts only as abstract reference for storytelling technique. Use when the user wants to create an original serialized short-form fiction series, season outline, story bible, or episode scripts for vertical video. Requires transcripts or a written brief before starting.
---

# Short-Form Series Developer

## Purpose
Build an original 20-episode series of ~30-second episodes. Reference transcripts inform technique (hooks, pacing, dialogue density, cliffhangers). They never supply characters, worlds, dialogue, or event sequences.

## Phase 0: Intake (required before any work)
Ask for any missing items in one message:
- Channel transcripts (text) and optional titles/metadata
- Genre, language, target audience
- Production constraints (locations, cast size, budget, VFX limits)

If transcripts are absent, say so and proceed only with the brief. Do not invent a "reference analysis" of material you have not seen.

## Phase 1: Source Analysis
Extract only abstract technique: hook types, dialogue density (words per second), pacing, genre conventions, cliffhanger methods, emotional arcs, structural patterns. Record nothing distinctive: no named characters, world details, catchphrases, or sequences.

## Phase 2: Concepts
Produce five substantially different concepts. For each: title, premise, genre, main characters, central conflict, mystery or dramatic question, potential for 20 episodes, possible ending. Recommend one and state why in two sentences.

**Stop here for approval of the concept.**

## Phase 3: Story Bible
Include: character profiles, motivations and secrets, setting and world rules, chronological timeline, revelation timeline, character arcs, central mystery, major plot turns, final resolution. Start a continuity ledger.

**Stop here for approval of the bible.**

## Phase 4: Season Outline
Plan all 20 episodes before any script. For each: number, title, objective, conflict, new information revealed, character development, link to earlier episodes, ending beat, setup for next episode. Not every episode needs a cliffhanger; vary the ending beat deliberately.

**Stop here for approval of the outline.**

## Phase 4.5: Character Creation Process (for AI-generated visual series)
For each named character, produce a two-step reference, generated once and reused for the whole season:
1. **Initial Portrait** — a full-body image on a neutral gray background, clear descriptive prompt (age, build, exact outfit, color palette, distinguishing features). This is the character's identity anchor.
2. **Character Sheet** — one 16:9 image combining: a face close-up, and full-body front, side, and back views, generated from the Initial Portrait as reference. This sheet is what every later scene generation references for that character — never re-prompt a character from text alone after this point; feed the saved sheet image back into the video tool as the reference.

Never use real, named, trademarked, or studio-owned characters (Marvel, DC, anime IP, etc.) as a design basis, even as "baby-sized" or "parody" versions — character design, proportions, color schemes, and insignia are protected regardless of scale or tone changes. Build original designs that evoke the same energy (e.g., a homemade, jugaad-style costume instead of a licensed superhero suit).

## Phase 4.6: Environment Reference Sheet
Before scripting, lock a reference image prompt for every recurring location the season uses (one prompt each, generated once, reused as the image/video reference for every scene set there). List them explicitly: e.g. "Village ground — kabaddi court," "Scorer's table," "Tea stall," "Antagonist's office." Note lighting/time-of-day variants only where the story requires them (day vs. evening versions of the same place), so continuity holds without re-describing the whole environment per episode.

## Phase 4.5: Character & Environment Creation Process (for AI-generated visuals)
Required before any image/video generation, not required for live-action.

**Characters — two-step process, once per character, before episode 1:**
1. Initial Portrait: one full-body image on a plain neutral background. Lock proportions, costume, key features in the prompt itself so it's reusable.
2. Character Sheet (16:9): face close-up + full-body front/side/back, same character, same style, same palette as the portrait.
Save both. Feed the saved Character Sheet back into the video tool as reference for every scene — never regenerate a character from text mid-series. Drift across episodes is the single most common AI-series continuity failure.

**Environments — same two-step discipline, once per recurring location:**
1. Establishing Shot: one wide image of the empty location, no characters, locking architecture/props/palette.
2. Location Sheet (16:9): the wide angle + one medium interaction angle + one key-prop close-up.

**Copyright check (mandatory):** No licensed, trademarked, or recognizable copyrighted characters — not reskinned, not "parody," not at reduced scale. If the user names an existing IP (a studio's characters, a franchise), decline that specific element and offer an original design with the same functional appeal (e.g. same proportions/archetype, new design) instead of silently complying or silently substituting without saying so.

**Continuity ledger extends to environments:** track which location each episode uses, not just which characters, so AI generation doesn't drift a location's layout or palette across the season.

## Phase 5: Scripts (batches of five)
Only after outline approval. Each episode:
- Targets 30 seconds (about 60–75 spoken words at natural pace, or fewer with visual-led scenes)
- Opens with a hook within the first 2–3 seconds
- Uses concise, natural dialogue
- Gives scene and sound direction
- Includes visual storytelling beats
- Ends with a dramatic beat
- Includes timestamps and an estimated spoken-word count

**When scripts are headed to AI image/video generation (not live-action):** keep visual descriptions simple and avoid staging current AI tools handle poorly — complex multi-character blocking, precise choreographed action, crowd scenes with individually readable people. Lean on elements that generate reliably instead: chat-bubble overlays, text/scoreboard overlays, phone-screen overlays, and single/double-character compositions. Reference locked Character Sheets and Location Sheets by name rather than re-describing appearance per episode — repeating full visual prompts in every episode both wastes tokens and reintroduces drift risk.

Deliver one batch, then wait for review before the next.

**AI-video accuracy constraint:** Do not write beats that depend on legible on-screen text, chat bubbles, phone/app UI, signage text, or any other rendered text — current video generation models cannot produce accurate text reliably. Convert any such beat into spoken dialogue, a described physical action, or an implied event instead (e.g., a character reading a message aloud rather than the audience reading it off a phone screen).

**Reference reuse, not per-episode prompts:** Do not write a new image/video generation prompt inside each episode script. Episodes reference the locked character sheets (Phase 4.5) and environment sheets (Phase 4.6) by name only (e.g., "at the Scorer's table, evening variant"). This keeps scripts lean and keeps the whole season visually consistent from one shared set of reference assets instead of twenty independently-drifting prompts.

## Phase 6: Continuity Review
Check each script against the bible, both timelines, character knowledge, established facts, and open mysteries. List contradictions with proposed fixes.

## Phase 7: Originality Review
Compare scripts against the reference transcripts at the level of characters, dialogue, plot events, and distinctive sequences. Flag matches. Replace flagged material with new material. Keep only generic genre conventions and abstract techniques.

**Limit:** this comparison is only as reliable as the transcripts actually provided in context. State which transcripts were checked.

## Phase 8: Final Output
Deliver as separate, versioned artifacts (v1, v2, ...):
1. Story bible
2. 20-episode timeline
3. All 20 scripts
4. Character continuity ledger
5. Episode dependency map
6. Production notes
7. Final quality-control report

## Rules
- Each phase gate requires explicit user approval before the next phase begins.
- Label uncertain claims about what transcripts contain. Do not assert a source feature without evidence in the provided text.
- Keep spoken dialogue short; visuals carry the rest in 30-second formats.
