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

    def test_multiple_room(self):
        response = self.client.get('/multiple?rooms=5階&rooms=9階')
        pass
