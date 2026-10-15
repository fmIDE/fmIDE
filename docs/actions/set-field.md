<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Set Field`

Assign a calculated value to a literal field target, optionally at a specified repetition.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| [Set Field](https://www.filemaker.com/redirects/fmp26_admin.html?page=cs_help&lang=en&hid=26076) | Yes | beta |  |

## Description

Assign a calculated value to a field in the current record context. `target` is a literal `table::field` name; use `Set Field By Name` when an expression must determine that name.

- `target` (or `field_name`): literal field target.
- `calculation`: expression evaluated when this action executes.
- `repetition`: optional calculation returning the repetition number; defaults to the first repetition.

The short form puts the field name in the key. Use `= ==` for runtime calculations. Normal FileMaker field access, record locking and validation rules still apply; committing a record is a separate action.

This action uses the shared Set implementation. The example below uses global fields in the fmIDE test file.

## Full Syntax

```
[+].Set Field.fmIDE_Test::_gTest = == "first"
[+].Set Field
[:]..target = "fmIDE_Test::_gTest"
[:]..repetition = == 2
[:]..calculation = == "second"
[+].Exit Script = == fmIDE_Test::_gTest & "/" & fmIDE_Test::_gTest[2]
```

## Usage

### Set Field




> ---
> 
> #### Test Case #1 "Set Field = == «calculation» (long form safe)"
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
> [+].Set Field
> [:]..field_name = "fmIDE_Test::_gTest"
> [:]..calculation = == 40 + $two
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Set Field = «calculation» (long form incorrect)"
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
> [+].Set Field
> [:]..field_name = "fmIDE_Test::_gTest"
> [:]..calculation = 40 + $two
> ```
> 
> 
> ##### Description
> 
> This test illustrates how omitting the "==" means fmJAML performs the evaluation, which can lead to unexpected results if variables or values are referenced, that have not yet been set by fmIDE
> 
> 
> 
> ---
> 
> #### Test Case #3 "Set Field = == «string» (short form)"
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
> [+].Set Field.fmIDE_Test::_gTest = == "No way"
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #4 "Set Field = «number» (short form for constants)"
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
> [+].Set Field.fmIDE_Test::_gTest = 42
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #5 "Set Field = empty (short form)"
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
> [+].Set Field.fmIDE_Test::_gTest = ""
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #6 "Set Field = «calculation» (short form with '=' - beware)"
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
> [+].Set Field.fmIDE_Test::_gTest.calculation = 1+2+3+4+5
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #7 "Set Field to calculation (short form with '=' - beware!)"
> 
> ##### Status
> 
> 🏧 automatic test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Set Variable.fmIDE_Test::_gTest.calculation = 1+2+3+4+5
> [+].Set Field.fmIDE_Test::_gTest.calculation = 1+2+3+4+5
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #8 "Set.Table::Field = === heredoc"
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
> [+].Set.fmIDE_Test::_gTest= ===
> "Success"
> ===
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #9 "Set.Table::Field.calculation = string"
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
> [+].Set.fmIDE_Test::_gTest.calculation="\"Success\""
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #10 "Set.Table::Field.calculation = «number»"
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
> [+].Set.fmIDE_Test::_gTest.calculation = 42
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #11 "Error: Set Field (missing field → 102)"
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
> [+].Set Field.fmIDE_Test::this field does not exist.calculation=123456
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #12 "Error: Set Field (missing table → 106)"
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
> [+].Set Field.this table does not exist::_gTest=123456
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #13 "Error: Set Field no target (missing field → 102)"
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
> [+].Set Field
> [:]..target=""
> [:]..calculation=123456
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #14 "Error: Set Field.Table::Field.calculation"
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
> [+].Set Field.fmIDE_Test::_gTest.calculation=1+2+3+4+5
> ```
> 
> 
> 
> 


## See also

- [Set](set.md)
