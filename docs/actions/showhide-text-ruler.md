<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Show/Hide Text Ruler`

Show or hide the text ruler using the supported state parameter.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Show/Hide Text Ruler](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26092) | Yes | beta | v0.86 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Show/Hide Text Ruler
[:]..state = "Hide"|"Show"|"Toggle"(default)

```

## Usage

### Show/Hide Text Ruler




> ---
> 
> #### Test Case #1 "Show/Hide Text Ruler (long form)"
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
> [+].Show/Hide Text Ruler
> [:]..state = "Show"
> [+].Show/Hide Text Ruler
> [:]..state = "Hide"
> [+].Set.$TextRulerVisible_hide = == Get ( TextRulerVisible )
> [+].Show/Hide Text Ruler
> [:]..state = "Toggle"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Show/Hide Text Ruler Hide (short form)"
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
> [+].Show/Hide Text Ruler = "Hide"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Show/Hide Text Ruler (short form = toggle)"
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
> [+].Show/Hide Text Ruler
> ```
> 
> 
> 
> 


