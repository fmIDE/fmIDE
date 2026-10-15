<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `layout_part_name`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | alpha |
| Category | 1 |
| Default action | [Go to Layout Part](../actions/go-to-layout-part.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Go To Layout Part
[:]..layout_id=$layout_id
[:]..layout_name=$layout_name
[:]..layout_number=$layout_number
[:]..layout_part_id=$layout_part_id
[:]..layout_part_name=$layout_part_name
[:]..layout_part_number=$layout_part_number
```
