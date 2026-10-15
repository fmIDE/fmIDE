<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Perform Script`

Run a FileMaker script with an optional parameter; the target file must be available.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Perform Script](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26001) | Yes | beta | v0.31 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Perform Script
[:]..by = "name"|"selected"
[:]..file_name = «string»
[:]..script_name = «string» (or = == «calculation» when .by = "name")
[:]..script_parameter = == «calculation»

```

## Usage

### Perform Script selected script




> ---
> 
> #### Test Case #1 "Perform Script (short form)"
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
> [+].Perform Script = "Test Return 1"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Perform Script.= "name""
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
> [+].Perform Script
> [:]..by = "name"
> [:]..script_name = == "Test Return 1"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Perform Script with script_parameter"
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
> [+].Perform Script
> [:]..script_name = "Test Return ScriptParameter"
> [:]..script_parameter = == $random
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Error: Perform Script (unknown script)"
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
> [+].Perform Script.script_name="adifhdaiufhadslfkhadsfhd"
> ```
> 
> 
> 
> 

### Perform Script by script_name




> ---
> 
> #### Test Case #1 "Perform Script.script_name"
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
> [+].Perform Script
> [:]..script_name = "Test Return 2"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Error: Perform Script.specified= "By name""
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
> [+].Set Error Capture = 1
> [+].Perform Script
> [:]..specified = "By name"
> [:]..script_name = == "Test Return 1"
> ```
> 
> 
> ##### Description
> 
> Wrong parameter specified was renamed to by -> this leads to an error Script is missing INSTEAD of a parameter or calculation error
> Since there is no `by` parameter, fmIDE is trying to find script `"Test Return 1"` - including the quotes - and failing - correctly - with a script not found error
> 
> 
> 

### Perform Script ( external file )




> ---
> 
> #### Test Case #1 "Perform Script.file_name"
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
> [+].Perform Script
> [:]..file_name = "FileA"
> [:]..script_name = "Test Return FileName"
> ```
> 
> 
> 
> 


## See also

- [fmIDE Call](fmide-call.md)
