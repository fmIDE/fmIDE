<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Object`

Activate a named layout object, optionally at a specified repetition.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Object](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26145) | Yes | beta | v0.1 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Go to Object
[:]..object_name = == «calculation»
[:]..repetition = == «calculation»
```

## Usage

### Go to Object




> ---
> 
> #### Test Case #1 "Go to Object"
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
> [+].Go to Object= == "_gTest"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go to Object .repetition"
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
> [+].Go to Object
> [:]..object_name= == "_gImage"
> [:]..repetition= 2
> 
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Go to NO Object"
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
> [+].Go to Object= == ""
> [+].Commit Records/Requests
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Error: Go to Object"
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
> [+].Go to Object= == "this object does not exist"
> ```
> 
> 
> 
> 


