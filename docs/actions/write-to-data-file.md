<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Write to Data File`

Write a calculated value to an open data file, optionally appending a line feed and choosing text encoding.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Write to Data File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26192) | Yes | beta | 0.49 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Write to Data File
[:]..file_id = == «calculation»
[:]..data_source = == «calculation»
[:]..append_line_feed = == «calculation»

```

## Usage

### Write to Data File




> ---
> 
> #### Test Case #1 "Write to Data File"
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
> [+].	Write to Data File
> [:].	.file_id = == $FileID
> [:].	.data_source = == $timestamp
> [:].	.append_line_feed = true
> ```
> 
> 
> ##### Description
> 
> This writes the current timestamp to the fmIDE_keyboard_buffer.txt file in the documents folder at the position = the current number of seconds
> 
> 
> 


