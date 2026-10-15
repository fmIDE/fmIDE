# Developing fmIDE in the demo file

The open `fmIDE.fmp12` is the editable implementation and documentation database. The exploded XML is a review and recovery view. Editing an exploded text file does not update the native script.

## Find the source of truth

| Work | Source |
| --- | --- |
| Action implementation | Native `fmIDE` script |
| Parser and helpers | Installed custom functions, especially `fmJAML` |
| Action summaries/details | `fmIDE_Action`, shown on **fmIDE Actions** and **fmIDE Actions Wiki Docs** |
| Usage variants | `fmIDE_Action_Usage` and its related tests |
| Name that Thing parameters | `NameThatThingParameter`, shown on the API Parameters and API Wiki Docs layouts |
| Regression tests | `fmIDE_Test`, with complete source and expected results |
| Review source | `src/xml/fmIDE.xml` and `src/exploded/` |

## Small change cycle

1. Verify the local database path and FileMaker version. Read the relevant action branch, docs, neighboring tests and existing issue.
2. Save a copy through the [Save a Copy as action](actions/save-a-copy-as.md). Record its path, byte size and SHA-256 outside FileMaker.
3. Add a focused regression before changing behavior. Run it through the native test harness and retain the result.
4. Make the smallest native change. Keep [MrWatson formatting](mrwatson-style.md), ordered aliases/elongation and action chains. Add a concise `codex` step comment for agent-made native changes when requested.
5. Save, export fresh XML, and compare the intended steps. Confirm no unrelated scripts changed. Re-run the focused tests.
6. Update the Actions table or parameter table, regenerate documentation, and save a checkpoint backup.

Read-only analysis and documentation exports do not require a new database backup every time. Take one before meaningful mutations and after a verified batch. Monitor free disk space; keep large XML and backup snapshots out of Git unless deliberately included.

## Action contracts

Describe canonical name and aliases, alias-specific defaults, ordered shorthand expansion, placeholders taken from key names, literal/calculation parameters, defaults, action order, results and errors. Explain when expressions run.

Some families deliberately chain operations. Script navigation selects a starting step, searches from there, then applies a relative `+` end-step selection. That new `+` behavior excludes `%`; do not “fix” it as if the two options were interchangeable.

Shared preparation can reduce repetition while retaining the native dispatch chain. Refactor one representative family and compare behavior before claiming a script-size reduction. Comments and spacing are part of its readability.

## Write and run tests

Use [the fmIDEAS guide](fmjaml-fmideas.md) and [saved native cases](../tests/fmIDEAS/README.md). The test harness executes FileMaker code; a Python generator can construct fixtures but is not a replacement for native verification.

Create complete records with unique UUIDs and titles, initially inactive. Verify the intended file, layout and record before each write. Activate after successful readback. Place new records beside the existing family, then use the existing renumber script while checking that the UUID order remains unchanged.

Tests should clean up their own persistent keys, temporary files and globals. Keep fixture names unique. Record whether the run was focused or the entire suite; a stored pass is not proof that every parameter combination works.

## Refresh source and documentation

Run the existing source-export and explode commands documented in [source storage](../src/README.md). `src/xml/fmIDE.xml` has a stable location so tools can resolve it relative to the database. The companion manifest records provenance and a coarse database modification-time freshness signal; data writes can also change that time.

The exploder is Malte Bastian's compiled tool, called by the repository's Python helper. The full raw export remains local; Git tracks the selected source view. Consult raw native DDR `StepText` if the readable exploder omits an option such as a variable repetition. Save as XML can contain sensitive metadata: do not publish the raw XML indiscriminately.

Regenerate [action docs](actions/README.md) after editing database documentation:

```sh
python3 tools/export_wiki.py --fmp 26
```

Generated pages are replaced on export. Edit their database source instead of their Markdown output. Review generated diffs, local links and manifests before committing.

## Completion record

Keep a short protocol: change, native test result, remaining issue, backup path/hash and source checkpoint. Distinguish changed, tested, committed, pushed and released. Issue comments should report reproducible behavior and evidence, without treating a local fix as an already-published release.
