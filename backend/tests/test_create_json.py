"""CreateJsonのテスト"""

import sys
import unittest

from src.create_json import CreateJson

#path = os.path.join(os.path.dirname(__file__), '../src')
#sys.path.append(path)

#from create_json import CreateJson as cj  # noqa


class TestCreateJson(unittest.TestCase):
    # def setUp(self):

    def test_get_last_row(self):
        json_creater = CreateJson([[], []], {})

        test_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

        expected = [6, 7, 8]

        actual = json_creater.get_last_row(test_list)

        self.assertEqual(expected, actual)
