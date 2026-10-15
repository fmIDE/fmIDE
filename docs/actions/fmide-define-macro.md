<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `fmIDE Define Macro`

Store named, reusable fmIDEAS code with optional metadata in the fmide_macros persistent store. Requires FileMaker 26.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta | v0.56 |

## Description

Store reusable fmIDEAS code in the file's `fmide_macros` persistent store (FileMaker 26 or later).

- `macro_name`: a calculation returning a non-empty name. A dotted name in the action key is literal shorthand.
- `code`: a calculation returning fmJAML or JSON action-script text. It is evaluated once when Define runs; the resulting text is stored.
- `metadata`: an optional JSON object, stored as data rather than reevaluated when the macro runs.

Defining an existing name replaces the whole macro, including its metadata. A missing or empty name reports error 5. Use explicit `macro_name` for names containing reserved parameter words. Use Get Macro to inspect the stored object.

## Full Syntax

```
# Literal name in the key; the here-text becomes the stored code.
[+].fmIDE Define Macro.Example = =====
[+].Exit Script = == "Hello"
=====

# Equivalent long form, with optional metadata.
[+].fmIDE Define Macro
[:]..macro_name = == "Example"
[:]..code = =====
[+].Exit Script = == "Hello"
=====
[:]..metadata.description = "Greeting example"
```

## Usage

### fmIDE Define Macro




> ---
> 
> #### Test Case #1 "fmIDE Define Macro HelloWorld"
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
> [+].fmIDE Define Macro.HelloWorld = =====
> [+].Show Custom Dialog
> [:]..message = == "Hello " & Case ( not IsEmpty ( $name ) ; $name ; "World" )
> [:]..buttons[+] = == "Hello"
> [:]..         ] = == "Hi"
> [:]..         ] = == "Bye"
> [+].Exit Script = == Get ( LastMessageChoice )
> ===
> ```
> 
> 
> 
> 


