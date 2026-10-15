<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Base Table`

Open Manage Database for a table in the current file and prepare its name in the fmAutoMate keyboard buffer; final selection is manual.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.12 |

## Description

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
[+].Go to Base Table
```

## Usage

### Go to Base Table




> ---
> 
> #### Test Case #1 "Go to Base Table (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Table
> [:]..table_name = "Table1"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Base Table (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Table = "Table1"
> ```
> 
> 
> 
> 


## See also

- [Go to Table](go-to-table.md)
- [Go to Table Occurrence](go-to-table-occurrence.md)
- [Go To Base Field](go-to-base-field.md)
