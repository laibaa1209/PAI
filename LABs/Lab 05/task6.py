class Employee:
    def __init__(self, name, salary):
        self.name  = name
        self.salary = salary

    def calculate_bonus(self):
        pass
        
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20 
    
    def hire(self):
        print(f"{self.name} is hiring!")

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10 

    def write_code(self):
        print(f"{self.name} developer is writing the code!")

class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30
    
def main():

    # Example usage
    manager = Manager("Laiba", 670000)
    developer = Developer("Bilal", 569800)
    senior_manager = SeniorManager("Aira", 345000)

    print(f"{manager.name}'s bonus: {manager.calculate_bonus()}")
    manager.hire()

    print(f"{developer.name}'s bonus: {developer.calculate_bonus()}")
    developer.write_code()

    print(f"{senior_manager.name}'s bonus: {senior_manager.calculate_bonus()}")

main()