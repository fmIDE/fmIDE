> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.

> The original local-variable lifetime warning is unresolved. Inspect the current continuation implementation before relying on values across a hiatus.

fmIDE must sometimes halt in the middle of an action script - to free up the FileMaker GUI - before continuing with the rest of the action script.

Such a momentary pause/interruption is called a **Hiatus**.

A Hiatus is used in the `Go to Custom Function` and `Go to Custom Menu` actions to access their otherwise unavailable menu commands (Since there is no script step in FileMaker and the menu items are greyed out while a script is running or even when it is paused

# Important to know

Any local script variables do not survive a Hiatus. (FIXME - is that still true?)

# How does it work?

fmIDE Hiatus is quite magical!

An action Hiatus works using a **'continuation' object**.

1. All necessary runtime variables are packed as a JSON `continuation` object
2. A timer is set up to restart the script in a moment, passing the JSON `continuation` object
3. The script is halted
4.  :
5. The script is restarted
6. The `continuation` object is received and the runtime variables are set up
7. The processing of the action script continues at exactly where it left off!

Magic! ✨
