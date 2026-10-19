# AI Bridge building blocks

The [macro sources](../macros/ai-bridge/manifest.json) package repeated jobs from this development session. Each receives named lower_snake_case variables through Run Macro frontmatter and returns a JSON object:

```json
{
  "ok": true,
  "macro": "AI Bridge.Context",
  "data": {},
  "error": {"kind":"", "code":0, "message":""},
  "context": {"file_name":"fmIDE", "file_path":"…", "fmide_release":"…"}
}
```

Check `ok`, not just the error number. Validation failures use `error.kind = "validation"` and code zero; they do not invent a FileMaker error code. Native failures retain their code and details. Data API failures use `error.kind = "data_api"`. Context always identifies the execution file.

| Macro | Inputs besides `expected_file_path` | Result / effect |
| --- | --- | --- |
| Context | None; identity input is optional | File, layout, table and versions |
| Design Names | None | Arrays of table, layout, script and value-list names |
| Read Records | `layout_name`, optional `limit`, `offset`, `query_json` | Local Data API response; limit 1–1000, default 100 |
| Write JSON | `output_file_path`, `result_json` | Writes one new UTF-8 file; refuses an existing file |
| Backup | `backup_file_path` | Saves a new `.fmp12` copy and checks its byte size |
| Inspect Script | `script_name`, optional `step_range` | Script text and selected lines/range; opens Script Workspace |
| Comment Steps | `comment_lines_json` | Escaped FileMaker comment-step XML; no clipboard mutation |
| Script Edit Plan | `script_name`, `step_range`, `replacement_xml` | Returns the intended patch as data; `executable` is false |

`expected_file_path` must match the full FileMaker path or an absolute POSIX suffix. Output paths use FileMaker's absolute path format. Query layout fields determine which data is exposed. `TableNames` lists table occurrences; it is not a base-table schema export. Script inspection requires macOS and MBS and changes editor focus/selection.

These are bounded building blocks, not an unrestricted mutation API. Script Edit Plan does not validate or execute the replacement XML. Suite 5 inspired the inspection and preparation blocks; its Press-based editing sketches remain unverified.

## Install

The library manifest uses `macro_name` for each entry's identity (schema version 2). The installer targets the [`macro_name` / `metadata` / `script` definition contract](fmjaml-fmideas.md#macro-definition-contract); use an fmIDE build implementing those keys. Macro execution results keep their existing `macro` and `error.code` fields.

With the local demo file open, from the repository root:

```sh
python3 tools/install_bridge_macros.py \
  --fmp 26 --file fmIDE \
  --database-path '/absolute/path/to/fmIDE.fmp12' \
  --backup-file-path 'file:/Volume/path/to/new-checkpoint.fmp12'
```

Use real paths for that machine. Installation first saves a checkpoint, preflights every macro name, defines missing entries, and verifies the stored `macro_name` and `script`. An identical entry is retained. A different definition or legacy `name`/`code` object stops the installer; review that macro before replacing it. Existing metadata is retained when the name and script match. The library lives in the file's `fmide_macros` store and requires FileMaker 26 plus the current macro fixes.

## Compose

```fmjaml
[+].fmIDE Run Macro
[:]..macro_name = == "AI Bridge.Design Names"
[:]..frontmatter = == "$expected_file_path = " & Quote ( Get ( FilePath ) ) & ";"
[+].Set.$report = == Get ( ScriptResult )
[+].If = == not JSONGetElement ( $report ; "ok" )
[+].  Exit Script = == $report
[+].End If

[+].fmIDE Run Macro
[:]..macro_name = == "AI Bridge.Write JSON"
[:]..frontmatter = ===
"$expected_file_path = " & Quote ( Get ( FilePath ) ) & ";" &
"$output_file_path = " & Quote ( Get ( DocumentsPath ) & "design-" & Get ( UUID ) & ".json" ) & ";" &
"$result_json = " & Quote ( $report ) & ";"
===
[+].Exit Script = == Get ( ScriptResult )
```

Capture the nested result immediately. Pass the actual data into the next block with `Quote`; do not interpolate unescaped text into frontmatter. File output is explicit so a read block can be reused without always touching disk.

For direct source execution, use `tools/fmide_run.py SOURCE --fmp 26 --file fmIDE --database-path PATH --vars-json INPUTS.json`. Input JSON keys omit `$`. The helper waits for completion in a unique local folder and retains an unresolved request after timeout. `--collect RESPONSE_FOLDER` reads a late result without dispatching again. This transport currently requires a repository under the execution user's Documents folder.

Inspect both the macro result and the helper's transport error. On a failed write, an incomplete new file may remain; its path is retained for inspection. No macro overwrites an existing output or silently retries a mutation.
