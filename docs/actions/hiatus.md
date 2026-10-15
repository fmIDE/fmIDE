<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Hiatus`

Halt execution and later resume the remaining actions; the original calling script is not resumed.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | dev | v0.74 |

## Description

A pause but where NO script is running.

Action flow halts and restarts after the pause.

Note that the script that called the fmIDE action script is not continued

## Full Syntax

```
[+].Hiatus
[:]..duration = == «calculation»
```

## Usage

### Hiatus




> ---
> 
> #### Test Case #1 "Hiatus 1 (Short Form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test ⏏️ uses HIATUS ⛔️ HALTS 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Hiatus = 1
> ```
> 
> 
> ##### Description
> 
> Hiatus can only be tested manually. Whilst it maintains the **fmIDE** call stack, it loses the FileMaker call stack.
> The test only 'completes', because the fmIDEAS itself performs the post test completion work :D
> 
> 
> 


