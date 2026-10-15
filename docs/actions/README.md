<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# fmIDE Actions

Short descriptions for people and AI agents. Each action links to its current Wiki detail, syntax, usage examples and recorded test results.

In fmJAML, `= == expression` preserves calculation text for fmIDE to evaluate when the action runs. A single `=` can evaluate it earlier, while fmJAML builds the action script. Data-processing specifiers do not format later fmIDE results.

Support and development-state values come from the Actions table. Recorded test results are snapshots, not a guarantee that every option works. Removed and proposed actions remain listed and are identified in their summaries.

| Action | Summary | FileMaker script step | Support | State | Introduced |
| --- | --- | --- | --- | --- | --- |
| [`#`](comment.md) | Add a comment to an action script; fmIDE ignores its content. |  | Yes | ok | v0.3 |
| [`Adjust Window`](adjust-window.md) | Resize or arrange the current window using the requested adjustment. | Adjust Window | Yes | ok | v0.53 |
| [`Allow User Abort`](allow-user-abort.md) | Control whether the user can interrupt the running action script. | Allow User Abort | Yes | ok | 0.42 |
| [`Assert`](assert.md) | Removed action; retained here for reference to older action scripts. |  | REMOVED | deleted | v0.42 |
| [`Beep`](beep.md) | Play the system alert sound. | Beep | Yes | ok | v0.3 |
| [`Clear`](clear.md) | Delete the current selection or active field contents. An explicit target is not yet supported. | Clear | Partial | alpha | v0.53 |
| [`Close Data File`](close-data-file.md) | Close an open data file by file ID; omit the ID to use the most recently opened data file. | Close Data File | Yes | beta | 0.49 |
| [`Close File`](close-file.md) | Close the current FileMaker file, or request that fmIDE in another file closes that file. | Close File | Partial | ok | v0.53 |
| [`Close Popover`](close-popover.md) | Close the currently open popover. | Close Popover | Yes | ok |  |
| [`Close Script Workspace`](close-script-workspace.md) | Close the Script Workspace through the development UI. |  | Yes | dev | 0.44 |
| [`Close Window`](close-window.md) | Close the selected or named FileMaker window. | Close Window | Yes | alpha | v0.76 |
| [`Commit`](commit.md) | Alias of Commit Records/Requests; save pending record or find-request changes. |  | Yes | alpha |  |
| [`Commit Records`](commit-records.md) | Alias of Commit Records/Requests; save pending record or find-request changes. |  | Partial | alpha |  |
| [`Commit Records/Requests`](commit-recordsrequests.md) | Save pending changes to the current record or find request, with optional confirmation. | Commit Records/Requests | Yes | alpha |  |
| [`Configure Persistent Data`](configure-persistent-data.md) | Store or delete a value by instance ID in the fixed fmIDE persistent store. Requires FileMaker 26. | Configure Persistent Data | Partial | beta | v0.56 |
| [`Constrain Found Set`](constrain-found-set.md) | Apply the current find requests within the existing found set. | Constrain Found Set | Yes | beta | v0.35.1 |
| [`Convert Clipboard`](convert-clipboard.md) | Convert supported FileMaker clipboard content between its available representations. |  | Yes | beta |  |
| [`Copy`](copy.md) | Copy the current selection to the clipboard. | Copy | Partial | alpha | 0.44 |
| [`Copy All Records/Requests`](copy-all-recordsrequests.md) | Copy the found records or find requests to the clipboard. | Copy All Records/Requests | Yes | alpha | v0.80 |
| [`Copy Record/Request`](copy-recordrequest.md) | Copy the current record or find request to the clipboard. | Copy Record/Request | Yes | alpha | v0.80 |
| [`Copy Script`](copy-script.md) | Select a script and copy it from the Script Workspace. This action is still in development. |  | Yes | dev | 0.44 |
| [`Create Data File`](create-data-file.md) | Create an empty file at a calculated path, optionally creating missing folders. | Create Data File | Yes | beta | 0.49 |
| [`Cut`](cut.md) | Move the current selection to the clipboard. An explicit target is not yet supported. | Cut | Partial | alpha | v0.53 |
| [`Delete All Records`](delete-all-records.md) | Delete every record in the current found set; confirmation is enabled by default. | Delete All Records | Yes | beta | v0.79 |
| [`Delete File`](delete-file.md) | Delete the file at file_path. | Delete File | Yes | beta | 0.49 |
| [`Delete Portal Row`](delete-portal-row.md) | Delete the selected portal row, with optional confirmation. | Delete Portal Row | Yes | beta | v0.80 |
| [`Delete Record/Request`](delete-recordrequest.md) | Delete the current record or find request, with optional confirmation. | Delete Record/Request | Yes | ok | v0.53 |
| [`Duplicate Record/Request`](duplicate-recordrequest.md) | Duplicate the current record or find request. | Duplicate Record/Request | Yes | alpha | v0.80 |
| [`Edit User Dictionary`](edit-user-dictionary.md) | Open FileMaker's user dictionary editor. | Edit User Dictionary | Yes | alpha | v0.80 |
| [`Else`](else.md) | Start the alternative branch of an If block when no earlier condition matched. | Else | Yes | ok | v0.4 |
| [`Else If`](else-if.md) | Evaluate another condition in an If block when no earlier condition matched. | Else If | Yes | ok | v0.4 |
| [`End If`](end-if.md) | End the current If block. | End If | Yes | ok | v0.4 |
| [`End Loop`](end-loop.md) | Return to the start of the current Loop block. | End Loop | Yes | ok | v0.4 |
| [`Enter Browse Mode`](enter-browse-mode.md) | Switch the current window to Browse mode. | Enter Browse Mode | Yes | ok |  |
| [`Enter Find Mode`](enter-find-mode.md) | Switch to Find mode to build find requests, with optional pause. | Enter Find Mode | Yes | beta |  |
| [`Enter Layout Mode`](enter-layout-mode.md) | Switch the current window to Layout mode. |  | Yes | alpha |  |
| [`Enter Preview Mode`](enter-preview-mode.md) | Switch the current window to Preview mode, with optional pause. | Enter Preview Mode | Yes | beta |  |
| [`Execute FileMaker Data API`](execute-filemaker-data-api.md) | Execute a FileMaker Data API request locally and capture its JSON response; accepts a request calculation or structured request. | Execute FileMaker Data API | Yes | beta | v0.13 |
| [`Exit Application`](exit-application.md) | Quit FileMaker Pro. | Exit Application | Yes | ok | v0.53 |
| [`Exit Loop If`](exit-loop-if.md) | Leave the current Loop block when the supplied calculation evaluates to true. | Exit Loop If | Yes | ok | v0.4 |
| [`Exit Script`](exit-script.md) | End the current action script and return the result of the supplied calculation. | Exit Script | Yes | ok | <v0.45 |
| [`Extend Found Set`](extend-found-set.md) | Add records matching the current find requests to the existing found set. | Extend Found Set | Yes | beta | v0.35.1 |
| [`Find Script Step`](find-script-step.md) | Search script steps in the Script Workspace using MBS; requires macOS and the MBS plugin. |  | Yes | beta |  |
| [`Flush Cache to Disk`](flush-cache-to-disk.md) | Write FileMaker's cached changes to disk. | Flush Cache to Disk | Yes | alpha | v0.80 |
| [`Freeze Window`](freeze-window.md) | Suspend window redraws while subsequent actions run. | Freeze Window | Yes | ok | 0.44 |
| [`Get Data File Position`](get-data-file-position.md) | Read the current byte position in an open data file into a target variable or field. | Get Data File Position | Yes | beta | 0.49 |
| [`Get Field Names`](get-field-names.md) | Deprecated; use FileMaker calculation functions to obtain field names. |  | Deprecated | ok |  |
| [`Get File Exists`](get-file-exists.md) | Check whether file_path exists and store the Boolean result in target. | Get File Exists | Yes | beta | 0.49 |
| [`Get File Size`](get-file-size.md) | Read the size of file_path in bytes and store it in target. | Get File Size | Yes | beta | v0.49 |
| [`Get Version`](get-version.md) | Removed; use Exit Script with the calculation $fmide_version to return the fmIDE version. |  | REMOVED | deleted | v0.8 |
| [`Go To Base Field`](go-to-base-field.md) | Open Manage Database for a field in the current file and prepare its name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | beta |  |
| [`Go to Account`](go-to-account.md) | Open Manage Security and prepare an account name in the fmAutoMate keyboard buffer for manual selection. |  | Yes | beta | v0.10 |
| [`Go to Base Layout`](go-to-base-layout.md) | Resolve and open the base layout for a table in the current file. |  | Partial | beta |  |
| [`Go to Base Table`](go-to-base-table.md) | Open Manage Database for a table in the current file and prepare its name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | beta | v0.12 |
| [`Go to Custom Function`](go-to-custom-function.md) | Open Manage Custom Functions and prepare the function name for manual selection; uses macOS, MBS and a hiatus. |  | Yes | beta | v0.12 |
| [`Go to Custom Menu`](go-to-custom-menu.md) | Open Manage Custom Menus and prepare the menu name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | alpha | v0.12 |
| [`Go to Custom Menu Item`](go-to-custom-menu-item.md) | Open Manage Custom Menus and prepare an item name; opening its menu and selecting the item remain manual. |  | Yes | alpha | v0.12 |
| [`Go to Custom Menu Set`](go-to-custom-menu-set.md) | Open Manage Custom Menus and prepare a menu-set name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | alpha | v0.12 |
| [`Go to Extended Privilege`](go-to-extended-privilege.md) | Open Manage Security and prepare an extended-privilege name; select the relevant panel and entry manually. |  | Yes | alpha | v0.12 |
| [`Go to External Data Source`](go-to-external-data-source.md) | Open Manage External Data Sources and prepare the source name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | beta | v0.12 |
| [`Go to Field`](go-to-field.md) | Alias of Go to Layout Field; attempts to activate a layout field using AppleScript on macOS. | Go to Field | Partial | alpha | v0.15 |
| [`Go to File Access`](go-to-file-access.md) | Open Manage Security for File Access; navigation within the dialog remains manual. |  | Yes | alpha | v0.75 |
| [`Go to File Authorization`](go-to-file-authorization.md) | Intended alias of Go to File Access; the current action-name dispatch has a known inconsistency. |  | Yes | alpha | v0.75 |
| [`Go to Layout`](go-to-layout.md) | Navigate to a layout by name, number, ID or original layout; shorthand text denotes a name and shorthand numbers denote a layout number. | Go to Layout | Yes | beta | v0.1 |
| [`Go to Layout Field`](go-to-layout-field.md) | Attempt to activate a field on the current layout using AppleScript on macOS; visual focus is not always updated. |  | Partial | alpha | v0.12 |
| [`Go to Layout Part`](go-to-layout-part.md) | Proposed action; layout-part navigation is not implemented. |  | Idea | idea | v0.18 |
| [`Go to List of Records`](go-to-list-of-records.md) | Open a list of records on the current or specified layout, optionally in a new document window; layout animation is unsupported. | Go to List of Records | Partial | beta | v0.53 |
| [`Go to Next Field`](go-to-next-field.md) | Move focus to the next field in the layout's tab order. | Go to Next Field | Yes | ok | v0.12 |
| [`Go to Object`](go-to-object.md) | Activate a named layout object, optionally at a specified repetition. | Go to Object | Yes | beta | v0.1 |
| [`Go to Original Layout`](go-to-original-layout.md) | Removed; use Go to Layout with by set to original. |  | REMOVED | deleted | v0.6 |
| [`Go to Original Window`](go-to-original-window.md) | Removed; use Select Window to select the required window. |  | REMOVED | deleted | 0.7 |
| [`Go to Portal Row`](go-to-portal-row.md) | Navigate to a portal row by position or calculated row number, optionally selecting it. | Go to Portal Row | Yes | ok | v0.12 |
| [`Go to Previous Field`](go-to-previous-field.md) | Move focus to the previous field in the layout's tab order. | Go to Previous Field | Yes | ok | v0.12 |
| [`Go to Privilege Set`](go-to-privilege-set.md) | Open Manage Security and prepare a privilege-set name for manual selection; this action halts script execution. |  | Yes | ok | v0.12 |
| [`Go to Record`](go-to-record.md) | Alias of Go to Record/Request/Page; navigate within the current found set. |  | Yes | beta | v0.5 |
| [`Go to Record/Request/Page`](go-to-recordrequestpage.md) | Navigate to a record, find request or preview page by position or calculated number. | Go to Record/Request/Page | Yes | ok | v0.5 |
| [`Go to Script`](go-to-script.md) | Open a script and focus its steps; can combine initial step selection, step search and subsequent selection extension. UI automation requires macOS and MBS. |  | Yes | ok | v0.1 |
| [`Go to Script Step`](go-to-script-step.md) | Navigate to a step in the Script Workspace; negative step numbers count from the end. Requires macOS and MBS. |  | Yes | ok | v0.1 |
| [`Go to Table`](go-to-table.md) | Navigate toward a table definition using the shared table-navigation actions; this action is still in development. |  | Yes | dev | v0.3 |
| [`Go to Table Occurrence`](go-to-table-occurrence.md) | Open Manage Database and prepare a table-occurrence name; select it manually in the Relationships graph. |  | Yes | alpha | v0.12 |
| [`Go to Theme`](go-to-theme.md) | Open Manage Themes and prepare the theme name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | ok | v0.12 |
| [`Go to Value List`](go-to-value-list.md) | Open Manage Value Lists and prepare the value-list name in the fmAutoMate keyboard buffer; final selection is manual. |  | Yes | ok | v0.12 |
| [`Halt Script`](halt-script.md) | Stop all currently running scripts, including the caller. | Halt Script | Yes | ok |  |
| [`Hello`](hello.md) | Display a greeting dialog to check that fmIDE can receive and execute an action. |  | Yes | ok | v0.8 |
| [`Hiatus`](hiatus.md) | Halt execution and later resume the remaining actions; the original calling script is not resumed. |  | Yes | dev | v0.74 |
| [`If`](if.md) | Evaluate a condition and run its branch when true; use the calculation shorthand because a long form is not implemented. | If | Yes | ok | v0.4 |
| [`Insert Calculated Result`](insert-calculated-result.md) | Insert a calculation result into the specified target or current selection. | Insert Calculated Result | Yes | beta | v0.45 |
| [`Insert Text`](insert-text.md) | Insert literal text into the current selection or supported target. | Insert Text | Yes | beta | v0.46 |
| [`Insert from URL`](insert-from-url.md) | Retrieve data from a calculated URL into a target, with supported request options. | Insert from URL | Yes | ok | v0.25 |
| [`Install OnTimer Script`](install-ontimer-script.md) | Schedule a script to run repeatedly in the current window at the calculated interval. | Install OnTimer Script | Yes | beta |  |
| [`Loop`](loop.md) | Start a repeated block of actions; pair with End Loop and an exit condition. | Loop | Yes | ok | v0.4 |
| [`Modify Last Find`](modify-last-find.md) | Restore the last find requests for editing. | Modify Last Find | Yes | ok | v0.79 |
| [`Move/Resize Window`](moveresize-window.md) | Move or resize a FileMaker window using calculated dimensions and coordinates. | Move/Resize Window | Yes | beta | 0.49 |
| [`New File`](new-file.md) | Open FileMaker's workflow for creating a database file. | New File | Yes | beta | v0.86 |
| [`New Record`](new-record.md) | Alias of New Record/Request; create a record in Browse mode. |  | Yes | ok |  |
| [`New Record/Request`](new-recordrequest.md) | Create a record in Browse mode or a find request in Find mode. | New Record/Request | Yes | ok |  |
| [`New Request`](new-request.md) | Alias of New Record/Request; create a find request in Find mode. |  | Yes | ok |  |
| [`New Window`](new-window.md) | Create a FileMaker window with the supported window options. | New Window | Partial | alpha | v0.76 |
| [`Omit Multiple Records`](omit-multiple-records.md) | Remove a specified number of records from the found set without deleting them. | Omit Multiple Records | Yes | alpha | v0.79 |
| [`Omit Record`](omit-record.md) | Remove the current record from the found set without deleting it. | Omit Record | Yes | ok | v0.79 |
| [`Open Data File`](open-data-file.md) | Open file_path for reading or writing and store its file ID in target. | Open Data File | Yes | beta | 0.49 |
| [`Open Edit Saved Finds`](open-edit-saved-finds.md) | Open the dialog for editing saved finds. | Open Edit Saved Finds | Yes | ok | v0.3 |
| [`Open Favorites`](open-favorites.md) | Open FileMaker's favorite-file view. | Open Favorites | Yes | ok | v0.3 |
| [`Open File`](open-file.md) | Open a FileMaker file using the supported file-opening options. | Open File | Partial | alpha | v0.53 |
| [`Open File Options`](open-file-options.md) | Open the current file's File Options dialog. | Open File Options | Yes | ok | v0.3 |
| [`Open Find/Replace`](open-findreplace.md) | Open the Find/Replace dialog. | Open Find/Replace | Yes | ok | v0.3 |
| [`Open Help`](open-help.md) | Open FileMaker Help. | Open Help | Yes | ok | v0.3 |
| [`Open Hosts`](open-hosts.md) | Open FileMaker's hosts browser. | Open Hosts | Yes | ok | v0.3 |
| [`Open Manage Containers`](open-manage-containers.md) | Open the dialog for managing container storage. | Open Manage Containers | Yes | ok | v0.3 |
| [`Open Manage Custom Functions`](open-manage-custom-functions.md) | Open the custom-functions editor through the development UI; platform and execution-context restrictions apply. |  | Partial | dev | v0.3 |
| [`Open Manage Custom Menus`](open-manage-custom-menus.md) | Open the custom-menu editor through the development UI; platform and execution-context restrictions apply. |  | Partial | dev | v0.3 |
| [`Open Manage Data Sources`](open-manage-data-sources.md) | Open the dialog for managing external data sources. | Open Manage Data Sources | Yes | ok | v0.3 |
| [`Open Manage Database`](open-manage-database.md) | Open Manage Database for the current file. | Open Manage Database | Yes | ok | v0.1 |
| [`Open Manage External Data Sources`](open-manage-external-data-sources.md) | Open the dialog for managing external data sources. |  | Yes | ok | v0.3 |
| [`Open Manage Layouts`](open-manage-layouts.md) | Open the dialog for managing layouts. | Open Manage Layouts | Yes | ok | v0.3 |
| [`Open Manage Scripts`](open-manage-scripts.md) | Alias of Open Script Workspace. |  | Yes | ok | v0.3 |
| [`Open Manage Security`](open-manage-security.md) | Open the current file's security settings. |  | Yes | dev | v0.3 |
| [`Open Manage Themes`](open-manage-themes.md) | Open the dialog for managing themes. | Open Manage Themes | Yes | ok | v0.3 |
| [`Open Manage Value Lists`](open-manage-value-lists.md) | Open the dialog for managing value lists. | Open Manage Value Lists | Yes | ok | v0.3 |
| [`Open Preferences`](open-preferences.md) | Deprecated name for Open Settings; open FileMaker's application settings. |  | Deprecated | ok | v0.3 |
| [`Open Record/Request`](open-recordrequest.md) | Open the current record or find request for editing. | Open Record/Request | Yes | ok | v0.53 |
| [`Open Script`](open-script.md) | Alias of Go to Script; open the specified script in the Script Workspace. |  | Yes | beta | v0.3 |
| [`Open Script Workspace`](open-script-workspace.md) | Open the Script Workspace, optionally navigating to a script or step using the shared script-navigation parameters. | Open Script Workspace | Yes | beta | v0.3 |
| [`Open Settings`](open-settings.md) | Open FileMaker's application settings. | Open Settings | Yes | ok | v0.3 |
| [`Open Sharing`](open-sharing.md) | Open FileMaker's sharing settings. | Open Sharing | Yes | ok | v0.3 |
| [`Open Upload To Host`](open-upload-to-host.md) | Open the workflow for uploading a FileMaker file to a host. | Open Upload To Host | Yes | ok | v0.3 |
| [`Open Url`](open-url.md) | Open a calculated URL using the system's associated application. | Open URL | Yes | ok | v0.13 |
| [`Paste`](paste.md) | Paste clipboard contents into the current selection. | Paste | Yes | alpha |  |
| [`Paste Into Current Layout`](paste-into-current-layout.md) | Switch to Layout mode and paste compatible clipboard content into the current layout. |  | Yes | dev |  |
| [`Pause`](pause.md) | Pause action-script execution for a calculated duration or indefinitely. |  | Yes | beta |  |
| [`Perform Find`](perform-find.md) | Perform the current find requests or construct requests from a structured query. | Perform Find | Yes | beta | v0.35.1 |
| [`Perform JavaScript in Web Viewer`](perform-javascript-in-web-viewer.md) | Call a JavaScript function in an active or named web viewer; the implementation supplies 20 argument positions. | Perform JavaScript in Web Viewer | Partial | beta | v0.75 |
| [`Perform Script`](perform-script.md) | Run a FileMaker script with an optional parameter; the target file must be available. | Perform Script | Yes | beta | v0.31 |
| [`Perform Script on Server`](perform-script-on-server.md) | Run a script on the host with an optional parameter and wait-for-completion setting. | Perform Script On Server | Yes | beta | v0.31 |
| [`Perform Script on Server with Callback`](perform-script-on-server-with-callback.md) | Run a script on the host and invoke the specified callback script when it completes. | Perform Script On Server with Callback | Yes | beta | v0.31 |
| [`Press`](press.md) | Send one or more key combinations through the supported keyboard automation. |  | Yes | beta | v0.12 |
| [`Print`](print.md) | Print using existing print settings, optionally showing the print dialog; printer selection is not exposed as an action parameter. | Print | Partial | alpha | v0.86 |
| [`Re-Login`](re-login.md) | Change the current FileMaker session's account using calculated credentials. | Re-Login | Yes | beta | v0.52 |
| [`Read from Data File`](read-from-data-file.md) | Read a specified amount from an open data file into a target variable or field. | Read from Data File | Yes | beta | 0.49 |
| [`Recover File`](recover-file.md) | Recover a FileMaker database at file_path; recovery is distinct from restoring a backup. | Recover File | Yes | alpha | v0.86 |
| [`Redo`](redo.md) | Repeat the last undone change; fixes the Undo/Redo action's direction to redo. |  | Yes | ok | v0.53 |
| [`Refresh Window`](refresh-window.md) | Redraw the current window, optionally flushing cached join results and external data. | Refresh Window | Yes | beta |  |
| [`Rename File`](rename-file.md) | Rename file_path to new_name within the same folder. | Rename File | Yes | beta | v0.80 |
| [`Revert Record/Request`](revert-recordrequest.md) | Discard uncommitted changes to the current record or find request. | Revert Record/Request | Yes | ok | v0.53 |
| [`Run Menu Command`](run-menu-command.md) | Invoke a supported FileMaker menu command through the development UI. |  | Yes | alpha | v0.69 |
| [`Save a Copy as`](save-a-copy-as.md) | Save a copy, clone, compacted copy or self-contained copy of the database. Supply an explicit file path for unattended backups. | Save a Copy as | Partial | alpha | v0.83 |
| [`Save a Copy as XML`](save-a-copy-as-xml.md) | Export a file's design as XML to a calculated path; FileMaker 26 options can be supplied as a calculation or structured json_options object. | Save a Copy as XML | Yes | beta | v0.73 |
| [`Save as XML`](save-as-xml.md) | Alias of Save a Copy as XML; export the database design to an XML file. |  | Partial | beta |  |
| [`Scroll Window`](scroll-window.md) | Scroll the current window using the requested scrolling option. | Scroll Window | Yes | beta | v0.86 |
| [`Select All`](select-all.md) | Select all content in the current field or active selection context. | Select All | Yes | ok | v0.53 |
| [`Select Script`](select-script.md) | Select a script in the Script Workspace while keeping focus in the script list; requires macOS and MBS. |  | Yes | beta | 0.44 |
| [`Select Script Folder`](select-script-folder.md) | Select a script folder in the Script Workspace by name; requires macOS and MBS. |  | Yes | dev | v0.77 |
| [`Select Script Steps`](select-script-steps.md) | Select a range of steps in the Script Workspace; can combine script navigation and step search. Requires macOS and MBS. |  | Yes | alpha | v0.18 |
| [`Select Window`](select-window.md) | Activate a named FileMaker window, optionally restricting selection to the current file. | Select Window | Yes | beta |  |
| [`Set`](set.md) | Assign a calculation result to a variable or field; the target can be a parameter or a key such as Set.$name. |  | Yes | ok | v0.29 |
| [`Set Clipboard Objects`](set-clipboard-objects.md) | Place supported FileMaker object data on the clipboard. |  | Yes | beta | v0.26 |
| [`Set Clipboard Text`](set-clipboard-text.md) | Replace the clipboard's text with a calculated value. |  | Yes | beta | v0.26 |
| [`Set Data File Position`](set-data-file-position.md) | Move the byte position within an open data file. | Set Data File Position | Yes | beta | 0.49 |
| [`Set Error Capture`](set-error-capture.md) | Control fmIDE error dialogs. Capturing errors does not stop execution; check $$fmide_get_last_error explicitly. | Set Error Capture | Yes | beta | v0.48 |
| [`Set Error Logging`](set-error-logging.md) | Enable or disable FileMaker script-error logging, optionally adding calculated debug information. | Set Error Logging | Yes | beta | <v0.67 |
| [`Set Field`](set-field.md) | Assign a calculated value to a literal field target, optionally at a specified repetition. | Set Field | Yes | beta |  |
| [`Set Field By Name`](set-field-by-name.md) | Calculate the target field name at runtime and assign the supplied calculation result. | Set Field By Name | Yes | alpha | v0.32 |
| [`Set Multi-User`](set-multi-user.md) | Set the current file's sharing state, including the supported hidden-file option. | Set Multi-User | Yes | dev | v0.89 |
| [`Set Selection`](set-selection.md) | Select a character range in the active field; an explicit target is not yet implemented. | Set Selection | Partial | alpha | v0.53 |
| [`Set Variable`](set-variable.md) | Assign a calculation result to a named local or global variable, optionally at a specified repetition. | Set Variable | Yes | beta |  |
| [`Set Web Viewer`](set-web-viewer.md) | Navigate, reload, reset or move through a named web viewer's history. | Set Web Viewer | Yes | alpha | v0.79 |
| [`Set Window Title`](set-window-title.md) | Set a FileMaker window's title from a calculation. | Set Window Title | Yes | beta | v0.74 |
| [`Set Zoom Level`](set-zoom-level.md) | Set the window's zoom level, optionally locking it. | Set Zoom Level | Partial | beta | v0.54 |
| [`Show All Records`](show-all-records.md) | Replace the current found set with all accessible records in the current table. | Show All Records | Yes | ok | v0.26 |
| [`Show Custom Dialog`](show-custom-dialog.md) | Show a dialog with calculated text, buttons and supported input fields; consult the detail page for limitations. | Show Custom Dialog | Partial | alpha |  |
| [`Show Omitted Only`](show-omitted-only.md) | Replace the found set with the records currently omitted from it. | Show Omitted Only | Yes | ok | v0.79 |
| [`Show Version`](show-version.md) | Removed; display $fmide_version with Show Custom Dialog instead. |  | REMOVED | deleted |  |
| [`Show/Hide Text Ruler`](showhide-text-ruler.md) | Show or hide the text ruler using the supported state parameter. | Show/Hide Text Ruler | Yes | beta | v0.86 |
| [`Show/Hide Toolbars`](showhide-toolbars.md) | Show or hide FileMaker toolbars using the supported state and locking options. | Show/Hide Toolbars | Yes | beta | v0.71 |
| [`Speak`](speak.md) | Speak calculated text with the default voice, optionally waiting for speech to finish. | Speak | Partial | beta | v0.86 |
| [`Store Keyboard Buffer`](store-keyboard-buffer.md) | Write text to the fmAutoMate keyboard buffer for later insertion with its keyboard shortcut. |  | Yes | alpha | v0.10 |
| [`Undo`](undo.md) | Undo the most recent change; fixes the Undo/Redo action's direction to undo. |  | Yes | ok | v0.53 |
| [`Undo/Redo`](undoredo.md) | Undo or redo the last applicable change according to the requested direction. | Undo/Redo | Partial | beta | v0.53 |
| [`Unsort Records`](unsort-records.md) | Remove the current sort order from the found set. | Unsort Records | Yes | ok | v0.80 |
| [`View As`](view-as.md) | Switch the layout's record view to Form, List or Table. | View As | Yes | ok | v0.54 |
| [`Write to Data File`](write-to-data-file.md) | Write a calculated value to an open data file, optionally appending a line feed and choosing text encoding. | Write to Data File | Yes | beta | 0.49 |
| [`fmIDE Call`](fmide-call.md) | Run an fmIDE action script in a specified FileMaker file that also contains fmIDE. |  | Yes | alpha | v0.92 |
| [`fmIDE Define Macro`](fmide-define-macro.md) | Store named, reusable fmIDEAS code with optional metadata in the fmide_macros persistent store. Requires FileMaker 26. |  | Yes | beta | v0.56 |
| [`fmIDE Get Macro`](fmide-get-macro.md) | Retrieve a stored macro object into a target; without a target, return it and exit the action script. Requires FileMaker 26. |  | Yes | beta | v0.69 |
| [`fmIDE Run Macro`](fmide-run-macro.md) | Execute a stored macro with optional frontmatter; an unknown macro reports error 1700. Requires FileMaker 26. |  | Yes | beta | v0.56 |
