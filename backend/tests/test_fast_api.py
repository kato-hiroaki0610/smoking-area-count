import csv
import pathlib
import unittest

import toml
from fast_api import app
from starlette.testclient import TestClient

SETTING_DIR = 'setting'
SETTING_FILE = 'setting.toml'


class TestFastAPI(unittest.TestCase):
    def create_toml(self, csv_file):
        """setting用のtomlファイルを作成する"""
        toml_data = {
            'detect_field_num': 4,
            'area':
            [
              {'場所': '5階', '利用者': csv_file, '待ち人数': '', '定員上限': 5},
              {'場所': '9階', '利用者': '', '待ち人数': '', '定員上限': 7},
              {'場所': '11階', '利用者': '', '待ち人数': '', '定員上限': 5}
            ]}

        pathlib.Path(SETTING_DIR).mkdir()
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).touch()

        with open(SETTING_DIR + '\\' + SETTING_FILE, 'wt', 
                  encoding='utf8') as fp:
            toml.dump(toml_data, fp)

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
        self.client = TestClient(app)

    def remove_toml(self):
        pathlib.Path(SETTING_DIR + '\\' + SETTING_FILE).unlink()
        pathlib.Path(SETTING_DIR).rmdir()

    def test_main(self):
        csv_file_name = 'tmp.csv'
        self.create_toml(csv_file_name)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        csv_file_name = 'tmp.csv'
        self.csv_create(csv_data, csv_file_name)

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

        expected = len(expecteds[0])
        actual = response_json['room_status']
        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            if(expecteds[i]['room'] == '12階'):
                continue

            self.assertEqual(expecteds[i], actual[i])

        self.remove_csv(csv_file_name)
        self.remove_toml()

    def test_specified_room(self):
        csv_file_name = 'tmp.csv'
        self.create_toml(csv_file_name)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        csv_file_name = 'tmp.csv'
        self.csv_create(csv_data, csv_file_name)

        target_room = '5階'
        response = self.client.get(f'/specified?room={target_room}')

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
            'limit': '',
            'is_limit': '',
            'wait': 10
        }]
        response_json = response.json()
        expected = dict
        actual = type(response_json)

        expected = len(expecteds[0])
        actual = response_json['room_status']

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            if expecteds[i]['room'] == target_room:
                self.assertEqual(expecteds[i], actual[i])
                break

        response = self.client.get('/specified?room=ff')
        response_json = response.json()

        expected = 204
        actual = response.status_code
        self.assertEqual(expected, actual)

        expected = 'room not found'
        actual = response_json['detail'][0]['msg']
        self.assertEqual(expected, actual)

        response = self.client.get('/specified?roo')
        response_json = response.json()

        expected = 422
        actual = response.status_code
        self.assertEqual(expected, actual)

        expected = 'field required'
        actual = response_json['detail'][0]['msg']
        self.assertEqual(expected, actual)

        self.remove_csv(csv_file_name)
        self.remove_toml()

    def test_multiple_room(self):
        csv_file_name = 'tmp.csv'
        self.create_toml(csv_file_name)
        csv_data = [['video_source', 'ymd', 'hms', 'fff', '5'],
                    ['video_source', 'ymd', 'hms', 'fff', '6'],
                    ['video_source', 'ymd', 'hms', 'fff', '5']]
        csv_file_name = 'tmp.csv'
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

        expected = len(expecteds[0])
        actual = response_json['room_status']

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
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

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            self.assertEqual(expecteds[i], actual[i])

        response = self.client.get('/multiple?room=ff')
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
