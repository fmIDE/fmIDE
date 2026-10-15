<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Close Data File`

Close an open data file by file ID; omit the ID to use the most recently opened data file.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Close Data File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26196) | Yes | beta | 0.49 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Close Data File
[:]..file_id = == $FileID
```

## Usage

### Close Data File




> ---
> 
> #### Test Case #1 "Data File Test Preperation: Check if any Data Files are open (fails if so)"
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
> [+].Exit Script = "Get ( OpenDataFileInfo )"
> ```
> 
> 
> ##### Description
> 
> This is a test to make sure that all DataFiles are closed, before we continue testing
> 
> 
> 
> ---
> 
> #### Test Case #2 "Data File Test Preperation: Close ALL OPEN Data Files (Loops till all closed)"
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
> [+].Loop
> [+].	Exit Loop If = == IsEmpty ( Get ( OpenDataFileInfo ) )
> [+].	Close Data File
> [+].End Loop
> ```
> 
> 
> ##### Description
> 
> This is not a test, rather closes all open Data Files, before we continue testing
> 
> 
> 
> ---
> 
> #### Test Case #3 "Close Data File"
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
> [+].	Close Data File = == $FileID
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Close Data File (long form)"
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
> [+].	Close Data File
> [:].	.file_id = == $FileID
> ```
> 
> 
> 
> 


## See also

- [Open Data File](open-data-file.md)
- [Read from Data File](read-from-data-file.md)
- [Write to Data File](write-to-data-file.md)
- [Set Data File Position](set-data-file-position.md)
