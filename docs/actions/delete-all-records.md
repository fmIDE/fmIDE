<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Delete All Records`

Delete every record in the current found set; confirmation is enabled by default.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Delete All Records](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26010) | Yes | beta | v0.79 |

## Description

Performs the equivalent script step.

Default is with dialog.

## Full Syntax

```
[+].Delete All Records
[:]..with_dialog = == «calculation»

```

## Usage

### Delete All Records




> ---
> 
> #### Test Case #1 "Delete All Records without dialog (Long form)"
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
> [+].	Delete All Records
> [:].	.with_dialog = false
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Delete All Records default (short form) = default with dialog"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].	Delete All Records
> ```
> 
> 
> 
> 


