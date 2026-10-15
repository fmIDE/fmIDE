<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `script_step_name`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | beta |
| Category | 1 |
| Default action | [Find Script Step](../actions/find-script-step.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].FindScriptStep
[:]..script_step_search=$script_step_name
```
