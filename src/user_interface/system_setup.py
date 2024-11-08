import json

from src.flights.domestic_flight import DomesticFlight
from src.flights.international_flight import InternationalFlight
from src.flight_companies.flight_company import FlightCompany


class FlightSystem:

    def __init__(self):
        self.flight_system = self.setup_flights()

    def setup_flights(self):
        init_data = self._read_data()
        companies = [
            FlightCompany(
                company_name=data["company_name"],
                flights=[
                    self._setup_flight(flight)
                    for flight in data["flights"]
                ]
            )
            for data in init_data["data"]
        ]
        return companies

    def add_flight_company(self):
        company_name = str(input('Add company name:'))
        try:
            if self.find_company(company_name):
                raise ValueError('Flight company already exists!')
        except ValueError:
            self.flight_system.append(FlightCompany(company_name, []))


    def add_flights(self):
        company_name = str(input('Add company name:'))
        flight_type = str(input('Add flight type (domestic / international):')).lower()
        flight_nbr: str = str(input('Add flight number:'))
        destination_airport: str = str(input('Add destination airport:'))
        max_seat_nbr: int = int(input('Add max seat number:'))
        ticket_price: int = int(input('Add ticket price:'))
        payload = {
            "flight_type": flight_type,
            "flight_nbr": flight_nbr,
            "destination_airport": destination_airport,
            "max_seat_nbr": max_seat_nbr,
            "ticket_price": ticket_price
        }
        try:
            if self.find_flight(company_name, flight_nbr):
                raise ValueError('Flight number already exists!')
        except ValueError:
            company = self.find_company(company_name)
            company.flights.append(self._setup_flight(payload))

    def find_company(self, flight_company):
        for company in self.flight_system:
            if company.company_name == flight_company:
                return company
        raise ValueError("Flight company does not exist!")

    def find_flight(self, flight_company: str, flight_number: str):
        company = self.find_company(flight_company)
        for flight in company.flights:
            if flight.flight_nbr == flight_number:
                return flight
        raise ValueError("Flight does not exist!")

    def validate_free_seats(self, flight_company: str, flight_nbr: str):
        flight = self.find_flight(flight_company, flight_nbr)
        if flight.current_occupation < flight.max_seat_nbr:
            return flight
        else:
            raise ValueError("Max seat number reached!")

    def list_flight_companies(self):
        print('*' * 20, ' FLIGHT COMPANY REPORT ', '*' * 20)
        for company in self.flight_system:
            print(company)
        print('-' * 50)

    def list_flights(self):
        print('*' * 20, ' FLIGHTS REPORT ', '*' * 20)
        for company in self.flight_system:
            print('COMPANY:', company)
            for flight in company.flights:
                print(flight)
        print('-' * 50)

    def _read_data(self):
        with open("../data/flights_data.json", 'r') as f:
            return json.load(f)

    def _setup_flight(self, flight):
        if flight["flight_type"] == "domestic":
            flight_type = DomesticFlight
        elif flight["flight_type"] == "international":
            flight_type = InternationalFlight
        else:
            raise ValueError("Flight type is not valid")
        return flight_type(
            flight_nbr=flight["flight_nbr"],
            destination_airport=flight["destination_airport"],
            max_seat_nbr=flight["max_seat_nbr"],
            ticket_price=flight["ticket_price"],
            current_occupation=flight.get("current_occupation", 0)
        )
