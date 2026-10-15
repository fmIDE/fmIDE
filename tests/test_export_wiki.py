"""Check that incomplete or unsafe Wiki exports cannot replace the last good docs."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


class WikiValidationTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location(
            'export_wiki', Path(__file__).resolve().parents[1] / 'tools/export_wiki.py')
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.manifest = {
            'generator': self.module.GENERATOR, 'actionCount': 2,
            'pages': [{'id': 'action-a', 'file': 'first.md'},
                      {'id': 'action-b', 'file': 'second.md'}],
        }
        self.write_manifest()
        marker = '<!-- Generated from fmIDE_Action. Edit the database, then export again. -->\n'
        self.marker = marker
        (self.folder / 'first.md').write_text(marker + '# First café\n[Next](second.md)\n', encoding='utf-8')
        (self.folder / 'second.md').write_text(marker + '# Second\n[All](README.md)\n', encoding='utf-8')
        (self.folder / 'README.md').write_text(marker + '\n'.join([
            '| Action | Summary | Support | State | Since | Alias |',
            '| --- | --- | --- | --- | --- | --- |',
            '| [First](first.md) | First summary | Yes | Ready | v1 | |',
            '| [Second](second.md) | Second summary | Yes | Ready | v1 | |',
        ]) + '\n', encoding='utf-8')

    def write_manifest(self):
        (self.folder / '_manifest.json').write_text(json.dumps(self.manifest), encoding='utf-8')

    def reject(self):
        with self.assertRaises(ValueError):
            self.module.validate(self.folder, 2)

    def test_complete_unicode_export_is_valid(self):
        self.assertEqual(self.module.validate(self.folder, 2), self.manifest)

    def test_missing_page_is_rejected(self):
        (self.folder / 'second.md').unlink()
        self.reject()

    def test_duplicate_identity_is_rejected(self):
        self.manifest['pages'][1]['id'] = 'action-a'
        self.write_manifest()
        self.reject()

    def test_path_outside_export_is_rejected(self):
        self.manifest['pages'][1]['file'] = '../second.md'
        self.write_manifest()
        self.reject()

    def test_link_to_missing_page_is_rejected(self):
        with (self.folder / 'first.md').open('a', encoding='utf-8') as stream:
            stream.write('[Missing](missing.md)\n')
        self.reject()

    def test_control_character_is_rejected(self):
        with (self.folder / 'first.md').open('a', encoding='utf-8') as stream:
            stream.write('hidden\x1dcharacter\n')
        self.reject()

    def test_header_must_match_six_column_rows(self):
        path = self.folder / 'README.md'
        path.write_text(path.read_text().replace(' Summary |', '', 1))
        self.reject()

    def test_symlink_page_is_rejected(self):
        path = self.folder / 'second.md'
        path.unlink()
        try:
            path.symlink_to(self.folder / 'first.md')
        except OSError as error:
            self.skipTest('Symlinks unavailable: ' + str(error))
        self.reject()


if __name__ == '__main__':
    unittest.main()
