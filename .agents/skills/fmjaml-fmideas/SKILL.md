---
name: fmjaml-fmideas
description: Construct, run and verify fmJAML fmIDE Action Scripts through fmIDE-CLI. Use for FileMaker navigation, inspection, record operations, backups, tests, macros and output files; includes evaluation timing and stalled-run recovery.
---

Read [fmJAML and fmIDEAS](../../../docs/fmjaml-fmideas.md) and [CLI and recovery](../../../docs/cli-and-recovery.md). Consult the relevant [generated action page](../../../docs/actions/README.md) and a working native test before using unfamiliar syntax.

Format every fmIDEAS script written in fmJAML to look as much like native FileMaker statements as possible, including generated scripts, macros, tests and documentation examples:

- Indent the bodies of block statements such as `If` and `Loop`; align `Else If`, `Else` and closing actions with their opening action.
- Put indentation **after** the array-path prefix (`[+].` or `[:].`), **before** the action name or `.parameter_name`.
- Use exactly **two spaces per indentation level**, never tabs, so alignment and recognition do not depend on tab stops.

See the [formatting example](../../../docs/fmjaml-fmideas.md#format-like-filemaker-statements).

1. Establish host, CLI version, FileMaker version, database path and required capability. Do not infer the target from the frontmost window.
2. Separate construction-time evaluation from action-time evaluation. Preserve runtime calculations with `= ==` or raw here-text; use quoted here-text for literal strings without manual escaping.
3. Use named lower_snake_case frontmatter parameters. Return structured results with a runtime JSONSetElement calculation. Do not invent runtime structured-leaf evaluation.
4. Guard mutations by file, layout/table and record UUID; back up at key checkpoints. Capture errors immediately and preserve them through cleanup.
5. Dispatch once into a unique response folder. Wait for all five files, check errors, identity and promised result shape, and read back mutations.
6. On timeout, inspect late files and application state before any new call. Never queue retries, bypass a locked session or silently change security settings.

Before using `Press` on macOS, verify that the executing FileMaker application has Accessibility permission in System Settings → Privacy & Security → Accessibility. Permission belongs to the application, so check the intended FileMaker version. Obtain user authorization before enabling it unless already approved in the session; do not treat missing permission as a timing defect. See [keyboard automation setup](../../../docs/cli-and-recovery.md#keyboard-automation-prerequisite).

Use Python for serialization and orchestration; run FileMaker semantics in FileMaker. Use available native UI controls only within the user's authorized scope. Treat Suite 5 as a mixture of examples and unfinished experiments. Do not test unreliable Press-based script editing on production scripts.

This skill grants no permission to publish, send messages, change privileges or perform destructive cleanup. Follow the active user's scope.
