#!/usr/bin/env python3
"""Stage, prepare and package an fmIDE release candidate without modifying the source file."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import uuid
import zipfile
from fmide_run import dispatch, quote, collect

REPO = Path(__file__).resolve().parents[1]


def sha256(path):
    with path.open('rb') as stream:
        digest=hashlib.sha256()
        for block in iter(lambda:stream.read(1024*1024),b''):digest.update(block)
    return digest.hexdigest()


def require_ok(response):
    if response['last_error'].strip()!='0' or not isinstance(response['result'],dict) or response['result'].get('ok') is not True:
        raise RuntimeError('FileMaker operation did not verify: '+json.dumps(response['result'],ensure_ascii=False))
    return response['result']


def write_state(path,state):
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n');temp.replace(path)


def stage(args):
    source=Path(args.database_path).resolve()
    if not source.is_file() or source.suffix.lower()!='.fmp12':raise ValueError('Source must be a local .fmp12 file')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,63}',args.version):raise ValueError('Use a simple release label, e.g. v0.94')
    root=Path(args.output_dir).resolve()
    if root.exists():raise ValueError('Output directory must not already exist')
    if shutil.disk_usage(root.parent).free<10*1024**3:raise RuntimeError('Less than 10 GiB free')
    root.relative_to(Path.home()/'Documents')  # Same local transport constraint as fmide_run.
    root.mkdir()
    name='fmIDE-release-work-'+uuid.uuid4().hex[:12]
    working=root/(name+'.fmp12')
    relative=working.relative_to(Path.home()/'Documents').as_posix()
    probe=require_ok(dispatch((REPO/'tools/probe-context.fmIDEAS').read_text(),fmp=args.fmp,file_name=args.file,database_path=str(source)))
    actual=probe['context']
    if not actual['file_path'].endswith(str(source)) or actual['fmide_release']!=args.expected_release:
        raise RuntimeError('Wrong source path or release string')
    # Use the source's verified Documents path calculation instead of assuming a volume name.
    code=(REPO/'macros/ai-bridge/backup.fmIDEAS').read_text()
    code='[+].Set.$backup_file_path = == Get ( DocumentsPath ) & '+quote(relative)+'\n'+code
    result=require_ok(dispatch(code,fmp=args.fmp,file_name=args.file,database_path=str(source)))
    if not working.is_file() or working.stat().st_size!=result['data']['bytes']:raise RuntimeError('Staged copy size mismatch')
    state={'schema_version':1,'phase':'staged','created_at':datetime.now(timezone.utc).isoformat(),
           'version':args.version,'expected_release':args.expected_release,'fmp':args.fmp,
           'source_path':str(source),'source_filemaker_path':actual['file_path'],'source_file_name':args.file,
           'working_path':str(working),'working_filemaker_path':result['data']['file_path'],
           'working_file_name':name,'stage_sha256':sha256(working)}
    write_state(root/'release-state.json',state)
    print('Staged:',working)
    print('Open this uniquely named copy in FileMaker '+args.fmp+', then run:')
    print('python3 tools/release_fmide.py prepare --state '+repr(str(root/'release-state.json')))


def prepare(args):
    path=Path(args.state).resolve();state=json.loads(path.read_text())
    if state['phase']!='staged':raise ValueError('Only a staged candidate can be prepared')
    working=Path(state['working_path'])
    if working.parent!=path.parent or working.name!=state['working_file_name']+'.fmp12' or not working.name.startswith('fmIDE-release-work-'):
        raise ValueError('Invalid staging identity')
    candidate=path.parent/'fmIDE.fmp12'
    if candidate.exists():raise ValueError('Candidate already exists; inspect the previous outcome')
    output=state['working_filemaker_path'].rsplit('/',1)[0]+'/fmIDE.fmp12'
    values={'release_source_path':state['source_filemaker_path'],'release_expected_release':state['expected_release'],'release_output_path':output}
    state['phase']='preparing';write_state(path,state)
    result=require_ok(dispatch((REPO/'tools/prepare-release.fmIDEAS').read_text(),fmp=state['fmp'],file_name=state['working_file_name'],database_path=str(working),values=values,timeout=240))
    finish_preparation(path,state,result)


def finish_preparation(path,state,result):
    working=Path(state['working_path']);candidate=path.parent/'fmIDE.fmp12'
    if not result['file_path'].endswith(str(working)) or result['release']!=state['expected_release'] or not candidate.is_file() or candidate.stat().st_size!=result['bytes']:
        raise RuntimeError('Candidate identity or size mismatch')
    state.update(phase='prepared',candidate_path=str(candidate),candidate_sha256=sha256(candidate),preparation=result)
    write_state(path,state);print('Prepared:',candidate);print('SHA256:',state['candidate_sha256'])


def recover(args):
    path=Path(args.state).resolve();state=json.loads(path.read_text())
    if state['phase']!='preparing':raise ValueError('Only an unresolved preparation can be recovered')
    response=collect(Path(args.response).resolve())
    if response['request']['database_path']!=state['working_path']:raise ValueError('Response belongs to another database')
    finish_preparation(path,state,require_ok(response))


def package(args):
    path=Path(args.state).resolve();state=json.loads(path.read_text())
    if state['phase']!='prepared':raise ValueError('A verified prepared candidate is required')
    candidate=Path(state['candidate_path'])
    if candidate.parent!=path.parent or sha256(candidate)!=state['candidate_sha256']:raise ValueError('Candidate changed after preparation')
    manifest={'version':state['version'],'fmide_release':state['expected_release'],'created_at':datetime.now(timezone.utc).isoformat(),
              'file':'fmIDE.fmp12','bytes':candidate.stat().st_size,'sha256':state['candidate_sha256'],'status':'release candidate; not published'}
    archive=path.parent/('fmIDE-'+state['version']+'.zip')
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED) as z:
        z.write(candidate,'fmIDE.fmp12');z.writestr('manifest.json',json.dumps(manifest,indent=2)+'\n')
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None or hashlib.sha256(z.read('fmIDE.fmp12')).hexdigest()!=state['candidate_sha256']:raise RuntimeError('Archive verification failed')
    state.update(phase='packaged',archive=str(archive),archive_sha256=sha256(archive));write_state(path,state)
    print('Packaged:',archive);print('SHA256:',state['archive_sha256']);print('No commit, tag, push or GitHub release was performed.')


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    s=sub.add_parser('stage');s.add_argument('--fmp',required=True);s.add_argument('--file',required=True);s.add_argument('--database-path',required=True);s.add_argument('--version',required=True);s.add_argument('--expected-release',required=True);s.add_argument('--output-dir',required=True);s.set_defaults(run=stage)
    for name,fn in [('prepare',prepare),('package',package)]:
        s=sub.add_parser(name);s.add_argument('--state',required=True,type=Path);s.set_defaults(run=fn)
    s=sub.add_parser('recover');s.add_argument('--state',required=True,type=Path);s.add_argument('--response',required=True,type=Path);s.set_defaults(run=recover)
    a=p.parse_args()
    try:a.run(a)
    except (OSError,ValueError,KeyError,RuntimeError,TimeoutError) as e:p.exit(2,'ERROR: '+str(e)+'\n')


if __name__=='__main__':main()
