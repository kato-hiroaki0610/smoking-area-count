"""CreateJsonクラスのテスト"""

import os
import unittest

from create_json import CreateJson


class TestCreateJson(unittest.TestCase):
    """CreateJsonクラスのテスト"""
    def test_get_last_row(self):
        """get_last_rowメソッドのテスト"""
        json_creater = CreateJson({})
        tests_dir = os.path.dirname(__file__)
        file_name = tests_dir + '/test_file/video_source.csv'

        expected = ['video_source', 'ymd', 'hms', 'fff', '5']
        actual = json_creater.get_last_row(file_name)

        self.assertEqual(expected, actual)

    def test_get_detect_column(self):
        """get_detect_columnのテスト"""
        json_creater = CreateJson({'detect_field_num': 1})

        test_list = [1, 2, 1, 2]
        expected = 2
        actual = json_creater.get_detect_column(test_list)
        self.assertEqual(expected, actual)

        json_creater._setting['detect_field_num'] = 0
        test_list = ['1']
        expected = 1
        actual = json_creater.get_detect_column(test_list)
        self.assertEqual(expected, actual)
        self.assertEqual(int, type(actual))
        self.assertNotEqual(str, type(actual))

        json_creater._setting['detect_field_num'] = 2
        test_list = [0, 1, -1]
        expected = -1
        actual = json_creater.get_detect_column(test_list)
        self.assertEqual(expected, actual)

        json_creater._setting['detect_field_num'] = 3
        test_list = [0, 1, 2, 9.9]
        expected = 9
        actual = json_creater.get_detect_column(test_list)
        self.assertEqual(expected, actual)
        expected = int
        actual = type(actual)
        self.assertEqual(expected, actual)
        expected = float
        self.assertNotEqual(float, actual)

    def test_is_capacity_over(self):
        """is_capacity_overのテスト"""
        json_creater = CreateJson({})

        contents = {
            '場所': '5階',
            '定員上限': 10,
        }

        expected = False
        actual = json_creater.is_capacity_over(contents, 9)
        self.assertEqual(expected, actual)

        expected = False
        actual = json_creater.is_capacity_over(contents, 10)
        self.assertEqual(expected, actual)

        expected = True
        actual = json_creater.is_capacity_over(contents, 11)
        self.assertEqual(expected, actual)

        contents['定員上限'] = '5'
        expected = False
        actual = json_creater.is_capacity_over(contents, 4)
        self.assertEqual(expected, actual)

        expected = False
        actual = json_creater.is_capacity_over(contents, 5)
        self.assertEqual(expected, actual)

        expected = True
        actual = json_creater.is_capacity_over(contents, 6)
        self.assertEqual(expected, actual)

    def test_execute_create(self):
        """execute_createのテスト"""
        json_creater = CreateJson({
            'detect_field_num':
            1,
            'area': [{
                '場所': '5階',
                '利用者': 'path/to/csv',
                '待ち人数': 'path/to/csv',
                '定員上限': 10
            }]
        })

        json_creater.execute_create()
        get_json = json_creater._created_json
        expected = 5

        actual = len(get_json[0])
        self.assertEqual(expected, actual)

        expected = [list, dict]
        actual = [type(get_json), type(get_json[0])]
        self.assertEqual(expected, actual)

    def test_get_created_json(self):
        """get_created_jsonのテスト"""
        tests_dir = os.path.dirname(__file__)
        file_name = tests_dir + '/test_file/video_source.csv'
        setting = {
            'detect_field_num':
            4,
            'area': [{
                '場所': '5階',
                '利用者': file_name,
                '待ち人数': file_name,
                '定員上限': 10
            }, {
                '場所': '9階',
                '利用者': file_name,
                '待ち人数': '',
                '定員上限': 3
            }, {
                '場所': 'aaa',
                '利用者': 'ddd',
                '待ち人数': file_name,
                '定員上限': 11
            }, {
                '場所': 'bbb',
                '利用者': file_name,
                '待ち人数': '',
                '定員上限': 5
            }]
        }
        json_creater = CreateJson(setting)

        json_creater.execute_create()
        created_json = json_creater.get_created_json()

        expected = [list, dict]
        actual = [type(created_json), type(created_json[0])]
        self.assertEqual(expected, actual)

        expected = setting['area'][0]['場所']
        actual = created_json[0]['room']
        self.assertEqual(expected, actual)

        expected = 5
        actual = created_json[0]['use']
        self.assertEqual(expected, actual)

        expected = 5
        actual = created_json[0]['wait']
        self.assertEqual(expected, actual)

        expected = False
        actual = created_json[0]['is_limit']
        self.assertEqual(expected, actual)

        expected = 10
        actual = created_json[0]['limit']
        self.assertEqual(expected, actual)

        expected = setting['area'][1]['場所']
        actual = created_json[1]['room']
        self.assertEqual(expected, actual)

        expected = ''
        actual = created_json[1]['wait']
        self.assertEqual(expected, actual)

        expected = 5
        actual = created_json[1]['use']
        self.assertEqual(expected, actual)

        expected = 3
        actual = created_json[1]['limit']
        self.assertEqual(expected, actual)

        expected = True
        actual = created_json[1]['is_limit']
        self.assertEqual(expected, actual)

        expected = setting['area'][2]['場所']
        actual = created_json[2]['room']
        self.assertEqual(expected, actual)

        expected = ''
        actual = created_json[2]['use']
        self.assertEqual(expected, actual)

        expected = 5
        actual = created_json[2]['wait']
        self.assertEqual(expected, actual)

        expected = 11
        actual = created_json[2]['limit']
        self.assertEqual(expected, actual)

        expected = ''
        actual = created_json[2]['is_limit']
        self.assertEqual(expected, actual)

        expected = 5
        actual = created_json[3]['use']
        self.assertEqual(expected, actual)

        expected = ''
        actual = created_json[3]['wait']
        self.assertEqual(expected, actual)

        expected = 5
        actual = created_json[3]['limit']
        self.assertEqual(expected, actual)

        expected = False
        actual = created_json[3]['is_limit']
        self.assertEqual(expected, actual)
