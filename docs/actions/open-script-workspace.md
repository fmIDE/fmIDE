<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Open Script Workspace`

Open the Script Workspace, optionally navigating to a script or step using the shared script-navigation parameters.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Open Script Workspace](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26088) | Yes | beta | v0.3 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Open Script Workspace
```

## Usage

### Open Script Workspace




> ---
> 
> #### Test Case #1 "Open Script Workspace"
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
> [+].Open Script Workspace
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Open Script Workspace & Pause Script (to inspect)"
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
> [+].Move/Resize Window
> [:]..left = == 10
> [:]..top = == Get ( WindowDesktopHeight )*3/4
> [:]..width = == Get ( WindowDesktopWidth ) -20
> [:]..height = == Get ( WindowDesktopHeight )*1/4 - 10
> [+].Open Script Workspace
> [+].Select Window
> [+].Show/Hide Toolbars = 1
> [+].Pause
> ```
> 
> 
> ##### Description
> 
> Script Workspace is visible but not editable because of paused script - interesting! you can edit it when the debugger is showing!
> 
> 
> 


