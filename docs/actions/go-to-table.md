<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Table`

Navigate toward a table definition using the shared table-navigation actions; this action is still in development.

[All actions](README.md)


| Alias | FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|---------|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Base Table / Go to Table Occurrence](go-to-base-table.md)| None | Yes | dev | v0.3 |

## Description

FIXME

Goes to the given base table, if possible(*).

1. Stores the base table name in the fmAutoMate Keyboard Buffer file.
2. Calculates the equivalent Base Layout name.
3. Goes to the Base Layout
4. Opens the `Manage Database` dialog

You must manually:

- switch to the Tables view
- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

(*) Note: It is only possible to go to base tables within the current file.

## Full Syntax

```
[+].Go to Table
```

## Usage

### Go to Table




> ---
> 
> #### Test Case #1 "Go to Table"
> 
> ##### Status
> 
> ✋ manual test 
> 
> 
> 
> 


## See also

- [Go to Base Table](go-to-base-table.md)
- [Go to Table Occurrence](go-to-table-occurrence.md)
