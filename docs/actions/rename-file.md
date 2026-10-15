<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Rename File`

Rename file_path to new_name within the same folder.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Rename File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26199) | Yes | beta | v0.80 |

## Description

Supply file_path as a calculation for the existing file and new_name as a calculation for its new filename. new_name is not a destination path.

file_path is evaluated when the action runs. source_file remains a compatibility alias. If file_path is present, it takes precedence even when empty or null; otherwise source_file is used. Only the selected expression is evaluated, once.

## Full Syntax

```
[+].Rename File
[:]..file_path = == «calculation»
[:]..new_name = == «calculation»
```

## Usage

### Rename File


Supply file_path as a calculation for the existing file and new_name as a calculation for its new filename. new_name is not a destination path. Use the canonical file_path parameter; source_file is accepted for compatibility.


> ---
> 
> #### Test Case #1 "Rename File"
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
> [+].Rename File
> [:]..file_path = == $FilePath
> [:]..new_name = == $NewName
> ```
> 
> 
> ##### Description
> 
> Short form
> 
> 
> 


