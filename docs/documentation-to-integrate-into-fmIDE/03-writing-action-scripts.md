# 3. Writing Action Scripts with fmJAML

[← fmJAML Syntax Reference](02-fmjaml-syntax-reference.md) · [Index](README.md) · [Next: Action Reference →](04-action-reference.md)

---

This is the main guide. It assumes you have skimmed
[fmIDE Action Scripts](01-fmide-action-scripts.md) and know that fmJAML is a `path = value`
language ([fmJAML Syntax Reference](02-fmjaml-syntax-reference.md)).

## 3.1 Hello, fmIDEAS

The smallest useful action script:

```fmjaml
[+].Show Custom Dialog = == Hello World
```

Run it with `Perform Script [ "fmIDE" ; Parameter: «that text» ]`.

Every line starts `[+].` — "append a new element to the action array" — followed by the
action name. That is the whole shape of an fmIDEAS:

```fmjaml
#!fmjaml
[+].«Action Name» [ = «value» ]
[:]..«parameter»  = «value»
[:]..«parameter»  = «value»
[+].«Action Name» …
```

- `[+]` starts a **new action**.
- `[:]..name` adds a **parameter to the action just started**.

A slightly bigger one — the classic "find all `Set` actions" script:

```fmjaml
[+].Go to Layout = "fmIDE Actions"
[+].Enter Find Mode
[+].Set Field.fmIDE_Action::ActionName = == "==Set"
[+].Perform Find
```

## 3.2 The two evaluation layers

**This is the section that saves you an afternoon.**

There are *two* evaluators between your text and the running step:

```
your fmJAML text
      │  (1) fmJAML evaluates the expression after "=" …unless a value operator says otherwise
      ▼
   JSON action array
      │  (2) fmIDE evaluates most parameter values as FileMaker calculations
      ▼
   the FileMaker step
```

### The classic trap

```fmjaml
[+].Exit Script = "a" & "b"
```

1. fmJAML evaluates `"a" & "b"` → the text `ab` → JSON `{"Exit Script":"ab"}`
2. fmIDE evaluates `ab` as a calculation → **`?`**

The result is `?`, not `ab`. Both layers ran, and the second one had nothing valid to chew on.

### The three reliable spellings

| You want fmIDE to… | Write | JSON | fmIDE evaluates → |
|---|---|---|---|
| **run a calculation** | `= == «calc»` | `"«calc»"` | the calculation's result |
| **run a multi-line calculation** | `= === «calc» ===` | `"«calc»"` | the calculation's result |
| **use a literal string** | `= ==== «text»` | `"\"«text»\""` | `«text»` |
| **use a multi-line literal** | `= ===== «text» ===` | `"\"«text»\""` | `«text»` |

```fmjaml
[+].Exit Script = == "a" & "b"                 # → ab   ✔
[+].Exit Script = == $fmide_actions            # → the action array
[+].Exit Script = ===
JSONSetElement ( "{}" ; "result" ; "[1,2,3]" ; JSONArray )
===
[+].Adjust Window = ==== Resize to Fit         # a literal string parameter
```

### The older spelling still works

Wrapping the calculation in quotes makes fmJAML evaluate the *quoted literal* back into the
calculation text, which achieves the same thing:

```fmjaml
[+].Exit Script = "$$result"                   # ≡ [+].Exit Script = == $$result
[+].If          = "$$fmide_last_error = 0"     # ≡ [+].If = == $$fmide_last_error = 0
```

You will see this style all over the fmIDE test suite and it is perfectly correct. It is
just harder to get right the moment your calculation itself contains quotes:

```fmjaml
[+].Exit Script = "\"\\\"Hello\\\", he said\""   # 😱
[+].Exit Script = ==== "Hello", he said          # 😀 same result
```

**Rule of thumb: reach for `==` / `===` by default, and `====` / `=====` when you want a
literal. Only fall back to `"…"` for short, quote-free calculations.**

### When does each layer run?

Layer 1 runs **once, up front**: fmIDE compiles the whole fmJAML text into the action array
*before* the first action executes. So a bare expression is frozen at compile time.

Layer 2 runs **at the moment the action executes**.

