from abc import ABC
from typing import List
from src.abstract_classes.i_flight import IFlight


class IFlightCompany(ABC):

    def __init__(
            self,
            company_name: str,
            flights: List[IFlight]):
        self.company_name: str = company_name
        self.flights: List[IFlight] | None  = flights

    def __str__(self):
        return self.company_name
