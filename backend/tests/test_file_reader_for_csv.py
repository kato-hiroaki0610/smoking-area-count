import os
import sys
import unittest

path = os.path.join(os.path.dirname(__file__), '../src')
sys.path.append(path)

from file_reader_for_csv import FileReaderForCSV as frc  # noqa


class TestFileReaderForCSV(unittest.TestCase):
    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.file_name = tests_dir + '/test_file/video_source.csv'
        self.detect_field_num = 4

    def test_get_contents(self):
        csv_reader = frc()
        csv_reader.set_file_path(self.file_name)
        csv_reader.load_file()

        expected = list()
        actual = csv_reader.get_contents()
        self.assertEqual(type(expected), type(actual))

        expected = '2'
        self.assertEqual(expected, actual[-1][self.detect_field_num])
