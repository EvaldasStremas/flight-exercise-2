'''
Run tests with: python -m unittest flights_tests
https://docs.python.org/3/library/unittest.html 
'''

import unittest
import flights
import os

class FlightsTestCase(unittest.TestCase):

    def setUp(self):
        self.itemUnderTest = flights.FlightTable(flights.available_flights)

    def test_init(self):
        self.assertEqual(len(self.itemUnderTest._flights), 11)

if __name__ == '__main__':
    os.system('cls')
    unittest.main()