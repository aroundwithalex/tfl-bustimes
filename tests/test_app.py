import unittest
import requests


class TestApp(unittest.TestCase):
    def test_index(self):
        """
        Tests that index.html up and running

        Args:
            None

        Returns:
            None
        
        Raises:
            None
        """
        r = requests.get("https://tfl-bustimes.herokuapp.com")
        self.assertTrue(r.ok)

    def test_json(self):
        """
        Tests to ensure that raw_json.html up and running

        Args:
            Self
        
        Returns:
            None
        
        Raises:
            None
        """
        r = requests.get("https://tfl-bustimes.herokuapp.com/raw_json.html")
        self.assertTrue(r.ok)

    def test_history(self):
        """
        Tests to ensure that history.html up and running

        Args:
            Self
        
        Returns:
            None
        
        Raises:
            None
        """
        r = requests.get("https://tfl-bustimes.herokuapp.com/history.html")
        self.assertTrue(r.ok)
    
    def test_api(self):
        """
        Tests API to ensure it is up and running

        Args:
            Self
        
        Returns:
            None

        Raises:
            None
        """
        r = requests.get('https://tfl-bustimes.herokuapp.com/api/history')
        self.assertTrue(r.ok)


if __name__ == "__main__":
    unittest.main()
