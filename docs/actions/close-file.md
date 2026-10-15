<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Close File`

Close the current FileMaker file, or request that fmIDE in another file closes that file.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Close File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26034) | Partial | ok | v0.53 |

## Description

Emulates the Close File script step.

Since the Close File step only supports hard coded file references fmIDE can only close the current file. It implements closing  other files by performing the Close File fmIDE Action in the referenced files.

Supported

- Close current file
- Close externally referenced files, so long as they support fmIDE/contain the fmIDE script

## Full Syntax

```
[+].Close File
[:]..file = == "FileA"
```

## Usage

### Close File Current file




> ---
> 
> #### Test Case #1 "Close File current file (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test ⛔️ HALTS 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Close File
> ```
> 
> 
> ##### Description
> 
> Closes this file
> 
> 
> 

### Close File FileRef




> ---
> 
> #### Test Case #1 "Close File FileA (short form)"
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
> [+].	Close File = == "FileA"
> ```
> 
> 
> ##### Description
> 
> Closes file FileA
> 
> 
> 
> ---
> 
> #### Test Case #2 "Close File FileA (long form)"
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
> [+].	Close File
> [:].	.file = == "FileA"
> ```
> 
> 
> ##### Description
> 
> Closes file FileA
> 
> 
> 


## See also

- [Open File](open-file.md)
