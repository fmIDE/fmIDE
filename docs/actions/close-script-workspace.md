<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Close Script Workspace`

Close the Script Workspace through the development UI.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | dev | 0.44 |

## Description

Tries to close the Script Workspace.

## Full Syntax

```
[+].Close ScriptWorkspace
```

## Usage

### Close ScriptWorkspace




> ---
> 
> #### Test Case #1 "Close Script Workspace (via Menu - does not work)"
> 
> ##### Status
> 
> ❌ Fail 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].	Close Script Workspace
> ```
> 
> 
> ##### Description
> 
> #52092	View	Close Tab
> #52093	View	Close All Tabs
> #52097	View	Close Workspace
> #	View	-
> #52094	View	Select Next Tab
> #52095	View	Select Previous Tab
> #52096	View	Move Tab to New Window
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Close Script Workspace with CMD+SHIFT-W - does not work"
> 
> ##### Status
> 
> ❌ Fail 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].	Press
> [:].	.command_key="W"
> [:].	.shift=1
> ```
> 
> 
> ##### Description
> 
> #52092	View	Close Tab
> #52093	View	Close All Tabs
> #52097	View	Close Workspace
> #	View	-
> #52094	View	Select Next Tab
> #52095	View	Select Previous Tab
> #52096	View	Move Tab to New Window
> 
> 
> 
> 


