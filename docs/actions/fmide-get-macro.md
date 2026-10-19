<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `fmIDE Get Macro`

Retrieve a stored macro object into a target; without a target, return it and exit the action script. Requires FileMaker 26.

[All actions](README.md)

The macro contract and syntax below were reconciled in the repository on 19 October 2026. Use `macro_name`, optional `metadata`, and `script`; older `name`/`code` objects are not assumed to be aliases. These corrections await synchronization to the database documentation and a fresh export. The recorded usage results below predate this revision.


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.69 |

## Description

Retrieve the complete stored macro object: `macro_name`, `script`, and any `metadata` (FileMaker 26 or later).

- `macro_name`: a calculation returning the name; a dotted action-key name is literal shorthand.
- `target`: an optional literal variable or field name. With a target, Get writes the object there and continues.

Without a target, Get returns the object and exits the current fmIDE action script. A missing stored macro returns `?`; it does not report Run Macro's error 1700. A missing or empty name reports error 5. Explicit names are evaluated once.

## Full Syntax

```
# Return the object and exit this action script.
[+].fmIDE Get Macro.Example

# Separate invocation: write to a target and continue.
# [+].fmIDE Get Macro
# [:]..macro_name = == "Example"
# [:]..target = "$macro"
# [+].Exit Script = == JSONGetElement ( $macro ; "script" )
```

## Usage

### fmIDE Get Macro




> ---
> 
> #### Test Case #1 "fmIDE Get Macro HelloWorld"
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
> [+].fmIDE Get Macro.macro_name = == "HelloWorld"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "fmIDE Get Macro Echo"
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
> [+].fmIDE Get Macro.Echo
> ```
> 
> 
> ##### Description
> 
> Format is
> [+].fmIDE Define Macro.«macro_name» = ==== «macro-fmJAML-code»
> [+].fmIDE Get Macro.«macro_name» = «path»
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "fmIDE Get Macro Echo"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].fmIDE Get Macro.Echo
> ```
> 
> 
> ##### Description
> 
> Format is
> [+].fmIDE Define Macro.«macro_name» = ==== «macro-fmJAML-code»
> [+].fmIDE Get Macro.«macro_name» = «path»
> 
> 
> 
> 


