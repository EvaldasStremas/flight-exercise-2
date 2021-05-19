'''
Run tests with: python -m unittest flights_tests
Run 2nd class: python -m unittest flights_tests.FlightsTestCase2
https://docs.python.org/3/library/unittest.html 
'''

from itertools import combinations
import unittest
import flights
# import os

class FlightsTestCase(unittest.TestCase):

    def setUp(self):
        self.itemUnderTest = flights.FlightTable(flights.available_flights)
        
    def tearDown(self):
        del self.itemUnderTest 
        self.itemUnderTest = None

    ####################################################################

    def test_input_flight_list_length(self):
        # Check input list values for expected list length
        self.assertEqual(len(self.itemUnderTest._flights), 11)
   
    def test_input_flight_list_type(self):
        # Check input list type
        self.assertEqual(type(self.itemUnderTest._flights), list)

    def test_get_ids_to_city(self):
        # Check 1st task function for expected result.
        expected_result = ['000', '004']
        results = self.itemUnderTest.get_ids_to_city('City X')
        self.assertEqual(results, expected_result)

    def test_get_availables_to_cities(self):
        # Check 2nd task function for expected result.
        expected_result = ['City Y', 'City E']

        results = self.itemUnderTest.get_availables_to_cities('City X')
        self.assertEqual(results, expected_result)

    def test_correctly_city_name(self):
        # Check input list cities names in correct(City X) format.
        words = []
        result = []

        results = self.itemUnderTest.get_flight_list()

        for city in results:
            for i in range(0, 2):
                words.append(list(city[i]))
        
        for word in words:
            # print(word)
            if (word[0].isupper() == True and word[1].islower() == True and 
            word[2].islower() == True and word[3].islower() == True and 
            word[4].isspace() == True and word[5].isupper()) == True:
                result.append(True)
            else:
                result.append(False)

            # print(word[0].isupper())
            # print(word[1].islower())
            # print(word[2].islower())
            # print(word[3].islower())
            # print(word[4].isspace())
            # print(word[5].isupper())
            # print()

        for test_state in result:
            # print(test_state)
            self.assertEqual(True, test_state)

    def test_combination_function(self):
        flight_list = self.itemUnderTest.get_flight_list()
        # print(flight_list)
        # for flight in flight_list:
        #     print(flight)

        combinations = self.itemUnderTest.get_needed_combinations_list(3, flight_list)
        
        for flight in combinations:
            print(flight)

    # def test_get_flight_list(self):
    #     results = self.itemUnderTest.get_flight_list()

    #     for flight in results:
    #         print(flight)

    #         # test_value2 = str(flight[1]).isalpha()
    #         # print(test_value2)
    #         # self.assertEqual(True, test_value)

    #         test_value = str(flight[2]).isnumeric()
    #         # print(test_value)
    #         self.assertEqual(True, test_value)


if __name__ == '__main__':
    # os.system('cls')
    unittest.main()