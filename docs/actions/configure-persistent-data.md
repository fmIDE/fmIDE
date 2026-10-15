<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Configure Persistent Data`

Store or delete a value by instance ID in the fixed fmIDE persistent store. Requires FileMaker 26.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Configure Persistent Data](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26238) | Partial | beta | v0.56 |

## Description

Store or delete a persistent value in the fixed `fmIDE` store (FileMaker 26 or later).

- `instance_id`: calculation returning the instance identifier.
- `calculation`: calculation returning the value to store. The parameter is named `calculation`, not `value`.
- `delete`: calculation returning true to delete the instance instead of storing a value.

Each supplied calculation is evaluated once when the action executes. Reusing an instance ID replaces its value. Zero and empty text remain stored instances; use deletion to remove them. Unicode, quotes and line breaks are preserved.

Use the long form when storing data. The scalar shorthand supplies an instance ID and currently selects deletion. Other store names are not supported by this action; macro storage is managed by the dedicated macro actions.

## Full Syntax

```
# Store a value.
[+].Configure Persistent Data
[:]..instance_id = == "Example"
[:]..calculation = == "Hello World from fmIDE"
[:]..delete = 0

# Read it with a FileMaker calculation.
[+].Exit Script = == GetPersistentData ( "fmIDE" ; "Example" )

# Deletion is a separate invocation:
# [+].Configure Persistent Data
# [:]..instance_id = == "Example"
# [:]..delete = 1
```

## Usage

### Configure Persistent Data (Set)




> ---
> 
> #### Test Case #1 "Configure Persistent Data (Set)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Configure Persistent Data
> [:]..instance_id = == "HelloWorld"
> [:]..calculation = == "Hello World from fmIDE"
> ```
> 
> 
> 
> 

### Configure Persistent Data (Delete)




> ---
> 
> #### Test Case #1 "Configure Persistent Data (Delete)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Configure Persistent Data
> [:]..instance_id = == "HelloWorld"
> [:]..delete = true
> ```
> 
> 
> 
> 


