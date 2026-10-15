<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->
# Parameter `curl_options`

[All parameters](README.md) · [Name that Thing](../name-that-thing.md)

No description is recorded in the source table yet.

| Property | Value |
| --- | --- |
| Type | String |
| Active | Yes |
| Development state | beta |
| Category | 7 |
| Default action | [Insert from URL](../actions/insert-from-url.md) |
| Default value | Not recorded |

## Stored action mapping

This is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.

```fmjaml
[+].Insert from URL
[:]..curl_options=$curl_options
[:]..url=$url
[:]..with_dialog=$with_dialog
```
