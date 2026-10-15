<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Else If`

Evaluate another condition in an If block when no earlier condition matched.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Else If](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26125) | Yes | ok | v0.4 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Else If = == «calculation»

# Else If has no long form!
```

## Usage

### Else If




> ---
> 
> #### Test Case #1 "Else If"
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
> [+].Else If=1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Else If 0 Else If 1"
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
> [+].Else If=0
> [+].	Exit Script=2
> [+].Else If=1
> [+].	Exit Script=3
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Else-If (nested)"
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
> [+].	If=1
> ```
> 
> 
> 
> 


## See also

- [If](if.md)
- [Else](else.md)
- [End If](end-if.md)
- [Exit Loop If](exit-loop-if.md)
