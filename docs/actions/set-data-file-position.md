<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Data File Position`

Move the byte position within an open data file.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Data File Position](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26195) | Yes | beta | 0.49 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Set Data File Position
[:]..file_id = == «calculation»

```

## Usage

### Set Data File Position




> ---
> 
> #### Test Case #1 "Set Data File Position"
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
> [+].	Set Data File Position = == $seconds
> ```
> 
> 
> ##### Description
> 
> This writes the current timestamp to the fmIDE_keyboard_buffer.txt file in the documents folder at the position = the current number of seconds
> 
> 
> 


