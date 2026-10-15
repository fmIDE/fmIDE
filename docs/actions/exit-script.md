<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Exit Script`

End the current action script and return the result of the supplied calculation.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Exit Script](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26103) | Yes | ok | <v0.45 |

## Description

Evaluate `script_result`, end the current fmIDE action script, and return the calculated value. The long-form parameter is `script_result`. The scalar short form, `Exit Script = == expression`, supplies that same parameter.

Use `= ==` to preserve an expression for evaluation when Exit Script is reached. To return JSON, use an explicit JSON-producing calculation such as the example below.

### Results for FileMaker callers

After calling fmIDE with Perform Script, read the returned value with `Get ( ScriptResult )`.

### Results for external callers

An fmp URL call is asynchronous. Supply an output modifier variable to write result data before fmIDE exits:

- `$fmide_on_exit_script_write_data_to_file_path`: FileMaker path to the result file.
- `$fmide_on_exit_script_write_data_to_folder_path`: FileMaker folder path ending in `/`. Creates five files: `script_result.txt`, `last_error.txt`, `last_error_detail.txt`, `last_error_location.txt` and `last_error_description.txt`.

The error files contain the corresponding `$$fmide_get_last_error`, `$$fmide_get_last_error_detail`, `$$fmide_get_last_error_location` and `$$fmide_get_last_error_description` values. File output appends a line feed. A completed fmp URL dispatch alone does not establish success; inspect the result and error files.

The local 14 October 2026 fix for [issue #204](https://github.com/fmIDE/fmIDE/issues/204) preserves the native return value when file output is enabled. The result calculation is evaluated once. This has been verified for plain, single-file and five-file output; earlier v0.94 copies without that fix overwrite the native return value in file-output modes.

## Full Syntax

```
[+].Set.$answer = == 42
[+].Exit Script
[:]..script_result = == JSONSetElement ( "{}" ; "answer" ; $answer ; JSONNumber )
```

## Usage

### Exit Script


Exit Script = == «calculation»


> ---
> 
> #### Test Case #1 "[+].Exit Script = == $result"
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
> [+].Exit Script = == $result
> ```
> 
> 
> ##### Description
> 
> [+].Exit Script = == «-fmIDE-calculation editor-space-»
> 
> Use `= ==` to encode a calculation that gets evaluated by fmIDE in context
> 
> 
> 
> ---
> 
> #### Test Case #2 "[+].Exit Script = === «calculation» === (heredoc multiline literal string)"
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
> [+].Exit Script = ===
> JSONSetElement ( "{}" ; "result" ; "[1,2,3]" ; JSONArray )
> ===
> ```
> 
> 
> 
> 

### Exit Script using write data (when called by fmp url)




> ---
> 
> #### Test Case #1 "[+].Exit Script with $fmide_on_exit_script_write_data_to_folder_path"
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
> ---
> $fmide_on_exit_script_write_data_to_folder_path = $$path
> ---
> [+].Set Error Capture = 1
> [+].Re-Login
> [:]..user = "Throw"
> [:]..password = "Error"
> [+].Exit Script = == "There should be a login error number 212"
> 
> ```
> 
> 
> ##### Description
> 
> Writes the script result and error details to a folder using these file names:
> 
> - last_error_location.txt
> - last_error_detail.txt
> - last_error.txt
> - script_result.txt
> 
> 
> 
> ---
> 
> #### Test Case #2 "[+].Exit Script with $fmide_on_exit_script_write_data_to_file_path"
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
> ---
> $fmide_on_exit_script_write_data_to_file_path = $$path
> ---
> [+].Exit Script = == "Hello Baz!"
> 
> ```
> 
> 
> ##### Description
> 
> Writes the script result and error details to a folder:
> 
> - last_error_location.txt
> - last_error_detail.txt
> - last_error.txt
> - script_result.txt
> 
> 
> 

### Exit Script using callback (when called by fmp url)


This is for when fmIDE is called by fmp url. This is an asynchronous call and the caller has no access to the normal ScriptResult.



