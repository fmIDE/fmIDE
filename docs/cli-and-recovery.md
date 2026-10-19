# Connect to FileMaker and recover a stalled run

## Establish the target

Confirm the host, installed `fmide` command and version, FileMaker application and database path. An edited checkout does not automatically replace the installed CLI. Start the intended FileMaker application and open the intended database explicitly. In an agent session, use the available application-control tool; do not guess the frontmost window or send a URL repeatedly to find out.

For a human using Terminal on this Mac, open the intended file explicitly from the repository root:

```sh
open -a "/Applications/FileMaker Pro 26.app" "$PWD/fmIDE.fmp12"
```

Use the actual installed application path. Agents should use their authorized application-control interface to open/check the same target, especially if a dialog needs attention. Then inspect the installed CLI:

```sh
command -v fmide
fmide --version
fmide --help
python3 tools/fmide_run.py tools/probe-context.fmIDEAS \
  --fmp 26 --file fmIDE --database-path "$PWD/fmIDE.fmp12"
```

The last command waits for the context result. Confirm its returned `file_path`, `application_version` and `fmide_release` before doing more work. `-fmp 26` selects that URL protocol. `-file fmIDE` selects the open file name, not a unique filesystem path: a returned path check is still necessary.

For another database, use its actual open filename. The fmIDE script, required custom functions and plugin support must be installed there. Confirm the account can run the script through FMP URLs (`fmurlscript`). Do not change privileges or security settings merely to make an unattended job work.

## Dispatch and collect a response

```sh
fmide -fmp 26 -file fmIDE \
  --frontmatter '$fmide_on_exit_script_write_data_to_folder_path = Get ( DocumentsPath ) & "fmIDE-response-UNIQUE/";' \
  --parameter-file job.fmIDEAS
```

Replace `UNIQUE` with a new request ID. Single quotes keep the shell from expanding `$` variables. Do not reuse a response folder: stale files can look like a new success. The folder must be reachable by FileMaker on the execution host.

Wait for all five files: `script_result.txt`, `last_error.txt`, `last_error_detail.txt`, `last_error_location.txt`, and `last_error_description.txt`. Check the error and parse the promised result type; preserve text results as text. Verify the response's database path and request identity. The CLI exit status only confirms dispatch.

For a single result file, use `$fmide_on_exit_script_write_data_to_file_path`. The folder and file options are output interfaces, not release packaging. Local fmIDE v0.95 includes the #204 correction preserving the synchronous result as well; older copies may return the wrong native result when writing files.

`--dry-run` / `--print-url` are useful for checking CLI construction. They do not validate fmJAML, run calculations or verify FileMaker behavior. CLI frontmatter is trusted FileMaker code; use `Quote` or a proper serializer when constructing it from data.

## When to use another tool

- Use Python for file comparison, hashing, packaging and waiting for completion.
- Use Execute FileMaker Data API for records exposed on a suitable layout; inspect its response `messages` as well as the action error.
- Use native UI control for a script-editor change only when it is explicitly in scope and a fresh backup exists.
- Do not run `Press` editing macros unattended until their behavior has been verified in that FileMaker version and editor state.
- Do not use fmIDEAS to bypass a locked session, missing privileges, a security prompt or an unresolved dispatch.

## Keyboard automation prerequisite

On macOS, `Press` uses MBS keyboard delivery. The executing FileMaker application needs its own enabled entry in **System Settings → Privacy & Security → Accessibility**. The installed FileMaker 26 entry was off in the 14 October 2026 investigation: enabling it with Russell’s approval changed the same Command-A test from error -2 / “Failed to send key” to error 0 and correct script-step selection. [MBS documents the requirement](https://www.mbsplugins.eu/RemoteControlPressKey.shtml).

Inspect permission before changing timing code. Enabling this permission grants computer control and needs explicit approval; macOS may require the user to authenticate locally. A successful selection probe does not validate every editing sequence. `Press.delay` is currently unused ([#205](https://github.com/fmIDE/fmIDE/issues/205)).

## Script-editor focus

A selected step does not prove the keyboard is focused on the script. During the 14 October 2026 native editing session, arrow keys still moved through the Scripts list and Paste stayed disabled. Opening the selected script in its own window with **Command-Shift-T** restored normal editing. Verify the window title, database and selected steps before pasting; save and compare a fresh XML export afterward. This verifies a native GUI workaround, not unattended `Press` editing. [Claris keyboard shortcuts](https://help.claris.com/en/pro-help/content/script-workspace-shortcuts-os-x.html).

## Recovery

1. Retain the source, request ID and response directory. A timeout does not cancel FileMaker.
2. Look for late completion files and read the current application state. Check for an open result card, script pause, debugger, calculation dialog, unsaved edit or locked Mac.
3. Do not send another FileMaker call while the first may still be running. Do useful offline work while waiting.
4. If the session is locked, leave it locked. If a known result card is blocking the job, close that card using its verified button or script; do not dismiss an unknown dialog blindly.
5. Stop/resume a script only after identifying it and understanding whether it has already written data. Never assume a timed-out mutation is safe to retry.
6. Recheck identity and inspect actual records/files before continuing. Use a new request ID for the next distinct job.

Do not force-quit FileMaker, alter security settings or delete pending-response state as a routine recovery strategy. If recovery needs a decision outside the authorized scope, preserve the checkpoint and report the exact blocker.
