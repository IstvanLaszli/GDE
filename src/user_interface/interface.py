from src.user_interface.system_setup import FlightSystem
from src.user_interface.reservation import ReservationSystem


def list_actions():
    print('\n',
            "1. List Flight Companies\n",
            "2. List Flights\n",
            "3. Add Flight Company\n",
            "4. Add Flights to Company\n",
            "5. Reserve Ticket\n",
            "6. Delete Reservation\n",
            "7. List Reservations\n",
            "8. Close application\n"
    )


if __name__ == '__main__':
    print('*' * 20, ' FLIGHT RESERVATION SYSTEM ', '*' * 20)
    flight_system = FlightSystem()
    reservation_system = ReservationSystem(flight_system)

    action: int = 0
    while action != 8:
        list_actions()
        action: int = int(input('What action to do? '))

        if action == 1:
            flight_system.list_flight_companies()
        elif action == 2:
            flight_system.list_flights()
        elif action == 3:
            flight_system.add_flight_company()
        elif action == 4:
            flight_system.add_flights()
        elif action == 5:
            reservation_system.reserve()
        elif action == 6:
            reservation_system.delete_reservation()
        elif action == 7:
            reservation_system.list_reservations()
        elif action == 8:
            break
        else:
            raise ValueError("Action not recognized!")
