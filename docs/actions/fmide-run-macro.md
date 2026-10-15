<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `fmIDE Run Macro`

Execute a stored macro with optional frontmatter; an unknown macro reports error 1700. Requires FileMaker 26.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.56 |

## Description

Execute code from the file's `fmide_macros` persistent store (FileMaker 26 or later). Read the nested script result immediately with `Get ( ScriptResult )`.

- `macro_name`: a calculation returning the name; a dotted action-key name is literal shorthand.
- `frontmatter`: an optional calculation returning variable definitions. The calculation runs once in the caller; its definitions run when the macro starts.

Supplied frontmatter is inserted before any stored frontmatter. Both blocks are retained, and a final semicolon on the supplied block is optional. Stored definitions run after supplied definitions, so later assignments to the same variable take precedence.

A missing or empty name reports error 5. An unknown macro reports error 1700. Check `$$fmide_get_last_error` when error capture is enabled.

## Full Syntax

```
# Run an existing macro and return its result.
[+].fmIDE Run Macro.Example
[+].Exit Script = == Get ( ScriptResult )

# Separate invocation: pass input definitions to the macro.
# [+].fmIDE Run Macro
# [:]..macro_name = == "Example"
# [:]..frontmatter = ==== $name = "Russell"
# [+].Exit Script = == Get ( ScriptResult )
```

## Usage

### fmIDE Run Macro




> ---
> 
> #### Test Case #1 "fmIDE Run Macro HelloWorld"
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
> [+].fmIDE Run Macro.HelloWorld = ==== $name = "you"
> [+].Exit Script = == Get ( ScriptResult )
> ```
> 
> 
> ##### Description
> 
> Format is
> [+].fmIDE Define Macro.«macro_name» = ==== «macro-fmJAML-code»
> [+].fmIDE Run Macro.«macro_name» = ==== «frontmatter-var-def»
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "fmIDE Run Macro Echo"
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
> [+].fmIDE Run Macro.Echo = ==== $script_parameter = "hello"
> ```
> 
> 
> ##### Description
> 
> Format is
> [+].fmIDE Define Macro.«macro_name» = ==== «macro-fmJAML-code»
> [+].fmIDE Run Macro.«macro_name» = ==== «frontmatter-var-def»
> 
> 
> 
> 


