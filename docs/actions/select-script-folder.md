<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Select Script Folder`

Select a script folder in the Script Workspace by name; requires macOS and MBS.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | dev | v0.77 |

## Description

Opens the Script Workspace, then selects and expands the named script folder. Requires macOS and the MBS plugin; there is no equivalent native script step.

Supply the folder name as literal text in script_name. The short form expands to script_name. To calculate the name when the action runs, set by to "name" and supply a calculation in script_name.

## Full Syntax

```
[+].Select Script Folder
[:]..script_name = "fmIDE Module"
```

## Usage

### Select Script Folder


Select and expand a folder by its literal name: [+].Select Script Folder = "fmIDE Module". The long form uses script_name.


> ---
> 
> #### Test Case #1 "Select Script Folder"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Select Script Folder = "fmIDE Module"
> ```
> 
> 
> ##### Description
> 
> Selects and expands the fmIDE Module script folder in the Script Workspace.
> 
> 
> 


