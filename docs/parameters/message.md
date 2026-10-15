<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `message`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

Static message

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | beta |
| Category | 7 |
| Default action | [Show Custom Dialog](../actions/show-custom-dialog.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Show Custom Dialog
[:]..message=$message
[:]..buttons_list=$buttons_list
```
