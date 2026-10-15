<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Else`

Start the alternative branch of an If block when no earlier condition matched.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Else](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26069) | Yes | ok | v0.4 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Else
```

## Usage

### Else




> ---
> 
> #### Test Case #1 "Else"
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
> [+].Else
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Else-Else (nested)"
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
> [+].Else
> [+].	If=0
> [+].		Exit Script=3
> [+].	Else
> ```
> 
> 
> 
> 


## See also

- [If](if.md)
- [Else If](else-if.md)
- [End If](end-if.md)
