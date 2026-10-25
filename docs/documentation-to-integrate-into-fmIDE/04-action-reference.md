# 4. Action Reference

[← Writing Action Scripts](03-writing-action-scripts.md) · [Index](README.md) · [Next: Cookbook & Pitfalls →](05-cookbook-and-pitfalls.md)

---

Every action fmIDE implements, grouped by purpose. For each action:

- **Short form** — the parameter a bare scalar value is assigned to.
- **Parameters** — the named parameters the action reads.
- Unless marked **literal**, parameters are **evaluated as FileMaker calculations**, so write
  them with `==` / `===` (calculation) or `====` / `=====` (literal string). See
  [§3.2](03-writing-action-scripts.md#32-the-two-evaluation-layers) — and note the
  literal/`_value` convention documented there.

Action names below are written in their natural form; any casing and any of the separators
` `, `_`, `-`, `/` work ([§1.2](01-fmide-action-scripts.md#action-names-are-normalised)).

**Legend:** 🍎 macOS only · 🔌 needs the MBS plugin · ⚠️ deprecated

---

## 4.1 Control & flow

### `If` / `Else If` / `Else` / `End If`

Short form: the **test calculation**. Evaluated and coerced with `GetAsBoolean()`.

```fmjaml
[+].If = "$$fmide_last_error = 0"
[+].	Show Custom Dialog = == Fine
[+].Else If = == $$fmide_last_error = 101
[+].	Show Custom Dialog = == Not found
[+].Else
[+].	Show Custom Dialog.message_value = == "Error " & $$fmide_last_error
[+].End If
```

An `Else If` / `Else` / `End If` outside an `If` block raises error `5`.

### `Loop` / `Exit Loop If` / `End Loop`

`Exit Loop If` takes the **test calculation** as its short form.

```fmjaml
[+].Set.$$result = 0
[+].Loop
[+].	Exit Loop If = "$$result > 2"
[+].	Set.$$result = "$$result + 1"
[+].End Loop
```

### `Exit Script`

Short form → `calculation`. The evaluated result becomes fmIDE's script result.

```fmjaml
[+].Exit Script = == Get ( FoundCount )
```

### `Halt Script`

No parameters.

### `Exit Application`

No parameters. Quits FileMaker.

### `Pause`

Short form → `duration` (seconds).

| Parameter | Notes |
|-----------|-------|
| `duration` | seconds; `0` = yield, omitted = indefinitely |
| `indefinitely` | boolean |
| `hiatus` | boolean — halt and resume via a continuation (🔌) |

```fmjaml
[+].Pause                       # indefinitely
[+].Pause = 1
[+].Pause.duration = 500/1000   # 0.5 s, locale-proof
[+].Pause
[:]..duration = 2
[:]..hiatus   = 1
```

> `Pause.ms` was dropped in v0.53 in favour of parity with the FileMaker step.

### `Perform Script` · `Perform Script on Server` · `Perform Script on Server with Callback`

Short form → `script_name` (**literal**).

| Parameter | Notes |
|-----------|-------|
| `specified` | `"By name"` to evaluate `script_name` as a calculation |
| `script_name` | literal by default |
| `file_name` | target file |
| `script_parameter` | evaluated |
| `wait_for_completion`, `callback_script_name`, `callback_file_name`, `callback_script_parameter`, `callback_script_option` | PSoS variants |

```fmjaml
[+].Perform Script = "Test Return 1"

[+].Perform Script
[:]..script_name      = "Test Return ScriptParameter"
[:]..script_parameter = == $random

[+].Perform Script
[:]..specified   = "By name"
[:]..script_name = == "Test Return " & $n
```

### `Allow User Abort`

Short form → `state`. Sets `$$fmide_allow_abort_state`.

### `Set Error Capture`

Short form → `state`. Sets `$$fmide_error_capture_state`. Any truthy value turns it on;
`0`, `""` and a missing value turn it off.

### `Set Error Logging`

| Parameter | |
|---|---|
| `state` | on/off |
| `custom_debug_info` | |

### `Install OnTimer Script`

No parameters — fmIDE can only *stop* the timer (scripts can only be hard-coded).

### `Assert` ⚠️

| Parameter | |
|---|---|
| `test` (short form) | calculation; false aborts the action script |
| `error_code`, `error_message`, `with_dialog` | |

### `Echo`

Short form: any value. Returns a JSON dump of fmIDE's parameter parsing — a debugging aid.

### `Hello`

No parameters. Says hello.

### `#` / `Comment` — comment action

Any action whose name is `#`, `# (comment)`, `Comment`, or begins with `#`, is skipped.

```fmjaml
[+].# = == This comment survives into the JSON. // It can contain dots!
```

### `//` — disabled action

An action name beginning `//` is skipped, as is any action with `disable: true` or
`enable: false`.

---

## 4.2 Navigation — "Go to…"

These are fmIDE's reason for existing. Most take just the thing's name.

| Action | Short form → | Other parameters |
|---|---|---|
| `Go to Layout` | `layout_name` (string) / `layout_number` (number) / *nothing* = original layout | `by` (`"name"`\|`"number"`\|`"id"`\|`"original layout"`), `layout_name`, `layout_number`, `layout_id` |
| `Go to Layout Part` | | `layout_part_name` / `_number` / `_id` |
| `Go to Layout Field` 🍎 | `layout_field_name` | `by`, `layout_name/_number/_id`, `layout_part_*`, `layout_field_name`, `object_name`, `repetition` |
| `Go to Field` | `layout_field_name` | |
| `Go to Object` | `object_name` | `repetition` |
| `Go to Next Field` / `Go to Previous Field` | | |
| `Go to Base Layout` | `table_name` | `base_table_name` |
| `Go to Base Table` / `Go to Table` | `base_table_name` / `t_o_name` | |
| `Go to Base Field` | `field_name` (string) / `field_id` (number) | `base_table_name`, `table_name` |
| `Go to Table Occurrence` | `t_o_name` | `table_name` |
| `Go to Account` | `account_name` | |
| `Go to Custom Function` | `custom_function_name` | |
| `Go to Custom Menu` | `custom_menu_name` | |
| `Go to Custom Menu Item` | `custom_menu_item_name` | |
| `Go to Custom Menu Set` | `custom_menu_set_name` | |
| `Go to Extended Privilege` | `extended_privilege_name` | |
| `Go to External Data Source` | `external_data_source_name` | |
| `Go to Privilege Set` | `privilege_set_name` | |
| `Go to Theme` | `theme_name` | |
| `Go to Value List` | `value_list_name` | |
| `Go to Original Layout` ⚠️ | | returns to the layout fmIDE started on |
| `Go to Original Window` ⚠️ | | |
| `Close Popover` | | |

```fmjaml
[+].Go to Layout = "fmIDE Actions"
[+].Go to Layout = 1
[+].Go to Layout
[:]..by            = "number"
[:]..layout_number = == Get ( LayoutNumber ) + 1

[+].Go to Object
[:]..object_name = == "_gImage"
[:]..repetition  = 2
```

> **`layout_name` is literal** unless you set `by = "name"`, which makes fmIDE evaluate it.
> `layout_number` and `layout_id` are always evaluated.

### Modes

`Enter Browse Mode` · `Enter Find Mode` · `Enter Layout Mode` · `Enter Preview Mode`

Browse/Find/Preview accept a `pause` parameter.

### `Go to Record/Request/Page`

Aliases: `Go to Record`, `Go to Request`, `Go to Page`.

Short form: a **string** matching `First`/`Previous`/`Next`/`Last`/`By Calculation` goes to
`position`; anything else (or a number) goes to `by_calculation`.

| Parameter | |
|---|---|
| `position` | `First` \| `Previous` \| `Next` \| `Last` \| `By Calculation` |
| `by_calculation` | record number calculation |
| `exit_after_last` | boolean — skips to the enclosing `End Loop` |
| `with_dialog` | |

```fmjaml
[+].Go to Record/Request/Page = "First"
[+].Go to Record/Request/Page.by_calculation = == Get ( RecordNumber ) + 6
[+].Go to Record/Request/Page
[:]..position        = "Next"
[:]..exit_after_last = true
```

> `"Prev"` fails fast — write `Previous`.

### `Go to Portal Row`

| Parameter | |
|---|---|
| `row` / `number` | row number |
| `select` | select the row |
| `exit_after_last`, `with_dialog` | |

### `Go to List of Records`

Short form → `list_of_record_ids` (needs FileMaker 22+). Also `layout_name`.

---

## 4.3 Script Workspace 🔌

| Action | Short form → | Parameters |
|---|---|---|
| `Go to Script` / `Open Script` | `script_name` | `script_name`, `script_name.calculation`, `script_name_stub`, `script_id`, `script_number`, `script_step_range`, `script_step_number`, `script_step_number_to`, `script_step_search`, `script_step_search_value` |
| `Go to Script Step` | | as above |
| `Select Script` | `script_name` | selects it in the script *list* |
| `Select Script Steps` | `script_step_range` | as above |
| `Open Script Workspace` / `Open Manage Scripts` | | |
| `Close ScriptWorkspace` | | |
| `Copy Script` | `script_name` | copies the script to the clipboard |
| `Find Script Step` | | `replace_text`, `replace_value` |

**`script_step_range`** accepts `…`, `...` or `..` as the separator and negative numbers
counting from the end:

```fmjaml
[+].Go To Script
[:]..script_name       = "Hello World"
[:]..script_step_range = == "1..-1"      # all steps
[:]..script_step_range = == "2..6"
[:]..script_step_range = == "2..-2"      # all but first and last
```

**Dynamic script names** need `.calculation` (or `«param».value`):

```fmjaml
[+].Go to Script.script_name.calculation = "$last_script"
```

**Look things up:** `script_name_stub` resolves the first script whose name *starts with* the
stub; `script_id` and `script_number` resolve via `ScriptIDs()`/`ScriptNames()`.

---

## 4.4 Fields, editing & the clipboard

| Action | Short form → | Parameters |
|---|---|---|
| `Set` / `Set Variable` / `Set Field` | target-key or `calculation` | `target` \| `name` \| `field_name` \| `variable_name`, `calculation` |
| `Set Field By Name` | `calculation` | `target`, `calculation` |
| `Insert Text` | `text` (**literal**) | `target`, `select`, `text`, `calculation` |
| `Insert Calculated Result` | `calculation` | `target`, `select`, `text`, `calculation` |
| `Insert from URL` | `url` | `target`/`name`/`field_name`/`variable_name`, `url`, `select`, `with_dialog`, `curl_options`, `do_not_automatically_encode_url` |
| `Copy` / `Cut` / `Paste` / `Clear` / `Select All` | | `Cut` and `Clear` accept `select` |
| `Set Selection` | `selection` (`"2-4"`) | |
| `Undo` / `Redo` / `Undo/Redo` | | |
| `Set Clipboard Text` | `text` (**literal**) | `text` (literal), `value` (calculation) |
| `Set Clipboard Objects` | | `fmxmlsnippet` (literal), `fmxmlsnippet_value` (calculation) |
| `Convert Clipboard` | `to` | |
| `Paste In Current Layout` / `Paste Into Current Layout` | | |
| `Press` 🔌 | | `key` (**literal**), `command_key` (**literal**), `option`, `shift`, `times` |
| `Store Keyboard Buffer` | | `text`, `append_line_feed` |

```fmjaml
[+].Set.$i                        = 1
[+].Set.$$total                   = == $$total + $i
[+].Set.fmIDE_Test::_gTest        = ===
"Success"
===
[+].Set Field.fmIDE_Test::_gTest.calculation = 1+2+3+4+5

[+].Set Field by Name
[:]..target      = == fmIDE_Test::_gTest
[:]..calculation = == "123" & "4567"

[+].Insert from URL
[:]..target = "fmIDE_Test::_gTest"
[:]..url    = == "https://cdn.jsdelivr.net/npm/left-pad@1.0/package.json"

[+].Press.key         = == hello
[+].Press.command_key = "A"
[+].Press.key         = Char ( 8 )      /* backspace */
```

- If `Insert from URL` has no target it inserts into the **active field**.
- `Set` distinguishes variable from field by the target: `$`/`$$` → variable, `::` → field.
- Missing target → error `5` (variable) / `102` (field).

---

## 4.5 Records & found sets

| Action | Short form → | Parameters |
|---|---|---|
| `New Record/Request` (aliases `New Record`, `New Request`) | | |
| `Delete Record/Request` (aliases `Delete Record`, `Delete Request`) | `with_dialog` | |
| `Open Record/Request` | | |
| `Revert Record/Request` | | `with_dialog` |
| `Commit Records/Requests` (aliases `Commit Records`, `Commit`) | | `with_dialog`, `skip_data_entry_validation`, `override_ess_locking_conflicts` |
| `Perform Find` | `query` | `query` |
| `Constrain Found Set` | `query` | |
| `Extend Found Set` | `query` | |
| `Show All Records` | `query` | |

```fmjaml
[+].Enter Find Mode
[+].Set Field.fmIDE_Test::Title = == "==Enter Browse Mode"
[+].Perform Find

[+].Commit Records
[:]..with_dialog = 0
```

---

## 4.6 Windows & view

| Action | Short form → | Parameters |
|---|---|---|
| `Adjust Window` | `state` (`Resize to Fit`, `Maximize`, `Minimize`, `Restore`, `Hide`) | |
| `Move/Resize Window` | | `window_name`, `current_file_only`, `top`, `left`, `width`, `height` |
| `Select Window` | `window_name` | `window_name`, `current_file` |
| `Freeze Window` | | |
| `Refresh Window` | *flush* | `flush_cached_join_script_results`, `flush_cached_external_data` |
| `Show/Hide Toolbars` (aliases `Show Toolbars`, `Hide Toolbars`) | | `state` (`Show`/`Hide`), `lock` |
| `Set Zoom Level` | `value` (25…400, `Zoom In`, `Zoom Out`) | `lock`, `value` |
| `View As` | `value` (`Form`, `List`, `Table`, `Cycle`) | |

```fmjaml
[+].Adjust Window = ==== Resize to Fit
[+].Move/Resize Window
[:]..left = 100
[+].Show/Hide Toolbars
[:]..state = "Hide"
[:]..lock  = 1
[+].Set Zoom Level = == "Zoom In"
[+].View As = ==== Table
```

---

## 4.7 Files & data files

| Action | Short form → | Parameters |
|---|---|---|
| `Open File` | `file` | `file`, `hidden` |
| `Close File` | `file` | |
| `Get File Exists` | | `source_file`, `target` |
| `Get File Size` | | `source_file`, `target` |
| `Create Data File` | `file_path` | `file_path`, `create_folders` |
| `Delete File` | `target_file` | |
| `Open Data File` | | `source_file`, `target` (receives the file id) |
| `Close Data File` | `file_id` | |
| `Read from Data File` | | `file_id`, `target`, `amount`, `read_as` (`bytes`) |
| `Write to Data File` | | `file_id`, `data_source`, `append_line_feed`, `write_as` |
| `Get Data File Position` | `position` | `file_id`, `target` |
| `Set Data File Position` | `position` | `file_id`, `position` |
| `Save a Copy as XML` / `Save as XML` | | `all`, `ddr`, `split_catalogs`, `json` |

Notes:

- For the `target` parameters, `target`, `name`, `field_name` and `variable_name` are synonyms.
- When `file_id` is omitted, the data-file actions default to the **last data file opened**.

```fmjaml
[+].Set Error Capture = 1
[+].Set.$FilePath = == Get ( TemporaryPath ) & "test.txt"
[+].Create Data File = == $FilePath
[+].If = "$$fmide_last_error = 0"
[+].	Open Data File
[:].	.source_file = == $FilePath
[:].	.target      = "$FileID"
[+].	If = "$$fmide_last_error = 0"
[+].		Write to Data File
[:].		.file_id           = "$FileID"
[:].		.data_source       = == Get ( CurrentTimestamp )
[:].		.append_line_feed  = true
[+].	End If
[+].	Close Data File = "$FileID"
[+].End If
```

---

## 4.8 Manage & preference dialogs

All take no parameters. Some hand control to the GUI and therefore use a continuation
(or, on some FileMaker versions, do not return to the calling script at all — noted).

`Open Manage Database` · `Open Manage Layouts` · `Open Manage Scripts` ·
`Open Manage Value Lists` · `Open Manage Custom Functions` *(does not continue)* ·
`Open Manage Custom Menus` *(may not continue)* · `Open Manage Security` *(may not continue)* ·
`Open Manage Themes` · `Open Manage Containers` ·
`Open Manage External Data Sources` (alias `Open Manage Data Sources`) ·
`Open Script Workspace` · `Open File Options` · `Open Find/Replace` · `Open Favorites` ·
`Open Edit Saved Finds` · `Open Hosts` · `Open Sharing` · `Open Upload To Host` ·
`Open Help` · `Open Settings` (alias `Open Preferences` ⚠️)

### `Open URL`

Short form → `url`.

| Parameter | |
|---|---|
| `url` | |
| `with_dialog` | |
| `external` | open in the default browser rather than in FileMaker |

---

## 4.9 Accounts & security

| Action | Short form → | Parameters |
|---|---|---|
| `Re-Login` | | `account_name`, `account_password`, `with_dialog` |
| `Go to Account` | `account_name` | |
| `Go to Privilege Set` | `privilege_set_name` | |
| `Go to Extended Privilege` | `extended_privilege_name` | |

```fmjaml
[+].Re-Login
[:]..account_name     = ==== user
[:]..account_password = ==== user
```

---

## 4.10 Data & metadata

### `Execute FileMaker Data API`

| Parameter | |
|---|---|
| `request` | the DAPI request JSON |
| `target` | variable / field to receive the result |
| `select` | |

The request can be built inline with fmJAML paths:

```fmjaml
[+].Execute FileMaker Data API
[:]..target = "$result"
[:]..select = true
[:]..request.layouts        = "fmIDE Tests"
[:]..request.query[+].Suite = "5 Test Examples"
[:]..request.query[:].Category = "fmIDE-AI-Bridge"
[:]..request.limit  = 100
[:]..request.offset = 1
[+].Exit Script = "$result"
```

…or as a heredoc calculation:

```fmjaml
[+].Execute FileMaker Data API
[:]..target  = == "$result"
[:]..select  = true
[:]..request = ===
JSONSetElement ( "{}"
;["layouts" ; "fmIDE Tests" ; JSONString]
;["limit"   ; 1 ; JSONNumber]
)
===
```

### `Get Field Names` ⚠️

Short form → `table_name`. Returns `{"data":{"field_names":"…"}}` via an injected `Exit Script`.

### `Get Resource` ⚠️

| Parameter | `resource`, `o_s` |

### `Get Version` ⚠️ / `Show Version` ⚠️

Dropped in v0.58. Use instead:

```fmjaml
[+].Exit Script        = == $fmide_version
[+].Show Custom Dialog = == $fmide_version
```

---

## 4.11 Dialogs

### `Show Custom Dialog`

Short form → `message`.

| Parameter | |
|---|---|
| `message` | the message — **literal text** |
| `message_value` | the message as a **calculation** |
| `title` | **literal text** |
| `buttons_list` | `¶`-separated button names (default `OK`) |
| `labels`, `inputs`, `commits` | input fields |
| `message__«B1»_«B2»_«B3»` | compact button syntax |

> ⚠️ `message` is **not** evaluated. For anything computed — including anything that changed
> earlier in the action script — use `message_value`.

The compact button syntax splits the key at `__` and then the button names at `_`:

```fmjaml
[+].Show Custom Dialog.message__OK_Cancel = == Replace this with that?
[+].If = "Get ( LastMessageChoice ) = 1"
[+].	Show Custom Dialog = == Doing it!
[+].End If
```

Recognised shorthands include `message__OK`, `message__OK_Cancel`, `message__Cancel_OK`,
`message__Yes_No`, `message__No_Yes`.

```fmjaml
[+].Show Custom Dialog
[:]..message_value = == "Hello " & Get ( AccountName )
[:]..title       = == fmIDE
```

### `Beep`

No parameters.

---

## 4.12 fmIDE-specific actions

### `Configure Persistent Data` (aliases `Set Persistent Data`, `Delete Persistent Data`)

| Parameter | |
|---|---|
| `instance_id` | key |
| `value` | value to store |
| `delete` | boolean |

```fmjaml
[+].Configure Persistent Data
[:]..instance_id = ==== fmide_macro HelloWorld
[:]..value       = ==== [+].Show Custom Dialog = "Hello World"
```

### `fmIDE Define Macro`

```fmjaml
[+].fmIDE Define Macro.«name» = ===== «fmJAML macro body» ===
```
Parameters: `macro_name`, `code`, `metadata`.

### `fmIDE Run Macro`

```fmjaml
[+].fmIDE Run Macro.«name» = ==== «frontmatter variable definitions»
```
Parameters: `macro_name`, `frontmatter`.

### `fmIDE Get Macro`

```fmjaml
[+].fmIDE Get Macro.«name»
```
Returns `{"name":…,"code":…,"metadata":…}` via an injected `Exit Script`.

Full example:

```fmjaml
[+].fmIDE Define Macro.Echo = ==== [+].Exit Script = == $script_parameter
[+].fmIDE Run Macro.Echo    = ==== $script_parameter = "hello"
[+].Exit Script             = == Get ( ScriptResult )      # → hello
```

---

## 4.13 Deprecated & removed

| Action | Status (v0.61–v0.63) |
|---|---|
| `Try` | **removed** — use the [TRY-loop idiom](03-writing-action-scripts.md#the-try-loop-idiom) |
| `Set Pref` | **removed** |
| `Get Version`, `Show Version` | dropped v0.58 — use `$fmide_version` |
| `Assert` | deprecated |
| `Get Field Names`, `Get Resource` | deprecated |
| `Go to Original Layout`, `Go to Original Window` | deprecated |
| `Open Preferences` | deprecated — alias of `Open Settings` |
| `Pause.ms` | removed v0.53 — use `duration` |
| `Beep.times` | removed v0.50 (parity with the script step) |

---

[← Writing Action Scripts](03-writing-action-scripts.md) · [Index](README.md) · [Next: Cookbook & Pitfalls →](05-cookbook-and-pitfalls.md)
