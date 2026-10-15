# FileMaker code in MrWatson style

Write code whose structure explains its work. This guide is drawn from the current fmIDE script, its custom functions and the existing Naming Conventions wiki page. Keep the style of the section you are editing; do not reformat unrelated code.

## Native scripts

Use comments and blank steps to expose the stages of the operation. In an fmIDE action branch, the recurring shape is:

```text
Else If [ $fmide__action_name = "ActionName" ]
    # Process Short Form
    …

    # Params
    …

    # Calculations
    …

    # Defaults
    …

    # Action
    …

    # Reset Vars
    …
```

These are stages, not a mandatory template. Defaults may depend on earlier results; some branches omit or reorder stages. Preserve those dependencies. Keep native FileMaker script-step indentation and place comments at the level they explain.

- Keep aliases together when they share an implementation. State any alias-specific default explicitly.
- Make shorthand expansion an ordered choice: type or shape → target parameter. Do not silently change the precedence of matching rules.
- Keep the navigation chain visible: select the script/start step → search from there → extend the selection. The new `+` end-step form is relative after search; its behavior is distinct from `%`.
- Destructure parameters together, evaluate at the required stage, perform the operation, then clear branch-local working variables. Retain a type variable only while later code needs that type.
- Capture `Get ( LastError )` and `Get ( LastErrorDetail )` immediately after the native operation. Another step can change them.
- Comment on a reason, contract or dependency. Keep useful section comments and spacing when refactoring.

## fmIDEAS in fmJAML

Make fmIDEAS resemble native FileMaker statements: indent block bodies with two spaces per level, placing the spaces after `[+].` or `[:].` and before the action name or `.parameter_name`. Never use tabs for indentation. See the [fmJAML formatting rules and example](fmjaml-fmideas.md#format-like-filemaker-statements).

## Names and scope

| Context | Convention |
| --- | --- |
| Action names | Headline Case: `Go to Layout` |
| Public JSON parameters / frontmatter variables | `layout_name`, `$layout_name` |
| New bridge-macro inputs | Clearly named `$lower_snake_case` |
| Script-local variables | `$name`; use a module prefix where appropriate |
| File globals | `$$name`; use only when that lifetime is needed |
| fmIDE internals | Existing `$fmide__…` and `$fmide___…` families; reserved for the engine |
| Calculation-local variables | The wiki recommends `¢lower_snake_case`; many existing functions use `vName` |
| Custom-function parameters | Existing functions commonly use `pName`; retain their public signatures |

Do not turn an observed convention into a bulk rename. A bare `vName` or `¢name` is calculation-local; `$name` has script scope. A custom function that writes `$` or `$$` variables has side effects: document them.

## Calculation layout

Use spaces around argument separators and operators. For a substantial expression, put the outer function, variable block and result on separate lines. Leave space around the major sections:

```filemaker
Let(
[

vText = Trim ( pText ) ;
vLength = Length ( vText )

];

Case(

vLength = 0 ; "" ;
vLength <= pMaximumLength ; vText ;

Left ( vText ; pMaximumLength )

)

)
```

This is a formatting example, not a new installed function. Existing code uses both `Let(` and `Let (`: preserve the surrounding choice. Do not mechanically reindent the variable block several levels just because its enclosing script step is nested; the calculation editor provides its own context.

### Ordered choices

In `Case`, keep a short condition and its result on one line. Separate longer alternatives with blank lines or a short comment. Put the fallback last. Preserve the order: first match wins.

```filemaker
Case(

/* Explicit name takes precedence */
not IsEmpty ( vName ) ; vName ;

/* Otherwise derive it from the number */
vNumber > 0 ; GetValue ( vNames ; vNumber ) ;

""

)
```

### JSON construction

Use the multi-entry `JSONSetElement` form. Put the semicolon at the **start** of each entry line; align the brackets so entries can be inserted or removed without repairing the preceding line.

```filemaker
JSONSetElement ( "{}"
; [ "ok" ; vError = 0 ; JSONBoolean ]
; [ "error" ; vError ; JSONNumber ]
; [ "data" ; vData ; JSONObject ]
)
```

Choose the JSON type deliberately. `JSONObject` and `JSONArray` require structured JSON; use `JSONString` for ordinary text, including text that merely looks like JSON. Do not add JSON quotes to a public interface that promises plain text.

### Iteration

Lay out `While` so initialization, condition, update and result are easy to find. Initialize each accumulated value outside the loop and make progress explicit:

```filemaker
While(
[

vI = 1 ;
vN = ValueCount ( pValues ) ;
vResult = "[]"

]; vI <= vN ;[

vValue = GetValue ( pValues ; vI ) ;
vResult = JSONSetElement ( vResult ; "[+]" ; vValue ; JSONString ) ;
vI = vI + 1

];

vResult

)
```

Use a script loop where it makes the native operations clearer. Do not introduce custom-function recursion merely to traverse values that a `While` can handle.

### Runtime expressions and side effects

Evaluate a supplied expression once, store its result, and use that value. Do not evaluate again merely to inspect its error. A retry can repeat variable increments, plugin calls or other side effects.

Keep expression text distinct from its result. In fmIDEAS, fmJAML construction happens before the action runs; a value already evaluated during construction cannot recover its original expression later.

## Custom functions

Give a nontrivial function a useful opening comment: signature, result, parameter meanings, dependencies and side effects. Keep history short or point to the existing history location.

```filemaker
/* FunctionName ( pText ; pMaximumLength )

Return …

@param pText (text) - …
@param pMaximumLength (number) - …
@returns text - …

20261014 codex: …
*/
```

Use the actual signature, including parameter order and casing. Document units and empty-input behavior where they matter. Prefer local intermediate values over repeating a long expression. Avoid introducing globals into a pure helper.

For very small private helpers, an obvious one-line expression can be sufficient. Do not copy a large header onto every trivial wrapper. Existing functions contain historical naming and formatting variations; preserve their contracts while improving the part being changed.

## Review before saving

Check the semantic boundaries: literal versus calculation, empty versus zero, object versus array, default versus supplied value, and caller scope versus callee scope. Use focused examples for the changed behavior.

For a native script change, keep a recoverable backup, add a concise `codex` change comment when requested, save, export XML, and compare only the intended steps. Generated readable source is an inspection view; consult native XML `StepText` when the exploder omits an option or repetition.

## Source examples

- fmIDE script: action stages, shared handlers, parameter extraction and cleanup.
- `_LookupValue`: compact `Let` with a separated result.
- `_Stubify`: a readable `While` with progress and accumulator variables.
- `_ColorImageRGB`: parameter documentation and staged calculation.
- `fmJAML`: public contract, internal scope and explicit input/output variables.
- Existing wiki: [fmIDE Naming Conventions](https://github.com/fmIDE/fmIDE/wiki/fmIDE-Naming-Conventions).
