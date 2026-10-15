<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to Record`

Alias of Go to Record/Request/Page; navigate within the current found set.

[All actions](README.md)


| Alias | FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|---------|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to Record/Request/Page](go-to-recordrequestpage.md)| None | Yes | beta | v0.5 |

## Description

Performs the equivalent script step.

## Full Syntax

```
[+].Go to Record
```

## Usage

### Go to Record




> ---
> 
> #### Test Case #1 "Error: Go to Record/Request/Page (out of bounds → 101)"
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
> [+].Go to Record/Request/Page.number = == Get ( FoundCount ) + 1
> ```
> 
> 
> ##### Description
> 
> Going to a record beyond the end of the found count throws an error but also takes you to the last record
> 
> 
> 
> ---
> 
> #### Test Case #2 "Error: Test error handling only when first thrown"
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
> [+].Go to Record/Request/Page.by_calculation = "Get ( FoundCount ) + 1"
> [+].If = 0 /* this should NOT report an error */
> [+].End If
> [+].Exit Script = "Get ( RecordNumber ) = Get ( FoundCOunt )"
> ```
> 
> 
> ##### Description
> 
> Going to a record beyond the end of the found count throws an error but also takes you to the last record
> 
> 
> 


