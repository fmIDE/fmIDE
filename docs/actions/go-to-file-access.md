<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to File Access`

Open Manage Security for File Access; navigation within the dialog remains manual.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | alpha | v0.75 |

## Description

Goes to the given File Access, if possible(1).

1. Stores the extended privilege name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage Security` dialog

You must manually:

- select the `Advanced Settings…` view
- switch to the File Access panel
- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

(1) Note: It is only possible to jump to custom privilege sets (because "[" cannot be typed in the list).

## Full Syntax

```
[+].Go to File Access
```

