# Current FileMaker source

`xml/fmIDE.xml` is the latest detailed **Save a Copy as XML** export of the repository's `fmIDE.fmp12`. Keep one current export here; no separate archive is maintained. Git history can retain earlier committed versions.

`exploded/` is generated from that export with [Malte Bastian's fm-xml-export-exploder](https://github.com/bc-m/fm-xml-export-exploder), including XML objects and readable `scripts_sanitized` text. The full SaXML remains the authoritative snapshot; generated files are for inspection and comparison, not an importable replacement for the database.

## Refresh the export

Run from the repository root on the Mac running the intended FileMaker 26 client. Open this checkout's `fmIDE.fmp12` with full access first. Confirm the executing file path rather than assuming that the frontmost client/database is the target.

```sh
mkdir -p src/xml
python3 tools/source_xml.py export --fmp 26
```

The action exports the executing file's window with details enabled and embedded binary data. Its destination is calculated from the executing file path, so it follows the checkout rather than a machine-specific Documents path.

The export action checks the expected database path before writing. The wrapper uses the shared `fmide_run.py` transport, waits for its unique result/error files, verifies that this checkout responded, parses the XML, and writes `src/xml/manifest.json`. Requests remain in `.fmide-work/`, including after a timeout; inspect and collect the original response before another dispatch. This local transport expects the checkout under the execution user’s Documents folder. Then rebuild:

```sh
python3 tools/explode_xml.py
```

The wrapper retains fmIDE’s five result/error files automatically. Prefer it to running the export action directly: the action requires `expected_file_path`, and only the wrapper updates the freshness manifest.

## Exploder dependency

The initial snapshot was generated with **v0.7.1**, `--lossless --output_tree db`. Lossless mode retains information omitted by the usual noise filter. `scripts_sanitized` is a convenient text view; consult XML for authoritative detail.

On macOS, install the pinned official universal release into the ignored local tools folder:

```sh
mkdir -p .tools
gh release download v0.7.1 --repo bc-m/fm-xml-export-exploder \
  --pattern fm-xml-export-exploder-universal-apple-darwin.tar.gz --dir .tools
shasum -a 256 .tools/fm-xml-export-exploder-universal-apple-darwin.tar.gz
# Expected: 2b73450aedab03d61ebd4c16034ecac615b231f1afa0158e5ca41a51a93b20e7
tar -xzf .tools/fm-xml-export-exploder-universal-apple-darwin.tar.gz -C .tools
python3 tools/explode_xml.py
```

Alternatively, set `FM_XML_EXPLODER_BIN` to an installed executable. The wrapper also checks PATH. The executable is a local dependency and is not committed.

The wrapper validates input and generated XML, builds in a temporary folder, and replaces only the generated `src/exploded` tree after success. This removes stale generated files from renamed/deleted objects. The `.fmide-generated` marker prevents replacing an unrelated directory. The manifest records the tool version, options, and source checksum.

The first export was captured on 13 October 2026 from FileMaker Pro 26.0.3, fmIDE release `20261011 @mrwatson-de v0.93`, with fmIDE last error 0. The XML describes database design, not a dump of test-record data.

## Initial size and Git tracking recommendation

Measured on 13 October 2026:

| Artifact | Size | Files |
| --- | ---: | ---: |
| Full SaXML | 24,366,235 bytes (23.24 MiB) | 1 |
| Full exploded tree, including manifest/marker | 24,091,085 bytes (22.98 MiB) | 1,831 |
| fmIDE Module script XML | 4,607,380 bytes (4.39 MiB) | 7 |
| fmIDE Module readable script text | 487,310 bytes (0.46 MiB) | 7 |
| All readable script text, including demo/test scripts | 717,513 bytes (0.68 MiB) | 373 |
| All custom-function XML | 180,850 bytes (0.17 MiB) | 74 |

Recommendation: keep the full export locally for complete inspection, but track a focused generated source view in Git: the fmIDE Module scripts (XML plus readable text), required custom functions, and optionally readable test/demo scripts. Tracking both the full export and all exploded catalogs duplicates about 46 MiB of source and adds changes from unrelated layouts, themes, and generated export metadata. The compact script view gives much more useful code review.

The full snapshot and exploded tree remain available locally. Root `.gitignore` rules exclude the raw XML and unrelated generated catalogs, while allowing module script XML, all readable scripts (including tests/demo), custom functions, and manifests/markers. A checkout contains this selected source view, not a complete Save as XML export; create a local export before rebuilding on a new checkout.

## Freshness check

```sh
python3 tools/source_xml.py check
```

The export manifest records UTC export completion time, the source database's completion-time modification timestamp (nanoseconds) and size, the XML checksum, database UUID, FileMaker version, and fmIDE release. Relative paths keep the manifest independent of the checkout location. The XML remains at its fixed `src/xml/fmIDE.xml` location.

The check exits 0 when recorded metadata/checksum match, 1 when the XML is potentially stale, and 2 when the check cannot be completed. It does not export or change the database. FileMaker can cache changes before writing to disk, and data changes also update the file; this is a conservative disk-metadata check, not a design-change detector. Copying the checkout can also change modification times. `changedDuringExport` records whether the source metadata differed across the export; this is not an atomic database snapshot guarantee.

Use the wrapper rather than dispatching `tools/export-source.fmIDEAS` directly when you need the freshness manifest refreshed. The exploded-tree manifest separately records which XML checksum it was built from; rebuild after a new export.

Run the focused freshness checks with `python3 -B tests/test_source_xml.py`.
