from itertools import permutations
from operator import itemgetter
import os

available_flights = [
    {"from": "City Y", "to": "City X", "price": 60, "flight id": "000"},
    {"from": "City X", "to": "City Z", "price": 78, "flight id": "001"},
    {"from": "City Y", "to": "City T", "price": 91, "flight id": "002"},
    {"from": "City Z", "to": "City Y", "price": 58, "flight id": "003"},
    {"from": "City E", "to": "City X", "price": 100, "flight id": "004"},
    {"from": "City T", "to": "City W", "price": 49, "flight id": "005"},
    {"from": "City Z", "to": "City T", "price": 45, "flight id": "006"},
    {"from": "City X", "to": "City W", "price": 205, "flight id": "007"},
    {"from": "City Z", "to": "City T", "price": 56, "flight id": "008"},
    {"from": "City W", "to": "City T", "price": 40, "flight id": "009"},
    {"from": "City Y", "to": "City M", "price": 50, "flight id": "010"},
];

class Flight:
   
    def __init__(self):
        pass

    def addFields(self, data):
        self.fromCity = data["from"]
        self.toCity = data["to"]
        self.price = data["price"]
        self.id = data["flight id"]

    def __str__(self):
        return "{} {} {} {}".format(self.fromCity, 
        self.toCity,
        self.price,
        self.id
        )

class FlightTable:

    _accessCount = 0
    _flights = []
    flights_list = []

    def __init__(self, flights):
        for fl in flights:
            fli = Flight()
            fli.addFields(fl)
            self._flights.append(fli)

# Get all flight ids for flights that are going to 'city t'
    def get_ids_to_city(self, city):
        ids_list = []

        for flight in self._flights:
            if flight.toCity == city:
                ids_list.append(flight.id)
        
        return ids_list

# Get all available destinations for every city mentioned in the input
    def get_availables_to_cities(self, input_city):
        available_cities = []

        for flight in self._flights:

            if input_city == flight.toCity:
                available_cities.append(flight.fromCity)

        return available_cities

# Get cheapest roundtrip from 'city x' to 'city w'
    def get_cheapest_roundtrip(self):
        price_list = []
        target_destinations = []

        for flight in self._flights:
            if flight.fromCity == 'City X' and flight.toCity == 'City W':
                target_destinations.append(str(flight))       
                price_list.append(flight.price)
                price_list.sort()
                lowest_price = price_list[0]

                for flight in self._flights:
                    if flight.price == lowest_price:
                        lowest_price_line = flight

        return lowest_price_line

    def get_flight_list(self):
        checkList = []
        endList = []

        for flight in self._flights:
            checkList = []
            checkList.append(flight.fromCity)
            checkList.append(flight.toCity)
            checkList.append(flight.price)
            endList.append(checkList)

        return endList

    def get_needed_combinations_list(self, DEPTH, array):
        perm = permutations(array, DEPTH) 
        combination_list = []

        for i in list(perm): 

            failed=False
            for j in range(0,len(i)-1): #netikriname paskutinio elemento
                if i[j][1] != i[j+1][0]:
                    failed = True
            if failed == False:

                i = list(i)
                # print(i)
                combination_list.append(i)
        
        return combination_list

    def get_sorted_flight_price_list(self, DEPTH, combination_list):
        price_list = []

        for flight in combination_list:
            flight_price = 0

            for price in flight:
                flight_price = flight_price + price[2]

            flight.append(flight_price)
            price_list.append(flight)

        sorted_list = sorted(price_list, key=itemgetter(DEPTH))

        return sorted_list

    def get_required_cities_list(self, input_from_city, input_to_city, flight_list):
        result_list = []

        for flight in flight_list:
            if flight[0][0] == input_from_city and flight[len(flight)-2][1] == input_to_city:
                result_list.append(flight)

        return result_list

    def get_cities_result_list(self, DEPTH):
        # Get all available combinations by flight list
        # Sort 

        # print('Gautos kombinacijos')
        combinations_list = self.get_needed_combinations_list(DEPTH, flight_list)
        # flighttable.list_print(combinations_list)
        # print()

        # print('Isrikiuotas listas')
        sorted_flight_price_list = flighttable.get_sorted_flight_price_list(DEPTH, combinations_list)
        # flighttable.list_print(sorted_flight_price_list)
        # print()

        # print('Isfiltruoti is x i w miesta')
        required_cities_list = flighttable.get_required_cities_list(FROM_CITY, TO_CITY, sorted_flight_price_list)
        # flighttable.list_print(required_cities_list)
        # print()

        return required_cities_list

    def list_print(self, list):
        #Print list values
            for flight in list:
                print(flight)

    def get_lowest_price_flight(self, flight_list):
        #Geting lowest price flight from flight list
        u = []

        for i in flight_list:
            o = len(i)
            # print(i[o-1])
            u.append(i[o-1])

        u.sort()
        # print(u[0])

        for y in flight_list:
            t = len(y)
            if u[0] == y[t-1]:
                result = y

        return result

    def get_filtered(self):
        #Get all available flight values by depth
        for depth_num in range(1, DEPTH+1):
            rez = flighttable.get_cities_result_list(depth_num)
            # print(rez)

            for flight in rez:
                result.append(flight)

        return result

DEPTH = 3
FROM_CITY = 'City X'
TO_CITY = 'City W'
result = []

os.system('cls')
flighttable = FlightTable(available_flights)

print('Pirma uzduotis:')
print(flighttable.get_ids_to_city('City X'))
print()

print('Antra uzduotis:')
print(flighttable.get_availables_to_cities('City X'))
print()

print('Trecia uzduotis:')
print()
# print(flighttable.get_cheapest_roundtrip())

print('Galimi skrydziai')
flight_list = flighttable.get_flight_list()
flighttable.list_print(flight_list)
print()

print('Isfiltruoti is x i w miesta')
result = flighttable.get_filtered()
flighttable.list_print(result)
print()

lowest_price_flight = flighttable.get_lowest_price_flight(result)
print(lowest_price_flight)