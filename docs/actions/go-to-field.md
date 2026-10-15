<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Field`

Alias of Go to Layout Field; attempts to activate a layout field using AppleScript on macOS.

[All actions](README.md)


| Alias | FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|---------|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Layout Field](go-to-layout-field.md)| [Go to Field](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26017) | Partial | alpha | v0.15 |

## Description

Goes to a layout field.

Implemented with Applescript => Mac only. not 100%: Field is activated but is not visually active

## Full Syntax

```
[+].Go to Field
[:]..table_name = "fmIDE_Test"
[:]..layout_field_name = "_gTest"
# or
[:]..layout_field_name = "fmIDE_Test::_gTest"

```

## Usage

### Go to Field




> ---
> 
> #### Test Case #1 "Go to Field table::field (short form)"
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
> [+].Go to Field = "fmIDE_Test::_gTest"
> ```
> 
> 
> ##### Description
> 
> Goes to a layout field
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Field layout_field_name (long form)"
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
> [+].Go to Field
> [:]..layout_field_name = "fmIDE_Test::_gTest"
> ```
> 
> 
> ##### Description
> 
> Goes to a layout field
> 
> 
> 
> ---
> 
> #### Test Case #3 "Go to Field table_name & layout_field_name (long form)"
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
> [+].Go to Field
> [:]..table_name = "fmIDE_Test"
> [:]..layout_field_name = "_gTest"
> ```
> 
> 
> ##### Description
> 
> Goes to a layout field
> 
> 
> 
> ---
> 
> #### Test Case #4 "Error: Go to Field"
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
> [+].Go to Field="fmIDE_Test::This field does not exist"
> ```
> 
> 
> 
> 


