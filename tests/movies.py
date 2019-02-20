import unittest
import requests

class TestMoviesService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5001/movies"

    def test_all_movie_records(self):
        """ Test /movies/<movieid> for all known movies"""
        for movieid, expected in GOOD_RESPONSES.items():
            expected['uri'] = "/movies/{}".format(movieid)
            reply = requests.get("{}/{}".format(self.url, movieid))
            actual_reply = reply.json()
            self.assertEqual( set(actual_reply.items()), set(expected.items()))

    def test_not_found(self):
        invalid_movie_id = "b18f"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_movie_id))
        self.assertEqual(actual_reply.status_code, 404,
                    "Got {} but expected 404".format(
                        actual_reply.status_code))






GOOD_RESPONSES = {
  "id1": {
    "title": "Bohemian Rhapsody",
    "rating": 8.2,
    "director": "Bryan Singer",
    "id": "id1"
  },
  "id2": {
    "title": "Glass",
    "rating": 7.0,
    "director": "M. Night Shyamalan",
    "id": "id2"
  },
  "id3": {
    "title": "The House That Jack Built",
    "rating": 7.0,
    "director": "Lars von Trier",
    "id": "id3"
  },
  "id4": {
    "title": "Green Book",
    "rating": 8.3,
    "director": "Peter Farrelly",
    "id": "id4"
  },
  "id5": {
    "title": "T-34",
    "rating": 6.2,
    "director": "Aleksey Sidorov",
    "id": "id5"
  },
  "id6": {
    "title": "Spider-Man: Into the Spider-Verse",
    "rating": 8.7,
    "director": " Bob Persichetti",
    "id": "id6"
  },
  "id7": {
    "title": "The Grinch",
    "rating": 6.3,
    "director": "Yarrow Cheney",
    "id": "id7"
  }
}