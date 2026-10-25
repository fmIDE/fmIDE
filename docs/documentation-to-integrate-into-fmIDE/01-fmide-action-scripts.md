# 1. fmIDE Action Scripts

[← Index](README.md) · [Next: fmJAML Syntax Reference →](02-fmjaml-syntax-reference.md)

---

## 1.1 What fmIDE is

fmIDE is a **single FileMaker script**, called `fmIDE`, that automates the FileMaker
*development environment*: going to layouts, scripts, custom functions, opening manage
dialogs, driving the Script Workspace, pressing keys, and so on — plus a useful subset of
ordinary script steps so that those navigations can be wrapped in logic.

Because it is one script with one name, you use it by **performing it with a parameter**:

```
Perform Script [ "fmIDE" ; Parameter: «action script» ]
```

…or by calling it through an `fmp` URL:

```
fmp://$/fmIDE?script=fmIDE&$fmide_actions=%5B%7B%22Beep%22%3Anull%7D%5D
```

## 1.2 What an action script is

An **fmIDE Action Script** — an *fmIDEAS* — is a **JSON array of action objects**. Each
element is one "step":

```json
[
  { "Go to Layout" : { "layout_name" : "fmIDE Actions" } },
  { "Enter Find Mode" : null },
  { "Set Field" : { "fmIDE_Action::ActionName" : "\"==Set\"" } },
  { "Perform Find" : null }
]
```

Written in fmJAML that same script is:

```fmjaml
[+].Go to Layout = "fmIDE Actions"
[+].Enter Find Mode
[+].Set Field.fmIDE_Action::ActionName = == "==Set"
[+].Perform Find
```

The action array is designed to *look like* a list of script steps. fmIDE walks it
one element at a time, exactly like FileMaker walks a script.

### Anatomy of an action

An action element is normally a **JSON object with exactly one key**: the key is the
action name, and the value carries the parameters.

```
{ "«action name»" : «parameters» }
```

The parameters can be:

| Form | Example JSON | fmJAML |
|------|--------------|--------|
| *none* (empty object or `null`) | `{"Beep":{}}` | `[+].Beep` |
| a **scalar** — the action's *default parameter* | `{"Go to Layout":"Home"}` | `[+].Go to Layout = "Home"` |
| an **object** of named parameters | `{"Pause":{"duration":2,"hiatus":true}}` | `[+].Pause`<br>`[:]..duration = 2`<br>`[:]..hiatus = true` |

There is also an alternative *flat* form in which the action name is itself a parameter —
useful when you build actions programmatically:

```json
{ "action_name" : "Go to Layout", "layout_name" : "fmIDE Actions" }
```

### Action names are normalised

Before dispatch, fmIDE normalises the action name with:

```
Substitute ( Proper ( «name» ) ; [" ";""] ; [Char(9);""] ; ["_";""] ; ["-";""] ; ["/";""] )
```

so **case and word separators do not matter**, as long as the words *are* separated:

| You write | Normalises to |
|-----------|---------------|
| `Go to Layout` | `GoToLayout` |
| `go_to_layout` | `GoToLayout` |
| `GO TO LAYOUT` | `GoToLayout` |
| `go-to-layout` | `GoToLayout` |
| `Go   to   layout` | `GoToLayout` |
| `Go to Record/Request/Page` | `GoToRecordRequestPage` |

> ⚠️ Because `Proper()` lower-cases everything after each word boundary, **run-together
> spellings do not work**: `GoToLayout` normalises to `Gotolayout`, which matches nothing.
> Always keep the separators. The two recommended styles are the natural FileMaker step
> name (`Go to Layout`) and `lower_snake_case` (`go_to_layout`).

Leading tabs and spaces inside the name are stripped too — which is why **indentation works**:

```fmjaml
[+].If = 1
[+].	Exit Script = 1
[+].End If
```

## 1.3 The seven parameter formats fmIDE accepts

fmIDE sniffs the script parameter and decides how to read it. This is the actual decision
table from the `fmIDE` script:

| Script parameter starts with… | Detected as | How it is processed |
|---|---|---|
| `#` | **fmJAML** | Compiled to an action array (a leading comment or `#!fmjaml` shebang) |
| `[+]` | **fmJAML** | Compiled to an action array |
| `[0]` | **fmJAML** | Compiled to an action array (legacy explicit-index style) |
| `{ … }` | JSON object | Used as is: an `actions` array, or a single action, or `«thing»_name` parameters |
| `[ … ]` | JSON array | Wrapped as `{"actions": … }` |
| *(empty)* | JSON null | No parameter — typically an `fmp` URL call where `$…` variables carry the request |
| `$` | "Let" | `$var = …` definitions, evaluated — the *Name that Thing* API |
| `---` | YAML | Reserved, **not yet supported** (but see frontmatter below — that is stripped first) |
| anything else | Text | Each line becomes one action (`Beep¶Open Manage Database`) |

**In practice: start your action script with `[+]` and you are writing fmJAML.**

### The "Name that Thing" API

If all you want is to *jump to something*, you do not need an action script at all — just
name the thing:

```
Perform Script [ "fmIDE" ; Parameter: "$script_name = \"fmIDE\"" ]
```

or as an fmp URL: `fmp://$/fmIDE?script=fmIDE&$layout_name=Splash8`

fmIDE turns `«thing»_«identifier»` into the corresponding *Go to…* action. Supported things:

```
account            custom_menu_item        field           object          table
base_table         custom_menu_set         layout          privilege_set   theme
custom_function    extended_privilege      layout_field    script          t_o
custom_menu        external_data_source    layout_part     script_step     value_list
```

