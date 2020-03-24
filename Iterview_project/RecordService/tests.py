from django.test import TestCase

# Create your tests here.

import requests
import unittest


class UserTest(unittest.TestCase):

    def setUp(self):
        self.base_url='http://127.0.0.1:8000/'

    def test_get_user(self):
        r = requests.get(self.base_url+'get_scores?client_id=test2')
        resulet = r.json()

        self.assertEqual(resulet["code"],  0)


if __name__ == '__main__':
    pass