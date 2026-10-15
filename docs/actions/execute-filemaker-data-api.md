<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Execute FileMaker Data API`

Execute a FileMaker Data API request locally and capture its JSON response; accepts a request calculation or structured request.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Execute FileMaker Data API](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26203) | Yes | beta | v0.13 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Execute FileMaker Data API
[:]..request = == $RequestJSON // specify as a JSON string
[:]..request                   // **or**
[:]...layouts = "fmIDE_Test"   // specify the elements
[:]...limit = 1                // directly / individually
[:]..select = true
[:]..target = == $dapi_result

# `.request` can be specified as a (JSON) string
# or the JSON elements can be specified individually
```

## Usage

### Execute FileMaker Data API




> ---
> 
> #### Test Case #1 "Execute FileMaker Data API (static request)"
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
> [+].Execute FileMaker Data API
> [:]..target = "$result"
> [:]..request.layouts = "fmIDE Test Code"
> [:]..       .limit = 1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Execute FileMaker Data API (dynamic request)"
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
> [+].Execute FileMaker Data API
> [:]..target = "$result"
> [:]..request = ===
> JSONSetElement ( "{}"
> ;["layouts"  ; "fmIDE_Test" ; JSONString]
> ;["limit" ; 1 ; JSONNumber]
> )
> ===
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Execute FileMaker Data API, reduced result"
> 
> ##### Status
> 
> ❌ Fail 
> ✋ manual test 
> 
> 
> ##### Description
> 
> Second (mostly) AI-written fmIDEAS
> 
> 
> 


