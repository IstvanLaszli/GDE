from abc import ABC


class IFlight(ABC):

    def __init__(
            self,
            flight_nbr: str,
            destination_airport: str,
            max_seat_nbr: int,
            ticket_price:int,
            current_occupation: int):
        self.flight_nbr: str = flight_nbr
        self.destination_airport: str = destination_airport
        self.max_seat_nbr: int = max_seat_nbr
        self.ticket_price: int = ticket_price
        self.current_occupation: int = current_occupation

    def __str__(self):
        return (
            f"{type(self).__name__} "
            f"{self.flight_nbr} \t"
            f"{self.destination_airport} "
            f"{self.max_seat_nbr} "
            f"{self.current_occupation} "
            f"{self.max_seat_nbr - self.current_occupation} "
            f"{self.ticket_price} "
        )
