# fmIDE Public API Variables ($fmide_*)

fmIDE API variables, which have the form `$fmide_*`, are public variables that allow you to modify or read settings from the fmIDE script and form part of the fmIDE API.

Variables with multiple underscores are [private internal variables](./fmIDE-private-internal-variables.md) that are used internally by the fmIDE script and should not be modified or read directly.

```text
$fmide_debugger // flag to tur the debugger on
$fmide_actions // input/output variable containing the array of fmIDE actions
$fmide_release // output variable containing the fmIDE release string
```

## `$fmide_action` (FIXME Input/Output)

contains the parameters of the current action.

The current action can be referenced and placed in a variable for inspection.

FIXME: TRUE? An action can be passed in.

## `$fmide_actions` (Input/Output)

contains the array of actions.

It can be referenced and placed in a variable or returned for inspection.

## `$$fmide_debug` (Input)

- The level of debugging to use

The higher the level, the more debugging information is displayed (see fmLog357 for details):

- 0 = no debugging
- 3 = debug errors
- 5 = debug information
- 7 = debug trace

## `$fmide_debugger` (Input/Output)

Pass in `$fmide_debugger = 1` to turn the debugger on.

Can be changed mid script.

Can be returned.

## `$$fmide_debug_applescript` (Input/Output)

FIXME

## `$$fmide_debug_log` (Output)

- The debug log

## `$$fmide_debug_script_result` (Input/Output)

- Flag to control debugging of the script result.
- If set to 1, the script result will be logged to the debug log.

## `$fmide_dialog_title` (FIXME Input/Output)

Defined in the script to be FIXME

FIXME Can be passed in.

FIXME Can be used in custom dialogs.

## `$$fmide_get_allow_abort_state` (Input/Output)

- equivalent to Get ( AllowAbortState )
- contains the state of the user abort.

## `$$fmide_get_error_capture_state` (Output)

- equivalent to Get ( ErrorCaptureState )
- contains the state of the error capture.

## `$$fmide_get_last_error` (Output)

- equivalent to Get ( LastError )
- contains the last error number.

## `$$fmide_get_last_error_detail` (Output)

- equivalent to Get ( LastErrorDetail )
- contains the detail text of the last error.

## `$$fmide_get_last_error_location` (Output)

- equivalent to Get ( LastErrorLocation )
- contains the number of the action in the action script where the last error occurred.

## `$$fmide_get_last_message_choice` (Output)

- equivalent to `Get ( LastMessageChoice )
- contains the last key pressed in a custom dialog.

## `$fmide_on_exit_script_write_data_to_file_path` (Input/Output)

Set this FileMaker path to write the script result to the file in utf-8.

## `$fmide_on_exit_script_write_data_to_folder_path` (Input/Output)

Set this FileMaker path to write the script outputs to file in utf-8 in the folder:.

- `script_result.txt`
- `last_error.txt`
- `last_error_description.txt`
- `last_error_detail.txt`
- `last_error_location.txt`

## `$fmide_release` (Output)

The `$fmide_release` variable contains the release string of the fmIDE script

```text
20261005 @mrwatson-de v0.90
```

Can be read and returned

## `$fmide_release_tag` (Output)

The `$fmide_release_tag` variable contains the release-tag of the fmIDE script

```text
v0.90
```

Can be read and returned

## `$fmide_version` (Output)

The `$fmide_version` variable contains the version string of the fmIDE script

```text
0.90
```

Can be read and returned

## `$$fmAutoMate.Search` (Input/Output)

The $$fmAutoMate.Search is the fmAutoMate variable that contains the MBS search string
and is used to coordinate the contents of the MBS script search field and fmAutoMate Search dialogs
