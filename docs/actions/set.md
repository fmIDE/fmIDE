<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set`

Assign a calculation result to a variable or field; the target can be a parameter or a key such as Set.$name.

[All actions](README.md)


| Alias | FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|---------|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Field / Set Variable](set-field.md)| None | Yes | ok | v0.29 |

## Description

Assign the result of a calculation to a variable or field. `Set`, `Set Variable` and `Set Field` share the same implementation: a target beginning with `$` selects a variable; other targets select fields.

- `target`: literal variable or `table::field` name. It can also be supplied in the action key, as in `Set.$count`.
- `calculation`: the expression to evaluate when this action executes.
- `repetition`: optional calculation returning the repetition number; omitted means the first repetition.

The target parameter aliases are checked in this order: `target`, `name`, `field_name`, `variable_name`; the first non-empty value wins. Prefer `target` in new code. Names beginning with `$fmide__` are reserved for fmIDE internals.

Use `= ==` to preserve a calculation for runtime evaluation. A bare `=` lets fmJAML evaluate while constructing the action script, before earlier actions have run. To assign JSON, use an explicit JSON-producing calculation such as `JSONSetElement`.

For a target name calculated at runtime, use `Set Field By Name`.

## Full Syntax

```
[+].Set.$quantity = == 3
[+].Set
[:]..target = "$items"
[:]..repetition = == 2
[:]..calculation = == $quantity * 12
[+].Exit Script = == $items[2]
```

## Usage

### Set.$var
.foobar




> ---
> 
> #### Test Case #1 "Set $i = 42 ..target..calculation (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set
> [:]..target = "$i"
> [:]..calculation  = 42
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set $i = 42 ..target..calculation (long form safe)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set
> [:]..target = "$i"
> [:]..calculation  = == 40 + $fmide__action_index_max /* max = number of actions in this action script = 2 */
> ```
> 
> 
> ##### Description
> 
> The `==`is important here
> 
> 
> 
> ---
> 
> #### Test Case #3 "Set $i = 42 (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set.$i=42
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Set.$$text = == (short form with hereline)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set.$$text = == "Hello World"
> 
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Set $variable.name.with.dots (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set.$variable.name.with.dots=42
> ```
> 
> 
> ##### Description
> 
> Repetition short form with number in apostrophes is NOT SUPPORTED.
> 
> 
> 
> ---
> 
> #### Test Case #6 "Set $forty.2 (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set.$forty.2=42
> ```
> 
> 
> ##### Description
> 
> Test repetition short form with number.
> 
> 
> 
> ---
> 
> #### Test Case #7 "Set repetition $i[2] with integer repetition (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set
> [:]..target= "$i"
> [:]..repetition = 2
> [:]..calculation = 42
> ```
> 
> 
> ##### Description
> 
> Test repetition parameter.
> 
> 
> 
> ---
> 
> #### Test Case #8 "Set repetition $i[2] with integer repetition (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set.$i[2]=42
> ```
> 
> 
> ##### Description
> 
> Test repetition short form.
> 
> 
> 
> ---
> 
> #### Test Case #9 "Set repetition $i[$forty.2]  calculated repetition (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set.$forty.2 = 42
> [+].Set
> [:]..target= "$i"
> [:]..repetition = == $forty.2
> [:]..calculation = == $forty.2
> ```
> 
> 
> ##### Description
> 
> Test repetition parameter.
> 
> 
> 
> ---
> 
> #### Test Case #10 "Error: Set (no target → 5)"
> 
> ##### Status
> 
> ✅ Pass 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set=1
> ```
> 
> 
> ##### Description
> 
> Set the default variable $$ to 1
> 
> 
> 


## See also

- [Set Variable](set-variable.md)
- [Set Field](set-field.md)
