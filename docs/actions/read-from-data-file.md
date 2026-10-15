<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Read from Data File`

Read a specified amount from an open data file into a target variable or field.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Read from Data File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26193) | Yes | beta | 0.49 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Read from Data File
[:]..target = "$bytes"
[:]..file_id = "$FileID"
[:]..read_as = "bytes"|FIXME
[:]..amount = == «calculation»

```

## Usage

### Read from Data File




> ---
> 
> #### Test Case #1 "Read from Data File (bytes)"
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
> [+].	Read from Data File
> [:].	.file_id = "$FileID"
> [:].	.target = "$bytes"
> [:].	.read_as = "bytes"
> [:].	.amount = "3+9"
> ```
> 
> 
> ##### Description
> 
> This reads the first 12 bytes of the Import.log file that sits next to the fmIDE.fmp12 file. THIS TEST ONLY WORKS WHEN THIS FILE IS PRESENT!
> The Import.log file is a UTF-8 text file with a 3 byte UTF BOM at the start, which means the first 9 letters, `Timestamp` should be read.
> 
> 
> 


