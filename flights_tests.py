'''
Run tests with: python -m unittest flights_tests
Run 2nd class: python -m unittest flights_tests.FlightsTestCase2
https://docs.python.org/3/library/unittest.html 
https://dev.to/karn/building-a-simple-state-machine-in-python
'''
#test

import unittest
import flights

DEBUG = False

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
        # Check input flight list type, is it 'list'
        self.assertEqual(type(self.itemUnderTest._flights), list) #testuoti funkcija


    def test_get_ids_to_city(self):
        # Check 1st task function expected result.
        expected_result = ['000', '004']
        results = self.itemUnderTest.get_ids_to_city('City X')
        self.assertEqual(results, expected_result)

        expected_result = ['003']
        results = self.itemUnderTest.get_ids_to_city('City Y')
        self.assertEqual(results, expected_result)
        
        expected_result = ['001']
        results = self.itemUnderTest.get_ids_to_city('City Z')
        self.assertEqual(results, expected_result)

        expected_result = ['005', '007']
        results = self.itemUnderTest.get_ids_to_city('City W')
        self.assertEqual(results, expected_result)

        expected_result = ['010']
        results = self.itemUnderTest.get_ids_to_city('City M')
        self.assertEqual(results, expected_result)

        expected_result = ['002', '006', '008', '009']
        results = self.itemUnderTest.get_ids_to_city('City T')
        self.assertEqual(results, expected_result)

        expected_result = []
        results = self.itemUnderTest.get_ids_to_city('City P')
        self.assertEqual(results, expected_result)


    def test_get_availables_to_cities(self):
        # Check 2nd task function expected result
        expected_result = ['City Y', 'City E']
        results = self.itemUnderTest.get_availables_to_cities('City X')
        self.assertEqual(results, expected_result)

        expected_result = ['City Z']
        results = self.itemUnderTest.get_availables_to_cities('City Y')
        self.assertEqual(results, expected_result)

        expected_result = ['City X']
        results = self.itemUnderTest.get_availables_to_cities('City Z')
        self.assertEqual(results, expected_result)
        
        expected_result = ['City Y', 'City Z', 'City Z', 'City W']
        results = self.itemUnderTest.get_availables_to_cities('City T')
        self.assertEqual(results, expected_result)

        expected_result = ['City Y']
        results = self.itemUnderTest.get_availables_to_cities('City M')
        self.assertEqual(results, expected_result)

        expected_result = ['City T', 'City X']
        results = self.itemUnderTest.get_availables_to_cities('City W')
        self.assertEqual(results, expected_result)


    def test_correctly_city_name(self):
        # Check input flight list cities names in correct(City X) format.
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

            
            self.my_print(word[0].isupper())
            self.my_print(word[1].islower())
            self.my_print(word[2].islower())
            self.my_print(word[3].islower())
            self.my_print(word[4].isspace())
            self.my_print(word[5].isupper())
            self.my_print()


        for test_state in result:
            # print(test_state)
            self.assertEqual(True, test_state)


    def test_combination_function(self):
        # Check all comibnations list types is it 'list'

        flight_list = self.itemUnderTest.get_flight_list()

        depth = 4 #Testing depth level (0..depth)

        for iteration in range(depth+1):

            self.my_print(iteration)
            combinations = self.itemUnderTest.get_needed_combinations_list(iteration, flight_list)
            
            for flight in combinations:
                result = []
                result.append(flight)
                result.append(type(flight))

                if type(flight) == list:
                    result.append(True)
                else:
                    result.append(False)

                
                self.my_print(result[2])
                self.my_print(flight)

                self.assertEqual(True, result[2])


    def my_print(self, msg='***'):
        if DEBUG == True:
            print(msg)

    ####################################################################

if __name__ == '__main__':
    unittest.main()