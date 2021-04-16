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

    def test_get_contents(self):
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        self.csv_create(csv_data, self.file_name)

        csv_reader = frc()
        csv_reader.set_file_path(self.file_name)
        csv_reader.load_file()

        expected = list()
        actual = csv_reader.get_contents()
        self.assertEqual(type(expected), type(actual))

        expected = '5'
        self.assertEqual(expected, actual[-1][self.detect_field_num])

        self.remove_csv(self.file_name)
