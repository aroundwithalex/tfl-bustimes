import unittest
from fetch import fetch_data, data_for_display


class TestFetchMethods(unittest.TestCase):
    def test_fetch(self):
        """
        Tests TFL API for fetching data

        Args:
            Self
        
        Returns:
            None
        
        Raises:
            None
        """
        res = fetch_data()
        self.assertIsInstance(res, list)

    def test_dict(self):
        """
        Tests formatting of response data from TFL API

        Args:
            Self
        
        Returns:
            None
        
        Raises:
            None
        """
        res = fetch_data()
        data = data_for_display(res)
        self.assertIsNotNone(data)


if __name__ == "__main__":
    unittest.main()
