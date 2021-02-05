"""CreateJsonクラスのテスト"""

import unittest

from src.create_json import CreateJson


class TestCreateJson(unittest.TestCase):
    """CreateJsonクラスのテスト"""

    def test_get_last_row(self):
        """get_last_rowメソッドのテスト"""
        json_creater = CreateJson([[], []], {})

        test_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

        expected = [6, 7, 8]

        actual = json_creater.get_last_row(test_list)

        self.assertEqual(expected, actual)

    def test_get_detect_column(self):
        """get_detect_columnのテスト"""
        json_creater = CreateJson([[0, 1], ['1', 2, -1, 9.99]],
                                  {'detect_field_num': 1})

        expected = 2
        actual = json_creater.get_detect_column()
        self.assertEqual(expected, actual)

        json_creater._setting['detect_field_num'] = 0
        expected = 1
        actual = json_creater.get_detect_column()
        self.assertEqual(expected, actual)
        self.assertEqual(int, type(actual))
        self.assertNotEqual(str, type(actual))

        json_creater._setting['detect_field_num'] = 2
        expected = -1
        actual = json_creater.get_detect_column()
        self.assertEqual(expected, actual)

        json_creater._setting['detect_field_num'] = 3
        expected = 9
        actual = json_creater.get_detect_column()
        self.assertEqual(expected, actual)
        self.assertEqual(int, type(actual))
        self.assertNotEqual(float, type(actual))

    def test_is_capacity_over(self):
        """is_capacity_overのテスト"""
        json_creater = CreateJson([[0, 1], [5, 10]],
                                  {'capacity_limit': {
                                      '5F': 10
                                  }})

        expected = True
        actual = json_creater.is_capacity_over(9)
        self.assertEqual(expected, actual)

        expected = True
        actual = json_creater.is_capacity_over(10)
        self.assertEqual(expected, actual)

        expected = False
        actual = json_creater.is_capacity_over(11)
        self.assertEqual(expected, actual)

        json_creater._setting['capacity_limit']['5F'] = '5'
        expected = True
        actual = json_creater.is_capacity_over(4)
        self.assertEqual(expected, actual)

        expected = True
        actual = json_creater.is_capacity_over(5)
        self.assertEqual(expected, actual)

        expected = False
        actual = json_creater.is_capacity_over(6)
        self.assertEqual(expected, actual)
