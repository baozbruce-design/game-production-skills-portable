---
name: game-cinematic-production
description: Produce consistent game cinematics and animated story clips from approved character references, with identity preservation, storyboard prompts, provider generation, media manifests, runtime integration, skip/fallback handling, and mobile-safe playback. Use for AI-generated game cutscenes, character skill animations, gallery clips, or story transitions.
---

# Game Cinematic Production

Use with `create-game-assets`, the project engine/runtime media skill, and a provider-specific video skill when available.

## Identity first

For recurring characters, establish one canonical source set before generation:

- approved character reference image(s)
- character bible: face, hair, outfit, proportions, signature equipment, palette, forbidden deviations
- creature/companion references when applicable
- target art style and framing rules

Do not generate a large animation family before identity is approved. Reuse the same identity source across actions.

## Shot design

For each clip, define:

- narrative purpose
- start pose/frame
- end pose/frame
- camera framing and movement
- character action in chronological order
- environment and lighting
- effect timing
- duration and orientation
- continuity requirements with previous/next clip
- what must not change

When a sequence is generated as multiple short clips, use the previous clip's final frame as the next clip's starting reference whenever the provider supports it.

## Mobile game defaults

When the game is portrait-first, prefer native portrait generation rather than cropping a landscape result unless the project explicitly wants otherwise. Keep faces, weapons, UI-safe action, and subtitles away from unsafe screen edges.

## Generation and provenance

For each source clip, preserve when available:

- provider/model
- prompt
- reference image hashes
- job ID
- seed
- native dimensions
- native FPS
- duration
- source file SHA-256

Keep raw provider output separate from edited runtime derivatives.

## Runtime finishing

Runtime derivatives may include:

- crop/resize
- codec conversion
- frame-rate normalization
- audio removal/replacement
- faststart / streaming optimization
- loop crossfade where appropriate
- subtitle timing metadata

Record derivative hashes and do not overwrite the source master.

## Playback contract

A cutscene must not be able to trap the player.

Implement:

- normal `ended` continuation
- explicit Skip
- load timeout fallback
- media error fallback
- background/foreground pause handling
- continuation that fires at most once
- stale callback/run/session rejection
- cleanup when scene/page is abandoned

For story rewards or progression, commit exactly once at the correct gameplay boundary. Gallery/replay mode must not grant rewards or mutate progression unless explicitly designed to do so.

## QA levels

Separate:

- visual source review
- media decode/probe
- browser/editor playback
- viewport/safe-area verification
- packaged asset verification
- physical device playback
- human approval of character consistency, motion quality, pacing, and continuity

Do not substitute file-level checks for visual approval.

## Handoff

Update the project handoff with clip purpose, runtime mapping, provider/job/seed metadata, hashes, playback behavior, verified QA level, and unresolved device/visual issues.
