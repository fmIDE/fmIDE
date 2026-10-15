<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Record/Request/Page`

Navigate to a record, find request or preview page by position or calculated number.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Record/Request/Page](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26016) | Yes | ok | v0.5 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Go to Record/Request/Page
[:]..by = "Next"|"Previous"|"number"
[:]..exit_after_last = == «calculation»
[:]..record_number = == «calculation»
```

## Usage

### Go to Record/Request/Page




> ---
> 
> #### Test Case #1 "Go to Record/Request/Page: First/Next/Last/Previous"
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
> [+].Go to Record/Request/Page = "First"
> [+].Go to Record/Request/Page = "Next"
> [+].Go to Record/Request/Page = "Last"
> [+].Go to Record/Request/Page = "Previous"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Record/Request/Page: Exit after Last: Last, Next → Exit"
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
> [+].Go to Record/Request/Page
> [:]..by = "Next"
> [:]..exit_after_last = true
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Error: Go to Record/Request/Page = "Prev" → Fail fast"
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
> [+].Go to Record/Request/Page = "Prev"
> ```
> 
> 
> ##### Description
> 
> Any string inc. "Prev" is interpreted as a calculation -> "?" -> 101 Record is missing
> 
> 
> 

### Go to Record/Request/Page by Calculation




> ---
> 
> #### Test Case #1 "Go to Record/Request/Page: By Calculation (record_number)"
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
> [+].Go to Record/Request/Page
> [:]..by = "number"
> [:]..record_number = "Get ( RecordNumber ) + 6"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Record/Request/Page.record_number"
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
> [+].Go to Record/Request/Page.record_number = == Get ( RecordNumber ) + 6
> ```
> 
> 
> 
> 


