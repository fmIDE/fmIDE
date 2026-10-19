#!/usr/bin/env python3
"""Install the repository's AI Bridge macro library without overwriting foreign macros."""
import argparse
import hashlib
import json
from pathlib import Path
from fmide_run import dispatch, quote

REPO = Path(__file__).resolve().parents[1]


def definition_matches(existing, macro_name, script):
    """Compare the stored identity and script, accepting FileMaker's CR line ends."""
    return (
        'Exact ( JSONGetElement ( ' + existing + ' ; "macro_name" ) ; ' + quote(macro_name) + ' )'
        ' and Exact ( Substitute ( JSONGetElement ( ' + existing + ' ; "script" ) ; Char ( 13 ) ; Char ( 10 ) ) ; '
        + quote(script) + ' )'
    )


def make_installer(folder):
    manifest = json.loads((folder / 'manifest.json').read_text())
    actions = [{'Set Error Capture': '1'}]
    def stop_if(condition, message):
        actions.extend([{'If': condition}, {'Exit Script': 'JSONSetElement ( "{}" ; ["ok" ; 0 ; JSONBoolean] ; ["message" ; ' + quote(message) + ' ; JSONString] )'}, {'End If': None}])
    stop_if('IsEmpty ( $expected_file_path ) or not ( Exact ( Get ( FilePath ) ; $expected_file_path ) or Exact ( Right ( Get ( FilePath ) ; Length ( $expected_file_path ) ) ; $expected_file_path ) )', 'Wrong database')
    # Preflight the whole library before the first write.
    for macro in manifest['macros']:
        script = (folder / macro['file']).read_text()
        if hashlib.sha256(script.encode()).hexdigest() != macro['sha256']:
            raise ValueError('Source hash mismatch: ' + macro['file'])
        name = quote(macro['macro_name'])
        existing = 'GetPersistentData ( "fmide_macros" ; ' + name + ' )'
        stop_if('not IsEmpty ( FilterValues ( ListPersistentDataIDs ( "fmide_macros" ) ; ' + name + ' ) ) and not ( ' + definition_matches(existing, macro['macro_name'], script) + ' )', 'Existing macro differs or uses legacy keys: ' + macro['macro_name'] + '. Review it before replacement.')
    for macro in manifest['macros']:
        script = (folder / macro['file']).read_text()
        actions += [{'If': 'IsEmpty ( FilterValues ( ListPersistentDataIDs ( "fmide_macros" ) ; ' + quote(macro['macro_name']) + ' ) )'},
                    {'fmIDE Define Macro': {'macro_name': quote(macro['macro_name']),
                     'metadata': {'owner':'fmIDE-AI-Bridge','version':macro['version'],'source_sha256':macro['sha256'],'inputs':macro['inputs'],'effect':macro['effect']},
                     'script': quote(script)}}]
        stop_if('$$fmide_get_last_error ≠ 0', 'Define failed: ' + macro['macro_name'])
        actions += [{'End If': None}]
    for macro in manifest['macros']:
        script = (folder / macro['file']).read_text()
        existing = 'GetPersistentData ( "fmide_macros" ; ' + quote(macro['macro_name']) + ' )'
        stop_if('not ( ' + definition_matches(existing, macro['macro_name'], script) + ' )', 'Readback failed: ' + macro['macro_name'])
    actions += [{'Exit Script':'JSONSetElement ( "{}" ; ["ok" ; 1 ; JSONBoolean] ; ["verified_macros" ; ' + str(len(manifest['macros'])) + ' ; JSONNumber] ; ["file_path" ; Get ( FilePath ) ; JSONString] )'}]
    return json.dumps(actions, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fmp', required=True)
    parser.add_argument('--file', required=True)
    parser.add_argument('--database-path', required=True)
    parser.add_argument('--backup-file-path', required=True, help='New absolute FileMaker path for the required checkpoint copy')
    args = parser.parse_args()
    folder = REPO / 'macros/ai-bridge'
    # The verified Backup body works before any macros are installed.
    backup = dispatch((folder/'backup.fmIDEAS').read_text(),fmp=args.fmp,file_name=args.file,database_path=args.database_path,
                      values={'backup_file_path':args.backup_file_path})
    if backup['last_error'].strip() != '0' or backup['result'].get('ok') is not True:
        raise RuntimeError('Backup failed: ' + json.dumps(backup['result']))
    result = dispatch(make_installer(folder), fmp=args.fmp,file_name=args.file,database_path=args.database_path)
    print(json.dumps({'backup':backup['result'],'installation':result['result']},ensure_ascii=False,indent=2))
    return 0 if result['last_error'].strip() == '0' and result['result'].get('ok') is True else 1


if __name__ == '__main__':
    raise SystemExit(main())
