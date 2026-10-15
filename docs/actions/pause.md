<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Pause`

Pause action-script execution for a calculated duration or indefinitely.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta |  |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Pause
[:]..duration = == «calculation»
[:]..indefinitely = == «calculation»
```

## Usage

### Pause for a duration




> ---
> 
> #### Test Case #1 "Pause.duration 500/1000 (long form)"
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
> [+].Pause
> [:]..duration = 500/1000
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Pause 0 seconds (short form)"
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
> [+].Pause = 0
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Pause 1 second (short form)"
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
> [+].Pause = 1
> ```
> 
> 
> 
> 

### Pause indefinitely




> ---
> 
> #### Test Case #1 "Pause.indefinitely = true (long form)"
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
> [+].Pause
> [:]..indefinitely = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Pause = "indefinitely" (short form)"
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
> [+].Pause = == "indefinitely"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Pause (shortest form default= indefinitely)"
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
> [+].Pause
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Pause (shortest form = indefinitely)"
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
> [+].Pause
> ```
> 
> 
> 
> 


