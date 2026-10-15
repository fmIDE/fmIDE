<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Select Window`

Activate a named FileMaker window, optionally restricting selection to the current file.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Select Window](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26123) | Yes | beta |  |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Select Window
[:]..current_file = 1
[:]..window_name = == "fmIDE"
```

## Usage

### Select Window




> ---
> 
> #### Test Case #1 "Select Window (long form)"
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
> [+].Select Window
> [:]..window_name = == "fmIDE"
> [:]..current_file = 1
> [+].Select Window = == $window_name_orig
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Select Window = == «window name» (short form)"
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
> [+].Select Window = == "fmIDE"
> ```
> 
> 
> ##### Description
> 
> Selects the original window
> 
> 
> 
> ---
> 
> #### Test Case #3 "Select Window = (short form for original window)"
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
> [+].Select Window
> ```
> 
> 
> ##### Description
> 
> Selects the original window
> 
> 
> 


