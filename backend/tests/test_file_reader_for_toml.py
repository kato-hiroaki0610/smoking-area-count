import os
import sys
import unittest

from file_reader_for_toml import FileReaderForToml as frt


class TestFileReaderFortoml(unittest.TestCase):
    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.file_name = tests_dir + '/test_file/setting.toml'

    def test_get_contents(self):
        toml_reader = frt()
        toml_reader.set_file_path(self.file_name)
        toml_reader.load_file()

        expect = dict
        actual = toml_reader.get_contents()

        self.assertEqual(expect, type(actual))
