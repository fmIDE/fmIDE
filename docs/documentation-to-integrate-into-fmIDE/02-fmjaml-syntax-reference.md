# 2. fmJAML Syntax Reference

[← fmIDE Action Scripts](01-fmide-action-scripts.md) · [Index](README.md) · [Next: Writing Action Scripts →](03-writing-action-scripts.md)

---

fmJAML is a line-oriented DSL that compiles text into JSON. It is a general-purpose JSON
templating language — it just happens to have been invented for writing fmIDE action scripts.

This page is the language reference. For how to *apply* it to fmIDE, see
[Writing Action Scripts](03-writing-action-scripts.md).

## 2.1 The line

Every fmJAML line has the shape:

```
«path» [ = [;«DPS»;] [«value-operator»] «expression» ]
```

- **`«path»`** — a FileMaker JSON path (`person.name`, `[+].Beep`, `array[0]`, `[:]..title`)
- **`;«DPS»;`** — the optional [Data Processing String](#26-the-data-processing-string-dps)
- **`«value-operator»`** — optional `==`, `===`, `====` or `=====` (see [§2.4](#24-values-and-value-operators))
- **`«expression»`** — a FileMaker calculation, or (with a value operator) raw text

Each line is **horizontally trimmed** first, so leading/trailing spaces and tabs are free.

```fmjaml
person.name = "John"
person.age  = 42
```

```json
{ "person" : { "age" : 42, "name" : "John" } }
```

### Lines that are ignored

| Line | Meaning |
|------|---------|
| *(empty)* | ignored |
| whitespace only | ignored |
| `# anything` | comment — ignored entirely |
| `#!fmjaml` | shebang — a comment, but also marks the parameter as fmJAML for fmIDE |

The `#` must be the first non-whitespace character. Indented comments are fine:

```fmjaml
[+].Loop
	# this comment never reaches the JSON
[+].	Exit Loop If = "$i > 10"
[+].End Loop
```

> **Do not confuse** a *fmJAML comment* (`# …`, disappears) with an *fmIDE comment action*
> (`[+].# = == …`, becomes a `#` element in the action array). See
> [§3.5](03-writing-action-scripts.md#35-comments-and-disabling-actions).

## 2.2 Path stubs, null and defaults

| fmJAML | JSON | Rule |
|--------|------|------|
| `person` | `{"person":{}}` | no `=` → **object** |
| `person =` | `{"person":null}` | `=` but no expression → **null** |
| `n = 42` | `{"n":42}` | expression *is* a plain number → **number** |
| `n = 4,321` | `{"n":4.321}` | …using the *current locale's* decimal separator |
| `b = true` | `{"b":true}` | `true`/`false` → **boolean** |
| `s = "abc"` | `{"s":"abc"}` | anything else → **string** |
| `n = 1+1` | `{"n":"2"}` | `1+1` is not a plain number, so the *evaluated* result is stored as a **string** |
| `n = ;N; 1+1` | `{"n":2}` | …force the type with the DPS |

> ⚠️ **Locale**: automatic number detection uses `GetAsNumber(«expression») = «expression»`.
> `4.321` is a number in an English locale and a string in a German one. When it matters,
> say `;N;` explicitly, or use the division operator (`;'1'/'2'N;` → `0.5`) to avoid hard-coding
> a decimal separator.

## 2.3 Paths, arrays and path inheritance

### Array append `[+]` and last element `[:]`

```fmjaml
[+].name = "Alice"
[:].owns = "looking glass"
```

```json
[ { "name" : "Alice", "owns" : "looking glass" } ]
```

- `[+]` — append a new element to the array
- `[:]` — address the **last** element of the array

FileMaker only supports `[+]`/`[:]` natively from v21. fmJAML detects the version and
emulates them on older versions via `ValueCount(JSONListKeys(…))`, so **your fmJAML works on
FileMaker 19 and 20 too**.

### Path inheritance

An **empty key** between delimiters inherits the corresponding key from the *previous* line's
path. This is what makes fmIDE action scripts readable.

```fmjaml
[+].person
[:]..name = "John"
[:]..age  = "42"
```

```json
[ { "person" : { "name" : "John", "age" : "42" } } ]
```

Line 2's path is `[:]..name`: the `..` means "reuse the key that was in this position last
time" — i.e. `person` — giving `[:].person.name`.

Any number of levels can be inherited, and the delimiter characters `.`, `[` and `]` all
participate:

```fmjaml
[+].#
[:]..array[+] = 1
[:].        ] = 2
[:].        ] = 3
```

```json
[ { "#" : { "array" : [1,2,3] } } ]
```

Here `.    ]` inherits `.array[+]` from the previous path and appends to the array — the
whitespace is only there to line the code up.

Equivalent array-append spellings, all valid:

```fmjaml
[:].#.array.[+].Beep
[:].#.array[+].Boop
[:].#.array..[+].Barp
```

> **Known limitation (v0.31):** path inheritance is fully implemented for *array* paths
> (`[:]..key`). Pure object-path inheritance (`person` / `.name` / `.age` on consecutive
> lines) is still under construction. In fmIDE action scripts you are always inside an array,
> so this rarely bites.

## 2.4 Values and value operators

This is the most important section of the language.

By default the expression after `=` is a **FileMaker calculation and fmJAML evaluates it**:

```fmjaml
greeting = "Hello " & "World"     →  { "greeting" : "Hello World" }
today    = ;D; Get ( CurrentDate ) →  { "today" : "2026-07-23" }
```

The **value operators** change that, and remove the need for escaping:

| Operator | Reads | Result placed in the JSON | Mnemonic |
|----------|-------|---------------------------|----------|
| *(none)* | rest of line | `Evaluate ( text )` | a calculation |
| `==` | rest of line | the text, **raw** | *hereline* — one line of literal text |
| `===` | until closing `===` | the block, **raw** | *heredoc* — a block of literal text |
| `====` | rest of line | `Quote ( text )` | a *quoted* hereline |
| `=====` | until closing `===` | `Quote ( block )` | a *quoted* heredoc |

```fmjaml
a =      "Hi Foo!" said Baz          # ✗ syntax error when evaluated
b = == "Hi Foo!" said Baz            # → "\"Hi Foo!\" said Baz"
c = ==== "Hi Foo!" said Baz          # → "\"\\\"Hi Foo!\\\" said Baz\""
```

- `==` / `===` give you **the text you typed**, as a JSON string. Use them when the consumer
  (fmIDE!) will evaluate the string as a calculation.
- `====` / `=====` give you **a FileMaker string literal** — the text wrapped in escaped
  quotes. Use them when the consumer evaluates the string but you want a plain literal back.

See [§3.2](03-writing-action-scripts.md#32-the-two-evaluation-layers) for exactly when to
reach for which.

### Heredocs

```fmjaml
text = ===
Hello
World
===
```

```json
{ "text" : "Hello\rWorld" }
```

Rules:

- The closing marker is always **`===`** — even when the opening marker was `=====`.
- An **identifier** may follow the marker; the closing marker must repeat it. Use one whenever
  the block itself might contain `===`:

  ```fmjaml
  [+].Set.$js = =====js
  function isTheAnswer(value) {
    return value === 42;
  }
  ===js
  ```

- The newline *before* the closing marker is **not** part of the value. To end the value with
  a carriage return, leave a blank line before the marker.
- The block is found by plain substring search, so the marker must not occur inside the block.

## 2.5 Data types

Types are chosen automatically ([§2.2](#22-path-stubs-null-and-defaults)) or stated
explicitly in the DPS with a **single letter**. The letters follow FileMaker's own field-type
keyboard shortcuts.

| Letter | Type | JSON output |
|--------|------|-------------|
| `T` | Text | `"…"` (`GetAsText`) |
| `N` | Number | `42` (`GetAsNumber`) |
| `B` | Boolean | `true` / `false` (`GetAsBoolean`) |
| `D` | Date | `"2026-03-23"` — ISO 8601 |
| `I` | tIme | `"01:02:03"` |
| `M` | tiMestamp | `"2026-03-23T01:02:03"` |
| `R` | containeR | `{"file":{"name":"…","data":"«base64 RFC 4648»"}}` |
| `A` | JSON Array | `[…]` |
| `O` | JSON Object | `{…}` |
| `J` | JSON Raw | whatever the text is: array, object, string, number, boolean or null |
| `U` | nUll | `null` |

```fmjaml
[+].#
[:]..date      = ;D; Date ( 3 ; 23 ; 2026 )
[:]..time      = ;I; Time ( 1 ; 2 ; 3 )
[:]..timestamp = ;M; Timestamp ( Date ( 3 ; 23 ; 2026 ) ; Time ( 1 ; 2 ; 3 ) )
[:]..object    = ;O; "{\"n\":12}"
[:]..null      = ;U; "whatever"
```

## 2.6 The Data Processing String (DPS)

The DPS sits between the `=` and the value, delimited by semicolons:

```
«path» = ;«DPS»; «expression»
```

It is a tiny stack-free instruction sequence, processed **strictly left to right with no
operator precedence**. Whitespace inside it is ignored.

```fmjaml
value = ;N?; "42"     # output as a number, drop the key if the number is empty
```

> ⚠️ Both semicolons are required. `= ;N 42` (missing the closing `;`) is not a DPS and
> produces a `?` error. `= ;;42` is a valid, empty DPS.

### 2.6.1 Operator table

| Operator | Name | Effect |
|----------|------|--------|
| `T N B D I M R A O J U` | data type | Coerce and output as that type ([§2.5](#25-data-types)) |
| `*` | trim | `Trim()` — spaces |
| `**` | horizontal trim | spaces **and** tabs |
| `***` | vertical trim ("super-trim") | spaces, tabs **and** newlines |
| `****` | compact JSON | `JSONGetElement ( value ; "" )` |
| `*****` | format JSON | `JSONFormatElements ( value )` |
| `?` | optional | test *presence*: `not IsEmpty(value)`. If the test fails and no `:` clause supplies a value, **the key is dropped entirely** |
| `-` | mapping | test *absence*: `IsEmpty(value)` |
| `:` | otherwise | else-branch of the preceding `?` / `-` test |
| `,` | end scope | close the conditional scope and start a fresh one |
| `!` | not (sticky) | the next value(s) *remove* the value if it matches |
| `'text'` | value | set the value to `text` (a `\¶` inside becomes a real carriage return) |
| `` `calc` `` | eval | set the value to `Evaluate ( calc )`; `$fmJAML__val` holds the current value |
| `¶1` | first line | `GetValue ( value ; 1 )` |
| `¶'x'` | EOL replace | normalise CRLF/LF to CR, then replace CR with `x` |
| `/` | divide | `'1'/'2'` → `0.5` — a locale-proof way to write decimals |
| `>` | replace | `'search'>'replace'` → `Substitute()` |
| `~regex~` | regex | *(MBS only)* used with `!` (match) or `>` (replace) |
| `@'flags'` | regex flags | *(MBS only)* e.g. `@'Caseless,Multiline,NewlineAny'` |
| `#` | comment | ignore the rest |
| `version` | version | output the fmJAML version string, e.g. `0.31` |
| `info` | info | output the full fmJAML info string, e.g. `2026-07-10 @mrwatson-de v0.31` |
| `==version` / `==info` | quoted variants | the same, but `Quote()`d (so fmIDE evaluates them back to the plain string) |

### 2.6.2 Data types

```fmjaml
[+].#.number  = ;N; "4"        # → 4
[+].#.boolean = ;B; 1          # → true
[+].#.text    = ;T; 4          # → "4"
```

### 2.6.3 Optional values (`?`)

`?` drops the key if the value is empty.

```fmjaml
[+].#
[:]..keep = ;?; "hello"        # → "keep":"hello"
[:]..drop = ;?; ""             # key omitted
```

**Coerce first, then test.** Putting the type *before* the `?` means you test the cleaned-up
value, which is nearly always what you want:

| DPS | Behaviour with `"abc"` |
|-----|------------------------|
| `?N` | `?` sees `"abc"` (not empty) → passes → `N` coerces → `0`… key kept |
| `N?` | `N` coerces `"abc"` → `""` → `?` drops the key ✔ |

Combine with trimming:

```fmjaml
[:]..a = ;*?;   "   "       # trim spaces then drop if empty
[:]..b = ;**?;  " \t "      # trim spaces+tabs then drop
[:]..c = ;***?; " \t¶ ¶ "   # super-trim then drop
```

`B`, `A` and `O` never produce an empty value, so a bare `?` is meaningless for them —
state the empty value you mean:

```fmjaml
[:]..trilean       = ;***?B;      «value»   # drop if blank, else boolean
[:]..truelean      = ;B!'0'?;     «value»   # drop unless true
[:]..array         = ;A!'[]'?;    «value»   # drop if []
[:]..object        = ;O!'{}'?;    «value»   # drop if {}
```

### 2.6.4 `?` / `-` / `:` — conditional clauses

- `?` — *if the value is present*
- `-` — *if the value is absent*
- `:` — otherwise
- `,` — end the conditional scope entirely

```fmjaml
[:]..number  = ;?N:T;  «value»   # a number, or "" when empty
[:]..number  = ;?N:U;  «value»   # a number, or null when empty
[:]..boolean = ;?B:U;  «value»   # true / false / null  ("trilean")
[:]..name    = ;***¶1?T:'anonymous'; $name
```

Mapping with `!` + `-`:

```fmjaml
[:]..fixed = ;!'Russel'-'Russell':T; $name        # correct one misspelling
[:]..yesno = ;!'ja'-'yes':!'nein'-'no':T; $answer # ja→yes, nein→no, else unchanged
```

How the chain reads: `!'ja'` removes the value if it is `ja` (making it empty); `-` tests for
emptiness; `'yes'` supplies the replacement; `:` moves on to the next clause; the final `T`
outputs whatever survived.

A larger mapping — log levels 0–10 to names:

```fmjaml
[:]..level = ;N!'''0'-T'off':!'1''2''3'-T'error':!'4''5''6'-T'information':!'7''8''9'-T'debug':T'illegal log level'; $level
```

### 2.6.5 The `!` not operator is sticky

Once `!` is seen, *every following value string* in the clause is a "remove if equal" test:

```fmjaml
[:]..x = ;!'0''1'; «value»    # blank the value if it is 0 or 1
[:]..y = ;!'0'!'1'; «value»   # identical — the repeated ! changes nothing
```

> ⚠️ `!` only *blanks* the value; it does not drop the key. Combine with `?`:
>
> ```fmjaml
> [:]..zero_dropped = ;N!'0'?; «value»   # drop when the number is empty or 0
> [:]..oops         = ;N!'0';  «value»   # 0 is blanked, then N turns "" back into 0 😱
> ```

### 2.6.6 Trimming and JSON formatting

```fmjaml
[:]..compact   = ;****;             "  { \"n\" : 1 } "   # → "{\"n\":1}"
[:]..pretty    = ;*****;            "{\"n\":1}"          # → formatted JSON
[:]..opt_json  = ;***?****!'[]'?;   $maybe_json          # super-trim, drop if blank,
                                                         # compact, drop if []
```

The `***?` prefix is a common idiom: it drops empty input *before* the JSON functions get a
chance to choke on it.

### 2.6.7 EOL handling

```fmjaml
[:]..first    = ;¶1;   "first¶line¶only"    # → "first"
[:]..joined   = ;¶'';  «multi-line»         # remove all EOLs
[:]..spaced   = ;¶' '; «multi-line»         # EOLs → spaces
[:]..standard = ;¶'¶'; «multi-line»         # CRLF/LF → CR
```

### 2.6.8 Replace and regex

```fmjaml
[:]..a = ;'search'>'replace';                      $text
[:]..b = ;'quite'>'really''good'>'great';          $text
[:]..c = ;~Search~>~Replace~;                      $text   # MBS
[:]..d = ;@'Caseless,Multiline,NewlineAny'~^s~>~r~; $text   # MBS, with flags
[:]..e = ;J!~^\?~;                                 $json   # drop invalid JSON
```

`!~regex~` removes the value when the regex matches — the `!~^\?~` idiom above is
"blank it if it starts with a `?`", i.e. if FileMaker's JSON parser reported an error.

### 2.6.9 Literal, computed and version values

```fmjaml
[:]..fixed   = ;'hello world';         «ignored»
[:]..multi   = ;'hello\¶world';        «ignored»
[:]..cleared = ;'';                    «ignored»       # → ""
[:]..calc    = ;`1+1`;                 «ignored»       # → 2
[:]..doubled = ;`$fmJAML__val*2`;      123             # → 246
[:]..half    = ;'1'/'2'N;                              # → 0.5
[:]..version = ;version;                               # → "0.31"
[:]..info    = ;info;                                  # → "2026-07-10 @mrwatson-de v0.31"
```

## 2.7 Calling fmJAML directly

```
fmJAML ( pOptionalInitialJSON ; pFmJAML )
```

- `pOptionalInitialJSON` — JSON to build **on top of** (pass `""` or `"[]"`/`"{}"` to start fresh)
- `pFmJAML` — the fmJAML text
- returns the resulting JSON

fmIDE ships with fmJAML **embedded** so that it has no custom-function dependency. Set
`$fmjaml_per_cf` to true if you want fmIDE to call the `fmJAML` custom function instead
(handy while developing fmJAML itself).

Debugging: set `$fmJAML_debug` to 5 (info), 7 (debug) or 8 (verbose) and read `$$fmJAML_log`.

---

[← fmIDE Action Scripts](01-fmide-action-scripts.md) · [Index](README.md) · [Next: Writing Action Scripts →](03-writing-action-scripts.md)
