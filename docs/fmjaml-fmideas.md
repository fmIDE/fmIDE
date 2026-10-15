# Writing fmJAML and fmIDEAS

fmJAML - FileMaker JSON as a Markdown Language - constructs JSON (elegantly).

fmIDEAS is an fmIDE Action Script, usually written in fmJAML - a text based dynamic FileMaker script, if you like.

/*
fmIDE executes it; fmIDE-CLI dispatches it. Keep those four layers distinct.
Use fmIDEAS for supported navigation, calculations, record operations, local Data API queries, backups, exports and repeatable tests.
Use the native script editor for implementation changes that the action API cannot safely perform.
Use Python for filesystem orchestration, comparisons and packaging; the calculations still run in FileMaker.
*/

## Build a structure

```fmjaml
person
.name = "Russell"
.age = == 42 + Random * 20
.active = true
.tags[+] = "FileMaker"
.    [+] = "MrWatson"
     [+] = "ToolMaker"
       ] = "AI+U+Me"
```

Dots introduce object keys, brackets address arrays, `[+]` appends, and `[:]` refers to the last array element. An omitted repeated key inherits the previous key at that level. Prefer explicit paths until the structure is clear.

An action script is an array of single-action objects:

```fmjaml
[+].Go to Layout
[:]..layout_name = "fmIDE Tests"
[+].Set.$answer = == 6 * 7
[+].Exit Script = == $answer
```

Here `[:]..layout_name` means the `layout_name` parameter of the preceding action. Compare an action's short and long forms in the [action reference](actions/README.md);

## Format like FileMaker statements

All fmIDEAS written in fmJAML should look as much like native FileMaker statements as possible. Apply this to handwritten and generated scripts, macros, test records and documentation examples.

- Use short forms, where possible, to reduce noise and actions on one line.
- Indent the body of each `If`, `Loop` or other block by **two spaces** per level. Align `Else If`, `Else`, `End If` and `End Loop` with their opening action.
- Keep the array-path prefix (`[+].` or `[:].`) at the start of the line. Place indentation **after that prefix**, before the action name or the leading dot of `.parameter_name`.
- Use spaces, **never tabs**, for indentation. Fixed two-space levels avoid visual inconsistencies and recognition problems caused by different tab stops.

```fmjaml
[+].If = == $ready
[+].  Loop
[+].    Set
[:].    .target = "$answer"
[:].    .calculation = == 6 * 7
[+].    Exit Loop If = == 1
[+].  End Loop
[+].Else
[+].  Set.$answer = == 0
[+].End If
[+].Exit Script = == $answer
```

The parameter lines above follow their action's block indentation: the spaces are between `[:].` and `.target` or `.calculation`.

## File paths

Use `.file_path` for a (FileMaker) filesystem path: Create Data File, Delete File, Get File Exists, Get File Size, Open Data File, Recover File, Rename File, Save a Copy as, and Save a Copy as XML. Supply a calculation that returns a FileMaker-format path.

```fmjaml
[+].Get File Exists
[:]..file_path = == $file_path
[:]..target = "$exists"
```

From v0.95, Recover File still accepts `.file`; Delete File accepts `.target_file`; Get File Exists, Get File Size, Open Data File and Rename File accept `.source_file`. When both keys are present, `.file_path` wins even when empty or null. Only the selected expression is evaluated, once. Existing short forms expand to `.file_path`.

Keep `.file` for a database name, `.file_id` for an open data-file handle, `.new_name` for Rename File's new filename, and `.target` for an output variable or field. These represent different things.

## Preserve calculation text until runtime

The `=` after the key separates the path from its value. The following value operator determines how fmJAML builds the JSON:

| Source | JSON contains | Intended use |
| --- | --- | --- |
| `key = "Hello"` | `Hello` | Literal parameter |
| `key = $name` | The current value of `$name` | Construction-time evaluation |
| `key = == $name` | `$name` | A calculation for later execution |
| `key = ==== Hello "Russell"` | A quoted calculation string | A runtime literal, without hand escaping |

For multiline calculation text, use a raw here-text:

