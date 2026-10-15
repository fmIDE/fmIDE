<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Script`

Open a script and focus its steps; can combine initial step selection, step search and subsequent selection extension. UI automation requires macOS and MBS.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | ok | v0.1 |

## Description

Goes to the given Script, if possible(1).

1. Stores the script name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Script Workspace`(2)
3. Locates the Script in the script list and activates it
4. Sets focus on the script steps panel
5. If script_number, script_number_range or script_number_to is specified script steps are selected
6. If script_step_search is specified the MBS search is activated

(1) MBS plugin shows an error, if the script cannot be found
(2) On windows (or without the MBS plugin) you must locate the script manually from here.

## Full Syntax

```
[+].Go to Script
[:]..by = "name"|"selected"(default)
[:]..script_name = "«string»" // when by≠"name"
[:]..script_name = == «calculation» // when by="name"
[:]..script_step_number = == «calculation»
[:]..script_step_number_to = == «calculation»
[:]..script_step_range = == «calculation»

```

## Usage

### Go to Script




> ---
> 
> #### Test Case #1 "Go to Script // Note: script_name parameter is **static**, not a calculation"
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
> [+].Go to Script = "fmIDE"
> ```
> 
> 
> 
> 


## See also

- [Go to Script Step](go-to-script-step.md)
- [Find Script Step](find-script-step.md)
