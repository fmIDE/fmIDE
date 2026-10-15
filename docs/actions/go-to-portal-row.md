<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Portal Row`

Navigate to a portal row by position or calculated row number, optionally selecting it.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Portal Row](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26099) | Yes | ok | v0.12 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Go to Portal Row
[:]..by = "First"|"Last"|"Previous"|"Next"|"number"
[:]..row_number = == «calculation»
[:]..select = == «calculation»
```

## Usage

### Go to Portal Row




> ---
> 
> #### Test Case #1 "Go to Portal Row = First (short form )"
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
> [+].Go to Portal Row = "First"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Portal Row.by = First"
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
> [+].Go to Portal Row.by = "First"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Error: Go to Portal Row"
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
> [+].Go to Portal Row
> [:]..row_number=9999999999
> [:]..select=true
> ```
> 
> 
> ##### Description
> 
> This script goes to a portal row that does not exist, and throws an ($$fmide_last_error) error 101.
> 
> 
> 
> ---
> 
> #### Test Case #4 "Error: Go to Portal Row.row = First"
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
> [+].Go to Portal Row.row = "First"
> ```
> 
> 
> ##### Description
> 
> Wrong parameter row was renamed to by
> 
> 
> 

### Go to Portal Row by number




> ---
> 
> #### Test Case #1 "Go to Portal Row = 2 (short form )"
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
> [+].Go to Portal Row = 2
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Portal Row = 1+1 (short form )"
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
> [+].Go to Portal Row = 1+1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Go to Portal Row.row_number"
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
> [+].Go to Portal Row
> [:]..row_number=1
> [:]..select = false
> ```
> 
> 
> 
> 


