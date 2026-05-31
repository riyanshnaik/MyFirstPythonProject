"""
A simple flight booking system for domestic flights within the USA.
"""

import datetime

class Flight:
    def __init__(self, flight_no, origin, destination, departure_time, seats):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.seats = seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            return True
        else:
            return False

    def __str__(self):
        return f"Flight {self.flight_no}: {self.origin} -> {self.destination} at {self.departure_time} | Seats left: {self.seats - self.booked_seats}"

class BookingSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def show_flights(self):
        for idx, flight in enumerate(self.flights, 1):
            print(f"{idx}. {flight}")

    def book_flight(self, flight_idx, passenger_name):
        if 0 <= flight_idx < len(self.flights):
            flight = self.flights[flight_idx]
            if flight.book_seat():
                booking = {
                    'passenger': passenger_name,
                    'flight_no': flight.flight_no,
                    'origin': flight.origin,
                    'destination': flight.destination,
                    'departure_time': flight.departure_time
                }
                self.bookings.append(booking)
                print(f"Booking successful for {passenger_name} on flight {flight.flight_no}.")
            else:
                print("Sorry, no seats available on this flight.")
        else:
            print("Invalid flight selection.")

    def show_bookings(self):
        if not self.bookings:
            print("No bookings yet.")
        for booking in self.bookings:
            print(f"Passenger: {booking['passenger']}, Flight: {booking['flight_no']}, {booking['origin']} -> {booking['destination']} at {booking['departure_time']}")

def main():
    system = BookingSystem()
    # Sample flights
    system.add_flight(Flight("AA101", "New York", "Los Angeles", "2026-06-01 08:00", 5))
    system.add_flight(Flight("DL202", "Chicago", "Miami", "2026-06-01 09:30", 3))
    system.add_flight(Flight("UA303", "Dallas", "San Francisco", "2026-06-01 11:00", 4))

    while True:
        print("\n--- USA Domestic Flight Booking ---")
        print("1. Show available flights")
        print("2. Book a flight")
        print("3. Show my bookings")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            system.show_flights()
        elif choice == '2':
            system.show_flights()
            try:
                idx_input = input("Select flight number to book: ")
                idx = int(idx_input) - 1
                if 0 <= idx < len(system.flights):
                    name = input("Enter passenger name: ")
                    system.book_flight(idx, name)
                else:
                    print("Invalid flight selection.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            system.show_bookings()
        elif choice == '4':
            print("Thank you for using the flight booking system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
