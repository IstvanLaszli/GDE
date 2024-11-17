from src.abstract_classes.i_system import ISystem
from src.flights.domestic_flight import DomesticFlight
from src.flights.international_flight import InternationalFlight
from src.flight_companies.flight_company import FlightCompany
from src.errors.erros import (
    FlightCompanyNotExists,
    FlightCompanyAlreadyExists,
    FlightNotExists,
    FlightAlreadyExists
)


class FlightSystem(ISystem):

    def __init__(self):
        self.flight_system = []
        self.setup_flights()

    def setup_flights(self):
        init_data = self.read_data("./data/flights_data.json")
        for data in init_data["data"]:
            self.add_flight_company(data["company_name"])
            for flight in data["flights"]:
                self.add_flights(
                    company_name=data["company_name"],
                    flight_type=flight["flight_type"],
                    flight_nbr=flight["flight_nbr"],
                    destination_airport=flight["destination_airport"],
                    max_seat_nbr=flight["max_seat_nbr"],
                    ticket_price=flight["ticket_price"],
                    current_occupation=flight.get("current_occupation", 0)
                )

    def add_flight_company(self, company_name: str = None):
        if not company_name:
            company_name = str(input('Add company name:'))
        try:
            if self.find_company(company_name):
                raise FlightCompanyAlreadyExists('Flight company already exists!')
        except FlightCompanyNotExists:
            self.flight_system.append(FlightCompany(company_name, []))

    def add_flights(
            self,
            company_name: str = None,
            flight_type: str = None,
            flight_nbr: str = None,
            destination_airport: str = None,
            max_seat_nbr: int = None,
            ticket_price: int = None,
            current_occupation: int = 0):
        if not (
                company_name
                and flight_type
                and flight_nbr
                and destination_airport
                and max_seat_nbr
                and ticket_price
        ):
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
            "ticket_price": ticket_price,
            "current_occupation": current_occupation
        }
        try:
            if self.find_flight(company_name, flight_nbr):
                raise FlightAlreadyExists('Flight number already exists!')
        except FlightNotExists:
            company = self.find_company(company_name)
            company.flights.append(self._add_flight_to_company(payload))

    def find_company(self, flight_company):
        for company in self.flight_system:
            if company.company_name == flight_company:
                return company
        raise FlightCompanyNotExists("Flight company does not exist!")

    def find_flight(self, flight_company: str, flight_number: str):
        company = self.find_company(flight_company)
        for flight in company.flights:
            if flight.flight_nbr == flight_number:
                return flight
        raise FlightNotExists("Flight does not exist!")

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

    @staticmethod
    def _add_flight_to_company(flight):
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
            current_occupation=flight["current_occupation"]
        )
