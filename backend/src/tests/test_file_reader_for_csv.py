import os
import unittest

from file_reader_for_csv import FileReaderForCSV as frc


class TestFileReaderForCSV(unittest.TestCase):
    def setUp(self):
        tests_dir = os.path.dirname(__file__)
        self.file_name = tests_dir + '/test_file/video_source.csv'

    def test_parse_file(self):
        csv_reader = frc()
        csv_reader.set_input_file(self.file_name)

        expected = '2'
        actual = csv_reader.parse_file()

        self.assertEqual(expected, actual)
