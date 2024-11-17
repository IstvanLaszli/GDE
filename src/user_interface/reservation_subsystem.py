from src.abstract_classes.i_system import ISystem


class Reservation:

    def __init__(
            self,
            reservation_number: str,
            flight_company: str,
            flight_nbr: str,
            destination_airport: str,
            ticket_price: int):
        self.reservation_number: str = reservation_number
        self.flight_company: str = flight_company
        self.flight_nbr: str = flight_nbr
        self.destination_airport: str = destination_airport
        self.ticket_price: int = ticket_price

    def __str__(self):
        return (
            f'{self.reservation_number} '
            f'{self.flight_company} '
            f'{self.flight_nbr} '
            f'{self.destination_airport} '
            f'{self.ticket_price} '
        )


class ReservationSystem(ISystem):

    def __init__(self, flight_system):
        self.flight_system = flight_system
        self.reservations = []
        self.setup_reservations()

    def setup_reservations(self):
        init_data = self.read_data("../data/reservations_data.json")
        for data in init_data["data"]:
            self.reserve(
                flight_company=data["flight_company"],
                flight_nbr=data["flight_nbr"]
            )

    def reserve(self, flight_company: str = None, flight_nbr = None):
        if not (flight_company and flight_nbr):
            flight_company: str = str(input('Add flight company name:'))
            flight_nbr: str = str(input('Add flight number:'))
        flight = self.flight_system.validate_free_seats(flight_company, flight_nbr)
        flight.current_occupation += 1
        self.reservations.append(
            Reservation(
                reservation_number=f'{flight.flight_nbr}_{str(flight.current_occupation)}',
                flight_company=flight_company,
                flight_nbr=flight.flight_nbr,
                destination_airport=flight.destination_airport,
                ticket_price=flight.ticket_price
            )
        )
        return flight.ticket_price

    def delete_reservation(self):
        reservation_number: str = str(input('Add reservation number:'))
        for idx, reservation in enumerate(self.reservations):
            if reservation.reservation_number == reservation_number:
                flight = self.flight_system.find_flight(
                    reservation.flight_company,
                    reservation.flight_nbr
                )
                flight.current_occupation -= 1
                print(f"The following reservation was removed: \n {self.reservations.pop(idx)}")
                return
        raise ValueError(f"The given reservation was not found: {reservation_number}")

    def list_reservations(self):
        print('*' * 20, ' RESERVATION REPORT ', '*' * 20)
        print('RES_NUM  FGHT_CMPY  FGHT_NUM  DEST_APT  PRICE')
        for reservation in self.reservations:
            print(reservation)
        print('-' * 50)
