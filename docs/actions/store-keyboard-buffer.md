<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Store Keyboard Buffer`

Write text to the fmAutoMate keyboard buffer for later insertion with its keyboard shortcut.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | alpha | v0.10 |

## Description

Places the given text in fmAutoMate's Keyboard Buffer file.

The user can then use fmAutoMate's keyboard shortcut (F12 or whatever) to retype the text

Install the fmAutoMate service and use the associated keyboard shortcut to retype the contents of this file.

## Full Syntax

```
[+].Store Keyboard Buffer
```

## Usage

### Store Keyboard Buffer




> ---
> 
> #### Test Case #1 "Store Keyboard Buffer (short form)"
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
> [+].Store Keyboard Buffer = "Store Keyboard Buffer success"
> ```
> 
> 
> 
> 


