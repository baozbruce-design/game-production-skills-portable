---
name: game-music-production
description: Produce, integrate, and validate game music for an existing project, including AI-generated tracks such as Suno, scene-based mapping, variant handling, looping, metadata, hashes, runtime lifecycle, and listening QA. Use when creating or replacing game OST, assigning tracks to scenes, importing downloaded songs, or debugging music playback.
---

# Game Music Production

Use with `audio-design` plus the detected engine/runtime audio skill.

## Production workflow

1. Read the current game state, scene list, music registry, and handoff before generating anything.
2. Define the **scene purpose** first: title, camp, exploration, forest battle, boss, emotional story beat, victory, defeat, etc.
3. Write a concise musical brief containing mood, energy curve, instrumentation, BPM range when relevant, motif continuity, loop needs, and whether vocals are prohibited.
4. Reuse an existing track when it already fits. Do not spend generation quota just to create superficial variation.
5. When a provider returns multiple songs in one generation, retain useful siblings as alternate tracks for the same scene family or related scenes.
6. Download the real source file and preserve it unchanged as a master.

## Import record

For every imported track, record when available:

- provider and model
- song/job ID
- generation prompt/brief
- source filename
- duration
- sample rate / codec
- SHA-256
- intended scene(s)
- runtime derivative filename, if any

Do not expose internal generation labels such as `A/B` to players unless they are intentional artistic names.

## Runtime integration

- Route music independently from SFX.
- Keep scene-to-track mapping data-driven.
- Avoid changing tracks in the middle of a scene merely because random selection runs again.
- For same-scene alternates, avoid immediate repetition when practical.
- Respect user mute/volume settings.
- Pause for gameplay pause where appropriate.
- Pause on background/hidden lifecycle events and resume only if the scene/game state is still eligible.
- Dispose old players/listeners when leaving a scene to avoid overlapping music or leaks.
- If a browser/mobile runtime needs a user gesture to unlock audio, wire one shared unlock path rather than duplicate hacks.

## Loop preparation

A full song is not automatically a good loop.

When looping matters:

1. audition intro and tail
2. decide whether to loop the whole master or create a derivative
3. trim/crossfade only in the runtime derivative
4. preserve the untouched original
5. validate duration/codec after processing
6. perform an actual listening check of the seam

Do not claim a loop is seamless based only on ffmpeg decode success.

## Validation layers

Treat these as separate checks:

- file exists and hash matches
- codec/metadata probe passes
- full decode passes
- runtime request/load succeeds
- play/pause/volume/lifecycle behavior works
- player/device output is audible
- human listening confirms level, mood, transitions, and loop seam

Report the highest layer actually completed.

## Generation-budget discipline

When using a limited daily AI-music quota:

- plan multiple scene briefs before generating
- prefer batches that can supply two related usable tracks
- never click Generate/Create repeatedly because the browser looks stale; check the provider library/history first
- preserve provider IDs so tracks can be recovered later

## Handoff

Update the project handoff with imported files, IDs, hashes, scene mapping, validation results, unresolved listening/device QA, and the next intended music scene.
