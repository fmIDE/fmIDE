<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `t_o_name`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | beta |
| Category | 1 |
| Default action | [Go to Table Occurrence](../actions/go-to-table-occurrence.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Go To Table Occurrence
[:]..t_o_name=$t_o_name
```
