> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.

This fmIDE cheatsheet lists useful stuff to get things done quicker within the FileMaker Developer Environment (GUI)

In development. (Please help!)

# FileMaker Pro

See the [Useful Links](#useful-links) at the bottom of this page

## General
| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| **Mac**
| Mac | editible Lists | <kbd><kbd>⌃</kbd><kbd>↑</kbd></kbd> / <kbd><kbd>⌃</kbd><kbd>↓</kbd></kbd> | Move selected element(s) in list <sup><a href="#fn-1" id="fnref-1">1</a></sup> |
||
| **Mac + MBS**
| Mac + MBS | Most List Dialogs | <kbd><kbd>⌘</kbd><kbd>C</kbd></kbd>	| Copy content. |
| Mac + MBS | Most List Dialogs | <kbd><kbd>⌘</kbd><kbd>F</kbd></kbd>    | Find in list |
| Mac + MBS | Most List Dialogs | <kbd><kbd>⌘</kbd><kbd>G</kbd></kbd>    | Find again in list |
| Mac + MBS | Most List Dialogs | <kbd><kbd>⇧</kbd><kbd>⌘</kbd><kbd>G</kbd></kbd>   |  Find again backwards in list |
| Mac + MBS | Most List Dialogs | <kbd><kbd>⌘</kbd><kbd>+</kbd></kbd>	| Zoom in. |
| Mac + MBS | Most List Dialogs | <kbd><kbd>⌘</kbd><kbd>-</kbd></kbd>	| Zoom out. |
| Mac + MBS | Most List Dialogs | <kbd><kbd>⌘</kbd><kbd>=</kbd></kbd>	| Zoom to 100%. |
| Mac + MBS | Most List Dialogs | <kbd><samp>Right-click</samp></kbd> | Show MBS Context Menu |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>⌥</kbd><kbd>C</kbd></kbd>	| copies styled text. |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>]</kbd></kbd>	| shift text to right. |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>[</kbd></kbd>	| shift text to left. |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>F</kbd></kbd>	| shows find bar. |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>G</kbd></kbd>	| goes to next found text. |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>R</kbd></kbd>	| shows rulers. |
| Mac + MBS | Text Area | <kbd><kbd>⌘</kbd><kbd>I</kbd></kbd>	| shows invisible characters |
||
| **fmAutoMate + Mac + MBS**
| fmAutoMate + Mac + MBS | fmAutoMate HotKeys ON | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>K</kbd></kbd> | Open fmAutoMate´s Extended HotKeys dialog |
| fmAutoMate + Mac + MBS | Most Dialogs + Workspaces | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>X</kbd></kbd> | Xut - Cut as XML |
| fmAutoMate + Mac + MBS | Most Dialogs + Workspaces | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>C</kbd></kbd> | Xopy - Xopy as XML |
| fmAutoMate + Mac + MBS | Most Dialogs + Workspaces | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>V</kbd></kbd> | PaXte - Paste XML |


<sup><a href="#fnref-1" id="fn-1">1</a></sup> Note: You may have to turn off the OS Mission Control shortcuts which clash with <kbd><kbd>⌃</kbd><kbd>↑</kbd></kbd> / <kbd><kbd>⌃</kbd><kbd>↓</kbd></kbd>.


## Script Workspace

| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| **Any OS**
| Any OS | script tab | <kbd><samp>Right-click</samp> > <samp>Check for Problems</samp></kbd> | Check script for problems |
||
| **Mac**
| Mac | script step | <kbd>+</kbd> | Edit script step options |
||
| **Mac + MBS**
| Mac + MBS |  | <kbd><kbd>⇧</kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> | Find in script list |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> | Find in script step text |
| Mac + MBS |  | <kbd><kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> then <kbd>Enter</kbd></kbd> | Find again in script step text |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>G</kbd></kbd> or <kbd><kbd>⌘</kbd><kbd>L</kbd></kbd> | Go to line in script steps |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>+</kbd></kbd> | Zoom in on active area|
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>-</kbd></kbd> | Zoom out on active area |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>=</kbd></kbd> | Zoom active area to 100% |
| Mac + MBS | script step  | <kbd><samp>Right-click</samp></kbd> | See a context Menu of MBS functions |
| Mac + MBS | script step  | <kbd><samp>Click</samp> `⌄`</kbd> (right of line number)| Toggle code block (section) |
| Mac + MBS | script step  | <kbd><kbd>⌥</kbd>+<samp>Click</samp> `⌄`</kbd> (right of line number)| Toggle code block (entire block) |
| Mac + MBS | Export Records Dialog | <kbd><samp>Hover Tooltip</samp></kbd> | Useful [Tooltips for the FileMaker export dialog](https://www.mbs-plugins.com/archive/2019-03-07/Tooltips_for_the_FileMaker_exp/monkeybreadsoftware_blog_filemaker) |
||
| **fmAutoMate + Mac + MBS**
| fmAutoMate + Mac + MBS | script step | <kbd><samp>Right-click</samp></kbd>| See a context Menu of fmAutomate functions |
| fmAutoMate + Mac + MBS | script step | <kbd><samp>Right-click</samp></kbd> then type <kbd>O</kbd><kbd>N</kbd><kbd>⏎</kbd> | Turn on fmAutoMate HotKeys |
| fmAutoMate + Mac + MBS | script step | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> | Find in script step text |
| fmAutoMate + Mac + MBS | script step | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>G</kbd></kbd> | Find Again in script step text |
| fmAutoMate + Mac + MBS | script step | <kbd><kbd>⌃</kbd><kbd>⇧</kbd><kbd>⌘</kbd><kbd>G</kbd></kbd> | Find Again backwards in script step text |
| fmAutoMate + Mac + MBS | selected script steps | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>A</kbd></kbd> | Replace All in XML of selected steps |
| fmAutoMate + Mac + MBS | script step | <kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>H</kbd></kbd> | Insert a history comment |

## Layout Workspace

| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| Mac + MBS | | <kbd><kbd>⌘</kbd><kbd>⌥</kbd><kbd>⇧</kbd><kbd>F</kbd></kbd> |	Find object in layout.|

## Calculation & Custom Function Editor

| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| **Mac + MBS**
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>⌥</kbd><kbd>C</kbd></kbd> | Copy MBS-styled text |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>]</kbd></kbd> (DE <kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>5</kbd></kbd>) | Indent selected text |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>[</kbd></kbd> (DE <kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>6</kbd></kbd>) | Outdent selected text |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> | Find |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>F</kbd> + <kbd>Enter</kbd></kbd> | Find Again |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>R</kbd></kbd> | Show Ruler - to (temporarily) edit tab stops |
| Mac + MBS |  | <kbd><kbd>⌘</kbd><kbd>I</kbd></kbd> | Toggle invisible characters |
| Mac + MBS |  | <kbd><kbd>⌃</kbd><kbd>↑</kbd>/<kbd>⌃</kbd><kbd>↓</kbd></kbd> | move lines up or down.

## Debugger

| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| **Mac**
| Mac |  | <kbd>F5</kbd> | Step Over |
| Mac |  | <kbd><kbd>⇧</kbd><kbd>⌘</kbd>F5</kbd> | Set Next Step |
| Mac |  | <kbd>F6</kbd> | Step Into |
| Mac |  | <kbd>F7</kbd> | Step Out |
| Mac |  | <kbd><kbd>⌘</kbd>F8</kbd> | Halt Script |
| Mac |  | <kbd><kbd>⌥</kbd>F8</kbd> | Continue |
| Mac |  | <kbd><kbd>⌘</kbd>F9</kbd> | Set Breakpoint |
| Mac |  | <kbd><kbd>⇧</kbd><kbd>⌘</kbd>F9</kbd> | Remove Breakpoint |
| Mac |  | <kbd><kbd>⌘</kbd>F10</kbd> | Edit Script |

## Data Viewer

| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| **Mac + MBS**
| Mac + MBS | focus on the list | <kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> |	Show find bar.|
| Mac + MBS | focus on the list | <kbd><kbd>⌘</kbd><kbd>G</kbd></kbd> |	Go to next found text.|
| Mac + MBS | focus on the list | <kbd><kbd>⇧</kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> |	Show/hide fields.|
| Mac + MBS | focus on the list | <kbd><kbd>⇧</kbd><kbd>⌘</kbd><kbd>G</kbd></kbd> |	Show/hide global variables.|
| Mac + MBS | focus on the list | <kbd><kbd>⌘</kbd><kbd>+</kbd></kbd> |	Zoom in.|
| Mac + MBS | focus on the list | <kbd><kbd>⌘</kbd><kbd>-</kbd></kbd> |	Zoom out.|
| Mac + MBS | focus on the list | <kbd><kbd>⌘</kbd><kbd>=</kbd></kbd> |	Zoom to 100%.|
| Mac + MBS | focus on the list | <kbd><kbd>⌘</kbd><kbd>⌥</kbd><kbd>C</kbd></kbd> |	Copy text in the list.|

## Relationship Dialog

| In this environment | In this context | Do/press this | In order to |
| ------------------- | --------------- | ------------- | ----------- |
| **Mac**
| Mac | relationship selected | <kbd><kbd>⌘</kbd><kbd>O</kbd></kbd> | Open the Edit Relationship dialog |
||
| **Mac + MBS**
| Mac + MBS | | <kbd><kbd>⌘</kbd><kbd>F</kbd></kbd> | Set focus to search field. |

## Links

### Plugins

- [MBS Plugin](https://www.monkeybreadsoftware.com/filemaker/)
- [fmAutoMate](https://www.fmworkmate.com/fmautomate)

### Documentation

- [Claris Pro and FileMaker Pro Help > Reference > Keyboard shortcuts (macOS)](https://help.claris.com/en/pro-help/content/shortcuts-os-x.html)
- [Claris Pro and FileMaker Pro Help > Reference > Keyboard shortcuts (Windows)](https://help.claris.com/en/pro-help/content/shortcuts-windows.html)
- [Mac keyboard shortcuts](https://support.apple.com/en-us/HT201236)
- [Create keyboard shortcuts for apps on Mac](https://support.apple.com/en-gb/guide/mac-help/mchlp2271/mac)
