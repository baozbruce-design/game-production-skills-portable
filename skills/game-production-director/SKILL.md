---
name: game-production-director
description: Orchestrate an existing game project from request to verified delivery. Use when continuing a game across agents, planning phased implementation, reconciling requirements, coordinating code/art/audio/cinematics, validating builds, maintaining handoffs, or preparing work for Codex, Claude, or another coding agent.
---

# Game Production Director

Use this skill as the production layer above engine- and discipline-specific skills.

## Core behavior

1. Inspect the living project before proposing changes. Read the nearest `AGENTS.md`, current handoff/status file, authoritative requirements, backlog/priority file, and the exact code or asset files affected.
2. Separate **current implementation**, **target design**, and **historical documents**. Never claim a target spec is already implemented.
3. Obey explicit product priority before choosing the easiest task. A subsystem spec controls *how* to implement that subsystem; the product backlog controls *what to do next*.
4. Prefer the smallest coherent implementation that preserves existing saves, IDs, gameplay contracts, package identity, and unrelated user work.
5. Route specialist work through the smallest relevant game skill set: engine API + discipline + optional genre/workflow. Do not bulk-load unrelated skills.
6. For substantial changes, implement in phases with a concrete acceptance contract for each phase.

## Evidence hierarchy

Do not equate these levels:

- source inspection / static validation
- unit or simulation tests
- browser/editor runtime tests
- packaged-build validation
- emulator/device test
- human visual or listening acceptance

Report exactly which level was reached. Do not say "mobile verified" from a desktop viewport, or "audio sounds good" from file decoding alone.

## Change protocol

Before editing:

- identify authoritative files and version
- inspect relevant callers/tests
- preserve unrelated dirty changes
- locate secrets and signing assets but never copy them into source archives

During implementation:

- keep data models canonical and migration-safe
- centralize shared rules instead of patching repeated effects one by one
- use deterministic seeds for reproducible gameplay tests when randomness matters
- add regression tests for the behavior contract, not just syntax
- keep platform lifecycle handling explicit: pause/resume, background/foreground, page hide/show, audio/media cleanup

After implementation:

- run the narrowest useful tests first, then broaden based on risk
- validate packaged assets and hashes when shipping a build
- verify package/version/signature continuity when an update must install over an existing app
- record unresolved device, performance, balance, visual, or listening risks explicitly
- update the handoff/status document with changed files, commands, results, limitations, and the next concrete move

## Cross-agent handoff format

When work may move between ChatGPT, Codex, Claude, or another agent, leave a compact authoritative handoff with:

- objective
- current version/state
- authoritative documents and precedence
- completed work
- active work
- blocked or unverified items
- exact next step
- relevant files
- exact validation commands and latest outcomes

Do not rely on chat history alone for project continuity.

## Art and cinematic rules

- Keep a visual/character bible for recurring characters.
- Approve one canonical identity image before generating a family of assets or animation clips.
- Track generated media with source prompt/provider/model/job/seed when available, dimensions, duration, SHA-256, and runtime destination.
- Game-ready assets require import/runtime verification, not only attractive source images.
- When a cinematic can block play, always provide skip/error/timeout fallback and ensure continuation fires at most once.

## Audio rules

- Separate music, ambience, and SFX routing.
- Pause/resume audio with the actual game lifecycle and gameplay pause state.
- A decoded music file is not a listening acceptance test.
- Multiple tracks generated from one batch may serve the same scene family, but runtime mapping should be scene-purpose based rather than exposing internal A/B development labels to players.
- Preserve original masters; create runtime derivatives separately when trimming, normalizing, or looping.

## Mobile delivery rules

For mobile-oriented games, explicitly test or mark unverified:

- touch controls
- safe areas / notches
- portrait/landscape layout
- background/foreground lifecycle
- audio resume behavior
- long-session frame rate, memory, thermals, and battery
- update install and save continuity

## Completion standard

A task is complete only when the requested behavior exists, relevant tests pass, packaging/runtime integration is checked at the appropriate level, the handoff is updated, and remaining unverified risks are stated without exaggeration.
