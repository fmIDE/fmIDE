<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Get File Size`

Read the size of file_path in bytes and store it in target.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Get File Size](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26189) | Yes | beta | v0.49 |

## Description

Supply file_path as a calculation and target as the output variable or field name. The result is the file size in bytes.

file_path is evaluated when the action runs. source_file remains a compatibility alias. If file_path is present, it takes precedence even when empty or null; otherwise source_file is used. Only the selected expression is evaluated, once.

The short form expands to file_path. target is a literal destination name, for example "$exists" or "$file_size".

## Full Syntax

```
[+].Get File Size
[:]..file_path = == $FilePath
[:]..target = "$file_size"
```

## Usage

### Get File Size


Supply file_path as a calculation and target as the output variable or field name. The result is the file size in bytes. Use the canonical file_path parameter; source_file is accepted for compatibility.


> ---
> 
> #### Test Case #1 "Get File Size"
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
> [+].Get File Size
> [:]. .file_path = == $FilePath
> [:]. .target = == $file_size
> ```
> 
> 
> ##### Description
> 
> This test returns the size of this file and checks that it is  > million bytes
> 
> 
> 


