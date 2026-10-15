<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Show/Hide Toolbars`

Show or hide FileMaker toolbars using the supported state and locking options.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Show/Hide Toolbars](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26029) | Yes | beta | v0.71 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Show/Hide Toolbars
[:]..lock  = == «calculation»
[:]..state = "Hide"|"Show" // also " lock"
```

## Usage

### Show/Hide Toolbars




> ---
> 
> #### Test Case #1 "Show/Hide Toolbars - Hide and unlock (=0)"
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
> [+].Show/Hide Toolbars
> [:]..state = "Hide"
> [:]..lock  = 0
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Show/Hide Toolbars - Show and unlock (=1)"
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
> [+].Show/Hide Toolbars
> [:]..state = "Show"
> [:]..lock  = 0
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Show/Hide Toolbars - Show and lock (=2)"
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
> [+].Show/Hide Toolbars
> [:]..state = "Show"
> [:]..lock  = 1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Show/Hide Toolbars - Hide and lock (=3)"
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
> [+].Show/Hide Toolbars
> [:]..state = "Hide"
> [:]..lock  = 1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Show/Hide Toolbars (short form = toggle)"
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
> [+].Show/Hide Toolbars
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #6 "Show/Hide Toolbars = 0 (short form = hide)"
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
> [+].Show/Hide Toolbars = 0
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #7 "Show/Hide Toolbars = 1 (short form = show)"
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
> [+].Show/Hide Toolbars = 1
> ```
> 
> 
> 
> 


