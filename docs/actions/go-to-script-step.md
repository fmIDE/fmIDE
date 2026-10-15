<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Script Step`

Navigate to a step in the Script Workspace; negative step numbers count from the end. Requires macOS and MBS.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | ok | v0.1 |

## Description

Goes to the given Script Step. (Mac only)

Negative script_step_numbers are relative to the end of the script.

## Full Syntax

```
[+].Go to Script Step
[:]..script_name        = "«script_name»"
[:]..script_step_number = == «calculation»
```

## Usage

### Go to Script Step




> ---
> 
> #### Test Case #1 "Go to Script, step_number 2"
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
> [+].Go to Script
> [:]..script_name        = "fmIDE"
> [:]..script_step_number = 2
> ```
> 
> 
> 
> 


## See also

- [Go to Script](go-to-script.md)
- [Find Script Step](find-script-step.md)
