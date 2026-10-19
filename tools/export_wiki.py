#!/usr/bin/env python3
"""Export live fmIDE Wiki docs, validate them, then publish docs/actions."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

REPO = Path(__file__).resolve().parents[1]
GENERATOR = 'fmIDE Wiki docs exporter v1'


def fm_quote(value):
    return '"' + str(value).replace('\\', '\\\\').replace('"', '\\"') + '"'


def validate(folder, expected_count):
    manifest = json.loads((folder / '_manifest.json').read_text(encoding='utf-8'))
    if manifest.get('generator') != GENERATOR or manifest.get('actionCount') != expected_count:
        raise ValueError('Unexpected documentation manifest.')
    pages = manifest['pages']
    names = [p['file'] for p in pages]
    ids = [p['id'] for p in pages]
    if len(names) != expected_count or len(set(names)) != len(names) or len(set(ids)) != len(ids):
        raise ValueError('Missing or duplicate action pages.')
    if any(not re.fullmatch(r'[a-z0-9-]+\.md', name) for name in names):
        raise ValueError('Unsafe action-page filename.')
    expected = set(names) | {'README.md', '_manifest.json'}
    if {p.name for p in folder.iterdir()} != expected:
        raise ValueError('Unexpected or missing generated files.')
    for name in sorted(expected):
        path = folder / name
        if path.is_symlink() or not path.is_file():
            raise ValueError('Generated files must be regular files: ' + name)
        text = path.read_text(encoding='utf-8')
        if any(ord(c) < 32 and c not in '\n\t' for c in text):
            raise ValueError('Control character in ' + name)
        if name.endswith('.md'):
            if not text.startswith('<!-- Generated from fmIDE_Action.'):
                raise ValueError('Missing generated-file marker: ' + name)
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if ':' not in link and not link.startswith('#') and link not in expected:
                    raise ValueError('Broken local link in ' + name + ': ' + link)
    rows = [line for line in (folder / 'README.md').read_text(encoding='utf-8').splitlines()
            if line.startswith('|')]
    if len(rows) != expected_count + 2 or any(line.count('|') != 7 for line in rows):
        raise ValueError('The index must have six columns and one row per action.')
    return manifest


def export(fmp, timeout):
    docs = REPO / 'docs'
    docs.mkdir(exist_ok=True)
    if shutil.disk_usage(REPO).free < 10 * 1024**3:
        raise RuntimeError('Less than 10 GiB free; documentation export was not started.')
    with tempfile.TemporaryDirectory(prefix='.wiki-response-', dir=docs) as scratch:
        response = Path(scratch)
        relative = response.relative_to(REPO).as_posix() + '/'
        frontmatter = (
            '$fmide_on_exit_script_write_data_to_folder_path = Let ( p = Get ( FilePath ) ; '
            'Left ( p ; Position ( p ; "/" ; Length ( p ) ; -1 ) ) & ' + fm_quote(relative) + ' ); '
            '$docs_expected_database_suffix = ' + fm_quote((REPO / 'fmIDE.fmp12').as_posix())
        )
        subprocess.run(['fmide', '-fmp', fmp, '-file', 'fmIDE', '-frontmatter', frontmatter,
                        '--parameter-file', str(REPO / 'tools/export-wiki.fmIDEAS')], check=True)
        expected = ['script_result.txt', 'last_error.txt', 'last_error_detail.txt',
                    'last_error_location.txt', 'last_error_description.txt']
        deadline = time.monotonic() + timeout
        while not all((response / name).is_file() for name in expected):
            if time.monotonic() >= deadline:
                raise RuntimeError('No verified completion from this checkout. Previous docs preserved.')
            time.sleep(0.25)
        result = json.loads((response / 'script_result.txt').read_text(encoding='utf-8'))
        if ((response / 'last_error.txt').read_text().strip() != '0'
                or result.get('status') != 'exported' or result.get('error') != 0):
            raise RuntimeError('fmIDE export stopped: ' + json.dumps(result, ensure_ascii=False))
    if not result['database'].endswith((REPO / 'fmIDE.fmp12').as_posix()):
        raise RuntimeError('The response is from a different database; previous docs preserved.')
    stage_id = result['folder'].rstrip('/').rsplit('/', 1)[-1]
    if not re.fullmatch(r'[0-9A-Fa-f-]{36}', stage_id):
        raise ValueError('Unexpected staging-folder name.')
    stage = docs / '.wiki-export' / stage_id
    if stage.is_symlink() or not result['folder'].rstrip('/').endswith(stage.as_posix()):
        raise ValueError('Unexpected staging-folder path.')
    count = result['actionCount']
    if not isinstance(count, int) or count < 1 or result['filesWritten'] != count + 2:
        raise ValueError('Incomplete export.')
    manifest = validate(stage, count)
    target = docs / 'actions'
    previous = None
    if target.exists() or target.is_symlink():
        if target.is_symlink():
            raise ValueError('Refusing to replace a linked documentation folder.')
        old = json.loads((target / '_manifest.json').read_text(encoding='utf-8'))
        if old.get('generator') != GENERATOR:
            raise ValueError('Refusing to replace documentation not owned by this exporter.')
        previous = docs / '.wiki-export' / ('previous-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
        target.rename(previous)
    try:
        stage.rename(target)
    except BaseException:
        if previous is not None:
            previous.rename(target)
        raise
    print(f'Published {count} action pages and a six-column index to {target}')
    print('Source: ' + manifest['fmIDERelease'] + '; ' + manifest['fileMakerVersion'])
    if previous is not None:
        print('Previous generated docs retained at ' + str(previous))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fmp', required=True, help='Explicit FileMaker version/protocol, e.g. 26')
    parser.add_argument('--timeout', type=float, default=180, help='Completion timeout in seconds')
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error('--timeout must be positive')
    try:
        export(args.fmp, args.timeout)
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.CalledProcessError) as error:
        print('ERROR: ' + str(error))
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
