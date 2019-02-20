import unittest
import requests

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5000/users"

    def test_user_records(self):
        for username, expected in GOOD_RESPONSES.items():
            actual_reply = requests.get("{}/{}".format(self.url, username))
            actual_reply = actual_reply.json()

            self.assertEqual(actual_reply, expected,
                             "Got {} user record but expected {}".format(
                                 actual_reply, expected
                             ))

    def test_user_not_found(self):
        """ Test /users/<username> for non-existent user"""
        invalid_user = "artem_karaulov"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_user))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))

GOOD_RESPONSES = {
  "egor_schukin" : {
    "id": "egor_schukin",
    "name": "Egor Schukin",
    "last_active": 110
  },
  "anna_filatova" : {
    "id": "anna_filatova",
    "name": "Anna Filatova",
    "last_active": 0
  },
  "george_bespalov" : {
    "id": "george_bespalov",
    "name": "George Bespalov",
    "last_active": 425
  },
  "larisa_burova" : {
    "id": "larisa_burova",
    "name": "Larisa Burova",
    "last_active": 625
  },
  "alla_drozdova" : {
    "id": "alla_drozdova",
    "name": "Alla Drozdova",
    "last_active": 325
  },
  "yury_osipov" : {
    "id": "yury_osipov",
    "name": "Yury Osipov",
    "last_active": 225
  },
  "ekaterina_zinovyeva" : {
    "id": "ekaterina_zinovyeva",
    "name": "Ekaterina Zinovyeva",
    "last_active": 202
  }
}