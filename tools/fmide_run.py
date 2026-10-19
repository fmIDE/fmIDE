#!/usr/bin/env python3
"""Dispatch once to a local FileMaker file; retain and verify completion evidence."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import subprocess
import time
import uuid

REPO = Path(__file__).resolve().parents[1]
NAMES = ('script_result', 'last_error', 'last_error_detail', 'last_error_location', 'last_error_description')


def quote(value):
    # Paragraph symbols and curly double quotes have syntax meaning in FileMaker.
    # Emit them as characters so arbitrary documentation stays literal.
    parts = re.split(r'([\r\n¶“”])', str(value))
    return ' & '.join('Char ( ' + str(ord(part)) + ' )' if part in ('\r', '\n', '¶', '“', '”')
                      else '"' + part.replace('\\', '\\\\').replace('"', '\\"') + '"'
                      for part in parts)


def variable_definitions(values):
    definitions = []
    for key, value in values.items():
        if not re.fullmatch(r'[a-z][a-z0-9_]*', key) or key.startswith(('fmide_', 'bridge_')):
            raise ValueError('Invalid or reserved input name: ' + key)
        if isinstance(value, bool):
            calculation = '1' if value else '0'
        elif isinstance(value, (int, float)):
            # GetAsNumber is locale-sensitive; JSONGetElement parses a JSON number consistently.
            calculation = 'JSONGetElement ( ' + quote(json.dumps([value], allow_nan=False)) + ' ; 0 )'
        elif value is None:
            calculation = '""'
        elif isinstance(value, (dict, list)):
            calculation = quote(json.dumps(value, ensure_ascii=False))
        else:
            calculation = quote(value)
        definitions.append('$' + key + ' = ' + calculation + ';')
    return ' '.join(definitions)


def collect(response):
    request = json.loads((response / 'request.json').read_text())
    missing = [name for name in NAMES if not (response / (name + '.txt')).is_file()]
    if missing:
        raise TimeoutError('Still pending: ' + str(response))
    # Decode bytes directly: text-mode universal newline conversion would change a
    # legitimate CR inside a plain-text FileMaker result into LF.
    output = {name: (response / (name + '.txt')).read_bytes().decode('utf-8').removesuffix('\n') for name in NAMES}
    try:
        output['result'] = json.loads(output['script_result'])
    except ValueError:
        output['result'] = output['script_result']
    output['request'] = request
    output['response_folder'] = str(response)
    (response / 'completion.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    pending = response.parent / 'pending.json'
    if pending.exists() and json.loads(pending.read_text()).get('request_id') == request['request_id']:
        pending.unlink()
    return output


def dispatch(source, *, fmp, file_name, database_path, values=None, timeout=180, cli='fmide', work_root=None):
    if timeout <= 0:
        raise ValueError('Timeout must be positive.')
    work = Path(work_root or REPO / '.fmide-work').resolve()
    if shutil.disk_usage(work if work.exists() else work.parent).free < 10 * 1024**3:
        raise RuntimeError('Less than 10 GiB free; dispatch not started.')
    work.mkdir(parents=True, exist_ok=True)
    pending = work / 'pending.json'
    if pending.exists():
        raise RuntimeError('A prior dispatch is unresolved. Inspect ' + str(pending) + ' and collect its late response first.')
    request_id = str(uuid.uuid4())
    response = work / request_id
    response.mkdir()
    # This local transport deliberately requires the user's Documents tree.
    relative = response.relative_to(Path.home() / 'Documents').as_posix() + '/'
    values = dict(values or {})
    if 'expected_file_path' in values and values['expected_file_path'] != database_path:
        raise ValueError('Conflicting expected_file_path.')
    values['expected_file_path'] = database_path
    frontmatter = variable_definitions(values)
    frontmatter += ' $fmide_on_exit_script_write_data_to_folder_path = Get ( DocumentsPath ) & ' + quote(relative) + ';'
    source_path = response / 'request.fmIDEAS'
    source_path.write_text(source, encoding='utf-8')
    request = {'request_id': request_id, 'started_at': datetime.now(timezone.utc).isoformat(),
               'fmp': str(fmp), 'file_name': file_name, 'database_path': database_path,
               'response_folder': str(response)}
    (response / 'request.json').write_text(json.dumps(request, indent=2) + '\n')
    # Exclusive creation prevents two helpers from dispatching concurrently.
    with pending.open('x') as stream:
        json.dump(request, stream, indent=2)
    try:
        subprocess.run([cli, '-fmp', str(fmp), '-file', file_name, '--frontmatter', frontmatter,
                        '--parameter-file', str(source_path)], check=True)
    except BaseException:
        # The URL may already have launched even if the process reports an error.
        raise RuntimeError('Dispatch outcome unknown; retained pending request at ' + str(response))
    deadline = time.monotonic() + timeout
    while not all((response / (name + '.txt')).is_file() for name in NAMES):
        if time.monotonic() >= deadline:
            raise TimeoutError('No verified completion yet. Do not redispatch. Inspect ' + str(response))
        time.sleep(0.25)
    return collect(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', type=Path)
    parser.add_argument('--fmp')
    parser.add_argument('--file')
    parser.add_argument('--database-path')
    parser.add_argument('--vars-json', type=Path, help='JSON object of lower_snake_case macro inputs')
    parser.add_argument('--timeout', type=float, default=180)
    parser.add_argument('--collect', type=Path, help='Collect an existing response; never dispatch again')
    args = parser.parse_args()
    try:
        if args.collect:
            result = collect(args.collect.resolve())
        else:
            if not all((args.source, args.fmp, args.file, args.database_path)):
                parser.error('source, --fmp, --file and --database-path are required')
            values = json.loads(args.vars_json.read_text()) if args.vars_json else {}
            result = dispatch(args.source.read_text(), fmp=args.fmp, file_name=args.file,
                              database_path=args.database_path, values=values, timeout=args.timeout)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result['last_error'].strip() == '0' and not (isinstance(result['result'], dict) and result['result'].get('ok') is False) else 1
    except (OSError, ValueError, RuntimeError, TimeoutError) as error:
        print('ERROR: ' + str(error))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
