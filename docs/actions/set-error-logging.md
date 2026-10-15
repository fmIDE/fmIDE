<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Error Logging`

Enable or disable FileMaker script-error logging, optionally adding calculated debug information.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Error Logging](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26200) | Yes | beta | <v0.67 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Set Error Logging
[:]..custom_debug_info = == «calculation»
[:]..state = 1
```

## Usage

### Set Error Logging




> ---
> 
> #### Test Case #1 "Set Error Logging - test no file lock when no errors occurred"
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
> [+].Set Error Logging
> [:]..state = 1
> [:]..custom_debug_info = "123"
> ```
> 
> 
> ##### Description
> 
> Apparently FileMaker keeps the file busy, so that it cannot be read after being written to by FileMaker
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Error Logging = true + custom debugging 123 + error"
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
> [+].Set Error Logging
> [:]..state = 1
> [:]..custom_debug_info = == $error_count+1
> ```
> 
> 
> ##### Description
> 
> Once FileMaker has written to the ScriptErrors.log file the file becomes locked and kept busy by FileMaker so that the file cannot be read after being written to by FileMaker (error 300). The solution is to turn error logging off again - which releases the file -  before reading the file.
> 
> 
> 
> ---
> 
> #### Test Case #3 "Throw error - use for testing Set Error Logging"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set Error Capture = true
> 
> [+].Re-Login
> [:]..user = "Throw"
> [:]..password = "Error"
> 
> 
> ```
> 
> 
> ##### Description
> 
> Apparently FileMaker keeps the file busy, so that it cannot be read after being written to by FileMaker
> 
> 
> 


