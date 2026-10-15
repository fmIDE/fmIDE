<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Value List`

Open Manage Value Lists and prepare the value-list name in the fmAutoMate keyboard buffer; final selection is manual.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | ok | v0.12 |

## Description

Goes to the given value list.

1. Stores the value list name in the fmAutoMate Keyboard Buffer file.
2. Opens the `Manage Value Lists` dialog

You must manually:

- press the fmAutoMate keyboard shortcut to retype the name

## Full Syntax

```
[+].Go to Value List
[:]..by = "selection"(default)|"name"|"number"
[:]..value_list_name = "Category"
[:]..value_list_number  = == «calculation»
```

## Usage

### Go to Value List




> ---
> 
> #### Test Case #1 "Go to Value List (short form)"
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
> [+].Go to Value List = "Category"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Value List (long form)"
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
> [+].Go to Value List
> [:]..value_list_name = "Category"
> ```
> 
> 
> 
> 

### Go to Value List by number


Goes to a value list in creation order. -1 thus goes to the latest value list.


> ---
> 
> #### Test Case #1 "Go to Value List last created using by="number" -1 (long form)"
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
> [+].Go to Value List
> [:]..by = "number"
> [:]..value_list_number  = -1
> ```
> 
> 
> 
> 


