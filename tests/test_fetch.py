import unittest
import types
from app.fetch import fetch_data, data_for_display


class TestFetchMethods(unittest.TestCase):
    def test_fetch(self):
        res = fetch_data()
        self.assertIsInstance(res, types.GeneratorType)

    def test_dict(self):
        res = fetch_data()
        for item in res:
            data = data_for_display(item)
            print(data)
            self.assertEqual(len(data.keys()), 8)


if __name__ == "__main__":
    unittest.main()
