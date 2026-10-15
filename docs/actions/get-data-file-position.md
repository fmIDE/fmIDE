<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Get Data File Position`

Read the current byte position in an open data file into a target variable or field.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Get Data File Position](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26194) | Yes | beta | 0.49 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Get Data File Position
[:]..file_id = == $FileID
[:]..target = == $position
```

## Usage

### Get Data File Position




> ---
> 
> #### Test Case #1 "Get Data File Position (default Position = 0)"
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
> [+].	Get Data File Position
> [:].	.file_id = == $FileID
> [:].	.target = == $position
> ```
> 
> 
> ##### Description
> 
> This writes the current timestamp to the fmIDE_keyboard_buffer.txt file in the documents folder at the position = the current number of seconds
> 
> 
> 


