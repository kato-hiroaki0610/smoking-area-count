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
