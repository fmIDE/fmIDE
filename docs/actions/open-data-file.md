<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Open Data File`

Open file_path for reading or writing and store its file ID in target.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Open Data File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26191) | Yes | beta | 0.49 |

## Description

Supply file_path as a calculation and target as the output variable or field name. Use the returned file_id for subsequent data-file actions, then close it.

file_path is evaluated when the action runs. source_file remains a compatibility alias. If file_path is present, it takes precedence even when empty or null; otherwise source_file is used. Only the selected expression is evaluated, once.

## Full Syntax

```
[+].Open Data File
[:]..target = "$FileID"
[:]..file_path = == «calculation»
```

## Usage

### Open Data File


Supply file_path as a calculation and target as the output variable or field name. Use the returned file_id for subsequent data-file actions, then close it. Use the canonical file_path parameter; source_file is accepted for compatibility.


> ---
> 
> #### Test Case #1 "Open Data File"
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
> [+].	Open Data File
> [:].	.target = "$FileID"
> [:].	.file_path = == $FilePath
> ```
> 
> 
> ##### Description
> 
> Creates a file, open the file, closes the file
> 
> 
> 
> ---
> 
> #### Test Case #2 "Error: Open Data File (file is locked or in use → 300)"
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
> [+].Open Data File
> [:]..target = "$FileID"
> [:]..file_path = "Get ( FilePath )"
> ```
> 
> 
> ##### Description
> 
> This test tries to open the current file, which is in use, so this automatically throws error 300
> 
> 
> 


