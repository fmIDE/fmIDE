<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Variable`

Assign a calculation result to a named local or global variable, optionally at a specified repetition.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Variable](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26141) | Yes | beta |  |

## Description

Assign a calculation result to a named variable. Use `$name` for a local variable or `$$name` for a file global; later actions in the same fmIDEAS can read the assigned value.

- `target` (or `variable_name`): literal variable name, including its `$` prefix.
- `calculation`: expression evaluated when this action executes.
- `repetition`: optional calculation returning the repetition number; defaults to the first repetition.

The short form puts the literal target in the key, for example `Set Variable.$count`. Use `= ==` for expressions that read values set by earlier actions. Names beginning with `$fmide__` are reserved.

This action uses the shared Set implementation; the target itself determines whether a variable or field is written. Prefer `Set Variable` with variable targets for clear code.

## Full Syntax

```
[+].Set Variable.$count = == 1
[+].Set Variable
[:]..target = "$count"
[:]..calculation = == $count + 1
[+].Set Variable
[:]..target = "$items"
[:]..repetition = == 2
[:]..calculation = == "second"
[+].Exit Script = == $count & "/" & $items[2]
```

## Usage

### Set Variable




> ---
> 
> #### Test Case #1 "Set Variable $i=42 (long form)"
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
> [+].Set Variable
> [:]..target = "$i"
> [:]..calculation  = 42
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Variable $i=42 (short form)"
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
> [+].Set Variable.$i=42
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Set $i = == $i+1 (short form)"
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
> [+].Set.$i = == $i+1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Set $$text = "\"text\"" (short form)"
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
> [+].Set.$$text = "\"text\""
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Error: Set Variable (no target → 5)"
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
> [+].Set Variable=1
> ```
> 
> 
> 
> 


## See also

- [Set](set.md)
