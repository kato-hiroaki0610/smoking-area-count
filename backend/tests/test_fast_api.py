import csv
import pathlib
import sys
import unittest
import urllib

import toml
from fast_api import app, get_frontend_path, read_toml
from starlette.testclient import TestClient

SETTING_DIR = 'setting'
SETTING_FILE = 'setting.toml'


class TestFastAPI(unittest.TestCase):
    def create_toml(self, toml_data):
        """setting用のtomlファイルを作成する"""
        if pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).exists():
            self.remove_toml()

        pathlib.Path(SETTING_DIR).mkdir()
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).touch()

        with open(SETTING_DIR + '\\' + SETTING_FILE, 'wt',
                  encoding='utf8') as fp:
            toml.dump(toml_data, fp)

    def remove_toml(self):
        """tomlを削除する"""
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).unlink()
        pathlib.Path(SETTING_DIR).rmdir()

    def csv_create(self, csv_data, file_name):
        """CSVを作成する"""
        pathlib.Path('./\\' + file_name).touch()

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)

    def remove_csv(self, file_name):
        """CSVを削除する"""
        pathlib.Path(file_name).unlink()

    def setUp(self):
        """webディレクトリを作成し、clientのインスタンスを作成する"""
        pathlib.Path('web').mkdir()
        self.client = TestClient(app)

    def tearDown(self):
        """webディレクトリを削除する"""
        pathlib.Path('web').rmdir()

    def test_main(self):
        """/APIのテスト"""
        csv_file_name = 'tmp.csv'
        csv_file_name2 = 'tmp2.csv'

        toml_data = {
            'detect_field_num': 4,
            'area':
            [
              {'場所': '5階', '利用者': csv_file_name, '待ち人数': '', '定員上限': 5},
              {'場所': '9階', '利用者': '', '待ち人数': '', '定員上限': 7},
              {'場所': '11階', '利用者': '', '待ち人数': '', '定員上限': 5},
              {'場所': '12階', '利用者': '', '待ち人数': csv_file_name2, '定員上限': 5}
            ]}
        self.create_toml(toml_data)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        self.csv_create(csv_data, csv_file_name)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '10']]
        self.csv_create(csv_data, csv_file_name2)

        response = self.client.get('/')

        expected = 200
        actual = response.status_code
        self.assertEqual(expected, actual)

        expecteds = [{
            'room': '5階',
            'use': 5,
            'limit': 5,
            'is_limit': False,
            'wait': ''
        }, {
            'room': '9階',
            'use': '',
            'limit': 7,
            'is_limit': '',
            'wait': ''
        }, {
            'room': '11階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': ''
        }, {
            'room': '12階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': 10
        }]
        response_json = response.json()

        expected = dict
        actual = type(response_json)

        is_room_status_key_exists = 'room_status' in response_json.keys()
        self.assertTrue(is_room_status_key_exists)

        expected = len(expecteds[0])
        actual = response_json['room_status']
        self.assertEqual(expected, len(actual[0]))
        for i in range(len(expecteds)):
            is_key_exists = actual[i].keys() >= {'room',
                                                 'use',
                                                 'limit',
                                                 'is_limit',
                                                 'wait'}
            self.assertTrue(is_key_exists)
            self.assertEqual(expecteds[i], actual[i])

        self.remove_csv(csv_file_name)
        self.remove_csv(csv_file_name2)
        self.remove_toml()

    def test_specified_room(self):
        """specified apiのテスト"""
        csv_file_name = 'tmp.csv'
        toml_data = {
            'detect_field_num': 4,
            'area':
            [
              {'場所': '5階', '利用者': csv_file_name, '待ち人数': '', '定員上限': 5},
              {'場所': '9階', '利用者': '', '待ち人数': '', '定員上限': 7},
              {'場所': '11階', '利用者': '', '待ち人数': '', '定員上限': 5},
            ]}
        self.create_toml(toml_data)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        self.csv_create(csv_data, csv_file_name)

        expecteds = [{
            'room': '5階',
            'use': 5,
            'limit': 5,
            'is_limit': False,
            'wait': ''
        }, {
            'room': '9階',
            'use': '',
            'limit': 7,
            'is_limit': '',
            'wait': ''
        }, {
            'room': '11階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': ''
        }, {
            'room': '12階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': 10
        }]

        target_room = ['5階', '9階']
        responses = {}
        for t in target_room:
            responses[t] = self.client.get(f'/specified?room={t}')

        # 複数のパラメーターを期待していない場合FastAPIが自動で末尾のパラメーターのみにしてくれる
        target_room.append('11階')
        responses['11階'] = self.client.get('/specified?room=5階&room=11階')

        for r in responses.values():
            expected = 200
            actual = r.status_code
            self.assertEqual(expected, actual)

            response_json = r.json()
            expected = dict
            actual = type(response_json)

            is_room_status_key_exists = 'room_status' in response_json.keys()
            self.assertTrue(is_room_status_key_exists)

            expected = len(expecteds[0])
            actual = response_json['room_status']
            self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            if expecteds[i]['room'] in target_room:
                tmp = responses[expecteds[i]['room']]
                response_json = tmp.json()
                actual = response_json['room_status']
                is_key_exists = actual[0].keys() >= {'room',
                                                     'use',
                                                     'limit',
                                                     'is_limit',
                                                     'wait'}
                self.assertTrue(is_key_exists)
                self.assertEqual(expecteds[i], actual[0])

        response = self.client.get('/specified?room=15階')
        expected = 204
        actual = response.status_code
        self.assertEqual(expected, actual)

        response_json = response.json()
        expected = 'room not found'
        actual = response_json['detail'][0]['msg']
        self.assertEqual(expected, actual)

        response = self.client.get('/specified?roo')
        expected = 422
        actual = response.status_code
        self.assertEqual(expected, actual)

        response_json = response.json()
        expected = 'field required'
        actual = response_json['detail'][0]['msg']
        self.assertEqual(expected, actual)

        self.remove_csv(csv_file_name)
        self.remove_toml()

    def test_multiple_room(self):
        """multiple apiのテスト"""
        csv_file_name = 'tmp.csv'
        toml_data = {
            'detect_field_num': 4,
            'area':
            [
              {'場所': '5階', '利用者': csv_file_name, '待ち人数': '', '定員上限': 5},
              {'場所': '9階', '利用者': '', '待ち人数': '', '定員上限': 7},
              {'場所': '11階', '利用者': '', '待ち人数': '', '定員上限': 5}
            ]}
        self.create_toml(toml_data)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        self.csv_create(csv_data, csv_file_name)

        target_rooms = ['5階', '9階', '11階']
        response = self.client.get(
            f'/multiple?room={target_rooms[0]}&room={target_rooms[2]}')

        expected = 200
        actual = response.status_code
        self.assertEqual(expected, actual)

        expecteds = [{
            'room': '5階',
            'use': 5,
            'limit': 5,
            'is_limit': False,
            'wait': ''
        }, {
            'room': '11階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': ''
        }]
        response_json = response.json()

        expected = dict
        actual = type(response_json)

        is_room_status_key_exists = 'room_status' in response_json.keys()
        self.assertTrue(is_room_status_key_exists)

        expected = len(expecteds[0])
        actual = response_json['room_status']

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            is_key_exists = actual[i].keys() >= {'room',
                                                 'use',
                                                 'limit',
                                                 'is_limit',
                                                 'wait'}
            self.assertTrue(is_key_exists)
            self.assertEqual(expecteds[i], actual[i])

        expecteds = [{
            'room': '5階',
            'use': 5,
            'limit': 5,
            'is_limit': False,
            'wait': ''
        }, {
            'room': '9階',
            'use': '',
            'limit': 7,
            'is_limit': '',
            'wait': ''
        }, {
            'room': '11階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': ''
        }]

        response = self.client.get('/multiple?'
                                   f'room={target_rooms[0]}'
                                   f'&room={target_rooms[1]}'
                                   f'&room={target_rooms[2]}')
        response_json = response.json()

        expected = len(expecteds[0])
        actual = response_json['room_status']
        is_room_status_key_exists = 'room_status' in response_json.keys()
        self.assertTrue(is_room_status_key_exists)
        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            is_key_exists = actual[i].keys() >= {'room',
                                                 'use',
                                                 'limit',
                                                 'is_limit',
                                                 'wait'}
            self.assertTrue(is_key_exists)
            self.assertEqual(expecteds[i], actual[i])

        response = self.client.get('/multiple?room=15階&room=20階')
        response_json = response.json()

        expected = 204
        actual = response.status_code
        self.assertEqual(expected, actual)

        expected = 'room not found'
        actual = response_json['detail'][0]['msg']
        self.assertEqual(expected, actual)

        response = self.client.get('/multiple?roo')
        response_json = response.json()

        expected = 422
        actual = response.status_code
        self.assertEqual(expected, actual)

        expected = 'field required'
        actual = response_json['detail'][0]['msg']
        self.assertEqual(expected, actual)

        expecteds = [{
            'room': '5階',
            'use': 5,
            'limit': 5,
            'is_limit': False,
            'wait': ''
        }, {
            'room': '11階',
            'use': '',
            'limit': 5,
            'is_limit': '',
            'wait': ''
        }]

        response = self.client.get('/multiple?'
                                   f'room={target_rooms[0]}'
                                   f'&room=ff階'
                                   f'&room={target_rooms[2]}')
        response_json = response.json()

        actual = response_json['room_status']

        for i in range(len(expecteds)):
            self.assertEqual(expecteds[i], actual[i])

        self.remove_csv(csv_file_name)
        self.remove_toml()

    def test_get_frontend_path(self):
        """get_frontend_pathのテスト"""
        expect = 'web'
        actual = str(get_frontend_path('web'))
        self.assertEqual(expect, actual)

        path = 'raise_test'
        with self.assertRaises(FileNotFoundError) as e:
            get_frontend_path(path)

        err_message = f'"{path}" directory not found. ' \
                      'Unable to display web screen'
        actual = str(e.exception)
        self.assertEqual(err_message, actual)

        # _MEIPASSが存在する場合のテスト
        sys._MEIPASS = '.'
        expect = 'web'
        actual = str(get_frontend_path('web'))
        self.assertEqual(expect, actual)

        path = 'raise_test'
        with self.assertRaises(FileNotFoundError) as e:
            get_frontend_path(path)

        actual = str(e.exception)
        self.assertEqual(err_message, actual)

    def test_read_toml(self):
        """read_tomlのテスト"""
        toml_data = {
            'detect_field_num': 4,
            'area':
            [
              {'場所': '5階', '利用者': 'path/to/csv1', '待ち人数': 'path/to/csv1-2',
               '定員上限': 5},
              {'場所': '9階', '利用者': 'path/to/csv2', '待ち人数': '', '定員上限': 7},
              {'場所': '11階', '利用者': '', '待ち人数': 'path/to/csv3', '定員上限': 5}
            ]}
        self.create_toml(toml_data)

        actual = read_toml()
        self.assertEqual(toml_data, actual)
        self.remove_toml()

        with self.assertRaises(FileNotFoundError) as e:
            read_toml()

        err_message = 'setting\\setting.tomlが見つかりませんでした'
        actual = str(e.exception)
        self.assertEqual(err_message, actual)

    def test_redict_view(self):
        """select apiのテスト"""
        toml_data = {
            'detect_field_num': 4,
            'area':
            [
              {'場所': '5階', '利用者': 'path/to/csv1', '待ち人数': 'path/to/csv1-2',
               '定員上限': 5},
              {'場所': '9階', '利用者': 'path/to/csv2', '待ち人数': '', '定員上限': 7},
              {'場所': '11階', '利用者': '', '待ち人数': 'path/to/csv3', '定員上限': 5}
            ]}
        self.create_toml(toml_data)

        urls = [
            '/select',
            '/select?room=5階',
            '/select?room=9階',
            '/select?room=11階',
            '/select?room=5階&room=9階',
            '/select?room=5階&room=11階',
            '/select?room=9階&room=11階',
            '/select?room=11階&room=9階',
            '/select?room=5階&room=9階',
            '/select?room=5階&room=9階&room=11階',
        ]

        expecteds = [
            'web/index.html',
            'web/index_5階.html',
            'web/index_9階.html',
            'web/index_11階.html',
            'web/index_5階_9階.html',
            'web/index_5階_11階.html',
            'web/index_9階_11階.html',
            'web/index_9階_11階.html',
            'web/index_5階_9階.html',
            'web/index_5階_9階_11階.html',
        ]

        for url, expected in zip(urls, expecteds):
            response = self.client.get(url)
            actual = urllib.parse.unquote(str(response.url))
            self.assertTrue(expected in actual)

        self.remove_toml()
