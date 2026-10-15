<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Base Layout`

Resolve and open the base layout for a table in the current file.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Partial | beta |  |

## Description

Goes to the base layout for the given base table or table or TO, if possible(*).

1. Stores the base layout name in the fmAutoMate Keyboard Buffer file.
2. Calculates the equivalent Base Layout name.
3. Goes to the Layout

(*) Note: It is only possible to go to a base layout if the base table is in the current file.

## Full Syntax

```
[+].Go to Base Layout
```

## Usage

### Go to Base Layout




> ---
> 
> #### Test Case #1 "Go to Base Layout (for this layout)"
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
> [+].Go to Base Layout
> ```
> 
> 
> 
> 


