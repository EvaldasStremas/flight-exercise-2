'''
Run tests with: python -m unittest flights_tests
Run 2nd class: python -m unittest flights_tests.FlightsTestCase2
https://docs.python.org/3/library/unittest.html 
'''

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

    def test_init(self):
        self.assertEqual(len(self.itemUnderTest._flights), 11)
   
    def test_get_ids_to_city(self):
        # First task final resul test
        expected_result = ['000', '004']
        results = self.itemUnderTest.get_ids_to_city('City X')
        self.assertEqual(results, expected_result)

    def test_get_availables_to_cities(self):
        expected_result = ['City Y', 'City E']

        results = self.itemUnderTest.get_availables_to_cities('City X')
        self.assertEqual(results, expected_result)

    # def test_get_same_list_values(self):
    #     # Second task final resul test

    #     for flights in self.itemUnderTest._flights:
    #         print('flight price: ', flights.price)
    #         print()

    def test_get_flight_list(self):
        results = self.itemUnderTest.get_flight_list()

        for flight in results:
            # print(flight)

            # test_value2 = str(flight[1]).isalpha()
            # print(test_value2)
            # self.assertEqual(True, test_value)

            test_value = str(flight[2]).isnumeric()
            # print(test_value)
            self.assertEqual(True, test_value)


    def test_correctly_city_name(self):
        # Check all list 
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


    # def test_get_availables_to_cities(self):
    #     # Second task final resul test
    #     # expected_result = ['City Y', 'City E']

    #     results = self.itemUnderTest.get_availables_to_cities('City X')



    #     self.assertEqual(results, expected_result)


    # def test_check_result_cities(self):
    #     # 
    #     expected_result = ['City Y', 'City E']

    #     results = self.itemUnderTest.lowest_price_flight
    #     print(results)

    #     # self.assertEqual(results, expected_result)


if __name__ == '__main__':
    # os.system('cls')
    unittest.main()