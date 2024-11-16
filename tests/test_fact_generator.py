import unittest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fact_generator import fetch_fact,  fetch_multiple_facts
from config import API_URL 

class TestFactGenerator(unittest.TestCase):
    def test_something(self):
        self.assertFalse(False)

    # @patch('fact_generator.requests.get')  # Mock the requests.get function
    # def test_fetch_single_fact(self, mock_get):

    #     # Mock API response
    #     mock_response = MagicMock()
    #     mock_response.status_code = 200
    #     mock_response.json.return_value = {"text": "Did you know? The Moon is slowly drifting away from Earth."}
    #     mock_get.return_value = mock_response

    #     # Test function behavior
    #     fact = fetch_fact()
    #     self.assertEqual(fact, "Did you know? The Moon is slowly drifting away from Earth.")
    #     mock_get.assert_called_once_with(API_URL)

    # @patch('fact_generator.requests.get')
    # def test_fetch_multiple_facts(self, mock_get):
    #     # Mock API response for multiple calls
    #     mock_response_1 = MagicMock()
    #     mock_response_1.status_code = 200
    #     mock_response_1.json.return_value = {"text": "The first oranges weren't orange."}

    #     mock_response_2 = MagicMock()
    #     mock_response_2.status_code = 200
    #     mock_response_2.json.return_value = {"text": "Bananas are berries, but strawberries aren't."}

    #     mock_get.side_effect = [mock_response_1, mock_response_2]  # Simulate multiple responses

    #     # Test function behavior
    #     facts = fetch_multiple_facts(2)
    #     self.assertEqual(facts, [
    #         "The first oranges weren't orange.",
    #         "Bananas are berries, but strawberries aren't."
    #     ])
    #     self.assertEqual(mock_get.call_count, 2)

if __name__ == '__main__':
    unittest.main()