```fmjaml
[+].Set.$n      = 1
[+].Set.$n      = == $n + 1
[+].Exit Script = $n      # ✗ evaluated at compile time — $n is empty then
[+].Exit Script = == $n   # ✔ evaluated when the action runs → 2
```

**Anything that depends on what earlier actions did must use `==` / `===`.**

### Which parameters get evaluated?

Most of them — fmIDE's per-action code has an explicit `#Calculations` phase that runs
`Evaluate()` over its parameters. Two families are **literal** instead:

**1. Identifier parameters** — the names of things:

- `layout_name` is literal — `[+].Go to Layout = "Home"` goes to the layout called `Home`.
  Opt into a calculation with `by = "name"`:

  ```fmjaml
  [+].Go to Layout
  [:]..by          = "name"
  [:]..layout_name = == $my_layout
  ```

- `script_name` is literal; use the `.calculation` sub-element for a dynamic one:

  ```fmjaml
  [+].Go to Script.script_name.calculation = == $script_name
  ```

- `layout_number`, `layout_id`, `object_name`, `repetition` and `script_step_range` **are**
  evaluated.

**2. Text-vs-value parameter pairs.** Several actions offer both a literal and a calculated
form of the same parameter. The convention is that the plain name is **literal** and the
`_value` / `.value` / `.calculation` variant is **evaluated**:

| Literal | Evaluated |
|---------|-----------|
| `Show Custom Dialog.message`, `.title` | `Show Custom Dialog.message_value` |
| `Set Clipboard Text.text` | `Set Clipboard Text.value` |
| `Set Clipboard Objects.fmxmlsnippet` | `…fmxmlsnippet_value` |
| `Insert Text.text` | `Insert Text.calculation` |
| `Press.key`, `.command_key` | — |
| `Go to Script.script_name` | `…script_name.calculation` |
| `…script_name_stub`, `…script_id`, `…script_number` | `….value` |
| `Find Script Step.script_step_search` | `…script_step_search_value` |

```fmjaml
[+].Show Custom Dialog.message       = == Something went wrong          # literal text
[+].Show Custom Dialog.message_value = == "Error " & $$fmide_last_error  # calculated
```

> `Execute FileMaker Data API.request` is a special case: if it already starts with `{` it is
> used as JSON, otherwise it is evaluated.

When in doubt: test it, or check [the action reference](04-action-reference.md).

## 3.3 The five ways to write an action

All five compile to the same JSON shape; pick whichever reads best.

### a) No parameters

```fmjaml
[+].Beep
[+].Enter Find Mode
[+].Commit Records
```

→ `{"Beep":{}}`

### b) Short form — the default parameter

Every action that takes one obvious parameter accepts it directly:

```fmjaml
[+].Go to Layout      = "fmIDE Actions"    # → layout_name
[+].Show Custom Dialog = == Hello          # → message
[+].Pause              = 2                 # → duration
[+].Set Error Capture  = 1                 # → state
[+].Perform Script     = "Test Return 1"   # → script_name
[+].Open URL           = ==== https://mrwatson.de
```

Some actions choose the parameter by **type**:

```fmjaml
[+].Go to Layout = "Home"   # string → layout_name
[+].Go to Layout = 1        # number → layout_number
[+].Go to Layout            # nothing → back to the original layout
```

See the [Action Reference](04-action-reference.md) for each action's default parameter.

### c) Long form — named parameters on following lines

```fmjaml
[+].Show Custom Dialog
[:]..message = == Hello World
[:]..title   = == ERROR
```

```fmjaml
[+].Go to Layout
[:]..by            = "number"
[:]..layout_number = == Get ( LayoutNumber ) + 1
```

`[:]..` means "same array element, same action key, new parameter". The action name is
inherited from the previous line by fmJAML's path inheritance — you never repeat it.

### d) Dotted form — first parameter inline, the rest below

```fmjaml
[+].Show Custom Dialog.message = == Hello World
[:]..title                     = == ERROR
```

```fmjaml
[+].Go to Record/Request/Page.by_calculation = == Get ( RecordNumber ) + 6
[+].Go to Script.script_name.calculation     = == $script_name
[+].Pause.duration                           = 500/1000
```

### e) Target-key form — for actions that write somewhere

