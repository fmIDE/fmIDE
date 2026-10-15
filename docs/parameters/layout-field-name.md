<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `layout_field_name`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | ok |
| Category | 1 |
| Default action | [Go to Layout Field](../actions/go-to-layout-field.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Go To Layout Field
[:]..layout_id=$layout_id
[:]..layout_name=$layout_name
[:]..layout_number=$layout_number
[:]..layout_field_id=$layout_field_id
[:]..layout_field_name=$layout_field_name
[:]..layout_field_number=$layout_field_number
```
