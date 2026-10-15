---
name: filemaker-mrwatson-style
description: Write or review native FileMaker scripts, calculations and custom functions in MrWatson style. Use for fmIDE implementation and formatting work, especially Let, Case, While, JSON construction and custom-function contracts.
---

Read [the coding style guide](../../../docs/mrwatson-style.md) before editing a substantial calculation. This skill belongs to the fmIDE repository; keep the repository alongside it.

Preserve local conventions and public signatures. Expose the operation's stages with useful comments and spacing. Use leading semicolons in multi-entry JSONSetElement calculations. Keep calculation-local variables distinct from script locals and globals; evaluate side-effecting expressions once.

Read the actual native source before assuming a parameter name or expansion rule. Keep aliases, ordered elongation, defaults and action chains explicit. Preserve unrelated code and formatting.

For native changes, follow the authorized task's backup and verification requirements. Verify the saved XML diff and focused native tests. An edit to exploded source is not a native FileMaker edit. Do not broaden authorization or change unrelated scripts because this skill is active.
