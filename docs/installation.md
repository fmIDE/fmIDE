# Install and check fmIDE

Open the demo file in the intended FileMaker application. The current development workflow is verified on macOS with FileMaker 26.0.3 and MBS. Macros and Configure Persistent Data require FileMaker 26; other action requirements vary. This is not a claim that every action is portable to every FileMaker version or Windows.

For another solution, copy the **fmIDE Module** script folder and the required custom functions from the current demo file, then check references. Adapt the callback scripts to the solution's base-table and layout naming conventions before distributing that configuration to its other files.

The script can be called directly. To use FMP URLs, the account needs the `fmurlscript` extended privilege. The solution owner should decide that access; agents should not silently grant it.

MBS powers much of the developer-interface navigation. Verify the installed plugin and the specific action on the execution host. The older Retype Keyboard Buffer service and fmAutoMate integrations are described in the [original installation notes](wiki/installation-history.md); they are not a substitute for testing the current action.

On macOS, enable **the FileMaker Pro application that runs fmIDE** in **System Settings → Privacy & Security → Accessibility**. MBS keyboard actions, including [Press](actions/press.md), require this permission. Check the correct application entry when switching or installing FileMaker versions. See [keyboard automation setup](cli-and-recovery.md#keyboard-automation-prerequisite).

For command-line use, install [fmIDE-CLI](https://github.com/fmIDE/fmIDE-CLI), then follow [CLI and recovery](cli-and-recovery.md). Confirm the installed command's version and help. The CLI and fmIDE database are separate installations.

Start with the read-only context probe, confirm the returned database path and release, and then test a simple known navigation such as `Hello World`. A successful URL launch alone does not establish that the intended database received it.

See [development](development.md) before changing the demo file, and [Name that Thing](name-that-thing.md) for the API.
