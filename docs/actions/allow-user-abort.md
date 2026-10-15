<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Allow User Abort`

Control whether the user can interrupt the running action script.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Allow User Abort](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26085) | Yes | ok | 0.42 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Allow User Abort
[:]..state = «boolean-expression»
```

## Usage

### Allow User Abort




> ---
> 
> #### Test Case #1 "Allow User Abort 0 (off)"
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
> [+].Allow User Abort = 0
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Allow User Abort 1 (on)"
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
> [+].Allow User Abort = 1
> ```
> 
> 
> 
> 


