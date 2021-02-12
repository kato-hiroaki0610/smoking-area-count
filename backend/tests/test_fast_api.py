import unittest

from fast_api import app
from starlette.testclient import TestClient


class TestFastAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_main(self):
        response = self.client.get('/')

        print(response)
