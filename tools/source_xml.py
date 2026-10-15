#!/usr/bin/env python3
"""Export the current local fmIDE checkout or check its XML freshness."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
DATABASE = REPO / 'fmIDE.fmp12'
XML = REPO / 'src/xml/fmIDE.xml'
MANIFEST = XML.with_name('manifest.json')


def stamp(path):
    stat = path.stat()
    return {'modifiedNs': stat.st_mtime_ns, 'bytes': stat.st_size}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check():
    if not MANIFEST.is_file():
        print('UNKNOWN: no export manifest. Run the export command first.')
        return 2
    data = json.loads(MANIFEST.read_text())
    if not DATABASE.is_file() or not XML.is_file():
        print('UNKNOWN: the source database or exported XML is missing.')
        return 2
    reasons = []
    if stamp(DATABASE) != data['source']['stat']:
        reasons.append('database modification time or size changed')
    if digest(XML) != data['xml']['sha256']:
        reasons.append('XML checksum changed')
    if reasons:
        print('POTENTIALLY STALE: ' + '; '.join(reasons) + '.')
        return 1
    print('CURRENT by recorded file metadata; exported at ' + data['exportedAt'] + '.')
    print('This checks disk writes, not unflushed FileMaker edits or design changes alone.')
    return 0


def export(fmp, timeout):
    XML.parent.mkdir(parents=True, exist_ok=True)
    before = stamp(DATABASE)
    # Share the retained, single-dispatch response transport used by the bridge.
    from fmide_run import dispatch
    completion = dispatch((REPO / 'tools/export-source.fmJAML').read_text(),
                          fmp=fmp, file_name='fmIDE', database_path=str(DATABASE),
                          timeout=timeout, work_root=REPO / '.fmide-work')
    result = completion['result']
    if completion['last_error'].strip() != '0' or not isinstance(result, dict) or result.get('ok') is not True:
        raise RuntimeError('fmIDE export failed: ' + json.dumps(result, ensure_ascii=False))
    if not result.get('file_path', '').endswith(DATABASE.as_posix()):
        raise RuntimeError('The responding database is not this local checkout.')
    root = ET.parse(XML).getroot()
    if root.tag != 'FMSaveAsXML' or root.attrib.get('File') != DATABASE.name:
        raise RuntimeError('The export is not the expected FileMaker XML document.')
    after = stamp(DATABASE)
    data = {
        'schemaVersion': 1,
        'exportedAt': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'source': {'path': 'fmIDE.fmp12', 'stat': after,
                   'changedDuringExport': before != after},
        'xml': {'path': 'src/xml/fmIDE.xml', 'sha256': digest(XML),
                'bytes': XML.stat().st_size, 'databaseUUID': root.attrib.get('UUID')},
        'applicationVersion': result['application_version'], 'fmideRelease': result['fmide_release'], 'fmideError': 0,
    }
    temporary = MANIFEST.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(MANIFEST)
    print('Exported and validated ' + str(XML))
    if data['source']['changedDuringExport']:
        print('Note: database disk metadata changed during export; the manifest records its completion-time metadata.')
    return check()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['export', 'check'])
    parser.add_argument('--fmp', default='26', help='FileMaker version/protocol for export (default: 26)')
    parser.add_argument('--timeout', type=float, default=120, help='Export completion timeout in seconds')
    args = parser.parse_args()
    try:
        return export(args.fmp, args.timeout) if args.command == 'export' else check()
    except (OSError, ValueError, KeyError, ET.ParseError, RuntimeError) as error:
        print('ERROR: ' + str(error))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
