# 5. Cookbook & Pitfalls

[← Action Reference](04-action-reference.md) · [Index](README.md)

---

## 5.1 Recipes

### Search for something in a table

```fmjaml
[+].Go to Layout = "fmIDE Actions"
[+].Enter Find Mode
[+].Set Field.fmIDE_Action::ActionName = == "==Set"
[+].Perform Find
```

### Open a script and select all of its steps

```fmjaml
[+].Go To Script
[:]..script_name       = "Hello World"
[:]..script_step_range = == "1..-1"
[+].Exit Script = == MBS ( "ScriptWorkspace.ScriptText" )
```

### Go to the *last* script in the file

```fmjaml
[+].Open Script Workspace
[+].Set.$last_script = ===
Substitute ( RightValues ( ScriptNames ( "" ) ; 1 ) ; ¶ ; "" )
===
[+].Go to Script.script_name.calculation = "$last_script"
[+].Exit Script = ===
MBS ( "ScriptWorkspace.CurrentTab" ) = $last_script
===
```

### Copy a script's steps to the clipboard

```fmjaml
[+].Go To Script
[:]..script_name       = "fmIDE"
[:]..script_step_range = == "1..-1"
[+].Copy
```

### Return structured data to the caller

```fmjaml
[+].Set.$before = == Get ( TotalRecordCount )
[+].New Record/Request
[+].Set.$after  = == Get ( TotalRecordCount )
[+].Exit Script = ===
JSONSetElement ( "{}"
;["before" ; $before ; JSONNumber]
;["after"  ; $after  ; JSONNumber]
;["added"  ; $after - $before ; JSONNumber]
)
===
```

### Read a text file next to the database

```fmjaml
[+].Set Error Capture = 1
[+].Set.$FilePath = == Substitute ( Get ( FilePath ) ; "fmIDE.fmp12" ; "Import.log" )
[+].Open Data File
[:]..source_file = "$FilePath"
[:]..target      = "$FileID"
[+].If = == $$fmide_last_error
[+].	Exit Script = == "Error " & $$fmide_last_error & " opening " & $FilePath
[+].Else
[+].	Read from Data File
[:].	.file_id = "$FileID"
[:].	.target  = "$bytes"
[:].	.read_as = "bytes"
[:].	.amount  = "3+9"
[+].	Set.$text = == TextDecode ( $bytes ; "utf-8" )
[+].End If
[+].Close Data File = "$FileID"
[+].Exit Script = "$text"
```

### Close every open data file

```fmjaml
[+].Loop
[+].	Exit Loop If = == IsEmpty ( Get ( OpenDataFileInfo ) )
[+].	Close Data File
[+].End Loop
```

### Query your own data with the Data API

```fmjaml
[+].Execute FileMaker Data API
[:]..target = "$result"
[:]..select = true
[:]..request.layouts           = "fmIDE Tests"
[:]..request.query[+].Suite    = "5 Test Examples"
[:]..request.query[:].Category = "fmIDE-AI-Bridge"
[:]..request.limit  = 100
[:]..request.offset = 1
[+].Exit Script = "$result"
```

### A guarded "TRY" block with a log

```fmjaml
[+].Set.$log = == ""
[+].Loop
[+].	Set.$error = == Case ( IsEmpty ( $input ) ; "Error: no input" )
[+].	Exit Loop If = == not IsEmpty ( $error )
[+].	Set.$log = == List ( $log ; "input present" )
#	… work …
[+].	Set.$error = == "OK"
[+].	Exit Loop If = 1
[+].End Loop
[+].Exit Script = == List ( $error ; $log )
```

### Define and run a macro

```fmjaml
[+].fmIDE Define Macro.HelloWorld = =====
[+].Show Custom Dialog = "Hello " & Case ( not IsEmpty ( $name ) ; $name ; "World" )
[+].Exit Script = == $name
===
[+].fmIDE Run Macro.HelloWorld = ==== $name = "Foo"
[+].Exit Script = == Get ( ScriptResult )
```

### Ask before acting

```fmjaml
[+].Show Custom Dialog.message__OK_Cancel = == Replace this with that?
[+].If = "Get ( LastMessageChoice ) = 1"
[+].	Press.command_key = "V"
[+].End If
```

### Show the versions

```fmjaml
[+].Set.$fmjaml = ;==version;
[+].Show Custom Dialog.message_value = == "fmIDE " & $fmide_version & " / fmJAML " & $fmjaml
```

