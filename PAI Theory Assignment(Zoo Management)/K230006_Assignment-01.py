#----------------------------------------------------ZOO MANAGEMENT SYSTEM----------------------------------------------------

class Animal:
    def __init__(self, name, age, habitat):
        # Initialize common attributes for all animals
        self.name = name
        self.age = age
        self.habitat = habitat
        self.is_available = True  # Initially set the animal as available for viewing

    def mark_availability(self, is_available):
        # Update the availability status of the animal
        self.is_available = is_available

    def is_available_method(self):
        # Print the availability status of the animal
        print(f"The {self.name} is available for viewing") if self.is_available else print(f"The {self.name} is quarantined.")

    def display_info(self):
        # Display common information about the animal
        print(f"Name: {self.name}\nAge: {self.age} years\nHabitat: {self.habitat}")
        self.is_available_method()
        
class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type):
        # Initialize attributes specific to mammals
        super().__init__(name, age, habitat)  # Call the constructor of the base class
        self.fur_length = fur_length
        self.diet_type = diet_type

    def display(self):
        # Display information about the mammal, including common and specific attributes
        super().display_info()  # Call the display_info method from the base class
        print(f"Fur length: {self.fur_length} cm\nDiet Type: {self.diet_type}")

class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude):
        # Initialize attributes specific to birds
        super().__init__(name, age, habitat)  # Call the constructor of the base class
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude

    def display(self):
        # Display information about the bird, including common and specific attributes
        super().display_info()  # Call the display_info method from the base class
        print(f"Wingspan: {self.wingspan} ft\nFlight Altitude: {self.flight_altitude} ft")

class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous_status):
        # Initialize attributes specific to reptiles
        super().__init__(name, age, habitat)  # Call the constructor of the base class
        self.scale_pattern = scale_pattern
        self.venomous_status = venomous_status

    def display(self):
        # Display information about the reptile, including common and specific attributes
        super().display_info()  # Call the display_info method from the base class
        print(f"Scale Pattern: {self.scale_pattern}\nVenomous Status: {self.venomous_status}")

def main():
    # Create instances of each animal type
    mammal1 = Mammal("Elephant", 30, "Grass Lands", 23, "Herbivore")
    mammal2 = Mammal("Tiger", 10, "Forest", 3, "Carnivore")
    
    bird1 = Bird("Eagle", 15, "Mountain", "10-20", "15,000-20,000")
    bird2 = Bird("Parrot", 40, "Tropical Forests", "3-4", "30-100")

    reptile1 = Reptile("Crocodile", 70, "Freshwater Rivers", "protective scales", "not venomous")
    reptile2 = Reptile("Snake", 12, "Desert", "stripes", "venomous")

    print("\n----------------------------------------------------ZOO MANAGEMENT SYSTEM----------------------------------------------------\n")

    # Display details of mammals
    print("Details for mammals:\n")
    print("Mammal 1:\n")
    mammal1.display()
    print("\nMammal 2:\n")
    mammal2.display()

    # Display details of birds
    print("\nDetails for Birds:\n")
    print("Bird 1:\n")
    bird1.display()
    print("\nBird 2:\n")
    bird2.display()

    # Display details of reptiles
    print("\nDetails for reptiles:\n")
    print("Reptile 1:\n")
    reptile1.display()
    print("\nReptile 2:\n")
    reptile2.display()

    # Changing availability of three animals
    mammal1.mark_availability(False)
    bird2.mark_availability(False)
    reptile1.mark_availability(False)

    # Display availability status after changes
    print("\nAfter changing availability status:\n")
    mammal1.is_available_method()
    mammal2.is_available_method()

    bird1.is_available_method()
    bird2.is_available_method()

    reptile1.is_available_method()
    reptile2.is_available_method()

if __name__ == "__main__":
    main()
