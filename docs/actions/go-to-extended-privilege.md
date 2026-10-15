<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Extended Privilege`

Open Manage Security and prepare an extended-privilege name; select the relevant panel and entry manually.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | alpha | v0.12 |

## Description

Goes to the given Extended Privilege, if possible(1).

1. Stores the extended privilege name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage Security` dialog

You must manually:

- select the `Advanced Settings…` view
- switch to the Extended Privilege panel
- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

(1) Note: It is only possible to jump to custom privilege sets (because "[" cannot be typed in the list).

## Full Syntax

```
[+].Go to Extended Privilege
```

## Usage

### Go to Extended Privilege




> ---
> 
> #### Test Case #1 "Go to Extended Privilege"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> 
> 


## See also

- [Go to Privilege Set](go-to-privilege-set.md)
- [Go to Account](go-to-account.md)
