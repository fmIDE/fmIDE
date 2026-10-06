![fmIDE logo][fmIDE]

# fmIDE

**A FileMaker integrated development environment - for AI + U + Me.**

fmIDE integrates the FileMaker Pro Client development environment into your classic or agentic development workflows.

Add the fmIDE script to each of your FileMaker solution files and you open up your solution to external tools and AI agents.

- You can jump from external tools, from your documentation to things in your solution.
- You can write dynamic scripts and run them dynamically in your solution.

This **enables AI agents to work with you** in your solution:

- AI agents can **show** you anything in your solution.
- AI agents can **act** in your solution and guide you through your development tasks - like a pair programmer.

## What fmIDE gives you

- **fmIDE 'Name that Thing' API** — (nouns) - name something to jump in to FileMaker and open it in the relevant development context.
  - with **Optional fmIDE macOS services** — navigate deeper into the FileMaker dialogs
- **fmIDE Action Script/fmIDEAS API** - (verbs) - pass an fmIDE action script, written in fmJAML (or JSON), to fmIDE to runperform repeatable FileMaker development actions.

- **AI integration** — let an AI agent inspect a solution, navigate FileMaker, and perform approved development tasks through the same API.

The fmIDE demo file provides

- the fmIDE test system, which proves what fmIDE can do (and not)
- documentation and examples
- a quicklink tool to help construct and run fmp urls in the current FileMaker

## Quick start

1. Follow the [installation and setup guide][Installation].
2. Enjoy

## The basic workflow

When you need to inspect or change something in a FileMaker solution:

1. Identify the object by its FileMaker name.
2. Ask fmIDE to navigate to it or perform an action.
3. Continue in FileMaker's native development interface.

For example, your AI-agent, or an external tool can send an `fmp` URL that asks fmIDE to open a script or field by name. The FileMaker window is brought to the relevant context, so you can work with the object immediately.

Alternatively, use the new fmIDE command line tool to call the fmIDE script in the filemaker version and file of your choice. See the [fmIDE-CLI repo](https://github.com/fmIDE/fmIDE-CLI) for more.

fmIDE is designed to complement FileMaker's development tools. It does not replace Script Workspace, Manage Layouts, or Manage Database; it gets you to the right place faster and provides a consistent automation boundary around those tools.

## fmIDE Action Scripts in fmJAML

An fmIDE Action Script is a sequence of fmIDE actions, preferably written in fmJAML (or JSON), for example this fmJAML snippet shows selected examples in the examples layout of the fmIDE demo file, sorted by the `Examples: Sort` script:

```fmjaml
[+].Go to Layout = "fmIDE Examples"
[+].Enter Find Mode
[+].Set Field.fmIDE_Example::Select = == 1
[+].Perform Find
[+].Perform Script = "Examples: Sort"
[+].Go to Record/Request/Page = "First"
```

Notes:

- Values which are from a selection menu in FileMaker, such as a layout name or script name use direct values `= "«static value»"`
- Otherwise use the `= == «calculation»` form to pass a FileMaker calculation (using the `==` 'Quote' value operator).


- The **fmIDE Examples** layout contains working examples and is a good place to start experimenting. - The **fmIDE Tests** layout also contains hundreds of tests (in test suite `3 fmIDEAS`).

Use the action documentation in the **fmIDE Actions Wiki Docs** layout or in the [fmIDE Wiki][Wiki] for the supported actions, parameters, error handling, and JSON forms.

## Working with AI agents

fmIDE can act as a controlled bridge between an AI agent and a FileMaker solution. A useful pattern is:

1. Export the relevant FileMaker metadata with **Save a Copy as XML**.
2. Inspect the XML to identify current layouts, tables, fields, scripts, and relationships.
3. Generate a small fmIDEAS script for the requested action.
4. Send it to fmIDE through an `fmp` URL.
5. Check FileMaker's visible state and fmIDE's error variables before continuing.

This keeps the agent grounded in the current solution and makes each change explicit and reviewable. The project’s separate `fmIDE-AI-Bridge` workspace contains examples, logs, metadata snapshots, and notes from this workflow.

## macOS fmIDE-Services

The `fmIDE-Services` folder contains two optional macOS services:

- **Store Clipboard to Keyboard Buffer** stores clipboard text for later use.
- **Retype Keyboard Buffer** types that text into the active FileMaker dialog.

These services are useful when fmIDE can open a FileMaker development dialog but cannot operate the dialog's final controls. See [fmIDE-Services/README.md](fmIDE-Services/README.md) for installation and keyboard-shortcut setup.

## Documentation and support

- [fmIDE Wiki][Wiki]
- [Installation and setup][Installation]
- [Name that Thing API][Name that Thing]
- [Latest releases][GitHub Releases]
- [fmIDE-Services guide](fmIDE-Services/README.md)

fmIDE was created by [FileMaker developers at MrWatson.de][MrWatson]. It was first presented at the fmGuru Rome FileMaker Week Conference in October 2022.

## License

fmIDE is distributed under the terms in [LICENSE](LICENSE).

[fmIDE]: https://github.com/fmIDE/fmIDE/wiki/images/fmide.png
[GitHub Releases]: https://github.com/fmIDE/fmIDE/releases
[Wiki]: https://github.com/fmIDE/fmIDE/wiki
[Installation]: https://github.com/fmIDE/fmIDE/wiki/About-fmIDE-Installation-and-Setup
[Name that Thing]: https://github.com/fmIDE/fmIDE/wiki/fmIDE-'Name-that-Thing'-API
[MrWatson]: http://www.mrwatson.de
