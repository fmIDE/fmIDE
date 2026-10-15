<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to External Data Source`

Open Manage External Data Sources and prepare the source name in the fmAutoMate keyboard buffer; final selection is manual.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.12 |

## Description

Goes to the given External Data Source.

1. Stores the external data source name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage External Data Sources` dialog

You must manually:

- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

## Full Syntax

```
[+].Go to External Data Source
[:]..external_data_source_name = «string»
```

## Usage

### Go to External Data Source




> ---
> 
> #### Test Case #1 "Go to External Data Source (Short Form)"
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
> [+].Go to External Data Source = "FileA"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to External Data Source (Long Form)"
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
> [+].Go to External Data Source
> [:]..external_data_source_name = "FileB"
> ```
> 
> 
> 
> 