`Set`, `Set Field`, `Set Field By Name`, `Insert Text`, `Insert Calculated Result` and
`Insert from URL` accept the **target as the key**. fmIDE recognises it because it starts
with `$` or contains `::`:

```fmjaml
[+].Set.$counter                   = 0
[+].Set.$$total                    = == $$total + 1
[+].Set.fmIDE_Test::_gTest         = == "Success"
[+].Set Field.fmIDE_Test::_gTest   = 1234567
[+].Insert from URL.fmIDE_Test::_gTest = == "https://example.org/data.json"
```

The value can itself be an object with `calculation` or `text`:

```fmjaml
[+].Set.fmIDE_Test::_gTest.calculation = 12345
[+].Set.$$a.text                       = == literal text
```

## 3.4 Layout and indentation

Indent with tabs after the `[+].` — fmIDE strips whitespace from the action name, so
indentation is purely cosmetic and entirely encouraged:

```fmjaml
[+].Set.$$result = 0
[+].Loop
[+].	Exit Loop If = "$$result > 2"
[+].	Set.$$result = "$$result + 1"
[+].End Loop
[+].Exit Script = "$$result"
```

Nested blocks with parameters keep the indentation in the inherited part of the path:

```fmjaml
[+].If = "$$fmide_last_error = 0"
[+].	Read from Data File
[:].	.file_id = "$FileID"
[:].	.target  = "$text"
[+].End If
```

Note the `[:].	.file_id` spelling: the `.` before the tab is the delimiter that inherits the
action key, the tab is indentation, and `.file_id` is the parameter. Line your `=` signs up
too — fmJAML trims horizontally, so it costs nothing:

```fmjaml
[+].Go To Script
[:]..script_name       = "Hello World"
[:]..script_step_range = == "1..-1"
```

## 3.5 Comments and disabling actions

There are three distinct mechanisms. Know which one you want.

### fmJAML comments — vanish completely

```fmjaml

# This never reaches the JSON at all

[+].Beep
```

### fmIDE comment actions — become a `#` step

```fmjaml
[+].# = == This is the preferred way to encode a comment. // It can contain dots!
```

→ `{"#":"This is the preferred way…"}` — fmIDE skips any action whose name starts with `#`
(or is `Comment`). Use these when you want the comment to survive into the JSON, e.g. when
the action script is generated, logged, or shown in the debugger.

There is a legacy convenience spelling — but it breaks if the text contains a `.`:

```fmjaml
[+].# This is the legacy comment syntax
```

### Disabling an action — `//`

```fmjaml
[+].// Exit Script = 1
```

fmIDE keeps the leading `//` through name normalisation and skips the action. Equivalent
explicit forms:

```fmjaml
[+].Exit Script
[:]..disable = true
```

```fmjaml
[+].Exit Script
[:]..enable = false
```

## 3.6 Variables and fields

`Set` is the workhorse. It sets **variables** (`$`, `$$`) and **fields** (`Table::Field`)
with the same syntax; fmIDE decides from the target.

```fmjaml
[+].Set.$i                 = 1
[+].Set.$$counter          = == $$counter + 1
[+].Set.fmIDE_Test::_gTest = == "Success"
```

The value is a **calculation**, so use `==` / `===`:

```fmjaml
[+].Set.$_SP = == Case ( not IsEmpty ( Get ( ScriptParameter ) ) ; Get ( ScriptParameter ) ; "{}" )

[+].Set.$readParams = ===
Let(
[
$foo = JSONGetElement ( $_SP ; "foo" ) ;
$bar = JSONGetElement ( $_SP ; "bar" )
];
""
)
===
```

Notes:

- Missing target → error `5` (`Set Variable`) or `102` (`Set Field`).
- Targeting a `$fmide__*` variable → error `1300`.
- Local variables set with `Set` are remembered in `$fmide__local_variables` and **survive a
  hiatus/continuation** — fmIDE stashes them in globals and restores them when it resumes.
- `Set Field` requires the field to be on the current layout, exactly like the script step.
  `Set Field By Name` does not.

## 3.7 Control flow

fmIDE implements `If` / `Else If` / `Else` / `End If` and `Loop` / `Exit Loop If` / `End Loop`
with a proper block stack, so they nest arbitrarily.

