import unittest
import requests


class TestApp(unittest.TestCase):
    def test_index(self):
        r = requests.get("https://tfl-bustimes.herokuapp.com")
        self.assertTrue(r.ok)

    def test_json(self):
        r = requests.get("https://tfl-bustimes.herokuapp.com/raw_json.html")
        self.assertTrue(r.ok)

    def test_history(self):
        r = requests.get("https://tfl-bustimes.herokuapp.com/history.html")
        self.assertTrue(r.ok)


if __name__ == "__main__":
    unittest.main()
