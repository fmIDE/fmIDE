<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Delete Portal Row`

Delete the selected portal row, with optional confirmation.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Delete Portal Row](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26104) | Yes | beta | v0.80 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Delete Portal Row
[:].	.with_dialog = == «calculation»
```

## Usage

### Delete Portal Row




> ---
> 
> #### Test Case #1 "Delete Portal Row without dialog (long form)"
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
> [+].	Delete Portal Row
> [:].	.with_dialog = false
> ```
> 
> 
> 
> 