```fmjaml
[+].If = 0
[+].	Exit Script = 1
[+].Else If = 1
[+].	Exit Script = 2
[+].Else
[+].	Exit Script = 3
[+].End If
```

The test is the action's value, evaluated and coerced with `GetAsBoolean()`. Use `==` for
anything with quotes:

```fmjaml
[+].If = == MBS ( "ScriptWorkspace.CurrentTab" ) = $script_name
[+].	Show Custom Dialog = == Found it!
[+].End If
```

Loops:

```fmjaml
[+].Set.$$result = 0
[+].Loop
[+].	Exit Loop If = "$$result > 2"
[+].	Set.$$result = "$$result + 1"
[+].End Loop
[+].Exit Script = "$$result"          # → 3
```

### The TRY-loop idiom

fmIDE has no `Try` action (it was removed in v0.61). The FileMaker-native pattern works
perfectly:

```fmjaml
[+].Set.$log = == ""
[+].# = == TRY loop
[+].Loop
[+].	Set.$error_message = == Case ( «precondition fails» ; "Error: …" )
[+].	Exit Loop If = == not IsEmpty ( $error_message )
[+].	Set.$log = == List ( $log ; "precondition ok" )
[+].	# … the real work …
[+].	Set.$error_message = == "OK"
[+].	Exit Loop If = 1
[+].End Loop
[+].Exit Script = == List ( $error_message ; $log )
```

### `Exit after last`

`Go to Record/Request/Page` supports FileMaker's *Exit after last*, which skips to the
corresponding `End Loop` (or the end of the script):

```fmjaml
[+].Go to Record/Request/Page
[:]..position        = "Next"
[:]..exit_after_last = true
```

## 3.8 Returning a result

`Exit Script` takes a **calculation** and its result becomes the script result of the
`fmIDE` script — exactly like the FileMaker step.

```fmjaml
[+].Exit Script = == Get ( LayoutName )
[+].Exit Script = 200                       # number
[+].Exit Script = ==== 200                  # the string "200"
[+].Exit Script = ===
JSONSetElement ( "{}"
;["found" ; Get ( FoundCount ) ; JSONNumber]
;["layout" ; Get ( LayoutName ) ; JSONString]
)
===
```

Since v0.58 every action that produces data returns it by **injecting** an `Exit Script`
action after itself, so there is exactly one exit point.

When fmIDE is called via an `fmp` URL there is no caller to return to. Use
`Insert from URL` inside the action script to post the result to a webhook instead.

## 3.9 Errors and assertions

```fmjaml
[+].Set Error Capture = 1
[+].Go to Layout = "does not exist"
[+].If = "$$fmide_last_error"
[+].	Exit Script = == "Error " & $$fmide_last_error & ": " & $$fmide_last_error_detail
[+].End If
```

- `Set Error Capture = 1` (or any truthy value) suppresses fmIDE's error dialog.
- `Allow User Abort = 0` removes the *Cancel* / *HALT* buttons from that dialog.
- `$$fmide_last_error` is reset to `0` at the start of each fmIDE call and updated by every
  action that can fail.
- `Assert` (deprecated in v0.61, still present) aborts the action script when its `test`
  calculation is false:

  ```fmjaml
  [+].Assert.test = == $count = 456
  [:]..with_dialog = 1
  ```

## 3.10 Passing values in

Three ways, in increasing order of formality.

**1. Just build the calculation** — everything in an fmJAML value is evaluated at run time,
so `Get(…)` functions and existing variables are available:

```fmjaml
[+].Go to Layout
[:]..by            = "number"
[:]..layout_number = == Get ( LayoutNumber ) + 1
```

**2. Set variables at the top of the script:**

```fmjaml
[+].Set.$layout = ==== fmIDE Actions
[+].Go to Layout
[:]..by          = "name"
[:]..layout_name = == $layout
```

**3. Frontmatter** — declarative, evaluated before any action runs, and the mechanism macros
use:

```fmjaml
---
$script_name = "Hello World" ;
$fmide_debug = 0
---
[+].Go To Script
[:]..script_name       = $script_name
[:]..script_step_range = "1..-1"
[+].Exit Script = == MBS ( "ScriptWorkspace.ScriptText" )
```

Since the action script text itself is a FileMaker calculation string when you build it in a
script, you can also interpolate at build time — but frontmatter is cleaner and keeps the
action script a plain, diffable text.

