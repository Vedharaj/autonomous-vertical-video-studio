# Troubleshooting & Pitfall Avoidance Bible

> Battle-tested failure modes, root causes, permanent fixes, and prevention checklists identified during the production of *Match Fixers* Episodes 1 through 4.

---

## 1. Gemini Reference Frame Split-Screen & Multi-Panel Hallucinations

* **Symptom:** In Episode 4 Shot 4, Gemini generated an image with a vertical split line, duplicate pitch wickets, or comic book panels instead of a single cinematic cricket ground.
* **Root Cause:** Demanding complex foreground action (batsman swinging at crease) and distant background action (outfielders in chairs + ball soaring over banyan tree) simultaneously forces diffusion models to composite multiple sub-scenes into collage grids.
* **Fix & Prevention:**
  1. Enforce a **single unified camera perspective** (e.g. low-angle looking up from behind the batsman towards the sky).
  2. Always include strict negative prompt constraints:
     `"Single unified composition, absolutely NO split screen, NO multi-panel collage, NO duplicated characters, NO motion trail lines, NO text."`
  3. Never prompt multiple separate spatial planes with detailed micro-actions in a single reference frame.

---

## 2. Google Flow Downloading Wrong Video Takes

* **Symptom:** In Episode 4 Shot 4, clicking the asset grid downloaded a previously generated scene take (`Boy_standing_at_batting_crease...` instead of `Chintu_watching_ball_hit_boundary...`).
* **Root Cause:** Google Flow's asset grid dynamically sorts tiles as renders complete or reload. Clicking by approximate CSS class or tile index can open an adjacent take.
* **Fix & Prevention:**
  1. **Verified Take Retrieval Gate:** After opening a take in the Flow editor (`/edit/<id>`), ALWAYS inspect the header (`h1` or `.header-title`) to confirm the title text matches the intended shot.
  2. Check downloaded file size (`> 1.0MB`) and duration via `ffprobe` before overwriting episode asset files.
  3. Never automate the download click without verifying the DOM header.

---

## 3. Out-of-Sequence Publishing Queue Enrollment

* **Symptom:** Enrolling Episode 4 into the SMM Google Sheets queue before Episode 3 causes YouTube's automated cron job to publish Episode 4 first, completely ruining narrative serial continuity.
* **Root Cause:** The publishing dispatcher script reads Google Sheets rows top-to-bottom in order of appearance.
* **Fix & Prevention:**
  1. **Sequential Publishing Order Invariant:** Before enrolling Episode $N$, inspect existing rows via `smm queue list "<channel>"`.
  2. Verify that all predecessor episodes ($1 \dots N-1$) are already present in the queue with status `COMPLETE` or `READY`.
  3. If any preceding episode is missing, enroll it first in strict numerical sequence.

---

## 4. Silent Character Action Beats Lacking Dubbed Dialogue

* **Symptom:** In Episode 4 Shot 6, Pandi hoisted Chintu's arm in victory, but the shot had no character dialogue in Tamil or Hindi, leaving the comedic punchline flat.
* **Root Cause:** When script outlines describe physical actions without explicit spoken lines in quotes, voiceover synthesis was omitted.
* **Fix & Prevention:**
  1. **Universal Dialogue Coverage Invariant:** Every visual shot featuring interacting characters, comedy beats, celebrations, or reactions must include dubbed dialogue across all target languages.
  2. Even for non-verbal reactions (referee arm hoists, crowd gasps, confused stares), script punchy character dialogue (e.g. Pandi: *"Here is our new champion Chintu! Sixer King da!"*).
  3. Always synchronize matching bottom-center English ASS subtitles for every spoken line.

---

## 5. Raw AI Speech Collision & Double Voices

* **Symptom:** Google Flow's Omni 1.1 Flash video engine occasionally hallucinates background English sports commentary or mumbling voices, which clashes discordantly with Sarvam Indic dubbing.
* **Root Cause:** Omni 1.1 Flash synthesizes audio and video jointly.
* **Fix & Prevention:**
  1. **Speech Collision Gating:** In any shot where character dialogue plays, completely purge/mute the raw take audio track.
  2. Only preserve environmental ambiance (wind, ball strikes, nature tone) from takes where characters do not speak.
  3. Apply smooth -3.5dB to -4dB dynamic ducking under dialogue windows so the vocal track remains crisp and clear.

---

## 6. Sarvam Synchronous STT 400 Error (> 30s Limit)

* **Symptom:** Running audio QA via Sarvam's synchronous STT API (`saaras:v3`) failed with:
  `STT failed: 400 Audio duration exceeds the maximum limit of 30 seconds`.
* **Root Cause:** The `saaras:v3` synchronous endpoint has a hard 30.0-second input limit.
* **Fix & Prevention:**
  1. Slice a representative 25.0s dialogue segment using FFmpeg:
     `ffmpeg -y -i master.wav -t 25.0 -c copy sample_25s.wav`
  2. Send the 25.0s slice to the STT API for transcription verification.

---

## 7. Signed CDN Video URL Fetch Failures (`TypeError: Failed to fetch`)

* **Symptom:** Attempting to download Flow video assets using `fetch(signed_url)` inside the browser page context failed with CORS / network exceptions.
* **Root Cause:** Flow's signed CDN URLs (`flow-content.google/video/...`) require internal session authentication cookies and disallow client-side cross-origin fetch calls.
* **Fix & Prevention:**
  1. Use the native Flow UI download menu: click `Download media` -> `720p Original size`.
  2. Alternatively, download using `curl -s -L "<signed_url>" -o take.mp4` outside the browser sandbox if cookies are not required for that signature.

---

## 8. Global vs Project-Local Skill Pollution (The Core Architectural Mistake)

* **Symptom:** Production skills (`google-flow-production`, `sarvam-indic-dubbing`, `short-form-series-production`) were placed in `~/.gemini/antigravity-cli/skills/`, leaking project-specific details into unrelated workspaces and creating machine-level drift.
* **Root Cause:** Developers or agents defaulted to the global user skill directory rather than isolating customizations inside the workspace.
* **Fix & Prevention:**
  1. **Local by Default Rule:** Keep all project-specific skills in `<project>/.agents/skills/` or `<project>/skills/`.
  2. AGI CLI discovers `.agents/skills/` automatically by traversing up from the working directory to the repository root.
  3. Global directories (`~/.gemini/...`) are reserved strictly for machine-wide, project-agnostic utilities (e.g. `playwriter`, `linux-disk-cleanup`).
