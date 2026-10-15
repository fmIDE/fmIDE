<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Multi-User`

Set the current file's sharing state, including the supported hidden-file option.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Multi-User](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26084) | Yes | dev | v0.89 |

## Description

Performs the equivalent of the Set Multi-User script step.

state is a calculation: 0 (or omitted) turns sharing off, 1 turns it on, and 2 turns it on with the file hidden from the host list. With state = 1, hidden = 1 also selects On (Hidden); hidden is ignored when state = 0. Both parameters are evaluated when the action runs.

The short form expands to state, for example [+].Set Multi-User = 2.

## Full Syntax

```
[+].Set Multi-User
[:]..state = == 1
[:]..hidden = == 0
```

