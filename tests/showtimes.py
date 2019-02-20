import unittest
import requests

class TestShowTimesService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5002/showtimes"

    def test_showtimes_records(self):
        """ Test /showtimes/<date> for all known showtimes"""
        for date, expected in GOOD_RESPONSES.items():
            reply = requests.get("{}/{}".format(self.url, date))
            actual_reply = reply.json()

            self.assertEqual(len(actual_reply), len(expected),
                             "Got {} showtimes but expected {}".format(
                                 len(actual_reply), len(expected)
                             ))

            # Use set because the order doesn't matter
            self.assertEqual(set(actual_reply), set(expected),
                             "Got {} but expected {}".format(
                                 actual_reply, expected))


    def test_not_found(self):
        """ Test /showtimes/<date> for non-existent dates"""
        invalid_date = 31122007
        actual_reply = requests.get("{}/{}".format(self.url, invalid_date))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))

GOOD_RESPONSES = {
  "08022017": [
    "id1",
    "id2",
    "id7"
  ],
  "09022017": [
    "id4",
    "id5",
    "id7",
    "id2"
  ],
  "10022017": [
    "id2",
    "id3",
    "id7",
    "id6"
  ],
  "11022017": [
    "id1",
    "id7"
  ],
  "12022017": [
    "id3",
    "id2",
    "id5"
  ],
  "13022017": [
    "id3",
    "id2",
    "id5",
    "id6",
    "id7"
  ]
}