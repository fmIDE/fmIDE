<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `If`

Evaluate a condition and run its branch when true; use the calculation shorthand because a long form is not implemented.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [If](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26068) | Yes | ok | v0.4 |

## Description

Performs the equivalent script step.

Note: `If` currently has no long form.

## Full Syntax

```
[+].If = == «calculation»
```

## Usage

### If




> ---
> 
> #### Test Case #1 "If (long form)"
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
> [+].If.calculation=1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "If (short form)"
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
> [+].If=1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "If-If (nested)"
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
> [+].If=1
> [+].	If=1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "If-Else (nested)"
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
> [+].If=1
> [+].	If=0
> [+].		Exit Script=1
> [+].	Else
> ```
> 
> 
> 
> 


## See also

- [Else If](else-if.md)
- [Else](else.md)
- [End If](end-if.md)
