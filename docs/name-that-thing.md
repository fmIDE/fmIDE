# Name that Thing

Tell fmIDE which development object you want, using lower_snake_case parameters. It expands those names into actions and runs them in the relevant order.

```json
{"script_name":"Hello World","script_step_number":3}
```

Pass that object to the `fmIDE` script, or use its variable-definition form:

```filemaker
$script_name = "Hello World"; $script_step_number = 3
```

With the CLI, explicitly select the application and open database:

```sh
fmide -fmp 26 -file fmIDE \
  -$ 'script_name=Hello World' \
  -$ 'script_step_number=3'
```

See the [generated parameter reference](parameters/README.md) for active, proposed and historical parameters, and the [action reference](actions/README.md) for the underlying operation. Both come from the demo file's documentation tables.

## FMP URLs

To run `Hello World` in the open demo file:

```text
fmp26://$/fmIDE?script=Hello%20World
```

To navigate to its third script step:

```text
fmp26://$/fmIDE?script=fmIDE&$script_name=Hello%20World&$script_step_number=3
```

Encode each value, for example with `GetAsURLEncoded`; do not concatenate unescaped names containing spaces, ampersands or percent signs. `$` denotes an already-open file. An explicit server address targets a hosted file. Choose the FileMaker protocol intentionally when several versions are installed.

In a native script, prefer Perform Script by name when avoiding a hard reference to a replaceable fmIDE script matters. Check the returned result or application state after dispatch.

## Tables, fields and layouts

`base_table_name` names the underlying table; `t_o_name` names a relationship-graph occurrence. `table_name` uses layout context to identify the corresponding base table. fmIDE can select a base layout before opening Manage Database, so the dialog starts in that table's context.

Inspect and adapt the callback scripts when your base tables, primary occurrences and base layouts have different names. Do not assume they match. The [original detailed explanation](wiki/tables-and-layouts.md) preserves the rationale and historical naming discussion.

## Integrating a tool

An analysis tool can read the object represented by its current record, map it to these parameters, then construct an FMP URL. It should retain the intended file/server/protocol rather than guessing them from focus.

The [Go to Thing integration guide](wiki/go-to-thing.md), [integration list](wiki/integrations.md) and [Thingamajig URI guide](wiki/thingamajig-uris.md) retain the existing wiki material. Thingamajig URIs are compact references expanded by the URIcorn using configured environment defaults.
