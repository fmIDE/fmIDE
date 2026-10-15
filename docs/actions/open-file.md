<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Open File`

Open a FileMaker file using the supported file-opening options.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Open File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26033) | Partial | alpha | v0.53 |

## Description

Emulates the Open File step by calling the fmIDE script in the named file.

## Full Syntax

```
[+].Open File
[:]..file = == «calculation»
[:]..hidden = == «calculation»

```

## Usage

### Open File




> ---
> 
> #### Test Case #1 "Open File FileA"
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
> [+].Open File = == "FileA"
> ```
> 
> 
> ##### Description
> 
> Opens FileA
> 
> 
> 


## See also

- [Close File](close-file.md)
