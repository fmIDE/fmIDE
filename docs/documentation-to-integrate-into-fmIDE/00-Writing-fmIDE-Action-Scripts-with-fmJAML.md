# Writing fmIDE Action Scripts with fmJAML



> **fmIDE** automates the FileMaker development environment.
> **fmJAML** is the text format you write those automations in.
>
> ```fmjaml
> [+].Go to Layout = "fmIDE Actions"
> [+].Enter Find Mode
> [+].Set Field.fmIDE_Action::ActionName = == "==Set"
> [+].Perform Find
> ```

This section documents how to write **fmIDE Action Scripts** (fmIDEAS) using **fmJAML**
(*FileMaker JSON As a Markdown Language*).

fmJAML is a compact, line-based `path = value` DSL that compiles to JSON. fmIDE consumes an
array of JSON action objects. Writing that JSON by hand — with FileMaker's escaping rules on
top of JSON's — is miserable. fmJAML turns it back into text you can type, read and diff.

## Read in this order

| # | Document | What it covers |
|---|----------|----------------|
| 1 | [fmIDE Action Scripts](01-fmide-action-scripts.md) | What an action script *is*, how fmIDE receives and executes it, the parameter formats, the runtime variables |
| 2 | [fmJAML Syntax Reference](02-fmjaml-syntax-reference.md) | The complete fmJAML language: paths, arrays, path inheritance, value operators, heredocs, the Data Processing String |
| 3 | [Writing Action Scripts](03-writing-action-scripts.md) | **The main guide.** The two-layer evaluation model, action forms, control flow, variables, results, errors, frontmatter, macros, debugging, style |
| 4 | [Action Reference](04-action-reference.md) | Every action fmIDE implements, with its short form, parameters and examples |
| 5 | [Cookbook & Pitfalls](05-cookbook-and-pitfalls.md) | Ready-made recipes, plus the mistakes everybody makes once |

If you only read one page, read **[Writing Action Scripts](03-writing-action-scripts.md)** —
and in particular the section *The two evaluation layers*, which explains the single most
common source of `?` results.

## Versions this documentation describes

| Component | Version |
|-----------|---------|
| fmIDE | v0.63 (2026-07-20) |
| fmJAML | v0.31 (2026-07-10), embedded in the `fmIDE` script |
| FileMaker | 19.5.1 minimum; 21+ for native `[+]`/`[:]` (fmJAML emulates them below that) |

Sources used: the `fmIDE.fmp12` DDR, the fmIDE/fmJAML test suite (569 tests), and the
[fmJAML repository](https://github.com/fmIDE/fmJAML).

## Requirements & caveats

- fmIDE refuses to run unless the account has **[Full Access]** privileges (otherwise error `9`).
- fmIDE is developed and tested on **macOS**. Some actions work on Windows, some do not.
- Many of the best actions (`Press`, `Go to Script`, `Select Script Steps`, Script Workspace
  interaction, window control) require the **MBS plugin**.
- fmJAML's regex operators (`~…~`) require MBS; without it they are silently ignored.

## Links

- fmIDE: <https://github.com/fmIDE/fmIDE> · [Wiki](https://github.com/fmIDE/fmIDE/wiki)
- fmJAML: <https://github.com/fmIDE/fmJAML> · [Wiki](https://github.com/fmIDE/fmJAML/wiki)
- Issues: <https://github.com/fmIDE/fmIDE/issues>
