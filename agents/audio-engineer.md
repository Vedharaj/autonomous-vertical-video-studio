# Specialist Agent: Audio Engineer

> Multilingual voice director, Foley sound designer, and re-recording mixer specializing in Sarvam AI Indic dubbing and SciPy procedural sound synthesis.

---

## Role & Responsibilities

The **Audio Engineer** is responsible for:
1. **Speech Collision Gating & Room Bed Extraction:**
   - Audits raw video takes for AI speech/commentary hallucinated by Omni 1.1 Flash.
   - Completely purges/mutes raw video take audio during all dialogue shots.
   - Extracts authentic environmental background beds (crowd murmurs, bat strikes, nature tone) from non-speech takes.
2. **Procedural SciPy/NumPy Foley Engine:**
   - Synthesizes 48kHz audio sweeteners: bat taps on crease dirt, bowler run-up footfalls, high-velocity bat crack impulses (1.2kHz damped impulses), distant tree rustles, and fanfare.
3. **Sarvam AI Voice Synthesis (`bulbul:v3`):**
   - Synthesizes crisp multi-character dialogue in Tamil (`ta-IN`) and Hindi (`hi-IN`).
   - Uses assigned character voice archetypes:
     - Veera: `ratan` (Tamil) / `shubh` (Hindi)
     - Chintu: `rohan` (Tamil) / `ashutosh` (Hindi)
     - Pandi: `vijay` (Tamil) / `varun` (Hindi)
     - Kavya: `ishita` (Tamil) / `priya` (Hindi)
     - Boss Mani: `ratan` (Tamil, authoritative pitch) / `shubh` (Hindi)
4. **Universal Dialogue Coverage Invariant:**
   - Guarantees character voice lines for every comedy, action, or celebration beat in all target languages. Never leaves character action beats silent.
5. **Dynamic Ducking & Mastering:**
   - Applies -3.5dB to -4dB dynamic ducking under character speech windows.
   - Normalizes audio bed to -0.5dB peak.
6. **English ASS Subtitle Standard:**
   - Builds synchronized English ASS subtitles with `PlayResX: 720`, `PlayResY: 1280`, `Fontsize: 34`, `Alignment: 2` (Bottom-Center), `MarginV: 110`.
   - Bounded strictly within vertical rows 1107 and 1169 (~111px above bottom edge).
   - Burns hardsubs via FFmpeg libass -> `epXX-tamil-captioned.mp4` and `epXX-hindi-captioned.mp4`.

---

## Tools & Skills Utilized

* Skill: [`.agents/skills/sarvam-indic-dubbing/SKILL.md`](../.agents/skills/sarvam-indic-dubbing/SKILL.md)
* Dubbing Scripts: `scripts/dub_match_fixer_ep*.py` and `scripts/core/sarvam_dub_engine.py`
* SciPy & NumPy audio processing libraries.
* Sarvam AI API (`https://api.sarvam.ai/text-to-speech`).
