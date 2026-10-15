<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `script_name`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | ok |
| Category | 1 |
| Default action | [Go to Script](../actions/go-to-script.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Go To Script
[:]..script_id=$script_id
[:]..script_name=$script_name
[:]..script_name_stub=$script_name_stub
[:]..script_number=$script_number
[:]..script_step_number=$script_step_number
[:]..script_step_number_to=$script_step_number_to
[:]..script_step_range=$script_step_range
[:]..script_step_search=$script_step_search
[:]..script_step_search_value=$script_step_search_value
```
