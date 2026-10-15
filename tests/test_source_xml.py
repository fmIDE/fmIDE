import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest


class FreshnessTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('source_xml', Path(__file__).resolve().parents[1] / 'tools/source_xml.py')
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.module.DATABASE = root / 'fmIDE.fmp12'
        self.module.XML = root / 'fmIDE.xml'
        self.module.MANIFEST = root / 'manifest.json'
        self.module.DATABASE.write_bytes(b'fixture database')
        self.module.XML.write_text('<FMSaveAsXML/>')
        self.module.MANIFEST.write_text(json.dumps({
            'exportedAt': '2026-10-13T00:00:00Z',
            'source': {'stat': self.module.stamp(self.module.DATABASE)},
            'xml': {'sha256': self.module.digest(self.module.XML)},
        }))

    def check(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return self.module.check()

    def test_unchanged_is_current(self):
        self.assertEqual(self.check(), 0)

    def test_modification_time_only_change_is_stale(self):
        p = self.module.DATABASE
        stat = p.stat()
        os.utime(p, ns=(stat.st_atime_ns, stat.st_mtime_ns + 1_000_000_000))
        self.assertEqual(self.check(), 1)

    def test_xml_tampering_is_stale(self):
        self.module.XML.write_text('<changed/>')
        self.assertEqual(self.check(), 1)

    def test_missing_manifest_is_unknown(self):
        self.module.MANIFEST.unlink()
        self.assertEqual(self.check(), 2)

    def test_missing_xml_is_unknown(self):
        self.module.XML.unlink()
        self.assertEqual(self.check(), 2)


if __name__ == '__main__':
    unittest.main()
