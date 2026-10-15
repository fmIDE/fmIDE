<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Omit Multiple Records`

Remove a specified number of records from the found set without deleting them.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Omit Multiple Records](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26026) | Yes | alpha | v0.79 |

## Description

Performs the equivalent script step.

Default is without dialog.

## Full Syntax

```
[+].Omit Multiple Records
[:]..calculation = == «calculation»
[:]..with_dialog = == «calculation»

```

## Usage

### Omit Multiple Records




> ---
> 
> #### Test Case #1 "Omit Multiple Records (long form)"
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
> [+].Omit Multiple Records
> [:]..calculation = == Get( FoundCount )+1 - Get ( RecordNumber )
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Omit Multiple Records = 1 (short form )"
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
> [+].Omit Multiple Records = 1
> ```
> 
> 
> 
> 


## See also

- [Omit Record](omit-record.md)
- [Show Omitted Only](show-omitted-only.md)
- [Show All Records](show-all-records.md)
