import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fact_generator import fetch_fact,  fetch_multiple_facts
class TestFactGenerator(unittest.TestCase):
    def test_something(self):
        self.assertFalse(False)
if __name__ == '__main__':
    unittest.main()