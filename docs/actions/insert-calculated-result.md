<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Insert Calculated Result`

Insert a calculation result into the specified target or current selection.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Insert Calculated Result](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26077) | Yes | beta | v0.45 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Insert Calculated Result
[:]..calculation = == «calculation»
[:]..target = «string»
```

## Usage

### Insert Calculated Result




> ---
> 
> #### Test Case #1 "Insert Calculated Result (short form)"
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
> [+].Insert Calculated Result.fmIDE_Test::_gTest = ===
> JSONSetElement("{}"
> ;["actions" ; $fmide_actions ; JSONArray]
> )
> ===
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Insert Calculated Result (long form)"
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
> [+].Insert Calculated Result
> [:]..target = "fmIDE_Test::_gTest"
> [:]..calculation = ===
> JSONSetElement("{}"
> ;["actions" ; $fmide_actions ; JSONArray]
> )
> ===
> ```
> 
> 
> 
> 


## See also

- [Insert Text](insert-text.md)
- [Insert from URL](insert-from-url.md)
