> Migrated from the existing fmIDE wiki. This page preserves background and historical examples; version-sensitive integration details have not all been re-tested. Use the current [action reference](../actions/README.md), [parameter reference](../parameters/README.md) and [setup guide](../installation.md) for active work.

In FileMaker `Base Tables` and `Table Occurrences` (`TOs`) are relatively straightforward concepts.

However, since FileMaker 7 it's always been a bit of problem to know what the term `table` refers to.

# TL;DR

On the meaning of `table` there are traditionally two opposing (and mostly exclusive) camps of thought. fmIDE, however, provides a third and clear semantic:

1. Some say `table` refers to a `base table` (and `t_o` clearly means `table occurrence`)
2. Others say `table` refers to a `table occurrence` ( and `base table` clearly means `base table`)
3. fmIDE says a `table` refers to a `LayoutTableName` - which is technically a `table occurrence` - but, as such, defines the (corresponding) `base table` where the fields of the layout come from (whilst a `t_o` clearly is a `t_o`, and a `base_table` a `base_table`!)

This table summarises the use of the terms `base_table`, `t_o` and `table` in fmIDE.

|   Thing      |   Refers to a     | Default action in fmIDE | Which goes to     | Explanation
|--------------|-------------------|-------------------------|-------------------|------------------------------------------
| `base_table` | Base Table        | Go to Base Table        | the Base Table    | Base tables are listed in the tables panel in the database management dialog
| `t_o`        | Table Occurrence  | Go to Table Occurrence  | the Table Occurrence | Table Occurrences exist in the relationship graph in the database management dialog
| `table`      | Layout table name | Go to Table             | the corresponding Base Table | While layout table names are actually table occurrence names, they define the layout context and where fields come from, and thus take you to the corresponding base_table. 

# Base Table

`Base Tables` are the core tables containing fields.

- `base_table_name` refers to the name of a base table in the database definition
- specifying a `base_table_name` will perform a [`Go to Base Table ( base_table_name )`](../actions/go-to-base-table.md) action

# Table Occurence

`Table Occurrences` are the occurrences of tables found in the relationship graph.

- `t_o_name` refers to the name of a table occurrence in the database relationship graph
- specifying a `t_o_name` will perform a [`Go to Table Occurrence ( t_o_name )`](../actions/go-to-table-occurrence.md) action

# Table

'Tables' are trickier, because they are a bit of a mix of the other two, however, fmIDE clearly dictates how the term is used and what it means in which situation:

- `table_name` refers to the name of a table occurrence
  - **however** it refers to the *context of the layout*, rather than the position in the relationship graph
  - and it is thus about *where fields come from*, from which base table.
  - It is what is returned by the `Get ( LayoutTableName )` function.
- specifying a `table_name` will perform a [`Go to Table ( table_name )`](../actions/go-to-table.md) action

# Fields and Layout Fields

Note: This semantic is still in consideration, and could possibly change.

fmIDE considers a field to be a field in a base table, thus specifying `field_name` = `StartTime` (along with a `table_name`) will take you to the `StartTime` field in the schema.

`layout_field_name`, on the other hand, is how you refer to fields in layouts.

# fmIDE Actions `Go to Base Table`, `Go to Table` and `Go to Table Occurrence`

- `Go to Table Occurrence` goes to the table occurrence `t_o_name` in the relationship graph.
  - A `table_name` parameter, if passed, is treated as a `t_o_name`

- `Go to Base Table` and `Go to Table` are indeed the same action
  - They go to base table `base_table_name` in the database definition.
  - If a `table_name` is passed the equivalent base table is targeted.

For many (the majority of?) FileMaker developers the base_table_name and PTO (primary table occurrence) table_name are identical anyhow.

# `Base Layouts`  (for targeting `Base Tables`)

In the current version of fmIDE, we don't have the technology to change to the correct view & table *once we are inside the `Define Database` dialog*. Thus **the base table is targeted by going to the corresponding layout ***before*** we open the database definition**. Like this, the database definition opens in the correct table context, and the user must only change to the correct desired (table o r field) view.

For clarity, we shall refer to such 'internal' layouts, or PTO layouts as the **`Base Layout`**

This method is slick, but requires developers

- to make sure they have a `Base Layout` for each `Base Table`
- to implement an fmIDE callback script `fmIDE.GetLayoutNameForTable` 
 
Since each developer/database uses different naming conventions for base tables, TOs and layouts,
the job of identifying the layout name for a particular table is defined in the callback script `fmIDE.GetLayoutNameForTable` in each file of the database.

# fmIDE Callback Script `fmIDE.GetBaseLayoutName` 
  
A function script that takes `base_table_name` and/or `table_name` and returns `base_layout_name`.

Implementation details in this historical section were not completed. Consult the current native callback scripts.
