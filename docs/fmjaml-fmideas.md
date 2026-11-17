# Writing fmJAML and fmIDEAS

fmJAML - FileMaker JSON as a Markdown Language - constructs JSON (elegantly).

fmIDEAS is an fmIDE Action Script, usually written in fmJAML - a text based dynamic FileMaker script, if you like.

Save action scripts with the `.fmIDEAS` extension, whether their contents use
fmJAML or JSON. The extension identifies the action script; its contents identify
the format. Reserve `.fmJAML` for general fmJAML documents that are not action
scripts.

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

## Value operators and fmIDE's second evaluation layer

fmJAML first constructs JSON. fmIDE then executes that JSON as an Action Script, and most action parameters are evaluated as FileMaker calculations at the moment the action runs.

That gives fmIDEAS two evaluation layers:

```text
fmJAML source
    │
    │  1. fmJAML constructs the JSON
    ▼
JSON Action Script
    │
    │  2. fmIDE evaluates calculation parameters
    ▼
running FileMaker action
```

This second layer is why the text and text-to-quote value operators are especially useful in fmIDEAS.

**fmJAML value operators are designed so that you never need to manually escape a string.**

### No value operator (normal single-line calculation)

**fmJAML:**

```fmjaml
value = 42
```

**JSON:**

```json
{"value":42}
```

#### How it works

```text
value = Evaluate ( «single-line-calculation» )
```

fmJAML evaluates the calculation while constructing the JSON. Simple values such as `42`, `true`, and `false` visually resonate with the JSON value they produce.

In an fmIDEAS parameter this means the expression is resolved **before the Action Script begins to run**. Do not use the bare form when the expression depends on variables or state created by earlier actions.

#### Syntax

```fmjaml
«path» = «single-line-calculation»
```

### Value operator `=` (multiline calculation operator / 'herecalc' operator)

**fmJAML:**

```fmjaml
value = =
Let ( [
    a = 6 ;
    b = 7
] ;
    a * b
)
===
```

**JSON:**

```json
{"value":"42"}
```

#### How it works

```text
value = Evaluate ( «multiline-calculation» )
```

The herecalc is the multiline counterpart of the normal calculation form. It is evaluated by fmJAML while constructing the JSON.

#### Syntax

```fmjaml
«path» = =
«multiline-calculation»
===
```

### Value operator `==` (single-line text-value / 'hereline' operator)

**fmJAML:**

```fmjaml
[+].Set.$answer = == 6 * 7
```

**JSON contains:**

```json
[{"Set":{"$answer":"6 * 7"}}]
```

When the `Set` action runs, fmIDE evaluates `6 * 7`, so `$answer` becomes `42`.

#### How it works

fmJAML takes the remainder of the line literally:

```text
value = «single-line-text-as-is»
```

For fmIDEAS this is normally **calculation text for later evaluation by fmIDE**.

#### Syntax

```fmjaml
«path» = == «single-line-text»
```

### Value operator `===` (multiline text-value operator)

**fmJAML:**

```fmjaml
[+].Exit Script = ===
JSONSetElement ( "{}"
; [ "answer" ; $answer ; JSONNumber ]
; [ "file_name" ; Get ( FileName ) ; JSONString ]
)
===
```

The JSON contains that multiline FileMaker calculation as text. When `Exit Script` runs, fmIDE evaluates it.

#### How it works

```text
value = «multiline-text-as-is»
```

This is the multiline counterpart of `==`: fmJAML preserves the calculation text so fmIDE can evaluate it later.

#### Syntax

```fmjaml
«path» = ===
«multiline-text»
===
```

An optional **identifier** can make the block unambiguous when the payload itself contains `===`:

```fmjaml
[+].Set.$javascript = ===JS
return value === 42;
===JS
```

The identifier is `JS`; the complete closing marker is `===JS`.

### Value operator `====` (single-line text-to-quote operator)

**fmJAML:**

```fmjaml
[+].Set.$message = ==== "Hello Foo", said Baz in the bar.
```

The source text is:

```text
"Hello Foo", said Baz in the bar.
```

fmJAML places a quoted FileMaker calculation into the JSON:

```text
"\"Hello Foo\", said Baz in the bar."
```

