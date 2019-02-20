import unittest
import requests


class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5003/bookings"

    def test_booking_records(self):
        """ Test /bookings/<username> for all known bookings"""
        for date, expected in GOOD_RESPONSES.items():
            reply = requests.get("{}/{}".format(self.url, date))
            actual_reply = reply.json()

            self.assertEqual(len(actual_reply), len(expected),
                             "Got {} booking but expected {}".format(
                                 len(actual_reply), len(expected)
                             ))

            self.assertEqual(set(actual_reply), set(expected),
                             "Got {} but expected {}".format(
                                 actual_reply, expected))

    def test_not_found(self):
        """ Test /showtimes/<date> for non-existent users"""
        invalid_user = "artem_karaulov"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_user))
        self.assertEqual(actual_reply.status_code, 404,
                         "Got {} but expected 404".format(
                             actual_reply.status_code))
							 
    def test_hello(self):
        actual_reply = requests.get("http://127.0.0.1:5003")
        self.assertEqual(200,actual_reply.status_code)
	

GOOD_RESPONSES = {
  "egor_schukin": {
    "09022019": [
      "id4"
    ]
  },
  "yury_osipov": {
    "09022019": [
      "id4"
    ],
    "10022019": [
      "id6"
    ]
  },
  "larisa_burova": {
    "09022019": [
      "id5",
      "id4"
    ],
    "13022019": [
      "id2",
      "id6"
    ]
  }
}