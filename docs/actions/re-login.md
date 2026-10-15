<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Re-Login`

Change the current FileMaker session's account using calculated credentials.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Re-Login](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26138) | Yes | beta | v0.52 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Re-Login
[:]..account_name = == «calculation»
[:]..account_password = == «calculation»
```

## Usage

### Re-Login




> ---
> 
> #### Test Case #1 "Re-Login"
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
> [+].	Re-Login
> [:].	.account_name = == "admin"
> [:].	.account_password = == "admin"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Error: Re-Login"
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
> [+].Re-Login
> [:]..account_name = == "Throw"
> [:]..account_password = == "Error"
> ```
> 
> 
> 
> 


