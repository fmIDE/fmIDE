<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go to List of Records`

Open a list of records on the current or specified layout, optionally in a new document window; layout animation is unsupported.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Go to List of Records](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26228) | Partial | beta | v0.53 |

## Description

Performs the equivalent script step.

Supported

- Current Layout or selected Layout
- New document window

Not supported

- Layout animation

## Full Syntax

```
[+].Go to List of Records
```

## Usage

### Go to List of Records




> ---
> 
> #### Test Case #1 "Go to List of Records (this record)"
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
> [+].Go to List of Records = == Get ( RecordID )
> ```
> 
> 
> ##### Description
> 
> Needs FileMaker 22+
> 
> 
> 


