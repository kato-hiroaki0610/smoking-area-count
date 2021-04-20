import pathlib
import unittest

import toml
from file_reader_for_toml import FileReaderForToml as frt

SETTING_DIR = 'setting'
SETTING_FILE = 'setting.toml'


class TestFileReaderFortoml(unittest.TestCase):
    def create_toml(self):
        """setting用のtomlファイルを作成する"""
        csv_file = 'E:\\project\\smoking-area-count\\' \
                    'backend\\tests\\test_file\\video_source.csv' # noqa
        self.toml_data = {
            'detect_field_num': 4,
            'area':
            [
                {'場所': '5階', '利用者': csv_file, '待ち人数': '', '定員上限': 5},
                {'場所': '9階', '利用者': '', '待ち人数': '', '定員上限': 7},
                {'場所': '11階', '利用者': '', '待ち人数': '', '定員上限': 5}
            ]}

        pathlib.Path(SETTING_DIR).mkdir()
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).touch()

        with open(SETTING_DIR + '\\' + SETTING_FILE, 'wt', 
                  encoding='utf8') as fp:
            toml.dump(self.toml_data, fp)

    def setUp(self):
        self.create_toml()
        self.file_name = SETTING_DIR + '\\' + SETTING_FILE

    def tearDown(self):
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).unlink()
        pathlib.Path(SETTING_DIR).rmdir()

    def test_set_file_path(self):
        toml_reader = frt()
        toml_reader.set_file_path(self.file_name)
        actual = toml_reader._file_path

        self.assertEqual(self.file_name, actual)

        expected = 'path/to/csv'
        toml_reader.set_file_path('path/to/csv')
        actual = toml_reader._file_path

        self.assertEqual(expected, actual)

    def test_load_file(self):
        toml_reader = frt()
        toml_reader.set_file_path(self.file_name)
        toml_reader.load_file()
        contents = toml_reader._contents

        expected = type({})
        actual = type(contents)
        self.assertEqual(expected, type(contents))

        expected = 2
        actual = len(contents)
        self.assertEqual(expected, actual)
        self.assertEqual(self.toml_data, contents)
        expected = 4
        actual = contents['detect_field_num']
        self.assertEqual(expected, actual)

        expected = self.toml_data['area']
        actual = contents['area']
        self.assertEqual(expected, actual)

        toml_reader.set_file_path('path/to/csv')
        with self.assertRaises(FileNotFoundError) as e:
            toml_reader.load_file()

        err_message = 'path/to/csvが見つかりませんでした'
        actual = str(e.exception)
        self.assertEqual(err_message, actual)

    def test_get_contents(self):
        toml_reader = frt()
        toml_reader.set_file_path(self.file_name)
        toml_reader.load_file()

        contents = toml_reader.get_contents()

        expected = dict
        actual = type(contents)
        self.assertEqual(expected, actual)
        expected = 2
        actual = len(contents)
        self.assertEqual(expected, actual)
        expected = 4
        expected = self.toml_data['area'][0]
        actual = contents['area'][0]
        self.assertEqual(expected, actual)
        actual = contents
        self.assertEqual(self.toml_data, actual)
        self.assertEqual(self.toml_data['detect_field_num'], 
                         actual['detect_field_num'])
        self.assertEqual(self.toml_data['area'], actual['area'])
