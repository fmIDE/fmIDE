<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Get File Exists`

Check whether file_path exists and store the Boolean result in target.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Get File Exists](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26188) | Yes | beta | 0.49 |

## Description

Supply file_path as a calculation and target as the output variable or field name. The result is 1 if the file exists and 0 otherwise.

file_path is evaluated when the action runs. source_file remains a compatibility alias. If file_path is present, it takes precedence even when empty or null; otherwise source_file is used. Only the selected expression is evaluated, once.

The short form expands to file_path. target is a literal destination name, for example "$exists" or "$file_size".

## Full Syntax

```
[+].Get File Exists
[:]..file_path = == $FilePath
[:]..target = "$exists"
```

## Usage

### Get File Exists


Supply file_path as a calculation and target as the output variable or field name. The result is 1 if the file exists and 0 otherwise. Use the canonical file_path parameter; source_file is accepted for compatibility.


> ---
> 
> #### Test Case #1 "Get File Exists"
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
> [+].Get File Exists
> [:]. .file_path = == $FilePath
> [:]. .target = == $exists
> [+].Get File Exists
> [:]. .file_path = == $FilePath & Random
> [:]. .target = == $doesnt_exist
> ```
> 
> 
> ##### Description
> 
> This test checks to see if this file exists and a non-existent neighbouring file exists
> 
> 
> 


