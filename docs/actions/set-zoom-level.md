<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Zoom Level`

Set the window's zoom level, optionally locking it.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Zoom Level](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26097) | Partial | beta | v0.54 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Set Zoom Level
[:]..calculation  = == «calculation»
[:]..lock  = == «calculation»
```

## Usage

### Set Zoom Level




> ---
> 
> #### Test Case #1 "Set Zoom Level"
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
> [+].Set Zoom Level = 25
> [+].Set Zoom Level = 50
> [+].Set Zoom Level = 100
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Zoom Level (long form)"
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
> [+].Set Zoom Level
> [:]..calculation  = 25
> [:]..lock  = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Set Zoom Level % (FM26)"
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
> [+].Set Zoom Level = 100 + 23
> [+].Set Zoom Level = 321
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Set Zoom Level (Zoom In)"
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
> [+].Set Zoom Level = == "Zoom In"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Set Zoom Level (Zoom Out)"
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
> [+].Set Zoom Level = == "Zoom Out"
> ```
> 
> 
> 
> 


