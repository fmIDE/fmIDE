# Prepare an fmIDE release candidate

`tools/release_fmide.py` stages a copy, runs the demo file's existing **Prepare Release** script in that copy, saves a compacted `fmIDE.fmp12`, and packages it with a checksum manifest. It does not edit the version, commit, tag, push or publish a GitHub release.

The working source remains open and unchanged by preparation. The staged file has a unique name so an FMP dispatch can target it unambiguously. The native preparation clears demo globals and arranges views; it preserves Actions, parameter and Test records. The wrapper checks those record counts and selected reset fields before saving the candidate.

## 1. Stage

From the repository root, with the intended source file open:

```sh
python3 tools/release_fmide.py stage \
  --fmp 26 --file fmIDE \
  --database-path '/absolute/path/to/fmIDE.fmp12' \
  --version v0.95 \
  --expected-release '20261014 @mrwatson-de v0.95' \
  --output-dir '/Users/you/Documents/fmIDE-release-v0.95'
```

Use the actual version, release string and paths. The output directory must be new and under the local execution user's Documents folder. The helper verifies the source's returned path and release, uses Save a Copy as, and records the staged copy's size and SHA-256.

Set the native release/version first using the project's normal development process. A different release string stops this tool; it does not silently relabel the implementation.

## 2. Prepare the copy

Open the uniquely named `fmIDE-release-work-….fmp12` printed by the stage command in the same FileMaker version. This explicit opening step avoids guessing the source of a same-named database.

```sh
python3 tools/release_fmide.py prepare \
  --state '/Users/you/Documents/fmIDE-release-v0.95/release-state.json'
```

The fmIDEAS in `tools/prepare-release.fmJAML` refuses the ordinary development file, checks the release string, refuses an existing output, runs preparation, verifies postconditions and saves the compacted copy. A failure leaves its staging evidence in place. An existing record edit also stops preparation.

## 3. Package and review

```sh
python3 tools/release_fmide.py package \
  --state '/Users/you/Documents/fmIDE-release-v0.95/release-state.json'
```

The ZIP contains `fmIDE.fmp12` and `manifest.json`. The helper checks the candidate's hash before packaging and checks the archived bytes afterward. Open and smoke-test the candidate separately before publishing it; preparation does not rerun the whole test suite or change account/security configuration.

Review release notes, local changes and intended distribution contents before using the repository's normal publishing process. Keep the source and staged backup until the candidate is accepted.

## Example-reset verification

The local v0.95 implementation fixes [issue #206](https://github.com/fmIDE/fmIDE/issues/206): the reset helper selects defaults by its advancing loop index, stores literal text in a variable, then writes the requested repetition with Set Field. It no longer depends on an active example field.

Six focused native cases passed in an isolated copy and the main demo: reset all, reset only example 1 and reset only example 2, from both the Examples and Actions layouts. Each case checked both repetitions exactly; original globals were restored afterward. A fresh v0.95 candidate preparation was also checked: both example globals matched their original native defaults exactly. The release wrapper checks selected reset fields and record counts, so review the intended candidate contents before publication.

## Timeout recovery

A timeout leaves the request under `.fmide-work/` and the release state marked `preparing`. Inspect the application and late response before another dispatch. If the original preparation completed successfully:

```sh
python3 tools/release_fmide.py recover \
  --state '/Users/you/Documents/fmIDE-release-v0.95/release-state.json' \
  --response '/absolute/path/to/repository/.fmide-work/REQUEST-ID'
```

Recovery reads the existing response and verifies its target and output; it does not run preparation again. For a genuine failed preparation, retain the evidence and stage a fresh copy after fixing the cause.
