<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Layout Field`

Attempt to activate a field on the current layout using AppleScript on macOS; visual focus is not always updated.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Partial | alpha | v0.12 |

## Description

Attempts to go to the given layout field.

Uses AppleScript.

## Full Syntax

```
[+].Go to Layout Field
[:]..layout_field_name = == fmIDE_Test::_gTest
[:]..repetition = == «calculation»
```

## Usage

### Go to Layout Field




> ---
> 
> #### Test Case #1 "Go to Layout Field"
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
> [+].Go to Layout Field = "fmIDE_Test::_gTest"
> 
> ```
> 
> 
> ##### Description
> 
> The current implementation of Go to Layout Field uses Applescript:
> - Only works on a Mac and does not activate the field 100%
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Layout Field .repetition"
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
> [+].Go to Layout Field
> [:]..layout_field_name= == fmIDE_Test::_gTest
> [:]..repetition= 2
> 
> ```
> 
> 
> ##### Description
> 
> The current implementation of Go to Layout Field uses Applescript:
> - Only works on a Mac and does not activate the field 100%
> 
> 
> 


## See also

- [Go To Base Field](go-to-base-field.md)
- [Go to Field](go-to-field.md)
