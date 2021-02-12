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
        actual = response.json()

        for i in range(len(expecteds)):
            self.assertEqual(expecteds[i], actual['room_status'][i])
