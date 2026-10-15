<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Window Title`

Set a FileMaker window's title from a calculation.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Window Title](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26124) | Yes | beta | v0.74 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Set Window Title
[:]..new_window_title = == «calculation»
[:]..window_name = == «calculation»
```

## Usage

### Set Window Title




> ---
> 
> #### Test Case #1 "Set Window Title (Short Form)"
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
> [+].Set Window Title = == "Hello"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Window Title of a named window"
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
> [+].Set Window Title
> [:]..window_name = == "fmIDE"
> [:]..new_window_title = == "fmIDE was here!"
> ```
> 
> 
> 
> 


