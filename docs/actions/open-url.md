<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Open Url`

Open a calculated URL using the system's associated application.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Open URL](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26111) | Yes | ok | v0.13 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Open Url
```

## Usage

### Open Url




> ---
> 
> #### Test Case #1 "Open Url // manual confirmation required"
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
> [+].Open URL = == "www.mrwatson.de"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Open Url with fmp url (intern) to call fmIDE to inspect a script using the Name that Thing API"
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
> [+].Set.$url= ===
> "fmp://$/fmIDE?script=fmIDE&option=5&$script_name=" & GetAsURLEncoded ( "Test Set $$fmide_script_test ( value )" )
> ===
> [+].Open URL = "$url"
> ```
> 
> 
> ##### Description
> 
> This test calls the fmIDE Script using an fmp url. The trick here is to use the fmp url option parameter (value 5 = Suspend and Resume) to force the fmIDE script to run whilst another script is running (the test script & fmIDE).
> 
> 
> 
> ---
> 
> #### Test Case #3 "Error: Open Url (illegal_protocol → 5)"
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
> [+].Open URL = == "illegal_protocol://www.mrwatson.de"
> ```
> 
> 
> 
> 