## 3.11 Macros

fmIDE can store action scripts persistently (using FileMaker's persistent-data store) and run
them by name.

```fmjaml
[+].fmIDE Define Macro.HelloWorld = =====
[+].Show Custom Dialog = "Hello " & Case ( not IsEmpty ( $name ) ; $name ; "World" )
[+].Exit Script = == $name
===
```

The `=====` heredoc quotes the whole macro body so it survives as a single JSON string.

Run it, passing arguments as frontmatter-style variable definitions:

```fmjaml
[+].fmIDE Run Macro.HelloWorld = ==== $name = "Foo"
```

Fetch its definition:

```fmjaml
[+].fmIDE Get Macro.HelloWorld
```

→ `{"code":"[+].Show Custom Dialog = …","name":"HelloWorld"}`

Macros carry `name`, `code` and `metadata`. Underneath they are ordinary persistent data, so
`Configure Persistent Data` (aliases `Set Persistent Data` / `Delete Persistent Data`) can
manage them directly:

```fmjaml
[+].Configure Persistent Data
[:]..instance_id = ==== fmide_macro HelloWorld
[:]..delete      = true
```

## 3.12 Debugging

### The fmIDE debugger

```fmjaml
---
$fmide_debugger = 1
---
[+].Go to Layout = "fmIDE Actions"
[+].Beep
```

You get a dialog at every action showing `«n»/«total» "«action name»"` and the action's JSON,
with **Continue / Pause / …** buttons; the `…` button offers **Debugger OFF / Continue / Halt**.

Conditional breakpoints:

```fmjaml
---
$fmide_pause_on_condition = 1 ;
$fmide_pause_on_condition_calculation = "$i > 5"
---
```

Break when an error is thrown (needs error capture on):

```fmjaml
---
$fmide_pause_on_error = 1
---
[+].Set Error Capture = 1
```

### Inspect the compiled JSON

The single most useful trick — have the action script return itself:

```fmjaml
[+].#
[:]..some = "thing"
[+].Exit Script = == $fmide_actions
```

→ `[{"#":{"some":"thing"}},{"Exit Script":"$fmide_actions"}]`

This is exactly how the fmJAML test-suite proves what each construct compiles to.

### Debug fmJAML itself

```fmjaml
---
$fmJAML_debug = 7
---
```

then read `$$fmJAML_log` (and `$$fmJAML_debug_dtype`). Levels: `3` errors, `5` info,
`7` debug, `8` verbose (per-character DPS trace).

### Version stamps

```fmjaml
[+].Set.$fmjaml_version = ;==version;
[+].Exit Script = == $fmide_version & " / " & $fmjaml_version
```

## 3.13 Style guide

These conventions come from the fmIDE test suite and make action scripts easy to read.

1. **Start every action with `[+].`, every parameter with `[:]..`.** Consistency beats
   cleverness; the terser inheritance spellings are for arrays of data, not for actions.
2. **Use `==` for calculations and `====` for literals.** Escaping quotes inside quotes is
   how bugs get in.
3. **Use `===` heredocs for any calculation longer than a line**, and keep the FileMaker
   formatting you would use in the Script Workspace.
4. **Indent block bodies with a tab after the `[+].`.** It is free and it makes structure
   visible.
5. **Line up the `=` signs** within a group of parameters.
6. **Use `#` comments for notes to yourself, `[+].#` comment actions for notes that belong
   to the script.**
7. **Turn on `Set Error Capture` in any script that checks `$$fmide_last_error`** — otherwise
   fmIDE's own dialog interrupts you first.
8. **Write the action name the way FileMaker writes the step** (`Go to Record/Request/Page`,
   `Show/Hide Toolbars`) — or in `lower_snake_case`. Never run the words together.
9. **End with an `Exit Script`** if the caller needs anything back.
10. **Keep a `#!fmjaml` shebang or a leading `#` comment** at the top when the script might
    be stored or passed around — it both documents the format and guarantees fmIDE sniffs it
    as fmJAML.

---

[← fmJAML Syntax Reference](02-fmjaml-syntax-reference.md) · [Index](README.md) · [Next: Action Reference →](04-action-reference.md)