When fmIDE evaluates that calculation, the result is exactly:

```text
"Hello Foo", said Baz in the bar.
```

#### How it works

**Text-to-quote takes the text as written and produces a FileMaker calculation which evaluates back to exactly that text.**

```text
value = Quote ( «single-line-text» )
```

That is precisely what fmIDEAS needs when a parameter will be evaluated by fmIDE, but the desired runtime result is literal text rather than a calculation result.

#### Syntax

```fmjaml
«path» = ==== «single-line-text»
```

### Value operator `=====` (multiline text-to-quote operator)

**fmJAML:**

```fmjaml
[+].Set.$message = =====MESSAGE
"Hello Foo",
said Baz
in the bar.
===MESSAGE
```

fmJAML turns the complete block into a quoted FileMaker calculation. When fmIDE evaluates that calculation, `$message` receives exactly the multiline text written in the source.

#### How it works

```text
value = Quote ( «multiline-text» )
```

This is the multiline counterpart of `====`.

#### Syntax

```fmjaml
«path» = =====«identifier»
«multiline-text»
===«identifier»
```

The identifier is optional. Both `===` and `=====` blocks use a closing marker beginning with exactly `===`; when an identifier is present, repeat it after those three equals signs.

### The fmIDEAS rule of thumb

For parameters that fmIDE evaluates as calculations:

| You want fmIDE to… | fmJAML form |
| --- | --- |
| evaluate a one-line calculation later | `= == «calculation»` |
| evaluate a multiline calculation later | `= === «calculation» … ===` |
| receive one-line literal text after evaluation | `= ==== «text»` |
| receive multiline literal text after evaluation | `= =====«identifier» … ===«identifier»` |

So in fmIDEAS:

- `==` / `===` mean **preserve this as calculation text for fmIDE to evaluate later**.
- `====` / `=====` mean **text-to-quote: make a calculation that evaluates back to this literal text**.
- the bare form and herecalc `=` are evaluated by fmJAML **up front**, before the first action executes.

For example:

```fmjaml
[+].Set.$n = == 1
[+].Set.$n = == $n + 1
[+].Exit Script = $n      # evaluated by fmJAML before the actions run
[+].Exit Script = == $n   # evaluated by fmIDE when this action runs
```

Anything that depends on what an earlier action did should normally use `==` or `===`.

Not every fmIDE parameter is calculation-valued. Some identifiers and explicit literal parameters are consumed directly; consult the relevant [action reference](actions/README.md) when that distinction matters.

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
===
[+].fmIDE Run Macro.Greeting = ==== $name = "Russell";
[+].Exit Script = == Get ( ScriptResult )
```

Define replaces an existing macro of that name. Check for collisions before installing a library. Read `Get ( ScriptResult )` immediately after Run Macro. Macros require FileMaker 26's persistent store.

### Macro definition contract

The renamed contract uses `macro_name`, optional `metadata`, and `script`. It requires a supporting fmIDE build; the older `name`/`code` stored keys are not aliases assumed by these examples.

```fmjaml
[+].fmIDE Define Macro
[:]..macro_name = == "Greeting"
[:]..metadata.description = "Return a greeting"
[:]..script = =====GREETING
[+].Exit Script = == "Hello"
===GREETING
[+].fmIDE Get Macro
[:]..macro_name = == "Greeting"
[:]..target = "$macro"
[+].Exit Script = == JSONGetElement ( $macro ; "script" )
```

Define evaluates the name and script calculations once and stores their results. The script text is executed later by Run Macro; metadata stays data. Get returns the stored object, for example:

```json
{
  "macro_name": "Greeting",
  "metadata": {"description": "Return a greeting"},
  "script": "[+].Exit Script = == \"Hello\""
}
```

Alphabetical presentation puts identity first, metadata second and implementation last. Read properties by key, never by their position. The dot-name shorthand, Run frontmatter and Get target keep their existing roles. Keys inside metadata and result objects, such as `error.code`, are unaffected.

The Define Macro and Get Macro action pages include repository corrections for this contract, explicitly marked as awaiting synchronization to their database documentation. Other generated content and the source XML/exploded scripts retain their last export provenance. Synchronize the database documentation and refresh those exports after reviewing the native implementation and its tests.

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
