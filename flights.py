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

    # _accessCount = 0
    # _flights = []

    def __init__(self, flights):
        # print('executing init')
        # print(len(self._flights))

        self._flights = []

        for fl in flights:
            fli = Flight()
            fli.addFields(fl)
            self._flights.append(fli)


    # def __del__(self):
    #     print("Destructor called")

    def get_ids_to_city(self, city):
        # Get all flight ids for flights that are going to 'city t'
        ids_list = []

        for flight in self._flights:
            # print('\n')
            # print(flight.id)
            if flight.toCity == city:
                ids_list.append(flight.id)
                # print(flight.id)
        
        return ids_list


    def get_availables_to_cities(self, input_city):
        # Get all available destinations for every city mentioned in the input
        available_cities = []

        for flight in self._flights:

            if input_city == flight.toCity:
                available_cities.append(flight.fromCity)

        return available_cities


    def get_cheapest_roundtrip(self):
        # Get cheapest roundtrip from 'city x' to 'city w'
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
            # print(flight.price)
            endList.append(checkList)

        return endList


    def get_needed_combinations_list(self, depth, array):
        perm = permutations(array, depth) 
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


    def get_sorted_flight_price_list(self, depth, combination_list):
        price_list = []

        for flight in combination_list:
            flight_price = 0

            for price in flight:
                flight_price = flight_price + price[2]

            flight.append(flight_price)
            price_list.append(flight)

        sorted_list = sorted(price_list, key=itemgetter(depth))

        return sorted_list


    def get_required_cities_list(self, input_from_city, input_to_city, flight_list):
        result_list = []

        for flight in flight_list:
            if flight[0][0] == input_from_city and flight[len(flight)-2][1] == input_to_city:
                result_list.append(flight)

        return result_list


    def get_cities_result_list(self, depth, flight_list, from_city, to_city):
        # Get all available combinations by flight list

        # print('Gautos kombinacijos')
        combinations_list = self.get_needed_combinations_list(depth, flight_list)
        # flighttable.list_print(combinations_list)
        # print()

        # print('Isrikiuotas listas')
        sorted_flight_price_list = self.get_sorted_flight_price_list(depth, combinations_list)
        # flighttable.list_print(sorted_flight_price_list)
        # print()

        # print('Isfiltruoti is x i w miesta')
        required_cities_list = self.get_required_cities_list(from_city, to_city, sorted_flight_price_list)
        # flighttable.list_print(required_cities_list)
        # print()

        return required_cities_list


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


    def get_filtered(self, depth, flight_list, from_city, to_city):
        #Get all available flight values by depth
        result = []

        for depth_num in range(1, depth+1):
            rez = self.get_cities_result_list(depth_num, flight_list, from_city, to_city)
            # print(rez)

            for flight in rez:
                result.append(flight)

        return result

class Functions:

    def list_print(self, input_list):
    #Print list values
        for flight in input_list:
            print(flight)

def main():
    depth = 2
    from_city = 'City X'
    to_city = 'City W'

    flighttable = FlightTable(available_flights)
    functions = Functions()

    print('1st task:')
    print(flighttable.get_ids_to_city('City X'))
    print()

    print('2nd task:')
    print(flighttable.get_availables_to_cities('City X'))
    print()

    print('3th task')
    # print(flighttable.get_cheapest_roundtrip())
    print('*Available flights from list*')
    flight_list = flighttable.get_flight_list()
    functions.list_print(flight_list)
    print()

    print('*Available flights from City X to City W*')
    result = flighttable.get_filtered(depth, flight_list, from_city, to_city)
    functions.list_print(result)
    print()

    print('*Cheapest destination flight*')
    lowest_price_flight = flighttable.get_lowest_price_flight(result)
    print(lowest_price_flight)

if __name__ == "__main__":
    os.system('cls')
    main()