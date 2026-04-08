import unittest
from unittest.mock import patch

from src.notebook import get_dollar_info

class TestUserService(unittest.TestCase):

    @patch("src.notebook.requests.get")
    def test_get_user_name(self, mock_get):
        # 1. Mock response object
        mock_response = mock_get.return_value
        mock_response.json.return_value = {"venta": 18.5}

        # 2. Call function
        result = get_dollar_info()

        # 3. Assertions
        self.assertEqual(result, 18.5)
        mock_get.assert_called_once_with("https://mx.dolarapi.com/v1/cotizaciones/usd")


if __name__ == "__main__":
    unittest.main()