### Build a data payload (fmJAML as a plain JSON templating language)

```fmjaml
feedback
.title     = ;¶'//'**;                    $title
.text      = ;***;                        $text
.priority  = ;**N?N:N'2';                 $priority
.name      = ;***¶1?T:'anonymous';        $name
.email     = ;***¶1?T:'error:missing';    $email
.timestamp = ;M;                          Get ( CurrentTimestamp )
```

### Call fmIDE from outside FileMaker

```text
fmp://$/fmIDE?script=fmIDE&$layout_name=Splash8
fmp://$/fmIDE?script=fmIDE&$script_name=fmIDE&$script_step_number=2
fmp://$/fmIDE?script=fmIDE&$fmide_actions=«url-encoded JSON action array»
```

Note that a URL call carries JSON, not fmJAML — build the JSON with `fmJAML ( "" ; «text» )`
first, then `GetAsURLEncoded()` it.

---

## 5.2 Pitfalls

### ⚡ 1. The double-evaluation trap

```fmjaml
[+].Exit Script = "a" & "b"      # → "?"
```

fmJAML evaluates `"a" & "b"` to `ab`, then fmIDE evaluates `ab` and fails.

```fmjaml
[+].Exit Script = == "a" & "b"   # → ab   ✔
```

See [§3.2](03-writing-action-scripts.md#32-the-two-evaluation-layers).

### ⚡ 1a. A bare expression is frozen at compile time

fmIDE compiles the whole fmJAML text into JSON *before* the first action runs. A bare
expression is therefore evaluated **once, up front** — it cannot see anything a later action
does.

```fmjaml
[+].Set.$n      = 1
[+].Exit Script = $n      # ✗ "" — $n did not exist at compile time
[+].Exit Script = == $n   # ✔ 1
```

### ⚡ 1b. `Show Custom Dialog.message` is *not* evaluated

`message` and `title` are literal text; `message_value` is the calculated variant.

```fmjaml
[+].Show Custom Dialog = == "Error " & $$fmide_last_error              # ✗ shows the calc text
[+].Show Custom Dialog.message_value = == "Error " & $$fmide_last_error # ✔
```

The same literal-vs-`_value` split applies to `Set Clipboard Text.text` / `.value` and
`Set Clipboard Objects.fmxmlsnippet` / `.fmxmlsnippet_value`, and `Press.key` is literal too.

### ⚡ 2. Number or string?

fmIDE evaluates `Exit Script`, so what you get back depends on how many layers of quoting
survive:

| fmJAML | JSON | Script result |
|---|---|---|
| `[+].Exit Script = 200` | `200` | number `200` |
| `[+].Exit Script = "200"` | `"200"` | number `200` (evaluated) |
| `[+].Exit Script = ==== 200` | `"\"200\""` | **string** `"200"` |
| `[+].Exit Script = 100+100` | `"200"` | number `200` |

### ⚡ 3. Dropping a value with `[+]` in the same line breaks the following `[:]`

```fmjaml
[+].#.drop = ;?; ""                     # ✗ the whole path — including [+] — is dropped
[:].#.this_breaks = 1                   #   …so [:] has no "last element" and trashes the array
```

Create the array element first, then drop parameters inside it:

```fmjaml
[+].#                                   # ✔ element exists
[:]..drop = ;?; ""                      #   only this key is dropped
[:]..this_is_fine = 1
```

### ⚡ 4. `N?` vs `?N`

```fmjaml
[:]..a = ;?N; "abc"    # ✗ ? passes "abc", then N coerces it to 0 — key kept
[:]..b = ;N?; "abc"    # ✔ N coerces to "", then ? drops the key
```

**Coerce first, then test.**

### ⚡ 5. `N!'0'` puts the zero back

```fmjaml
[:]..x = ;N!'0';  "0"   # ✗ → 0   (! blanks it, then N turns "" back into 0)
[:]..y = ;N!'0'?; "0"   # ✔ key dropped
```

`!` only blanks the value — you still need `?` to drop the key.

### ⚡ 6. `B`, `A` and `O` never look empty

A bare `?` is useless with them. Say what "empty" means:

```fmjaml
[:]..a = ;B!'0'?;  «value»   # drop unless true
[:]..b = ;A!'[]'?; «value»   # drop if []
[:]..c = ;O!'{}'?; «value»   # drop if {}
[:]..d = ;***?B;   «value»   # drop if blank, else boolean
```

### ⚡ 7. The DPS needs both semicolons

```fmjaml
[:]..half = ;        # ✗ → "?"
[:]..half = ;;       # ✔ empty DPS
[:]..half = ;N;42    # ✔
```

### ⚡ 8. Decimal separators are locale-dependent

`n = 4.321` is a number in an English locale and a string in a German one. Force it:

```fmjaml
[:]..a = ;N; 4.321
[:]..b = ;'1'/'2'N;         # → 0.5, whatever the locale
[+].Pause.duration = 500/1000
```

### ⚡ 9. Run-together action names do not work

Name normalisation is `Proper()` + strip separators, so `GoToLayout` becomes `Gotolayout` and
matches nothing. Use `Go to Layout` or `go_to_layout`.

### ⚡ 10. `layout_name` is literal — unless you say `by = "name"`

```fmjaml
[+].Go to Layout = "Home"                 # literal layout called Home
[+].Go to Layout
[:]..by          = "name"                 # ← makes layout_name a calculation
[:]..layout_name = == $target_layout
```

The same distinction applies to `script_name` (use `script_name.calculation`).

### ⚡ 11. `Prev` is not `Previous`

`Go to Record/Request/Page = "Prev"` fails fast on purpose. Write `Previous`.

### ⚡ 12. fmJAML comments vs comment actions

```fmjaml

# vanishes entirely

[+].# = == becomes a "#" element in the action array
[+].# careful — the legacy form breaks if the text contains a dot
```

### ⚡ 13. Heredoc markers are found by plain substring search

If your block contains `===`, use an identifier:

```fmjaml
[+].Set.$js = =====js
value === 42
===js
```

Also remember: the newline before the closing marker is not part of the value. Leave a blank
line if you want a trailing carriage return.

### ⚡ 14. Reserved variables

Anything named `$fmide__*`, `$$fmide__*`, `$fmJAML__*` or `$$fmJAML__*` belongs to the
interpreters. `Set` on one raises error `1300`.

### ⚡ 15. Errors interrupt you unless you capture them

Without `Set Error Capture = 1`, fmIDE shows its own dialog for every *newly thrown* error.
Turn capture on in any script that tests `$$fmide_last_error` itself.

### ⚡ 16. `Set Field` needs the field on the layout

Exactly like the script step. Use `Set Field By Name` when it is not.

### ⚡ 17. Not everything comes back

Some GUI actions (`Open Manage Custom Functions`, `Open Manage Custom Menus`,
`Open Manage Security`, `Go to Account`) hand control to FileMaker and the calling script may
not resume. Put them last, or accept the hiatus.

### ⚡ 18. fmIDE needs Full Access

Without `[Full Access]` fmIDE exits immediately with error `9`.

---

## 5.3 Quick reference card

```fmjaml
#!fmjaml                                   # optional shebang / marks the text as fmJAML
---                                        # optional frontmatter
$name = "World"
---
[+].Action Name                            # new action, no parameters
[+].Action Name = «short form value»       # new action, default parameter
[+].Action Name.«param» = «value»          # new action, first parameter inline
[:]..«param»            = «value»          # …another parameter of the same action
[+].Set.$var            = == «calculation»  # target-key form
[+].// Action Name                         # disabled action
[+].# = == comment action

# fmJAML comment (invisible)

```

| Value form | Meaning |
|---|---|
| `= «calc»` | fmJAML evaluates it |
| `= == «calc»` | raw text → fmIDE evaluates it |
| `= === … ===` | raw block → fmIDE evaluates it |
| `= ==== «text»` | quoted text → fmIDE evaluates it back to the literal |
| `= ===== … ===` | quoted block → literal multi-line text |
| `= ;«DPS»; «calc»` | with data processing |

| DPS essentials | |
|---|---|
| `T N B D I M R A O J U` | data types |
| `?` `-` `:` `,` | present / absent / otherwise / end scope |
| `*` `**` `***` `****` `*****` | trim → super-trim → compact JSON → format JSON |
| `!'x'` | blank the value if it equals `x` (sticky) |
| `'x'` `` `calc` `` | literal / computed value |
| `¶1` `¶'x'` | first line / replace EOLs |
| `'a'>'b'` `~a~>~b~` | substitute / regex replace 🔌 |
| `/` | divide (locale-proof decimals) |
| `version` `info` | fmJAML version stamps |

---

[← Action Reference](04-action-reference.md) · [Index](README.md)
