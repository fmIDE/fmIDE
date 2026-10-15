---
name: fmide-development
description: Develop and document fmIDE using the demo file, Actions and Test tables, source XML, local docs and focused regression tests. Use for action-contract reviews, small native fixes, test records and release preparation.
---

Read [the development guide](../../../docs/development.md), then the relevant action docs, test records and implementation branch. Use the adjacent FileMaker-style and fmJAML skills when writing code.

Work in small batches: establish identity → backup → reproduce → minimal change → save/export/diff → native test → documentation/readback → checkpoint. Keep aliases, elongation precedence and chained navigation behavior intact.

Edit documentation in its source tables. Export Actions and Name that Thing parameters to the local docs; do not hand-edit generated pages. Native test records need complete metadata, test/endtest markers, stable expected results and cleanup. Verify the exact found set before running the harness.

Record only useful protocol facts: change, verification, known limitation, backup and issue. Distinguish local changes from commits, pushes and releases. Preserve unrelated work. Release tooling should prepare an explicitly identified copy, not clear the developer's live working state.

If UI editing is unavailable or a dispatch is unresolved, continue useful offline analysis without queuing more FileMaker work. Stop at the user's time, disk or usage limits. This skill does not authorize a release or a destructive operation beyond the current task.
