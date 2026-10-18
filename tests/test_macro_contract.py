"""Offline checks for the renamed macro contract, not native execution tests."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools'))
from fmide_run import quote
from install_bridge_macros import make_installer


class InstallerContractTests(unittest.TestCase):
    def test_definitions_preserve_script_text_and_metadata_with_new_keys(self):
        script = '[+].Exit Script = == JSONSetElement ( "{}" ; "error.code" ; 0 ; JSONNumber )\n'
        macro = {
            'macro_name': 'Example.Café "name"',
            'file': 'example.fmJAML',
            'version': 2,
            'sha256': hashlib.sha256(script.encode()).hexdigest(),
            'inputs': {'name': 'caller name', 'code': 'caller error code'},
            'effect': 'read',
        }
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / macro['file']).write_text(script)
            (folder / 'manifest.json').write_text(json.dumps({'macros': [macro]}))
            actions = json.loads(make_installer(folder))
        definitions = [a['fmIDE Define Macro'] for a in actions if 'fmIDE Define Macro' in a]
        self.assertEqual(len(definitions), 1)
        definition = definitions[0]
        self.assertEqual(list(definition), ['macro_name', 'metadata', 'script'])
        self.assertEqual(definition['macro_name'], quote(macro['macro_name']))
        self.assertEqual(definition['script'], quote(script))
        self.assertEqual(definition['metadata']['inputs'], macro['inputs'])
        self.assertEqual(definition['metadata']['source_sha256'], macro['sha256'])

    def test_library_preflights_and_verifies_identity_and_script(self):
        actions = json.loads(make_installer(REPO / 'macros/ai-bridge'))
        definitions = [i for i, a in enumerate(actions) if 'fmIDE Define Macro' in a]
        comparisons = [(i, a['If']) for i, a in enumerate(actions)
                       if 'JSONGetElement ( GetPersistentData' in a.get('If', '')]
        self.assertEqual(len(definitions), 8)
        self.assertEqual(len(comparisons), 16)
        self.assertTrue(all(i < definitions[0] for i, _ in comparisons[:8]))
        self.assertTrue(all(i > definitions[-1] for i, _ in comparisons[8:]))
        for _, condition in comparisons:
            self.assertIn('; "macro_name" )', condition)
            self.assertIn('; "script" )', condition)
            self.assertNotIn('; "name" )', condition)
            self.assertNotIn('; "code" )', condition)

    def test_changed_source_is_rejected_before_an_installer_is_returned(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / 'example.fmJAML').write_text('changed')
            (folder / 'manifest.json').write_text(json.dumps({'macros': [{
                'macro_name': 'Example', 'file': 'example.fmJAML',
                'sha256': hashlib.sha256(b'original').hexdigest(),
            }]}))
            with self.assertRaisesRegex(ValueError, 'Source hash mismatch'):
                make_installer(folder)


class NativeFixtureContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder = REPO / 'tests/fmIDEAS/macro-regression'
        cls.records = json.loads((cls.folder / 'records.json').read_text())
        manifest = json.loads((REPO / 'tests/fmIDEAS/manifest.json').read_text())
        cls.group = next(g for g in manifest['groups'] if g['name'] == 'macro-regression')

    def test_sources_record_snapshots_and_manifest_agree(self):
        by_id = {record['id']: record for record in self.records}
        self.assertEqual(len(by_id), self.group['count'])
        self.assertEqual(set(by_id), {entry['id'] for entry in self.group['tests']})
        for entry in self.group['tests']:
            with self.subTest(test=entry['title']):
                record = by_id[entry['id']]
                source = (self.folder / entry['file']).read_text().replace('\n', '\r')
                self.assertEqual(source, record['fmIDE_Parameter'])
                self.assertEqual(record['Title'], entry['title'])
                self.assertEqual(int(record['Sort']), entry['sort'])
                self.assertEqual(source.count('#@test\r'), 1)
                self.assertEqual(source.count('\r#@endtest'), 1)
                body = source.split('#@test\r', 1)[1].split('\r#@endtest', 1)[0]
                self.assertEqual(body, record['CodeUnderTest'])
                self.assertNotRegex(source, r'(?m)^\[:\]\.\s*\.code\s*=')
                self.assertNotRegex(source, r'JSONGetElement\s*\([^\r]*;\s*"(?:name|code)"\s*\)')

    def test_full_macro_expected_results_use_new_keys_and_preserve_metadata(self):
        for index in [0, 1, 4, 6, 7, 8, 9, 10, 15]:
            expected = json.loads(self.records[index]['TestExpectedResult'])
            macro = expected.get('macro', expected)
            with self.subTest(index=index + 1):
                self.assertTrue({'macro_name', 'script'} <= macro.keys())
                self.assertTrue(macro.keys() <= {'macro_name', 'metadata', 'script'})
                self.assertIsInstance(macro['script'], str)
                self.assertTrue(macro['macro_name'].startswith('fmIDE_Test.MacroRegression.'))
        metadata = json.loads(self.records[9]['TestExpectedResult'])['metadata']
        self.assertEqual(metadata, {
            'author': 'fmIDE regression tests',
            'description': 'Quotes " and backslash \\ and café',
            'version': 2,
        })

    def test_revised_cases_do_not_claim_old_native_passes(self):
        self.assertEqual(self.group['verificationStatus'], 'native_run_pending')
        self.assertIsNone(self.group['recordedPasses'])
        self.assertEqual(self.group['previousVerification']['recordedPasses'], 39)
        for record, entry in zip(self.records, self.group['tests']):
            self.assertIsNone(entry['recordedPass'])
            self.assertIsNone(entry['recordedAt'])
            for key in ['IsTested', 'TestActualResult', 'TestLastTimestamp',
                        'fmIDE_ScriptResult', '_kIsTestPass', '_kIsTestFail']:
                self.assertEqual(record[key], '', (record['id'], key))


if __name__ == '__main__':
    unittest.main()
