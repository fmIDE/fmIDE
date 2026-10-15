<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Create Data File`

Create an empty file at a calculated path, optionally creating missing folders.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Create Data File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26190) | Yes | beta | 0.49 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Create Data File
[:]..file_path = == "«file_path»"
[:]..create_folders = «boolean-expression»

```

## Usage

### Create Data File




> ---
> 
> #### Test Case #1 "Create Data File"
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
> [+].Create Data File = == $FilePath
> ```
> 
> 
> ##### Description
> 
> Short form
> 
> 
> 


