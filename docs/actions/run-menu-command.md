<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Run Menu Command`

Invoke a supported FileMaker menu command through the development UI.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | alpha | v0.69 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Run Menu Command
```

## Usage

### Run Menu Command




> ---
> 
> #### Test Case #1 "Run Menu Command (About FileMaker Pro...)"
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
> [+].Run Menu Command = == "FileMaker Pro¶About FileMaker Pro..."
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Run Menu Command (Edit > Select All / 57642)"
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
> [+].Run Menu Command = 57642	// "Edit¶Select All"
> ```
> 
> 
> 
> 


