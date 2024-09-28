from abc import ABC, abstractmethod
from datetime import datetime


class Vehicle(ABC):
    def __init__(self, make, model, rental_price, is_available=True):
        self.make = make
        self.model = model
        self._rental_price = rental_price  
        self._is_available = is_available  

    @abstractmethod
    def check_availability(self):
        pass
    @abstractmethod
    def total_rental_cost(self, period):
        pass
    @abstractmethod
    def display_details(self):
        pass
    @abstractmethod
    def change_availability(self):
        pass


class Car(Vehicle):
    def check_availability(self):
        return self._is_available
    def total_rental_cost(self, period):
        return self._rental_price * period
    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nRental Price: {self._rental_price}\nAvailable: {self._is_available}")
    def change_availability(self, return_vehicle):
        self._is_available = return_vehicle

class SUV(Vehicle):
    def check_availability(self):
        return self._is_available
    def total_rental_cost(self, period):
        return self._rental_price * period
    def display_details(self):
        print(f"SUV Details:\nMake: {self.make}\nModel: {self.model}\nRental Price: {self._rental_price}\nAvailable: {self._is_available}")
    def change_availability(self, return_vehicle):
        self._is_available = return_vehicle

class Truck(Vehicle):
    def check_availability(self):
        return self._is_available
    def total_rental_cost(self, period):
        return self._rental_price * period
    def display_details(self):
        print(f"Truck Details:\nMake: {self.make}\nModel: {self.model}\nRental Price: {self._rental_price}\nAvailable: {self._is_available}")
    def change_availability(self, return_vehicle):
        self._is_available = return_vehicle

class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def reservation_details(self):
        print(f"Reservation Details:\nCustomer: {self.customer.name}\nVehicle: {self.vehicle.make} {self.vehicle.model}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}")

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info 
        self.rental_history = []

    def add_rental(self, rental_reservation):
        self.rental_history.append(rental_reservation)
    def display_rental_history(self):
        print(f"Rental History for {self.name}:")
        for rental in self.rental_history:
            rental.reservation_details()

def main():
    car = Car("Toyota", "Corolla", 50)
    suv = SUV("Ford", "Explorer", 70)
    truck = Truck("Chevrolet", "Silverado", 100)

    customer1 = Customer("Laiba", "laiba@example.com")
    customer2 = Customer("Bilal", "bilal@example.com")

    rental1 = RentalReservation(customer1, car, datetime(2024, 9, 28), datetime(2024, 10, 5))
    rental2 = RentalReservation(customer2, suv, datetime(2024, 9, 30), datetime(2024, 10, 6))

    customer1.add_rental(rental1)
    customer2.add_rental(rental2)

    car.display_details()
    suv.display_details()
    truck.display_details()

    customer1.display_rental_history()
    customer2.display_rental_history()

main()