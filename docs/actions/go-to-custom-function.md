<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Custom Function`

Open Manage Custom Functions and prepare the function name for manual selection; uses macOS, MBS and a hiatus.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.12 |

## Description

Goes to the given Custom Function.

1. Stores the custom_function_name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Custom Functions` dialog

You must manually:

- press the fmAutoMate keyboard shortcut to retype the name

Note:

This dialog has no native script step to open it, and can only be opened when there is no script running. fmIDE thus uses some tricks (a 'Hiatus' and some MBS tricks to get there)

## Full Syntax

```
[+].Go to Custom Function
```

## Usage

### Go to Custom Function




> ---
> 
> #### Test Case #1 "Go to Custom Function"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Custom Function = "fmJAML"
> ```
> 
> 
> 
> 


