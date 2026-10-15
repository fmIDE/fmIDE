<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `script_step_range`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | ok |
| Category | 2 |
| Default action | [Select Script Steps](../actions/select-script-steps.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Select Script Steps
[:]..script_step_number=$script_step_number
[:]..script_step_number_to=$script_step_number_to
[:]..script_step_range=$script_step_range
```
