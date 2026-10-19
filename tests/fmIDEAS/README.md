# Native fmIDEAS regression tests

These are the action scripts and complete record fixtures for 61 tests added to `fmIDE_Test` on 14 October 2026. The macro fixtures were revised in the repository on 18 October for the `macro_name` / `metadata` / `script` contract and await a native run. The database is the test runner; the `.fmIDEAS` files make the cases readable and recoverable in Git.

| Group | Cases | Last verified result |
| --- | ---: | --- |
| File-path contract | 6 | 6 pass, 0 fail, 0 skipped; local fix for [#210](https://github.com/fmIDE/fmIDE/issues/210) |
| Macro handling | 39 | Revised contract: native run pending; previous contract had 39 passes |
| Script-step search | 4 | 4 pass, 0 fail, 0 skipped; local fix for [#179](https://github.com/fmIDE/fmIDE/issues/179) |
| Persistent data | 7 | 7 pass, 0 fail, 0 skipped; no fixture instances remain |
| Exit Script output | 5 | 5 pass, 0 fail, 0 skipped; local fix for [#204](https://github.com/fmIDE/fmIDE/issues/204) |

The macro group covers names, short/long forms, targets, metadata, missing resources, error capture, frontmatter and exactly-once evaluation. It requires FileMaker 26. Test fixtures use the `fmIDE_Test.MacroRegression` name prefix.

Macro definitions now use `.script`; returned objects and expected results use `macro_name`, optional `metadata`, and `script`. Test UUIDs and sort order are unchanged. The revised record fixtures have their old run results cleared; `manifest.json` retains the previous verification separately. Require a build implementing the renamed contract, then update the matching native records from these fixtures before running the wrapper. Pulling the repository does not update those database records. No native FileMaker changes or native reruns were performed for this revision.

The search group requires macOS and MBS. It opens the existing **Tests: Reset global Test fields** script and reads selection/search state; it does not modify or execute that script. The unique **Reset Result fields** comment is expected at step 21. If that fixture script changes, review this assumption before changing an assertion. The cases verified the local fix for #179: the step-search calculation wrapper is recognized independently of the script-list search.

The persistent-data group requires FileMaker 26. Each case allocates a UUID instance in the fixed `fmIDE` store, checks for collision, captures the result, and deletes only that instance if it still exists. It covers runtime evaluation once per parameter, Unicode/multiline text, zero, empty text, replacement, explicit deletion and scalar Configure deletion. The complete persistent-ID list was unchanged after the run.

The Exit Script output group calls fmIDE synchronously and checks result preservation and one-time evaluation. File cases read back all expected response files, close their own file IDs and delete their UUID temporary files. Counter globals are restored; empty temporary folders are left for operating-system cleanup.

The file-path group covers all six renamed actions: canonical and legacy keys, precedence, one evaluation, and observed filesystem results. Get File Exists also checks an explicitly empty canonical path. Recovery uses isolated temporary folders and deletes its source and recovered databases; small recovery logs and empty folders remain for OS cleanup. These tests require fmIDE v0.95 with #210.

## Run in the fmIDE test file

For offline repository checks, run `python3 -B -m unittest discover -s tests -v` from the repository root. These checks verify the `.fmIDEAS` file inventory against all 61 manifest entries and record snapshots, and validate the macro installer and `macro_name` / `metadata` / `script` fixtures. They do not execute FileMaker or establish native test passes.

Open this repository's `fmIDE.fmp12` in FileMaker 26, then run from the repository root:

```sh
fmide -fmp 26 -file fmIDE --parameter-file tests/fmIDEAS/run-macro-regression.fmIDEAS
fmide -fmp 26 -file fmIDE --parameter-file tests/fmIDEAS/run-script-search-regression.fmIDEAS
fmide -fmp 26 -file fmIDE --parameter-file tests/fmIDEAS/run-persistent-data-regression.fmIDEAS
fmide -fmp 26 -file fmIDE --parameter-file tests/fmIDEAS/run-exit-output-regression.fmIDEAS
python3 tools/fmide_run.py tests/fmIDEAS/run-file-path-regression.fmIDEAS \
  --fmp 26 --file fmIDE --database-path "$PWD/fmIDE.fmp12"
```

Run one group at a time and close its result card before starting another. Each wrapper finds the saved records, checks the expected count and exact UUID membership, sorts them and calls **Tests: Run Found Tests automatically**—the same runner used by **Run THESE Tests**. Inspect the result card; successful CLI dispatch alone does not establish that the tests passed. GUI tests need an unlocked interactive session.

Each test uses `#@test` / `#@endtest` to identify code under test. The native framework supplies context, resets global test fields, evaluates pre/post calculations and stores results. `records.json` preserves expected values and the record metadata; it is a snapshot, not an automatic import. The wrappers require those records already to exist and stop if the set differs.

Refresh these source snapshots when editing their database records. Recorded results in `manifest.json` describe the last verified run, not the outcome on another installation; null results mean the revised fixture has not been run. Times copied from the database use Europe/Berlin.
