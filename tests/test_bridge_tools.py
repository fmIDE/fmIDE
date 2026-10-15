import argparse
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
import fmide_run
import release_fmide
import export_parameters


class CompletionTests(unittest.TestCase):
    def test_plain_text_result_preserves_cr_and_removes_only_transport_lf(self):
        with tempfile.TemporaryDirectory() as tmp:
            response=Path(tmp)/'request';response.mkdir()
            (response/'request.json').write_text('{"request_id":"one"}')
            for name in fmide_run.NAMES:
                (response/(name+'.txt')).write_bytes(('first\rsecond\n\n' if name=='script_result' else '0\n').encode())
            result=fmide_run.collect(response)
            self.assertEqual(result['script_result'],'first\rsecond\n')
            self.assertEqual(result['result'],'first\rsecond\n')

    def test_timeout_preserves_pending_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);response=root/'request';response.mkdir()
            request={'request_id':'one'}
            (response/'request.json').write_text(json.dumps(request));(root/'pending.json').write_text(json.dumps(request))
            with self.assertRaises(TimeoutError):fmide_run.collect(response)
            self.assertTrue((root/'pending.json').exists())

    def test_late_completion_clears_only_its_own_pending_request(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);response=root/'request';response.mkdir()
            (response/'request.json').write_text('{"request_id":"one"}')
            (root/'pending.json').write_text('{"request_id":"other"}')
            for name in fmide_run.NAMES:
                (response/(name+'.txt')).write_text('{"ok":true}\n' if name=='script_result' else '0\n')
            self.assertTrue(fmide_run.collect(response)['result']['ok'])
            self.assertTrue((root/'pending.json').exists())
            (root/'pending.json').write_text('{"request_id":"one"}')
            fmide_run.collect(response)
            self.assertFalse((root/'pending.json').exists())

    def test_parameter_names_cannot_inject_frontmatter(self):
        for key in ['x; $other','$$global','name = 1','fmide_debugger','bridge_error']:
            with self.subTest(key=key),self.assertRaises(ValueError):fmide_run.variable_definitions({key:'value'})

    def test_text_representation_preserves_control_characters(self):
        expression=fmide_run.quote('a\r\nb¶"\\“curly”')
        self.assertIn('Char ( 13 )',expression);self.assertIn('Char ( 10 )',expression);self.assertIn('Char ( 182 )',expression)
        self.assertNotIn('\n',expression);self.assertNotIn('\r',expression)
        self.assertIn('Char ( 8220 )',expression);self.assertIn('Char ( 8221 )',expression)
        self.assertIn('\\"',expression);self.assertIn('\\\\',expression)


class ReleaseTests(unittest.TestCase):
    def fixture(self, root):
        root=root.resolve();candidate=root/'fmIDE.fmp12';candidate.write_bytes(b'candidate bytes for archive verification')
        state={'phase':'prepared','version':'v-test','expected_release':'test','candidate_path':str(candidate),'candidate_sha256':release_fmide.sha256(candidate)}
        path=root/'release-state.json';path.write_text(json.dumps(state));return path,candidate

    def test_package_rejects_changed_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path,candidate=self.fixture(Path(tmp));candidate.write_bytes(b'changed')
            with self.assertRaises(ValueError):release_fmide.package(argparse.Namespace(state=path))
            self.assertEqual(list(path.parent.glob('*.zip')),[])

    def test_package_contains_exact_verified_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path,candidate=self.fixture(Path(tmp));release_fmide.package(argparse.Namespace(state=path))
            with zipfile.ZipFile(path.parent/'fmIDE-v-test.zip') as z:
                self.assertEqual(set(z.namelist()),{'fmIDE.fmp12','manifest.json'})
                self.assertEqual(z.read('fmIDE.fmp12'),candidate.read_bytes())

    def test_package_refuses_unprepared_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path,candidate=self.fixture(Path(tmp));s=json.loads(path.read_text());s['phase']='preparing';path.write_text(json.dumps(s))
            with self.assertRaises(ValueError):release_fmide.package(argparse.Namespace(state=path))


class ParameterDocsTests(unittest.TestCase):
    def test_duplicate_slugs_do_not_silently_replace_a_page(self):
        record={'id':'a','ParameterName':'field_name','DataType':'String','Active':'1','DevState':'ok','Category':'1','DefaultAction':'','DefaultValue':'','Description':'','TriggeredActions':''}
        second=dict(record,id='b',ParameterName='field-name')
        snapshot={'parameters':[record,second],'release':'test','application':'test','queryError':''}
        with tempfile.TemporaryDirectory() as tmp,self.assertRaises(ValueError):
            export_parameters.render(snapshot,Path(tmp),{'pages':[]})


if __name__=='__main__':unittest.main()
