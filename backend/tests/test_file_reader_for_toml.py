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
        toml_data = {
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
            toml.dump(toml_data, fp)

    def setUp(self):
        self.create_toml()
        self.file_name = SETTING_DIR + '\\' + SETTING_FILE

    def tearDown(self):
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).unlink()
        pathlib.Path(SETTING_DIR).rmdir()

    def test_get_contents(self):
        toml_reader = frt()
        toml_reader.set_file_path(self.file_name)
        toml_reader.load_file()

        expect = dict
        actual = toml_reader.get_contents()

        self.assertEqual(expect, type(actual))