each with the identifiers `_name`, `_number`, `_id` and `_uuid` (plus `script_name_stub`,
`script_step_number_to`, `window_name`).

## 1.4 Frontmatter

An action script may be preceded by **frontmatter**: a `---`-delimited block of FileMaker
variable definitions that is evaluated *before* the actions run.

```fmjaml
---
$script_name = "Hello World" ;
$mode        = "readonly"
---
[+].Go To Script
[:]..script_name = $script_name
[+].Exit Script = == MBS ( "ScriptWorkspace.ScriptText" )
```

Rules:

- The parameter must **start** with `---` followed by a newline; the block ends at the next
  line beginning `---`.
- The contents are wrapped in `Let([ … ; r=0];0)` and evaluated, so it is a semicolon-separated
  list of `$var = «calculation»` assignments. A trailing `;` is optional.
- Frontmatter is stripped before the parameter-type sniffing above, so
  `---…---` + `[+]…` is still detected as fmJAML.
- Frontmatter is also how you pass arguments to an **fmIDE macro** (see
  [Writing Action Scripts §3.11](03-writing-action-scripts.md#311-macros)).

## 1.5 The execution model

```
for each action in $fmide_actions:
    resolve action name  →  normalise  →  check enable/disable
    if control action (If/Else If/Else/End If/Loop/Exit Loop If/End Loop):
        manipulate the block stack / skip flag
    else if skipping:
        skip
    else:
        expand short form → read parameters → evaluate calculations → perform the step
    catch errors → $$fmide_last_error / dialog
    advance the action pointer
```

Points worth knowing:

- **Blocks use a stack.** `If` and `Loop` push a frame recording the block type, the index
  and the skip state; `End If`/`End Loop` pop it. Nesting therefore works to any depth.
- **`End Loop` jumps back** to the index recorded by its `Loop` frame.
- **Skipping is a state, not a scan.** When an `If` test is false, fmIDE sets a skip flag and
  keeps walking; every non-control action is skipped until `Else`, `Else If` or `End If`
  clears it. A mis-nested `Else If` raises error `5`.
- **Some actions inject actions.** Convenience actions that return data (`fmIDE Get Macro`,
  `Get Field Names`, …) inject an `Exit Script` action immediately after themselves, so
  there is exactly one exit point.
- **Continuations.** Actions that must hand control to the GUI (`Pause` with `hiatus`,
  some manage-dialogs, `Paste In Current Layout`) halt the script, save the whole interpreter
  state — action array, stack, pointer, local variables — into a continuation object, and
  use MBS to re-call `fmIDE` with it a moment later. Execution resumes exactly where it
  stopped. This is why local variables set with `Set` survive a hiatus.

## 1.6 Runtime variables

### Public — you may read (and sometimes set) these

| Variable | Meaning |
|----------|---------|
| `$fmide_version` | fmIDE version string |
| `$fmide_actions` | The action array currently being executed |
| `$fmide_action` | The action object currently being executed |
| `$fmide_dialog_title` | Title used for fmIDE's own dialogs (`«file»::fmIDE`) |
| `$$fmide_last_error` | Last error number raised by an action (`0` = none) |
| `$$fmide_last_error_detail` | Text detail for the last error |
| `$$fmide_error_capture_state` | Set by the `Set Error Capture` action; fmIDE's analogue of `Get(ErrorCaptureState)` |
| `$$fmide_allow_abort_state` | Set by the `Allow User Abort` action |

### Debugging switches — set these in frontmatter or with `Set`

| Variable | Effect |
|----------|--------|
| `$fmide_debug` | Show fmIDE debugging information |
| `$fmide_debugger` | `1` → step through the action script with a dialog at every action |
| `$fmide_pause_on_error` | With error capture on, drop into the debugger when an error is thrown |
| `$fmide_pause_on_condition` + `$fmide_pause_on_condition_calculation` | Conditional breakpoint: the calculation is evaluated before each action; when true the debugger opens |
| `$fmJAML_debug` | fmJAML log level: `0`=off, `3`=errors, `5`=info, `7`=debug, `8`=verbose |
| `$$fmJAML_log` | fmJAML's debugging log output |

### Reserved — do not use

Every variable beginning `$fmide__`, `$$fmide__`, `$fmJAML__` or `$$fmJAML__` belongs to the
interpreters. Targeting one with `Set` raises error `1300`.

## 1.7 Errors

- Every action that can fail stores `Get(LastError)` in `$$fmide_last_error` and
  `Get(LastErrorDetail)` in `$$fmide_last_error_detail`.
- By default (error capture **off**) fmIDE shows its own dialog when an error is *newly*
  thrown, offering OK / Cancel / HALT.
- `[+].Set Error Capture = 1` suppresses that dialog; you then test `$$fmide_last_error`
  yourself, exactly as you would with `Get(LastError)`.
- fmIDE-specific errors include `5` (missing target for `Set Variable`, or bad block
  structure), `9` (insufficient privileges), `102` (missing target for `Set Field`),
  `1300` (attempt to write a reserved variable).

```fmjaml
[+].Set Error Capture = 1
[+].Go to Layout = "this layout does not exist"
[+].If = "$$fmide_last_error"
[+].	Show Custom Dialog.message_value = == "Error " & $$fmide_last_error & ": " & $$fmide_last_error_detail
[+].End If
```

---

[← Index](README.md) · [Next: fmJAML Syntax Reference →](02-fmjaml-syntax-reference.md)
