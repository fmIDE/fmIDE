<!-- Generated from fmIDE_Action. Edit the database, then export again. -->
# Action `Go To Base Field`

Open Manage Database for a field in the current file and prepare its name in the fmAutoMate keyboard buffer; final selection is manual.

[All actions](README.md)


| FileMaker Script Step | Support | DevState | Originated in fmIDE version |
|-----------------------|:-------:|:--------:|:--------------------:|
| None | Yes | beta |  |

## Description

Goes to the given base field, if possible(*).

The table may be given

- together in the `base_field_name` parameter: «base_table_name::base_field_name»
- separately in the `base_table_name` parameter

1. Stores the base field name in the fmAutoMate Keyboard Buffer file.
2. Calculates the equivalent Base Layout name.
3. Goes to the Base Layout
4. Opens the `Manage Database` dialog

fmIDE can only get you as far as the `Manage Database` dialog. From there you must manually:

- switch to the Tables view
- click in the list
- press the fmAutoMate keyboard shortcut to retype the name

(*) Note: It is only possible to go to base fields in tables from the current file.

## Full Syntax

```
[+].Go To Base Field
[:]..base_table_name = "fmIDE_Test"
[:]..table_name = "fmIDE_Test"
[:]..field_name = "__UUID" // field name can be separate
[:]..field_name = "fmIDE_Test::__UUID" // fully qualified
[:]..field_name = "130::2" // field name can even contain ids
[:]..field_number = -1

```

## Usage

### Go To Base Field




> ---
> 
> #### Test Case #1 "Go To Base Field (short form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Field = == fmIDE_Test::_gTest
> 
> ```
> 
> 
> 
> 

### Go To Base Field by number


Goes to the field based on creation order


> ---
> 
> #### Test Case #1 "Go To Base Field newest field using field_number = -1 and table_name (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Field
> [:]..table_name = "fmIDE_Test"
> [:]..field_number = -1
> 
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go To Base Field newest field using field_number = -1 and base_table_name (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Field
> [:]..base_table_name = "fmIDE_Test"
> [:]..field_number = -1
> 
> ```
> 
> 
> 
> 

### Go To Base Field "(base_)table_id::field_id"


Here a field is referenced via field_name, but ids are used (Filemaker's handle on a field) rather than name (Users' handle on a field)


> ---
> 
> #### Test Case #1 "Go To Base Field "«table_id»::«field_id»" (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Field.field_name = "1065089::1"
> 
> ```
> 
> 
> 
> 
> ---
> 
> #### Test Case #2 "Go To Base Field "«base_table_id»::«field_id»" (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Field
> [:]..field_name = "130::2"
> 
> ```
> 
> 
> 
> 

### Go To Base Field of current layout


When no table is specified the current layout table is assumed.


> ---
> 
> #### Test Case #1 "Go To Base Field field_id = 1 from current table (long form)"
> 
> ##### Status
> 
> ✅ Pass 
> ✋ manual test 
> 
> 
> ##### Code under Test
> 
> ```
> [+].Go to Base Field
> [:]..field_id = 1
> 
> ```
> 
> 
> ##### Description
> 
> This jumps to the first created field of the current layout's table.
> 
> 
> 


## See also

- [Go to Base Table](go-to-base-table.md)
- [Go to Layout Field](go-to-layout-field.md)
- [Go to Field](go-to-field.md)
