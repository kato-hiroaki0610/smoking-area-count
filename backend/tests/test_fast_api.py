import unittest

from fast_api import app
from starlette.testclient import TestClient


class TestFastAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_main(self):
        response = self.client.get('/')

        expected = 200
        actual = response.status_code
        self.assertEqual(expected, actual)

        expecteds = [{
            '階数': '5階',
            '利用者数': 2,
            '上限超え': False,
            '待ち人数': 10
        }, {
            '階数': '9階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': ''
        }, {
            '階数': '11階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': 8
        }, {
            '階数': '12階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': 10
        }]
        response_json = response.json()

        expected = dict
        actual = type(response_json)

        expected = len(expecteds[0])
        actual = response_json['room_status']

        self.assertEqual(expected, len(actual))

        for i in range(len(expecteds)):
            self.assertEqual(expecteds[i], actual[i])

    def test_specified_room(self):
        target_room = '5階'
        response = self.client.get(f'/specified?room={target_room}')

        expected = 200
        actual = response.status_code
        self.assertEqual(expected, actual)

        expecteds = [{
            '階数': '5階',
            '利用者数': 2,
            '上限超え': False,
            '待ち人数': 10
        }, {
            '階数': '9階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': ''
        }, {
            '階数': '11階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': 8
        }, {
            '階数': '12階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': 10
        }]
        response_json = response.json()

        expected = dict
        actual = type(response_json)

        expected = len(expecteds[0])
        actual = response_json['specified_room_status']

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            if expecteds[i]['階数'] == target_room:
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

    def test_multiple_room(self):
        target_rooms = ['5階', '9階', '12階']
        response = self.client.get(
            f'/multiple?rooms={target_rooms[0]}&rooms={target_rooms[2]}')

        expected = 200
        actual = response.status_code
        self.assertEqual(expected, actual)

        expecteds = [{
            '階数': '5階',
            '利用者数': 2,
            '上限超え': False,
            '待ち人数': 10
        }, {
            '階数': '12階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': 10
        }]
        response_json = response.json()

        expected = dict
        actual = type(response_json)

        expected = len(expecteds[0])
        actual = response_json['multiple_room_status']

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            self.assertEqual(expecteds[i], actual[i])

        response = self.client.get('/multiple?'
                                   f'rooms={target_rooms[0]}'
                                   f'&rooms={target_rooms[1]}'
                                   f'&rooms={target_rooms[2]}')
        response_json = response.json()

        expecteds = [{
            '階数': '5階',
            '利用者数': 2,
            '上限超え': False,
            '待ち人数': 10
        }, {
            '階数': '9階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': ''
        }, {
            '階数': '12階',
            '利用者数': '',
            '上限超え': '',
            '待ち人数': 10
        }]

        expected = len(expecteds[0])
        actual = response_json['multiple_room_status']

        self.assertEqual(expected, len(actual[0]))

        for i in range(len(expecteds)):
            self.assertEqual(expecteds[i], actual[i])

        response = self.client.get('/multiple?rooms=ff')
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
