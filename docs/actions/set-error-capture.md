<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Error Capture`

Control fmIDE error dialogs. Capturing errors does not stop execution; check $$fmide_get_last_error explicitly.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Error Capture](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26086) | Yes | beta | v0.48 |

## Description

Syntax ok, but behaviour might change

## Full Syntax

```
[+].Set Error Capture
```

## Usage

### Set Error Capture




> ---
> 
> #### Test Case #1 "Set Error Capture=1 (on)"
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
> [
> 	{
> 		"Set Error Capture" : 1
> 	},
> 	{
> 		"Exit Script" : "$$fmide_get_error_capture_state"
> 	}
> ]
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Error Capture=0 (off)"
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
> [
> 	{
> 		"Set Error Capture" : 1
> 	},
> 	{
> 		"Set Error Capture" : 0
> 	},
> 	{
> 		"Exit Script" : "$$fmide_get_error_capture_state"
> 	}
> ]
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #3 "Set Error Capture="" (off)"
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
> [
> 	{
> 		"Set Error Capture" : 1
> 	},
> 	{
> 		"Set Error Capture" : ""
> 	},
> 	{
> 		"Exit Script" : "$$fmide_get_error_capture_state"
> 	}
> ]
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Set Error Capture= (off)"
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
> [
> 	{
> 		"Set Error Capture" : 1
> 	},
> 	{
> 		"Set Error Capture" : null
> 	},
> 	{
> 		"Exit Script" : "$$fmide_get_error_capture_state"
> 	}
> ]
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Set Error Capture (off)"
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
> [
> 	{
> 		"Set Error Capture" : 1
> 	},
> 	{
> 		"Set Error Capture" : null
> 	},
> 	{
> 		"Exit Script" : "$$fmide_get_error_capture_state"
> 	}
> ]
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #6 "Set Error Capture=2 (on) // allowed value because GetAsBoolean( … ) = 1"
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
> [
> 	{
> 		"Set Error Capture" : 2
> 	},
> 	{
> 		"Exit Script" : "$$fmide_get_error_capture_state"
> 	}
> ]
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #7 "Set Error Capture=1 (on)"
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
> [+].Set Error Capture=1
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #8 "Set Error Capture=2 (on)"
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
> [+].Set Error Capture = 2
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #9 "Set Error Capture=0 (off)"
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
> [+].Set Error Capture=0
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #10 "Set Error Capture="" (off)"
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
> [+].Set Error Capture = ""
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #11 "Set Error Capture= (off)"
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
> [+].Set Error Capture = 1
> [+].Set Error Capture =
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #12 "Set Error Capture (off)"
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
> [+].Set Error Capture =
> ```
> 
> 
> 
> 


