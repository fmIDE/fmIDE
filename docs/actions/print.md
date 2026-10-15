<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Print`

Print using existing print settings, optionally showing the print dialog; printer selection is not exposed as an action parameter.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Print](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26043) | Partial | alpha | v0.86 |

## Description

Performs the equivalent script step.

Supports

.with_dialog (true/false)

Does not Support

Printer choice/settings

## Full Syntax

```
[+].Print
[:]..with_dialog = true|false
```

## Usage

### Print




> ---
> 
> #### Test Case #1 "Print with Dialog"
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
> [+].Print
> [:]..with_dialog = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Print with no Dialog"
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
> [+].Print
> [:]..with_dialog = false
> ```
> 
> 
> 
> 


