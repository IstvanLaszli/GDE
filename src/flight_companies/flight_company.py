from typing import List


from src.abstract_classes.i_flight import IFlight
from src.abstract_classes.i_flight_company import IFlightCompany


class FlightCompany(IFlightCompany):

    def __init__(
            self,
            company_name: str,
            flights: List[IFlight] | None = None):
        super().__init__(
            company_name,
            flights
        )
