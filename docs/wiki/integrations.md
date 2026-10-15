> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.

![fmIDE Integrations](images/fmide-integrations-256.png)

fmIDE integrates your FileMaker solutions with the tools you use in your developer environment.

This page lists tools which integrate with fmIDE (via the [fmIDE 'Name that Thing' API](../name-that-thing.md)).

Some of the tools use an [`fmIDE-Go to Thing` Script](go-to-thing.md).



## BaseElements (unofficial integration script)

![BaseElements Logo](https://baseelements.com/wp-content/uploads/2016/05/logo_BaseElements.png)

[BaseElements](https://baseelements.com/) is a FileMaker Analysis tool from [Goya](https://goya.com.au/) in Australia

MrWatson is in the process of writing an unofficial [integration script for BaseElements](https://github.com/fmIDE/Script-fmIDE-Go-to-Thing-from-BaseElements), which can jump from the record you are viewing in BaseElements to that thing in FileMaker.  (More information coming very soon)


## CrossCheck™ (unofficial integration script)

![CrossCheck™ Logo](http://www.fm-crosscheck.com/Home_files/CrossCheck_Logo.jpg)

[CrossCheck™](http://www.fm-crosscheck.com/Home.html) is a FileMaker Analysis tool from [[x] Cross Solution](http://www.fm-crosscheck.com/About_Us.html) in Germany

MrWatson has written an unofficial [integration script for CrossCheck™](https://github.com/fmIDE/Script-fmIDE-Go-to-Thing-from-CrossCheck), which can jump from the record you are viewing in CrossCheck to that thing in FileMaker.  (More information coming very soon)


## MrWatson's tools

fmIDE works well together with [MrWatson's tools](http://mrwatson.de).


![fmWorkMate Logo](https://raw.githubusercontent.com/mrwatson-de/fmWorkMate/master/docs/img/fmWorkMate_ICON_200x200_sm.png)
### fmWorkMate

[fmWorkMate](https://fmWorkMate.com) is a toolbox of FileMaker power tools.

fmIDE is integrated into several of fmWorkMate's tools.

Read on.

Download the [latest release of fmWorkMate from GitHub](https://github.com/mrwatson-de/fmWorkMate/releases/)

### fmCheckMate

fmCheckMate, part of [fmWorkMate](#fmworkmate), converts the FileMaker clipboard to XML, and lets you edit it, analyse it, change it, transform it.

- Once you have copied scripts (or other stuff) and converted them to XML, …
- …or if you 'print' the copied script and view it in the text viewer, …
- …select `fmIDE: Go to Thing` or press ⇧⌘M to jump to the thing that is in focus under the cursor.

### fmLogAnalyser

fmLogAnalyser, part of [fmWorkMate](#fmworkmate), analyses FileMaker's import.log to help you find errors you introduce while coding / pasting code.

- When viewing a line in your import log, …
- …select `fmIDE: Go to Thing` or press ⇧⌘M to jump to the thing.

Note: 2022-10-08 Work in progress: fmLogAnalyser needs further work to extract some error details out of the script line.

### fmAutoMate

fmAutoMate is an extension to your FileMaker IDE, which provides

- a context menu in the script workspace
- extension services to the context menu in the calculation editor and access to hot


- fmAutoMate HotKeys
  - fmAutomate has some useful functions to jump between windows when you have tools open in thew same FileMaker as your FileMaker solution databases and all the windows are mixed up:
    - Press ⇧⌃W to open a window switcher
    - Press ⇧⌃⌥W to switch to the previous window

- fmAutoMate Services
  - With fmAutoMate Services you can open fmp urls on websites


fmAutoMate is a separate tool to [fmWorkMate](#fmworkmate). Download the [latest release of fmAutoMate from GitHub](https://github.com/mrwatson-de/fmAutoMate/releases/)
