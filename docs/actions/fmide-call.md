<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `fmIDE Call`

Run an fmIDE action script in a specified FileMaker file that also contains fmIDE.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | alpha | v0.92 |

## Description

Calls fmIDE in another file and passes an action script (or other fmIDE parameter).

frontmatter can also be passed to define variables or fmide options (like $fmide_debugger = 1)

In the short form, the target file name can be specified directly as a key and the value is the parameter.

## Full Syntax

```
[+].fmIDE Call
[:]..file = == «calculation»
[:]..frontmatter = == «calculation»
[:]..param = == «calculation»
# which can be encoded as a block string (5*`=`!):
[:]..param = =====
Block
of
fmJAML
===
# or even as a json actions array with elegant short array paths:
[:]..param[]
[:][+].Show Custom Dialog = == Get ( FileName )
[:][+].Exit Script = == Get ( FileName )

```

## Usage

### fmIDE Call with string param


Here the parameter for fmIDE is passed as a normal string, just as you would, when calling fmIDE by Perform Script


> ---
> 
> #### Test Case #1 "fmIDE Call → FileA (long form with string param)"
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
> [+].fmIDE Call
> [:]..file = == "FileA"
> [:]..frontmatter = == "$number=2"
> [:]..param = =====
> [+].//Show Custom Dialog = == Get ( FileName )
> [+].Exit Script = == $number & ": " & Get ( FileName )
> ===
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "fmIDE Call → FileA (short form with string param)"
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
> [+].fmIDE Call.FileA = =====
> [+].//Show Custom Dialog = == Get ( FileName )
> [+].Exit Script = == "2: " & Get ( FileName )
> ===
> ```
> 
> 
> ##### Description
> 
> Opens and calls fmIDE in File A to return the number two and the file name. Receives the script result and outputs any error thrown in THIS file
> Important: errors are implemented as $$global (=file) variables: They must thus be passed *explicitly* back in the script result, if needed.
> 
> 
> 

### fmIDE Call with array param


Here the parameter for fmIDE is encoded as an array, which allows the fmJAML to be seemless between the code for the current file and for the remote file


> ---
> 
> #### Test Case #1 "fmIDE Call → FileA (short form with array param)"
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
> [+].fmIDE Call.FileA[]
> [:][+].//Show Custom Dialog = == Get ( FileName )
> [:][+].Set.$log = == "	2 " & Get ( FileName ) & ¶
> [:][+].Exit Script = == $log
> ```
> 
> 
> ##### Description
> 
> Opens and calls fmIDE in File A to return the number two - using the beautifully short path `[:][+].` to build the actions array for FileA
> Important: errors are implemented as $$global (=file) variables: They must thus be passed *explicitly* back in the script result, if needed.
> 
> 
> 

### fmIDE Call within fmIDE Call using array params


Using an array as parameter to fmIDE makes it extremely elegant to write multi-file scripts which seemlessly flow from file to file


> ---
> 
> #### Test Case #1 "fmIDE Call → FileA → FileB (short form with array param)"
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
> [+].fmIDE Call.FileA[]
> [:][+].//Show Custom Dialog = == Get ( FileName )
> [:][+].Set.$log = == "	2.1 " & Get ( FileName ) & ¶
> [:][+].fmIDE Call.FileB[]
> [:][:][+].//Show Custom Dialog = == $log
> [:][:][+].Exit Script = == "		2.2 " & Get ( FileName ) & ¶
> [:][+].Set.$log = == $log & Get ( ScriptResult ) & "	→ LastError: " & $$fmide_get_last_error & ¶
> [:][+].Exit Script = == $log
> ```
> 
> 
> ##### Description
> 
> First calls fmIDE in File A and that calls fmIDE in FileB - using the beautifully short paths to indicate the depth of calls: `[:][+].` for FileA and `[:][:][+].` for FileB
> Important: errors are implemented as $$global (=file) variables: They must thus be passed *explicitly* back in the script result, if needed.
> 
> 
> 


## See also

- [Perform Script](perform-script.md)
