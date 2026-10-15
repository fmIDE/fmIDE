#!/usr/bin/env python3
"""Generate Name that Thing reference pages from the live parameter table."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import tempfile
from fmide_run import dispatch

REPO = Path(__file__).resolve().parents[1]
GENERATOR = 'fmIDE Name that Thing parameter exporter v1'


def clean(text):
    return ''.join(c for c in str(text).replace('\r\n','\n').replace('\r','\n') if c in '\n\t' or ord(c)>=32)


def cell(text):
    return clean(text).replace('|','&#124;').replace('\n','<br>')


def render(snapshot, destination, action_manifest):
    records = snapshot['parameters']
    if snapshot.get('queryError') or not records:
        raise ValueError('Parameter query failed or returned no records')
    ids = [r['id'] for r in records]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate parameter UUIDs')
    actions = {p['name'].casefold():p['file'] for p in action_manifest['pages']}
    pages=[]
    rows=['| Parameter | Type | Active | State | Default action |','| --- | --- | --- | --- | --- |']
    marker='<!-- Generated from NameThatThingParameter. Edit the database, then export again. -->\n'
    for r in records:
        name=r['ParameterName']
        slug=re.sub('[^a-z0-9]+','-',name.lower()).strip('-') or 'action-array'
        filename=slug+'.md'
        if filename in [p['file'] for p in pages] or filename=='readme.md':
            raise ValueError('Duplicate parameter filename: '+filename)
        action=clean(r['DefaultAction'])
        if action.casefold() in actions:
            action='['+action+'](../actions/'+actions[action.casefold()]+')'
        description=clean(r['Description']).strip() or 'No description is recorded in the source table yet.'
        content=marker+'# Parameter `'+name+'`\n\n[All parameters](README.md) · [Name that Thing](../name-that-thing.md)\n\n'+description+'\n\n'
        content+='| Property | Value |\n| --- | --- |\n'
        for label,value in [('Type',r['DataType']),('Active','Yes' if r['Active']=='1' else 'No'),('Development state',r['DevState']),('Category',r['Category']),('Default action',action),('Default value',r['DefaultValue'] or 'Not recorded')]:
            content+='| '+label+' | '+cell(value)+' |\n'
        if r['TriggeredActions']:
            content+='\n## Stored action mapping\n\nThis is the mapping recorded by the demo file. It may use construction-time variables; it is not a standalone script.\n\n```fmjaml\n'+clean(r['TriggeredActions']).rstrip()+'\n```\n'
        (destination/filename).write_text(content,encoding='utf-8')
        pages.append({'id':r['id'],'name':name,'file':filename})
        rows.append('| [`'+cell(name)+'`]('+filename+') | '+cell(r['DataType'])+' | '+('Yes' if r['Active']=='1' else 'No')+' | '+cell(r['DevState'])+' | '+cell(action)+' |')
    intro=marker+'# Name that Thing parameters\n\nThese '+str(len(records))+' entries come from the live `NameThatThingParameter` table. Active and development-state values are preserved; proposed entries are not promises of implemented behavior. Blank descriptions remain explicit documentation gaps.\n\n[API guide](../name-that-thing.md) · [Actions](../actions/README.md)\n\n'
    (destination/'README.md').write_text(intro+'\n'.join(rows)+'\n',encoding='utf-8')
    manifest={'generator':GENERATOR,'exported_at':datetime.now(timezone.utc).isoformat(),'fmide_release':snapshot['release'],'filemaker_version':snapshot['application'],'parameter_count':len(records),'pages':pages}
    (destination/'_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return manifest


def publish(snapshot):
    docs=REPO/'docs';target=docs/'parameters'
    stage=Path(tempfile.mkdtemp(prefix='.parameter-export-',dir=docs))
    previous=None
    try:
        manifest=render(snapshot,stage,json.loads((docs/'actions/_manifest.json').read_text()))
        if target.exists():
            if target.is_symlink() or json.loads((target/'_manifest.json').read_text()).get('generator')!=GENERATOR:
                raise ValueError('Refusing to replace unowned parameter documentation')
            previous=docs/('.parameter-previous-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
            target.rename(previous)
        try:stage.rename(target)
        except BaseException:
            if previous:previous.rename(target)
            raise
        print('Published',manifest['parameter_count'],'parameter pages to',target)
    finally:
        if stage.exists():shutil.rmtree(stage)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--fmp',required=True);p.add_argument('--timeout',type=float,default=240);a=p.parse_args()
    result=dispatch((REPO/'tools/export-parameters.fmJAML').read_text(),fmp=a.fmp,file_name='fmIDE',database_path=str(REPO/'fmIDE.fmp12'),timeout=a.timeout)
    snapshot=result['result']
    if result['last_error'].strip()!='0' or not isinstance(snapshot,dict) or not snapshot.get('file','').endswith(str(REPO/'fmIDE.fmp12')):
        raise RuntimeError('Wrong or failed FileMaker response; previous pages preserved')
    publish(snapshot)


if __name__=='__main__':main()
