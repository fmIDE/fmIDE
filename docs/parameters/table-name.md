<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `table_name`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | beta |
| Category | 1 |
| Default action | [Go to Table](../actions/go-to-table.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Go To Table
[:]..table_name=$table_name
[:]..field_name=$field_name
[:]..field_id=$field_id
```
