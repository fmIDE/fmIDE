![fmIDE logo][fmIDE]

# fmIDE

**A FileMaker integrated development environment — for AI + U + Me.**

fmIDE connects FileMaker Pro's development environment to classic and agentic development workflows. Add the fmIDE script module to your solution files to open them up to external tools, documentation and AI agents.

Your tools and AI pair programmer can **show you things** in FileMaker and **act** in your solution, using two complementary APIs:

- **[Name that Thing][Name that Thing] (nouns):** name a script, field, layout or other development object to open it in the relevant FileMaker context.
- **[fmIDE Action Scripts (fmIDEAS)](docs/fmjaml-fmideas.md) (verbs):** build and run sequences of actions in readable fmJAML or JSON, including approved development tasks.

The **fmIDE demo file** includes documentation, examples, a test system and a Quicklink tool for constructing and running `fmp` URLs.

## Quick start

1. Get the [latest release][GitHub Releases] and follow the [installation and setup guide][Installation].
2. Explore the **fmIDE Examples** and **fmIDE Tests** layouts in the demo file.
3. Call fmIDE in your solution through an `fmp` URL or [fmIDE-CLI](https://github.com/fmIDE/fmIDE-CLI), targeting the FileMaker version and file you want to use.

Navigate straight to an object and continue in FileMaker's native development interface, or run an action script to automate a task.

## An action script in fmJAML

This example finds selected records in the demo file's **fmIDE Examples** layout, sorts them and goes to the last record and finally turns the number of found records.

```fmjaml
[+].Go to Layout = "fmIDE Examples"
[+].Enter Find Mode
[+].Set Field.fmIDE_Example::Select = 1
[+].Perform Find
[+].Perform Script = "Examples: Sort"
[+].Go to Record/Request/Page = "Last"
[+].Exit Script = == Get ( Found Count )
```

The layout and script names above are literal values.

```
`= ==` preserves a FileMaker calculation for evaluation when the action runs.
# See the [fmJAML and fmIDEAS guide](docs/fmjaml-fmideas.md) for syntax and evaluation rules.
```

## Documentation and support

- [Documentation home](docs/README.md), [action reference](docs/actions/README.md) and [Name that Thing parameter reference](docs/parameters/README.md)
- [Agent skills](.agents/skills/README.md), [AI Bridge macros](docs/ai-bridge.md) and [development guide](docs/development.md)
- [Source XML and exploded scripts](src/README.md) and [native regression tests](tests/fmIDEAS/README.md)
- [Optional macOS services](fmIDE-Services/README.md) and [existing wiki][Wiki]
- [fmIDE website](https://fmworkmate.com/fmide.html) and [issues](https://github.com/fmIDE/fmIDE/issues)

Action documentation is also available inside the demo file on **fmIDE Actions Wiki Docs**.

Created by [MrWatson][MrWatson]; first presented at the fmGuru Rome FileMaker Week Conference in October 2022.

## License

See [LICENSE](LICENSE).

[fmIDE]: docs/wiki/images/fmide.png
[GitHub Releases]: https://github.com/fmIDE/fmIDE/releases
[Wiki]: https://github.com/fmIDE/fmIDE/wiki
[Installation]: docs/installation.md
[Name that Thing]: docs/name-that-thing.md
[MrWatson]: http://www.mrwatson.de
