from src.abstract_classes.i_flight import IFlight

class DomesticFlight(IFlight):

    def __init__(
            self,
            flight_nbr: str,
            destination_airport: str,
            max_seat_nbr: int,
            ticket_price: int,
            current_occupation: int):
        super().__init__(
            flight_nbr,
            destination_airport,
            max_seat_nbr,
            ticket_price,
            current_occupation
        )