```fmjaml
[+].Exit Script = ===
JSONSetElement ( "{}"
; [ "answer" ; $answer ; JSONNumber ]
; [ "file_name" ; Get ( FileName ) ; JSONString ]
)
===
```

For multiline **literal** text passed to a calculation parameter, use a quoted here-text:

```fmjaml
[+].Set.$message = =====
Hello "Russell"
This text contains quotes and a second line.
=====
[+].Exit Script = == $message
```

Choose a delimiter that does not appear inside its payload. Nested macro definitions can instead be built with a real JSON serializer; that removes delimiter collisions without changing the stored fmJAML.

`Set.$answer` uses the key as the variable target. `Set.Table::Field` similarly selects a field target. Keep runtime expressions after `==`; otherwise fmJAML may evaluate them before preceding actions have created their variables.

Data-processing specifiers run while fmJAML constructs JSON. They do **not** format a later fmIDE result. In particular, `;M;` cannot pretty-print JSON that an action has yet to calculate. Call `JSONFormatElements` in the runtime expression instead.

The supported structured `Execute FileMaker Data API.request` is useful for static request data. Do not generalize that into runtime evaluation of arbitrary structured `Set` or `Exit Script` leaves. Return a JSON object using a normal runtime `JSONSetElement` calculation, as above. Exit Script's long parameter is **`script_result`**.

## Frontmatter and macros

Frontmatter is a FileMaker variable-definition block, evaluated before the actions:

```fmjaml
---
$name = "Russell" ;
$limit = 10 ;
---
[+].Exit Script = == $name
```

Use named, lower_snake_case inputs. Avoid hidden dependencies on globals. Stored macro frontmatter follows supplied frontmatter, so an unconditional stored assignment overrides the caller. Use defaults that preserve supplied values; distinguish missing, empty and zero when the contract needs that distinction.

```fmjaml
[+].fmIDE Define Macro.Greeting = =====
[+].Exit Script = == JSONSetElement ( "{}" ; "greeting" ; "Hello " & $name ; JSONString )
=====
[+].fmIDE Run Macro.Greeting = ==== $name = "Russell";
[+].Exit Script = == Get ( ScriptResult )
```

Define replaces an existing macro of that name. Check for collisions before installing a library. Read `Get ( ScriptResult )` immediately after Run Macro. Macros require FileMaker 26's persistent store.

## Verify errors and identity

`Set Error Capture` suppresses the engine's error dialogue; it does not abort your action script. Check `$$fmide_get_last_error` immediately after a fallible action, before another action can replace it. Save code, detail, location and description together when preserving an error across cleanup.

Before editing a record, verify file path, layout/table and UUID. After `New Record`, verify its assigned UUID; after setting fields, commit and read back the stored values. A successful dispatch or a displayed progress message is not evidence of a successful mutation.

Use unique fixture names, restore globals, close only your own data-file handles, and delete only your own temporary files. Keep the first failure when cleanup also fails.

## Native Test records

Read a neighboring complete record before creating one. Supply title, description, suite, category, sort, target action/usage, source, expected result, preconditions and active/manual flags where applicable. Calculated fields such as `CodeUnderTest` and syntax/status fields are not inputs.

```fmjaml
# Arrange
[+].Set.$answer = == 0
#@test
[+].Set.$answer = == 6 * 7
#@endtest
# Assert by returning a stable value for TestExpectedResult
[+].Exit Script = == $answer
```

Use `#@test` and `#@endtest` to identify the code under test. Put setup and cleanup outside them. Prefer self-contained cases for empty/zero, Unicode, aliases, calculation timing and error paths. Avoid side effects in preconditions: their evaluation is currently inconsistent (issue #203).

Find the exact new UUIDs, verify the found set, and run **Tests: Run Found Tests automatically**, the equivalent of **Run These Tests**. Inspect stored actual/expected results, fmIDE error fields, pass/fail and skipped counts. Manual tests need their separate manual run. Preserve UUID order when using the existing renumber script.

The [saved native regression records](../tests/fmIDEAS/README.md) are working examples. Suite 5 also contains sketches, disabled experiments and known broken examples; treat them as design evidence, not automatically as correct templates.
