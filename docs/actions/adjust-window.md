<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Adjust Window`

Resize or arrange the current window using the requested adjustment.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Adjust Window](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26031) | Yes | ok | v0.53 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Adjust Window
[:]..state = == "Hide"|"Maximize"|"Minimize"|"Resize to Fit"|"Restore"
```

## Usage

### Adjust Window




> ---
> 
> #### Test Case #1 "Adjust Window (short forms)"
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
> [+].Adjust Window = ==== Resize to Fit
> [+].Adjust Window = ==== Hide
> [+].Adjust Window = ==== Restore
> [+].Adjust Window = ==== Maximize
> [+].Adjust Window = ==== Minimize
> [+].Adjust Window = ==== Restore
> ```
> 
> 
> ##### Description
> 
> Test requires MBS
> 
> 
> 
> ---
> 
> #### Test Case #2 "Adjust Window (long form)"
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
> [+].Adjust Window
> [:]..state = ==== Resize to Fit
> [+].Adjust Window
> [:]..state = ==== Hide
> [+].Adjust Window
> [:]..state = ==== Restore
> [+].Adjust Window
> [:]..state = ==== Maximize
> [+].Adjust Window
> [:]..state = ==== Minimize
> [+].Adjust Window
> [:]..state = ==== Restore
> ```
> 
> 
> ##### Description
> 
> Test requires MBS
> 
> 
> 


