<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Field By Name`

Calculate the target field name at runtime and assign the supplied calculation result.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Field By Name](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26147) | Yes | alpha | v0.32 |

## Description

Calculate a field name at runtime, then assign the result of another calculation to that field.

- `target`: calculation returning a complete field name, such as `"fmIDE_Test::_gTest"`.
- `calculation`: expression returning the value to assign.

Use `= ==` for both expressions so they run when this action executes. A variable set by an earlier action can supply the target name. Normal field access, record locking and validation rules still apply; committing a record is separate.

Use the long form shown below. The legacy short form puts a target calculation in the key and is deprecated because it is easy to confuse a literal name with a calculation. The example uses a global field in the fmIDE test file.

## Full Syntax

```
[+].Set.$field = == "fmIDE_Test::_gTest"
[+].Set Field By Name
[:]..target = == $field
[:]..calculation = == "calculated target"
[+].Exit Script = == fmIDE_Test::_gTest
```

## Usage

### Set Field By Name


Target field is calculated


> ---
> 
> #### Test Case #1 "Set Field By Name (long form)"
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
> [+].Set Field By Name
> [:]..target = == "fmIDE_Test::_gTest"
> [:]..calculation = == "123" & "4567"
> ```
> 
> 
> 
> 

### Set Field By Name (short form) - Deprecated!


The short form of Set Field By Name is rather confusing. Deprecated.


> ---
> 
> #### Test Case #1 "Set Field By Name.«target-calculation» (short form)"
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
> [+].Set Field By Name."fmIDE_Test::_gTest" = 123456
> ```
> 
> 
> ##### Description
> 
> Short forms for `Set Field By Name`, while it is possible, are not recommended, since they can be easily misinterpreted.
> 
> For example, does this code set the field `fmIDE_Test::_gTest` or does it use the contents of that field to decide what field to set?
> 
> And Quotes in a key name? No thank you!
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Field By Name.$field_name (short form)"
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
> [+].Set.$field_name = == "fmIDE_Test::_gTest"
> [+].Set Field By Name.$field_name = 123456
> ```
> 
> 
> ##### Description
> 
> Short forms for `Set Field By Name`, while it is possible, are not recommended, since they can be easily misinterpreted.
> 
> For example, does this code set the variable `$field_name` or does it use the contents of that variable to decide what field to set?
> 
> 
> 


