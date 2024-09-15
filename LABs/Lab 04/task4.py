# Make a class "Employee". Create "get_data" function inside this class that will take input
# from user employee name ,monthly salary and percentage of tax. Create another function
# "Salary_after_tax" that will deduct 2% tax on monthly salary and return remaining salary.
# There will be another function of "update_tax_percentage" inside this class that will change
# tax percentage (for example initially if it was taken 2% then you may update it to 3%).
# Now again salary will be calculated based on this new tax percentage.

class Employee:
    def __init__(self):
        self.name = ""
        self.monthly_salary = 0.0
        self.percentage_of_tax = 0.0

    def get_data(self):
        self.name = input("Enter The name of employee: ")
        self.monthly_salary = float(input("Enter the Monthly salary: "))
        self.percentage_of_tax = float(input("Enter the Tax percenatge: "))
    
    def dedcut_salary(self):
        return self.monthly_salary - (self.monthly_salary * self.percentage_of_tax / 100)
    
    def update_tax_percenatge(self, new_tax_rate):
        self.percentage_of_tax = new_tax_rate

def main():
    e = Employee()
    e.get_data()
    
    print("Salary before change of tax.")
    print(e.dedcut_salary())

    e.update_tax_percenatge(3)

    print("Salary after change of tax.")
    print(e.dedcut_salary())

main()
        