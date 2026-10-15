<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `View As`

Switch the layout's record view to Form, List or Table.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [View As](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26030) | Yes | ok | v0.54 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].View As
[:]..value = == «calculation»
```

## Usage

### View As




> ---
> 
> #### Test Case #1 "View As"
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
> [+].Set.$view_states = ""
> [+].View As = "Form"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> [+].View As = "List"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> [+].View As = "Table"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> [+].View As = "Cycle"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> [+].View As = "Cycle"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> [+].View As = "Cycle"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> [+].View As = "Cycle"
> [+].Set.$view_states = == List ( $view_states ; Get ( LayoutViewState ) )
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "View As (long form)"
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
> [+].View As
> [:]..value = "Form"
> ```
> 
> 
> 
> 


