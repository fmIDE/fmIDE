<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `layout_number`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | Number |
| Active | No |
| Development state | idea |
| Category | 2 |
| Default action | [Go To Layout](../actions/go-to-layout.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Go To Layout
[:]..layout_id=$layout_id
[:]..layout_name=$layout_name
[:]..layout_number=$layout_number
```
