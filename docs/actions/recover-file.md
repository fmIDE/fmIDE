<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Recover File`

Recover a FileMaker database at file_path; recovery is distinct from restoring a backup.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Recover File](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26095) | Yes | alpha | v0.86 |

## Description

Performs the equivalent of the Recover File script step. Supply file_path as a calculation for the database to recover. Use a closed copy, not the database currently running this action.

file_path is evaluated when the action runs. file remains a compatibility alias. If file_path is present, it takes precedence even when empty or null; otherwise file is used. Only the selected expression is evaluated, once.

The short form expands to file_path.

Check $$fmide_get_last_error immediately afterwards; $$fmide_get_last_error_detail contains any native error detail.

with_dialog is evaluated once when the action runs and defaults to Off when omitted. On uses FileMaker's recovery dialogs; in FileMaker Pro 26.0.3 with a supplied path, this includes choosing the recovered file destination and viewing the recovery results. Off runs without those dialogs. Without a file path, FileMaker asks for the source file.

An error code of 0 confirms completion, not a clean recovery. Review Recover.log for warnings or repairs.

## Full Syntax

```
[+].Recover File
[:].	.file_path = == «calculation»
[:].	.with_dialog = == «boolean-expression»
```

## Usage

### Recover File


Supply file_path as a calculation for the database to recover. Use a closed copy, not the database currently running this action. Use the canonical file_path parameter; file is accepted for compatibility. Check $$fmide_get_last_error immediately after recovery.

Set with_dialog to a Boolean calculation to show or suppress the native recovery dialogs; the default is Off. Review Recover.log even when the action returns error 0.


> ---
> 
> #### Test Case #1 "Recover File (long form)"
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
> [+].	Recover File
> [:].	.file_path = == $FilePath
> [:].	.with_dialog = false
> ```
> 
> 
> ##### Description
> 
> Recovers a saved copy of fmIDE in a fresh milliseconds-named temporary folder. Checks the final recovery log entry. Fixed source and recovered filenames make the result repeatable across runs.
> 
> 
> 


