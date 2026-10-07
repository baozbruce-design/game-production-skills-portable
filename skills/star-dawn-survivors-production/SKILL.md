---
name: star-dawn-survivors-production
description: Continue the user's Star Dawn Survivors project safely across ChatGPT, Codex, Claude, or OpenChatX. Use only for the Star Dawn Survivors project to preserve its authoritative docs, one-engine combat contract, web/mobile/Godot boundaries, product backlog order, save compatibility, media pipeline, and handoff discipline.
---

# Star Dawn Survivors Production Overlay

Use together with `game-production-director` and the relevant engine/discipline skills.

## Identify the project

Canonical project name: **Star Dawn Survivors / 星之破曉**.

Before changes, locate and read the project's current:

- `AGENTS.md`
- `CODEX_HANDOFF.md`
- `docs/PRODUCT_PRIORITY_BACKLOG_*.md` when present
- subsystem requirement file named by AGENTS for the requested feature
- affected runtime source and tests

Treat older planning copies and historical specs as historical unless the current AGENTS/handoff explicitly reactivates them.

## Gameplay invariants

- There is one real-time survivor combat engine. Story battles, bosses, chases, pacification, scripted losses, solo/duo encounters, and endless mode configure that same combat engine rather than creating a separate tactical/turn-based battle engine.
- Camp is a management/progression screen, not an alternate combat system.
- Preserve non-lethal story outcomes where current canon specifies taming, calming, pacification, or understanding.
- Permanent profile progression and temporary run progression must remain separate.
- Do not claim target skill-system design is implemented merely because the requirements document exists.

## Current runtime boundaries

The project can contain multiple delivery surfaces with different maturity levels:

- HTML5/web runtime may be ahead of Godot.
- Android packages may wrap a tested web source snapshot.
- Godot source may still be a smaller/older implementation.

State which surface you changed and validated. Never imply parity unless verified.

## Product priority

When a current product-priority backlog exists, execute new feature work in that order unless the user explicitly changes it. A specialized requirement document governs implementation details inside its subsystem but does not silently reorder the product backlog.

## Save and identity safety

Preserve unless explicitly migrated:

- skill IDs and recipe IDs
- Profile/Journal keys
- rank/SP semantics
- Android package name and signing continuity for update installs
- canonical story/canon identifiers

Migrations must be explicit, testable, and safe for existing permanent progress.

## Story and source material

External story projects used as reference are read-only unless the user separately authorizes edits. Copy approved assets into this project's managed asset directories; do not create runtime dependencies on another local project path.

## Media production

### Music

- Map tracks to scene purpose such as title, camp, forest battle, boss, or emotional story beat.
- Internal generation variants may be retained, but player-facing naming should be scene/track based rather than development A/B terminology.
- Keep original music masters and runtime derivatives separate.
- Verify decode, duration, hash, runtime loading, pause/resume, and actual listening separately.

### Cinematics

- Reuse canonical character identity references and the current character bible.
- Mobile story/cinematic output should respect the project's current orientation and safe-area requirements.
- Cutscenes must have skip/error/timeout fallback and must not double-complete rewards or story state.
- Gallery playback must not grant gameplay rewards.

## Android delivery

For an update APK:

- increment versionCode/versionName appropriately
- preserve package and signer if update-install continuity is required
- verify packaged asset hashes
- verify zip alignment/signature where applicable
- keep secrets/keystore material out of source archives
- distinguish desktop/browser simulation from physical Android testing

When the project has a retention rule for old APK/source packages, obey the newest rule in AGENTS/handoff before deleting anything.

## Required handoff update

After each meaningful phase, update `CODEX_HANDOFF.md` with:

- version/state
- behavior changed
- files changed
- tests/commands and results
- package/hash/signature evidence when relevant
- exactly what was not tested
- next concrete step

This handoff is the primary cross-agent continuity surface.
