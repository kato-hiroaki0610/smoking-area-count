import csv
import pathlib
import unittest

from file_reader_for_csv import FileReaderForCSV as frc


class TestFileReaderForCSV(unittest.TestCase):
    def setUp(self):
        self.file_name = 'tmp.csv'
        self.detect_field_num = 4

    def csv_create(self, csv_data, file_name):
        """CSVを作成する"""
        pathlib.Path('./\\' + file_name).touch()

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)

    def remove_csv(self, file_name):
        """CSVを削除する"""
        pathlib.Path(file_name).unlink()

    def test_set_file_path(self):
        csv_reader = frc()
        csv_reader.set_file_path(self.file_name)
        actual = csv_reader._file_path

        self.assertEqual(self.file_name, actual)

        expected = 'path/to/csv'
        csv_reader.set_file_path('path/to/csv')
        actual = csv_reader._file_path

        self.assertEqual(expected, actual)

    def test_load_file(self):
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        self.csv_create(csv_data, self.file_name)

        csv_reader = frc()
        csv_reader.set_file_path(self.file_name)
        csv_reader.load_file()

        self.remove_csv(self.file_name)

        expected = type([])
        contents = csv_reader._contents

        actual = type(contents)
        self.assertEqual(expected, type(contents))
        expected = 3
        actual = len(contents)
        self.assertEqual(expected, actual)
        expected = 5
        actual = len(contents[0])
        self.assertEqual(expected, actual)
        self.assertEqual(csv_data, contents)

        csv_reader.set_file_path('path/to/csv')
        with self.assertRaises(FileNotFoundError) as e:
            csv_reader.load_file()

        err_message = 'path/to/csvが見つかりませんでした'
        actual = str(e.exception)
        self.assertEqual(err_message, actual)

    def test_get_contents(self):
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        self.csv_create(csv_data, self.file_name)

        csv_reader = frc()
        csv_reader.set_file_path(self.file_name)
        csv_reader.load_file()
        actual = csv_reader.get_contents()

        expected = list()
        self.assertEqual(type(expected), type(actual))
        expected = 3
        self.assertEqual(expected, len(actual))
        expected = 5
        self.assertEqual(expected, len(actual[0]))
        self.assertEqual(csv_data, actual)
        self.assertEqual(csv_data[0], actual[0])
        self.assertEqual(csv_data[0], actual[-1])

        self.remove_csv(self.file_name)
