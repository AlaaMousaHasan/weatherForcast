import unittest
from fetch_data import FetchData
from unittest.mock import patch

class TestFetchData(unittest.TestCase):
    @patch('fetch_data.requests.get')  
    def test_fetch_weather_success(self, mock_get):
        mock_get.return_value.status_code = 200;
        mock_get.return_value.json.return_value = {'location': {'name': 'Berlin'},'forecast': {'forecastday': [{'date': '2024-01-01', 'day': {}}]}
        }
        fetcher = FetchData(api_key='SetYourAPIKeyHere');
        result = fetcher.parse('Berlin');
        # Assertions
        self.assertEqual(result['location']['name'], 'Berlin')  ;

if __name__ == '__main__':
    unittest.main()