# fmIDE documentation

fmIDE connects FileMaker's native development environment with developer tools and AI. Name an object to navigate to it, or compose actions into an fmIDEAS script.

| Start here | Reference and development |
| --- | --- |
| [Install and check fmIDE](installation.md) | [185 action entries](actions/README.md) |
| [Name that Thing](name-that-thing.md) | [102 parameter entries](parameters/README.md) |
| [Write fmJAML and fmIDEAS](fmjaml-fmideas.md) | [MrWatson coding style](mrwatson-style.md) |
| [CLI, startup and recovery](cli-and-recovery.md) | [Develop in the demo file](development.md) |
| [AI Bridge macro building blocks](ai-bridge.md) | [Prepare a release candidate](release.md) |

Agents can use the repository skills in [`.agents/skills`](../.agents/skills/README.md). The [native test sources](../tests/fmIDEAS/README.md), [current source workflow](../src/README.md), [public API variables](fmIDE-public-api-variables.md) and [internal-variable notes](fmIDE-private-internal-variables.md) provide more detail.

Try the [Tests layout overlay tour](../examples/tests-overlay-tour/README.txt): a standalone fmIDEAS example with HTML speech bubbles and Back/Stop/Next controls, tested on macOS with MBS.

## Documentation from the database

Edit `fmIDE_Action::SummaryTextForListView`, Description and syntax/usage content through **fmIDE Actions**. Review its calculated Wiki content on **fmIDE Actions Wiki Docs**. The action exporter produces a summary index and one detail page per action, including stored examples and test results.

Edit Name that Thing documentation in `NameThatThingParameter`, through **fmIDE 'Name that Thing' API Parameters** and its Wiki Docs layout. Its exporter produces an index and individual parameter pages with active status, type, defaults and stored action mappings.

From this repository, with its local `fmIDE.fmp12` open in FileMaker 26:

```sh
python3 tools/export_wiki.py --fmp 26
python3 tools/export_parameters.py --fmp 26
```

Run these sequentially. Both use the installed fmIDE CLI and verify completion before replacing their owned generated folders. Python uses the standard library. Generation manifests record provenance; previous generated output is retained locally and ignored by Git.

Do not hand-edit generated pages: change their database source and export again. Reference entries include historical/proposed actions and parameters. Their support/state columns matter. Stored test passes describe specific examples, not every option. Older details and explicit gaps still need targeted review.

The 19 October 2026 merge reconciled the repository copies of [Define Macro](actions/fmide-define-macro.md) and [Get Macro](actions/fmide-get-macro.md) with the [current macro contract](fmjaml-fmideas.md#macro-definition-contract). These two pages carry explicit correction notices; their database documentation must be synchronized before the next export. The action manifest retains the original export provenance and records these repository corrections separately. The preserved source XML and exploded scripts are older snapshots; editing them would not change the native implementation.

## Existing wiki material

The local docs are the replacement entry point. [The migration map](wiki-migration.json) accounts for all 19 existing wiki pages. Core API and workflow pages now link here; background material and local images are preserved under `wiki/` with its historical status stated.

- [Integrations](wiki/integrations.md) and [Go to Thing integration scripts](wiki/go-to-thing.md)
- [Tables and layouts](wiki/tables-and-layouts.md), [deep linking](wiki/deep-linking.md), [Thingamajig URIs](wiki/thingamajig-uris.md) and [hiatus background](wiki/hiatus.md)
- [Keyboard cheatsheet](wiki/cheatsheet.md), [original naming conventions](wiki/naming-conventions.md) and [credits](wiki/credits.md)

The hosted wiki has not been deleted or changed. Review the local docs and generated diffs before switching its public entry point.
