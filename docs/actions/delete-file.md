<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Delete File`

Delete the file at file_path.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Delete File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26197) | Yes | beta | 0.49 |

## Description

Supply file_path as a calculation for the file to delete.

file_path is evaluated when the action runs. target_file remains a compatibility alias. If file_path is present, it takes precedence even when empty or null; otherwise target_file is used. Only the selected expression is evaluated, once.

The short form expands to file_path.

## Full Syntax

```
[+].Delete File
[:]..file_path = == $FilePath
```

## Usage

### Delete File


Supply file_path as a calculation for the file to delete. Use the canonical file_path parameter; target_file is accepted for compatibility.


> ---
> 
> #### Test Case #1 "Delete File (short form)"
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
> [+].		Delete File = == $FilePath
> ```
> 
> 
> ##### Description
> 
> This test creates a file, pauses for a moment and then deletes it again
> 
> 
> 
> ---
> 
> #### Test Case #2 "Delete File (long form)"
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
> [+].		Delete File
> [:].		.file_path = == $FilePath
> ```
> 
> 
> ##### Description
> 
> This test creates a file, pauses for a moment and then deletes it again
> 
> 
> 


