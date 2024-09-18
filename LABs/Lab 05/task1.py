class Vehicle() :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.fare = self.capacity * 100
    def calculate(self) :
        pass

class Bus(Vehicle) :
    def __init__(self,capacity) :
        super().__init__(capacity)
    def calculate(self) :
        self.fare = 1.10 * self.fare


bus = Bus(100)
bus.calculate()
print(f"Bus has Seating capacity of {bus.capacity} and fare is {bus.fare}")