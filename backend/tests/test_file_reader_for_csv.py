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

    def test_load_file(self):
        csv_reader = frc()
        csv_reader.set_file_path(self.file_name)

        expected = '2'
        actual = csv_reader.load_file()

        self.assertEqual(expected, actual)