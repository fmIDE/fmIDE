<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Privilege Set`

Open Manage Security and prepare a privilege-set name for manual selection; this action halts script execution.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | ok | v0.12 |

## Description

Goes to the given Privilege Set, if possible(1).

1. Stores the privilege set name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage Security` dialog

You must manually:

- select the `Advanced Settings…` view
- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

(1) Note: It is only possible to jump to custom privilege sets (because "[" cannot be typed in the list).

Important: This step halts.

## Full Syntax

```
[+].Go to Privilege Set
```

## Usage

### Go to Privilege Set




> ---
> 
> #### Test Case #1 "Go to Privilege Set"
> 
> ##### Status
> 
> ❌ Fail 
> ✋ manual test ⛔️ HALTS 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Privilege Set = "Test" // "[Data Entry Only]" - Note it is not possible to type the square brackets in the dialog!
> ```
> 
> 
> ##### Description
> 
> The script stops
> 
> 
> 


## See also

- [Go to Account](go-to-account.md)
- [Go to Extended Privilege](go-to-extended-privilege.md)
